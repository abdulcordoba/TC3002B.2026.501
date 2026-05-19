import ast
import math

from antlr.RaraLangListener import RaraLangListener
from antlr.RaraLangParser import RaraLangParser


class MIPSListener(RaraLangListener):
    def __init__(self):
        self.data = []
        self.text = [
            ".text",
            ".globl main",
            "main:",
        ]
        self.string_count = 0
        self.variables = {}
        self.expr_stack = []
        self.value_stack = []
        self.free_registers = [f"$t{i}" for i in range(10)]

    def output(self):
        lines = []

        if self.data:
            lines.append(".data")
            lines.extend(self.data)

        lines.extend(self.text)
        lines.extend([
            "    li $v0, 10",
            "    syscall",
        ])

        return "\n".join(lines) + "\n"

    def _emit_print(self, literal):
        if literal.startswith('"') and literal.endswith('"'):
            self._emit_print_string(literal)
        else:
            reg = self._load_int_literal(literal)
            self._emit_print_int(reg)
            self._free_register(reg)

    def _parse_int_literal(self, literal):
        if literal.startswith("[") and literal.endswith("]"):
            digits, base = literal[1:-1].split(":", 1)
            return int(digits, int(base))

        return int(literal)

    def _load_int_literal(self, literal):
        reg = self._alloc_register()
        self.text.append(f"    li {reg}, {self._parse_int_literal(literal)}")
        return reg

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

    def _decode_string(self, literal):
        value = ast.literal_eval(literal)
        return (
            value
            .replace("\\", "\\\\")
            .replace("\n", "\\n")
            .replace("\t", "\\t")
            .replace('"', '\\"')
        )

    def exitLiteralExpr(self, ctx):
        literal = ctx.literal().getText()
        value = self._parse_int_literal(literal)
        self.expr_stack.append(self._load_int_literal(literal))
        self.value_stack.append(value)

    def exitVarExpr(self, ctx):
        name = ctx.ID().getText()
        label = self._ensure_variable(name)
        reg = self._alloc_register()
        self.text.append(f"    lw {reg}, {label}")
        self.expr_stack.append(reg)
        self.value_stack.append(None)

    def exitAddSubExpr(self, ctx):
        right = self.expr_stack.pop()
        left = self.expr_stack.pop()
        right_value = self.value_stack.pop()
        left_value = self.value_stack.pop()
        op = ctx.getChild(1).getText()

        if op == "+":
            self.text.append(f"    add {left}, {left}, {right}")
            value = None if left_value is None or right_value is None else left_value + right_value
        else:
            self.text.append(f"    sub {left}, {left}, {right}")
            value = None if left_value is None or right_value is None else left_value - right_value

        self._free_register(right)
        self.expr_stack.append(left)
        self.value_stack.append(value)

    def exitMulDivExpr(self, ctx):
        right = self.expr_stack.pop()
        left = self.expr_stack.pop()
        right_value = self.value_stack.pop()
        left_value = self.value_stack.pop()
        op = ctx.getChild(1).getText()

        if op == "×":
            self.text.extend([
                f"    mult {left}, {right}",
                f"    mflo {left}",
            ])
            value = None if left_value is None or right_value is None else left_value * right_value
        else:
            if right_value == 0:
                raise ValueError("Division entre cero en una expresion constante")

            self.text.extend([
                f"    div {left}, {right}",
                f"    mflo {left}",
            ])
            value = None if left_value is None or right_value is None else left_value // right_value

        self._free_register(right)
        self.expr_stack.append(left)
        self.value_stack.append(value)

    def exitAssignStat(self, ctx):
        name = ctx.ID().getText()
        label = self._ensure_variable(name)
        reg = self.expr_stack.pop()
        self.value_stack.pop()
        self.text.append(f"    sw {reg}, {label}")
        self._free_register(reg)

    def exitPrintStat(self, ctx):
        print_arg = ctx.printArg()
        if isinstance(print_arg, RaraLangParser.StringPrintArgContext):
            self._emit_print_string(print_arg.STRING().getText())
            return

        reg = self.expr_stack.pop()
        self.value_stack.pop()
        self._emit_print_int(reg)
        self._free_register(reg)

    def _ensure_variable(self, name):
        if name not in self.variables:
            label = f"var_{name}"
            self.variables[name] = label
            self.data.append(f"{label}: .word 0")

        return self.variables[name]

    def _alloc_register(self):
        if not self.free_registers:
            raise RuntimeError("No hay registros temporales disponibles")

        return self.free_registers.pop(0)

    def exitNegExpr(self, ctx):
        reg = self.expr_stack[-1]
        self.text.append(f"    neg {reg}, {reg}")
        v = self.value_stack[-1]
        self.value_stack[-1] = None if v is None else -v

    def exitModExpr(self, ctx):
        right = self.expr_stack.pop()
        left = self.expr_stack.pop()
        rv = self.value_stack.pop()
        lv = self.value_stack.pop()
        self.text.extend([
            f"    div {left}, {right}",
            f"    mfhi {left}",
        ])
        self._free_register(right)
        self.expr_stack.append(left)
        self.value_stack.append(None if lv is None or rv is None else lv % rv)

    def exitDoublePlusExpr(self, ctx):
        right = self.expr_stack.pop()
        left = self.expr_stack.pop()
        rv = self.value_stack.pop()
        lv = self.value_stack.pop()
        self.text.extend([
            f"    sll {left}, {left}, 1",
            f"    add {left}, {left}, {right}",
        ])
        self._free_register(right)
        self.expr_stack.append(left)
        self.value_stack.append(None if lv is None or rv is None else 2 * lv + rv)

    def exitAvgExpr(self, ctx):
        right = self.expr_stack.pop()
        left = self.expr_stack.pop()
        rv = self.value_stack.pop()
        lv = self.value_stack.pop()
        self.text.extend([
            f"    add {left}, {left}, {right}",
            f"    sra {left}, {left}, 1",
        ])
        self._free_register(right)
        self.expr_stack.append(left)
        self.value_stack.append(None if lv is None or rv is None else math.floor((lv + rv) / 2))

    def _free_register(self, reg):
        if reg not in self.free_registers:
            self.free_registers.insert(0, reg)
