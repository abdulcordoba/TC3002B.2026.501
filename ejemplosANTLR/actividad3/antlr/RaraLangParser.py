# Generated from RaraLang.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        3,2,28,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,39,8,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,56,8,3,
        10,3,12,3,59,9,3,1,4,1,4,1,4,0,1,6,5,0,2,4,6,8,0,3,1,0,5,6,1,0,7,
        8,1,0,13,14,68,0,13,1,0,0,0,2,23,1,0,0,0,4,27,1,0,0,0,6,38,1,0,0,
        0,8,60,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,
        0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,
        1,1,0,0,0,18,19,5,16,0,0,19,20,5,3,0,0,20,24,3,6,3,0,21,22,5,4,0,
        0,22,24,3,4,2,0,23,18,1,0,0,0,23,21,1,0,0,0,24,3,1,0,0,0,25,28,5,
        15,0,0,26,28,3,6,3,0,27,25,1,0,0,0,27,26,1,0,0,0,28,5,1,0,0,0,29,
        30,6,3,-1,0,30,31,5,1,0,0,31,32,3,6,3,0,32,33,5,2,0,0,33,39,1,0,
        0,0,34,39,3,8,4,0,35,39,5,16,0,0,36,37,5,12,0,0,37,39,3,6,3,6,38,
        29,1,0,0,0,38,34,1,0,0,0,38,35,1,0,0,0,38,36,1,0,0,0,39,57,1,0,0,
        0,40,41,10,5,0,0,41,42,7,0,0,0,42,56,3,6,3,6,43,44,10,4,0,0,44,45,
        5,10,0,0,45,56,3,6,3,5,46,47,10,3,0,0,47,48,5,9,0,0,48,56,3,6,3,
        4,49,50,10,2,0,0,50,51,5,11,0,0,51,56,3,6,3,3,52,53,10,1,0,0,53,
        54,7,1,0,0,54,56,3,6,3,2,55,40,1,0,0,0,55,43,1,0,0,0,55,46,1,0,0,
        0,55,49,1,0,0,0,55,52,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,
        1,0,0,0,58,7,1,0,0,0,59,57,1,0,0,0,60,61,7,2,0,0,61,9,1,0,0,0,6,
        13,23,27,38,55,57
    ]

class RaraLangParser ( Parser ):

    grammarFileName = "RaraLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'<--'", "'print'", "'\\u00D7'", 
                     "'\\u00F7'", "'+'", "'-'", "'\\u229E'", "'\\u22A0'", 
                     "'\\u2248'", "'\\u00B1'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ASSIGN", "PRINT", 
                      "MUL", "DIV", "PLUS", "MINUS", "MOD", "DOUBLE_PLUS", 
                      "AVG", "NEG", "INT", "BASED_INT", "STRING", "ID", 
                      "WS", "LINE_COMMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_printArg = 2
    RULE_expr = 3
    RULE_literal = 4

    ruleNames =  [ "prog", "stat", "printArg", "expr", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ASSIGN=3
    PRINT=4
    MUL=5
    DIV=6
    PLUS=7
    MINUS=8
    MOD=9
    DOUBLE_PLUS=10
    AVG=11
    NEG=12
    INT=13
    BASED_INT=14
    STRING=15
    ID=16
    WS=17
    LINE_COMMENT=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RaraLangParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.StatContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.StatContext,i)


        def getRuleIndex(self):
            return RaraLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RaraLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==16:
                self.state = 10
                self.stat()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(RaraLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RaraLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RaraLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(RaraLangParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStat" ):
                listener.enterAssignStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStat" ):
                listener.exitAssignStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStat" ):
                return visitor.visitAssignStat(self)
            else:
                return visitor.visitChildren(self)


    class PrintStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(RaraLangParser.PRINT, 0)
        def printArg(self):
            return self.getTypedRuleContext(RaraLangParser.PrintArgContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = RaraLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = RaraLangParser.AssignStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(RaraLangParser.ID)
                self.state = 19
                self.match(RaraLangParser.ASSIGN)
                self.state = 20
                self.expr(0)
                pass
            elif token in [4]:
                localctx = RaraLangParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(RaraLangParser.PRINT)
                self.state = 22
                self.printArg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RaraLangParser.RULE_printArg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringPrintArgContext(PrintArgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.PrintArgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(RaraLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringPrintArg" ):
                listener.enterStringPrintArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringPrintArg" ):
                listener.exitStringPrintArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringPrintArg" ):
                return visitor.visitStringPrintArg(self)
            else:
                return visitor.visitChildren(self)


    class ExprPrintArgContext(PrintArgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.PrintArgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPrintArg" ):
                listener.enterExprPrintArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPrintArg" ):
                listener.exitExprPrintArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPrintArg" ):
                return visitor.visitExprPrintArg(self)
            else:
                return visitor.visitChildren(self)



    def printArg(self):

        localctx = RaraLangParser.PrintArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printArg)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = RaraLangParser.StringPrintArgContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(RaraLangParser.STRING)
                pass
            elif token in [1, 12, 13, 14, 16]:
                localctx = RaraLangParser.ExprPrintArgContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RaraLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(RaraLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(RaraLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(RaraLangParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(RaraLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEG(self):
            return self.getToken(RaraLangParser.NEG, 0)
        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegExpr" ):
                listener.enterNegExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegExpr" ):
                listener.exitNegExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class AvgExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)

        def AVG(self):
            return self.getToken(RaraLangParser.AVG, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvgExpr" ):
                listener.enterAvgExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvgExpr" ):
                listener.exitAvgExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAvgExpr" ):
                return visitor.visitAvgExpr(self)
            else:
                return visitor.visitChildren(self)


    class ModExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)

        def MOD(self):
            return self.getToken(RaraLangParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModExpr" ):
                listener.enterModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModExpr" ):
                listener.exitModExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModExpr" ):
                return visitor.visitModExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RaraLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class DoublePlusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)

        def DOUBLE_PLUS(self):
            return self.getToken(RaraLangParser.DOUBLE_PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoublePlusExpr" ):
                listener.enterDoublePlusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoublePlusExpr" ):
                listener.exitDoublePlusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoublePlusExpr" ):
                return visitor.visitDoublePlusExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RaraLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RaraLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(RaraLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(RaraLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(RaraLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RaraLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = RaraLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 30
                self.match(RaraLangParser.T__0)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(RaraLangParser.T__1)
                pass
            elif token in [13, 14]:
                localctx = RaraLangParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.literal()
                pass
            elif token in [16]:
                localctx = RaraLangParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(RaraLangParser.ID)
                pass
            elif token in [12]:
                localctx = RaraLangParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(RaraLangParser.NEG)
                self.state = 37
                self.expr(6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = RaraLangParser.MulDivExprContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = RaraLangParser.DoublePlusExprContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 44
                        self.match(RaraLangParser.DOUBLE_PLUS)
                        self.state = 45
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = RaraLangParser.ModExprContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 47
                        self.match(RaraLangParser.MOD)
                        self.state = 48
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = RaraLangParser.AvgExprContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 50
                        self.match(RaraLangParser.AVG)
                        self.state = 51
                        self.expr(3)
                        pass

                    elif la_ == 5:
                        localctx = RaraLangParser.AddSubExprContext(self, RaraLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 53
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(2)
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RaraLangParser.INT, 0)

        def BASED_INT(self):
            return self.getToken(RaraLangParser.BASED_INT, 0)

        def getRuleIndex(self):
            return RaraLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = RaraLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




