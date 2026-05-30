# Generated from RaraLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
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


    # Enter a parse tree produced by RaraLangParser#item.
    def enterItem(self, ctx:RaraLangParser.ItemContext):
        pass

    # Exit a parse tree produced by RaraLangParser#item.
    def exitItem(self, ctx:RaraLangParser.ItemContext):
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


    # Enter a parse tree produced by RaraLangParser#IfStat.
    def enterIfStat(self, ctx:RaraLangParser.IfStatContext):
        pass

    # Exit a parse tree produced by RaraLangParser#IfStat.
    def exitIfStat(self, ctx:RaraLangParser.IfStatContext):
        pass


    # Enter a parse tree produced by RaraLangParser#WhileStat.
    def enterWhileStat(self, ctx:RaraLangParser.WhileStatContext):
        pass

    # Exit a parse tree produced by RaraLangParser#WhileStat.
    def exitWhileStat(self, ctx:RaraLangParser.WhileStatContext):
        pass


    # Enter a parse tree produced by RaraLangParser#ReturnStat.
    def enterReturnStat(self, ctx:RaraLangParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by RaraLangParser#ReturnStat.
    def exitReturnStat(self, ctx:RaraLangParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by RaraLangParser#funcDef.
    def enterFuncDef(self, ctx:RaraLangParser.FuncDefContext):
        pass

    # Exit a parse tree produced by RaraLangParser#funcDef.
    def exitFuncDef(self, ctx:RaraLangParser.FuncDefContext):
        pass


    # Enter a parse tree produced by RaraLangParser#block.
    def enterBlock(self, ctx:RaraLangParser.BlockContext):
        pass

    # Exit a parse tree produced by RaraLangParser#block.
    def exitBlock(self, ctx:RaraLangParser.BlockContext):
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


    # Enter a parse tree produced by RaraLangParser#CompareExpr.
    def enterCompareExpr(self, ctx:RaraLangParser.CompareExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#CompareExpr.
    def exitCompareExpr(self, ctx:RaraLangParser.CompareExprContext):
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


    # Enter a parse tree produced by RaraLangParser#NegExpr.
    def enterNegExpr(self, ctx:RaraLangParser.NegExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#NegExpr.
    def exitNegExpr(self, ctx:RaraLangParser.NegExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#CallExpr.
    def enterCallExpr(self, ctx:RaraLangParser.CallExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#CallExpr.
    def exitCallExpr(self, ctx:RaraLangParser.CallExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#AvgExpr.
    def enterAvgExpr(self, ctx:RaraLangParser.AvgExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#AvgExpr.
    def exitAvgExpr(self, ctx:RaraLangParser.AvgExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#ModExpr.
    def enterModExpr(self, ctx:RaraLangParser.ModExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#ModExpr.
    def exitModExpr(self, ctx:RaraLangParser.ModExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#ParenExpr.
    def enterParenExpr(self, ctx:RaraLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#ParenExpr.
    def exitParenExpr(self, ctx:RaraLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by RaraLangParser#DoublePlusExpr.
    def enterDoublePlusExpr(self, ctx:RaraLangParser.DoublePlusExprContext):
        pass

    # Exit a parse tree produced by RaraLangParser#DoublePlusExpr.
    def exitDoublePlusExpr(self, ctx:RaraLangParser.DoublePlusExprContext):
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