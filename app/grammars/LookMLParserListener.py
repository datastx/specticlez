# Generated from LookMLParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LookMLParser import LookMLParser
else:
    from LookMLParser import LookMLParser

# This class defines a complete listener for a parse tree produced by LookMLParser.
class LookMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by LookMLParser#lookml.
    def enterLookml(self, ctx:LookMLParser.LookmlContext):
        pass

    # Exit a parse tree produced by LookMLParser#lookml.
    def exitLookml(self, ctx:LookMLParser.LookmlContext):
        pass


    # Enter a parse tree produced by LookMLParser#view_def.
    def enterView_def(self, ctx:LookMLParser.View_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#view_def.
    def exitView_def(self, ctx:LookMLParser.View_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#sql_table_name_def.
    def enterSql_table_name_def(self, ctx:LookMLParser.Sql_table_name_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#sql_table_name_def.
    def exitSql_table_name_def(self, ctx:LookMLParser.Sql_table_name_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#field_def.
    def enterField_def(self, ctx:LookMLParser.Field_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#field_def.
    def exitField_def(self, ctx:LookMLParser.Field_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#dim_def.
    def enterDim_def(self, ctx:LookMLParser.Dim_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#dim_def.
    def exitDim_def(self, ctx:LookMLParser.Dim_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#type_def.
    def enterType_def(self, ctx:LookMLParser.Type_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#type_def.
    def exitType_def(self, ctx:LookMLParser.Type_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#sql_def.
    def enterSql_def(self, ctx:LookMLParser.Sql_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#sql_def.
    def exitSql_def(self, ctx:LookMLParser.Sql_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#primary_key_def.
    def enterPrimary_key_def(self, ctx:LookMLParser.Primary_key_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#primary_key_def.
    def exitPrimary_key_def(self, ctx:LookMLParser.Primary_key_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#primary_key_value.
    def enterPrimary_key_value(self, ctx:LookMLParser.Primary_key_valueContext):
        pass

    # Exit a parse tree produced by LookMLParser#primary_key_value.
    def exitPrimary_key_value(self, ctx:LookMLParser.Primary_key_valueContext):
        pass


    # Enter a parse tree produced by LookMLParser#timeframes_def.
    def enterTimeframes_def(self, ctx:LookMLParser.Timeframes_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#timeframes_def.
    def exitTimeframes_def(self, ctx:LookMLParser.Timeframes_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#timeframe.
    def enterTimeframe(self, ctx:LookMLParser.TimeframeContext):
        pass

    # Exit a parse tree produced by LookMLParser#timeframe.
    def exitTimeframe(self, ctx:LookMLParser.TimeframeContext):
        pass


    # Enter a parse tree produced by LookMLParser#measure_def.
    def enterMeasure_def(self, ctx:LookMLParser.Measure_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#measure_def.
    def exitMeasure_def(self, ctx:LookMLParser.Measure_defContext):
        pass


    # Enter a parse tree produced by LookMLParser#value_format_def.
    def enterValue_format_def(self, ctx:LookMLParser.Value_format_defContext):
        pass

    # Exit a parse tree produced by LookMLParser#value_format_def.
    def exitValue_format_def(self, ctx:LookMLParser.Value_format_defContext):
        pass



del LookMLParser