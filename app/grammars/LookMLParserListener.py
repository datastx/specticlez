# Generated from LookMLParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LookMLParser import LookMLParser
else:
    from LookMLParser import LookMLParser

# This class defines a complete listener for a parse tree produced by LookMLParser.
class LookMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by LookMLParser#lookml_file.
    def enterLookml_file(self, ctx:LookMLParser.Lookml_fileContext):
        pass

    # Exit a parse tree produced by LookMLParser#lookml_file.
    def exitLookml_file(self, ctx:LookMLParser.Lookml_fileContext):
        pass


    # Enter a parse tree produced by LookMLParser#model.
    def enterModel(self, ctx:LookMLParser.ModelContext):
        pass

    # Exit a parse tree produced by LookMLParser#model.
    def exitModel(self, ctx:LookMLParser.ModelContext):
        pass


    # Enter a parse tree produced by LookMLParser#view.
    def enterView(self, ctx:LookMLParser.ViewContext):
        pass

    # Exit a parse tree produced by LookMLParser#view.
    def exitView(self, ctx:LookMLParser.ViewContext):
        pass


    # Enter a parse tree produced by LookMLParser#explore.
    def enterExplore(self, ctx:LookMLParser.ExploreContext):
        pass

    # Exit a parse tree produced by LookMLParser#explore.
    def exitExplore(self, ctx:LookMLParser.ExploreContext):
        pass


    # Enter a parse tree produced by LookMLParser#model_property.
    def enterModel_property(self, ctx:LookMLParser.Model_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#model_property.
    def exitModel_property(self, ctx:LookMLParser.Model_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#view_property.
    def enterView_property(self, ctx:LookMLParser.View_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#view_property.
    def exitView_property(self, ctx:LookMLParser.View_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#explore_property.
    def enterExplore_property(self, ctx:LookMLParser.Explore_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#explore_property.
    def exitExplore_property(self, ctx:LookMLParser.Explore_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#sql_table_name_property.
    def enterSql_table_name_property(self, ctx:LookMLParser.Sql_table_name_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#sql_table_name_property.
    def exitSql_table_name_property(self, ctx:LookMLParser.Sql_table_name_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#explore_view_name.
    def enterExplore_view_name(self, ctx:LookMLParser.Explore_view_nameContext):
        pass

    # Exit a parse tree produced by LookMLParser#explore_view_name.
    def exitExplore_view_name(self, ctx:LookMLParser.Explore_view_nameContext):
        pass


    # Enter a parse tree produced by LookMLParser#join.
    def enterJoin(self, ctx:LookMLParser.JoinContext):
        pass

    # Exit a parse tree produced by LookMLParser#join.
    def exitJoin(self, ctx:LookMLParser.JoinContext):
        pass


    # Enter a parse tree produced by LookMLParser#derived_table.
    def enterDerived_table(self, ctx:LookMLParser.Derived_tableContext):
        pass

    # Exit a parse tree produced by LookMLParser#derived_table.
    def exitDerived_table(self, ctx:LookMLParser.Derived_tableContext):
        pass


    # Enter a parse tree produced by LookMLParser#relationship.
    def enterRelationship(self, ctx:LookMLParser.RelationshipContext):
        pass

    # Exit a parse tree produced by LookMLParser#relationship.
    def exitRelationship(self, ctx:LookMLParser.RelationshipContext):
        pass


    # Enter a parse tree produced by LookMLParser#link.
    def enterLink(self, ctx:LookMLParser.LinkContext):
        pass

    # Exit a parse tree produced by LookMLParser#link.
    def exitLink(self, ctx:LookMLParser.LinkContext):
        pass


    # Enter a parse tree produced by LookMLParser#join_property.
    def enterJoin_property(self, ctx:LookMLParser.Join_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#join_property.
    def exitJoin_property(self, ctx:LookMLParser.Join_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#derived_table_property.
    def enterDerived_table_property(self, ctx:LookMLParser.Derived_table_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#derived_table_property.
    def exitDerived_table_property(self, ctx:LookMLParser.Derived_table_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#dimension.
    def enterDimension(self, ctx:LookMLParser.DimensionContext):
        pass

    # Exit a parse tree produced by LookMLParser#dimension.
    def exitDimension(self, ctx:LookMLParser.DimensionContext):
        pass


    # Enter a parse tree produced by LookMLParser#dimension_group.
    def enterDimension_group(self, ctx:LookMLParser.Dimension_groupContext):
        pass

    # Exit a parse tree produced by LookMLParser#dimension_group.
    def exitDimension_group(self, ctx:LookMLParser.Dimension_groupContext):
        pass


    # Enter a parse tree produced by LookMLParser#measure.
    def enterMeasure(self, ctx:LookMLParser.MeasureContext):
        pass

    # Exit a parse tree produced by LookMLParser#measure.
    def exitMeasure(self, ctx:LookMLParser.MeasureContext):
        pass


    # Enter a parse tree produced by LookMLParser#filter.
    def enterFilter(self, ctx:LookMLParser.FilterContext):
        pass

    # Exit a parse tree produced by LookMLParser#filter.
    def exitFilter(self, ctx:LookMLParser.FilterContext):
        pass


    # Enter a parse tree produced by LookMLParser#parameter.
    def enterParameter(self, ctx:LookMLParser.ParameterContext):
        pass

    # Exit a parse tree produced by LookMLParser#parameter.
    def exitParameter(self, ctx:LookMLParser.ParameterContext):
        pass


    # Enter a parse tree produced by LookMLParser#dimension_property.
    def enterDimension_property(self, ctx:LookMLParser.Dimension_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#dimension_property.
    def exitDimension_property(self, ctx:LookMLParser.Dimension_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#dimension_group_property.
    def enterDimension_group_property(self, ctx:LookMLParser.Dimension_group_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#dimension_group_property.
    def exitDimension_group_property(self, ctx:LookMLParser.Dimension_group_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#measure_property.
    def enterMeasure_property(self, ctx:LookMLParser.Measure_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#measure_property.
    def exitMeasure_property(self, ctx:LookMLParser.Measure_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#filter_property.
    def enterFilter_property(self, ctx:LookMLParser.Filter_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#filter_property.
    def exitFilter_property(self, ctx:LookMLParser.Filter_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#parameter_property.
    def enterParameter_property(self, ctx:LookMLParser.Parameter_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#parameter_property.
    def exitParameter_property(self, ctx:LookMLParser.Parameter_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#type_property.
    def enterType_property(self, ctx:LookMLParser.Type_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#type_property.
    def exitType_property(self, ctx:LookMLParser.Type_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#sql_property.
    def enterSql_property(self, ctx:LookMLParser.Sql_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#sql_property.
    def exitSql_property(self, ctx:LookMLParser.Sql_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#primary_key_property.
    def enterPrimary_key_property(self, ctx:LookMLParser.Primary_key_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#primary_key_property.
    def exitPrimary_key_property(self, ctx:LookMLParser.Primary_key_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#allowed_value_property.
    def enterAllowed_value_property(self, ctx:LookMLParser.Allowed_value_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#allowed_value_property.
    def exitAllowed_value_property(self, ctx:LookMLParser.Allowed_value_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#timeframes_property.
    def enterTimeframes_property(self, ctx:LookMLParser.Timeframes_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#timeframes_property.
    def exitTimeframes_property(self, ctx:LookMLParser.Timeframes_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#value_format_property.
    def enterValue_format_property(self, ctx:LookMLParser.Value_format_propertyContext):
        pass

    # Exit a parse tree produced by LookMLParser#value_format_property.
    def exitValue_format_property(self, ctx:LookMLParser.Value_format_propertyContext):
        pass


    # Enter a parse tree produced by LookMLParser#allowed_value_list.
    def enterAllowed_value_list(self, ctx:LookMLParser.Allowed_value_listContext):
        pass

    # Exit a parse tree produced by LookMLParser#allowed_value_list.
    def exitAllowed_value_list(self, ctx:LookMLParser.Allowed_value_listContext):
        pass


    # Enter a parse tree produced by LookMLParser#timeframe_list.
    def enterTimeframe_list(self, ctx:LookMLParser.Timeframe_listContext):
        pass

    # Exit a parse tree produced by LookMLParser#timeframe_list.
    def exitTimeframe_list(self, ctx:LookMLParser.Timeframe_listContext):
        pass



del LookMLParser