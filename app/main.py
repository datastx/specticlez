from antlr4 import *
from app.grammars.LookMLViewLexer import LookMLViewLexer
from app.grammars.LookMLViewParser import LookMLViewParser


def main():
    input_stream = FileStream('app/fixtures/lookml_test.view.lkml')
    lexer = LookMLViewLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LookMLViewParser(stream)
    tree = parser.file()
    print(tree.toStringTree(recog=parser))