import glob

from antlr4 import FileStream, CommonTokenStream
from app.grammars.LookMLLexer import LookMLLexer
from app.grammars.LookMLParser import LookMLParser


def parse_lookml_file(file_path):
    # Read the input file
    input_stream = FileStream(file_path)

    # Create a lexer and token stream for the input
    lexer = LookMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Create a parser and parse the input
    parser = LookMLParser(token_stream)
    parse_tree = parser.lookml()

    # (Optional) Print the parse tree
    print(parse_tree.toStringTree(recog=parser))

    return parse_tree


if __name__ == "__main__":
    directory = '/Users/brianmoore/githib.com/datastx/specticlez/app/fixtures/'
    extension = '.lkml'
    import os
    for file in os.listdir(directory):
        if file.endswith(extension):
            lookml_file_path = os.path.join(directory, file)
            print(f"Processing {lookml_file_path}")
            parse_tree = parse_lookml_file(lookml_file_path)
