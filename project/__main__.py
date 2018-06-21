
import sys
import json
import argparse
import antlr4
from project.gen.cminusLexer import cminusLexer
from project.gen.cminusParser import cminusParser
from project.createAST import CreateAst
from project.printAst import printAst
from project.semanticAnalysis import SemanticAnalysisTableG
from project.intermedCode import intermedCode


def main(argv):
    parser = argparse.ArgumentParser(description='cminus compiler')
    parser.add_argument('--file')
    parser.add_argument('--lexer', action='store_true')
    parser.add_argument('--ast', action='store_true')
    parser.add_argument('--symbol', action='store_true')
    parser.add_argument('--intermediate', action='store_true')

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
        if args.intermediate:
            cont = 0
            inter = intermedCode(ast)
            print(' ')
            print(args.file,': ')
            with open(args.file, 'r') as file:
                print(' ')
                print(file.read())
            for i in inter.intermediario:
                print(cont,' : (', end = '')
                print(*i, sep = ', ', end = '')
                print(') ')
                cont += 1

if __name__ == '__main__':
    main(sys.argv)
