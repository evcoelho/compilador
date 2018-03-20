# Generated from /home/everton/Documentos/compiladores/compilador/cminus.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cminusParser import cminusParser
else:
    from cminusParser import cminusParser

# This class defines a complete generic visitor for a parse tree produced by cminusParser.

class cminusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cminusParser#programa.
    def visitPrograma(self, ctx:cminusParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#declaracao_lista.
    def visitDeclaracao_lista(self, ctx:cminusParser.Declaracao_listaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#declaracao.
    def visitDeclaracao(self, ctx:cminusParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#var_declaracao.
    def visitVar_declaracao(self, ctx:cminusParser.Var_declaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#tipo_especificador.
    def visitTipo_especificador(self, ctx:cminusParser.Tipo_especificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#fun_declaracao.
    def visitFun_declaracao(self, ctx:cminusParser.Fun_declaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#params.
    def visitParams(self, ctx:cminusParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#param_lista.
    def visitParam_lista(self, ctx:cminusParser.Param_listaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#param.
    def visitParam(self, ctx:cminusParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#composto_decl.
    def visitComposto_decl(self, ctx:cminusParser.Composto_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#local_declaracoes.
    def visitLocal_declaracoes(self, ctx:cminusParser.Local_declaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#statement_lista.
    def visitStatement_lista(self, ctx:cminusParser.Statement_listaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#statement.
    def visitStatement(self, ctx:cminusParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#expressao_decl.
    def visitExpressao_decl(self, ctx:cminusParser.Expressao_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#selecao_decl.
    def visitSelecao_decl(self, ctx:cminusParser.Selecao_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#iteracao_decl.
    def visitIteracao_decl(self, ctx:cminusParser.Iteracao_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#retorno_decl.
    def visitRetorno_decl(self, ctx:cminusParser.Retorno_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#expressao.
    def visitExpressao(self, ctx:cminusParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#var.
    def visitVar(self, ctx:cminusParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#simples_expressao.
    def visitSimples_expressao(self, ctx:cminusParser.Simples_expressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#soma_expressao.
    def visitSoma_expressao(self, ctx:cminusParser.Soma_expressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#termo.
    def visitTermo(self, ctx:cminusParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#fator.
    def visitFator(self, ctx:cminusParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#ativacao.
    def visitAtivacao(self, ctx:cminusParser.AtivacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cminusParser#arg_lista.
    def visitArg_lista(self, ctx:cminusParser.Arg_listaContext):
        return self.visitChildren(ctx)



del cminusParser