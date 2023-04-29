# Generated from LookMLViewParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LookMLViewParser import LookMLViewParser
else:
    from LookMLViewParser import LookMLViewParser

# This class defines a complete listener for a parse tree produced by LookMLViewParser.
class LookMLViewParserListener(ParseTreeListener):

    # Enter a parse tree produced by LookMLViewParser#viewFile.
    def enterViewFile(self, ctx:LookMLViewParser.ViewFileContext):
        pass

    # Exit a parse tree produced by LookMLViewParser#viewFile.
    def exitViewFile(self, ctx:LookMLViewParser.ViewFileContext):
        pass


    # Enter a parse tree produced by LookMLViewParser#viewDefinition.
    def enterViewDefinition(self, ctx:LookMLViewParser.ViewDefinitionContext):
        pass

    # Exit a parse tree produced by LookMLViewParser#viewDefinition.
    def exitViewDefinition(self, ctx:LookMLViewParser.ViewDefinitionContext):
        pass


    # Enter a parse tree produced by LookMLViewParser#dimensionDefinition.
    def enterDimensionDefinition(self, ctx:LookMLViewParser.DimensionDefinitionContext):
        pass

    # Exit a parse tree produced by LookMLViewParser#dimensionDefinition.
    def exitDimensionDefinition(self, ctx:LookMLViewParser.DimensionDefinitionContext):
        pass


    # Enter a parse tree produced by LookMLViewParser#measureDefinition.
    def enterMeasureDefinition(self, ctx:LookMLViewParser.MeasureDefinitionContext):
        pass

    # Exit a parse tree produced by LookMLViewParser#measureDefinition.
    def exitMeasureDefinition(self, ctx:LookMLViewParser.MeasureDefinitionContext):
        pass



del LookMLViewParser