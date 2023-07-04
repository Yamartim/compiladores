from sys import argv
from antlr4 import FileStream, CommonTokenStream, Token
from AlgumaLexer import AlgumaLexer
from AlgumaParser import AlgumaParser
from antlr4.error.ErrorListener import ErrorListener

print('t3')
class MyErrorListener( ErrorListener ):
    output = None
    def __init__(self, file):
        super(MyErrorListener, self).__init__()
        self.output = file

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  
        #print('Linha '+ str(line)+ ' : erro sintatico proximo a ' + offendingSymbol.text)
        if(offendingSymbol.text == '<EOF>'):
            offendingSymbol.text = 'EOF'
        self.output.write(f'Linha {line}: erro sintatico proximo a {offendingSymbol.text}\n')
        raise Exception("erro")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        #raise Exception("Oh no2!!")
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        #raise Exception("Oh no3!!")
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        #raise Exception("Oh no4!!")
        pass

def main(argv):
    input = FileStream(argv[1], encoding='utf-8') #lendo arquivo

    file_out = open(argv[2], 'w')
    lexer = AlgumaLexer(input)

    vocabulary = lexer.ruleNames
    vocabulary.remove('Letra')
    vocabulary.remove('Digito')
    
    
    # itera por todos os tokens detectados pelo lexer
    t = lexer.nextToken()

    
    while (t.type != Token.EOF) :
        
        tokenTypeTemp = vocabulary[t.type-1]
        print(tokenTypeTemp)

        # tokens são analisados e printados no na saida até que se encontre um erro ou chegue ao final
        if tokenTypeTemp == 'NaoIdentificado':
            print('aqui')
            file_out.write(f"Linha {t.line}: {t.text} - simbolo nao identificado\n")
            file_out.write('Fim da compilacao\n')
            return
        elif tokenTypeTemp == 'ErroComentario':
            print('aqui')
            file_out.write(f"Linha {t.line}: comentario nao fechado\n")
            file_out.write('Fim da compilacao\n')
            return
        elif tokenTypeTemp == 'CADEIANAOFECHADA':
            print('aqui')
            file_out.write(f"Linha {t.line}: cadeia literal nao fechada\n")
            file_out.write('Fim da compilacao\n')
            return
        
        # passa para o proximo token e continua o loop
        t = lexer.nextToken()

    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = AlgumaParser(stream)
    parser.addErrorListener( MyErrorListener(file_out))
    try:
        parser.programa()
    except:
        file_out.write('Fim da compilacao\n')
        return

    file_out.write('Fim da compilacao\n')
    
if __name__ == '__main__':
    main(argv)
