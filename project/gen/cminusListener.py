# Generated from cminus.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cminusParser import cminusParser
else:
    from cminusParser import cminusParser

# This class defines a complete listener for a parse tree produced by cminusParser.
class cminusListener(ParseTreeListener):

    # Enter a parse tree produced by cminusParser#programa.
    def enterPrograma(self, ctx:cminusParser.ProgramaContext):
        pass

    # Exit a parse tree produced by cminusParser#programa.
    def exitPrograma(self, ctx:cminusParser.ProgramaContext):
        pass


    # Enter a parse tree produced by cminusParser#declaracao.
    def enterDeclaracao(self, ctx:cminusParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by cminusParser#declaracao.
    def exitDeclaracao(self, ctx:cminusParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by cminusParser#var_declaracao.
    def enterVar_declaracao(self, ctx:cminusParser.Var_declaracaoContext):
        pass

    # Exit a parse tree produced by cminusParser#var_declaracao.
    def exitVar_declaracao(self, ctx:cminusParser.Var_declaracaoContext):
        pass


    # Enter a parse tree produced by cminusParser#tipo_especificador.
    def enterTipo_especificador(self, ctx:cminusParser.Tipo_especificadorContext):
        pass

    # Exit a parse tree produced by cminusParser#tipo_especificador.
    def exitTipo_especificador(self, ctx:cminusParser.Tipo_especificadorContext):
        pass


    # Enter a parse tree produced by cminusParser#fun_declaracao.
    def enterFun_declaracao(self, ctx:cminusParser.Fun_declaracaoContext):
        pass

    # Exit a parse tree produced by cminusParser#fun_declaracao.
    def exitFun_declaracao(self, ctx:cminusParser.Fun_declaracaoContext):
        pass


    # Enter a parse tree produced by cminusParser#params.
    def enterParams(self, ctx:cminusParser.ParamsContext):
        pass

    # Exit a parse tree produced by cminusParser#params.
    def exitParams(self, ctx:cminusParser.ParamsContext):
        pass


    # Enter a parse tree produced by cminusParser#param_lista.
    def enterParam_lista(self, ctx:cminusParser.Param_listaContext):
        pass

    # Exit a parse tree produced by cminusParser#param_lista.
    def exitParam_lista(self, ctx:cminusParser.Param_listaContext):
        pass


    # Enter a parse tree produced by cminusParser#param.
    def enterParam(self, ctx:cminusParser.ParamContext):
        pass

    # Exit a parse tree produced by cminusParser#param.
    def exitParam(self, ctx:cminusParser.ParamContext):
        pass


    # Enter a parse tree produced by cminusParser#composto_decl.
    def enterComposto_decl(self, ctx:cminusParser.Composto_declContext):
        pass

    # Exit a parse tree produced by cminusParser#composto_decl.
    def exitComposto_decl(self, ctx:cminusParser.Composto_declContext):
        pass


    # Enter a parse tree produced by cminusParser#local_declaracoes.
    def enterLocal_declaracoes(self, ctx:cminusParser.Local_declaracoesContext):
        pass

    # Exit a parse tree produced by cminusParser#local_declaracoes.
    def exitLocal_declaracoes(self, ctx:cminusParser.Local_declaracoesContext):
        pass


    # Enter a parse tree produced by cminusParser#statement_lista.
    def enterStatement_lista(self, ctx:cminusParser.Statement_listaContext):
        pass

    # Exit a parse tree produced by cminusParser#statement_lista.
    def exitStatement_lista(self, ctx:cminusParser.Statement_listaContext):
        pass


    # Enter a parse tree produced by cminusParser#statement.
    def enterStatement(self, ctx:cminusParser.StatementContext):
        pass

    # Exit a parse tree produced by cminusParser#statement.
    def exitStatement(self, ctx:cminusParser.StatementContext):
        pass


    # Enter a parse tree produced by cminusParser#expressao_decl.
    def enterExpressao_decl(self, ctx:cminusParser.Expressao_declContext):
        pass

    # Exit a parse tree produced by cminusParser#expressao_decl.
    def exitExpressao_decl(self, ctx:cminusParser.Expressao_declContext):
        pass


    # Enter a parse tree produced by cminusParser#selecao_decl.
    def enterSelecao_decl(self, ctx:cminusParser.Selecao_declContext):
        pass

    # Exit a parse tree produced by cminusParser#selecao_decl.
    def exitSelecao_decl(self, ctx:cminusParser.Selecao_declContext):
        pass


    # Enter a parse tree produced by cminusParser#iteracao_decl.
    def enterIteracao_decl(self, ctx:cminusParser.Iteracao_declContext):
        pass

    # Exit a parse tree produced by cminusParser#iteracao_decl.
    def exitIteracao_decl(self, ctx:cminusParser.Iteracao_declContext):
        pass


    # Enter a parse tree produced by cminusParser#retorno_decl.
    def enterRetorno_decl(self, ctx:cminusParser.Retorno_declContext):
        pass

    # Exit a parse tree produced by cminusParser#retorno_decl.
    def exitRetorno_decl(self, ctx:cminusParser.Retorno_declContext):
        pass


    # Enter a parse tree produced by cminusParser#expressao.
    def enterExpressao(self, ctx:cminusParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by cminusParser#expressao.
    def exitExpressao(self, ctx:cminusParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by cminusParser#var.
    def enterVar(self, ctx:cminusParser.VarContext):
        pass

    # Exit a parse tree produced by cminusParser#var.
    def exitVar(self, ctx:cminusParser.VarContext):
        pass


    # Enter a parse tree produced by cminusParser#simples_expressao.
    def enterSimples_expressao(self, ctx:cminusParser.Simples_expressaoContext):
        pass

    # Exit a parse tree produced by cminusParser#simples_expressao.
    def exitSimples_expressao(self, ctx:cminusParser.Simples_expressaoContext):
        pass


    # Enter a parse tree produced by cminusParser#soma_expressao.
    def enterSoma_expressao(self, ctx:cminusParser.Soma_expressaoContext):
        pass

    # Exit a parse tree produced by cminusParser#soma_expressao.
    def exitSoma_expressao(self, ctx:cminusParser.Soma_expressaoContext):
        pass


    # Enter a parse tree produced by cminusParser#termo.
    def enterTermo(self, ctx:cminusParser.TermoContext):
        pass

    # Exit a parse tree produced by cminusParser#termo.
    def exitTermo(self, ctx:cminusParser.TermoContext):
        pass


    # Enter a parse tree produced by cminusParser#fator.
    def enterFator(self, ctx:cminusParser.FatorContext):
        pass

    # Exit a parse tree produced by cminusParser#fator.
    def exitFator(self, ctx:cminusParser.FatorContext):
        pass


    # Enter a parse tree produced by cminusParser#ativacao.
    def enterAtivacao(self, ctx:cminusParser.AtivacaoContext):
        pass

    # Exit a parse tree produced by cminusParser#ativacao.
    def exitAtivacao(self, ctx:cminusParser.AtivacaoContext):
        pass


