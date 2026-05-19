# Generated from RaraLang.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RaraLangParser import RaraLangParser
else:
    from RaraLangParser import RaraLangParser

# This class defines a complete listener for a parse tree produced by RaraLangParser.
class RaraLangListener(ParseTreeListener):

    # Enter a parse tree produced by RaraLangParser#prog.
    def enterProg(self, ctx:RaraLangParser.ProgContext):
        pass

    # Exit a parse tree produced by RaraLangParser#prog.
    def exitProg(self, ctx:RaraLangParser.ProgContext):
        pass


    # Enter a parse tree produced by RaraLangParser#AssignStat.
    def enterAssignStat(self, ctx:RaraLangParser.AssignStatContext):
        pass

    # Exit a parse tree produced by RaraLangParser#AssignStat.
    def exitAssignStat(self, ctx:RaraLangParser.AssignStatContext):
        pass


    # Enter a parse tree produced by RaraLangParser#PrintStat.
    def enterPrintStat(self, ctx:RaraLangParser.PrintStatContext):
        pass

    # Exit a parse tree produced by RaraLangParser#PrintStat.
    def exitPrintStat(self, ctx:RaraLangParser.PrintStatContext):
        pass


    # Enter a parse tree produced by RaraLangParser#StringPrintArg.
    def enterStringPrintArg(self, ctx:RaraLangParser.StringPrintArgContext):
        pass

    # Exit a parse tree produced by RaraLangParser#StringPrintArg.
    def exitStringPrintArg(self, ctx:RaraLangParser.StringPrintArgContext):
        pass


    # Enter a parse tree produced by RaraLangParser#ExprPrintArg.
    def enterExprPrintArg(self, ctx:RaraLangParser.ExprPrintArgContext):
        pass

    # Exit a parse tree produced by RaraLangParser#ExprPrintArg.
    def exitExprPrintArg(self, ctx:RaraLangParser.ExprPrintArgContext):
        pass


    # Enter a parse tree produced by RaraLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:RaraLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:RaraLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:RaraLangParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:RaraLangParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#VarExpr.
    def enterVarExpr(self, ctx:RaraLangParser.VarExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#VarExpr.
    def exitVarExpr(self, ctx:RaraLangParser.VarExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#ParenExpr.
    def enterParenExpr(self, ctx:RaraLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#ParenExpr.
    def exitParenExpr(self, ctx:RaraLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:RaraLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:RaraLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#literal.
    def enterLiteral(self, ctx:RaraLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by RaraLangParser#literal.
    def exitLiteral(self, ctx:RaraLangParser.LiteralContext):
        pass



del RaraLangParser