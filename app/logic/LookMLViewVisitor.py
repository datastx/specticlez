from LookMLViewParserVisitor import LookMLViewParserVisitor

class LookMLViewVisitor(LookMLViewParserVisitor):
    def visitViewDefinition(self, ctx):
        view_name = ctx.IDENTIFIER().getText()
        print(f"view_{view_name} = {{}}")
        return self.visitChildren(ctx)

    def visitDimensionDefinition(self, ctx):
        dim_name = ctx.IDENTIFIER().getText()
        print(f"view_{dim_name} = None")
        return None

    def visitMeasureDefinition(self, ctx):
        measure_name = ctx.IDENTIFIER().getText()
        print(f"view_{measure_name} = None")
        return None
