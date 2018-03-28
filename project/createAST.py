from project.gen.cminusParser import cminusParser
from project.gen.cminusVisitor import cminusVisitor


class AstNo:
    def __init__(self, line = -1):
        self.line = line

class Programa(AstNo):
    def __init__(self,decl_lista, line = -1):
        super().__init__(line)
        self.decl_lista = decl_lista

        
class Decl(AstNo):
    def __init__(self, varDecl, funDecl, line = -1):
        super().__init__(line)
        self.varDecl = varDecl
        self.funDecl = funDecl
        
class VarDecl(AstNo):
    def __init__(self, tipo, id_, num=None, line = -1):
        super().__init__(line)
        self.tipo = tipo
        self.id_ = id_
        self.num = num
        
class TipoEsp(AstNo):
    def __init__(self, tipoE_, line = -1):
        super().__init__(line)
        self.tipoE = tipoE_

class FunDecl(AstNo):
    def __init__(self, tipoE, id_, parametros, declComp, line = -1):
        super().__init__(line)
        self.tipoE = tipoE
        self.id_ = id_
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
    def __init__(self, tipoEsp, id_, flagVet=None, line = -1):
        super().__init__(line)
        self.tipoEsp = tipoEsp
        self.id_ = id_
        self.flagVet = flagVet
        
class CompDecl(AstNo):
    def __init__(self, localDecl, stmLista, line = -1):
        super().__init__(line)
        self.localDecl = localDecl
        self.stmLista = stmLista

class LocalDeclaracoes(AstNo):
    def __init__(self, varDecl, line = -1):
        super().__init__(line)
        self.varDecl = varDecl
        
class StatementLista(AstNo):
    def __init__(self, stm, line = -1):
        super().__init__(line)
        self.stm = stm

class Stm(AstNo):
    def __init__(self, child, line = -1):
        super().__init__(line)
        self.child = child

class ExpressaoDecl(AstNo):
    def __init__(self, exp, line = -1):
        super().__init__(line)
        self.exp = exp

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
        
class Express(AstNo):
    def __init__(self, var, expressao, simplesExpressao, line = -1):
        super().__init__(line)
        self.var = var
        self.expressao = expressao
        self.simplesExpressao = simplesExpressao
        
class Variavel(AstNo):
    def __init__(self, id_, expressao=None, line = -1):
        super().__init__(line)
        self.id_ = id_
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
    def __init__(self, id_, argLista=None, line = -1):
        super().__init__(line)
        self.id_ = id_;
        self.argLista = argLista


class fat(AstNo):
    def __init__(self, num, variavel, ativacao, expressao, line = -1):
        super().__init__(line)
        self.num = num
        self.variavel = variavel
        self.ativacao = ativacao
        self.expressao = expressao


class CreateAst(cminusVisitor):
    # Visit a parse tree produced by cminusParser#programa.
    def visitPrograma(self, ctx: cminusParser.ProgramaContext):
        return Programa(
            decl_lista=[self.visit(decls) for decls in ctx.decl],
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#declaracao_lista.
    def visitDeclaracao(self, ctx: cminusParser.DeclaracaoContext):
        return Decl(
            varDecl=self.visit(ctx.var_declaracao()) if ctx.var_declaracao() is not None else None,
            funDecl=self.visit(ctx.fun_declaracao()) if ctx.fun_declaracao() is not None else None,
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#var_declaracao.
    def visitVar_declaracao(self, ctx: cminusParser.Var_declaracaoContext):
        if ctx.NUM() is not None:
            return VarDecl(
                tipo=(self.visit(ctx.tipo_especificador())),
                id_=ctx.ID().getText(),
                num=ctx.NUM().getText(),
                line=ctx.start.line,
            )
        return VarDecl(
            tipo=self.visit(ctx.tipo_especificador()),
            id_=ctx.ID().getText(),
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
            id_=ctx.ID().getText(),
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
            id_=ctx.ID().getText(),
            flagVet=True if ctx.LSBRACKET() else False,
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#composto_decl.
    def visitComposto_decl(self, ctx: cminusParser.Composto_declContext):
        return CompDecl(
            localDecl=[self.visit(decl) for decl in ctx.l_decl] if ctx.local_declaracoes() else [],
            stmLista=[self.visit(stm) for stm in ctx.stm_list] if ctx.statement_lista() else [],
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#local_declaracoes.
    def visitLocal_declaracoes(self, ctx: cminusParser.Local_declaracoesContext):
        return LocalDeclaracoes(
            varDecl=[self.visit(decl) for decl in ctx.var_decl],
            line=ctx.start.line,
        )
       
    # Visit a parse tree produced by cminusParser#statement_lista.
    def visitStatement_lista(self, ctx: cminusParser.Statement_listaContext):
        return StatementLista(
            stm=[self.visit(stm) for stm in ctx.stms],
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#statement.
    def visitStatement(self, ctx: cminusParser.StatementContext):
        if ctx.expressao_decl():
            return Stm(child=self.visit(ctx.expressao_decl()),
                       line=ctx.start.line,
                       )
        elif ctx.composto_decl():
            return Stm(child=self.visit(ctx.composto_decl()),
                       line=ctx.start.line,)
        elif ctx.selecao_decl():
            return Stm(child=self.visit(ctx.selecao_decl()),
                       line=ctx.start.line,)
        elif ctx.iteracao_decl():
            return Stm(child=self.visit(ctx.iteracao_decl()),
                       line=ctx.start.line,)
        elif ctx.retorno_decl():
            return Stm(child=self.visit(ctx.retorno_decl()),
                       line=ctx.start.line,)

    # Visit a parse tree produced by cminusParser#expressao_decl.
    def visitExpressao_decl(self, ctx: cminusParser.Expressao_declContext):
        return ExpressaoDecl(
            exp=self.visit(ctx.expressao()) if ctx.expressao() is not None else None,
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#selecao_decl.
    def visitSelecao_decl(self, ctx: cminusParser.Selecao_declContext):
        if ctx.corpoElse is not None:
            return IfDecl(
                condicao=self.visit(ctx.condicao),
                corpoIf=[self.visit(cif) for cif in ctx.corpoIF],
                corpoElse=[self.visit(cel) for cel in ctx.corpoElse],
                line=ctx.start.line,
            )
        return IfDecl(
            condicao=self.visit(ctx.expressao()),
            corpoIf=[self.visit(cif) for cif in ctx.corpoIF],
            corpoElse= [],
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
            return Express(
                var=None,
                expressao=None,
                simplesExpressao=self.visit(ctx.simples_expressao()),
                line=ctx.start.line,
            )
        return Express(
            var=self.visit(ctx.var()),
            expressao=self.visit(ctx.expressao()),
            simplesExpressao=None,
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#var.
    def visitVar(self, ctx: cminusParser.VarContext):
        if ctx.expressao() is not None:
            return Variavel(
                id_=ctx.ID().getText(),
                expressao=self.visit(ctx.expressao()),
                line=ctx.start.line,
            )
        return Variavel(
            id_=ctx.ID().getText(),
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#simples_expressao.
    def visitSimples_expressao(self, ctx: cminusParser.Simples_expressaoContext):
        return Comp(
            esq=self.visit(ctx.esquerda) if ctx.esquerda else None,
            relacional=ctx.relacional.text if ctx.relacional else None,
            dir=self.visit(ctx.direita) if ctx.direita else None,
            operacao=self.visit(ctx.operacao) if ctx.operacao else None,
            line=ctx.start.line,
        )


        # Visit a parse tree produced by cminusParser#soma_expressao.

    def visitSoma_expressao(self, ctx: cminusParser.Soma_expressaoContext):
        return Operacao(
            esq=self.visit(ctx.soma_expressao()) if ctx.soma_expressao() else None,
            op=ctx.op.text if ctx.op else None,
            dir=self.visit(ctx.termo()) if ctx.termo() else None,
            line=ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#termo.
    def visitTermo(self, ctx: cminusParser.TermoContext):
        return Operacao(
            esq=self.visit(ctx.termo()) if ctx.termo() else None,
            op=ctx.op.text if ctx.op else None,
            dir=self.visit(ctx.fator()) if ctx.fator() else None,
            line = ctx.start.line,
        )

    # Visit a parse tree produced by cminusParser#fator.
    def visitFator(self, ctx: cminusParser.FatorContext):
        return fat(
            num=ctx.NUM().getText() if ctx.NUM() else None,
            variavel=self.visit(ctx.var()) if ctx.var() else None,
            ativacao=self.visit(ctx.ativacao()) if ctx.ativacao() else None,
            expressao=self.visit(ctx.expressao()) if ctx.expressao() else None,
            line=ctx.start.line,
        )


    # Visit a parse tree produced by cminusParser#ativacao.
    def visitAtivacao(self, ctx: cminusParser.AtivacaoContext):
        return Ativ(
            id_=ctx.ID().getText(),
            argLista=[self.visit(args) for args in ctx.arg_list] if ctx.expressao() is not None else None,
            line=ctx.start.line,
        )



class AstVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))






