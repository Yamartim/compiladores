from antlr4 import FileStream, CommonTokenStream, Token
from antlr4.error.ErrorListener import ErrorListener
from TileMapLexer import TileMapLexer
from TileMapParser import TileMapParser
from listaErros import listaErros


class ErroSintaticoListener( ErrorListener ):
    output = None
    def __init__(self, lista_erros: listaErros):
        self.erros = lista_erros
        super(ErroSintaticoListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  
        #print('Linha '+ str(line)+ ' : erro sintatico proximo a ' + offendingSymbol.text)
        if(offendingSymbol.text == '<EOF>'):
            offendingSymbol.text = 'EOF'
        #self.output.write(f'Linha {line}: erro sintatico proximo a {offendingSymbol.text}\n')
        self.erros.adicionarErro(offendingSymbol.line, 'erro sintatico proximo a ' + offendingSymbol.text)
        self.erros.printarErros()
        raise Exception('erro')

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        #raise Exception("Oh no2!!")
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        #raise Exception("Oh no3!!")
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        #raise Exception("Oh no4!!")
        pass

def ErrosLexicos(lexer, lista_erros: listaErros):
    token = lexer.nextToken()

    while token.type != Token.EOF:
        tokenType = lexer.ruleNames[token.type - 1]
        print(tokenType, token.text)

        if tokenType == 'CADEIANAOFECHADA':
            lista_erros.adicionarErro(token, 'cadeia literal nao fechada')
        elif tokenType == 'NaoIdentificado':
            lista_erros.adicionarErro(token, 'simbolo \'' + token.text + '\' nao identificado')

        token = lexer.nextToken()

    lexer.reset()