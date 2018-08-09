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
            aux = line
            for i in range(0, len(line)):
                if line[i] == '$rt':
                    line[i] = '$r28'
                elif line[i] == '$stp':
                    line[i] = '$r29'
                elif line[i] == '$rl':
                    line[i] = '$r30'
                elif line[i] == '$ra':
                    line[i] = '$r31'
            if line[0] == 'add':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(1,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'addi':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(2,
                                                                     int(line[1][2:]),
                                                                     int(line[2][2:]),
                                                                     int(line[3])) + '; //' + str(aux))
            elif line[0] == 'sub':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(3,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'subi':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(4,
                                                                     int(line[1][2:]),
                                                                     int(line[2][2:]),
                                                                     int(line[3])) + '; //' + str(aux))
            elif line[0] == 'mult':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(5,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
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
            elif line[0] == 'load':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(12,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'loadi':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:021b}'.format(13,
                                                             int(line[1][2:]),
                                                             int(line[2])) + '; //' + str(aux))


            elif line[0] == 'store':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(14,
                                                                     int(line[1][2:]),
                                                                     int(line[2][2:]),
                                                                     0) + '; //' + str(aux))
            elif line[0] == 'move':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(15,
                                                                     int(line[1][2:]),
                                                                     int(line[2][2:]),
                                                                     0) + '; //' + str(aux))
            elif line[0] == 'jmpi':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:021b}'.format(16,
                                                             0,
                                                             int(self.hash_labels[line[1]])) + '; //' + str(aux))
            elif line[0] == 'jmp':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:021b}'.format(17,
                                                             int(line[1][2:]),
                                                             0) + '; //' + str(aux))
            elif line[0] == 'je':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(18,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'jne':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(19,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'ja':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(20,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'jna':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(21,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'in':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:021b}'.format(22,
                                                             int(line[1][2:]),
                                                             0) + '; //' + str(aux))
            elif line[0] == 'out':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:021b}'.format(23,
                                                             int(line[1][2:]),
                                                             0) + '; //' + str(aux))
            elif line[0] == 'nop':
                self.bin.append(
                    code + '{0:06b}_{1:026b}'.format(24, 0) + '; //' + str(aux))
            elif line[0] == 'halt':
                self.bin.append(
                    code + '{0:06b}_{1:026b}'.format(25, 0) + '; //' + str(aux))
            elif line[0] == 'div':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(26,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'eq':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(27,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'neq':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(28,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'abv':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(29,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'nab':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(30,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'lt':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(31,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'nlt':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:05b}_{4:011b}'.format(32,
                                                                             int(line[1][2:]),
                                                                             int(line[2][2:]),
                                                                             int(line[3][2:]),
                                                                             0) + '; //' + str(aux))
            elif line[0] == 'jal':
                self.bin.append(
                    code + '{0:06b}_{1:026b}'.format(33,
                                                     int(self.hash_labels[line[1]])
                                                     ) + '; //' + str(aux))
            elif line[0] == 'jei':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(34,
                                                                     int(line[1][2:]),
                                                                     int(line[2][2:]),
                                                                     int(self.hash_labels[line[3]])
                                                                     ) + '; //' + str(aux))
            elif line[0] == 'push':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(35,
                                                                     int(line[1][2:]),
                                                                     int(line[2][2:]),
                                                                     0) + '; //' + str(aux))
            elif line[0] == 'pop':
                self.bin.append(
                    code + '{0:06b}_{1:05b}_{2:05b}_{3:016b}'.format(36,
                                                                     int(line[1][2:]),
                                                                     int(line[2][2:]),
                                                                     0) + '; //' + str(aux))
            if len(line) > 1:
                line_n += 1

        self.bin.append('mem_ram[' + str(line_n) + "] = 32'b" + '{0:06b}_{1:026b}'.format(25, 0) + '; // halt')
