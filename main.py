import sys
from antlr4 import *
from AlgumaLexer import AlgumaLexer


def main(argv):
    input = FileStream(argv[1], encoding='utf-8')
    #input = FileStream('casos-de-teste/1.casos_teste_t1/entrada/1-algoritmo_2-2_apostila_LA.txt', encoding='utf-8')
    #file_str = open('input.txt','r').read()
    file_out = open(argv[2], 'w')
    lexer = AlgumaLexer(input)

    t = lexer.nextToken()
    while (t.type != Token.EOF) :
        tokenTypeTemp = lexer.symbolicNames[t.type]
        if tokenTypeTemp == 'PalavraChave' or tokenTypeTemp == 'OperadorArit':
            file_out.write('<\'' + t.text + '\',\'' + t.text + '\'>\n')
            #print('<\'' + t.text + '\',\'' + t.text + '\'>')
        elif tokenTypeTemp == 'OperadorArit':
            print('operador arit')
            file_out.write('<\'' + t.text + '\',\'' + t.text + '\'>\n')
        else:
            file_out.write('<\'' + t.text + '\',' + tokenTypeTemp + '>\n')
            #print('<\'' + t.text + '\',' + tokenTypeTemp + '>')
        t = lexer.nextToken()
    
if __name__ == '__main__':
    main(sys.argv)
