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
        4,1,27,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,3,3,50,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,5,4,59,8,4,10,4,12,4,62,9,4,1,4,1,4,3,4,66,8,4,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,5,9,
        87,8,9,10,9,12,9,90,9,9,1,9,1,9,3,9,94,8,9,1,10,1,10,3,10,98,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,4,11,107,8,11,11,11,12,11,108,
        1,11,1,11,3,11,113,8,11,1,12,1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,
        8,10,12,14,16,18,20,22,24,0,0,118,0,26,1,0,0,0,2,29,1,0,0,0,4,42,
        1,0,0,0,6,49,1,0,0,0,8,51,1,0,0,0,10,67,1,0,0,0,12,71,1,0,0,0,14,
        76,1,0,0,0,16,80,1,0,0,0,18,82,1,0,0,0,20,95,1,0,0,0,22,99,1,0,0,
        0,24,114,1,0,0,0,26,27,3,2,1,0,27,28,5,0,0,1,28,1,1,0,0,0,29,30,
        5,1,0,0,30,31,5,10,0,0,31,32,5,20,0,0,32,33,5,18,0,0,33,37,3,4,2,
        0,34,36,3,6,3,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,19,0,0,41,3,1,0,0,0,
        42,43,5,2,0,0,43,44,5,10,0,0,44,45,5,21,0,0,45,46,5,12,0,0,46,5,
        1,0,0,0,47,50,3,8,4,0,48,50,3,22,11,0,49,47,1,0,0,0,49,48,1,0,0,
        0,50,7,1,0,0,0,51,52,5,3,0,0,52,53,5,10,0,0,53,54,5,20,0,0,54,60,
        5,18,0,0,55,59,3,10,5,0,56,59,3,12,6,0,57,59,3,14,7,0,58,55,1,0,
        0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,
        1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,65,5,19,0,0,64,66,5,11,0,
        0,65,64,1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,68,5,4,0,0,68,69,5,
        10,0,0,69,70,5,20,0,0,70,11,1,0,0,0,71,72,5,5,0,0,72,73,5,10,0,0,
        73,74,5,24,0,0,74,75,5,12,0,0,75,13,1,0,0,0,76,77,5,6,0,0,77,78,
        5,10,0,0,78,79,3,16,8,0,79,15,1,0,0,0,80,81,5,25,0,0,81,17,1,0,0,
        0,82,83,5,7,0,0,83,84,5,10,0,0,84,88,5,16,0,0,85,87,3,20,10,0,86,
        85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,
        0,90,88,1,0,0,0,91,93,5,17,0,0,92,94,5,11,0,0,93,92,1,0,0,0,93,94,
        1,0,0,0,94,19,1,0,0,0,95,97,5,20,0,0,96,98,5,13,0,0,97,96,1,0,0,
        0,97,98,1,0,0,0,98,21,1,0,0,0,99,100,5,8,0,0,100,101,5,10,0,0,101,
        102,5,20,0,0,102,106,5,18,0,0,103,107,3,10,5,0,104,107,3,12,6,0,
        105,107,3,24,12,0,106,103,1,0,0,0,106,104,1,0,0,0,106,105,1,0,0,
        0,107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,
        0,110,112,5,19,0,0,111,113,5,11,0,0,112,111,1,0,0,0,112,113,1,0,
        0,0,113,23,1,0,0,0,114,115,5,9,0,0,115,116,5,10,0,0,116,117,5,22,
        0,0,117,25,1,0,0,0,11,37,49,58,60,65,88,93,97,106,108,112
    ]

class LookMLParser ( Parser ):

    grammarFileName = "LookMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'view'", "'sql_table_name'", "'dimension'", 
                     "'type'", "'sql'", "'primary_key'", "'timeframes'", 
                     "'measure'", "'value_format'", "':'", "';'", "';;'", 
                     "','", "'('", "')'", "'['", "']'", "'{'", "'}'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'", "<INVALID>", "'yes'" ]

    symbolicNames = [ "<INVALID>", "VIEW", "SQL_TABLE_NAME", "DIMENSION", 
                      "TYPE", "SQL", "PRIMARY_KEY", "TIMEFRAMES", "MEASURE", 
                      "VALUE_FORMAT", "COLON", "SEMICOLON", "DOUBLE_SEMICOLON", 
                      "COMMA", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
                      "LCURLY", "RCURLY", "ID", "SCHEMA_NAME", "STRING", 
                      "DOT", "EXPR", "YES", "WS", "NEWLINE" ]

    RULE_lookml = 0
    RULE_view_def = 1
    RULE_sql_table_name_def = 2
    RULE_field_def = 3
    RULE_dim_def = 4
    RULE_type_def = 5
    RULE_sql_def = 6
    RULE_primary_key_def = 7
    RULE_primary_key_value = 8
    RULE_timeframes_def = 9
    RULE_timeframe = 10
    RULE_measure_def = 11
    RULE_value_format_def = 12

    ruleNames =  [ "lookml", "view_def", "sql_table_name_def", "field_def", 
                   "dim_def", "type_def", "sql_def", "primary_key_def", 
                   "primary_key_value", "timeframes_def", "timeframe", "measure_def", 
                   "value_format_def" ]

    EOF = Token.EOF
    VIEW=1
    SQL_TABLE_NAME=2
    DIMENSION=3
    TYPE=4
    SQL=5
    PRIMARY_KEY=6
    TIMEFRAMES=7
    MEASURE=8
    VALUE_FORMAT=9
    COLON=10
    SEMICOLON=11
    DOUBLE_SEMICOLON=12
    COMMA=13
    LPAREN=14
    RPAREN=15
    LBRACKET=16
    RBRACKET=17
    LCURLY=18
    RCURLY=19
    ID=20
    SCHEMA_NAME=21
    STRING=22
    DOT=23
    EXPR=24
    YES=25
    WS=26
    NEWLINE=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LookmlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def view_def(self):
            return self.getTypedRuleContext(LookMLParser.View_defContext,0)


        def EOF(self):
            return self.getToken(LookMLParser.EOF, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_lookml

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLookml" ):
                listener.enterLookml(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLookml" ):
                listener.exitLookml(self)




    def lookml(self):

        localctx = LookMLParser.LookmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lookml)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.view_def()
            self.state = 27
            self.match(LookMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class View_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIEW(self):
            return self.getToken(LookMLParser.VIEW, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def ID(self):
            return self.getToken(LookMLParser.ID, 0)

        def LCURLY(self):
            return self.getToken(LookMLParser.LCURLY, 0)

        def sql_table_name_def(self):
            return self.getTypedRuleContext(LookMLParser.Sql_table_name_defContext,0)


        def RCURLY(self):
            return self.getToken(LookMLParser.RCURLY, 0)

        def field_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Field_defContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Field_defContext,i)


        def getRuleIndex(self):
            return LookMLParser.RULE_view_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterView_def" ):
                listener.enterView_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitView_def" ):
                listener.exitView_def(self)




    def view_def(self):

        localctx = LookMLParser.View_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_view_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(LookMLParser.VIEW)
            self.state = 30
            self.match(LookMLParser.COLON)
            self.state = 31
            self.match(LookMLParser.ID)
            self.state = 32
            self.match(LookMLParser.LCURLY)
            self.state = 33
            self.sql_table_name_def()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==8:
                self.state = 34
                self.field_def()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(LookMLParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sql_table_name_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQL_TABLE_NAME(self):
            return self.getToken(LookMLParser.SQL_TABLE_NAME, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def SCHEMA_NAME(self):
            return self.getToken(LookMLParser.SCHEMA_NAME, 0)

        def DOUBLE_SEMICOLON(self):
            return self.getToken(LookMLParser.DOUBLE_SEMICOLON, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_sql_table_name_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_table_name_def" ):
                listener.enterSql_table_name_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_table_name_def" ):
                listener.exitSql_table_name_def(self)




    def sql_table_name_def(self):

        localctx = LookMLParser.Sql_table_name_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sql_table_name_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(LookMLParser.SQL_TABLE_NAME)
            self.state = 43
            self.match(LookMLParser.COLON)
            self.state = 44
            self.match(LookMLParser.SCHEMA_NAME)
            self.state = 45
            self.match(LookMLParser.DOUBLE_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim_def(self):
            return self.getTypedRuleContext(LookMLParser.Dim_defContext,0)


        def measure_def(self):
            return self.getTypedRuleContext(LookMLParser.Measure_defContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_field_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_def" ):
                listener.enterField_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_def" ):
                listener.exitField_def(self)




    def field_def(self):

        localctx = LookMLParser.Field_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_field_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 47
                self.dim_def()
                pass
            elif token in [8]:
                self.state = 48
                self.measure_def()
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


    class Dim_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIMENSION(self):
            return self.getToken(LookMLParser.DIMENSION, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def ID(self):
            return self.getToken(LookMLParser.ID, 0)

        def LCURLY(self):
            return self.getToken(LookMLParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(LookMLParser.RCURLY, 0)

        def type_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Type_defContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Type_defContext,i)


        def sql_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Sql_defContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Sql_defContext,i)


        def primary_key_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Primary_key_defContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Primary_key_defContext,i)


        def SEMICOLON(self):
            return self.getToken(LookMLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_dim_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDim_def" ):
                listener.enterDim_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDim_def" ):
                listener.exitDim_def(self)




    def dim_def(self):

        localctx = LookMLParser.Dim_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dim_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(LookMLParser.DIMENSION)
            self.state = 52
            self.match(LookMLParser.COLON)
            self.state = 53
            self.match(LookMLParser.ID)
            self.state = 54
            self.match(LookMLParser.LCURLY)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 58
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 55
                    self.type_def()
                    pass
                elif token in [5]:
                    self.state = 56
                    self.sql_def()
                    pass
                elif token in [6]:
                    self.state = 57
                    self.primary_key_def()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(LookMLParser.RCURLY)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 64
                self.match(LookMLParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(LookMLParser.TYPE, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def ID(self):
            return self.getToken(LookMLParser.ID, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_type_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_def" ):
                listener.enterType_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_def" ):
                listener.exitType_def(self)




    def type_def(self):

        localctx = LookMLParser.Type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(LookMLParser.TYPE)
            self.state = 68
            self.match(LookMLParser.COLON)
            self.state = 69
            self.match(LookMLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sql_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQL(self):
            return self.getToken(LookMLParser.SQL, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def EXPR(self):
            return self.getToken(LookMLParser.EXPR, 0)

        def DOUBLE_SEMICOLON(self):
            return self.getToken(LookMLParser.DOUBLE_SEMICOLON, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_sql_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_def" ):
                listener.enterSql_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_def" ):
                listener.exitSql_def(self)




    def sql_def(self):

        localctx = LookMLParser.Sql_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sql_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(LookMLParser.SQL)
            self.state = 72
            self.match(LookMLParser.COLON)
            self.state = 73
            self.match(LookMLParser.EXPR)
            self.state = 74
            self.match(LookMLParser.DOUBLE_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_key_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMARY_KEY(self):
            return self.getToken(LookMLParser.PRIMARY_KEY, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def primary_key_value(self):
            return self.getTypedRuleContext(LookMLParser.Primary_key_valueContext,0)


        def getRuleIndex(self):
            return LookMLParser.RULE_primary_key_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_key_def" ):
                listener.enterPrimary_key_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_key_def" ):
                listener.exitPrimary_key_def(self)




    def primary_key_def(self):

        localctx = LookMLParser.Primary_key_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primary_key_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(LookMLParser.PRIMARY_KEY)
            self.state = 77
            self.match(LookMLParser.COLON)
            self.state = 78
            self.primary_key_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_key_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def YES(self):
            return self.getToken(LookMLParser.YES, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_primary_key_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_key_value" ):
                listener.enterPrimary_key_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_key_value" ):
                listener.exitPrimary_key_value(self)




    def primary_key_value(self):

        localctx = LookMLParser.Primary_key_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primary_key_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(LookMLParser.YES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Timeframes_defContext(ParserRuleContext):
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

        def RBRACKET(self):
            return self.getToken(LookMLParser.RBRACKET, 0)

        def timeframe(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.TimeframeContext)
            else:
                return self.getTypedRuleContext(LookMLParser.TimeframeContext,i)


        def SEMICOLON(self):
            return self.getToken(LookMLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_timeframes_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeframes_def" ):
                listener.enterTimeframes_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeframes_def" ):
                listener.exitTimeframes_def(self)




    def timeframes_def(self):

        localctx = LookMLParser.Timeframes_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_timeframes_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(LookMLParser.TIMEFRAMES)
            self.state = 83
            self.match(LookMLParser.COLON)
            self.state = 84
            self.match(LookMLParser.LBRACKET)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 85
                self.timeframe()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(LookMLParser.RBRACKET)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 92
                self.match(LookMLParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeframeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LookMLParser.ID, 0)

        def COMMA(self):
            return self.getToken(LookMLParser.COMMA, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_timeframe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeframe" ):
                listener.enterTimeframe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeframe" ):
                listener.exitTimeframe(self)




    def timeframe(self):

        localctx = LookMLParser.TimeframeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_timeframe)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(LookMLParser.ID)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 96
                self.match(LookMLParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Measure_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEASURE(self):
            return self.getToken(LookMLParser.MEASURE, 0)

        def COLON(self):
            return self.getToken(LookMLParser.COLON, 0)

        def ID(self):
            return self.getToken(LookMLParser.ID, 0)

        def LCURLY(self):
            return self.getToken(LookMLParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(LookMLParser.RCURLY, 0)

        def type_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Type_defContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Type_defContext,i)


        def sql_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Sql_defContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Sql_defContext,i)


        def value_format_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LookMLParser.Value_format_defContext)
            else:
                return self.getTypedRuleContext(LookMLParser.Value_format_defContext,i)


        def SEMICOLON(self):
            return self.getToken(LookMLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LookMLParser.RULE_measure_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasure_def" ):
                listener.enterMeasure_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasure_def" ):
                listener.exitMeasure_def(self)




    def measure_def(self):

        localctx = LookMLParser.Measure_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_measure_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(LookMLParser.MEASURE)
            self.state = 100
            self.match(LookMLParser.COLON)
            self.state = 101
            self.match(LookMLParser.ID)
            self.state = 102
            self.match(LookMLParser.LCURLY)
            self.state = 106 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 103
                    self.type_def()
                    pass
                elif token in [5]:
                    self.state = 104
                    self.sql_def()
                    pass
                elif token in [9]:
                    self.state = 105
                    self.value_format_def()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 108 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 560) != 0)):
                    break

            self.state = 110
            self.match(LookMLParser.RCURLY)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 111
                self.match(LookMLParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_format_defContext(ParserRuleContext):
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
            return LookMLParser.RULE_value_format_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_format_def" ):
                listener.enterValue_format_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_format_def" ):
                listener.exitValue_format_def(self)




    def value_format_def(self):

        localctx = LookMLParser.Value_format_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value_format_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(LookMLParser.VALUE_FORMAT)
            self.state = 115
            self.match(LookMLParser.COLON)
            self.state = 116
            self.match(LookMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





