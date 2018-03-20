from antlr4 import *
from gen.cminusParser import cminusParser
from gen.cminusVisitor import cminusVisitor


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
    def __init__(self, tipo, id, num=None, line = -1):
        super().__init__(line)
        self.tipo = tipo
        self.id = id
        self.num = num
        
class TipoEsp(AstNo):
    def __init__(self, tipoE_, line = -1):
        super().__init__(line)
        self.tipoE = tipoE_

class FunDecl(AstNo):
    def __init__(self, tipoE, id, parametros, declComp, line = -1):
        super().__init__(line)
        self.tipoE = tipoE
        self.id = id
        self.parametros = parametros
        self.declComp = declComp
        
class Parametros(AstNo):
    def __init__(self, listaParam=None, tipo=None, line = -1):
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
    def __init__(self, condicao, corpoIf, corpoElse=None, line = -1):
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
    def __init__(self, id, argLista=None, line = -1):
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
        return Programa(
            decl_lista=(self.visit(ctx.declaracao_lista())),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#declaracao_lista.
    def visitDeclaracao_lista(self, ctx: cminusParser.Declaracao_listaContext):
        if ctx.declaracao_lista() is not None:
            return DeclaracaoLista(
                decl_lista=(self.visit(ctx.declaracao_lista())),
                decl=(self.visit(ctx.declaracao())),
                line=ctx.start.line,
            )
        return self.visit(ctx.declaracao())

    # Visit a parse tree produced by cminusParser#declaracao.
    def visitDeclaracao(self, ctx: cminusParser.DeclaracaoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#var_declaracao.
    def visitVar_declaracao(self, ctx: cminusParser.Var_declaracaoContext):
        if ctx.NUM() is not None:
            return VarDecl(
                tipo=(self.visit(ctx.tipo_especificador())),
                id=(self.visit(ctx.ID())),
                num=(self.visit(ctx.NUM())),
                line=ctx.start.line,
            )
        return VarDecl(
            tipo=self.visit(ctx.tipo_especificador()),
            id=self.visit(ctx.ID()),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#tipo_especificador.
    def visitTipo_especificador(self, ctx: cminusParser.Tipo_especificadorContext):
        return TipoEsp(
                tipoE_=ctx.getText(),
                line=ctx.start.line,
            )

    # Visit a parse tree produced by cminusParser#fun_declaracao.
    def visitFun_declaracao(self, ctx: cminusParser.Fun_declaracaoContext):
        return FunDecl(
            tipoE=self.visit(ctx.tipo_especificador()),
            id=ctx.ID().getText(),
            parametros=self.visit(ctx.params()),
            declComp=self.visit(ctx.composto_decl()),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#params.
    def visitParams(self, ctx: cminusParser.ParamsContext):
        if ctx.param_lista() is not None:
            return Parametros(
                listaParam=self.visit(ctx.param_lista()),
                line=ctx.start.line,
            )
        return Parametros(
            tipo=ctx.getText(),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#param_lista.
    def visitParam_lista(self, ctx: cminusParser.Param_listaContext):
        if ctx.param_lista() is not None:
            return ListaParametros(
                listaParam=self.visit(ctx.param_lista()),
                param=self.visit(ctx.param()),
                line=ctx.start.line
            )
        return ListaParametros(
            listaParam=None,
            param=self.visit(ctx.param()),
            line=ctx.start.line
        )

    # Visit a parse tree produced by cminusParser#param.
    def visitParam(self, ctx: cminusParser.ParamContext):
        return Param(
            tipoEsp=self.visit(ctx.tipo_especificador()),
            id=ctx.ID().getText(),
            line=ctx.start.line
        )

    # Visit a parse tree produced by cminusParser#composto_decl.
    def visitComposto_decl(self, ctx: cminusParser.Composto_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#local_declaracoes.
    def visitLocal_declaracoes(self, ctx: cminusParser.Local_declaracoesContext):
        if ctx.local_declaracoes() is not None:
            return LocalDeclaracoes(
                localDecl=self.visit(ctx.local_declaracoes()),
                varDecl=self.visit(ctx.var_declaracao()),
                line=ctx.start.line,
            )
        return LocalDeclaracoes(
            localDecl=None,
            varDecl=self.visit(ctx.var_declaracao()),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#statement_lista.
    def visitStatement_lista(self, ctx: cminusParser.Statement_listaContext):
        if ctx.statement_lista() is not None:
            return StatementLista(
                stmLista=self.visit(ctx.statement_lista()),
                stm=self.visit(ctx.statement()),
                line=ctx.start.line,
            )
        return StatementLista(
            stmLista=None,
            stm=self.visit(ctx.statement()),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#statement.
    def visitStatement(self, ctx: cminusParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#expressao_decl.
    def visitExpressao_decl(self, ctx: cminusParser.Expressao_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#selecao_decl.
    def visitSelecao_decl(self, ctx: cminusParser.Selecao_declContext):
        if ctx.corpoElse is not None:
            return IfDecl(
                condicao=self.visit(ctx.expressao()),
                corpoIf=self.visit(ctx.corpoIF),
                corpoElse=self.visit(ctx.corpoElse),
                line=ctx.start.line,
            )
        return IfDecl(
            condicao=self.visit(ctx.expressao()),
            corpoIf=self.visit(ctx.corpoIF),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#iteracao_decl.
    def visitIteracao_decl(self, ctx: cminusParser.Iteracao_declContext):
        return WhileDecl(
            condicao=self.visit(ctx.expressao()),
            corpo=self.visit(ctx.statement()),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#retorno_decl.
    def visitRetorno_decl(self, ctx: cminusParser.Retorno_declContext):
        if ctx.expressao() is not None:
            return ReturnDecl(
                expressao=self.visit(ctx.expressao()),
                line=ctx.start.line,
            )
        return ReturnDecl(
            expressao=None,
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#expressao.
    def visitExpressao(self, ctx: cminusParser.ExpressaoContext):
        if ctx.simples_expressao() is not None:
            return ExpressaoDecl(
                var=None,
                expressao=None,
                simplesExpressao=self.visit(ctx.simples_expressao()),
                line=ctx.start.line,
            )
        return ExpressaoDecl(
            var=self.visit(ctx.var()),
            expressao=self.visit(ctx.expressao()),
            simplesExpressao=None,
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#var.
    def visitVar(self, ctx: cminusParser.VarContext):
        if ctx.expressao() is not None:
            return Variavel(
                id=ctx.ID().getText(),
                expressao=self.visit(ctx.expressao()),
                line=ctx.start.line,
            )
        return Variavel(
            id=ctx.ID().getText(),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#simples_expressao.
    def visitSimples_expressao(self, ctx: cminusParser.Simples_expressaoContext):
        if ctx.relacional:
            return Comp(
                esq=self.visit(ctx.esquerda),
                relacional=ctx.relacional.text,
                dir=self.visit(ctx.direita),
                line=ctx.start.line,
            )
        return  self.visit(ctx.operacao)

        # Visit a parse tree produced by cminusParser#soma_expressao.

    def visitSoma_expressao(self, ctx: cminusParser.Soma_expressaoContext):
        if ctx.op:
            return Operacao(
                esq=self.visit(ctx.soma_expressao()),
                op=ctx.op.text,
                dir=self.visit(ctx.termo()),
                line=ctx.start.line,
            )
        return self.visit(ctx.termo())

    # Visit a parse tree produced by cminusParser#termo.
    def visitTermo(self, ctx: cminusParser.TermoContext):
        if ctx.op:
            return Operacao(
                esq=self.visit(ctx.termo()),
                op=ctx.op.text,
                dir=self.visit(ctx.fator()),
                line = ctx.start.line,
            )
        return self.visit(ctx.fator())

    # Visit a parse tree produced by cminusParser#fator.
    def visitFator(self, ctx: cminusParser.FatorContext):
        if ctx.NUM():
            return numero(
                num=ctx.NUM().getText(),
                line=ctx.start.line,
            )
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cminusParser#ativacao.
    def visitAtivacao(self, ctx: cminusParser.AtivacaoContext):
        if ctx.arg_lista() is not None:
            return Ativ(
                id=ctx.ID().getText,
                argLista=self.visit(ctx.arg_lista()),
                line=ctx.start.line,
            )
        return Ativ(
            id=ctx.ID().getText,
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#arg_lista.
    def visitArg_lista(self, ctx: cminusParser.Arg_listaContext):
        if ctx.arg_lista() is not None:
            return ListaArgumentos(
                argLista=self.visit(ctx.arg_lista()),
                exp=self.visit(ctx.expressao()),
                line=ctx.start.line,
            )
        return self.visit(ctx.expressao())



class AstVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))






