from sys import argv
from antlr4 import FileStream, CommonTokenStream, Token
from AlgumaLexer import AlgumaLexer
from AlgumaParser import AlgumaParser
from antlr4.error.ErrorListener import ErrorListener
from MyVisitor import AlgumaVisitor
from GeradorCodigo import GeradorCodigo
from listaErros import listaErros


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
    verificarLexico = False

    vocabulary = lexer.ruleNames
    vocabulary.remove('Letra')
    vocabulary.remove('Digito')
    

    if(verificarLexico):
        # itera por todos os tokens detectados pelo lexer
        t = lexer.nextToken()
        while (t.type != Token.EOF) :
        
            token_type_temp = vocabulary[t.type-1]
            print(token_type_temp)

            # tokens são analisados e printados no na saida até que se encontre um erro ou chegue ao final
            if token_type_temp == 'NaoIdentificado':
                print('aqui')
                file_out.write(f"Linha {t.line}: {t.text} - simbolo nao identificado\n")
                file_out.write('Fim da compilacao\n')
                return
            elif token_type_temp == 'ErroComentario':
                print('aqui')
                file_out.write(f"Linha {t.line}: comentario nao fechado\n")
                file_out.write('Fim da compilacao\n')
                return
            elif token_type_temp == 'CADEIANAOFECHADA':
                print('aqui')
                file_out.write(f"Linha {t.line}: cadeia literal nao fechada\n")
                file_out.write('Fim da compilacao\n')
                return
        
            # passa para o proximo token e continua o loop
            t = lexer.nextToken()

        lexer.reset()

    stream = CommonTokenStream(lexer)
    parser = AlgumaParser(stream)
    #parser.addErrorListener( MyErrorListener(file_out))
    #try:
    tree = parser.programa()
    visitor = AlgumaVisitor()
    visitor.visitPrograma(tree, parser)
        
    listaErros.printarErros()
    if listaErros.listaErrosSemanticos != []:
        listaErros.printarArquivo(file_out)
    else:
        input = FileStream(argv[1], encoding='utf-8')
        lexer = AlgumaLexer(input)
        stream2 = CommonTokenStream(lexer)
        parser = AlgumaParser(stream2)
        tree = parser.programa()
        gerador = GeradorCodigo(parser)
        gerador.visitPrograma(tree)
        print(gerador.saida)
        file_out.write(gerador.saida)

    return

    
if __name__ == '__main__':
    main(argv)
