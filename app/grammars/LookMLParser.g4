parser grammar LookMLParser;

options { tokenVocab=LookMLLexer; }

lookml_file: (model | view | explore)* EOF;

// lookml_file: (view )* EOF;

model: MODEL COLON IDENTIFIER LBRACE model_property* RBRACE;
view: VIEW COLON IDENTIFIER LBRACE view_property* RBRACE;
explore: EXPLORE COLON IDENTIFIER LBRACE explore_property* RBRACE;

model_property: (join | derived_table);
view_property: (sql_table_name_property | dimension | dimension_group | measure | filter | parameter);
explore_property: (join | derived_table | relationship | link);

sql_table_name_property: SQL_TABLE_NAME COLON IDENTIFIER (DOT IDENTIFIER)? SEMI SEMI;

join: JOIN IDENTIFIER LBRACE join_property* RBRACE;
derived_table: DERIVED_TABLE LBRACE derived_table_property* RBRACE;
relationship: RELATIONSHIP COLON IDENTIFIER;
link: LINK COLON STRING;

join_property: SQL COLON STRING;
derived_table_property: SQL COLON STRING;

dimension: DIMENSION COLON IDENTIFIER LBRACE dimension_property* RBRACE;
dimension_group: DIMENSION_GROUP COLON IDENTIFIER LBRACE dimension_group_property* RBRACE;
measure: MEASURE COLON IDENTIFIER LBRACE measure_property* RBRACE;
filter: FILTER COLON IDENTIFIER LBRACE filter_property* RBRACE;
parameter: PARAMETER COLON IDENTIFIER LBRACE parameter_property* RBRACE;

dimension_property: (type_property | sql_property | primary_key_property | timeframes_property);
dimension_group_property: (type_property | sql_property | timeframes_property);
measure_property: (type_property | sql_property | value_format_property);
filter_property: (type_property | sql_property);
parameter_property: (type_property | sql_property | allowed_value_property);

type_property: TYPE COLON IDENTIFIER;
sql_property: SQL COLON DOLLAR LBRACE IDENTIFIER RBRACE DOT IDENTIFIER SEMI SEMI;
primary_key_property: PRIMARY_KEY COLON IDENTIFIER;
allowed_value_property: ALLOWED_VALUES COLON allowed_value_list;
timeframes_property: TIMEFRAMES COLON LBRACKET timeframe_list RBRACKET;
value_format_property: VALUE_FORMAT COLON STRING;

allowed_value_list: LPAREN (STRING (COMMA STRING)*)? RPAREN;
timeframe_list: (IDENTIFIER (COMMA IDENTIFIER)*)?;
