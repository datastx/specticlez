lexer grammar LookMLViewLexer;

VIEW: 'view:';
DIMENSION: 'dimension:';
MEASURE: 'measure:';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
WHITESPACE: [ \t\r\n]+ -> skip;
LBRACE: '{';
RBRACE: '}';
SEMICOLON: ';';
COLON: ':';
