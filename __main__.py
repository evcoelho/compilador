import json
import sys
from antlr4 import *
from project.gen.cminusLexer import cminusLexer
from project.gen.cminusParser import cminusParser
from project.createAST import CriarAst
from project.printAst import printAst
from project.print_ast_json import print_ast_json


def main(argv):
    input = FileStream(argv[1])
    lexer = cminusLexer(input)
    stream = CommonTokenStream(lexer)
    parser = cminusParser(stream)
    tree = parser.programa()

    """for token in stream.tokens:
        print(token.line, ":", token.text)
    """
    ast = CriarAst().visit(tree)

    printAst().visit(ast)
    '''json_tree = print_ast_json().visit(ast)
    json_tree = json.dumps(json_tree, indent=2)
    print(json_tree)
    '''

if __name__ == '__main__':
    main(sys.argv)
