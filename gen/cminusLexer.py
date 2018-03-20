# Generated from /home/everton/Documentos/compiladores/compilador/cminus.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37")
        buf.write("\u00a4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\6\33\u0087\n\33\r\33\16\33\u0088\3\34\6\34\u008c\n\34")
        buf.write("\r\34\16\34\u008d\3\35\3\35\3\35\3\35\7\35\u0094\n\35")
        buf.write("\f\35\16\35\u0097\13\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\6\36\u009f\n\36\r\36\16\36\u00a0\3\36\3\36\3\u0095\2")
        buf.write("\37\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37\3\2\5\4\2C\\c|\3")
        buf.write("\2\62;\5\2\13\f\16\17\"\"\2\u00a7\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\3=\3\2\2\2\5B\3\2\2\2\7E\3\2\2\2\tI\3\2\2")
        buf.write("\2\13P\3\2\2\2\rU\3\2\2\2\17[\3\2\2\2\21^\3\2\2\2\23a")
        buf.write("\3\2\2\2\25c\3\2\2\2\27f\3\2\2\2\31i\3\2\2\2\33k\3\2\2")
        buf.write("\2\35m\3\2\2\2\37o\3\2\2\2!q\3\2\2\2#s\3\2\2\2%u\3\2\2")
        buf.write("\2\'w\3\2\2\2)y\3\2\2\2+{\3\2\2\2-}\3\2\2\2/\177\3\2\2")
        buf.write("\2\61\u0081\3\2\2\2\63\u0083\3\2\2\2\65\u0086\3\2\2\2")
        buf.write("\67\u008b\3\2\2\29\u008f\3\2\2\2;\u009e\3\2\2\2=>\7g\2")
        buf.write("\2>?\7n\2\2?@\7u\2\2@A\7g\2\2A\4\3\2\2\2BC\7k\2\2CD\7")
        buf.write("h\2\2D\6\3\2\2\2EF\7k\2\2FG\7p\2\2GH\7v\2\2H\b\3\2\2\2")
        buf.write("IJ\7t\2\2JK\7g\2\2KL\7v\2\2LM\7w\2\2MN\7t\2\2NO\7p\2\2")
        buf.write("O\n\3\2\2\2PQ\7x\2\2QR\7q\2\2RS\7k\2\2ST\7f\2\2T\f\3\2")
        buf.write("\2\2UV\7y\2\2VW\7j\2\2WX\7k\2\2XY\7n\2\2YZ\7g\2\2Z\16")
        buf.write("\3\2\2\2[\\\7>\2\2\\]\7?\2\2]\20\3\2\2\2^_\7@\2\2_`\7")
        buf.write("?\2\2`\22\3\2\2\2ab\7?\2\2b\24\3\2\2\2cd\7?\2\2de\7?\2")
        buf.write("\2e\26\3\2\2\2fg\7#\2\2gh\7?\2\2h\30\3\2\2\2ij\7>\2\2")
        buf.write("j\32\3\2\2\2kl\7@\2\2l\34\3\2\2\2mn\7-\2\2n\36\3\2\2\2")
        buf.write("op\7/\2\2p \3\2\2\2qr\7,\2\2r\"\3\2\2\2st\7\61\2\2t$\3")
        buf.write("\2\2\2uv\7*\2\2v&\3\2\2\2wx\7+\2\2x(\3\2\2\2yz\7=\2\2")
        buf.write("z*\3\2\2\2{|\7.\2\2|,\3\2\2\2}~\7}\2\2~.\3\2\2\2\177\u0080")
        buf.write("\7\177\2\2\u0080\60\3\2\2\2\u0081\u0082\7]\2\2\u0082\62")
        buf.write("\3\2\2\2\u0083\u0084\7_\2\2\u0084\64\3\2\2\2\u0085\u0087")
        buf.write("\t\2\2\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\66\3\2\2\2\u008a")
        buf.write("\u008c\t\3\2\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e8\3\2\2")
        buf.write("\2\u008f\u0090\7\61\2\2\u0090\u0091\7,\2\2\u0091\u0095")
        buf.write("\3\2\2\2\u0092\u0094\13\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\u0097\3\2\2\2\u0095\u0096\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\7")
        buf.write(",\2\2\u0099\u009a\7\61\2\2\u009a\u009b\3\2\2\2\u009b\u009c")
        buf.write("\b\35\2\2\u009c:\3\2\2\2\u009d\u009f\t\4\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\b\36\2")
        buf.write("\2\u00a3<\3\2\2\2\7\2\u0088\u008d\u0095\u00a0\3\b\2\2")
        return buf.getvalue()


class cminusLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ELSE = 1
    IF = 2
    INT = 3
    RETURN = 4
    VOID = 5
    WHILE = 6
    LETHAN = 7
    GETHAN = 8
    ASSIGN = 9
    EQ = 10
    DF = 11
    LT = 12
    GT = 13
    PLUS = 14
    MINUS = 15
    TIMES = 16
    OVER = 17
    LPAREN = 18
    RPAREN = 19
    SEMI = 20
    COMMA = 21
    LCBRACKET = 22
    RCBRACKET = 23
    LSBRACKET = 24
    RSBRACKET = 25
    ID = 26
    NUM = 27
    BLOCK_COMMENT = 28
    WS = 29

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'else'", "'if'", "'int'", "'return'", "'void'", "'while'", 
            "'<='", "'>='", "'='", "'=='", "'!='", "'<'", "'>'", "'+'", 
            "'-'", "'*'", "'/'", "'('", "')'", "';'", "','", "'{'", "'}'", 
            "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "ELSE", "IF", "INT", "RETURN", "VOID", "WHILE", "LETHAN", "GETHAN", 
            "ASSIGN", "EQ", "DF", "LT", "GT", "PLUS", "MINUS", "TIMES", 
            "OVER", "LPAREN", "RPAREN", "SEMI", "COMMA", "LCBRACKET", "RCBRACKET", 
            "LSBRACKET", "RSBRACKET", "ID", "NUM", "BLOCK_COMMENT", "WS" ]

    ruleNames = [ "ELSE", "IF", "INT", "RETURN", "VOID", "WHILE", "LETHAN", 
                  "GETHAN", "ASSIGN", "EQ", "DF", "LT", "GT", "PLUS", "MINUS", 
                  "TIMES", "OVER", "LPAREN", "RPAREN", "SEMI", "COMMA", 
                  "LCBRACKET", "RCBRACKET", "LSBRACKET", "RSBRACKET", "ID", 
                  "NUM", "BLOCK_COMMENT", "WS" ]

    grammarFileName = "cminus.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


