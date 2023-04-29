parser grammar LookMLParser;

options { tokenVocab=LookMLLexer; }

lookml: view_def EOF;

view_def: VIEW COLON ID LCURLY sql_table_name_def field_def* RCURLY;

sql_table_name_def: SQL_TABLE_NAME COLON SCHEMA_NAME DOUBLE_SEMICOLON;

field_def: (dim_def | measure_def);

dim_def: DIMENSION COLON ID LCURLY (type_def | sql_def | primary_key_def)* RCURLY SEMICOLON?;

type_def: TYPE COLON ID ;

sql_def: SQL COLON EXPR DOUBLE_SEMICOLON;

primary_key_def: PRIMARY_KEY COLON primary_key_value ;

primary_key_value: YES;

timeframes_def: TIMEFRAMES COLON LBRACKET timeframe* RBRACKET SEMICOLON?;

timeframe: ID COMMA?;

measure_def: MEASURE COLON ID LCURLY (type_def | sql_def | value_format_def)+ RCURLY SEMICOLON?;

value_format_def: VALUE_FORMAT COLON STRING;
