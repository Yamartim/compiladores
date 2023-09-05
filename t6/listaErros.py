#import TabelaDeSimbolos
#from antlr4 import *
#from AlgumaParser import AlgumaParser

class listaErros():

    def __init__(self):
        self.listaErros = []

    def adicionarErro(self, linha, mensagem):
        self.listaErros.append(f'Linha {linha}: {mensagem}')

    def printarErros(self):
        self.listaErros = list(dict.fromkeys(self.listaErros))
        for erro in self.listaErros:
            print(erro)
    
    def printarArquivo(self, arquivo):
        
        self.listaErros = list(dict.fromkeys(self.listaErros))
        for erro in self.listaErros:
            arquivo.write(erro + '\n')
        arquivo.write('Fim da compilacao\n')
        

