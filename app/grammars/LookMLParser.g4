parser grammar LookMLParser;

options { tokenVocab=LookMLLexer; }

lookml: view_def EOF;

view_def: VIEW COLON ID LCURLY sql_table_name_def dim_def* measure_def* RCURLY;

sql_table_name_def: SQL_TABLE_NAME COLON STRING SEMICOLON SEMICOLON;

dim_def: DIMENSION COLON ID LCURLY (type_def | sql_def | primary_key_def)+ RCURLY;

type_def: TYPE COLON ID SEMICOLON;

sql_def: SQL COLON EXPR SEMICOLON SEMICOLON;

primary_key_def: PRIMARY_KEY COLON ID SEMICOLON;

timeframes_def: TIMEFRAMES COLON LBRACKET timeframe* RBRACKET SEMICOLON;

timeframe: ID COMMA?;

measure_def: MEASURE COLON ID LCURLY (type_def | sql_def | value_format_def)+ RCURLY;

value_format_def: VALUE_FORMAT COLON STRING SEMICOLON;
