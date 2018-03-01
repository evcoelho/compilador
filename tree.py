import sys
import re
from antlr4 import *
from antlr4.InputStream import InputStream
from gen.cminusLexer import cminusLexer
from gen.cminusParser import cminusParser
from gen.cminusListener import cminusListener
from gen.cminusVisitor import cminusVisitor
from createAST import createAST



def main(argv):
    input = FileStream(argv[1])
    lexer = cminusLexer(input)
    stream = CommonTokenStream(lexer)
    parser = cminusParser(stream)
    tree = parser.programa()
    """
    printer = printTree()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    """
    visitor = visitTree()
    arvore = visitor.visit(tree)



if __name__ == '__main__':
    main(sys.argv)
