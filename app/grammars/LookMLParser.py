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
        4,1,40,317,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,5,
        0,68,8,0,10,0,12,0,71,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,80,8,1,
        10,1,12,1,83,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,92,8,2,10,2,12,
        2,95,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,104,8,3,10,3,12,3,107,9,
        3,1,3,1,3,1,4,1,4,3,4,113,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,121,8,
        5,1,6,1,6,1,6,1,6,3,6,127,8,6,1,7,1,7,1,7,1,7,1,7,3,7,134,8,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,143,8,8,10,8,12,8,146,9,8,1,8,1,8,
        1,9,1,9,1,9,5,9,153,8,9,10,9,12,9,156,9,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,5,14,181,8,14,10,14,12,14,184,9,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,5,15,193,8,15,10,15,12,15,196,9,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,5,16,205,8,16,10,16,12,16,208,
        9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,5,17,217,8,17,10,17,12,17,
        220,9,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,5,18,229,8,18,10,18,
        12,18,232,9,18,1,18,1,18,1,19,1,19,1,19,1,19,3,19,240,8,19,1,20,
        1,20,1,20,3,20,245,8,20,1,21,1,21,1,21,3,21,250,8,21,1,22,1,22,3,
        22,254,8,22,1,23,1,23,1,23,3,23,259,8,23,1,24,1,24,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,
        1,29,1,29,1,30,1,30,1,30,1,30,5,30,298,8,30,10,30,12,30,301,9,30,
        3,30,303,8,30,1,30,1,30,1,31,1,31,1,31,5,31,310,8,31,10,31,12,31,
        313,9,31,3,31,315,8,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,0,
        321,0,69,1,0,0,0,2,74,1,0,0,0,4,86,1,0,0,0,6,98,1,0,0,0,8,112,1,
        0,0,0,10,120,1,0,0,0,12,126,1,0,0,0,14,128,1,0,0,0,16,138,1,0,0,
        0,18,149,1,0,0,0,20,159,1,0,0,0,22,163,1,0,0,0,24,167,1,0,0,0,26,
        171,1,0,0,0,28,175,1,0,0,0,30,187,1,0,0,0,32,199,1,0,0,0,34,211,
        1,0,0,0,36,223,1,0,0,0,38,239,1,0,0,0,40,244,1,0,0,0,42,249,1,0,
        0,0,44,253,1,0,0,0,46,258,1,0,0,0,48,260,1,0,0,0,50,264,1,0,0,0,
        52,275,1,0,0,0,54,279,1,0,0,0,56,283,1,0,0,0,58,289,1,0,0,0,60,293,
        1,0,0,0,62,314,1,0,0,0,64,68,3,2,1,0,65,68,3,4,2,0,66,68,3,6,3,0,
        67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,
        0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,0,0,1,73,
        1,1,0,0,0,74,75,5,2,0,0,75,76,5,29,0,0,76,77,5,35,0,0,77,81,5,25,
        0,0,78,80,3,8,4,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,
        1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,26,0,0,85,3,1,0,0,0,
        86,87,5,3,0,0,87,88,5,29,0,0,88,89,5,35,0,0,89,93,5,25,0,0,90,92,
        3,10,5,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,
        94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,26,0,0,97,5,1,0,0,0,98,99,5,
        9,0,0,99,100,5,29,0,0,100,101,5,35,0,0,101,105,5,25,0,0,102,104,
        3,12,6,0,103,102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,
        1,0,0,0,106,108,1,0,0,0,107,105,1,0,0,0,108,109,5,26,0,0,109,7,1,
        0,0,0,110,113,3,16,8,0,111,113,3,18,9,0,112,110,1,0,0,0,112,111,
        1,0,0,0,113,9,1,0,0,0,114,121,3,14,7,0,115,121,3,28,14,0,116,121,
        3,30,15,0,117,121,3,32,16,0,118,121,3,34,17,0,119,121,3,36,18,0,
        120,114,1,0,0,0,120,115,1,0,0,0,120,116,1,0,0,0,120,117,1,0,0,0,
        120,118,1,0,0,0,120,119,1,0,0,0,121,11,1,0,0,0,122,127,3,16,8,0,
        123,127,3,18,9,0,124,127,3,20,10,0,125,127,3,22,11,0,126,122,1,0,
        0,0,126,123,1,0,0,0,126,124,1,0,0,0,126,125,1,0,0,0,127,13,1,0,0,
        0,128,129,5,20,0,0,129,130,5,29,0,0,130,133,5,35,0,0,131,132,5,32,
        0,0,132,134,5,35,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,135,1,0,
        0,0,135,136,5,31,0,0,136,137,5,31,0,0,137,15,1,0,0,0,138,139,5,10,
        0,0,139,140,5,35,0,0,140,144,5,25,0,0,141,143,3,24,12,0,142,141,
        1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,147,
        1,0,0,0,146,144,1,0,0,0,147,148,5,26,0,0,148,17,1,0,0,0,149,150,
        5,15,0,0,150,154,5,25,0,0,151,153,3,26,13,0,152,151,1,0,0,0,153,
        156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,
        154,1,0,0,0,157,158,5,26,0,0,158,19,1,0,0,0,159,160,5,16,0,0,160,
        161,5,29,0,0,161,162,5,35,0,0,162,21,1,0,0,0,163,164,5,18,0,0,164,
        165,5,29,0,0,165,166,5,37,0,0,166,23,1,0,0,0,167,168,5,11,0,0,168,
        169,5,29,0,0,169,170,5,37,0,0,170,25,1,0,0,0,171,172,5,11,0,0,172,
        173,5,29,0,0,173,174,5,37,0,0,174,27,1,0,0,0,175,176,5,4,0,0,176,
        177,5,29,0,0,177,178,5,35,0,0,178,182,5,25,0,0,179,181,3,38,19,0,
        180,179,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,
        183,185,1,0,0,0,184,182,1,0,0,0,185,186,5,26,0,0,186,29,1,0,0,0,
        187,188,5,5,0,0,188,189,5,29,0,0,189,190,5,35,0,0,190,194,5,25,0,
        0,191,193,3,40,20,0,192,191,1,0,0,0,193,196,1,0,0,0,194,192,1,0,
        0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,194,1,0,0,0,197,198,5,26,
        0,0,198,31,1,0,0,0,199,200,5,6,0,0,200,201,5,29,0,0,201,202,5,35,
        0,0,202,206,5,25,0,0,203,205,3,42,21,0,204,203,1,0,0,0,205,208,1,
        0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,206,1,
        0,0,0,209,210,5,26,0,0,210,33,1,0,0,0,211,212,5,7,0,0,212,213,5,
        29,0,0,213,214,5,35,0,0,214,218,5,25,0,0,215,217,3,44,22,0,216,215,
        1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,
        1,0,0,0,220,218,1,0,0,0,221,222,5,26,0,0,222,35,1,0,0,0,223,224,
        5,8,0,0,224,225,5,29,0,0,225,226,5,35,0,0,226,230,5,25,0,0,227,229,
        3,46,23,0,228,227,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,
        1,0,0,0,231,233,1,0,0,0,232,230,1,0,0,0,233,234,5,26,0,0,234,37,
        1,0,0,0,235,240,3,48,24,0,236,240,3,50,25,0,237,240,3,52,26,0,238,
        240,3,56,28,0,239,235,1,0,0,0,239,236,1,0,0,0,239,237,1,0,0,0,239,
        238,1,0,0,0,240,39,1,0,0,0,241,245,3,48,24,0,242,245,3,50,25,0,243,
        245,3,56,28,0,244,241,1,0,0,0,244,242,1,0,0,0,244,243,1,0,0,0,245,
        41,1,0,0,0,246,250,3,48,24,0,247,250,3,50,25,0,248,250,3,58,29,0,
        249,246,1,0,0,0,249,247,1,0,0,0,249,248,1,0,0,0,250,43,1,0,0,0,251,
        254,3,48,24,0,252,254,3,50,25,0,253,251,1,0,0,0,253,252,1,0,0,0,
        254,45,1,0,0,0,255,259,3,48,24,0,256,259,3,50,25,0,257,259,3,54,
        27,0,258,255,1,0,0,0,258,256,1,0,0,0,258,257,1,0,0,0,259,47,1,0,
        0,0,260,261,5,13,0,0,261,262,5,29,0,0,262,263,5,35,0,0,263,49,1,
        0,0,0,264,265,5,11,0,0,265,266,5,29,0,0,266,267,5,38,0,0,267,268,
        5,25,0,0,268,269,5,35,0,0,269,270,5,26,0,0,270,271,5,32,0,0,271,
        272,5,35,0,0,272,273,5,31,0,0,273,274,5,31,0,0,274,51,1,0,0,0,275,
        276,5,14,0,0,276,277,5,29,0,0,277,278,5,35,0,0,278,53,1,0,0,0,279,
        280,5,19,0,0,280,281,5,29,0,0,281,282,3,60,30,0,282,55,1,0,0,0,283,
        284,5,21,0,0,284,285,5,29,0,0,285,286,5,27,0,0,286,287,3,62,31,0,
        287,288,5,28,0,0,288,57,1,0,0,0,289,290,5,22,0,0,290,291,5,29,0,
        0,291,292,5,37,0,0,292,59,1,0,0,0,293,302,5,23,0,0,294,299,5,37,
        0,0,295,296,5,30,0,0,296,298,5,37,0,0,297,295,1,0,0,0,298,301,1,
        0,0,0,299,297,1,0,0,0,299,300,1,0,0,0,300,303,1,0,0,0,301,299,1,
        0,0,0,302,294,1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,305,5,
        24,0,0,305,61,1,0,0,0,306,311,5,35,0,0,307,308,5,30,0,0,308,310,
        5,35,0,0,309,307,1,0,0,0,310,313,1,0,0,0,311,309,1,0,0,0,311,312,
        1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,314,306,1,0,0,0,314,315,
        1,0,0,0,315,63,1,0,0,0,25,67,69,81,93,105,112,120,126,133,144,154,
        182,194,206,218,230,239,244,249,253,258,299,302,311,314
    ]

class LookMLParser ( Parser ):

    grammarFileName = "LookMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'looker'", "'model'", "'view'", "'dimension'", 
                     "'dimension_group'", "'measure'", "'filter'", "'parameter'", 
                     "'explore'", "'join'", "'sql'", "'alias'", "'type'", 
                     "'primary_key'", "'derived_table'", "'relationship'", 
                     "'required'", "'link'", "'allowed_values'", "'sql_table_name'", 
                     "'timeframes'", "'value_format'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "':'", "','", "';'", "'.'", "'='", 
                     "'|'", "<INVALID>", "<INVALID>", "<INVALID>", "'$'" ]

    symbolicNames = [ "<INVALID>", "LOOKER", "MODEL", "VIEW", "DIMENSION", 
                      "DIMENSION_GROUP", "MEASURE", "FILTER", "PARAMETER", 
                      "EXPLORE", "JOIN", "SQL", "ALIAS", "TYPE", "PRIMARY_KEY", 
                      "DERIVED_TABLE", "RELATIONSHIP", "REQUIRED", "LINK", 
                      "ALLOWED_VALUES", "SQL_TABLE_NAME", "TIMEFRAMES", 
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
    RULE_join = 8
    RULE_derived_table = 9
    RULE_relationship = 10
    RULE_link = 11
    RULE_join_property = 12
    RULE_derived_table_property = 13
    RULE_dimension = 14
    RULE_dimension_group = 15
    RULE_measure = 16
    RULE_filter = 17
    RULE_parameter = 18
    RULE_dimension_property = 19
    RULE_dimension_group_property = 20
    RULE_measure_property = 21
    RULE_filter_property = 22
    RULE_parameter_property = 23
    RULE_type_property = 24
    RULE_sql_property = 25
    RULE_primary_key_property = 26
    RULE_allowed_value_property = 27
    RULE_timeframes_property = 28
    RULE_value_format_property = 29
    RULE_allowed_value_list = 30
    RULE_timeframe_list = 31

    ruleNames =  [ "lookml_file", "model", "view", "explore", "model_property", 
                   "view_property", "explore_property", "sql_table_name_property", 
                   "join", "derived_table", "relationship", "link", "join_property", 
                   "derived_table_property", "dimension", "dimension_group", 
                   "measure", "filter", "parameter", "dimension_property", 
                   "dimension_group_property", "measure_property", "filter_property", 
                   "parameter_property", "type_property", "sql_property", 
                   "primary_key_property", "allowed_value_property", "timeframes_property", 
                   "value_format_property", "allowed_value_list", "timeframe_list" ]

    EOF = Token.EOF
    LOOKER=1
    MODEL=2
    VIEW=3
    DIMENSION=4
    DIMENSION_GROUP=5
    MEASURE=6
    FILTER=7
    PARAMETER=8
    EXPLORE=9
    JOIN=10
    SQL=11
    ALIAS=12
    TYPE=13
    PRIMARY_KEY=14
    DERIVED_TABLE=15
    RELATIONSHIP=16
    REQUIRED=17
    LINK=18
    ALLOWED_VALUES=19
    SQL_TABLE_NAME=20
    TIMEFRAMES=21
    VALUE_FORMAT=22
    LPAREN=23
    RPAREN=24
    LBRACE=25
    RBRACE=26
    LBRACKET=27
    RBRACKET=28
    COLON=29
    COMMA=30
    SEMI=31
    DOT=32
    EQ=33
    PIPE=34
    IDENTIFIER=35
    NUMBER=36
    STRING=37
    DOLLAR=38
    COMMENT=39
    WS=40

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
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 524) != 0):
                self.state = 67
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 64
                    self.model()
                    pass
                elif token in [3]:
                    self.state = 65
                    self.view()
                    pass
                elif token in [9]:
                    self.state = 66
                    self.explore()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
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
            self.state = 74
            self.match(LookMLParser.MODEL)
            self.state = 75
            self.match(LookMLParser.COLON)
            self.state = 76
            self.match(LookMLParser.IDENTIFIER)
            self.state = 77
            self.match(LookMLParser.LBRACE)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==15:
                self.state = 78
                self.model_property()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
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
            self.state = 86
            self.match(LookMLParser.VIEW)
            self.state = 87
            self.match(LookMLParser.COLON)
            self.state = 88
            self.match(LookMLParser.IDENTIFIER)
            self.state = 89
            self.match(LookMLParser.LBRACE)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1049072) != 0):
                self.state = 90
                self.view_property()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
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
            self.state = 98
            self.match(LookMLParser.EXPLORE)
            self.state = 99
            self.match(LookMLParser.COLON)
            self.state = 100
            self.match(LookMLParser.IDENTIFIER)
            self.state = 101
            self.match(LookMLParser.LBRACE)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 361472) != 0):
                self.state = 102
                self.explore_property()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
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
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 110
                self.join()
                pass
            elif token in [15]:
                self.state = 111
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
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 114
                self.sql_table_name_property()
                pass
            elif token in [4]:
                self.state = 115
                self.dimension()
                pass
            elif token in [5]:
                self.state = 116
                self.dimension_group()
                pass
            elif token in [6]:
                self.state = 117
                self.measure()
                pass
            elif token in [7]:
                self.state = 118
                self.filter_()
                pass
            elif token in [8]:
                self.state = 119
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
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 122
                self.join()
                pass
            elif token in [15]:
                self.state = 123
                self.derived_table()
                pass
            elif token in [16]:
                self.state = 124
                self.relationship()
                pass
            elif token in [18]:
                self.state = 125
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
            self.state = 128
            self.match(LookMLParser.SQL_TABLE_NAME)
            self.state = 129
            self.match(LookMLParser.COLON)
            self.state = 130
            self.match(LookMLParser.IDENTIFIER)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 131
                self.match(LookMLParser.DOT)
                self.state = 132
                self.match(LookMLParser.IDENTIFIER)


            self.state = 135
            self.match(LookMLParser.SEMI)
            self.state = 136
            self.match(LookMLParser.SEMI)
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
        self.enterRule(localctx, 16, self.RULE_join)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(LookMLParser.JOIN)
            self.state = 139
            self.match(LookMLParser.IDENTIFIER)
            self.state = 140
            self.match(LookMLParser.LBRACE)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 141
                self.join_property()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
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
        self.enterRule(localctx, 18, self.RULE_derived_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(LookMLParser.DERIVED_TABLE)
            self.state = 150
            self.match(LookMLParser.LBRACE)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 151
                self.derived_table_property()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
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
        self.enterRule(localctx, 20, self.RULE_relationship)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(LookMLParser.RELATIONSHIP)
            self.state = 160
            self.match(LookMLParser.COLON)
            self.state = 161
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
        self.enterRule(localctx, 22, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(LookMLParser.LINK)
            self.state = 164
            self.match(LookMLParser.COLON)
            self.state = 165
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
        self.enterRule(localctx, 24, self.RULE_join_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(LookMLParser.SQL)
            self.state = 168
            self.match(LookMLParser.COLON)
            self.state = 169
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
        self.enterRule(localctx, 26, self.RULE_derived_table_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(LookMLParser.SQL)
            self.state = 172
            self.match(LookMLParser.COLON)
            self.state = 173
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
        self.enterRule(localctx, 28, self.RULE_dimension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(LookMLParser.DIMENSION)
            self.state = 176
            self.match(LookMLParser.COLON)
            self.state = 177
            self.match(LookMLParser.IDENTIFIER)
            self.state = 178
            self.match(LookMLParser.LBRACE)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2123776) != 0):
                self.state = 179
                self.dimension_property()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
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
        self.enterRule(localctx, 30, self.RULE_dimension_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(LookMLParser.DIMENSION_GROUP)
            self.state = 188
            self.match(LookMLParser.COLON)
            self.state = 189
            self.match(LookMLParser.IDENTIFIER)
            self.state = 190
            self.match(LookMLParser.LBRACE)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2107392) != 0):
                self.state = 191
                self.dimension_group_property()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
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
        self.enterRule(localctx, 32, self.RULE_measure)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(LookMLParser.MEASURE)
            self.state = 200
            self.match(LookMLParser.COLON)
            self.state = 201
            self.match(LookMLParser.IDENTIFIER)
            self.state = 202
            self.match(LookMLParser.LBRACE)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4204544) != 0):
                self.state = 203
                self.measure_property()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
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
        self.enterRule(localctx, 34, self.RULE_filter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(LookMLParser.FILTER)
            self.state = 212
            self.match(LookMLParser.COLON)
            self.state = 213
            self.match(LookMLParser.IDENTIFIER)
            self.state = 214
            self.match(LookMLParser.LBRACE)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==13:
                self.state = 215
                self.filter_property()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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
        self.enterRule(localctx, 36, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(LookMLParser.PARAMETER)
            self.state = 224
            self.match(LookMLParser.COLON)
            self.state = 225
            self.match(LookMLParser.IDENTIFIER)
            self.state = 226
            self.match(LookMLParser.LBRACE)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 534528) != 0):
                self.state = 227
                self.parameter_property()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
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
        self.enterRule(localctx, 38, self.RULE_dimension_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 235
                self.type_property()
                pass
            elif token in [11]:
                self.state = 236
                self.sql_property()
                pass
            elif token in [14]:
                self.state = 237
                self.primary_key_property()
                pass
            elif token in [21]:
                self.state = 238
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
        self.enterRule(localctx, 40, self.RULE_dimension_group_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 241
                self.type_property()
                pass
            elif token in [11]:
                self.state = 242
                self.sql_property()
                pass
            elif token in [21]:
                self.state = 243
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
        self.enterRule(localctx, 42, self.RULE_measure_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 246
                self.type_property()
                pass
            elif token in [11]:
                self.state = 247
                self.sql_property()
                pass
            elif token in [22]:
                self.state = 248
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
        self.enterRule(localctx, 44, self.RULE_filter_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 251
                self.type_property()
                pass
            elif token in [11]:
                self.state = 252
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
        self.enterRule(localctx, 46, self.RULE_parameter_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 255
                self.type_property()
                pass
            elif token in [11]:
                self.state = 256
                self.sql_property()
                pass
            elif token in [19]:
                self.state = 257
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
        self.enterRule(localctx, 48, self.RULE_type_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(LookMLParser.TYPE)
            self.state = 261
            self.match(LookMLParser.COLON)
            self.state = 262
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
        self.enterRule(localctx, 50, self.RULE_sql_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(LookMLParser.SQL)
            self.state = 265
            self.match(LookMLParser.COLON)
            self.state = 266
            self.match(LookMLParser.DOLLAR)
            self.state = 267
            self.match(LookMLParser.LBRACE)
            self.state = 268
            self.match(LookMLParser.IDENTIFIER)
            self.state = 269
            self.match(LookMLParser.RBRACE)
            self.state = 270
            self.match(LookMLParser.DOT)
            self.state = 271
            self.match(LookMLParser.IDENTIFIER)
            self.state = 272
            self.match(LookMLParser.SEMI)
            self.state = 273
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
        self.enterRule(localctx, 52, self.RULE_primary_key_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(LookMLParser.PRIMARY_KEY)
            self.state = 276
            self.match(LookMLParser.COLON)
            self.state = 277
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
        self.enterRule(localctx, 54, self.RULE_allowed_value_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(LookMLParser.ALLOWED_VALUES)
            self.state = 280
            self.match(LookMLParser.COLON)
            self.state = 281
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
        self.enterRule(localctx, 56, self.RULE_timeframes_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(LookMLParser.TIMEFRAMES)
            self.state = 284
            self.match(LookMLParser.COLON)
            self.state = 285
            self.match(LookMLParser.LBRACKET)
            self.state = 286
            self.timeframe_list()
            self.state = 287
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
        self.enterRule(localctx, 58, self.RULE_value_format_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(LookMLParser.VALUE_FORMAT)
            self.state = 290
            self.match(LookMLParser.COLON)
            self.state = 291
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
        self.enterRule(localctx, 60, self.RULE_allowed_value_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(LookMLParser.LPAREN)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 294
                self.match(LookMLParser.STRING)
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 295
                    self.match(LookMLParser.COMMA)
                    self.state = 296
                    self.match(LookMLParser.STRING)
                    self.state = 301
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 304
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
        self.enterRule(localctx, 62, self.RULE_timeframe_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 306
                self.match(LookMLParser.IDENTIFIER)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 307
                    self.match(LookMLParser.COMMA)
                    self.state = 308
                    self.match(LookMLParser.IDENTIFIER)
                    self.state = 313
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





