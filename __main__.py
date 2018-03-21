import sys
from antlr4 import *
from project.gen.cminusLexer import cminusLexer
from project.gen.cminusParser import cminusParser
from project.createAST import CriarAst
from project.printAst import printAst


def main(argv):
    input = FileStream(argv[1])
    lexer = cminusLexer(input)
    stream = CommonTokenStream(lexer)
    parser = cminusParser(stream)
    tree = parser.programa()

    for token in stream.tokens:
        print(token.line, ":", token.text)

    ast = CriarAst().visit(tree)

    print(ast)

    printAst.visit(ast)


if __name__ == '__main__':
    main(sys.argv)
