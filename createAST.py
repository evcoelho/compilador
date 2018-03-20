from antlr4 import *
from .gen.cminusVisitor import cminusVisitor


if __name__ is not None and "." in __name__:
    from gen.cminusParser import cminusParser
else:
    from gen.cminusParser import cminusParser

class AstNo:
    def __init__(self, line = -1):
        self.line = line

class Programa(AstNo):
    def __init__(self,decl_lista, line = -1):
        super().__init__(line)
        self.decl_lista = decl_lista

class DeclaracaoLista(AstNo):
    def __init__(self, decl_lista, decl, line = -1):
        super().__init__(line)
        self.decl_lista = decl_lista
        self.decl = decl
        
class Decl(AstNo):
    def __init__(self, decl, line = -1):
        super().__init__(line)
        self.decl = decl
        
class VarDecl(AstNo):
    def __init__(self, tipo, id, num, line = -1):
        super().__init__(line)
        self.tipo = tipo
        self.id = id
        self.num = num
        
class TipoEsp(AstNo):
    def __init__(self, tipoE, line = -1):
        super().__init__(line)
        self.tipoE = tipoE

class FunDecl(AstNo):
    def __init__(self, tipoE, id, parametros, declComp, line = -1):
        super().__init__(line)
        self.tipoE = tipoE
        self.id = id
        self.parametros = parametros
        self.declComp = declComp
        
class Parametros(AstNo):
    def __init__(self, listaParam, tipo, line = -1):
        super().__init__(line)
        self.listaParam = listaParam
        self.tipo = tipo
        

class ListaParametros(AstNo):
    def __init__(self, listaParam, param, line = -1):
        super().__init__(line)
        self.listaParam = listaParam
        self.param = param
 
class Param(AstNo):
    def __init__(self, tipoEsp, id, line = -1):
        super().__init__(line)
        self.tipoEsp = tipoEsp
        self.id = id
        
class CompDecl(AstNo):
    def __init__(self, localDecl, stmLista, line = -1):
        super().__init__(line)
        self.localDecl = localDecl
        self.stmLista = stmLista

class LocalDeclaracoes(AstNo):
    def __init__(self, localDecl, varDecl, line = -1):
        super().__init__(line)
        self.locaDecl = localDecl
        self.varDecl = varDecl
        
class StatementLista(AstNo):
    def __init__(self, stmLista, stm, line = -1):
        super().__init__(line)
        self.stmLista = stmLista
        self.stm = stm

class IfDecl(AstNo):
    def __init__(self, condicao, corpoIf, corpoElse, line = -1):
        super().__init__(line)
        self.condicao = condicao
        self.corpoIf = corpoIf
        self.corpoElse = corpoElse

class WhileDecl(AstNo):
    def __init__(self, condicao, corpo, line = -1):
        super().__init__(line)
        self.condicao = condicao
        self.corpo = corpo

class ReturnDecl(AstNo):
    def __init__(self, expressao=None, line = -1):
        super().__init__(line)
        self.expressao = expressao
        
class ExpressaoDecl(AstNo):
    def __init__(self, var, expressao, simplesExpressao, line = -1):
        super().__init__(line)
        self.var = var
        self.expressao = expressao
        self.simplesExpressao = simplesExpressao
        
class Variavel(AstNo):
    def __init__(self, id, expressao=None, line = -1):
        super().__init__(line)
        self.id = id
        self.expressao = expressao
        
class Comp(AstNo):
    def __init__(self, esq, relacional, dir, operacao = None, line = -1):
        super().__init__(line)
        self.esq = esq
        self.relacional = relacional
        self.dir = dir
        self.operacao = operacao

class Operacao(AstNo):
    def __init__(self, esq, op, dir, line = -1):
        super().__init__(line)
        self.esq = esq
        self.op = op
        self.dir = dir
        
class Ativ(AstNo):
    def __init__(self, id, argLista, line = -1):
        super().__init__(line)
        self.id = id;
        self.argLista = argLista

class ListaArgumentos(AstNo):
    def __init__(self, argLista, exp, line = -1):
        super().__init__(line)
        self.argLista = argLista
        self.exp = exp

class numero(AstNo):
    def __init__(self, num, line = -1):
        super().__init__(line)
        self.num = int(num)


class CriarAst(cminusVisitor):
    # Visit a parse tree produced by cminusParser#programa.
    def visitPrograma(self, ctx: cminusParser.ProgramaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#declaracao_lista.
    def visitDeclaracao_lista(self, ctx: cminusParser.Declaracao_listaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#declaracao.
    def visitDeclaracao(self, ctx: cminusParser.DeclaracaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#var_declaracao.
    def visitVar_declaracao(self, ctx: cminusParser.Var_declaracaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#tipo_especificador.
    def visitTipo_especificador(self, ctx: cminusParser.Tipo_especificadorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#fun_declaracao.
    def visitFun_declaracao(self, ctx: cminusParser.Fun_declaracaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#params.
    def visitParams(self, ctx: cminusParser.ParamsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#param_lista.
    def visitParam_lista(self, ctx: cminusParser.Param_listaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#param.
    def visitParam(self, ctx: cminusParser.ParamContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#composto_decl.
    def visitComposto_decl(self, ctx: cminusParser.Composto_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#local_declaracoes.
    def visitLocal_declaracoes(self, ctx: cminusParser.Local_declaracoesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#statement_lista.
    def visitStatement_lista(self, ctx: cminusParser.Statement_listaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#statement.
    def visitStatement(self, ctx: cminusParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#expressao_decl.
    def visitExpressao_decl(self, ctx: cminusParser.Expressao_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#selecao_decl.
    def visitSelecao_decl(self, ctx: cminusParser.Selecao_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#iteracao_decl.
    def visitIteracao_decl(self, ctx: cminusParser.Iteracao_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#retorno_decl.
    def visitRetorno_decl(self, ctx: cminusParser.Retorno_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#expressao.
    def visitExpressao(self, ctx: cminusParser.ExpressaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#var.
    def visitVar(self, ctx: cminusParser.VarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#simples_expressao.
    def visitSimples_expressao(self, ctx: cminusParser.Simples_expressaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#addsub.
    def visitAddsub(self, ctx: cminusParser.AddsubContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#term.
    def visitTerm(self, ctx: cminusParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#termo.
    def visitTermo(self, ctx: cminusParser.TermoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#fator.
    def visitFator(self, ctx: cminusParser.FatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#ativacao.
    def visitAtivacao(self, ctx: cminusParser.AtivacaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#arg_lista.
    def visitArg_lista(self, ctx: cminusParser.Arg_listaContext):
        return self.visitChildren(ctx)



class AstVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))






