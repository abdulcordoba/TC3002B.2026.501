import ast
import math

from antlr.RaraLangParser import RaraLangParser
from antlr.RaraLangVisitor import RaraLangVisitor


class CompileError(Exception):
    pass


class MIPSGenerator(RaraLangVisitor):
    def __init__(self):
        self.data = []
        self.main_text = []
        self.function_text = []
        self.text = self.main_text
        self.string_count = 0
        self.label_count = 0
        self.variables = {}
        self.assigned_variables = set()
        self.functions = {}
        self.current_function = None
        self.function_return_labels = []
        self.function_has_return = []
        self.free_registers = [f"$t{i}" for i in range(10)]

    def output(self):
        lines = []
        if self.data:
            lines.append(".data")
            lines.extend(self.data)

        lines.extend([
            ".text",
            ".globl main",
            "main:",
        ])
        lines.extend(self.main_text)
        lines.extend([
            "    li $v0, 10",
            "    syscall",
        ])
        lines.extend(self.function_text)
        return "\n".join(lines) + "\n"

    def visitProg(self, ctx):
        for item in ctx.item():
            func = item.funcDef()
            if func is None:
                continue

            name = func.ID().getText()
            if name == "main":
                raise CompileError("No se puede definir una funcion llamada main")
            if name in self.functions:
                raise CompileError(f"Funcion duplicada: {name}")
            self.functions[name] = func

        for item in ctx.item():
            if item.stat() is not None:
                self.visit(item.stat())

        saved_text = self.text
        self.text = self.function_text
        for name, func in self.functions.items():
            self._compile_function(name, func)
        self.text = saved_text

    def visitAssignStat(self, ctx):
        name = ctx.ID().getText()
        reg, _ = self.visit(ctx.expr())
        self.text.append(f"    sw {reg}, {self._ensure_variable(name, declare=True)}")
        self._free_register(reg)

    def visitPrintStat(self, ctx):
        print_arg = ctx.printArg()
        if isinstance(print_arg, RaraLangParser.StringPrintArgContext):
            self._emit_print_string(print_arg.STRING().getText())
            return

        reg, _ = self.visit(print_arg.expr())
        self._emit_print_int(reg)
        self._free_register(reg)

    def visitIfStat(self, ctx):
        else_label = self._new_label("else")
        end_label = self._new_label("endif")
        condition, _ = self.visit(ctx.expr())
        self.text.append(f"    beq {condition}, $zero, {else_label}")
        self._free_register(condition)

        self.visit(ctx.block(0))
        self.text.append(f"    j {end_label}")
        self.text.append(f"{else_label}:")
        if len(ctx.block()) > 1:
            self.visit(ctx.block(1))
        self.text.append(f"{end_label}:")

    def visitWhileStat(self, ctx):
        start_label = self._new_label("while")
        end_label = self._new_label("endwhile")
        self.text.append(f"{start_label}:")
        condition, _ = self.visit(ctx.expr())
        self.text.append(f"    beq {condition}, $zero, {end_label}")
        self._free_register(condition)
        self.visit(ctx.block())
        self.text.append(f"    j {start_label}")
        self.text.append(f"{end_label}:")

    def visitReturnStat(self, ctx):
        if self.current_function is None:
            raise CompileError("return solo puede usarse dentro de una funcion")

        reg, _ = self.visit(ctx.expr())
        self.text.append(f"    move $v0, {reg}")
        self._free_register(reg)
        self.function_has_return[-1] = True
        self.text.append(f"    j {self.function_return_labels[-1]}")

    def visitBlock(self, ctx):
        for stat in ctx.stat():
            self.visit(stat)

    def visitLiteralExpr(self, ctx):
        literal = ctx.literal().getText()
        value = self._parse_int_literal(literal)
        reg = self._alloc_register()
        self.text.append(f"    li {reg}, {value}")
        return reg, value

    def visitVarExpr(self, ctx):
        name = ctx.ID().getText()
        reg = self._alloc_register()
        self.text.append(f"    lw {reg}, {self._ensure_variable(name)}")
        return reg, None

    def visitCallExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.functions:
            raise CompileError(f"Funcion no definida: {name}")

        live_registers = self._live_registers()
        for reg in live_registers:
            self.text.extend([
                "    addiu $sp, $sp, -4",
                f"    sw {reg}, 0($sp)",
            ])

        self.text.extend([
            "    addiu $sp, $sp, -4",
            "    sw $ra, 0($sp)",
            f"    jal func_{name}",
            "    lw $ra, 0($sp)",
            "    addiu $sp, $sp, 4",
        ])

        for reg in reversed(live_registers):
            self.text.extend([
                f"    lw {reg}, 0($sp)",
                "    addiu $sp, $sp, 4",
            ])

        reg = self._alloc_register()
        self.text.append(f"    move {reg}, $v0")
        return reg, None

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitNegExpr(self, ctx):
        reg, value = self.visit(ctx.expr())
        self.text.append(f"    neg {reg}, {reg}")
        return reg, None if value is None else -value

    def visitAddSubExpr(self, ctx):
        left, left_value = self.visit(ctx.expr(0))
        right, right_value = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == "+":
            self.text.append(f"    add {left}, {left}, {right}")
            value = None if left_value is None or right_value is None else left_value + right_value
        else:
            self.text.append(f"    sub {left}, {left}, {right}")
            value = None if left_value is None or right_value is None else left_value - right_value

        self._free_register(right)
        return left, value

    def visitMulDivExpr(self, ctx):
        left, left_value = self.visit(ctx.expr(0))
        right, right_value = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == "×":
            self.text.extend([
                f"    mult {left}, {right}",
                f"    mflo {left}",
            ])
            value = None if left_value is None or right_value is None else left_value * right_value
        else:
            if right_value == 0:
                raise CompileError("Division entre cero en una expresion constante")
            self._emit_division_guard(right, "division")
            self.text.extend([
                f"    div {left}, {right}",
                f"    mflo {left}",
            ])
            value = None if left_value is None or right_value is None else math.trunc(left_value / right_value)

        self._free_register(right)
        return left, value

    def visitModExpr(self, ctx):
        left, left_value = self.visit(ctx.expr(0))
        right, right_value = self.visit(ctx.expr(1))
        if right_value == 0:
            raise CompileError("Modulo entre cero en una expresion constante")
        self._emit_division_guard(right, "modulo")
        self.text.extend([
            f"    div {left}, {right}",
            f"    mfhi {left}",
        ])
        self._free_register(right)
        value = None if left_value is None or right_value is None else left_value % right_value
        return left, value

    def visitDoublePlusExpr(self, ctx):
        left, left_value = self.visit(ctx.expr(0))
        right, right_value = self.visit(ctx.expr(1))
        self.text.extend([
            f"    sll {left}, {left}, 1",
            f"    add {left}, {left}, {right}",
        ])
        self._free_register(right)
        value = None if left_value is None or right_value is None else 2 * left_value + right_value
        return left, value

    def visitAvgExpr(self, ctx):
        left, left_value = self.visit(ctx.expr(0))
        right, right_value = self.visit(ctx.expr(1))
        self.text.extend([
            f"    add {left}, {left}, {right}",
            f"    sra {left}, {left}, 1",
        ])
        self._free_register(right)
        value = None if left_value is None or right_value is None else math.floor((left_value + right_value) / 2)
        return left, value

    def visitCompareExpr(self, ctx):
        left, left_value = self.visit(ctx.expr(0))
        right, right_value = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == "<":
            self.text.append(f"    slt {left}, {left}, {right}")
        elif op == ">":
            self.text.append(f"    slt {left}, {right}, {left}")
        elif op == "<=":
            self.text.extend([
                f"    slt {left}, {right}, {left}",
                f"    xori {left}, {left}, 1",
            ])
        elif op == ">=":
            self.text.extend([
                f"    slt {left}, {left}, {right}",
                f"    xori {left}, {left}, 1",
            ])
        elif op == "==":
            self.text.extend([
                f"    sub {left}, {left}, {right}",
                f"    sltiu {left}, {left}, 1",
            ])
        elif op == "!=":
            self.text.extend([
                f"    sub {left}, {left}, {right}",
                f"    sltu {left}, $zero, {left}",
            ])

        self._free_register(right)
        if left_value is None or right_value is None:
            return left, None
        return left, 1 if self._eval_compare(left_value, right_value, op) else 0

    def _compile_function(self, name, ctx):
        saved_function = self.current_function
        self.current_function = name
        return_label = self._new_label(f"return_{name}")
        self.function_return_labels.append(return_label)
        self.function_has_return.append(False)

        self.text.append(f"func_{name}:")
        self.visit(ctx.block())
        if not self.function_has_return[-1]:
            raise CompileError(f"La funcion {name} no tiene return")
        self.text.extend([
            f"{return_label}:",
            "    jr $ra",
        ])

        self.function_return_labels.pop()
        self.function_has_return.pop()
        self.current_function = saved_function

    def _emit_print_int(self, reg):
        self.text.extend([
            f"    move $a0, {reg}",
            "    li $v0, 1",
            "    syscall",
        ])
        self._emit_newline()

    def _emit_print_string(self, literal):
        label = f"str_{self.string_count}"
        self.string_count += 1
        self.data.append(f'{label}: .asciiz "{self._decode_string(literal)}"')
        self.text.extend([
            f"    la $a0, {label}",
            "    li $v0, 4",
            "    syscall",
        ])
        self._emit_newline()

    def _emit_newline(self):
        self.text.extend([
            "    li $a0, 10",
            "    li $v0, 11",
            "    syscall",
        ])

    def _emit_division_guard(self, divisor_reg, operation):
        ok_label = self._new_label(f"{operation}_ok")
        message = self._add_string(f"ERROR: {operation} entre cero")
        self.text.extend([
            f"    bne {divisor_reg}, $zero, {ok_label}",
            f"    la $a0, {message}",
            "    li $v0, 4",
            "    syscall",
            "    li $v0, 10",
            "    syscall",
            f"{ok_label}:",
        ])

    def _parse_int_literal(self, literal):
        try:
            if literal.startswith("[") and literal.endswith("]"):
                digits, base_text = literal[1:-1].split(":", 1)
                base = int(base_text)
                if base not in (2, 8, 10, 16):
                    raise CompileError(f"Base no soportada: {base}")
                return int(digits, base)
            return int(literal)
        except ValueError as exc:
            raise CompileError(f"Literal entero invalido: {literal}") from exc

    def _decode_string(self, literal):
        value = ast.literal_eval(literal)
        return (
            value
            .replace("\\", "\\\\")
            .replace("\n", "\\n")
            .replace("\t", "\\t")
            .replace('"', '\\"')
        )

    def _add_string(self, value):
        label = f"str_{self.string_count}"
        self.string_count += 1
        escaped = (
            value
            .replace("\\", "\\\\")
            .replace("\n", "\\n")
            .replace("\t", "\\t")
            .replace('"', '\\"')
        )
        self.data.append(f'{label}: .asciiz "{escaped}"')
        return label

    def _ensure_variable(self, name, declare=False):
        if not declare and name not in self.assigned_variables:
            raise CompileError(f"Variable no asignada: {name}")
        if name not in self.variables:
            label = f"var_{name}"
            self.variables[name] = label
            self.data.append(f"{label}: .word 0")
        if declare:
            self.assigned_variables.add(name)
        return self.variables[name]

    def _new_label(self, prefix):
        label = f"{prefix}_{self.label_count}"
        self.label_count += 1
        return label

    def _alloc_register(self):
        if not self.free_registers:
            raise CompileError("No hay registros temporales disponibles")
        return self.free_registers.pop(0)

    def _free_register(self, reg):
        if reg not in self.free_registers:
            self.free_registers.insert(0, reg)

    def _live_registers(self):
        return [f"$t{i}" for i in range(10) if f"$t{i}" not in self.free_registers]

    def _eval_compare(self, left, right, op):
        if op == "<":
            return left < right
        if op == ">":
            return left > right
        if op == "<=":
            return left <= right
        if op == ">=":
            return left >= right
        if op == "==":
            return left == right
        if op == "!=":
            return left != right
        raise CompileError(f"Operador de comparacion desconocido: {op}")


class MIPSListener(MIPSGenerator):
    pass
