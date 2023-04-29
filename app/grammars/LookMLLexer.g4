lexer grammar LookMLLexer;

LOOKER: 'looker';
MODEL: 'model';
VIEW: 'view';
DIMENSION: 'dimension';
DIMENSION_GROUP: 'dimension_group';
MEASURE: 'measure';
FILTER: 'filter';
PARAMETER: 'parameter';
EXPLORE: 'explore';
JOIN: 'join';
SQL: 'sql';
ALIAS: 'alias';
TYPE: 'type';
PRIMARY_KEY: 'primary_key';
DERIVED_TABLE: 'derived_table';
RELATIONSHIP: 'relationship';
REQUIRED: 'required';
LINK: 'link';
ALLOWED_VALUES: 'allowed_values';
SQL_TABLE_NAME: 'sql_table_name';
TIMEFRAMES: 'timeframes';
VALUE_FORMAT: 'value_format';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
COLON: ':';
COMMA: ',';
SEMI: ';';
DOT: '.';
EQ: '=';
PIPE: '|';

IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9-]*; // Allow hyphenated names
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n\t])* '"';
DOLLAR: '$';
COMMENT: '#' .*? '\r'? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;
