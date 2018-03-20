import sys
import re
from antlr4 import *
from antlr4.InputStream import InputStream
from gen.cminusLexer import cminusLexer
from gen.cminusParser import cminusParser
from gen.cminusVisitor import cminusVisitor
from createAST import CriarAst



def main(argv):
    input = FileStream(argv[1])
    lexer = cminusLexer(input)
    stream = CommonTokenStream(lexer)
    parser = cminusParser(stream)
    tree = parser.programa()

    for token in stream.tokens:
        print(token.line, ":", token.text)


if __name__ == '__main__':
    main(sys.argv)
