grammar cminus;


/* Parser Rules */

 programa
    : declaracao_lista
    ;

  declaracao_lista
    : declaracao_lista declaracao
    | declaracao
    ;

  declaracao
    : var_declaracao
    | fun_declaracao
    ;

  var_declaracao
    : tipo_especificador ID SEMI
    | tipo_especificador ID LSBRACKET NUM RSBRACKET SEMI
    ;

  tipo_especificador
    : INT
    | VOID
    ;

  fun_declaracao
    : tipo_especificador ID LPAREN params RPAREN composto_decl
    ;

  params
    : param_lista
    | VOID
    ;

  param_lista
    : param_lista COMMA param
    | param
    ;

  param
    : tipo_especificador ID
    | tipo_especificador ID LSBRACKET RSBRACKET
    ;

  composto_decl
    : LCBRACKET local_declaracoes statement_lista RCBRACKET
    | LCBRACKET local_declaracoes RCBRACKET
    | LCBRACKET statement_lista RCBRACKET
    | LCBRACKET RCBRACKET
    ;

  local_declaracoes
    : local_declaracoes var_declaracao
    | var_declaracao
    ;

  statement_lista
    : statement_lista statement
    | statement
    ;

  statement
    : expressao_decl
    | composto_decl
    | selecao_decl
    | iteracao_decl
    | retorno_decl
    ;

  expressao_decl
    : expressao SEMI
    | SEMI
    ;

  selecao_decl
    : IF LPAREN expressao RPAREN corpoIF=statement
    | IF LPAREN expressao RPAREN corpoIF=statement ELSE corpoElse=statement
    ;

  iteracao_decl
    : WHILE LPAREN expressao RPAREN statement
    ;

  retorno_decl
    : RETURN SEMI
    | RETURN expressao SEMI
    ;

  expressao
    : var ASSIGN expressao
    | simples_expressao
    ;

  var
    : ID
    | ID LSBRACKET expressao RSBRACKET
    ;

  simples_expressao
    : esquerda=soma_expressao relacional=(LETHAN| LT| GT| GETHAN| EQ| DF) direita=soma_expressao
    | operacao=soma_expressao
    ;

  soma_expressao
    : soma_expressao op=('+'|'-') termo     # addsub
    | termo                                             # term
    ;


  termo
    : termo op=('/'|'*') fator
    | fator
    ;


  fator
    : LPAREN expressao RPAREN
    | var
    | ativacao
    | NUM
    ;

  ativacao
    : ID LPAREN arg_lista RPAREN
    | ID LPAREN RPAREN
    ;

  arg_lista
    : arg_lista COMMA expressao
    | expressao
    ;

    /* Lexer Rules */

      //RESERVED_WORD : 'else' | 'if' | 'int' | 'return' | 'void' | 'while' ;
      ELSE : 'else' ;
      IF : 'if' ;
      INT : 'int' ;
      RETURN : 'return' ;
      VOID : 'void' ;
      WHILE : 'while';
      LETHAN : '<=' ;
      GETHAN : '>=' ;
      ASSIGN : '=' ;
      EQ : '==' ;
      DF : '!=' ;
      LT : '<' ;
      GT : '>' ;
      PLUS : '+' ;
      MINUS : '-' ;
      TIMES : '*' ;
      OVER : '/' ;
      LPAREN : '(';
      RPAREN : ')';
      SEMI : ';' ;
      COMMA : ',' ;
      LCBRACKET : '{' ;
      RCBRACKET : '}' ;
      LSBRACKET : '[';
      RSBRACKET : ']' ;

      //tokens {ELSE, IF, INT, RETURN, VOID, WHILE}
      
      ID : [a-zA-Z]+ ; // match identifiers
      NUM : [0-9]+ ; // match integers

      BLOCK_COMMENT: '/*' .*? '*/' -> skip
      ;
      //LINE_COMMENT: '//' ~[\r\n]* -> skip
      //;
      // Whitespace
      WS : [ \t\r\n\f]+ -> skip ;
