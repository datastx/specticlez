

from antlr4 import FileStream, CommonTokenStream
from app.grammars.LookMLLexer import LookMLLexer
from app.grammars.LookMLParser import LookMLParser


def main(file_path):
    # Read the test file
    input_stream = FileStream(file_path)

    # Create a lexer and parser for the input
    lexer = LookMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LookMLParser(token_stream)

    # Parse the test file starting from the top-level rule
    tree = parser.lookml_file()

    # Print the parse tree (optional)
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    directory = '/Users/brianmoore/githib.com/datastx/specticlez/app/fixtures/'
    extension = '.lkml'
    import os
    for file in os.listdir(directory):
        if file.endswith(extension):
            lookml_file_path = os.path.join(directory, file)
            print(f"Processing {lookml_file_path}")
            parse_tree = main(lookml_file_path)
