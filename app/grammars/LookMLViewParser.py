# Generated from LookMLViewParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write(" \4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\7\3\23\n\3\f\3\16\3\26\13\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2\35\2\n\3\2")
        buf.write("\2\2\4\r\3\2\2\2\6\31\3\2\2\2\b\34\3\2\2\2\n\13\5\4\3")
        buf.write("\2\13\f\7\2\2\3\f\3\3\2\2\2\r\16\7\3\2\2\16\17\7\6\2\2")
        buf.write("\17\24\7\b\2\2\20\23\5\6\4\2\21\23\5\b\5\2\22\20\3\2\2")
        buf.write("\2\22\21\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24\25\3\2")
        buf.write("\2\2\25\27\3\2\2\2\26\24\3\2\2\2\27\30\7\t\2\2\30\5\3")
        buf.write("\2\2\2\31\32\7\4\2\2\32\33\7\6\2\2\33\7\3\2\2\2\34\35")
        buf.write("\7\5\2\2\35\36\7\6\2\2\36\t\3\2\2\2\4\22\24")
        return buf.getvalue()


class LookMLViewParser ( Parser ):

    grammarFileName = "LookMLViewParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'view:'", "'dimension:'", "'measure:'", 
                     "<INVALID>", "<INVALID>", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "VIEW", "DIMENSION", "MEASURE", "IDENTIFIER", 
                      "WHITESPACE", "LBRACE", "RBRACE", "SEMICOLON", "COLON" ]

    RULE_viewFile = 0
    RULE_viewDefinition = 1
    RULE_dimensionDefinition = 2
    RULE_measureDefinition = 3

    ruleNames =  [ "viewFile", "viewDefinition", "dimensionDefinition", 
                   "measureDefinition" ]

    EOF = Token.EOF
    VIEW=1
    DIMENSION=2
    MEASURE=3
    IDENTIFIER=4
    WHITESPACE=5
    LBRACE=6
    RBRACE=7
    SEMICOLON=8
    COLON=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ViewFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def viewDefinition(self):
            return self.getTypedRuleContext(LookMLViewParser.ViewDefinitionContext,0)


        def EOF(self):
            return self.getToken(LookMLViewParser.EOF, 0)

        def getRuleIndex(self):
            return LookMLViewParser.RULE_viewFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterViewFile" ):
                listener.enterViewFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitViewFile" ):
                listener.exitViewFile(self)




    def viewFile(self):

        localctx = LookMLViewParser.ViewFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_viewFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.viewDefinition()
            self.state = 9
            self.match(LookMLViewParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ViewDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIEW(self):
            return self.getToken(LookMLViewParser.VIEW, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLViewParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLViewParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLViewParser.RBRACE, 0)

        def dimensionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLViewParser.DimensionDefinitionContext)
            else:
                return self.getTypedRuleContext(LookMLViewParser.DimensionDefinitionContext,i)


        def measureDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLViewParser.MeasureDefinitionContext)
            else:
                return self.getTypedRuleContext(LookMLViewParser.MeasureDefinitionContext,i)


        def getRuleIndex(self):
            return LookMLViewParser.RULE_viewDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterViewDefinition" ):
                listener.enterViewDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitViewDefinition" ):
                listener.exitViewDefinition(self)




    def viewDefinition(self):

        localctx = LookMLViewParser.ViewDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_viewDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(LookMLViewParser.VIEW)
            self.state = 12
            self.match(LookMLViewParser.IDENTIFIER)
            self.state = 13
            self.match(LookMLViewParser.LBRACE)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LookMLViewParser.DIMENSION or _la==LookMLViewParser.MEASURE:
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LookMLViewParser.DIMENSION]:
                    self.state = 14
                    self.dimensionDefinition()
                    pass
                elif token in [LookMLViewParser.MEASURE]:
                    self.state = 15
                    self.measureDefinition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(LookMLViewParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIMENSION(self):
            return self.getToken(LookMLViewParser.DIMENSION, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLViewParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LookMLViewParser.RULE_dimensionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimensionDefinition" ):
                listener.enterDimensionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimensionDefinition" ):
                listener.exitDimensionDefinition(self)




    def dimensionDefinition(self):

        localctx = LookMLViewParser.DimensionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dimensionDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(LookMLViewParser.DIMENSION)
            self.state = 24
            self.match(LookMLViewParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasureDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEASURE(self):
            return self.getToken(LookMLViewParser.MEASURE, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLViewParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LookMLViewParser.RULE_measureDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasureDefinition" ):
                listener.enterMeasureDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasureDefinition" ):
                listener.exitMeasureDefinition(self)




    def measureDefinition(self):

        localctx = LookMLViewParser.MeasureDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_measureDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(LookMLViewParser.MEASURE)
            self.state = 27
            self.match(LookMLViewParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





