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
        for decl in no.decl_lista:
            self.visit(decl)

    def visit_Decl(self, no: createAST.Decl):
        if no.varDecl:
            self.visit(no.varDecl)
        elif no.funDecl:
            self.visit(no.funDecl)

    def visit_VarDecl(self, no: createAST.VarDecl):
        name = self.scoped_name(no.id_)
        if name in self.table:
            self.errors.append(f'{no.line}: Variable "{no.id_}" already declared')
            return False
        if no.id_ in self.table:
            self.errors.append(f'{no.line}: Variable "{no.id_}" shares name with a function')
        if no.tipo.tipoE == 'void':
            self.errors.append(f'{no.line}: Void variable cannot be declared')

        if no.num:
            self.table[name] = Symbol(no.id_, self._scope, no.line, 'var[]', no.tipo.tipoE)
        else:
            self.table[name] = Symbol(no.id_, self._scope, no.line, 'var', no.tipo.tipoE)
        return True

    """
    def visit_TipoEsp(self, no: createAST.TipoEsp):
        return
    """
    def visit_FunDecl(self, no: createAST.FunDecl):
        if no.id_ in self.table:
            self.errors.append(f'{no.line}: Function "{no.id_}" already declared')

        if self._scope == '':
            self.table[no.id_] = Symbol(no.id_, 'global', no.line, 'funct', no.tipoE.tipoE)
        else:
            self.table[no.id_] = Symbol(no.id_, self._scope, no.line, 'funct', no.tipoE.tipoE)

        self._scope = no.id_
        self.visit(no.parametros)
        self.visit(no.declComp)
        self._scope = ''

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
        name = self.scoped_name(no.id_)
        if name in self.table:
            self.errors.append(f'{no.line}: Variable "{no.id_}" already declared')
            return False
        if no.tipoEsp.tipoE == 'void':
            self.errors.append(f'{no.line}: Cannot declare void variable')

        if no.flagVet:
            self.table[name] = Symbol(no.id_, self._scope, no.line, 'var[]', no.tipoEsp.tipoE)
        else:
            self.table[name] = Symbol(no.id_, self._scope, no.line, 'var', no.tipoEsp.tipoE)

    def visit_CompDecl(self, no: createAST.CompDecl):
        if no.localDecl:
            for decl in no.localDecl:
                self.visit(decl)
        if no.stmLista:
            for stm in no.stmLista:
                self.visit(stm)

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
            self.visit(no.simplesExpressao)
        else:
            self.visit(no.var)
            if no.expressao.simplesExpressao:
                if no.expressao.simplesExpressao.operacao:
                    if no.expressao.simplesExpressao.operacao.dir:
                        if no.expressao.simplesExpressao.operacao.dir.dir:
                            if no.expressao.simplesExpressao.operacao.dir.dir.ativacao:
                                func = no.expressao.simplesExpressao.operacao.dir.dir.ativacao.id_
                                if func in self.table:
                                    if self.table[func].canonical_type == 'void':
                                        self.errors.append(f'{no.line}: Invalid Assignment of Type "void"')
            self.visit(no.expressao)





    def visit_Variavel(self, no: createAST.Variavel):
        name = self.scoped_name(no.id_)
        in_local_scope = name in self.table
        in_global_scope = no.id_ in self.table
        if in_local_scope:
            self.table[name].lines.add(no.line)
        elif in_global_scope:
            self.table[no.id_].lines.add(no.line)

        else:
            self.errors.append(f'{no.line}: Variable "{no.id_}" used without previous declaration')
            return False
        return True

    def visit_Comp(self, no: createAST.Comp):
        if no.relacional:
            self.visit(no.esq)
            self.visit(no.dir)
        else:
            self.visit(no.operacao)

    def visit_Operacao(self, no: createAST.Operacao):
        if no.esq:
            self.visit(no.esq)
            self.visit(no.dir)
        else:
            self.visit(no.dir)

    def visit_fat(self, no: createAST.fat):
        if no.variavel:
            self.visit(no.variavel)
        elif no.ativacao:
            self.visit(no.ativacao)
        elif no.expressao:
            self.visit(no.expressao)

    def visit_Ativ(self, no: createAST.Ativ):
        name = no.id_
        in_global_scope = name in self.table
        if not in_global_scope:
            self.errors.append(f'{no.line}: Function "{no.id_}" used without declaration')
            return False
        self.table[name].lines.add(no.line)
        for arg in no.argLista:
            self.visit(arg)

