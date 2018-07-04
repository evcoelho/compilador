from  project import intermediate_to_assembly

class AsmToBin:
    def __init__(self, assembly: intermediate_to_assembly.IntermediateToAssembly):
        self.bin = []
        self.assembly = assembly.assembly
        self.hash_labels = {}
        self.assemblyToBin()

    def assemblyToBin(self):
        line_n = 0
        code = ''
        i = 0
        for label in self.assembly:
            if len(label) == 1:
                self.hash_labels[label[0][:-1]] = i
                # print(self.hash_labels[label[0][:-1]])
            else:
                i += 1

        for line in self.assembly:
            code = 'mem_ram[' + str(line_n) + "] = 32'b"

            for i in range(0, len(line)):
                if line[i] == '$rt':
                    line[i] = 29
                elif line[i] == '$stp':
                    line[i] = 30
                elif line[i] == '$rl':
                    line[i] = 31
                elif line[i] == '$ra':
                    line[i] = 32

            if line[0] == 'add':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(1,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + ';')
            elif line[0] == 'addi':
                self.bin.append(code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(2,
                                                                                 int(line[1]),
                                                                                 int(line[2]),
                                                                                 int(line[3])) + ';')
            elif line[0] == 'sub':
                self.bin.append(code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(3,
                                                                                         int(line[1][2:]),
                                                                                         int(line[2][2:]),
                                                                                         int(line[3][2:]),
                                                                                         0) + ';')
            # elif line[0] == 'subi':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(4, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'mult':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(5, int(line[1][1:]), int(line[3][1:]), int(line[2][:])) + ';\n'
            # elif line[0] == 'and':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(6, int(line[1][1:]), 0, int(line[2][1:]), 0) + ';\n'
            # elif line[0] == 'or':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(7, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'xor':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(8, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'not':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(9, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'shr':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(10, int(line[1][1:]), 0, int(line[2][1:]), 0) + ';\n'
            # elif line[0] == 'shl':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(11, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'load':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:05b}{5:06b}'.format(12, int(line[1][1:]), 0, int(line[3][1:]), int(line[2][:]), 0) + ';\n'
            # elif line[0] == 'loadi':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:05b}{5:06b}'.format(13, int(line[1][1:]), 0, int(line[3][1:]), int(line[2][:]), 0) + ';\n'
            # elif line[0] == 'store':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(14, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'move':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(15, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'jmpi':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(16, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'jmp':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(17, int(line[1][1:]), int(line[2][1:]), int(line[3][:])) + ';\n'
            # elif line[0] == 'je':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(18, int(line[1][1:]), int(line[2][1:]), int(line[3][:])) + ';\n'
            # elif line[0] == 'jne':
            #     code += '{0:06b}{1:026b}'.format(19, int(line[1][:])) + ';\n'
            # elif line[0] == 'ja':
            #     code += '{0:06b}{1:05b}{2:021b}'.format(20, int(line[1][1:]), 0) + ';\n'
            # elif line[0] == 'jna':
            #     code += '{0:06b}{1:026b}'.format(21, 0) + ';\n'
            # elif line[0] == 'in':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(22, int(0), int(line[1][1:]), int(0)) + ';\n'
            # elif line[0] == 'out':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(23, 0, int(line[1][1:]),0) + ';\n'
            # elif line[0] == 'nop':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(24, int(line[1][1:]), int(line[3][1:]), int(line[2][:])) + ';\n'
            # elif line[0] == 'halt':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(25, int(line[1][1:]), int(line[3][1:]), int(line[2][:])) + ';\n'
            # elif line[0] == 'div':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(26, 0, int(line[1][1:]), 0) + ';\n'
            # elif line[0] == 'eq':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(27, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'neq':
            #     code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(28, int(line[1][1:]), int(line[2][1:]), int(line[3][1:]), 0) + ';\n'
            # elif line[0] == 'abv':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(29, int(line[1][1:]), int(line[3][1:]), int(line[2][:])) + ';\n'
            # elif line[0] == 'nab':
            #     code += '{0:06b}{1:026b}'.format(30,0) + ';\n'
            # elif line[0] == 'lt':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(31, int(line[1][1:]), int(line[3][1:]),                                                           int(line[2][:])) + ';\n'
            # elif line[0] == 'nlt':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(32, int(line[1][1:]), int(line[3][1:]),                                                        int(line[2][:])) + ';\n'
            # elif line[0] == 'jal':
            #     code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(33, int(line[1][1:]), int(line[3][1:]),
            #                                                    int(line[2][:])) + ';\n'

            if len(line) > 1:
                line_n += 1
