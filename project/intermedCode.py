from tabulate import tabulate

from project import createAST




class intermedCode(createAST.AstVisitor):


    def __init__(self, ast_):
        self.intermediario = []
        self.line = -1
        self.temp = 0
        self.visit(ast_)


    def visit_Programa(self, no: createAST.Programa):
        for decl in no.decl_lista:
            if no.decl_lista is not None:
                self.visit(decl)

    def visit_Decl(self, no: createAST.Decl):
        if no.varDecl is not None:
            self.visit(no.varDecl)
        elif no.funDecl is not None:
            self.visit(no.funDecl)

    def visit_VarDecl(self, no: createAST.VarDecl):

        return

    """
    def visit_TipoEsp(self, no: createAST.TipoEsp):
        return
    """

    def visit_FunDecl(self, no: createAST.FunDecl):
        self.visit(no.parametros)
        self.visit(no.declComp)

    def visit_Parametros(self, no: createAST.Parametros):
        if no.listaParam:
            self.visit(no.listaParam)

    def visit_ListaParametros(self, no: createAST.ListaParametros):
        if no.listaParam:
            self.visit(no.listaParam)
            self.visit(no.param)
        else:
            self.visit(no.param)

    def visit_Param(self, no: createAST.Param):
        return

    def visit_CompDecl(self, no: createAST.CompDecl):
        for decls in no.localDecl:
            self.visit(decls)
        for stms in no.stmLista:
            self.visit(stms)

    def visit_LocalDeclaracoes(self, no: createAST.LocalDeclaracoes):
        for locD in no.varDecl:
            self.visit(locD)

    def visit_StatementLista(self, no: createAST.StatementLista):
        for stm in no.stm:
            self.visit(stm)

    def visit_Stm(self, no: createAST.Stm):
        if no.child:
            self.visit(no.child)

    def visit_ExpressaoDecl(self, no: createAST.ExpressaoDecl):
        if no.exp:
            self.visit(no.exp)

    def visit_IfDecl(self, no: createAST.IfDecl):
        self.visit(no.condicao)
        if no.corpoElse:
            for ci in no.corpoIf:
                self.visit(ci)

            for ce in no.corpoElse:
                self.visit(ce)
        else:
            for ci in no.corpoIf:
                self.visit(ci)

    def visit_WhileDecl(self, no: createAST.WhileDecl):
        self.visit(no.condicao)
        self.visit(no.corpo)


    def visit_ReturnDecl(self, no: createAST.ReturnDecl):
        if no.expressao:
            self.visit(no.expressao)


    def visit_Express(self, no: createAST.Express):
        if no.simplesExpressao:
            return self.visit(no.simplesExpressao)
        else:

            if no.var.expressao:
                k = self.visit(no.var.expressao)
                y = self.visit(no.expressao)
                self.temp += 1
                lista_aux = ['assign_end_vet', no.var.id_, k, f't{self.temp}']
                self.intermediario.append(lista_aux)
                lista_aux = ['assign', f't{self.temp}', y, '']
                self.intermediario.append(lista_aux)
            else:
                x = self.visit(no.var)
                y = self.visit(no.expressao)
                lista_aux = ['assign', x, y, '']
                self.intermediario.append(lista_aux)

    def visit_Variavel(self, no: createAST.Variavel):
        if no.expressao:
            x = self.visit(no.expressao)
            self.temp += 1
            lista_aux = ['assign_vet', no.id_, x, f't{self.temp}']
            self.intermediario.append(lista_aux)
            return f't{self.temp}'
        elif no.id_:
            return no.id_

    def visit_Comp(self, no: createAST.Comp):
        if no.operacao:
            return self.visit(no.operacao)
        else:
            self.visit(no.esq)
            self.visit(no.dir)

    def visit_Operacao(self, no: createAST.Operacao):
        if no.esq:
            x = self.visit(no.esq)
            y = self.visit(no.dir)

            self.temp += 1
            if no.op == '+':
                operacao = 'addition'
            elif no.op == '-':
                operacao = 'subtraction'
            elif no.op == '/':
                operacao = 'division'
            elif no.op == '*':
                operacao = 'multiplication'

            lista_aux = [operacao, x, y, f't{self.temp}']
            self.intermediario.append(lista_aux)
            return f't{self.temp}'

        else:
            return self.visit(no.dir)


    def visit_fat(self, no: createAST.fat):
        if no.num:
            return no.num
        elif no.variavel:
            return self.visit(no.variavel)
        elif no.expressao:
            return self.visit(no.expressao)
        elif no.ativacao:
            self.visit(no.ativacao)


    def visit_Ativ(self, no: createAST.Ativ):
        if no.argLista:
            for arg in no.argLista:
                self.visit(arg)
