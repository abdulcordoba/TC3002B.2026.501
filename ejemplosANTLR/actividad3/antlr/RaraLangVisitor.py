# Generated from RaraLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RaraLangParser import RaraLangParser
else:
    from RaraLangParser import RaraLangParser

# This class defines a complete generic visitor for a parse tree produced by RaraLangParser.

class RaraLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RaraLangParser#prog.
    def visitProg(self, ctx:RaraLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#item.
    def visitItem(self, ctx:RaraLangParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#AssignStat.
    def visitAssignStat(self, ctx:RaraLangParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#PrintStat.
    def visitPrintStat(self, ctx:RaraLangParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#IfStat.
    def visitIfStat(self, ctx:RaraLangParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#WhileStat.
    def visitWhileStat(self, ctx:RaraLangParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#ReturnStat.
    def visitReturnStat(self, ctx:RaraLangParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#funcDef.
    def visitFuncDef(self, ctx:RaraLangParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#block.
    def visitBlock(self, ctx:RaraLangParser.BlockContext):
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


    # Visit a parse tree produced by RaraLangParser#CompareExpr.
    def visitCompareExpr(self, ctx:RaraLangParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:RaraLangParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#VarExpr.
    def visitVarExpr(self, ctx:RaraLangParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#NegExpr.
    def visitNegExpr(self, ctx:RaraLangParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#CallExpr.
    def visitCallExpr(self, ctx:RaraLangParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#AvgExpr.
    def visitAvgExpr(self, ctx:RaraLangParser.AvgExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#ModExpr.
    def visitModExpr(self, ctx:RaraLangParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#ParenExpr.
    def visitParenExpr(self, ctx:RaraLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#DoublePlusExpr.
    def visitDoublePlusExpr(self, ctx:RaraLangParser.DoublePlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:RaraLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaraLangParser#literal.
    def visitLiteral(self, ctx:RaraLangParser.LiteralContext):
        return self.visitChildren(ctx)



del RaraLangParser