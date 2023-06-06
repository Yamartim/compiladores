import sys
from antlr4 import *
from AlgumaLexer import AlgumaLexer


def main(argv):
    input = FileStream(argv[1], encoding='utf-8')
    #input = FileStream('casos-de-teste/1.casos_teste_t1/entrada/1-algoritmo_2-2_apostila_LA.txt', encoding='utf-8')
    #file_str = open('input.txt','r').read()
    file_out = open(argv[2], 'w')
    lexer = AlgumaLexer(input)
    contador = 1

    t = lexer.nextToken()
    lista = ['PalavraChave' , 'OperadorArit', 'Op_Relacional', 'OperadorLog', 'FatorLogico',
            'PontoIdent', 'Dimensao', 'ParcelaLogica']
    while (t.type != Token.EOF) :
        tokenTypeTemp = lexer.symbolicNames[t.type]
        if tokenTypeTemp == 'QuebraLinha':
            contador += 1
            t = lexer.nextToken()
            continue

        if tokenTypeTemp in lista:
            file_out.write('<\'' + t.text + '\',\'' + t.text + '\'>\n')
            #print('<\'' + t.text + '\',\'' + t.text + '\'>')
        elif tokenTypeTemp == 'NaoIdentificado':
            file_out.write('Linha ' + str(contador)+ ': ' + t.text + ' - simbolo nao identificado\n')
            return
        elif tokenTypeTemp == 'ErroComentario':
            file_out.write('Linha ' + str(contador)+ ': comentario nao fechado\n')
            return
        elif tokenTypeTemp == 'CADEIANAOFECHADA':
            file_out.write('Linha ' + str(contador) + ': cadeia literal nao fechada\n')
            return
        else:
            file_out.write('<\'' + t.text + '\',' + tokenTypeTemp + '>\n')
            #print('<\'' + t.text + '\',' + tokenTypeTemp + '>')
        t = lexer.nextToken()
    
if __name__ == '__main__':
    main(sys.argv)
