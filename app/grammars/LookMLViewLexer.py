# Generated from LookMLViewLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("E\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\7\5\62\n\5\f\5\16\5\65\13")
        buf.write("\5\3\6\6\68\n\6\r\6\16\69\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\3\2\5\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\2F\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\3\25\3\2\2\2\5\33\3\2\2\2\7&\3\2\2\2\t/")
        buf.write("\3\2\2\2\13\67\3\2\2\2\r=\3\2\2\2\17?\3\2\2\2\21A\3\2")
        buf.write("\2\2\23C\3\2\2\2\25\26\7x\2\2\26\27\7k\2\2\27\30\7g\2")
        buf.write("\2\30\31\7y\2\2\31\32\7<\2\2\32\4\3\2\2\2\33\34\7f\2\2")
        buf.write("\34\35\7k\2\2\35\36\7o\2\2\36\37\7g\2\2\37 \7p\2\2 !\7")
        buf.write("u\2\2!\"\7k\2\2\"#\7q\2\2#$\7p\2\2$%\7<\2\2%\6\3\2\2\2")
        buf.write("&\'\7o\2\2\'(\7g\2\2()\7c\2\2)*\7u\2\2*+\7w\2\2+,\7t\2")
        buf.write("\2,-\7g\2\2-.\7<\2\2.\b\3\2\2\2/\63\t\2\2\2\60\62\t\3")
        buf.write("\2\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3")
        buf.write("\2\2\2\64\n\3\2\2\2\65\63\3\2\2\2\668\t\4\2\2\67\66\3")
        buf.write("\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\b\6")
        buf.write("\2\2<\f\3\2\2\2=>\7}\2\2>\16\3\2\2\2?@\7\177\2\2@\20\3")
        buf.write("\2\2\2AB\7=\2\2B\22\3\2\2\2CD\7<\2\2D\24\3\2\2\2\5\2\63")
        buf.write("9\3\b\2\2")
        return buf.getvalue()


class LookMLViewLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VIEW = 1
    DIMENSION = 2
    MEASURE = 3
    IDENTIFIER = 4
    WHITESPACE = 5
    LBRACE = 6
    RBRACE = 7
    SEMICOLON = 8
    COLON = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'view:'", "'dimension:'", "'measure:'", "'{'", "'}'", "';'", 
            "':'" ]

    symbolicNames = [ "<INVALID>",
            "VIEW", "DIMENSION", "MEASURE", "IDENTIFIER", "WHITESPACE", 
            "LBRACE", "RBRACE", "SEMICOLON", "COLON" ]

    ruleNames = [ "VIEW", "DIMENSION", "MEASURE", "IDENTIFIER", "WHITESPACE", 
                  "LBRACE", "RBRACE", "SEMICOLON", "COLON" ]

    grammarFileName = "LookMLViewLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


