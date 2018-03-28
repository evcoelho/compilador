from project import createAST

IND = 2

class printAst(createAST.AstVisitor):
    def __init__(self):
        super().__init__()
        self.ident=0

    def visit_Programa(self, no: createAST.Programa):
        self.ident += IND

        print('Programa:{')
        print('|' * self.ident, 'Declarações:{')
        for decl in no.decl_lista:
            if no.decl_lista is not None:
                self.visit(decl)
        print('|' * self.ident, '}')
        print('}')
        self.ident -= IND


    def visit_Decl(self, no: createAST.Decl):
        self.ident += IND

        if no.varDecl is not None:
            print('|' * self.ident, "var:{")
            self.visit(no.varDecl)
            print('|' * self.ident, '}')
        elif no.funDecl is not None:
            print('|' * self.ident, "func:{")
            self.visit(no.funDecl)
            print('|' * self.ident, '}')

        self.ident -= IND

    def visit_VarDecl(self, no: createAST.VarDecl):
        self.ident += IND

        if no.num is not None:
            print('|' * self.ident, "tipo:", self.visit(no.tipo), " id:", no.id_, "tam vect: ", no.num)
        else:
            print('|' * self.ident, "tipo:", self.visit(no.tipo), " id:", no.id_)

        self.ident -= IND

    def visit_TipoEsp(self, no: createAST.TipoEsp):
        return no.tipoE

    def visit_FunDecl(self, no: createAST.FunDecl):
        self.ident += IND

        print('|' * self.ident, "tipo:", self.visit(no.tipoE), "id:", no.id_)
        print('|' * self.ident, "argumentos da função:{")
        self.visit(no.parametros)
        print('|' * self.ident, '}')
        print('|' * self.ident, "corpo da função:{")
        self.visit(no.declComp)
        print('|' * self.ident, '}')

        self.ident -= IND

    def visit_Parametros(self, no: createAST.Parametros):
        self.ident += IND

        if no.tipo:
            print('|' * self.ident, no.tipo)
        else:
            self.visit(no.listaParam)

        self.ident -= IND

    def visit_ListaParametros(self, no: createAST.ListaParametros):
        if no.listaParam:
            self.visit(no.listaParam)
            self.visit(no.param)
        else:
            self.visit(no.param)


    def visit_Param(self, no: createAST.Param):

        print('|' * self.ident, "tipo:", self.visit(no.tipoEsp), " id:", no.id_)

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

    def visit_ExpressaoDecl(self, no: createAST.ExpressaoDecl):
        if no.exp:
            self.visit(no.exp)

    def visit_IfDecl(self, no: createAST.IfDecl):
        self.ident += IND

        print('|' * self.ident, "declaracao if:{")
        print('|' * self.ident, "condicao:{")
        self.visit(no.condicao)
        print('|' * self.ident, '}')
        if no.corpoElse:
            print('|' * self.ident,"corpo if:{")
            for ci in no.corpoIf:
                self.visit(ci)
            print('|' * self.ident, '}')

            print('|' * self.ident,"corpo else:{")
            for ce in no.corpoElse:
                self.visit(ce)
            print('|' * self.ident, '}')
        else:
            print('|' * self.ident, "corpo if:{")
            for ci in no.corpoIf:
                self.visit(ci)
            print('|' * self.ident, '}')

        self.ident -= IND

    def visit_WhileDecl(self, no: createAST.WhileDecl):
        self.ident += IND

        print('|' * self.ident, "declaracao while:{")
        print('|' * self.ident, "condicao:{")
        self.visit(no.condicao)
        print('|' * self.ident, '}')
        print('|' * self.ident,"corpo while:{")
        self.visit(no.corpo)
        print('|' * self.ident, '}')
        self.ident -= IND

    def visit_ReturnDecl(self, no: createAST.ReturnDecl):
        self.ident += IND

        if no .expressao:
            print('|' * self.ident,"retorno:{")
            self.visit(no.expressao)
            print('|' * self.ident, '}')
        else:
            print('|' * self.ident,"retorno vazio")

        self.ident -= IND

    def visit_Express(self, no: createAST.Express):
        self.ident += IND

        if no.simplesExpressao:
            self.visit(no.simplesExpressao)
        else:
            print('|' * self.ident,"Atribuicao:{")
            self.visit(no.var)
            self.visit(no.expressao)
            print('|' * self.ident, '}')

        self.ident -= IND


    def visit_Variavel(self, no: createAST.Variavel):
        self.ident += IND

        print('|' * self.ident, "variavel:{")
        if no.expressao:
            print('|' * self.ident,"id:", no.id_)
            self.visit(no.expressao)
        else:
            print('|' * self.ident, "id:",no.id_)
        print('|' * self.ident, '}')

        self.ident -= IND

    def visit_Comp(self, no: createAST.Comp):
        self.ident += IND

        print('|' * self.ident, "simples expressao:{")
        if no.operacao:
            self.visit(no.operacao)
        else:
            print('|' * self.ident, "esquerda:{")
            self.visit(no.esq)
            print('|' * self.ident, '}')
            print('|' * self.ident, no.relacional)
            print('|' * self.ident, "direita:{")
            self.visit(no.dir)
            print('|' * self.ident, '}')
        print('|' * self.ident, '}')

        self.ident -= IND

    def visit_Operacao(self, no: createAST.Operacao):
        self.ident += IND

        print('|' * self.ident, "operacao:{")
        self.visit(no.esq)
        print('|' * self.ident, no.op)
        self.visit(no.dir)
        print('|' * self.ident, '}')

        self.ident -= IND

    def visit_numero(self, no: createAST.numero):
        self.ident += IND

        print('|' * self.ident, "Numero:", no.num)

        self.ident -= IND

    def visit_Ativ(self, no: createAST.Ativ):
        self.ident += IND

        print('|' * self.ident, "chamada de func:{")
        print('|' * self.ident, "id:", no.id_)
        if no.argLista:
            print('|' * self.ident, "argumentos:{")
            for arg in no.argLista:
                self.visit(arg)
            print('|' * self.ident, '}')
        print('|' * self.ident, '}')

        self.ident -= IND



