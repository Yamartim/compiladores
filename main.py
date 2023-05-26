import sys
from antlr4 import *
from AlgumaLexer import AlgumaLexer


def main(argv):
    input = FileStream(argv[1], encoding='utf-8')
    #input = FileStream('input.txt', encoding='utf-8')
    #file_str = open('input.txt','r').read()
    file_out = open('saidaProduzida/saida_t1/'+ argv[1][:-4] + '_saida.txt', 'w')
    lexer = AlgumaLexer(input)

    t = lexer.nextToken()
    while (t.type != Token.EOF) :
        tokenTypeTemp = lexer.symbolicNames[t.type]
        if tokenTypeTemp == 'PalavraChave':
            file_out.write('<\'' + t.text + '\',\'' + t.text + '\'>\n')
            #print('<\'' + t.text + '\',\'' + t.text + '\'>')
        else:
            file_out.write('<\'' + t.text + '\',\'' + tokenTypeTemp + '\'>\n')
            #print('<\'' + t.text + '\',' + tokenTypeTemp + '>')
        t = lexer.nextToken()
    
if __name__ == '__main__':
    main(sys.argv)
