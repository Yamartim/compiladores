//java -jar ..\antlr-4.13.0-complete.jar TileMap.g4 -Dlanguage=Python3 -visitor -o .antlr/ 
grammar TileMap;

/*palavras chave*/


programa : declMapa declaracoes comandos EOF;

declMapa : 'mapa' Identificador Num_Inteiro'px' Num_Inteiro'x'Num_Inteiro;

declaracoes : (regioes|biomas|areas|tiles|estruturas)*;

regioes: 'Regioes:' declRegiao+; //conjunto de areas com um bioma associado
declRegiao : Identificador '-' Identificador 'areas''['Identificador (',' Identificador)* ']';

biomas: 'Biomas:' declBioma+;
declBioma : Identificador '-' 'bg''['Identificador']' (',' 'tiles''['Identificador (',' Identificador)* ']')? (',' 'estruturas''['Identificador (',' Identificador)* ']')? ; //pensar no que define um bioma

areas: 'Areas:' declArea+;
declArea : Identificador '-' tipoArea;

tiles: 'Tiles:' declTile+;
declTile : Identificador '-' CADEIA;

estruturas: 'Estruturas:' declEstrutura+;
declEstrutura : Identificador':' serieTiles+;
unidadeSerie : Nada | Identificador;
serieTiles : '[' unidadeSerie (',' unidadeSerie)* ']'; //incluir tile null

/*areas e estruturas*/

tipoArea : ponto | linha | retang | polign | circulo;

ponto : '('Num_Inteiro','Num_Inteiro')';

linha : 'Linha''('ponto'-'ponto')';

retang : 'Retangulo''('ponto'vert'','ponto'vert)'
       | 'Retangulo''('ponto'c'','Num_Inteiro'lx'','Num_Inteiro'ly'')';

polign : 'Poligono''('ponto'c'','Num_Inteiro'r'','Num_Inteiro'ly'')';

circulo : 'Circulo''('ponto'c'','Num_Inteiro'r'')';


/*comandos*/

comandos : (cmdDesenhe|cmdEspalharEstruturas|cmdMostrarDesenho|cmdSalvarDesenho)* ;

cmdDesenhe : 'Desenhe''('Identificador')' ;

cmdEspalharEstruturas : 'Espalhe''('Identificador','Identificador')';

cmdMostrarDesenho: 'Mostrar''('')';

cmdSalvarDesenho: 'Salvar''('')';


/*whitespace e comentarios*/

Comentario: '//' ~('\n'|'\r'|'}')* '\r'? '\n' -> skip;
Ws: ( ' ' | '\t' | '\r' | '\n') -> skip;

Nada: 'nada'|'_';

Num_Inteiro: ('0'..'9')+;

CADEIA
    : ('\'' ~('\'' | '\n')* '\'') | ('"'  ~('"' | '\n')* '"')
    ;
CADEIANAOFECHADA
    : ('\'' ~('\'' | '\n')* '\n') | ('"'  ~('"' | '\n')* '\n')
    ;

Identificador: ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
