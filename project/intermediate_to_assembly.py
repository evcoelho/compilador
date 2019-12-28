
from project import intermedCode
from project import semanticAnalysis
import re


class IntermediateToAssembly:

    def __init__(self, semantic: semanticAnalysis.SemanticAnalysisTableG, intermediate: intermedCode.IntermedCode):
        self.assembly = []
        self.semantic_table = semantic.table
        self.intermediate = intermediate
        self.stack_register = []
        self.stack_args = []
        self.stack_vars = []
        self.temp_to_register = {}
        self.status_reg = []
        self.inicialize_reg_list()
        self.scope = 'global'
        self.convertToAssembly()

    def convertToAssembly(self):

        self.assembly.append(['loadi', '$r0', '0'])
        self.assembly.append(['loadi', '$stp', '0'])
        self.assembly.append(['loadi', '$ra', '0'])
        self.assembly.append(['jmpi', 'main'])
        for inter in self.intermediate.intermediario:

            if inter[0] == 'function':
                self.assembly.append([f'{inter[1]}:'])
                self.scope = inter[1]
                lista_args = self.semantic_table[inter[1]].args
                for i in range(0, self.get_qtd_args_function(inter[1])):
                    type = self.search_type(lista_args[i])
                    RD = self.ret_reg_free()

                    if type == 'var':
                        pos_men = self.get_mem_pos(lista_args[i])
                        self.assembly.append(['subi', f'$stp', '$stp', '1'])
                        self.assembly.append(['pop', f'$r{RD}', '$stp'])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['store', f'$r{RD}', f'$rl'])
                    self.free_reg(RD)


            if inter[0] == 'label':
                self.assembly.append([f'{inter[1]}.'])

            if inter[0] == 'equal_to':
                line = self.operation_instructions(inter)
                line[0] = 'eq'
                self.assembly.append(line)

            if inter[0] == 'less_than_equal_to':
                line = self.operation_instructions(inter)
                line[0] = 'nab'
                self.assembly.append(line)

            if inter[0] == 'greatest_than_equal_to':
                line = self.operation_instructions(inter)
                line[0] = 'nlt'
                self.assembly.append(line)

            if inter[0] == 'diferent_to':
                line = self.operation_instructions(inter)
                line[0] = 'neq'
                self.assembly.append(line)

            if inter[0] == 'less_than':
                line = self.operation_instructions(inter)
                line[0] = 'lt'
                self.assembly.append(line)

            if inter[0] == 'greatest_than':
                line = self.operation_instructions(inter)
                line[0] = 'abv'
                self.assembly.append(line)

            if inter[0] == 'jump_if_false':
                type1 = self.search_type(inter[1])
                RS = self.ret_reg_free()
                if type1 == 'var':
                    pos_men = self.get_mem_pos(inter[1])
                    self.assembly.append(['loadi', f'$rl', pos_men])
                    self.assembly.append(['load', f'$r{RS}', '$rl'])
                elif type1 == 'imt':
                    self.assembly.append(['loadi', f'$r{RS}', inter[1]])
                elif type1 == 'temp':
                    if inter[1] in self.temp_to_register:
                        self.free_reg(RS)
                        RS = self.temp_to_register[inter[1]]
                self.assembly.append(['jei', f'$r0', f'$r{RS}', inter[2]])
                self.free_reg(RS)
                self.temp_to_register[inter[1]] = -1

            if inter[0] == 'addition':
                line = self.operation_instructions(inter)
                line[0] = 'add'
                self.assembly.append(line)

            if inter[0] == 'subtraction':
                line = self.operation_instructions(inter)
                line[0] = 'sub'
                self.assembly.append(line)

            if inter[0] == 'division':
                line = self.operation_instructions(inter)
                line[0] = 'div'
                self.assembly.append(line)

            if inter[0] == 'multiplication':
                line = self.operation_instructions(inter)
                line[0] = 'mult'
                self.assembly.append(line)

            if inter[0] == 'assign':
                type1 = self.search_type(inter[1])
                RS = self.ret_reg_free()

                if type1 == 'var':
                    pos_men = self.get_mem_pos(inter[1])
                    self.assembly.append(['loadi', f'$r{RS}', pos_men])
                elif type1 == 'imt':
                    self.assembly.append(['loadi', f'$r{RS}', inter[1]])
                elif type1 == 'temp':
                    if inter[1] in self.temp_to_register:
                        self.free_reg(RS)
                        RS = self.temp_to_register[inter[1]]

                type2 = self.search_type(inter[2])
                RD = self.ret_reg_free()

                if type2 == 'var':
                    pos_men = self.get_mem_pos(inter[2])
                    self.assembly.append(['loadi', f'$rl', pos_men])
                    self.assembly.append(['load', f'$r{RD}', f'$rl'])
                elif type2 == 'imt':
                    self.assembly.append(['loadi',  f'$r{RD}', inter[2]])
                elif type2 == 'temp':
                    if inter[2] in self.temp_to_register:
                        self.free_reg(RD)
                        RD = self.temp_to_register[inter[2]]

                self.assembly.append(['store', f'$r{RD}', f'$r{RS}'])
                self.free_reg(RS)
                self.temp_to_register[inter[1]] = -1
                self.free_reg(RD)
                self.temp_to_register[inter[2]] = -1

            if inter[0] == 'return':
                type1 = self.search_type(inter[1])
                RS = self.ret_reg_free()

                if type1 == 'var':
                    pos_men = self.get_mem_pos(inter[1])
                    self.assembly.append(['loadi', f'$r{RS}', pos_men])
                    self.assembly.append(['load', f'$rt', f'$r{RS}'])
                elif type1 == 'imt':
                    self.assembly.append(['loadi', f'$rt', inter[1]])
                elif type1 == 'temp':
                    if inter[1] in self.temp_to_register:
                        self.free_reg(RS)
                        RS = self.temp_to_register[inter[1]]
                        self.assembly.append(['move', f'$rt', f'$r{RS}'])
                self.assembly.append(['jmp', f'$ra'])
                self.free_reg(RS)
                self.temp_to_register[inter[1]] = -1
                self.free_all_reg()

            if inter[0] == 'function_call':
                self.push_temp_ocuped_in_stack()
                if inter[1] == self.scope:
                    # print(f'{inter[1]} esta no escopo:{self.scope}')
                    self.push_vars_in_scope()
                for i in range(0, inter[2]):
                    arg = self.stack_args.pop()
                    type1 = self.search_type(arg[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg[1])
                        if self.is_a_vet(arg[1]):
                            if self.is_a_parameter(arg[1]):
                                self.assembly.append(['loadi', f'$rl', pos_men])
                                self.assembly.append(['load', f'$r{RS}', f'$rl'])
                            else:
                                self.assembly.append(['loadi', f'$r{RS}', pos_men])
                        else:
                            self.assembly.append(['loadi', f'$rl', pos_men])
                            self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg[1]])
                    elif type1 == 'temp':
                        if arg[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg[1]]

                    self.assembly.append(['push', f'$r{RS}', '$stp'])
                    self.assembly.append(['addi', f'$stp', '$stp', '1'])

                    self.free_reg(RS)
                    self.temp_to_register[inter[1]] = -1

                self.assembly.append(['jal', inter[1]])
                if inter[1] == self.scope:
                    self.pop_vars_in_scope()
                self.pop_temp_ocuped_in_stack()

            if inter[0] == 'arg':
                self.stack_args.append(inter)

            if inter[0] == 'assign_ret':
                if self.search_type(inter[1]) == 'temp':
                    self.temp_to_register[inter[1]] = self.ret_reg_free()
                    RD = self.temp_to_register[inter[1]]
                self.assembly.append(['move', f'$r{RD}', f'$rt'])

            if inter[0] == 'sys_call':
                if inter[1] == 'input':
                    self.assembly.append(['in', f'$rt'])

                if inter[1] == 'output':
                    arg = self.stack_args.pop()
                    type1 = self.search_type(arg[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg[1]])
                    elif type1 == 'temp':
                        if arg[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg[1]]
                    self.assembly.append(['out', f'$r{RS}'])
                    self.free_reg(RS)
                    self.temp_to_register[arg[1]] = -1

                if inter[1] == 'flagrd':
                    self.assembly.append(['flagrd', ' '])

                if inter[1] == 'flagrsrt':
                    self.assembly.append(['flagrsrt', ' '])

                if inter[1] == 'movehdmem':

                    arg3 = self.stack_args.pop()
                    type1 = self.search_type(arg3[1])
                    RT = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg3[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RT}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RT}', arg3[1]])
                    elif type1 == 'temp':
                        if arg3[1] in self.temp_to_register:
                            self.free_reg(RT)
                            RT = self.temp_to_register[arg3[1]]

                    arg2 = self.stack_args.pop()
                    type1 = self.search_type(arg2[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg2[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg2[1]])
                    elif type1 == 'temp':
                        if arg2[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg2[1]]

                    arg1 = self.stack_args.pop()
                    type1 = self.search_type(arg1[1])
                    RD = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg1[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RD}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RD}', arg1[1]])
                    elif type1 == 'temp':
                        if arg1[1] in self.temp_to_register:
                            self.free_reg(RD)
                            RD = self.temp_to_register[arg1[1]]

                    self.assembly.append(['movehdmem', f'$r{RD}', f'$r{RS}', f'$r{RT}'])
                    self.free_reg(RD)
                    self.free_reg(RS)
                    self.free_reg(RT)
                    self.temp_to_register[arg1[1]] = -1
                    self.temp_to_register[arg2[1]] = -1
                    self.temp_to_register[arg3[1]] = -1

                if inter[1] == 'writeosmem':
                    arg3 = self.stack_args.pop()
                    type1 = self.search_type(arg3[1])
                    RT = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg3[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RT}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RT}', arg3[1]])
                    elif type1 == 'temp':
                        if arg3[1] in self.temp_to_register:
                            self.free_reg(RT)
                            RT = self.temp_to_register[arg3[1]]

                    arg2 = self.stack_args.pop()
                    type1 = self.search_type(arg2[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg2[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg2[1]])
                    elif type1 == 'temp':
                        if arg2[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg2[1]]

                    arg1 = self.stack_args.pop()
                    type1 = self.search_type(arg1[1])
                    RD = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg1[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RD}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RD}', arg1[1]])
                    elif type1 == 'temp':
                        if arg1[1] in self.temp_to_register:
                            self.free_reg(RD)
                            RD = self.temp_to_register[arg1[1]]

                    self.assembly.append(['writeosmem', f'$r{RD}', f'$r{RS}', f'$r{RT}'])
                    self.free_reg(RD)
                    self.free_reg(RS)
                    self.free_reg(RT)
                    self.temp_to_register[arg1[1]] = -1
                    self.temp_to_register[arg2[1]] = -1
                    self.temp_to_register[arg3[1]] = -1

                if inter[1] == 'setprogos':
                    self.assembly.append(['setprogos', ' '])

                if inter[1] == 'savepcprog':
                    self.assembly.append(['savepcprog', ' '])

                if inter[1] == 'setpcprog':
                    self.assembly.append(['setpcprog', '$rpc'])

                if inter[1] == 'printf':
                    arg = self.stack_args.pop()
                    type1 = self.search_type(arg[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg[1]])
                    elif type1 == 'temp':
                        if arg[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg[1]]
                    self.assembly.append(['move', f'rout', f'$r{RS}'])
                    self.assembly.append(['loadi', f'$interrupt', '1'])
                    self.assembly.append(['setprogos', ' '])
                    self.free_reg(RS)
                    self.temp_to_register[arg[1]] = -1

                if inter[1] == 'scanf':
                    self.assembly.append(['loadi', f'$interrupt', '2'])
                    self.assembly.append(['setprogos', ' '])

                if inter[1] == 'setInicialStack':
                    arg = self.stack_args.pop()
                    type1 = self.search_type(arg[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg[1]])
                    elif type1 == 'temp':
                        if arg[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg[1]]
                    self.assembly.append(['move', f'$stp', f'$r{RS}'])
                    self.free_reg(RS)
                    self.temp_to_register[arg[1]] = -1

                if inter[1] == 'setInicialMem':
                    arg = self.stack_args.pop()
                    type1 = self.search_type(arg[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg[1]])
                    elif type1 == 'temp':
                        if arg[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg[1]]
                    self.assembly.append(['move', f'$rmem', f'$r{RS}'])
                    self.free_reg(RS)
                    self.temp_to_register[arg[1]] = -1

                if inter[1] == 'regtomem':
                    arg2 = self.stack_args.pop()
                    type1 = self.search_type(arg2[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg2[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg2[1]])
                    elif type1 == 'temp':
                        if arg2[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg2[1]]

                    arg1 = self.stack_args.pop()
                    type1 = self.search_type(arg1[1])
                    RD = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg1[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RD}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RD}', arg1[1]])
                    elif type1 == 'temp':
                        if arg1[1] in self.temp_to_register:
                            self.free_reg(RD)
                            RD = self.temp_to_register[arg1[1]]

                    self.assembly.append(['store', f'$r{RD}', f'$r{RS}'])
                    self.free_reg(RD)
                    self.free_reg(RS)
                    self.temp_to_register[arg1[1]] = -1
                    self.temp_to_register[arg2[1]] = -1

                if inter[1] == 'memtoreg':
                    arg2 = self.stack_args.pop()
                    type1 = self.search_type(arg2[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg2[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RS}', arg2[1]])
                    elif type1 == 'temp':
                        if arg2[1] in self.temp_to_register:
                            self.free_reg(RS)
                            RS = self.temp_to_register[arg2[1]]

                    arg1 = self.stack_args.pop()
                    type1 = self.search_type(arg1[1])
                    RD = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(arg1[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RD}', f'$rl'])
                    elif type1 == 'imt':
                        self.assembly.append(['loadi', f'$r{RD}', arg1[1]])
                    elif type1 == 'temp':
                        if arg1[1] in self.temp_to_register:
                            self.free_reg(RD)
                            RD = self.temp_to_register[arg1[1]]

                    self.assembly.append(['load', f'$r{RD}', f'$r{RS}'])
                    self.free_reg(RD)
                    self.free_reg(RS)
                    self.temp_to_register[arg1[1]] = -1
                    self.temp_to_register[arg2[1]] = -1

            if inter[0] == 'go_to':
                self.assembly.append(['jmpi', f'{inter[1]}'])

            if inter[0] == 'assign_end_vet': # passagem de vetor como parametro tratado
                if self.is_a_parameter(inter[1]):
                    # self.assembly.append(['----------------------------'])
                    type1 = self.search_type(inter[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(inter[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', '$rl'])

                    type2 = self.search_type(inter[2])
                    RD = self.ret_reg_free()

                    if type2 == 'var':
                        pos_men = self.get_mem_pos(inter[2])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RD}', f'$rl'])
                    elif type2 == 'imt':
                        self.assembly.append(['loadi', f'$r{RD}', inter[2]])
                    elif type2 == 'temp':
                        if inter[2] in self.temp_to_register:
                            self.free_reg(RD)
                            RD = self.temp_to_register[inter[2]]

                    if self.search_type(inter[3]) == 'temp':
                        self.temp_to_register[inter[3]] = self.ret_reg_free()
                        RT = self.temp_to_register[inter[3]]

                    self.assembly.append(['add', f'$r{RT}', f'$r{RS}', f'$r{RD}'])
                    self.free_reg(RS)
                    self.temp_to_register[inter[1]] = -1
                    self.free_reg(RD)
                    self.temp_to_register[inter[2]] = -1
                    # self.assembly.append(['----------------------------'])
                else:
                    # self.assembly.append(['----------------------------'])
                    type1 = self.search_type(inter[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(inter[1])
                        self.assembly.append(['loadi', f'$r{RS}', pos_men])

                    type2 = self.search_type(inter[2])
                    RD = self.ret_reg_free()

                    if type2 == 'var':
                        pos_men = self.get_mem_pos(inter[2])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RD}', f'$rl'])
                    elif type2 == 'imt':
                        self.assembly.append(['loadi', f'$r{RD}', inter[2]])
                    elif type2 == 'temp':
                        if inter[2] in self.temp_to_register:
                            self.free_reg(RD)
                            RD = self.temp_to_register[inter[2]]

                    if self.search_type(inter[3]) == 'temp':
                        self.temp_to_register[inter[3]] = self.ret_reg_free()
                        RT = self.temp_to_register[inter[3]]

                    self.assembly.append(['add', f'$r{RT}', f'$r{RS}', f'$r{RD}'])
                    self.free_reg(RS)
                    self.temp_to_register[inter[1]] = -1
                    self.free_reg(RD)
                    self.temp_to_register[inter[2]] = -1
                    # self.assembly.append(['----------------------------'])

            if inter[0] == 'assign_vet': # tratar passagem de vetor como parametro
                # self.assembly.append(['----------------------------'])
                if self.is_a_parameter(inter[1]):
                    type1 = self.search_type(inter[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(inter[1])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RS}', '$rl'])

                    type2 = self.search_type(inter[2])
                    RD = self.ret_reg_free()

                    if type2 == 'var':
                        pos_men = self.get_mem_pos(inter[2])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RD}', f'$rl'])
                    elif type2 == 'imt':
                        self.assembly.append(['loadi', f'$r{RD}', inter[2]])
                    elif type2 == 'temp':
                        if inter[2] in self.temp_to_register:
                            self.free_reg(RD)
                            RD = self.temp_to_register[inter[2]]

                    if self.search_type(inter[3]) == 'temp':
                        self.temp_to_register[inter[3]] = self.ret_reg_free()
                        RT = self.temp_to_register[inter[3]]
                    rd = self.ret_reg_free()
                    self.assembly.append(['add', f'$r{rd}', f'$r{RS}', f'$r{RD}'])
                    self.assembly.append(['load', f'$r{RT}', f'$r{rd}'])
                    self.free_reg(rd)
                    self.free_reg(RS)
                    self.temp_to_register[inter[1]] = -1
                    self.free_reg(RD)
                    self.temp_to_register[inter[2]] = -1
                else:
                    type1 = self.search_type(inter[1])
                    RS = self.ret_reg_free()

                    if type1 == 'var':
                        pos_men = self.get_mem_pos(inter[1])
                        self.assembly.append(['loadi', f'$r{RS}', pos_men])

                    type2 = self.search_type(inter[2])
                    RD = self.ret_reg_free()

                    if type2 == 'var':
                        pos_men = self.get_mem_pos(inter[2])
                        self.assembly.append(['loadi', f'$rl', pos_men])
                        self.assembly.append(['load', f'$r{RD}', f'$rl'])
                    elif type2 == 'imt':
                        self.assembly.append(['loadi', f'$r{RD}', inter[2]])
                    elif type2 == 'temp':
                        if inter[2] in self.temp_to_register:
                            self.free_reg(RD)
                            RD = self.temp_to_register[inter[2]]

                    if self.search_type(inter[3]) == 'temp':
                        self.temp_to_register[inter[3]] = self.ret_reg_free()
                        RT = self.temp_to_register[inter[3]]
                    rd = self.ret_reg_free()
                    self.assembly.append(['add', f'$r{rd}', f'$r{RS}', f'$r{RD}'])
                    self.assembly.append(['load', f'$r{RT}', f'$r{rd}'])
                    self.free_reg(rd)
                    self.free_reg(RS)
                    self.temp_to_register[inter[1]] = -1
                    self.free_reg(RD)
                    self.temp_to_register[inter[2]] = -1
                    # self.assembly.append(['----------------------------'])

    def is_a_vet(self, vet):
        name = f'{self.scope}.{vet}'
        if name in self.semantic_table:
            if self.semantic_table[name].id_type == 'var[]':
                return True
        name = f'global.{vet}'
        if name in self.semantic_table:
            if self.semantic_table[name].id_type == 'var[]':
                return True
        return False

    def is_a_parameter(self, var):
        if self.scope in self.semantic_table:
            parameters = self.semantic_table[self.scope].args
            if var in parameters:
                return True
        return False

    def is_a_arg(self, name):
        for arg in self.stack_args:
            type1 = self.search_type(arg[1])
            if type1 == 'temp':
                if arg[1] in self.temp_to_register:
                    RS = self.temp_to_register[arg[1]]
                    if name == RS:
                        return True
        return False

    def push_vars_in_scope(self):
        # self.assembly.append(['............................................'])
        for key in self.semantic_table:
            if re.match(f'{self.scope}.[a-zA-Z]', key):
                RS = self.ret_reg_free()
                pos_men = self.get_mem_pos(self.semantic_table[key].name)
                self.stack_vars.append(self.semantic_table[key].name)
                self.assembly.append(['loadi', f'$rl', pos_men])
                self.assembly.append(['load', f'$r{RS}', f'$rl'])
                self.assembly.append(['push', f'$r{RS}', f'$stp'])
                self.assembly.append(['addi', f'$stp', '$stp', '1'])
                self.free_reg(RS)
        # self.assembly.append(['............................................'])

    def pop_vars_in_scope(self):
        # self.assembly.append(['............................................'])
        for i in range(0, len(self.stack_vars)):

                register = self.ret_reg_free()
                var = self.stack_vars.pop()
                pos_men = self.get_mem_pos(var)
                self.assembly.append(['subi', f'$stp', '$stp', '1'])
                self.assembly.append(['pop', f'$r{register}', '$stp'])
                self.assembly.append(['loadi', f'$rl', pos_men])
                self.assembly.append(['store', f'$r{register}', '$rl'])
                self.free_reg(register)
        # self.assembly.append(['............................................'])

    def push_temp_ocuped_in_stack(self):

        # self.assembly.append(['-----------------------------------------------'])
        self.assembly.append(['push', f'$ra', '$stp'])
        self.assembly.append(['addi', f'$stp', '$stp', '1'])
        for reg in self.status_reg:
            if reg[1] == 0:
                reg[1] = 1
                if not self.is_a_arg(reg[0]):
                    self.stack_register.append(reg[0])
                    self.assembly.append(['push', f'$r{reg[0]}', '$stp'])
                    self.assembly.append(['addi', f'$stp', '$stp', '1'])

        # self.assembly.append(['-----------------------------------------------'])

    def pop_temp_ocuped_in_stack(self):
        # self.assembly.append(['-----------------------------------------------'])
        for i in range(0, len(self.stack_register)):
            register = self.stack_register.pop()
            self.status_reg[register-1][1] = 0
            self.assembly.append(['subi', f'$stp', '$stp', '1'])
            self.assembly.append(['pop', f'$r{register}', '$stp'])
        self.assembly.append(['subi', f'$stp', '$stp', '1'])
        self.assembly.append(['pop', f'$ra', '$stp'])

        # self.assembly.append(['-----------------------------------------------'])

    def operation_instructions(self,inst):

        type1 = self.search_type(inst[1])
        RS = self.ret_reg_free()

        if type1 == 'var':
            pos_men = self.get_mem_pos(inst[1])
            self.assembly.append(['loadi', f'$rl', pos_men])
            self.assembly.append(['load', f'$r{RS}', f'$rl'])
        elif type1 == 'imt':
            self.assembly.append(['loadi', f'$r{RS}', inst[1]])
        elif type1 == 'temp':
            if inst[1] in self.temp_to_register:
                self.free_reg(RS)
                RS = self.temp_to_register[inst[1]]

        type2 = self.search_type(inst[2])
        RT = self.ret_reg_free()

        if type2 == 'var':
            pos_men = self.get_mem_pos(inst[2])
            self.assembly.append(['loadi', f'$rl', pos_men])
            self.assembly.append(['load', f'$r{RT}', f'$rl'])
        elif type2 == 'imt':
            self.assembly.append(['loadi', f'$r{RT}', inst[2]])
        elif type2 == 'temp':
            if inst[2] in self.temp_to_register:
                self.free_reg(RT)
                RT = self.temp_to_register[inst[2]]

        if self.search_type(inst[3]) == 'temp':
            self.temp_to_register[inst[3]] = self.ret_reg_free()
            RD = self.temp_to_register[inst[3]]

        self.free_reg(RS)
        self.temp_to_register[inst[1]] = -1
        self.free_reg(RT)
        self.temp_to_register[inst[2]] = -1
        return ['', f'$r{RD}', f'$r{RS}', f'$r{RT}']

    def get_mem_pos(self,var):
        name = f'{self.scope}.{var}'
        if name in self.semantic_table:
            return self.semantic_table[name].pos_mem
        name = f'global.{var}'
        if name in self.semantic_table:
            return self.semantic_table[name].pos_mem

    def get_qtd_args_function(self, name):
        func = self.semantic_table[name]
        return func.qtd_args

    def free_reg(self, reg):
        for i in self.status_reg:
            if i[0] == reg:
                i[1] = 1
                return 1
        return 0

    def free_all_reg(self):
        for i in self.status_reg:
            if i[1] == 0:
                i[1] = 1
        return 1

    def ret_reg_free(self):
        for reg in self.status_reg:
            if reg[1] == 1:
                reg[1] = 0
                return reg[0]

    def inicialize_reg_list(self):
        cont = 1
        while cont < 21:
            self.status_reg.append([cont, 1])
            cont += 1

    def search_type(self, string):
        x=''
        if re.match('t[0-9]', string):
            x = 'temp'
        elif re.match('[0-9]', string):
            x = 'imt'
        elif re.match('[a-zA-Z]', string):
            x = 'var'
        return x
