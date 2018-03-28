
import sys
import json
import argparse
import antlr4
from project.gen.cminusLexer import cminusLexer
from project.gen.cminusParser import cminusParser
from project.createAST import CreateAst
from project.printAst import printAst
from project.print_ast_json import print_ast_json
from project.semanticAnalysis import semanticAnalysisTableG


def main(argv):
    parser = argparse.ArgumentParser(description='cminus compiler')
    parser.add_argument('--file')
    parser.add_argument('--lexer', action='store_true')
    parser.add_argument('--ast', action='store_true')
    parser.add_argument('--symbol', action='store_true')

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

    semantic = semanticAnalysisTableG(ast)

    if args.symbol:
        print(semantic)

    if semantic.errors:
        print('Errors')
        for error in semantic.errors:
            print(error)


if __name__ == '__main__':
    main(sys.argv)
