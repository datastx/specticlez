lexer grammar LookMLLexer;

// Keywords
VIEW: 'view';
SQL_TABLE_NAME: 'sql_table_name';
DIMENSION: 'dimension';
TYPE: 'type';
SQL: 'sql';
PRIMARY_KEY: 'primary_key';
TIMEFRAMES: 'timeframes';
MEASURE: 'measure';
VALUE_FORMAT: 'value_format';

// Literals
COLON: ':';
SEMICOLON: ';';
DOUBLE_SEMICOLON: ';;';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
LCURLY: '{';
RCURLY: '}';

// Identifier
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

// Schema name
SCHEMA_NAME: ID DOT ID;

// Strings
STRING: '"' ~["\r\n]*? '"';
// QUOTED_STRING: '\'' ~['\r\n]*? '\'';
DOT: '.';

// Expression
EXPR: '${' (~('}') | ('}' ~('}')))* '}';

// Primary key value
YES: 'yes';

// Whitespace and newline
WS: [ \t]+ -> skip;
NEWLINE: [\r\n]+ -> skip;
