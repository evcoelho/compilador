from project import createAST


class printAst(createAST.AstVisitor):
    def __init__(self):
        super().__init__()
        self.ident=0

    def visit_Programa(self, no: createAST.Programa):
        self.ident += 2

        print('Program:')
        print(' |' * self.ident, 'Declarations:')
        for decl in no.decl_lista:
            print(self.visit(decl))

        self.ident -= 2
""""
    def visit_Decl(self, no: createAST.Decl):


    def visit_VarDecl(self, no: createAST.VarDecl):


    def visit_TipoEsp(self, no: createAST.TipoEsp):


    def visit_FunDecl(self, no: createAST.FunDecl):


    def visit_Parametros(self, no: createAST.Parametros):


    def visit_ListaParametros(self, no: createAST.ListaParametros):


    def visit_Param(self, no: createAST.Param):


    def visit_CompDecl(self, no: createAST.CompDecl):


    def visit_LocalDeclaracoes(self, no: createAST.LocalDeclaracoes):


    def visit_StatementLista(self, no: createAST.StatementLista):


    def visit_ExpressaoDecl(self, no: createAST.ExpressaoDecl):


    def visit_IfDecl(self, no: createAST.IfDecl):


    def visit_WhileDecl(self, no: createAST.WhileDecl):

    def visit_ReturnDecl(self, no: createAST.ReturnDecl):


    def visit_Express(self, no: createAST.Express):


    def visit_Variavel(self, no: createAST.Variavel):


    def visit_Comp(self, no: createAST.Comp):


    def visit_Operacao(self, no: createAST.Operacao):


    def visit_Ativ(self, no: createAST.Ativ):


    def visit_numero(self, no: createAST.numero):

    """

