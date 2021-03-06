
import sys
import json
import argparse
import antlr4
from project.gen.cminusLexer import cminusLexer
from project.gen.cminusParser import cminusParser
from project.createAST import CreateAst
from project.printAst import printAst
from project.semanticAnalysis import SemanticAnalysisTableG
from project.intermedCode import IntermedCode
from project.intermediate_to_assembly import IntermediateToAssembly
from project.asm_to_bin import AsmToBin


def main(argv):
    parser = argparse.ArgumentParser(description='cminus compiler')
    parser.add_argument('--file')
    parser.add_argument('--lexer', action='store_true')
    parser.add_argument('--ast', action='store_true')
    parser.add_argument('--symbol', action='store_true')
    parser.add_argument('--intermediate', action='store_true')
    parser.add_argument('--asbly', action='store_true')
    parser.add_argument('--bin', action='store_true')

    args = parser.parse_args()

    input = antlr4.FileStream(args.file)
    lexer = cminusLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = cminusParser(stream)
    tree = parser.programa()

    if args.lexer:
        for token in stream.tokens:
            print(token.line, ":", token.text)

    ast = CreateAst().visit(tree)

    if args.ast:
        printAst().visit(ast)

    semantic = SemanticAnalysisTableG(ast)

    if args.symbol:
        print(semantic)

    if semantic.errors:
        print('Errors:')
        for error in semantic.errors:
            print(error)

    else:
        inter = IntermedCode(ast)
        if args.intermediate:
            cont = 0
            print(' ')
            print(args.file,': ')
            with open(args.file, 'r') as file:
                print(' ')
                print(file.read())
            for i in inter.intermediario:
                print(cont, ' : (', end='')
                print(*i, sep=', ', end='')
                print(') ')
                cont += 1
        asm = IntermediateToAssembly(semantic,inter)
        if args.asbly:
            print('\n')
            i = 0
            for line in asm.assembly:
                if len(line) == 1:
                    print(*line)
                else:
                    print('    ', f'{i}:', *line)
                    i += 1
        bina = AsmToBin(asm)
        if args.bin:
            print('\n')
            file_bin = open('bin.txt','w')
            for line in bina.bin:
                print(line)
                file_bin.write(line+'\n')
            file_bin.close()


if __name__ == '__main__':
    main(sys.argv)
