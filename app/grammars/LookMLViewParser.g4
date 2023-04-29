parser grammar LookMLViewParser;

options { tokenVocab=LookMLViewLexer; }

viewFile: viewDefinition EOF;

viewDefinition: VIEW IDENTIFIER LBRACE (dimensionDefinition | measureDefinition)* RBRACE;

dimensionDefinition: DIMENSION IDENTIFIER;

measureDefinition: MEASURE IDENTIFIER;
