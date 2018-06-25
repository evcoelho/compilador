# Generated from /home/everton/Documentos/compiladores/compilador/cminus.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u00fa\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\6\2\62\n\2\r\2\16\2\63\3\3\3\3\5\38\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4E\n\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7R\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\7\bZ\n\b\f\b\16\b]\13\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\tg\n\t\3\n\3\n\7\nk\n\n\f\n\16\nn\13\n")
        buf.write("\3\n\7\nq\n\n\f\n\16\nt\13\n\3\n\3\n\3\13\6\13y\n\13\r")
        buf.write("\13\16\13z\3\f\6\f~\n\f\r\f\16\f\177\3\r\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u0087\n\r\3\16\5\16\u008a\n\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\7\17\u0094\n\17\f\17\16\17\u0097")
        buf.write("\13\17\3\17\3\17\3\17\3\17\7\17\u009d\n\17\f\17\16\17")
        buf.write("\u00a0\13\17\3\17\5\17\u00a3\n\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00b1\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\5\22\u00b8\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00c0\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\5\24\u00c7\n\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u00cf\n\25\f\25\16\25\u00d2\13\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u00da\n\26\f\26\16\26\u00dd\13\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00e6\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\7\30\u00ed\n\30\f\30\16\30\u00f0")
        buf.write("\13\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00f8\n\30\3")
        buf.write("\30\2\5\16(*\31\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\2\6\4\2\5\5\7\7\4\2\t\n\f\17\3\2\20\21\3\2\22")
        buf.write("\23\2\u00ff\2\61\3\2\2\2\4\67\3\2\2\2\6D\3\2\2\2\bF\3")
        buf.write("\2\2\2\nH\3\2\2\2\fQ\3\2\2\2\16S\3\2\2\2\20f\3\2\2\2\22")
        buf.write("h\3\2\2\2\24x\3\2\2\2\26}\3\2\2\2\30\u0086\3\2\2\2\32")
        buf.write("\u0089\3\2\2\2\34\u008d\3\2\2\2\36\u00a4\3\2\2\2 \u00b0")
        buf.write("\3\2\2\2\"\u00b7\3\2\2\2$\u00bf\3\2\2\2&\u00c6\3\2\2\2")
        buf.write("(\u00c8\3\2\2\2*\u00d3\3\2\2\2,\u00e5\3\2\2\2.\u00f7\3")
        buf.write("\2\2\2\60\62\5\4\3\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\3\3\2\2\2\658\5\6\4\2\668\5")
        buf.write("\n\6\2\67\65\3\2\2\2\67\66\3\2\2\28\5\3\2\2\29:\5\b\5")
        buf.write("\2:;\7\34\2\2;<\7\26\2\2<E\3\2\2\2=>\5\b\5\2>?\7\34\2")
        buf.write("\2?@\7\32\2\2@A\7\35\2\2AB\7\33\2\2BC\7\26\2\2CE\3\2\2")
        buf.write("\2D9\3\2\2\2D=\3\2\2\2E\7\3\2\2\2FG\t\2\2\2G\t\3\2\2\2")
        buf.write("HI\5\b\5\2IJ\7\34\2\2JK\7\24\2\2KL\5\f\7\2LM\7\25\2\2")
        buf.write("MN\5\22\n\2N\13\3\2\2\2OR\5\16\b\2PR\7\7\2\2QO\3\2\2\2")
        buf.write("QP\3\2\2\2R\r\3\2\2\2ST\b\b\1\2TU\5\20\t\2U[\3\2\2\2V")
        buf.write("W\f\4\2\2WX\7\27\2\2XZ\5\20\t\2YV\3\2\2\2Z]\3\2\2\2[Y")
        buf.write("\3\2\2\2[\\\3\2\2\2\\\17\3\2\2\2][\3\2\2\2^_\5\b\5\2_")
        buf.write("`\7\34\2\2`g\3\2\2\2ab\5\b\5\2bc\7\34\2\2cd\7\32\2\2d")
        buf.write("e\7\33\2\2eg\3\2\2\2f^\3\2\2\2fa\3\2\2\2g\21\3\2\2\2h")
        buf.write("l\7\30\2\2ik\5\24\13\2ji\3\2\2\2kn\3\2\2\2lj\3\2\2\2l")
        buf.write("m\3\2\2\2mr\3\2\2\2nl\3\2\2\2oq\5\26\f\2po\3\2\2\2qt\3")
        buf.write("\2\2\2rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\7\31")
        buf.write("\2\2v\23\3\2\2\2wy\5\6\4\2xw\3\2\2\2yz\3\2\2\2zx\3\2\2")
        buf.write("\2z{\3\2\2\2{\25\3\2\2\2|~\5\30\r\2}|\3\2\2\2~\177\3\2")
        buf.write("\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\27\3\2\2\2\u0081")
        buf.write("\u0087\5\32\16\2\u0082\u0087\5\22\n\2\u0083\u0087\5\34")
        buf.write("\17\2\u0084\u0087\5\36\20\2\u0085\u0087\5 \21\2\u0086")
        buf.write("\u0081\3\2\2\2\u0086\u0082\3\2\2\2\u0086\u0083\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\31\3\2")
        buf.write("\2\2\u0088\u008a\5\"\22\2\u0089\u0088\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\7\26\2\2\u008c")
        buf.write("\33\3\2\2\2\u008d\u008e\7\4\2\2\u008e\u008f\7\24\2\2\u008f")
        buf.write("\u0090\5\"\22\2\u0090\u0091\7\25\2\2\u0091\u0095\7\30")
        buf.write("\2\2\u0092\u0094\5\30\r\2\u0093\u0092\3\2\2\2\u0094\u0097")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u00a2\7\31\2")
        buf.write("\2\u0099\u009a\7\3\2\2\u009a\u009e\7\30\2\2\u009b\u009d")
        buf.write("\5\30\r\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a1\u00a3\7\31\2\2\u00a2\u0099")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\35\3\2\2\2\u00a4\u00a5")
        buf.write("\7\b\2\2\u00a5\u00a6\7\24\2\2\u00a6\u00a7\5\"\22\2\u00a7")
        buf.write("\u00a8\7\25\2\2\u00a8\u00a9\5\30\r\2\u00a9\37\3\2\2\2")
        buf.write("\u00aa\u00ab\7\6\2\2\u00ab\u00b1\7\26\2\2\u00ac\u00ad")
        buf.write("\7\6\2\2\u00ad\u00ae\5\"\22\2\u00ae\u00af\7\26\2\2\u00af")
        buf.write("\u00b1\3\2\2\2\u00b0\u00aa\3\2\2\2\u00b0\u00ac\3\2\2\2")
        buf.write("\u00b1!\3\2\2\2\u00b2\u00b3\5$\23\2\u00b3\u00b4\7\13\2")
        buf.write("\2\u00b4\u00b5\5\"\22\2\u00b5\u00b8\3\2\2\2\u00b6\u00b8")
        buf.write("\5&\24\2\u00b7\u00b2\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8")
        buf.write("#\3\2\2\2\u00b9\u00c0\7\34\2\2\u00ba\u00bb\7\34\2\2\u00bb")
        buf.write("\u00bc\7\32\2\2\u00bc\u00bd\5\"\22\2\u00bd\u00be\7\33")
        buf.write("\2\2\u00be\u00c0\3\2\2\2\u00bf\u00b9\3\2\2\2\u00bf\u00ba")
        buf.write("\3\2\2\2\u00c0%\3\2\2\2\u00c1\u00c2\5(\25\2\u00c2\u00c3")
        buf.write("\t\3\2\2\u00c3\u00c4\5(\25\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c7\5(\25\2\u00c6\u00c1\3\2\2\2\u00c6\u00c5\3\2\2\2")
        buf.write("\u00c7\'\3\2\2\2\u00c8\u00c9\b\25\1\2\u00c9\u00ca\5*\26")
        buf.write("\2\u00ca\u00d0\3\2\2\2\u00cb\u00cc\f\4\2\2\u00cc\u00cd")
        buf.write("\t\4\2\2\u00cd\u00cf\5*\26\2\u00ce\u00cb\3\2\2\2\u00cf")
        buf.write("\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1)\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\b\26\1")
        buf.write("\2\u00d4\u00d5\5,\27\2\u00d5\u00db\3\2\2\2\u00d6\u00d7")
        buf.write("\f\4\2\2\u00d7\u00d8\t\5\2\2\u00d8\u00da\5,\27\2\u00d9")
        buf.write("\u00d6\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc+\3\2\2\2\u00dd\u00db\3\2\2")
        buf.write("\2\u00de\u00df\7\24\2\2\u00df\u00e0\5\"\22\2\u00e0\u00e1")
        buf.write("\7\25\2\2\u00e1\u00e6\3\2\2\2\u00e2\u00e6\5$\23\2\u00e3")
        buf.write("\u00e6\5.\30\2\u00e4\u00e6\7\35\2\2\u00e5\u00de\3\2\2")
        buf.write("\2\u00e5\u00e2\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e6-\3\2\2\2\u00e7\u00e8\7\34\2\2\u00e8\u00ee")
        buf.write("\7\24\2\2\u00e9\u00ea\5\"\22\2\u00ea\u00eb\7\27\2\2\u00eb")
        buf.write("\u00ed\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ed\u00f0\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1\3")
        buf.write("\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\5\"\22\2\u00f2")
        buf.write("\u00f3\7\25\2\2\u00f3\u00f8\3\2\2\2\u00f4\u00f5\7\34\2")
        buf.write("\2\u00f5\u00f6\7\24\2\2\u00f6\u00f8\7\25\2\2\u00f7\u00e7")
        buf.write("\3\2\2\2\u00f7\u00f4\3\2\2\2\u00f8/\3\2\2\2\32\63\67D")
        buf.write("Q[flrz\177\u0086\u0089\u0095\u009e\u00a2\u00b0\u00b7\u00bf")
        buf.write("\u00c6\u00d0\u00db\u00e5\u00ee\u00f7")
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
    RULE_declaracao = 1
    RULE_var_declaracao = 2
    RULE_tipo_especificador = 3
    RULE_fun_declaracao = 4
    RULE_params = 5
    RULE_param_lista = 6
    RULE_param = 7
    RULE_composto_decl = 8
    RULE_local_declaracoes = 9
    RULE_statement_lista = 10
    RULE_statement = 11
    RULE_expressao_decl = 12
    RULE_selecao_decl = 13
    RULE_iteracao_decl = 14
    RULE_retorno_decl = 15
    RULE_expressao = 16
    RULE_var = 17
    RULE_simples_expressao = 18
    RULE_soma_expressao = 19
    RULE_termo = 20
    RULE_fator = 21
    RULE_ativacao = 22

    ruleNames =  [ "programa", "declaracao", "var_declaracao", "tipo_especificador", 
                   "fun_declaracao", "params", "param_lista", "param", "composto_decl", 
                   "local_declaracoes", "statement_lista", "statement", 
                   "expressao_decl", "selecao_decl", "iteracao_decl", "retorno_decl", 
                   "expressao", "var", "simples_expressao", "soma_expressao", 
                   "termo", "fator", "ativacao" ]

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
            self._declaracao = None # DeclaracaoContext
            self.decl = list() # of DeclaracaoContexts

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(cminusParser.DeclaracaoContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                localctx._declaracao = self.declaracao()
                localctx.decl.append(localctx._declaracao)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cminusParser.INT or _la==cminusParser.VOID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 2, self.RULE_declaracao)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.var_declaracao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
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
        self.enterRule(localctx, 4, self.RULE_var_declaracao)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.tipo_especificador()
                self.state = 56
                self.match(cminusParser.ID)
                self.state = 57
                self.match(cminusParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.tipo_especificador()
                self.state = 60
                self.match(cminusParser.ID)
                self.state = 61
                self.match(cminusParser.LSBRACKET)
                self.state = 62
                self.match(cminusParser.NUM)
                self.state = 63
                self.match(cminusParser.RSBRACKET)
                self.state = 64
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
        self.enterRule(localctx, 6, self.RULE_tipo_especificador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
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
        self.enterRule(localctx, 8, self.RULE_fun_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.tipo_especificador()
            self.state = 71
            self.match(cminusParser.ID)
            self.state = 72
            self.match(cminusParser.LPAREN)
            self.state = 73
            self.params()
            self.state = 74
            self.match(cminusParser.RPAREN)
            self.state = 75
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
        self.enterRule(localctx, 10, self.RULE_params)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.param_lista(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_param_lista, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.param()
            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.Param_listaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_param_lista)
                    self.state = 84
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 85
                    self.match(cminusParser.COMMA)
                    self.state = 86
                    self.param() 
                self.state = 91
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
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.tipo_especificador()
                self.state = 93
                self.match(cminusParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.tipo_especificador()
                self.state = 96
                self.match(cminusParser.ID)
                self.state = 97
                self.match(cminusParser.LSBRACKET)
                self.state = 98
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
            self._local_declaracoes = None # Local_declaracoesContext
            self.l_decl = list() # of Local_declaracoesContexts
            self._statement_lista = None # Statement_listaContext
            self.stm_list = list() # of Statement_listaContexts

        def LCBRACKET(self):
            return self.getToken(cminusParser.LCBRACKET, 0)

        def RCBRACKET(self):
            return self.getToken(cminusParser.RCBRACKET, 0)

        def local_declaracoes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.Local_declaracoesContext)
            else:
                return self.getTypedRuleContext(cminusParser.Local_declaracoesContext,i)


        def statement_lista(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.Statement_listaContext)
            else:
                return self.getTypedRuleContext(cminusParser.Statement_listaContext,i)


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
        self.enterRule(localctx, 16, self.RULE_composto_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(cminusParser.LCBRACKET)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cminusParser.INT or _la==cminusParser.VOID:
                self.state = 103
                localctx._local_declaracoes = self.local_declaracoes()
                localctx.l_decl.append(localctx._local_declaracoes)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cminusParser.IF) | (1 << cminusParser.RETURN) | (1 << cminusParser.WHILE) | (1 << cminusParser.LPAREN) | (1 << cminusParser.SEMI) | (1 << cminusParser.LCBRACKET) | (1 << cminusParser.ID) | (1 << cminusParser.NUM))) != 0):
                self.state = 109
                localctx._statement_lista = self.statement_lista()
                localctx.stm_list.append(localctx._statement_lista)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(cminusParser.RCBRACKET)
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
            self._var_declaracao = None # Var_declaracaoContext
            self.var_decl = list() # of Var_declaracaoContexts

        def var_declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.Var_declaracaoContext)
            else:
                return self.getTypedRuleContext(cminusParser.Var_declaracaoContext,i)


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




    def local_declaracoes(self):

        localctx = cminusParser.Local_declaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_local_declaracoes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 117
                    localctx._var_declaracao = self.var_declaracao()
                    localctx.var_decl.append(localctx._var_declaracao)

                else:
                    raise NoViableAltException(self)
                self.state = 120 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_listaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._statement = None # StatementContext
            self.stms = list() # of StatementContexts

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.StatementContext)
            else:
                return self.getTypedRuleContext(cminusParser.StatementContext,i)


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




    def statement_lista(self):

        localctx = cminusParser.Statement_listaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement_lista)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 122
                    localctx._statement = self.statement()
                    localctx.stms.append(localctx._statement)

                else:
                    raise NoViableAltException(self)
                self.state = 125 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cminusParser.LPAREN, cminusParser.SEMI, cminusParser.ID, cminusParser.NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.expressao_decl()
                pass
            elif token in [cminusParser.LCBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.composto_decl()
                pass
            elif token in [cminusParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.selecao_decl()
                pass
            elif token in [cminusParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.iteracao_decl()
                pass
            elif token in [cminusParser.RETURN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
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

        def SEMI(self):
            return self.getToken(cminusParser.SEMI, 0)

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


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
        self.enterRule(localctx, 24, self.RULE_expressao_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cminusParser.LPAREN) | (1 << cminusParser.ID) | (1 << cminusParser.NUM))) != 0):
                self.state = 134
                self.expressao()


            self.state = 137
            self.match(cminusParser.SEMI)
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
            self.condicao = None # ExpressaoContext
            self._statement = None # StatementContext
            self.corpoIF = list() # of StatementContexts
            self.corpoElse = list() # of StatementContexts

        def IF(self):
            return self.getToken(cminusParser.IF, 0)

        def LPAREN(self):
            return self.getToken(cminusParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(cminusParser.RPAREN, 0)

        def LCBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(cminusParser.LCBRACKET)
            else:
                return self.getToken(cminusParser.LCBRACKET, i)

        def RCBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(cminusParser.RCBRACKET)
            else:
                return self.getToken(cminusParser.RCBRACKET, i)

        def expressao(self):
            return self.getTypedRuleContext(cminusParser.ExpressaoContext,0)


        def ELSE(self):
            return self.getToken(cminusParser.ELSE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.StatementContext)
            else:
                return self.getTypedRuleContext(cminusParser.StatementContext,i)


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
        self.enterRule(localctx, 26, self.RULE_selecao_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(cminusParser.IF)
            self.state = 140
            self.match(cminusParser.LPAREN)
            self.state = 141
            localctx.condicao = self.expressao()
            self.state = 142
            self.match(cminusParser.RPAREN)
            self.state = 143
            self.match(cminusParser.LCBRACKET)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cminusParser.IF) | (1 << cminusParser.RETURN) | (1 << cminusParser.WHILE) | (1 << cminusParser.LPAREN) | (1 << cminusParser.SEMI) | (1 << cminusParser.LCBRACKET) | (1 << cminusParser.ID) | (1 << cminusParser.NUM))) != 0):
                self.state = 144
                localctx._statement = self.statement()
                localctx.corpoIF.append(localctx._statement)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(cminusParser.RCBRACKET)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cminusParser.ELSE:
                self.state = 151
                self.match(cminusParser.ELSE)
                self.state = 152
                self.match(cminusParser.LCBRACKET)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cminusParser.IF) | (1 << cminusParser.RETURN) | (1 << cminusParser.WHILE) | (1 << cminusParser.LPAREN) | (1 << cminusParser.SEMI) | (1 << cminusParser.LCBRACKET) | (1 << cminusParser.ID) | (1 << cminusParser.NUM))) != 0):
                    self.state = 153
                    localctx._statement = self.statement()
                    localctx.corpoElse.append(localctx._statement)
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 159
                self.match(cminusParser.RCBRACKET)


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
        self.enterRule(localctx, 28, self.RULE_iteracao_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(cminusParser.WHILE)
            self.state = 163
            self.match(cminusParser.LPAREN)
            self.state = 164
            self.expressao()
            self.state = 165
            self.match(cminusParser.RPAREN)
            self.state = 166
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
        self.enterRule(localctx, 30, self.RULE_retorno_decl)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(cminusParser.RETURN)
                self.state = 169
                self.match(cminusParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(cminusParser.RETURN)
                self.state = 171
                self.expressao()
                self.state = 172
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
        self.enterRule(localctx, 32, self.RULE_expressao)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.var()
                self.state = 177
                self.match(cminusParser.ASSIGN)
                self.state = 178
                self.expressao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
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
        self.enterRule(localctx, 34, self.RULE_var)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(cminusParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(cminusParser.ID)
                self.state = 185
                self.match(cminusParser.LSBRACKET)
                self.state = 186
                self.expressao()
                self.state = 187
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
        self.enterRule(localctx, 36, self.RULE_simples_expressao)
        self._la = 0 # Token type
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                localctx.esquerda = self.soma_expressao(0)
                self.state = 192
                localctx.relacional = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cminusParser.LETHAN) | (1 << cminusParser.GETHAN) | (1 << cminusParser.EQ) | (1 << cminusParser.DF) | (1 << cminusParser.LT) | (1 << cminusParser.GT))) != 0)):
                    localctx.relacional = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 193
                localctx.direita = self.soma_expressao(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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
            self.op = None # Token

        def termo(self):
            return self.getTypedRuleContext(cminusParser.TermoContext,0)


        def soma_expressao(self):
            return self.getTypedRuleContext(cminusParser.Soma_expressaoContext,0)


        def getRuleIndex(self):
            return cminusParser.RULE_soma_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoma_expressao" ):
                listener.enterSoma_expressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoma_expressao" ):
                listener.exitSoma_expressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoma_expressao" ):
                return visitor.visitSoma_expressao(self)
            else:
                return visitor.visitChildren(self)



    def soma_expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cminusParser.Soma_expressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_soma_expressao, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.termo(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.Soma_expressaoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_soma_expressao)
                    self.state = 201
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 202
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==cminusParser.PLUS or _la==cminusParser.MINUS):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 203
                    self.termo(0) 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_termo, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.fator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cminusParser.TermoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==cminusParser.TIMES or _la==cminusParser.OVER):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 214
                    self.fator() 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_fator)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(cminusParser.LPAREN)
                self.state = 221
                self.expressao()
                self.state = 222
                self.match(cminusParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.ativacao()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 226
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
            self._expressao = None # ExpressaoContext
            self.arg_list = list() # of ExpressaoContexts

        def ID(self):
            return self.getToken(cminusParser.ID, 0)

        def LPAREN(self):
            return self.getToken(cminusParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(cminusParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cminusParser.COMMA)
            else:
                return self.getToken(cminusParser.COMMA, i)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cminusParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(cminusParser.ExpressaoContext,i)


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
        self.enterRule(localctx, 44, self.RULE_ativacao)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(cminusParser.ID)
                self.state = 230
                self.match(cminusParser.LPAREN)
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 231
                        localctx._expressao = self.expressao()
                        localctx.arg_list.append(localctx._expressao)
                        self.state = 232
                        self.match(cminusParser.COMMA) 
                    self.state = 238
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                self.state = 239
                localctx._expressao = self.expressao()
                localctx.arg_list.append(localctx._expressao)
                self.state = 240
                self.match(cminusParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(cminusParser.ID)
                self.state = 243
                self.match(cminusParser.LPAREN)
                self.state = 244
                self.match(cminusParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.param_lista_sempred
        self._predicates[19] = self.soma_expressao_sempred
        self._predicates[20] = self.termo_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def param_lista_sempred(self, localctx:Param_listaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def soma_expressao_sempred(self, localctx:Soma_expressaoContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def termo_sempred(self, localctx:TermoContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




