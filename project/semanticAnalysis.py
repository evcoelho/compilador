from tabulate import tabulate

from project import createAST


class Symbol:
    def __init__(self, name, scope, line, id_type, canonical_type):
        self.name = name
        self.scope = scope
        self.lines = {line}
        self.id_type = id_type
        self.canonical_type = canonical_type

    def as_tuple(self):
        return self.name, self.scope, ', '.join(map(str, sorted(self.lines))), self.id_type, self.canonical_type


class semanticAnalysisTableG(createAST.AstVisitor):
    def __init__(self, ast_):
        self.table = {}
        self.errors = []
        self._scope = ''

        self.visit(ast_)

        if 'main' not in self.table:
            self.errors.append(f'No main function declared')

    def __str__(self):
        return tabulate(
            tabular_data=[(key,) + symbol.as_tuple() for key, symbol in self.table.items()],
            headers=['Key', 'Name', 'Scope', 'Lines', 'Id Type', 'Data Type'],
            tablefmt='grid',
        )

    def scoped_name(self, name):
        if not self._scope:
            return name
        return f'{self._scope}.{name}'

    def visit_Programa(self, no: createAST.Programa):
        return

    def visit_Decl(self, no: createAST.Decl):
        return

    def visit_VarDecl(self, no: createAST.VarDecl):
        return

    def visit_TipoEsp(self, no: createAST.TipoEsp):
        return

    def visit_FunDecl(self, no: createAST.FunDecl):
        return

    def visit_Parametros(self, no: createAST.Parametros):
        return

    def visit_ListaParametros(self, no: createAST.ListaParametros):
        return

    def visit_Param(self, no: createAST.Param):
        return

    def visit_CompDecl(self, no: createAST.CompDecl):
        return

    def visit_LocalDeclaracoes(self, no: createAST.LocalDeclaracoes):
        return

    def visit_StatementLista(self, no: createAST.StatementLista):
        return

    def visit_ExpressaoDecl(self, no: createAST.ExpressaoDecl):
        return

    def visit_IfDecl(self, no: createAST.IfDecl):
        return

    def visit_WhileDecl(self, no: createAST.WhileDecl):
        return

    def visit_ReturnDecl(self, no: createAST.ReturnDecl):
        return

    def visit_Express(self, no: createAST.Express):
        return

    def visit_Variavel(self, no: createAST.Variavel):
        return

    def visit_Comp(self, no: createAST.Comp):
        return

    def visit_Operacao(self, no: createAST.Operacao):
        return

    def visit_numero(self, no: createAST.numero):
        return

    def visit_Ativ(self, no: createAST.Ativ):
        return
