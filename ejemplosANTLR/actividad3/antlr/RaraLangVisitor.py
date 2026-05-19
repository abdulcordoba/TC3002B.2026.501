# Generated from RaraLang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RaraLangParser import RaraLangParser
else:
    from RaraLangParser import RaraLangParser

# This class defines a complete generic visitor for a parse tree produced by RaraLangParser.

class RaraLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RaraLangParser#prog.
    def visitProg(self, ctx:RaraLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#AssignStat.
    def visitAssignStat(self, ctx:RaraLangParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#PrintStat.
    def visitPrintStat(self, ctx:RaraLangParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#StringPrintArg.
    def visitStringPrintArg(self, ctx:RaraLangParser.StringPrintArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#ExprPrintArg.
    def visitExprPrintArg(self, ctx:RaraLangParser.ExprPrintArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:RaraLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:RaraLangParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#VarExpr.
    def visitVarExpr(self, ctx:RaraLangParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#ParenExpr.
    def visitParenExpr(self, ctx:RaraLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:RaraLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#literal.
    def visitLiteral(self, ctx:RaraLangParser.LiteralContext):
        return self.visitChildren(ctx)



del RaraLangParser