
from project import intermedCode
from project import  semanticAnalysis
import re


class IntermediateToAssembly:

    def __init__(self, semantic: semanticAnalysis.SemanticAnalysisTableG, intermediate: intermedCode.IntermedCode):
        self.assembly = []
        self.semantic_table = semantic.table
        self.intermediate = intermediate
        self.stack_register = []
        self.stack_args = []
        self.temp_to_register = {}
        self.status_reg = []
        self.inicialize_reg_list()
        self.scope = ''
        self.convertToAssembly()

    def convertToAssembly(self):

        self.assembly.append(['loadi', '$r0', '0'])
        self.assembly.append(['jmp', 'main'])
        for inter in self.intermediate.intermediario:

            if inter[0] == 'function':
                self.assembly.append([f'{inter[1]}:'])
                self.scope = inter[1]

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
                    self.assembly.append(['load', f'$r{RS}', pos_men])
                elif type1 == 'imt':
                    self.assembly.append(['loadi', f'$r{RS}', inter[1]])
                elif type1 == 'temp':
                    if inter[1] in self.temp_to_register:
                        RS = self.temp_to_register[inter[1]]
                self.assembly.append(['je', f'$r0', f'$r{RS}', inter[2]])
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
                    self.assembly.append(['loadi', f'$rl', pos_men])
                    self.assembly.append(['load', f'$r{RS}', f'$rl'])
                elif type1 == 'imt':
                    self.assembly.append(['loadi', f'$r{RS}', inter[1]])
                elif type1 == 'temp':
                    if inter[1] in self.temp_to_register:
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
                        RS = self.temp_to_register[inter[1]]
                        self.assembly.append(['move', f'$rt', f'$r{RS}'])
                self.assembly.append(['jmp', f'$ra'])
                self.free_reg(RS)
                self.temp_to_register[inter[1]] = -1

            if inter[0] == 'function_call':
                for i in range(0, inter[2]):
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
                            RS = self.temp_to_register[arg[1]]

                    self.assembly.append(['push', f'$r{RS}'])
                    self.assembly.append(['addi', f'$stp', '$stp', '1'])

                    self.free_reg(RS)
                    self.temp_to_register[inter[1]] = -1

                self.assembly.append(['jal', inter[1]])

            if inter[0] == 'arg':
                self.stack_args.append(inter)


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
        infos = self.semantic_table[f'{self.scope}.{var}']
        if infos:
            return infos.pos_mem
        return None

    def free_reg(self, reg):
        for i in self.status_reg:
            if i[0] == reg:
                i[1] = 1
                return 1
        return 0

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

    def search_type(self,string):
        x=''
        if re.match('t[0-9]', string):
            x = 'temp'
        elif re.match('[0-9]', string):
            x = 'imt'
        elif re.match('[a-zA-Z]', string):
            x = 'var'
        return x
