from  project import intermediate_to_assembly

class AsmToBin:
    def __init__(self, assembly: intermediate_to_assembly.IntermediateToAssembly):
        self.bin = []
        self.assembly = assembly.assembly

    def assemblyToBin(self, path):
        line_n = -1
        code = ''
        for line in self.assembly:
            line = line[:-1]
            line_n += 1
            code = code + 'mem[' + str(line_n) + "] = 32'b"
            tokens = line.split(' ')
            if(tokens[0] == 'NOP'):
                code += '{0:32b}'.format(0)
            elif(tokens[0] == 'ADD'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(1, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'ADDI'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(2, int(tokens[1][1:]), int(tokens[3][1:]), int(tokens[2][:])) + ';\n'
            elif(tokens[0] == 'ADD1'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(3, int(tokens[1][1:]), 0, int(tokens[2][1:]), 0) + ';\n'
            elif(tokens[0] == 'SUB'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(4, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'SUBI'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(5, int(tokens[1][1:]), int(tokens[3][1:]), int(tokens[2][:])) + ';\n'
            elif(tokens[0] == 'SUB1'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(6, int(tokens[1][1:]), 0, int(tokens[2][1:]), 0) + ';\n'
            elif(tokens[0] == 'AND'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(7, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'OR'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(8, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'XOR'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(9, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'NOT'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(10, int(tokens[1][1:]), 0, int(tokens[2][1:]), 0) + ';\n'
            elif(tokens[0] == 'MOD'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(11, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'SHIFTL'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:05b}{5:06b}'.format(12, int(tokens[1][1:]), 0, int(tokens[3][1:]), int(tokens[2][:]), 0) + ';\n'
            elif(tokens[0] == 'SHIFTR'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:05b}{5:06b}'.format(13, int(tokens[1][1:]), 0, int(tokens[3][1:]), int(tokens[2][:]), 0) + ';\n'
            elif(tokens[0] == 'SLT'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(14, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'SHT'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(15, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'SEQ'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(16, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'BEQ'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(17, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][:])) + ';\n'
            elif(tokens[0] == 'BNE'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(18, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][:])) + ';\n'
            elif(tokens[0] == 'J'):
                code += '{0:06b}{1:026b}'.format(19, int(tokens[1][:])) + ';\n'
            elif(tokens[0] == 'JR'):
                code += '{0:06b}{1:05b}{2:021b}'.format(20, int(tokens[1][1:]), 0) + ';\n'
            elif(tokens[0] == 'HALT'):
                code += '{0:06b}{1:026b}'.format(21, 0) + ';\n'
            elif(tokens[0] == 'IN'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(22, int(0), int(tokens[1][1:]), int(0)) + ';\n'
            elif(tokens[0] == 'OUT'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(23, 0, int(tokens[1][1:]),0) + ';\n'
            elif(tokens[0] == 'LOAD'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(24, int(tokens[1][1:]), int(tokens[3][1:]), int(tokens[2][:])) + ';\n'
            elif(tokens[0] == 'LOADI'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(25, int(tokens[1][1:]), int(tokens[3][1:]), int(tokens[2][:])) + ';\n'
            elif(tokens[0] == 'LOADA'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(26, 0, int(tokens[1][1:]), 0) + ';\n'
            elif(tokens[0] == 'MULT'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(27, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'DIV'):
                code += '{0:06b}{1:05b}{2:05b}{3:05b}{4:011b}'.format(28, int(tokens[1][1:]), int(tokens[2][1:]), int(tokens[3][1:]), 0) + ';\n'
            elif(tokens[0] == 'STORE'):
                code += '{0:06b}{1:05b}{2:05b}{3:016b}'.format(29, int(tokens[1][1:]), int(tokens[3][1:]), int(tokens[2][:])) + ';\n'
            elif(tokens[0] == 'RESET'):
                code += '{0:06b}{1:026b}'.format(30,0) + ';\n'

        with open(path[:-1]+'bin', 'w') as f:
            f.write(code)
        return(code)