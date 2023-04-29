from antlr4 import FileStream, CommonTokenStream
from app.grammars.LookMLLexer import LookMLLexer
from app.grammars.LookMLParser import LookMLParser


def main(file_path: str) -> None:
    """Parse a LookML file and print the parse tree.

    Args:
        file_path (str): fully qualified path to a LookML file
    """
    
    input_stream = FileStream(file_path)
    
    lexer = LookMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LookMLParser(token_stream)

    tree = parser.lookml_file()
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    import os
    directory = os.path.join(os.getcwd(), 'app', 'fixtures')
    extension = '.lkml'
    for file in os.listdir(directory):
        if file.endswith(extension):
            lookml_file_path = os.path.join(directory, file)
            print(f"Processing {lookml_file_path}")
            parse_tree = main(lookml_file_path)
