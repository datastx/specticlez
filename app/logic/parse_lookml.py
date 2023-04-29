from antlr4 import FileStream, CommonTokenStream
from LookMLViewLexer import LookMLViewLexer
from LookMLViewParser import LookMLViewParser
from LookMLViewVisitor import LookMLViewVisitor

def parse_lookml(file_path):
    input_stream = FileStream(file_path)
    lexer = LookMLViewLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LookMLView
