from project import createAST



class print_ast_json(createAST.AstVisitor):

    def visit_Programa(self, no: createAST.Programa):

        return {
            'Programa:': {
                'Declaracoes:': [self.visit(decl) for decl in no.decl_lista] if no.decl_lista else []
            }

        }

    def visit_Decl(self, no: createAST.Decl):
        return {
            'Globais': self.visit(no.varDecl) if no.varDecl else None,
            'Funcoes': self.visit(no.funDecl) if no.funDecl else None,
        }

    def visit_VarDecl(self, no: createAST.VarDecl):

        if no.num:
            return {
                'variavel:': {
                    'tipo:': self.visit(no.tipo),
                    'id:': no.id_,
                    'tam vect:': no.num,
                }
            }
        else:
            return {
                'variavel:': {
                    'tipo:': self.visit(no.tipo),
                    'id:': no.id_,
                }
            }

    def visit_TipoEsp(self, no: createAST.TipoEsp):
        return no.tipoE

    def visit_FunDecl(self, no: createAST.FunDecl):
        return {
            'funcao:':{
                'tipo:': self.visit(no.tipoE),
                'id:': no.id_,
                'corpo da funcao:':{
                    'parametros': self.visit(no.parametros),
                    'corpo': self.visit(no.declComp)
                }
            }

        }


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

    def visit_Ativ(self, no: createAST.Ativ):
        return

    def visit_numero(self, no: createAST.numero):
        return
