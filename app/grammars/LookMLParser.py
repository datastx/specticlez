# Generated from LookMLParser.g4 by ANTLR 4.12.0
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
        4,1,41,324,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        5,1,82,8,1,10,1,12,1,85,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,94,8,
        2,10,2,12,2,97,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,106,8,3,10,3,
        12,3,109,9,3,1,3,1,3,1,4,1,4,3,4,115,8,4,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,123,8,5,1,6,1,6,1,6,1,6,1,6,3,6,130,8,6,1,7,1,7,1,7,1,7,1,7,
        3,7,137,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,150,
        8,9,10,9,12,9,153,9,9,1,9,1,9,1,10,1,10,1,10,5,10,160,8,10,10,10,
        12,10,163,9,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,
        5,15,188,8,15,10,15,12,15,191,9,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,5,16,200,8,16,10,16,12,16,203,9,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,17,5,17,212,8,17,10,17,12,17,215,9,17,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,5,18,224,8,18,10,18,12,18,227,9,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,5,19,236,8,19,10,19,12,19,239,9,19,1,19,1,19,
        1,20,1,20,1,20,1,20,3,20,247,8,20,1,21,1,21,1,21,3,21,252,8,21,1,
        22,1,22,1,22,3,22,257,8,22,1,23,1,23,3,23,261,8,23,1,24,1,24,1,24,
        3,24,266,8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,
        1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,5,31,305,8,31,10,31,12,31,308,9,31,3,31,310,8,31,1,31,1,31,
        1,32,1,32,1,32,5,32,317,8,32,10,32,12,32,320,9,32,3,32,322,8,32,
        1,32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,0,327,0,71,1,0,0,0,2,
        76,1,0,0,0,4,88,1,0,0,0,6,100,1,0,0,0,8,114,1,0,0,0,10,122,1,0,0,
        0,12,124,1,0,0,0,14,131,1,0,0,0,16,141,1,0,0,0,18,145,1,0,0,0,20,
        156,1,0,0,0,22,166,1,0,0,0,24,170,1,0,0,0,26,174,1,0,0,0,28,178,
        1,0,0,0,30,182,1,0,0,0,32,194,1,0,0,0,34,206,1,0,0,0,36,218,1,0,
        0,0,38,230,1,0,0,0,40,246,1,0,0,0,42,251,1,0,0,0,44,256,1,0,0,0,
        46,260,1,0,0,0,48,265,1,0,0,0,50,267,1,0,0,0,52,271,1,0,0,0,54,282,
        1,0,0,0,56,286,1,0,0,0,58,290,1,0,0,0,60,296,1,0,0,0,62,300,1,0,
        0,0,64,321,1,0,0,0,66,70,3,2,1,0,67,70,3,4,2,0,68,70,3,6,3,0,69,
        66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,
        0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,0,0,1,75,1,1,
        0,0,0,76,77,5,2,0,0,77,78,5,30,0,0,78,79,5,36,0,0,79,83,5,26,0,0,
        80,82,3,8,4,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,
        0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,5,27,0,0,87,3,1,0,0,0,88,
        89,5,3,0,0,89,90,5,30,0,0,90,91,5,36,0,0,91,95,5,26,0,0,92,94,3,
        10,5,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,
        98,1,0,0,0,97,95,1,0,0,0,98,99,5,27,0,0,99,5,1,0,0,0,100,101,5,10,
        0,0,101,102,5,30,0,0,102,103,5,36,0,0,103,107,5,26,0,0,104,106,3,
        12,6,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,
        0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,5,27,0,0,111,7,1,0,
        0,0,112,115,3,18,9,0,113,115,3,20,10,0,114,112,1,0,0,0,114,113,1,
        0,0,0,115,9,1,0,0,0,116,123,3,14,7,0,117,123,3,30,15,0,118,123,3,
        32,16,0,119,123,3,34,17,0,120,123,3,36,18,0,121,123,3,38,19,0,122,
        116,1,0,0,0,122,117,1,0,0,0,122,118,1,0,0,0,122,119,1,0,0,0,122,
        120,1,0,0,0,122,121,1,0,0,0,123,11,1,0,0,0,124,129,3,16,8,0,125,
        130,3,18,9,0,126,130,3,20,10,0,127,130,3,22,11,0,128,130,3,24,12,
        0,129,125,1,0,0,0,129,126,1,0,0,0,129,127,1,0,0,0,129,128,1,0,0,
        0,130,13,1,0,0,0,131,132,5,21,0,0,132,133,5,30,0,0,133,136,5,36,
        0,0,134,135,5,33,0,0,135,137,5,36,0,0,136,134,1,0,0,0,136,137,1,
        0,0,0,137,138,1,0,0,0,138,139,5,32,0,0,139,140,5,32,0,0,140,15,1,
        0,0,0,141,142,5,4,0,0,142,143,5,30,0,0,143,144,5,36,0,0,144,17,1,
        0,0,0,145,146,5,11,0,0,146,147,5,36,0,0,147,151,5,26,0,0,148,150,
        3,26,13,0,149,148,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,
        1,0,0,0,152,154,1,0,0,0,153,151,1,0,0,0,154,155,5,27,0,0,155,19,
        1,0,0,0,156,157,5,16,0,0,157,161,5,26,0,0,158,160,3,28,14,0,159,
        158,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,
        164,1,0,0,0,163,161,1,0,0,0,164,165,5,27,0,0,165,21,1,0,0,0,166,
        167,5,17,0,0,167,168,5,30,0,0,168,169,5,36,0,0,169,23,1,0,0,0,170,
        171,5,19,0,0,171,172,5,30,0,0,172,173,5,38,0,0,173,25,1,0,0,0,174,
        175,5,12,0,0,175,176,5,30,0,0,176,177,5,38,0,0,177,27,1,0,0,0,178,
        179,5,12,0,0,179,180,5,30,0,0,180,181,5,38,0,0,181,29,1,0,0,0,182,
        183,5,5,0,0,183,184,5,30,0,0,184,185,5,36,0,0,185,189,5,26,0,0,186,
        188,3,40,20,0,187,186,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,
        190,1,0,0,0,190,192,1,0,0,0,191,189,1,0,0,0,192,193,5,27,0,0,193,
        31,1,0,0,0,194,195,5,6,0,0,195,196,5,30,0,0,196,197,5,36,0,0,197,
        201,5,26,0,0,198,200,3,42,21,0,199,198,1,0,0,0,200,203,1,0,0,0,201,
        199,1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,201,1,0,0,0,204,
        205,5,27,0,0,205,33,1,0,0,0,206,207,5,7,0,0,207,208,5,30,0,0,208,
        209,5,36,0,0,209,213,5,26,0,0,210,212,3,44,22,0,211,210,1,0,0,0,
        212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,
        215,213,1,0,0,0,216,217,5,27,0,0,217,35,1,0,0,0,218,219,5,8,0,0,
        219,220,5,30,0,0,220,221,5,36,0,0,221,225,5,26,0,0,222,224,3,46,
        23,0,223,222,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,
        0,0,226,228,1,0,0,0,227,225,1,0,0,0,228,229,5,27,0,0,229,37,1,0,
        0,0,230,231,5,9,0,0,231,232,5,30,0,0,232,233,5,36,0,0,233,237,5,
        26,0,0,234,236,3,48,24,0,235,234,1,0,0,0,236,239,1,0,0,0,237,235,
        1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,237,1,0,0,0,240,241,
        5,27,0,0,241,39,1,0,0,0,242,247,3,50,25,0,243,247,3,52,26,0,244,
        247,3,54,27,0,245,247,3,58,29,0,246,242,1,0,0,0,246,243,1,0,0,0,
        246,244,1,0,0,0,246,245,1,0,0,0,247,41,1,0,0,0,248,252,3,50,25,0,
        249,252,3,52,26,0,250,252,3,58,29,0,251,248,1,0,0,0,251,249,1,0,
        0,0,251,250,1,0,0,0,252,43,1,0,0,0,253,257,3,50,25,0,254,257,3,52,
        26,0,255,257,3,60,30,0,256,253,1,0,0,0,256,254,1,0,0,0,256,255,1,
        0,0,0,257,45,1,0,0,0,258,261,3,50,25,0,259,261,3,52,26,0,260,258,
        1,0,0,0,260,259,1,0,0,0,261,47,1,0,0,0,262,266,3,50,25,0,263,266,
        3,52,26,0,264,266,3,56,28,0,265,262,1,0,0,0,265,263,1,0,0,0,265,
        264,1,0,0,0,266,49,1,0,0,0,267,268,5,14,0,0,268,269,5,30,0,0,269,
        270,5,36,0,0,270,51,1,0,0,0,271,272,5,12,0,0,272,273,5,30,0,0,273,
        274,5,39,0,0,274,275,5,26,0,0,275,276,5,36,0,0,276,277,5,27,0,0,
        277,278,5,33,0,0,278,279,5,36,0,0,279,280,5,32,0,0,280,281,5,32,
        0,0,281,53,1,0,0,0,282,283,5,15,0,0,283,284,5,30,0,0,284,285,5,36,
        0,0,285,55,1,0,0,0,286,287,5,20,0,0,287,288,5,30,0,0,288,289,3,62,
        31,0,289,57,1,0,0,0,290,291,5,22,0,0,291,292,5,30,0,0,292,293,5,
        28,0,0,293,294,3,64,32,0,294,295,5,29,0,0,295,59,1,0,0,0,296,297,
        5,23,0,0,297,298,5,30,0,0,298,299,5,38,0,0,299,61,1,0,0,0,300,309,
        5,24,0,0,301,306,5,38,0,0,302,303,5,31,0,0,303,305,5,38,0,0,304,
        302,1,0,0,0,305,308,1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,
        310,1,0,0,0,308,306,1,0,0,0,309,301,1,0,0,0,309,310,1,0,0,0,310,
        311,1,0,0,0,311,312,5,25,0,0,312,63,1,0,0,0,313,318,5,36,0,0,314,
        315,5,31,0,0,315,317,5,36,0,0,316,314,1,0,0,0,317,320,1,0,0,0,318,
        316,1,0,0,0,318,319,1,0,0,0,319,322,1,0,0,0,320,318,1,0,0,0,321,
        313,1,0,0,0,321,322,1,0,0,0,322,65,1,0,0,0,25,69,71,83,95,107,114,
        122,129,136,151,161,189,201,213,225,237,246,251,256,260,265,306,
        309,318,321
    ]

class LookMLParser ( Parser ):

    grammarFileName = "LookMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'looker'", "'model'", "'view'", "'view_name'", 
                     "'dimension'", "'dimension_group'", "'measure'", "'filter'", 
                     "'parameter'", "'explore'", "'join'", "'sql'", "'alias'", 
                     "'type'", "'primary_key'", "'derived_table'", "'relationship'", 
                     "'required'", "'link'", "'allowed_values'", "'sql_table_name'", 
                     "'timeframes'", "'value_format'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "':'", "','", "';'", "'.'", "'='", 
                     "'|'", "<INVALID>", "<INVALID>", "<INVALID>", "'$'" ]

    symbolicNames = [ "<INVALID>", "LOOKER", "MODEL", "VIEW", "VIEW_NAME", 
                      "DIMENSION", "DIMENSION_GROUP", "MEASURE", "FILTER", 
                      "PARAMETER", "EXPLORE", "JOIN", "SQL", "ALIAS", "TYPE", 
                      "PRIMARY_KEY", "DERIVED_TABLE", "RELATIONSHIP", "REQUIRED", 
                      "LINK", "ALLOWED_VALUES", "SQL_TABLE_NAME", "TIMEFRAMES", 
                      "VALUE_FORMAT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "COLON", "COMMA", "SEMI", 
                      "DOT", "EQ", "PIPE", "IDENTIFIER", "NUMBER", "STRING", 
                      "DOLLAR", "COMMENT", "WS" ]

    RULE_lookml_file = 0
    RULE_model = 1
    RULE_view = 2
    RULE_explore = 3
    RULE_model_property = 4
    RULE_view_property = 5
    RULE_explore_property = 6
    RULE_sql_table_name_property = 7
    RULE_explore_view_name = 8
    RULE_join = 9
    RULE_derived_table = 10
    RULE_relationship = 11
    RULE_link = 12
    RULE_join_property = 13
    RULE_derived_table_property = 14
    RULE_dimension = 15
    RULE_dimension_group = 16
    RULE_measure = 17
    RULE_filter = 18
    RULE_parameter = 19
    RULE_dimension_property = 20
    RULE_dimension_group_property = 21
    RULE_measure_property = 22
    RULE_filter_property = 23
    RULE_parameter_property = 24
    RULE_type_property = 25
    RULE_sql_property = 26
    RULE_primary_key_property = 27
    RULE_allowed_value_property = 28
    RULE_timeframes_property = 29
    RULE_value_format_property = 30
    RULE_allowed_value_list = 31
    RULE_timeframe_list = 32

    ruleNames =  [ "lookml_file", "model", "view", "explore", "model_property", 
                   "view_property", "explore_property", "sql_table_name_property", 
                   "explore_view_name", "join", "derived_table", "relationship", 
                   "link", "join_property", "derived_table_property", "dimension", 
                   "dimension_group", "measure", "filter", "parameter", 
                   "dimension_property", "dimension_group_property", "measure_property", 
                   "filter_property", "parameter_property", "type_property", 
                   "sql_property", "primary_key_property", "allowed_value_property", 
                   "timeframes_property", "value_format_property", "allowed_value_list", 
                   "timeframe_list" ]

    EOF = Token.EOF
    LOOKER=1
    MODEL=2
    VIEW=3
    VIEW_NAME=4
    DIMENSION=5
    DIMENSION_GROUP=6
    MEASURE=7
    FILTER=8
    PARAMETER=9
    EXPLORE=10
    JOIN=11
    SQL=12
    ALIAS=13
    TYPE=14
    PRIMARY_KEY=15
    DERIVED_TABLE=16
    RELATIONSHIP=17
    REQUIRED=18
    LINK=19
    ALLOWED_VALUES=20
    SQL_TABLE_NAME=21
    TIMEFRAMES=22
    VALUE_FORMAT=23
    LPAREN=24
    RPAREN=25
    LBRACE=26
    RBRACE=27
    LBRACKET=28
    RBRACKET=29
    COLON=30
    COMMA=31
    SEMI=32
    DOT=33
    EQ=34
    PIPE=35
    IDENTIFIER=36
    NUMBER=37
    STRING=38
    DOLLAR=39
    COMMENT=40
    WS=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Lookml_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LookMLParser.EOF, 0)

        def model(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.ModelContext)
            else:
                return self.getTypedRuleContext(LookMLParser.ModelContext,i)


        def view(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.ViewContext)
            else:
                return self.getTypedRuleContext(LookMLParser.ViewContext,i)


        def explore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.ExploreContext)
            else:
                return self.getTypedRuleContext(LookMLParser.ExploreContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_lookml_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLookml_file" ):
                listener.enterLookml_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLookml_file" ):
                listener.exitLookml_file(self)




    def lookml_file(self):

        localctx = LookMLParser.Lookml_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lookml_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1036) != 0):
                self.state = 69
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 66
                    self.model()
                    pass
                elif token in [3]:
                    self.state = 67
                    self.view()
                    pass
                elif token in [10]:
                    self.state = 68
                    self.explore()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(LookMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODEL(self):
            return self.getToken(LookMLParser.MODEL, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def model_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Model_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Model_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)




    def model(self):

        localctx = LookMLParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(LookMLParser.MODEL)
            self.state = 77
            self.match(LookMLParser.COLON)
            self.state = 78
            self.match(LookMLParser.IDENTIFIER)
            self.state = 79
            self.match(LookMLParser.LBRACE)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==16:
                self.state = 80
                self.model_property()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ViewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIEW(self):
            return self.getToken(LookMLParser.VIEW, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def view_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.View_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.View_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_view

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterView" ):
                listener.enterView(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitView" ):
                listener.exitView(self)




    def view(self):

        localctx = LookMLParser.ViewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_view)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(LookMLParser.VIEW)
            self.state = 89
            self.match(LookMLParser.COLON)
            self.state = 90
            self.match(LookMLParser.IDENTIFIER)
            self.state = 91
            self.match(LookMLParser.LBRACE)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2098144) != 0):
                self.state = 92
                self.view_property()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExploreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPLORE(self):
            return self.getToken(LookMLParser.EXPLORE, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def explore_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Explore_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Explore_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_explore

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplore" ):
                listener.enterExplore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplore" ):
                listener.exitExplore(self)




    def explore(self):

        localctx = LookMLParser.ExploreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_explore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LookMLParser.EXPLORE)
            self.state = 101
            self.match(LookMLParser.COLON)
            self.state = 102
            self.match(LookMLParser.IDENTIFIER)
            self.state = 103
            self.match(LookMLParser.LBRACE)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 104
                self.explore_property()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Model_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def join(self):
            return self.getTypedRuleContext(LookMLParser.JoinContext,0)


        def derived_table(self):
            return self.getTypedRuleContext(LookMLParser.Derived_tableContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_model_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_property" ):
                listener.enterModel_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_property" ):
                listener.exitModel_property(self)




    def model_property(self):

        localctx = LookMLParser.Model_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_model_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 112
                self.join()
                pass
            elif token in [16]:
                self.state = 113
                self.derived_table()
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


    class View_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sql_table_name_property(self):
            return self.getTypedRuleContext(LookMLParser.Sql_table_name_propertyContext,0)


        def dimension(self):
            return self.getTypedRuleContext(LookMLParser.DimensionContext,0)


        def dimension_group(self):
            return self.getTypedRuleContext(LookMLParser.Dimension_groupContext,0)


        def measure(self):
            return self.getTypedRuleContext(LookMLParser.MeasureContext,0)


        def filter_(self):
            return self.getTypedRuleContext(LookMLParser.FilterContext,0)


        def parameter(self):
            return self.getTypedRuleContext(LookMLParser.ParameterContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_view_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterView_property" ):
                listener.enterView_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitView_property" ):
                listener.exitView_property(self)




    def view_property(self):

        localctx = LookMLParser.View_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_view_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 116
                self.sql_table_name_property()
                pass
            elif token in [5]:
                self.state = 117
                self.dimension()
                pass
            elif token in [6]:
                self.state = 118
                self.dimension_group()
                pass
            elif token in [7]:
                self.state = 119
                self.measure()
                pass
            elif token in [8]:
                self.state = 120
                self.filter_()
                pass
            elif token in [9]:
                self.state = 121
                self.parameter()
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


    class Explore_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explore_view_name(self):
            return self.getTypedRuleContext(LookMLParser.Explore_view_nameContext,0)


        def join(self):
            return self.getTypedRuleContext(LookMLParser.JoinContext,0)


        def derived_table(self):
            return self.getTypedRuleContext(LookMLParser.Derived_tableContext,0)


        def relationship(self):
            return self.getTypedRuleContext(LookMLParser.RelationshipContext,0)


        def link(self):
            return self.getTypedRuleContext(LookMLParser.LinkContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_explore_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplore_property" ):
                listener.enterExplore_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplore_property" ):
                listener.exitExplore_property(self)




    def explore_property(self):

        localctx = LookMLParser.Explore_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_explore_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.explore_view_name()
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 125
                self.join()
                pass
            elif token in [16]:
                self.state = 126
                self.derived_table()
                pass
            elif token in [17]:
                self.state = 127
                self.relationship()
                pass
            elif token in [19]:
                self.state = 128
                self.link()
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


    class Sql_table_name_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQL_TABLE_NAME(self):
            return self.getToken(LookMLParser.SQL_TABLE_NAME, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LookMLParser.IDENTIFIER)
            else:
                return self.getToken(LookMLParser.IDENTIFIER, i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(LookMLParser.SEMI)
            else:
                return self.getToken(LookMLParser.SEMI, i)

        def DOT(self):
            return self.getToken(LookMLParser.DOT, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_sql_table_name_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_table_name_property" ):
                listener.enterSql_table_name_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_table_name_property" ):
                listener.exitSql_table_name_property(self)




    def sql_table_name_property(self):

        localctx = LookMLParser.Sql_table_name_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sql_table_name_property)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(LookMLParser.SQL_TABLE_NAME)
            self.state = 132
            self.match(LookMLParser.COLON)
            self.state = 133
            self.match(LookMLParser.IDENTIFIER)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 134
                self.match(LookMLParser.DOT)
                self.state = 135
                self.match(LookMLParser.IDENTIFIER)


            self.state = 138
            self.match(LookMLParser.SEMI)
            self.state = 139
            self.match(LookMLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explore_view_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIEW_NAME(self):
            return self.getToken(LookMLParser.VIEW_NAME, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_explore_view_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplore_view_name" ):
                listener.enterExplore_view_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplore_view_name" ):
                listener.exitExplore_view_name(self)




    def explore_view_name(self):

        localctx = LookMLParser.Explore_view_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_explore_view_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(LookMLParser.VIEW_NAME)
            self.state = 142
            self.match(LookMLParser.COLON)
            self.state = 143
            self.match(LookMLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(LookMLParser.JOIN, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def join_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Join_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Join_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_join

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin" ):
                listener.enterJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin" ):
                listener.exitJoin(self)




    def join(self):

        localctx = LookMLParser.JoinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_join)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(LookMLParser.JOIN)
            self.state = 146
            self.match(LookMLParser.IDENTIFIER)
            self.state = 147
            self.match(LookMLParser.LBRACE)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 148
                self.join_property()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Derived_tableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DERIVED_TABLE(self):
            return self.getToken(LookMLParser.DERIVED_TABLE, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def derived_table_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Derived_table_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Derived_table_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_derived_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDerived_table" ):
                listener.enterDerived_table(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDerived_table" ):
                listener.exitDerived_table(self)




    def derived_table(self):

        localctx = LookMLParser.Derived_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_derived_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(LookMLParser.DERIVED_TABLE)
            self.state = 157
            self.match(LookMLParser.LBRACE)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 158
                self.derived_table_property()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationshipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RELATIONSHIP(self):
            return self.getToken(LookMLParser.RELATIONSHIP, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_relationship

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationship" ):
                listener.enterRelationship(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationship" ):
                listener.exitRelationship(self)




    def relationship(self):

        localctx = LookMLParser.RelationshipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relationship)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(LookMLParser.RELATIONSHIP)
            self.state = 167
            self.match(LookMLParser.COLON)
            self.state = 168
            self.match(LookMLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINK(self):
            return self.getToken(LookMLParser.LINK, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def STRING(self):
            return self.getToken(LookMLParser.STRING, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)




    def link(self):

        localctx = LookMLParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(LookMLParser.LINK)
            self.state = 171
            self.match(LookMLParser.COLON)
            self.state = 172
            self.match(LookMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQL(self):
            return self.getToken(LookMLParser.SQL, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def STRING(self):
            return self.getToken(LookMLParser.STRING, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_join_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin_property" ):
                listener.enterJoin_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin_property" ):
                listener.exitJoin_property(self)




    def join_property(self):

        localctx = LookMLParser.Join_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_join_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(LookMLParser.SQL)
            self.state = 175
            self.match(LookMLParser.COLON)
            self.state = 176
            self.match(LookMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Derived_table_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQL(self):
            return self.getToken(LookMLParser.SQL, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def STRING(self):
            return self.getToken(LookMLParser.STRING, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_derived_table_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDerived_table_property" ):
                listener.enterDerived_table_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDerived_table_property" ):
                listener.exitDerived_table_property(self)




    def derived_table_property(self):

        localctx = LookMLParser.Derived_table_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_derived_table_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(LookMLParser.SQL)
            self.state = 179
            self.match(LookMLParser.COLON)
            self.state = 180
            self.match(LookMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIMENSION(self):
            return self.getToken(LookMLParser.DIMENSION, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def dimension_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Dimension_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Dimension_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_dimension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension" ):
                listener.enterDimension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension" ):
                listener.exitDimension(self)




    def dimension(self):

        localctx = LookMLParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dimension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(LookMLParser.DIMENSION)
            self.state = 183
            self.match(LookMLParser.COLON)
            self.state = 184
            self.match(LookMLParser.IDENTIFIER)
            self.state = 185
            self.match(LookMLParser.LBRACE)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4247552) != 0):
                self.state = 186
                self.dimension_property()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIMENSION_GROUP(self):
            return self.getToken(LookMLParser.DIMENSION_GROUP, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def dimension_group_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Dimension_group_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Dimension_group_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_dimension_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension_group" ):
                listener.enterDimension_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension_group" ):
                listener.exitDimension_group(self)




    def dimension_group(self):

        localctx = LookMLParser.Dimension_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dimension_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(LookMLParser.DIMENSION_GROUP)
            self.state = 195
            self.match(LookMLParser.COLON)
            self.state = 196
            self.match(LookMLParser.IDENTIFIER)
            self.state = 197
            self.match(LookMLParser.LBRACE)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4214784) != 0):
                self.state = 198
                self.dimension_group_property()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEASURE(self):
            return self.getToken(LookMLParser.MEASURE, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def measure_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Measure_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Measure_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_measure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasure" ):
                listener.enterMeasure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasure" ):
                listener.exitMeasure(self)




    def measure(self):

        localctx = LookMLParser.MeasureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_measure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(LookMLParser.MEASURE)
            self.state = 207
            self.match(LookMLParser.COLON)
            self.state = 208
            self.match(LookMLParser.IDENTIFIER)
            self.state = 209
            self.match(LookMLParser.LBRACE)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8409088) != 0):
                self.state = 210
                self.measure_property()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(LookMLParser.FILTER, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def filter_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Filter_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Filter_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter" ):
                listener.enterFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter" ):
                listener.exitFilter(self)




    def filter_(self):

        localctx = LookMLParser.FilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_filter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(LookMLParser.FILTER)
            self.state = 219
            self.match(LookMLParser.COLON)
            self.state = 220
            self.match(LookMLParser.IDENTIFIER)
            self.state = 221
            self.match(LookMLParser.LBRACE)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==14:
                self.state = 222
                self.filter_property()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(LookMLParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def parameter_property(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Parameter_propertyContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Parameter_propertyContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = LookMLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(LookMLParser.PARAMETER)
            self.state = 231
            self.match(LookMLParser.COLON)
            self.state = 232
            self.match(LookMLParser.IDENTIFIER)
            self.state = 233
            self.match(LookMLParser.LBRACE)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1069056) != 0):
                self.state = 234
                self.parameter_property()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(LookMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_property(self):
            return self.getTypedRuleContext(LookMLParser.Type_propertyContext,0)


        def sql_property(self):
            return self.getTypedRuleContext(LookMLParser.Sql_propertyContext,0)


        def primary_key_property(self):
            return self.getTypedRuleContext(LookMLParser.Primary_key_propertyContext,0)


        def timeframes_property(self):
            return self.getTypedRuleContext(LookMLParser.Timeframes_propertyContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_dimension_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension_property" ):
                listener.enterDimension_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension_property" ):
                listener.exitDimension_property(self)




    def dimension_property(self):

        localctx = LookMLParser.Dimension_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dimension_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 242
                self.type_property()
                pass
            elif token in [12]:
                self.state = 243
                self.sql_property()
                pass
            elif token in [15]:
                self.state = 244
                self.primary_key_property()
                pass
            elif token in [22]:
                self.state = 245
                self.timeframes_property()
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


    class Dimension_group_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_property(self):
            return self.getTypedRuleContext(LookMLParser.Type_propertyContext,0)


        def sql_property(self):
            return self.getTypedRuleContext(LookMLParser.Sql_propertyContext,0)


        def timeframes_property(self):
            return self.getTypedRuleContext(LookMLParser.Timeframes_propertyContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_dimension_group_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension_group_property" ):
                listener.enterDimension_group_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension_group_property" ):
                listener.exitDimension_group_property(self)




    def dimension_group_property(self):

        localctx = LookMLParser.Dimension_group_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dimension_group_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 248
                self.type_property()
                pass
            elif token in [12]:
                self.state = 249
                self.sql_property()
                pass
            elif token in [22]:
                self.state = 250
                self.timeframes_property()
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


    class Measure_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_property(self):
            return self.getTypedRuleContext(LookMLParser.Type_propertyContext,0)


        def sql_property(self):
            return self.getTypedRuleContext(LookMLParser.Sql_propertyContext,0)


        def value_format_property(self):
            return self.getTypedRuleContext(LookMLParser.Value_format_propertyContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_measure_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasure_property" ):
                listener.enterMeasure_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasure_property" ):
                listener.exitMeasure_property(self)




    def measure_property(self):

        localctx = LookMLParser.Measure_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_measure_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 253
                self.type_property()
                pass
            elif token in [12]:
                self.state = 254
                self.sql_property()
                pass
            elif token in [23]:
                self.state = 255
                self.value_format_property()
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


    class Filter_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_property(self):
            return self.getTypedRuleContext(LookMLParser.Type_propertyContext,0)


        def sql_property(self):
            return self.getTypedRuleContext(LookMLParser.Sql_propertyContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_filter_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter_property" ):
                listener.enterFilter_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter_property" ):
                listener.exitFilter_property(self)




    def filter_property(self):

        localctx = LookMLParser.Filter_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_filter_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 258
                self.type_property()
                pass
            elif token in [12]:
                self.state = 259
                self.sql_property()
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


    class Parameter_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_property(self):
            return self.getTypedRuleContext(LookMLParser.Type_propertyContext,0)


        def sql_property(self):
            return self.getTypedRuleContext(LookMLParser.Sql_propertyContext,0)


        def allowed_value_property(self):
            return self.getTypedRuleContext(LookMLParser.Allowed_value_propertyContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_parameter_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_property" ):
                listener.enterParameter_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_property" ):
                listener.exitParameter_property(self)




    def parameter_property(self):

        localctx = LookMLParser.Parameter_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parameter_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 262
                self.type_property()
                pass
            elif token in [12]:
                self.state = 263
                self.sql_property()
                pass
            elif token in [20]:
                self.state = 264
                self.allowed_value_property()
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


    class Type_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(LookMLParser.TYPE, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_type_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_property" ):
                listener.enterType_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_property" ):
                listener.exitType_property(self)




    def type_property(self):

        localctx = LookMLParser.Type_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_type_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(LookMLParser.TYPE)
            self.state = 268
            self.match(LookMLParser.COLON)
            self.state = 269
            self.match(LookMLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sql_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQL(self):
            return self.getToken(LookMLParser.SQL, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def DOLLAR(self):
            return self.getToken(LookMLParser.DOLLAR, 0)

        def LBRACE(self):
            return self.getToken(LookMLParser.LBRACE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LookMLParser.IDENTIFIER)
            else:
                return self.getToken(LookMLParser.IDENTIFIER, i)

        def RBRACE(self):
            return self.getToken(LookMLParser.RBRACE, 0)

        def DOT(self):
            return self.getToken(LookMLParser.DOT, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(LookMLParser.SEMI)
            else:
                return self.getToken(LookMLParser.SEMI, i)

        def getRuleIndex(self):
            return LookMLParser.RULE_sql_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_property" ):
                listener.enterSql_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_property" ):
                listener.exitSql_property(self)




    def sql_property(self):

        localctx = LookMLParser.Sql_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_sql_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(LookMLParser.SQL)
            self.state = 272
            self.match(LookMLParser.COLON)
            self.state = 273
            self.match(LookMLParser.DOLLAR)
            self.state = 274
            self.match(LookMLParser.LBRACE)
            self.state = 275
            self.match(LookMLParser.IDENTIFIER)
            self.state = 276
            self.match(LookMLParser.RBRACE)
            self.state = 277
            self.match(LookMLParser.DOT)
            self.state = 278
            self.match(LookMLParser.IDENTIFIER)
            self.state = 279
            self.match(LookMLParser.SEMI)
            self.state = 280
            self.match(LookMLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_key_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMARY_KEY(self):
            return self.getToken(LookMLParser.PRIMARY_KEY, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def IDENTIFIER(self):
            return self.getToken(LookMLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_primary_key_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_key_property" ):
                listener.enterPrimary_key_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_key_property" ):
                listener.exitPrimary_key_property(self)




    def primary_key_property(self):

        localctx = LookMLParser.Primary_key_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primary_key_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(LookMLParser.PRIMARY_KEY)
            self.state = 283
            self.match(LookMLParser.COLON)
            self.state = 284
            self.match(LookMLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allowed_value_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALLOWED_VALUES(self):
            return self.getToken(LookMLParser.ALLOWED_VALUES, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def allowed_value_list(self):
            return self.getTypedRuleContext(LookMLParser.Allowed_value_listContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_allowed_value_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllowed_value_property" ):
                listener.enterAllowed_value_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllowed_value_property" ):
                listener.exitAllowed_value_property(self)




    def allowed_value_property(self):

        localctx = LookMLParser.Allowed_value_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_allowed_value_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(LookMLParser.ALLOWED_VALUES)
            self.state = 287
            self.match(LookMLParser.COLON)
            self.state = 288
            self.allowed_value_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Timeframes_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIMEFRAMES(self):
            return self.getToken(LookMLParser.TIMEFRAMES, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def LBRACKET(self):
            return self.getToken(LookMLParser.LBRACKET, 0)

        def timeframe_list(self):
            return self.getTypedRuleContext(LookMLParser.Timeframe_listContext,0)


        def RBRACKET(self):
            return self.getToken(LookMLParser.RBRACKET, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_timeframes_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeframes_property" ):
                listener.enterTimeframes_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeframes_property" ):
                listener.exitTimeframes_property(self)




    def timeframes_property(self):

        localctx = LookMLParser.Timeframes_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_timeframes_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(LookMLParser.TIMEFRAMES)
            self.state = 291
            self.match(LookMLParser.COLON)
            self.state = 292
            self.match(LookMLParser.LBRACKET)
            self.state = 293
            self.timeframe_list()
            self.state = 294
            self.match(LookMLParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_format_propertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALUE_FORMAT(self):
            return self.getToken(LookMLParser.VALUE_FORMAT, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def STRING(self):
            return self.getToken(LookMLParser.STRING, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_value_format_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_format_property" ):
                listener.enterValue_format_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_format_property" ):
                listener.exitValue_format_property(self)




    def value_format_property(self):

        localctx = LookMLParser.Value_format_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_value_format_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(LookMLParser.VALUE_FORMAT)
            self.state = 297
            self.match(LookMLParser.COLON)
            self.state = 298
            self.match(LookMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allowed_value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LookMLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LookMLParser.RPAREN, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(LookMLParser.STRING)
            else:
                return self.getToken(LookMLParser.STRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LookMLParser.COMMA)
            else:
                return self.getToken(LookMLParser.COMMA, i)

        def getRuleIndex(self):
            return LookMLParser.RULE_allowed_value_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllowed_value_list" ):
                listener.enterAllowed_value_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllowed_value_list" ):
                listener.exitAllowed_value_list(self)




    def allowed_value_list(self):

        localctx = LookMLParser.Allowed_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_allowed_value_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(LookMLParser.LPAREN)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 301
                self.match(LookMLParser.STRING)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 302
                    self.match(LookMLParser.COMMA)
                    self.state = 303
                    self.match(LookMLParser.STRING)
                    self.state = 308
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 311
            self.match(LookMLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Timeframe_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LookMLParser.IDENTIFIER)
            else:
                return self.getToken(LookMLParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LookMLParser.COMMA)
            else:
                return self.getToken(LookMLParser.COMMA, i)

        def getRuleIndex(self):
            return LookMLParser.RULE_timeframe_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeframe_list" ):
                listener.enterTimeframe_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeframe_list" ):
                listener.exitTimeframe_list(self)




    def timeframe_list(self):

        localctx = LookMLParser.Timeframe_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_timeframe_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 313
                self.match(LookMLParser.IDENTIFIER)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 314
                    self.match(LookMLParser.COMMA)
                    self.state = 315
                    self.match(LookMLParser.IDENTIFIER)
                    self.state = 320
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





