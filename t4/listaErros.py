import TabelaDeSimbolos
from antlr4 import *
from AlgumaParser import AlgumaParser

class listaErros():
    listaErrosSemanticos = []

    def __init__(self):
        listaErros.listaErrosSemanticos = []

    def adicionarErroSemantico(t, mensagem):
        listaErros.listaErrosSemanticos.append(f'Linha {t.line}: {mensagem}')

    def printarErros():
        for erro in listaErros.listaErrosSemanticos:
            print(erro)
    
    def printarArquivo(arquivo):
        for erro in listaErros.listaErrosSemanticos:
            arquivo.write(erro + '\n')
        arquivo.write('Fim da compilacao\n')
        

