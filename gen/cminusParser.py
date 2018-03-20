# Generated from /home/everton/Documentos/compiladores/compilador/cminus.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u010e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3<\n\3\f")
        buf.write("\3\16\3?\13\3\3\4\3\4\5\4C\n\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5P\n\5\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\5\b]\n\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\7\te\n\t\f\t\16\th\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\nr\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0083\n\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u008a\n\f\f\f\16\f\u008d\13\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\7\r\u0094\n\r\f\r\16\r\u0097\13\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u009e\n\16\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u00a4\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00b4\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u00c2\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u00c9")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00d1\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u00d8\n\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u00e0\n\26\f\26\16\26\u00e3\13\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00eb\n\27\f\27\16")
        buf.write("\27\u00ee\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u00f7\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u0101\n\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0109")
        buf.write("\n\32\f\32\16\32\u010c\13\32\3\32\2\t\4\20\26\30*,\62")
        buf.write("\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\2\6\4\2\5\5\7\7\4\2\t\n\f\17\3\2\20\21\3\2\22\23\2")
        buf.write("\u0110\2\64\3\2\2\2\4\66\3\2\2\2\6B\3\2\2\2\bO\3\2\2\2")
        buf.write("\nQ\3\2\2\2\fS\3\2\2\2\16\\\3\2\2\2\20^\3\2\2\2\22q\3")
        buf.write("\2\2\2\24\u0082\3\2\2\2\26\u0084\3\2\2\2\30\u008e\3\2")
        buf.write("\2\2\32\u009d\3\2\2\2\34\u00a3\3\2\2\2\36\u00b3\3\2\2")
        buf.write("\2 \u00b5\3\2\2\2\"\u00c1\3\2\2\2$\u00c8\3\2\2\2&\u00d0")
        buf.write("\3\2\2\2(\u00d7\3\2\2\2*\u00d9\3\2\2\2,\u00e4\3\2\2\2")
        buf.write(".\u00f6\3\2\2\2\60\u0100\3\2\2\2\62\u0102\3\2\2\2\64\65")
        buf.write("\5\4\3\2\65\3\3\2\2\2\66\67\b\3\1\2\678\5\6\4\28=\3\2")
        buf.write("\2\29:\f\4\2\2:<\5\6\4\2;9\3\2\2\2<?\3\2\2\2=;\3\2\2\2")
        buf.write("=>\3\2\2\2>\5\3\2\2\2?=\3\2\2\2@C\5\b\5\2AC\5\f\7\2B@")
        buf.write("\3\2\2\2BA\3\2\2\2C\7\3\2\2\2DE\5\n\6\2EF\7\34\2\2FG\7")
        buf.write("\26\2\2GP\3\2\2\2HI\5\n\6\2IJ\7\34\2\2JK\7\32\2\2KL\7")
        buf.write("\35\2\2LM\7\33\2\2MN\7\26\2\2NP\3\2\2\2OD\3\2\2\2OH\3")
        buf.write("\2\2\2P\t\3\2\2\2QR\t\2\2\2R\13\3\2\2\2ST\5\n\6\2TU\7")
        buf.write("\34\2\2UV\7\24\2\2VW\5\16\b\2WX\7\25\2\2XY\5\24\13\2Y")
        buf.write("\r\3\2\2\2Z]\5\20\t\2[]\7\7\2\2\\Z\3\2\2\2\\[\3\2\2\2")
        buf.write("]\17\3\2\2\2^_\b\t\1\2_`\5\22\n\2`f\3\2\2\2ab\f\4\2\2")
        buf.write("bc\7\27\2\2ce\5\22\n\2da\3\2\2\2eh\3\2\2\2fd\3\2\2\2f")
        buf.write("g\3\2\2\2g\21\3\2\2\2hf\3\2\2\2ij\5\n\6\2jk\7\34\2\2k")
        buf.write("r\3\2\2\2lm\5\n\6\2mn\7\34\2\2no\7\32\2\2op\7\33\2\2p")
        buf.write("r\3\2\2\2qi\3\2\2\2ql\3\2\2\2r\23\3\2\2\2st\7\30\2\2t")
        buf.write("u\5\26\f\2uv\5\30\r\2vw\7\31\2\2w\u0083\3\2\2\2xy\7\30")
        buf.write("\2\2yz\5\26\f\2z{\7\31\2\2{\u0083\3\2\2\2|}\7\30\2\2}")
        buf.write("~\5\30\r\2~\177\7\31\2\2\177\u0083\3\2\2\2\u0080\u0081")
        buf.write("\7\30\2\2\u0081\u0083\7\31\2\2\u0082s\3\2\2\2\u0082x\3")
        buf.write("\2\2\2\u0082|\3\2\2\2\u0082\u0080\3\2\2\2\u0083\25\3\2")
        buf.write("\2\2\u0084\u0085\b\f\1\2\u0085\u0086\5\b\5\2\u0086\u008b")
        buf.write("\3\2\2\2\u0087\u0088\f\4\2\2\u0088\u008a\5\b\5\2\u0089")
        buf.write("\u0087\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\27\3\2\2\2\u008d\u008b\3\2")
        buf.write("\2\2\u008e\u008f\b\r\1\2\u008f\u0090\5\32\16\2\u0090\u0095")
        buf.write("\3\2\2\2\u0091\u0092\f\4\2\2\u0092\u0094\5\32\16\2\u0093")
        buf.write("\u0091\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\31\3\2\2\2\u0097\u0095\3\2")
        buf.write("\2\2\u0098\u009e\5\34\17\2\u0099\u009e\5\24\13\2\u009a")
        buf.write("\u009e\5\36\20\2\u009b\u009e\5 \21\2\u009c\u009e\5\"\22")
        buf.write("\2\u009d\u0098\3\2\2\2\u009d\u0099\3\2\2\2\u009d\u009a")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\33\3\2\2\2\u009f\u00a0\5$\23\2\u00a0\u00a1\7\26\2\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a4\7\26\2\2\u00a3\u009f\3\2\2")
        buf.write("\2\u00a3\u00a2\3\2\2\2\u00a4\35\3\2\2\2\u00a5\u00a6\7")
        buf.write("\4\2\2\u00a6\u00a7\7\24\2\2\u00a7\u00a8\5$\23\2\u00a8")
        buf.write("\u00a9\7\25\2\2\u00a9\u00aa\5\32\16\2\u00aa\u00b4\3\2")
        buf.write("\2\2\u00ab\u00ac\7\4\2\2\u00ac\u00ad\7\24\2\2\u00ad\u00ae")
        buf.write("\5$\23\2\u00ae\u00af\7\25\2\2\u00af\u00b0\5\32\16\2\u00b0")
        buf.write("\u00b1\7\3\2\2\u00b1\u00b2\5\32\16\2\u00b2\u00b4\3\2\2")
        buf.write("\2\u00b3\u00a5\3\2\2\2\u00b3\u00ab\3\2\2\2\u00b4\37\3")
        buf.write("\2\2\2\u00b5\u00b6\7\b\2\2\u00b6\u00b7\7\24\2\2\u00b7")
        buf.write("\u00b8\5$\23\2\u00b8\u00b9\7\25\2\2\u00b9\u00ba\5\32\16")
        buf.write("\2\u00ba!\3\2\2\2\u00bb\u00bc\7\6\2\2\u00bc\u00c2\7\26")
        buf.write("\2\2\u00bd\u00be\7\6\2\2\u00be\u00bf\5$\23\2\u00bf\u00c0")
        buf.write("\7\26\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00bb\3\2\2\2\u00c1")
        buf.write("\u00bd\3\2\2\2\u00c2#\3\2\2\2\u00c3\u00c4\5&\24\2\u00c4")
        buf.write("\u00c5\7\13\2\2\u00c5\u00c6\5$\23\2\u00c6\u00c9\3\2\2")
        buf.write("\2\u00c7\u00c9\5(\25\2\u00c8\u00c3\3\2\2\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c9%\3\2\2\2\u00ca\u00d1\7\34\2\2\u00cb\u00cc")
        buf.write("\7\34\2\2\u00cc\u00cd\7\32\2\2\u00cd\u00ce\5$\23\2\u00ce")
        buf.write("\u00cf\7\33\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ca\3\2\2")
        buf.write("\2\u00d0\u00cb\3\2\2\2\u00d1\'\3\2\2\2\u00d2\u00d3\5*")
        buf.write("\26\2\u00d3\u00d4\t\3\2\2\u00d4\u00d5\5*\26\2\u00d5\u00d8")
        buf.write("\3\2\2\2\u00d6\u00d8\5*\26\2\u00d7\u00d2\3\2\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8)\3\2\2\2\u00d9\u00da\b\26\1\2\u00da")
        buf.write("\u00db\5,\27\2\u00db\u00e1\3\2\2\2\u00dc\u00dd\f\4\2\2")
        buf.write("\u00dd\u00de\t\4\2\2\u00de\u00e0\5,\27\2\u00df\u00dc\3")
        buf.write("\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2+\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5")
        buf.write("\b\27\1\2\u00e5\u00e6\5.\30\2\u00e6\u00ec\3\2\2\2\u00e7")
        buf.write("\u00e8\f\4\2\2\u00e8\u00e9\t\5\2\2\u00e9\u00eb\5.\30\2")
        buf.write("\u00ea\u00e7\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3")
        buf.write("\2\2\2\u00ec\u00ed\3\2\2\2\u00ed-\3\2\2\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ef\u00f0\7\24\2\2\u00f0\u00f1\5$\23\2\u00f1")
        buf.write("\u00f2\7\25\2\2\u00f2\u00f7\3\2\2\2\u00f3\u00f7\5&\24")
        buf.write("\2\u00f4\u00f7\5\60\31\2\u00f5\u00f7\7\35\2\2\u00f6\u00ef")
        buf.write("\3\2\2\2\u00f6\u00f3\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f7/\3\2\2\2\u00f8\u00f9\7\34\2\2\u00f9")
        buf.write("\u00fa\7\24\2\2\u00fa\u00fb\5\62\32\2\u00fb\u00fc\7\25")
        buf.write("\2\2\u00fc\u0101\3\2\2\2\u00fd\u00fe\7\34\2\2\u00fe\u00ff")
        buf.write("\7\24\2\2\u00ff\u0101\7\25\2\2\u0100\u00f8\3\2\2\2\u0100")
        buf.write("\u00fd\3\2\2\2\u0101\61\3\2\2\2\u0102\u0103\b\32\1\2\u0103")
        buf.write("\u0104\5$\23\2\u0104\u010a\3\2\2\2\u0105\u0106\f\4\2\2")
        buf.write("\u0106\u0107\7\27\2\2\u0107\u0109\5$\23\2\u0108\u0105")
        buf.write("\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\63\3\2\2\2\u010c\u010a\3\2\2\2\27")
        buf.write("=BO\\fq\u0082\u008b\u0095\u009d\u00a3\u00b3\u00c1\u00c8")
        buf.write("\u00d0\u00d7\u00e1\u00ec\u00f6\u0100\u010a")
        return buf.getvalue()


class cminusParser ( Parser ):

    grammarFileName = "cminus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'else'", "'if'", "'int'", "'return'", 
                     "'void'", "'while'", "'<='", "'>='", "'='", "'=='", 
                     "'!='", "'<'", "'>'", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "';'", "','", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "ELSE", "IF", "INT", "RETURN", "VOID", 
                      "WHILE", "LETHAN", "GETHAN", "ASSIGN", "EQ", "DF", 
                      "LT", "GT", "PLUS", "MINUS", "TIMES", "OVER", "LPAREN", 
                      "RPAREN", "SEMI", "COMMA", "LCBRACKET", "RCBRACKET", 
                      "LSBRACKET", "RSBRACKET", "ID", "NUM", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_programa = 0
    RULE_declaracao_lista = 1
    RULE_declaracao = 2
    RULE_var_declaracao = 3
    RULE_tipo_especificador = 4
    RULE_fun_declaracao = 5
    RULE_params = 6
    RULE_param_lista = 7
    RULE_param = 8
    RULE_composto_decl = 9
    RULE_local_declaracoes = 10
    RULE_statement_lista = 11
    RULE_statement = 12
    RULE_expressao_decl = 13
    RULE_selecao_decl = 14
    RULE_iteracao_decl = 15
    RULE_retorno_decl = 16
    RULE_expressao = 17
    RULE_var = 18
    RULE_simples_expressao = 19
    RULE_soma_expressao = 20
    RULE_termo = 21
    RULE_fator = 22
    RULE_ativacao = 23
    RULE_arg_lista = 24

    ruleNames =  [ "programa", "declaracao_lista", "declaracao", "var_declaracao", 
                   "tipo_especificador", "fun_declaracao", "params", "param_lista", 
                   "param", "composto_decl", "local_declaracoes", "statement_lista", 
                   "statement", "expressao_decl", "selecao_decl", "iteracao_decl", 
                   "retorno_decl", "expressao", "var", "simples_expressao", 
                   "soma_expressao", "termo", "fator", "ativacao", "arg_lista" ]

    EOF = Token.EOF
    ELSE=1
    IF=2
    INT=3
    RETURN=4
    VOID=5
    WHILE=6
    LETHAN=7
    GETHAN=8
    ASSIGN=9
    EQ=10
    DF=11
    LT=12
    GT=13
    PLUS=14
    MINUS=15
    TIMES=16
    OVER=17
    LPAREN=18
    RPAREN=19
    SEMI=20
    COMMA=21
    LCBRACKET=22
    RCBRACKET=23
    LSBRACKET=24
    RSBRACKET=25
    ID=26
    NUM=27
    BLOCK_COMMENT=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_lista(self):
            return self.getTypedRuleContext(cminusParser.Declaracao_listaContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = cminusParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.declaracao_lista(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaracao_listaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self):
            return self.getTypedRuleContext(cminusParser.DeclaracaoContext,0)


        def declaracao_lista(self):
            return self.getTypedRuleContext(cminusParser.Declaracao_listaContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_declaracao_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_lista" ):
                listener.enterDeclaracao_lista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_lista" ):
                listener.exitDeclaracao_lista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_lista" ):
                return visitor.visitDeclaracao_lista(self)
            else:
                return visitor.visitChildren(self)



    def declaracao_lista(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cminusParser.Declaracao_listaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_declaracao_lista, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.declaracao()
            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.Declaracao_listaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declaracao_lista)
                    self.state = 55
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 56
                    self.declaracao() 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclaracaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaracao(self):
            return self.getTypedRuleContext(cminusParser.Var_declaracaoContext,0)


        def fun_declaracao(self):
            return self.getTypedRuleContext(cminusParser.Fun_declaracaoContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = cminusParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.var_declaracao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.fun_declaracao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_declaracaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo_especificador(self):
            return self.getTypedRuleContext(cminusParser.Tipo_especificadorContext,0)


        def ID(self):
            return self.getToken(cminusParser.ID, 0)

        def SEMI(self):
            return self.getToken(cminusParser.SEMI, 0)

        def LSBRACKET(self):
            return self.getToken(cminusParser.LSBRACKET, 0)

        def NUM(self):
            return self.getToken(cminusParser.NUM, 0)

        def RSBRACKET(self):
            return self.getToken(cminusParser.RSBRACKET, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_var_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declaracao" ):
                listener.enterVar_declaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declaracao" ):
                listener.exitVar_declaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaracao" ):
                return visitor.visitVar_declaracao(self)
            else:
                return visitor.visitChildren(self)




    def var_declaracao(self):

        localctx = cminusParser.Var_declaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declaracao)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.tipo_especificador()
                self.state = 67
                self.match(cminusParser.ID)
                self.state = 68
                self.match(cminusParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.tipo_especificador()
                self.state = 71
                self.match(cminusParser.ID)
                self.state = 72
                self.match(cminusParser.LSBRACKET)
                self.state = 73
                self.match(cminusParser.NUM)
                self.state = 74
                self.match(cminusParser.RSBRACKET)
                self.state = 75
                self.match(cminusParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tipo_especificadorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(cminusParser.INT, 0)

        def VOID(self):
            return self.getToken(cminusParser.VOID, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_tipo_especificador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_especificador" ):
                listener.enterTipo_especificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_especificador" ):
                listener.exitTipo_especificador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo_especificador" ):
                return visitor.visitTipo_especificador(self)
            else:
                return visitor.visitChildren(self)




    def tipo_especificador(self):

        localctx = cminusParser.Tipo_especificadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipo_especificador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==cminusParser.INT or _la==cminusParser.VOID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fun_declaracaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo_especificador(self):
            return self.getTypedRuleContext(cminusParser.Tipo_especificadorContext,0)


        def ID(self):
            return self.getToken(cminusParser.ID, 0)

        def LPAREN(self):
            return self.getToken(cminusParser.LPAREN, 0)

        def params(self):
            return self.getTypedRuleContext(cminusParser.ParamsContext,0)


        def RPAREN(self):
            return self.getToken(cminusParser.RPAREN, 0)

        def composto_decl(self):
            return self.getTypedRuleContext(cminusParser.Composto_declContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_fun_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFun_declaracao" ):
                listener.enterFun_declaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFun_declaracao" ):
                listener.exitFun_declaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_declaracao" ):
                return visitor.visitFun_declaracao(self)
            else:
                return visitor.visitChildren(self)




    def fun_declaracao(self):

        localctx = cminusParser.Fun_declaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fun_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.tipo_especificador()
            self.state = 82
            self.match(cminusParser.ID)
            self.state = 83
            self.match(cminusParser.LPAREN)
            self.state = 84
            self.params()
            self.state = 85
            self.match(cminusParser.RPAREN)
            self.state = 86
            self.composto_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_lista(self):
            return self.getTypedRuleContext(cminusParser.Param_listaContext,0)


        def VOID(self):
            return self.getToken(cminusParser.VOID, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = cminusParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.param_lista(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(cminusParser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_listaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(cminusParser.ParamContext,0)


        def param_lista(self):
            return self.getTypedRuleContext(cminusParser.Param_listaContext,0)


        def COMMA(self):
            return self.getToken(cminusParser.COMMA, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_param_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_lista" ):
                listener.enterParam_lista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_lista" ):
                listener.exitParam_lista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lista" ):
                return visitor.visitParam_lista(self)
            else:
                return visitor.visitChildren(self)



    def param_lista(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cminusParser.Param_listaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_param_lista, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.param()
            self._ctx.stop = self._input.LT(-1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.Param_listaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_param_lista)
                    self.state = 95
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 96
                    self.match(cminusParser.COMMA)
                    self.state = 97
                    self.param() 
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo_especificador(self):
            return self.getTypedRuleContext(cminusParser.Tipo_especificadorContext,0)


        def ID(self):
            return self.getToken(cminusParser.ID, 0)

        def LSBRACKET(self):
            return self.getToken(cminusParser.LSBRACKET, 0)

        def RSBRACKET(self):
            return self.getToken(cminusParser.RSBRACKET, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = cminusParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.tipo_especificador()
                self.state = 104
                self.match(cminusParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.tipo_especificador()
                self.state = 107
                self.match(cminusParser.ID)
                self.state = 108
                self.match(cminusParser.LSBRACKET)
                self.state = 109
                self.match(cminusParser.RSBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Composto_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCBRACKET(self):
            return self.getToken(cminusParser.LCBRACKET, 0)

        def local_declaracoes(self):
            return self.getTypedRuleContext(cminusParser.Local_declaracoesContext,0)


        def statement_lista(self):
            return self.getTypedRuleContext(cminusParser.Statement_listaContext,0)


        def RCBRACKET(self):
            return self.getToken(cminusParser.RCBRACKET, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_composto_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposto_decl" ):
                listener.enterComposto_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposto_decl" ):
                listener.exitComposto_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposto_decl" ):
                return visitor.visitComposto_decl(self)
            else:
                return visitor.visitChildren(self)




    def composto_decl(self):

        localctx = cminusParser.Composto_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_composto_decl)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(cminusParser.LCBRACKET)
                self.state = 114
                self.local_declaracoes(0)
                self.state = 115
                self.statement_lista(0)
                self.state = 116
                self.match(cminusParser.RCBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(cminusParser.LCBRACKET)
                self.state = 119
                self.local_declaracoes(0)
                self.state = 120
                self.match(cminusParser.RCBRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(cminusParser.LCBRACKET)
                self.state = 123
                self.statement_lista(0)
                self.state = 124
                self.match(cminusParser.RCBRACKET)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.match(cminusParser.LCBRACKET)
                self.state = 127
                self.match(cminusParser.RCBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Local_declaracoesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaracao(self):
            return self.getTypedRuleContext(cminusParser.Var_declaracaoContext,0)


        def local_declaracoes(self):
            return self.getTypedRuleContext(cminusParser.Local_declaracoesContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_local_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_declaracoes" ):
                listener.enterLocal_declaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_declaracoes" ):
                listener.exitLocal_declaracoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_declaracoes" ):
                return visitor.visitLocal_declaracoes(self)
            else:
                return visitor.visitChildren(self)



    def local_declaracoes(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cminusParser.Local_declaracoesContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_local_declaracoes, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.var_declaracao()
            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.Local_declaracoesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_local_declaracoes)
                    self.state = 133
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 134
                    self.var_declaracao() 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Statement_listaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(cminusParser.StatementContext,0)


        def statement_lista(self):
            return self.getTypedRuleContext(cminusParser.Statement_listaContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_statement_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_lista" ):
                listener.enterStatement_lista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_lista" ):
                listener.exitStatement_lista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_lista" ):
                return visitor.visitStatement_lista(self)
            else:
                return visitor.visitChildren(self)



    def statement_lista(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cminusParser.Statement_listaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_statement_lista, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.Statement_listaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_lista)
                    self.state = 143
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 144
                    self.statement() 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_decl(self):
            return self.getTypedRuleContext(cminusParser.Expressao_declContext,0)


        def composto_decl(self):
            return self.getTypedRuleContext(cminusParser.Composto_declContext,0)


        def selecao_decl(self):
            return self.getTypedRuleContext(cminusParser.Selecao_declContext,0)


        def iteracao_decl(self):
            return self.getTypedRuleContext(cminusParser.Iteracao_declContext,0)


        def retorno_decl(self):
            return self.getTypedRuleContext(cminusParser.Retorno_declContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = cminusParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cminusParser.LPAREN, cminusParser.SEMI, cminusParser.ID, cminusParser.NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.expressao_decl()
                pass
            elif token in [cminusParser.LCBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.composto_decl()
                pass
            elif token in [cminusParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.selecao_decl()
                pass
            elif token in [cminusParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.iteracao_decl()
                pass
            elif token in [cminusParser.RETURN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 154
                self.retorno_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expressao_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def SEMI(self):
            return self.getToken(cminusParser.SEMI, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_expressao_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_decl" ):
                listener.enterExpressao_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_decl" ):
                listener.exitExpressao_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao_decl" ):
                return visitor.visitExpressao_decl(self)
            else:
                return visitor.visitChildren(self)




    def expressao_decl(self):

        localctx = cminusParser.Expressao_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expressao_decl)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cminusParser.LPAREN, cminusParser.ID, cminusParser.NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.expressao()
                self.state = 158
                self.match(cminusParser.SEMI)
                pass
            elif token in [cminusParser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(cminusParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Selecao_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.corpoIF = None # StatementContext
            self.corpoElse = None # StatementContext

        def IF(self):
            return self.getToken(cminusParser.IF, 0)

        def LPAREN(self):
            return self.getToken(cminusParser.LPAREN, 0)

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def RPAREN(self):
            return self.getToken(cminusParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.StatementContext)
            else:
                return self.getTypedRuleContext(cminusParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(cminusParser.ELSE, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_selecao_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelecao_decl" ):
                listener.enterSelecao_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelecao_decl" ):
                listener.exitSelecao_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelecao_decl" ):
                return visitor.visitSelecao_decl(self)
            else:
                return visitor.visitChildren(self)




    def selecao_decl(self):

        localctx = cminusParser.Selecao_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_selecao_decl)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(cminusParser.IF)
                self.state = 164
                self.match(cminusParser.LPAREN)
                self.state = 165
                self.expressao()
                self.state = 166
                self.match(cminusParser.RPAREN)
                self.state = 167
                localctx.corpoIF = self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(cminusParser.IF)
                self.state = 170
                self.match(cminusParser.LPAREN)
                self.state = 171
                self.expressao()
                self.state = 172
                self.match(cminusParser.RPAREN)
                self.state = 173
                localctx.corpoIF = self.statement()
                self.state = 174
                self.match(cminusParser.ELSE)
                self.state = 175
                localctx.corpoElse = self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Iteracao_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(cminusParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(cminusParser.LPAREN, 0)

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def RPAREN(self):
            return self.getToken(cminusParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(cminusParser.StatementContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_iteracao_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIteracao_decl" ):
                listener.enterIteracao_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIteracao_decl" ):
                listener.exitIteracao_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIteracao_decl" ):
                return visitor.visitIteracao_decl(self)
            else:
                return visitor.visitChildren(self)




    def iteracao_decl(self):

        localctx = cminusParser.Iteracao_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_iteracao_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(cminusParser.WHILE)
            self.state = 180
            self.match(cminusParser.LPAREN)
            self.state = 181
            self.expressao()
            self.state = 182
            self.match(cminusParser.RPAREN)
            self.state = 183
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Retorno_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(cminusParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(cminusParser.SEMI, 0)

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_retorno_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno_decl" ):
                listener.enterRetorno_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno_decl" ):
                listener.exitRetorno_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno_decl" ):
                return visitor.visitRetorno_decl(self)
            else:
                return visitor.visitChildren(self)




    def retorno_decl(self):

        localctx = cminusParser.Retorno_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_retorno_decl)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(cminusParser.RETURN)
                self.state = 186
                self.match(cminusParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(cminusParser.RETURN)
                self.state = 188
                self.expressao()
                self.state = 189
                self.match(cminusParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(cminusParser.VarContext,0)


        def ASSIGN(self):
            return self.getToken(cminusParser.ASSIGN, 0)

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def simples_expressao(self):
            return self.getTypedRuleContext(cminusParser.Simples_expressaoContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = cminusParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressao)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.var()
                self.state = 194
                self.match(cminusParser.ASSIGN)
                self.state = 195
                self.expressao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.simples_expressao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(cminusParser.ID, 0)

        def LSBRACKET(self):
            return self.getToken(cminusParser.LSBRACKET, 0)

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def RSBRACKET(self):
            return self.getToken(cminusParser.RSBRACKET, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = cminusParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(cminusParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(cminusParser.ID)
                self.state = 202
                self.match(cminusParser.LSBRACKET)
                self.state = 203
                self.expressao()
                self.state = 204
                self.match(cminusParser.RSBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simples_expressaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.esquerda = None # Soma_expressaoContext
            self.relacional = None # Token
            self.direita = None # Soma_expressaoContext
            self.operacao = None # Soma_expressaoContext

        def soma_expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.Soma_expressaoContext)
            else:
                return self.getTypedRuleContext(cminusParser.Soma_expressaoContext,i)


        def LETHAN(self):
            return self.getToken(cminusParser.LETHAN, 0)

        def LT(self):
            return self.getToken(cminusParser.LT, 0)

        def GT(self):
            return self.getToken(cminusParser.GT, 0)

        def GETHAN(self):
            return self.getToken(cminusParser.GETHAN, 0)

        def EQ(self):
            return self.getToken(cminusParser.EQ, 0)

        def DF(self):
            return self.getToken(cminusParser.DF, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_simples_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimples_expressao" ):
                listener.enterSimples_expressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimples_expressao" ):
                listener.exitSimples_expressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimples_expressao" ):
                return visitor.visitSimples_expressao(self)
            else:
                return visitor.visitChildren(self)




    def simples_expressao(self):

        localctx = cminusParser.Simples_expressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_simples_expressao)
        self._la = 0 # Token type
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                localctx.esquerda = self.soma_expressao(0)
                self.state = 209
                localctx.relacional = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cminusParser.LETHAN) | (1 << cminusParser.GETHAN) | (1 << cminusParser.EQ) | (1 << cminusParser.DF) | (1 << cminusParser.LT) | (1 << cminusParser.GT))) != 0)):
                    localctx.relacional = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 210
                localctx.direita = self.soma_expressao(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                localctx.operacao = self.soma_expressao(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Soma_expressaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cminusParser.RULE_soma_expressao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddsubContext(Soma_expressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cminusParser.Soma_expressaoContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def soma_expressao(self):
            return self.getTypedRuleContext(cminusParser.Soma_expressaoContext,0)

        def termo(self):
            return self.getTypedRuleContext(cminusParser.TermoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddsub" ):
                listener.enterAddsub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddsub" ):
                listener.exitAddsub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddsub" ):
                return visitor.visitAddsub(self)
            else:
                return visitor.visitChildren(self)


    class TermContext(Soma_expressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cminusParser.Soma_expressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo(self):
            return self.getTypedRuleContext(cminusParser.TermoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def soma_expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cminusParser.Soma_expressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_soma_expressao, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = cminusParser.TermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 216
            self.termo(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.AddsubContext(self, cminusParser.Soma_expressaoContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_soma_expressao)
                    self.state = 218
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 219
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==cminusParser.PLUS or _la==cminusParser.MINUS):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 220
                    self.termo(0) 
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TermoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def fator(self):
            return self.getTypedRuleContext(cminusParser.FatorContext,0)


        def termo(self):
            return self.getTypedRuleContext(cminusParser.TermoContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)



    def termo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cminusParser.TermoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_termo, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.fator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.TermoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo)
                    self.state = 229
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 230
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==cminusParser.TIMES or _la==cminusParser.OVER):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 231
                    self.fator() 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(cminusParser.LPAREN, 0)

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def RPAREN(self):
            return self.getToken(cminusParser.RPAREN, 0)

        def var(self):
            return self.getTypedRuleContext(cminusParser.VarContext,0)


        def ativacao(self):
            return self.getTypedRuleContext(cminusParser.AtivacaoContext,0)


        def NUM(self):
            return self.getToken(cminusParser.NUM, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = cminusParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_fator)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(cminusParser.LPAREN)
                self.state = 238
                self.expressao()
                self.state = 239
                self.match(cminusParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.ativacao()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.match(cminusParser.NUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtivacaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(cminusParser.ID, 0)

        def LPAREN(self):
            return self.getToken(cminusParser.LPAREN, 0)

        def arg_lista(self):
            return self.getTypedRuleContext(cminusParser.Arg_listaContext,0)


        def RPAREN(self):
            return self.getToken(cminusParser.RPAREN, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_ativacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtivacao" ):
                listener.enterAtivacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtivacao" ):
                listener.exitAtivacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtivacao" ):
                return visitor.visitAtivacao(self)
            else:
                return visitor.visitChildren(self)




    def ativacao(self):

        localctx = cminusParser.AtivacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ativacao)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(cminusParser.ID)
                self.state = 247
                self.match(cminusParser.LPAREN)
                self.state = 248
                self.arg_lista(0)
                self.state = 249
                self.match(cminusParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(cminusParser.ID)
                self.state = 252
                self.match(cminusParser.LPAREN)
                self.state = 253
                self.match(cminusParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arg_listaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def arg_lista(self):
            return self.getTypedRuleContext(cminusParser.Arg_listaContext,0)


        def COMMA(self):
            return self.getToken(cminusParser.COMMA, 0)

        def getRuleIndex(self):
            return cminusParser.RULE_arg_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_lista" ):
                listener.enterArg_lista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_lista" ):
                listener.exitArg_lista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_lista" ):
                return visitor.visitArg_lista(self)
            else:
                return visitor.visitChildren(self)



    def arg_lista(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cminusParser.Arg_listaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_arg_lista, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.expressao()
            self._ctx.stop = self._input.LT(-1)
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.Arg_listaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arg_lista)
                    self.state = 259
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 260
                    self.match(cminusParser.COMMA)
                    self.state = 261
                    self.expressao() 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.declaracao_lista_sempred
        self._predicates[7] = self.param_lista_sempred
        self._predicates[10] = self.local_declaracoes_sempred
        self._predicates[11] = self.statement_lista_sempred
        self._predicates[20] = self.soma_expressao_sempred
        self._predicates[21] = self.termo_sempred
        self._predicates[24] = self.arg_lista_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def declaracao_lista_sempred(self, localctx:Declaracao_listaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def param_lista_sempred(self, localctx:Param_listaContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def local_declaracoes_sempred(self, localctx:Local_declaracoesContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def statement_lista_sempred(self, localctx:Statement_listaContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def soma_expressao_sempred(self, localctx:Soma_expressaoContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def termo_sempred(self, localctx:TermoContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def arg_lista_sempred(self, localctx:Arg_listaContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




