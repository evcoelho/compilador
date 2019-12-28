from tabulate import tabulate

from project import createAST


class IntermedCode(createAST.AstVisitor):


    def __init__(self, ast_):
        self.intermediario = []
        self.line = -1
        self.temp = 0
        self.label = 0
        self.sys_call = ['input', 'output', 'flagrd',
                         'flagrsrt', 'loadhd', 'storehd',
                         'movehdmem', 'writeosmem', 'setprogos',
                         'savepcprog', 'setpcprog',
                         'printf', 'scanf', 'setInitialStack', 'setInitialMem', 'regtomem', 'memtoreg']
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

        lista_aux = ['function', no.id_, '', '']
        self.intermediario.append(lista_aux)
        self.visit(no.parametros)
        self.visit(no.declComp)
        # add um return
        if no.id_ != 'main':
            self.intermediario.append(['return', '0', '', ''])

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
        cond = self.visit(no.condicao)
        self.label += 1
        end_if = self.label
        self.label += 1
        end_else = self.label
        lista_aux = ['jump_if_false', cond, f'L{end_if}', '']
        self.intermediario.append(lista_aux)

        if no.corpoElse:
            for ci in no.corpoIf:
                self.visit(ci)

            lista_aux = ['go_to', f'L{end_else}', '', '']
            self.intermediario.append(lista_aux)

            lista_aux = ['label', f'L{end_if}', '', '']
            self.intermediario.append(lista_aux)
            for ce in no.corpoElse:
                self.visit(ce)
            lista_aux = ['label', f'L{end_else}', '', '']
            self.intermediario.append(lista_aux)

        else:
            for ci in no.corpoIf:
                self.visit(ci)
            lista_aux = ['label', f'L{end_if}', '', '']
            self.intermediario.append(lista_aux)


    def visit_WhileDecl(self, no: createAST.WhileDecl):
        self.label += 1
        label_start = self.label
        lista_aux = ['label', f'L{label_start}', '', '']
        self.intermediario.append(lista_aux)

        cond = self.visit(no.condicao)
        self.label += 1
        label_end = self.label

        lista_aux = ['jump_if_false', cond, f'L{label_end}', '']
        self.intermediario.append(lista_aux)

        self.visit(no.corpo)
        lista_aux = ['go_to', f'L{label_start}', '', '']
        self.intermediario.append(lista_aux)

        lista_aux = ['label', f'L{label_end}', '', '']
        self.intermediario.append(lista_aux)


    def visit_ReturnDecl(self, no: createAST.ReturnDecl):
        if no.expressao:
            x = self.visit(no.expressao)
            lista_aux = ['return', x, '', '']
            self.intermediario.append(lista_aux)
        else:
            lista_aux = ['return', '', '', '']
            self.intermediario.append(lista_aux)

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
            x = self.visit(no.esq)
            y = self.visit(no.dir)

            self.temp += 1
            if no.relacional == '<=':
                operacao = 'less_than_equal_to'
            elif no.relacional == '>=':
                operacao = 'greatest_than_equal_to'
            elif no.relacional == '==':
                operacao = 'equal_to'
            elif no.relacional == '!=':
                operacao = 'diferent_to'
            elif no.relacional == '<':
                operacao = 'less_than'
            elif no.relacional == '>':
                operacao = 'greatest_than'

            lista_aux = [operacao, x, y, f't{self.temp}']
            self.intermediario.append(lista_aux)
            return f't{self.temp}'



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
            # self.temp += 1
            # lista_aux = ['load_imediate', no.num, f't{self.temp}', '']
            # self.intermediario.append(lista_aux)
            # return f't{self.temp}'
            return no.num
        elif no.variavel:
            return self.visit(no.variavel)
        elif no.expressao:
            return self.visit(no.expressao)
        elif no.ativacao:
            return self.visit(no.ativacao)


    def visit_Ativ(self, no: createAST.Ativ):
        i = 0
        if no.argLista:
            if no.id_ in self.sys_call:
                call = 'sys_call'
            else:
                call = 'function_call'
            lista_aux = [call, f'{no.id_}']
            for arg in no.argLista:
                i += 1
                temp = self.visit(arg)
                self.intermediario.append(['arg', temp, '', ''])
            lista_aux.append(i)
            lista_aux.append('')
            self.intermediario.append(lista_aux)
            self.temp += 1
            if no.id_ != 'output' \
                    and no.id_ != 'flagrd' \
                    and no.id_ != 'flagrsrt' \
                    and no.id_ != 'movehdmem'\
                    and no.id_ != 'writeosmem' \
                    and no.id_ != 'setprogos' \
                    and no.id_ != 'savepcprog' \
                    and no.id_ != 'setpcprog' \
                    and no.id_ != 'printf' \
                    and no.id_ != 'setInitialStack' \
                    and no.id_ != 'setInitialMem'\
                    and no.id_ != 'regtomem'\
                    and no.id_ != 'memtoreg':
                lista_aux = ['assign_ret', f't{self.temp}', 'RT', '']
                self.intermediario.append(lista_aux)
                return f't{self.temp}'
        elif no.id_:
            if no.id_ in self.sys_call:
                call = 'sys_call'
            else:
                call = 'function_call'
            self.temp += 1
            lista_aux = [call, f'{no.id_}', '', '']
            if no.id_ == 'input' or no.id_ == 'scanf':
                self.intermediario.append(lista_aux)
                lista_aux = ['assign_ret', f't{self.temp}', 'RT', '']
            self.intermediario.append(lista_aux)
            return f't{self.temp}'
