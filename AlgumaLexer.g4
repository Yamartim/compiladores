lexer grammar AlgumaLexer;

PalavraChave
    : ('inteiro' | 'logico' | 'algoritmo' | 'declare' | 'leia' | 'fim_algoritmo' | 'literal' | 'escreva' |
    'real' | 'se' | 'entao' | 'fim_se' | 'registro' | 'fim_registro' | 'faca' | 'ate' | 'para' |
    'fim_para' | 'caso' | 'seja' | 'fim_caso' | 'enquanto' | 'senao' | 'retorne' | 'fim_enquanto' | 'tipo' |
    'procedimento' | 'fim_procedimento' | 'funcao' | 'fim_funcao' | 'var' | 'constante' |'<-' | ':' |
    '(' | ')' | ',' | '..')
    ;

OperadorArit
    : ('*' | '/' | '+' | '-' | '%')
    ;
Op_Relacional
    : ('=' | '<>' | '>=' | '<=' | '>' | '<')
    ;
Dimensao
    : ('[' | ']')
    ;
OperadorLog
    : ('e' | 'ou' | '^' | '&')
    ;
FatorLogico
    : ('nao')
    ;
ParcelaLogica
    : ('falso' | 'verdadeiro')
    ;

fragment Letra	:	'a'..'z' | 'A'..'Z';

fragment Digito	:	'0'..'9';

IDENT	:	Letra(Letra|Digito|'_')* ;

NUM_REAL
    :   (Digito)+ '.' (Digito)+
    ;

NUM_INT
    :   (Digito)+
    ;

PontoIdent
    : '.'
    ;

CADEIA  :   '"'~["\\\r\n]+?'"' ;

CADEIANAOFECHADA : '"'~["\\\r\n]+? '\n' ;

WS
    : (' ' | '\t' | '\r' ) -> skip
    ;
QuebraLinha
    : '\n'
    ;

Comentario 
    : '{' ~('\n'|'\r')*? '\r'? '}' -> skip
    ;

ErroComentario
    : '{' ~('\n'|'\r'|'}')* '\n'
    ;

NaoIdentificado
    :  .
    ;