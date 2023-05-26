parser grammar LookMLParser;

options { tokenVocab=LookMLLexer; }

// LookML file block structure
lookml_file: (explore_block | include_property | model_block | test_block | view_block)* EOF;

// Main blocks
explore_block: EXPLORE COLON IDENTIFIER LBRACE explore_properties* RBRACE;
model_block: MODEL COLON IDENTIFIER LBRACE model_properties* RBRACE;
test_block: TEST COLON IDENTIFIER LBRACE test_properties* RBRACE;
view_block: VIEW COLON IDENTIFIER LBRACE view_properties* RBRACE;

// Sub blocks based on main or sub blocks
access_filter_block: ACCESS_FILTER COLON LBRACE access_filter_properties* RBRACE;
action_block: ACTION COLON LBRACE action_properties* RBRACE;
action_param_block: PARAM COLON LBRACE action_param_properties* RBRACE;
action_form_block: FORM_PARAM COLON LBRACE action_form_param_properties* RBRACE;
action_form_param_option_block: OPTION COLON LBRACE action_form_option_properties* RBRACE;
action_user_attribute_param_block: USER_ATTRIBUTE_PARAM COLON LBRACE action_user_attribute_param_properties* RBRACE;
aggregate_table_block: AGGREGATE_TABLE COLON IDENTIFIER LBRACE aggregate_table_properties* RBRACE;
aggregate_table_materilization_block: MATERIALIZATION COLON LBRACE aggregate_table_materilization_properties* RBRACE;
aggregate_table_query_block: QUERY COLON LBRACE aggregate_table_query_properties* RBRACE;
always_filter_block: ALWAYS_FILTER COLON LBRACE always_filter_properties* RBRACE;
assert_block: ASSERT COLON IDENTIFIER LBRACE assert_properties* RBRACE;
case_block: CASE COLON LBRACE case_properties* RBRACE;
column_block: COLUMN COLON IDENTIFIER LBRACE column_properties* RBRACE;
conditionally_filter_block: CONDITIONALLY_FILTER COLON LBRACE conditionally_filter_properties* RBRACE;
dimension_block: DIMENSION COLON IDENTIFIER LBRACE dimension_properties* RBRACE;
dimension_group_block: DIMENSION_GROUP COLON IDENTIFIER LBRACE dimension_group_properties* RBRACE;
explore_source_block: EXPLORE_SOURCE COLON IDENTIFIER LBRACE explore_source_properties* RBRACE;
filter_block: FILTER COLON IDENTIFIER LBRACE filter_properties* RBRACE;
join_block: JOIN COLON IDENTIFIER LBRACE join_properties* RBRACE;
link_block: LINK COLON LBRACE link_properties* RBRACE;
measure_block: MEASURE COLON IDENTIFIER LBRACE measure_properties* RBRACE;
parameter_block: PARAMETER COLON IDENTIFIER LBRACE parameter_properties* RBRACE;
query_block: QUERY COLON IDENTIFIER LBRACE query_properties* RBRACE;
when_block: WHEN COLON LBRACE when_properties* RBRACE;

// Properties
access_filter_properties: (field_property | user_attribute_property);
action_properties: (action_user_attribute_param_block |  action_param_block | action_form_block | label_property | form_url_property | icon_url_property | url_property);
action_form_param_properties: (description_property | default_property | required_property | name_property | action_form_param_option_block | type_action_form_param_property | label_property);
action_param_properties: (name_property | value_property);
action_form_option_properties: (name_property | label_property);
action_user_attribute_param_properties: ( user_attribute_property | name_property);
aggregate_table_properties: (aggregate_table_query_block | aggregate_table_materilization_block);
aggregate_table_materilization_properties: (datagroup_trigger_property);
aggregate_table_query_properties: (dimensions_property | filters_property | measures_property | timeframes_property);
always_filter_properties: (filters_property);
assert_properties: (expression_property);
case_properties: (when_block | else_property);
column_properties: (field_property);
conditionally_filter_properties: (filters_property | unless_property);
dimension_group_properties: (type_view_property | sql_property | timeframes_property);
dimension_properties: ( end_location_field_property | html_property | case_block | required_fields_property |required_access_grants_property |  required_access_grants_property |  primary_key_property | fanout_on_property | primary_key_property | data_type_property | convert_tz_property | bypass_suggest_restrictions_property | full_suggestions_property| suggest_dimension_property | suggest_explore_property | suggest_persist_for_property | suggestable_property | suggestions_property |   case_sensitive_property | can_filter_property |  view_label_property |style_property | order_by_field_property | hidden_property | label_property | label_from_parameter_property | group_item_label_property | group_label_property | description_property | alpha_sort_proptery | alias_property | link_block | tags_property | drill_fields_property | action_block  | type_view_property | sql_property | primary_key_property | timeframes_property);
explore_properties: (access_filter_block | aggregate_table_block | always_filter_block | always_join_property | case_sensitive_property | cancel_grouping_fields_property | conditionally_filter_block | description_property | extension_property | extends_property | fields_property | final_property | from_property | group_label_property | hidden_property | join_block | label_property | link_property | persist_for_property | persist_with_property | query_block | relationship_property | required_access_grants_property | required_joins_property | sql_on_property | sql_table_name_property | symmetric_aggregates_property | tags_property | type_view_property | view_label_property | view_name_property);
explore_source_properties: (column_block | filters_test_property);
filter_properties: (type_view_property | sql_property);
join_properties: (fields_property | foreign_key_property | from_property | outer_only_property | relationship_property | required_access_grants_property | required_joins_property | sql_on_property | type_join_property | view_label_property);
link_properties: (url_property | label_property | icon_url_property);
measure_properties: (type_view_property | sql_property | value_format_property);
model_properties: (derived_table | join_block);
parameter_properties: (type_view_property | sql_property | allowed_value_property);
test_properties: (explore_source_block | assert_block);
query_properties: (description_property | dimension_query_property | filters_property | label_property | limit_property | measure_query_property | pivots_property | sorts_property);
view_properties: (dimension_block | dimension_group_block | extension_property | extends_property | filter_block | measure_block | parameter_block | sql_table_name_property);
when_properties: (sql_case_property | label_property);

// Property(s)
allowed_value_property: ALLOWED_VALUES COLON allowed_value_list;
always_join_property: ALWAYS_JOIN COLON LBRACKET identifier_list RBRACKET ;
alias_property: ALIAS COLON LBRACKET identifier_list RBRACKET ;
alpha_sort_proptery: ALPHA_SORT COLON (YES | NO);
bypass_suggest_restrictions_property: BYPASS_SUGGEST_RESTRICTIONS COLON (YES | NO);
case_sensitive_property: CASE_SENSITIVE COLON (YES | NO);
can_filter_property: CAN_FILTER COLON (YES | NO);
cancel_grouping_fields_property: CANCEL_GROUPING_FIELDS COLON LBRACKET identifier_list RBRACKET;
convert_tz_property
    : CONVERT_TZ COLON (YES | NO)
    ;

datagroup_trigger_property: DATAGROUP_TRIGGER COLON IDENTIFIER;
data_type_property
    : DATATYPE COLON datatype_value
    ;
default_property: DEFAULT COLON QUOTED_STRING;
description_property: DESCRIPTION COLON QUOTED_STRING;
derived_table_property: SQL COLON QUOTED_STRING;
dimension_query_property: DIMENSIONS COLON LBRACKET identifier_list RBRACKET ;
dimensions_property: DIMENSIONS COLON LBRACKET identifier_list RBRACKET ;
drill_fields_property: DRILL_FIELDS COLON LBRACKET identifier_list RBRACKET;
else_property: ELSE COLON QUOTED_STRING;
end_location_field_property: END_LOCATION_FIELD COLON IDENTIFIER;
expression_property: EXPRESSION COLON DOLLAR LBRACE IDENTIFIER RBRACE EQ NUMBER SEMI SEMI;
extension_property: EXTENSION COLON REQUIRED;
extends_property: EXTENDS COLON LBRACKET identifier_list RBRACKET;
fanout_on_property
    : FANOUT_ON COLON IDENTIFIER
    ;

fields_property: FIELDS COLON LBRACKET identifier_list RBRACKET;
field_property: FIELD COLON IDENTIFIER;
filters_property: FILTERS COLON LBRACKET string_list_key_values RBRACKET;
filters_test_property: FILTERS COLON LBRACKET IDENTIFIER COLON QUOTED_STRING RBRACKET;
final_property: FINAL COLON (YES | NO);
foreign_key_property: FOREIGN_KEY COLON  IDENTIFIER;
form_url_property: FORM_URL COLON QUOTED_STRING;
from_property: FROM COLON  IDENTIFIER;
full_suggestions_property: FULL_SUGESTIONS COLON (YES | NO);
group_item_label_property: GROUP_ITEM_LABEL COLON QUOTED_STRING;
group_label_property: GROUP_LABEL COLON QUOTED_STRING;
hidden_property: HIDDEN_ COLON (YES | NO);
html_property: HTML COLON  SEMI SEMI ;
icon_url_property: ICON_URL COLON QUOTED_STRING;
include_property: INCLUDE COLON QUOTED_STRING;
label_property: LABEL COLON QUOTED_STRING;
label_from_parameter_property: LABEL_FROM_PARAMETER COLON IDENTIFIER;
limit_property: LIMIT COLON NUMBER;
link_property: LINK COLON QUOTED_STRING;
measure_query_property: MEASURES COLON LBRACKET identifier_list RBRACKET ;
measures_property: MEASURES COLON LBRACKET identifier_list RBRACKET ;
name_property: NAME COLON QUOTED_STRING;
order_by_field_property: ORDER_BY_FIELD COLON IDENTIFIER;
outer_only_property: OUTER_ONLY COLON (YES | NO);
// TODO: Make this more detailed of a parser pattern
persist_for_property: PERSIST_FOR COLON QUOTED_STRING;
persist_with_property: PERSIST_WITH COLON IDENTIFIER;
primary_key_property: PRIMARY_KEY COLON (YES | NO);
pivots_property: PIVOTS COLON LBRACKET identifier_list RBRACKET;
relationship_property: RELATIONSHIP COLON (MANY_TO_MANY | MANY_TO_ONE | ONE_TO_ONE | ONE_TO_MANY);
required_property: REQUIRED COLON (YES | NO);
required_access_grants_property: REQUIRED_ACCESS_GRANTS COLON LBRACKET identifier_list RBRACKET;
required_fields_property
    : REQUIRED_FIELDS COLON LBRACKET identifier_list RBRACKET
    ;
required_joins_property: REQUIRED_JOINS COLON LBRACKET identifier_list RBRACKET;
sorts_property: SORTS COLON LBRACKET identifier_list_key_values_asc_desc RBRACKET;
// TODO: Make this more detailed of a parser pattern
style_property: STYLE COLON IDENTIFIER ;
// TODO: review these sql properties
sql_property: SQL COLON DOLLAR LBRACE IDENTIFIER RBRACE DOT IDENTIFIER SEMI SEMI;
sql_case_property: SQL COLON DOLLAR LBRACE IDENTIFIER RBRACE DOT IDENTIFIER EQ NUMBER SEMI SEMI;
sql_on_property: SQL_ON COLON DOLLAR LBRACE IDENTIFIER RBRACE EQ DOLLAR LBRACE IDENTIFIER RBRACE SEMI SEMI;
sql_table_name_property: SQL_TABLE_NAME COLON IDENTIFIER (DOT IDENTIFIER)? SEMI SEMI;
suggest_dimension_property: SUGGEST_DIMENSION COLON IDENTIFIER;
suggest_explore_property: SUGGEST_EXPLORE COLON IDENTIFIER;
suggest_persist_for_property: SUGGEST_PERSIST_FOR COLON QUOTED_STRING;
suggestable_property: SUGGESTABLE COLON (YES | NO);
suggestions_property: SUGGESTIONS COLON LBRACKET string_list RBRACKET;
symmetric_aggregates_property: SYMMETRIC_AGGREGATES COLON (YES | NO);
tags_property: TAGS COLON LBRACKET string_list RBRACKET;
timeframes_property: TIMEFRAMES COLON LBRACKET timeframe_list RBRACKET;
// TODO: rename type property to something else
type_join_property: TYPE COLON (INNER | CROSS | FULL_OUTER | LEFT_OUTER);
type_view_property: TYPE COLON IDENTIFIER;
type_action_form_param_property: TYPE COLON IDENTIFIER;
unless_property: UNLESS COLON LBRACKET identifier_list RBRACKET ;
user_attribute_property: USER_ATTRIBUTE COLON IDENTIFIER;
url_property: URL COLON QUOTED_STRING;
value_property: VALUE COLON QUOTED_STRING;
value_format_property: VALUE_FORMAT COLON QUOTED_STRING;
view_label_property: VIEW_LABEL COLON QUOTED_STRING;
view_name_property: VIEW_NAME COLON IDENTIFIER;

// Derived table and relationship properties needs to be organized better
derived_table: DERIVED_TABLE LBRACE derived_table_property* RBRACE;

// Identifier and string lists
identifier_list: (IDENTIFIER (COMMA IDENTIFIER)*)?;
string_list: (QUOTED_STRING (COMMA QUOTED_STRING)*)?;

// Key-value lists
identifier_key_value: IDENTIFIER COLON IDENTIFIER;
identifier_list_key_values: (identifier_key_value (COMMA identifier_key_value)*)?;

identifier_key_value_asc_desc: IDENTIFIER COLON (ASC | DESC);
identifier_list_key_values_asc_desc: (identifier_key_value_asc_desc (COMMA identifier_key_value_asc_desc)*)?;

string_key_value: IDENTIFIER COLON QUOTED_STRING;
string_list_key_values: (string_key_value (COMMA string_key_value)*)?;

// Allowed value and timeframe lists
allowed_value_list: LPAREN (QUOTED_STRING (COMMA QUOTED_STRING)*)? RPAREN;
timeframe_list: (IDENTIFIER (COMMA IDENTIFIER)*)?;
unlimited_identifiers: (IDENTIFIER (IDENTIFIER)*)?;
// values
datatype_value
    : EPOCH
    | TIMESTAMP
    | DATETIME
    | DATE
    | YYYYMMDD
    ;