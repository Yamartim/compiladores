import sys
from antlr4 import *
from AlgumaLexer import AlgumaLexer


def main(argv):
    input = FileStream(argv[1], encoding='utf-8')
    #file_str = open('input.txt','r').read()
    lexer = AlgumaLexer(input)

    t = lexer.nextToken()
    while (t.type != Token.EOF) :
        tokenTypeTemp = lexer.symbolicNames[t.type]
        if tokenTypeTemp == 'PalavraChave':
            print('<' + t.text + ',' + t.text + '>')
        else:
            print('<' + t.text + ',' + tokenTypeTemp + '>')
        t = lexer.nextToken()
    
if __name__ == '__main__':
    main(sys.argv)