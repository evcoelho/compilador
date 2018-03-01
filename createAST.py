import sys
import re
from antlr4 import *
from antlr4.InputStream import InputStream
from gen.cminusLexer import cminusLexer
from gen.cminusParser import cminusParser
from gen.cminusVisitor import cminusVisitor


class createAST(cminusVisitor):
    # Visit a parse tree produced by cminusParser#programa.
    def visitPrograma(self, ctx: cminusParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#declaracao_lista.
    def visitDeclaracao_lista(self, ctx: cminusParser.Declaracao_listaContext):
        return self.visitChildren(ctx)