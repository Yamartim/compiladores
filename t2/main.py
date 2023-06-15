import sys
from antlr4 import *
from AlgumaLexer import AlgumaLexer
from AlgumaParser import AlgumaParser
from antlr4.error.ErrorListener import ErrorListener

#Da uma olhada aqui embaixo Martim
#peguei do stack overflow, está sendo chamado junto com algum detector de erro do antlr
#mas, como o q só conta é o que está nos casos de teste, acho que da para usar,
#já que a saída impressa no terminal não é considerada
class MyErrorListener( ErrorListener ):
    output = None
    def __init__(self, file):
        super(MyErrorListener, self).__init__()
        self.output = file

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  
        #print('Linha '+ str(line)+ ' : erro sintatico proximo a ' + offendingSymbol.text)
        if(offendingSymbol.text == '<EOF>'):
            offendingSymbol.text = 'EOF'
        self.output.write('Linha '+ str(line)+ ': erro sintatico proximo a ' + offendingSymbol.text + '\n')
        #transformar o print para uma linha no arquivo de saída.

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception("Oh no2!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("Oh no3!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Oh no4!!")

def main(argv):
    input = FileStream(argv[1], encoding='utf-8')

    file_out = open(argv[2], 'w')
    lexer = AlgumaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AlgumaParser(stream)
    parser.addErrorListener( MyErrorListener(file_out))
    parser.programa()
    file_out.write('Fim da compilacao\n')
    '''
    print(tree.toStringTree(recog=parser))
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
    '''
    
if __name__ == '__main__':
    main(sys.argv)
