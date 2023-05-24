lexer grammar AlgumaLexer;

PalavraChave
    : ('inteiro' | 'logico' | 'algoritmo' | 'declare' | 'leia' |
    'fim_algoritmo' | 'literal' | 'escreva' | 'real' | ':' | '(' | ')' | ',')
    ;

fragment
Letra		:	'a'..'z' | 'A'..'Z';

fragment
Digito	:	'0'..'9';

IDENT	:	Letra(Letra|Digito)* ;

WS
    : (' ' | '\t' | '\r' | '\n') -> skip
    ;
Comentario 
    : '{ ' ~('\n'|'\r')* '\r'? '}' -> skip
    ;
Cadeia
    : ('\'' ~('\'')* '\'') | ('"'  ~('"')* '"')
    ;