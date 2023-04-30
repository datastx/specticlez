import os
import sys

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from app.grammars.LookMLLexer import LookMLLexer
from app.grammars.LookMLParser import LookMLParser


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Error at line {line}, column {column}: {msg}")


class ParsingError(Exception):
    pass


def main(file_path: str) -> None:
    """Parse a LookML file and print the parse tree.

    Args:
        file_path (str): fully qualified path to a LookML file
    """
    
    input_stream = FileStream(file_path)
    
    lexer = LookMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LookMLParser(token_stream)

    # Add the custom error listener
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    try:
        tree = parser.lookml_file()
        print(tree.toStringTree(recog=parser))
    except SyntaxError as e:
        print(f"Error parsing {file_path}: {e}")
        raise ParsingError("Parsing failed") from e


if __name__ == "__main__":
    directory = os.path.join(os.getcwd(), 'app', 'fixtures')
    extension = '.lkml'
    for f in os.listdir(directory):
        if f.endswith(extension):
            lookml_file_path = os.path.join(directory, f)
            print(f"Processing {lookml_file_path}")
            try:
                parse_tree = main(lookml_file_path)
            except ParsingError:
                sys.exit(1)
