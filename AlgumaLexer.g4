lexer grammar AlgumaLexer;

PalavraChave
    : ('inteiro' | 'logico' | 'algoritmo' | 'declare' | 'leia' | 'fim_algoritmo' | 'literal' | 'escreva' |
    'real' | 'se' | 'entao' | 'fim_se' | 'registro' | 'fim_registro' | 'faca' | 'ate' | 'para' |
    'fim_para' | 'caso' | 'seja' | 'fim_caso' | 'enquanto' | 'senao' | 'retorne' | 'fim_enquanto' |'<-' | ':' |
    '(' | ')' | ',' | '..')
    ;

OperadorArit
    : ('*' | '/' | '+' | '-' | '%')
    ;
Op_Relacional
    : ('=' | '<>' | '>=' | '<=' | '>' | '<')
    ;

fragment
Letra		:	'a'..'z' | 'A'..'Z';

fragment
Digito	:	'0'..'9';

IDENT	:	Letra(Letra|Digito)* ;

NUM_REAL
    :   (Digito)+ '.' (Digito)+
    ;

NUM_INT
    :   (Digito)+
    ;

CADEIA  :   '"'~["\\\r\n]+?'"' ;

WS
    : (' ' | '\t' | '\r' | '\n') -> skip
    ;
Comentario 
    : '{' ~('\n'|'\r')* '\r'? '}' -> skip
    ;
Cadeia
    : ('\'' ~('\'')* '\'') | ('"'  ~('"')* '"')
    ;
ErroComentario
    : '{' ~('\n'|'\r'|'}')* '\n'
    ;

