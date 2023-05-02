
from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Tree import ParseTree
from app.engine.antlr.LookMLLexer import LookMLLexer
from app.engine.antlr.LookMLParser import LookMLParser
from app.engine.errors import CustomErrorListener, ParsingError




def build_ast(file_path: str) -> ParseTree:
    """
    Parse a LookML file and print the parse tree.
    We have custom error implemtation logic.

    Args:
        file_path (str): Fully qualified path to a LookML file.
    """
    input_stream = FileStream(file_path)

    lexer = LookMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LookMLParser(token_stream)

    # Add the custom error listener
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    try:
        ast: ParseTree = parser.lookml_file()
        print(ast.toStringTree(recog=parser))
    except SyntaxError as e:
        print(f"Error parsing {file_path}: {e}")
        raise ParsingError("Parsing failed") from e

    return ast
