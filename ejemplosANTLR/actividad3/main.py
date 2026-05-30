"""
Uso:
    python main.py tests/07_if_then.rara        # un archivo
"""

import sys
from pathlib import Path
from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener

from antlr.RaraLangLexer import RaraLangLexer
from antlr.RaraLangParser import RaraLangParser
from MIPSListener import CompileError, MIPSGenerator


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise CompileError(f"Error de sintaxis en linea {line}, columna {column}: {msg}")


def compile_file(path: str) -> str:
    stream = FileStream(path, encoding="utf-8")
    lexer = RaraLangLexer(stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())
    tokens = CommonTokenStream(lexer)
    parser = RaraLangParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.prog()
    generator = MIPSGenerator()
    generator.visit(tree)
    return generator.output()


def run(path: str) -> None:
    mips = compile_file(path)
    out = Path(path).with_suffix(".asm")
    out.write_text(mips, encoding="utf-8")
    print(mips)
    print(f"\n# → {out}", flush=True)


if __name__ == "__main__":
    args = sys.argv[1:]

    source = args[0] if args else "tests/01_iteracion_1/01_01_int_literal.rara"
    try:
        run(source)
    except CompileError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
