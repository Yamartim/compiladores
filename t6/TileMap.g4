grammar TileMap;

/*palavras chave*/

Programa : DeclMapa Declaracoes Comandos EOF;

DeclMapa : 'mapa' Identificador Num_Inteiro'px' Num_Inteiro'x'Num_Inteiro;

Declaracoes : Regioes|Biomas|Areas|Tiles;

Regioes: 'Regioes:' DeclRegiao+; //conjunto de areas com um bioma associado
DeclRegiao : Identificador '-' 'areas['Identificador (',' Identificador)* ']' 'areas['Identificador (',' Identificador)* ']';

Biomas: 'Biomas:' DeclBioma+;
DeclBioma : Identificador '-' ; //pensar no que define um bioma

Areas: 'Areas:' DeclArea+;
DeclArea : Identificador '-' TipoArea;

Tiles: 'Tiles:' DeclTile+;
DeclTile : Identificador '-' CADEIA;

/*areas e estruturas*/

TipoArea : Ponto | Linha | Retang | Polign | Circulo;

Ponto : '('Num_Inteiro','Num_Inteiro')';

Linha : 'Linha('Ponto'-'Ponto')';

Retang : 'Retangulo('Ponto'c'Num_Inteiro'lx'Num_Inteiro'ly)';

Polign : 'Poligono('Ponto'c'Num_Inteiro'r'Num_Inteiro'ly)';

Circulo : 'Circulo('Ponto'c'Num_Inteiro'r)';

DeclEstrutura : Identificador':' SerieTiles+;
SerieTiles : '[' Identificador (',' Identificador)* ']'; //incluir tile null


/*comandos*/

Comandos:;

/*whitespace e comentarios*/

Comentario: '//' ~('\n'|'\r'|'}')* '\r'? '\n' {skip();};
Ws: ( ' ' | '\t' | '\r' | '\n') {skip();};


Num_Inteiro: ('0'..'9')+;

CADEIA
    : ('\'' ~('\'' | '\n')* '\'') | ('"'  ~('"' | '\n')* '"')
    ;
CADEIANAOFECHADA
    : ('\'' ~('\'' | '\n')* '\n') | ('"'  ~('"' | '\n')* '\n')
    ;

Identificador: ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
