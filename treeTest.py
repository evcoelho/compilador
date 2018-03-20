import sys
import re
#from antlr4 import *
import antlr4
from gen.cminusLexer import cminusLexer
from gen.cminusParser import cminusParser
from gen.cminusListener import cminusListener

IDENT_SIZE = 1

class printTree(cminusListener):
    def __init__(self):
        self.ident = 0

    def exitVar_declaracao(self, ctx:cminusParser.Var_declaracaoContext):
        self.ident -= IDENT_SIZE
        if (ctx.ID() != None):
            print(' ' * self.ident, ctx.ID())
        if (ctx.NUM() != None):
            print(' ' * self.ident, ctx.NUM())
        pass

    def enterVar_declaracao(self, ctx:cminusParser.Var_declaracaoContext):
        self.ident += IDENT_SIZE
        pass

    def exitTipo_especificador(self, ctx: cminusParser.Tipo_especificadorContext):
        self.ident -= IDENT_SIZE
        if(ctx.VOID() != None):
            print(' ' * self.ident,ctx.VOID())
        if (ctx.INT() != None):
            print(' ' * self.ident,ctx.INT())
        pass

    def enterTipo_especificador(self, ctx: cminusParser.Tipo_especificadorContext):
        self.ident += IDENT_SIZE
        pass

    def exitFun_declaracao(self, ctx: cminusParser.Fun_declaracaoContext):
        self.ident -= IDENT_SIZE
        if (ctx.ID() != None):
            print(' ' * self.ident, ctx.ID())
        pass

    def enterFun_declaracao(self, ctx: cminusParser.Fun_declaracaoContext):
        self.ident += IDENT_SIZE
        pass

    def exitParams(self, ctx:cminusParser.ParamsContext):
        self.ident -= IDENT_SIZE
        if (ctx.VOID() != None):
            print(' ' * self.ident, ctx.VOID())
        pass

    def enterParams(self, ctx:cminusParser.ParamsContext):
        self.ident += IDENT_SIZE
        pass

    def exitParam(self, ctx:cminusParser.ParamContext):
        self.ident -= IDENT_SIZE
        if (ctx.ID() != None):
            print(' ' * self.ident, ctx.ID())
        pass

    def enterParam(self, ctx:cminusParser.ParamContext):
        self.ident += IDENT_SIZE
        pass


    def exitSelecao_decl(self, ctx:cminusParser.Selecao_declContext):
        self.ident -= IDENT_SIZE
        if (ctx.IF() != None):
            print(' ' * self.ident, ctx.IF())
        if (ctx.ELSE() != None):
            print(' ' * self.ident, ctx.ELSE())
        pass

    def enterSelecao_decl(self, ctx:cminusParser.Selecao_declContext):
        self.ident += IDENT_SIZE
        pass

    def exitIteracao_decl(self, ctx:cminusParser.Iteracao_declContext):
        self.ident -= IDENT_SIZE
        if (ctx.WHILE() != None):
            print(' ' * self.ident, ctx.WHILE())
        pass

    def enterIteracao_decl(self, ctx:cminusParser.Iteracao_declContext):
        self.ident += IDENT_SIZE
        pass

    def exitRetorno_decl(self, ctx:cminusParser.Retorno_declContext):
        self.ident -= IDENT_SIZE
        if (ctx.RETURN() != None):
            print(' ' * self.ident, ctx.RETURN())
        pass

    def enterRetorno_decl(self, ctx:cminusParser.Retorno_declContext):
        self.ident += IDENT_SIZE
        pass

    def exitExpressao(self, ctx: cminusParser.ExpressaoContext):
        self.ident -= IDENT_SIZE
        if (ctx.ASSIGN() != None):
            print(' ' * self.ident, ctx.ASSIGN())
        pass

    def enterExpressao(self, ctx: cminusParser.ExpressaoContext):
        self.ident += IDENT_SIZE
        pass

    def exitVar(self, ctx:cminusParser.VarContext):
        self.ident -= IDENT_SIZE
        if (ctx.ID() != None):
            print(' ' * self.ident, ctx.ID())
        pass

    def enterVar(self, ctx:cminusParser.VarContext):
        self.ident += IDENT_SIZE
        pass

    def exitRelacional(self, ctx:cminusParser.RelacionalContext):
        self.ident -= IDENT_SIZE
        if (ctx.LETHAN() != None):
            print(' ' * self.ident, ctx.LETHAN())
        if (ctx.LT() != None):
            print(' ' * self.ident, ctx.LT())
        if (ctx.GT() != None):
            print(' ' * self.ident, ctx.GT())
        if (ctx.GETHAN() != None):
            print(' ' * self.ident, ctx.GETHAN())
        if (ctx.EQ() != None):
            print(' ' * self.ident, ctx.EQ())
        if (ctx.DF() != None):
            print(' ' * self.ident, ctx.DF())
        pass

    def enterRelacional(self, ctx:cminusParser.RelacionalContext):
        self.ident += IDENT_SIZE
        pass

    def exitSoma(self, ctx:cminusParser.SomaContext):
        self.ident -= IDENT_SIZE
        if (ctx.PLUS() != None):
            print(' ' * self.ident, ctx.PLUS())
        if (ctx.MINUS() != None):
            print(' ' * self.ident, ctx.MINUS())
        pass

    def enterSoma(self, ctx:cminusParser.SomaContext):
        self.ident += IDENT_SIZE
        pass

    def exitTermo(self, ctx:cminusParser.TermoContext):
        self.ident -= IDENT_SIZE
        pass

    # Exit a parse tree produced by cminusParser#termo.
    def enterTermo(self, ctx:cminusParser.TermoContext):
        self.ident += IDENT_SIZE
        pass

    def exitMult(self, ctx:cminusParser.MultContext):
        self.ident -= IDENT_SIZE
        if (ctx.TIMES() != None):
            print(' ' * self.ident, ctx.TIMES())
        if (ctx.OVER() != None):
            print(' ' * self.ident, ctx.OVER())
        pass

    def enterMult(self, ctx:cminusParser.MultContext):
        self.ident += IDENT_SIZE
        pass

    def exitFator(self, ctx:cminusParser.FatorContext):
        self.ident -= IDENT_SIZE
        if (ctx.NUM() != None):
            print(' ' * self.ident, ctx.NUM())
        pass

    def enterFator(self, ctx:cminusParser.FatorContext):
        self.ident += IDENT_SIZE
        pass

    def exitAtivacao(self, ctx:cminusParser.AtivacaoContext):
        self.ident -= IDENT_SIZE
        if (ctx.ID() != None):
            print(' ' * self.ident, ctx.ID())
        pass

    def enterAtivacao(self, ctx:cminusParser.AtivacaoContext):
        self.ident += IDENT_SIZE
        pass


def main(argv):
    input = antlr4.FileStream(argv[1])
    lexer = cminusLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = cminusParser(stream)
    tree = parser.programa()
    #tree_str = tree.toStringTree(recog=parser)
    #print(tree_str)

    printer = printTree()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
