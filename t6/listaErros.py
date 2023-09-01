#import TabelaDeSimbolos
from antlr4 import *
#from AlgumaParser import AlgumaParser

class listaErros():
    listaErros = []

    def __init__(self):
        listaErros.listaErros = []

    def adicionarErro(t, mensagem):
        listaErros.listaErros.append(f'Linha {t.line}: {mensagem}')

    def printarErros():
        listaErros.listaErros = list(dict.fromkeys(listaErros.listaErros))
        for erro in listaErros.listaErros:
            print(erro)
    
    def printarArquivo(arquivo):
        
        listaErros.listaErros = list(dict.fromkeys(listaErros.listaErros))
        for erro in listaErros.listaErros:
            arquivo.write(erro + '\n')
        arquivo.write('Fim da compilacao\n')
        

