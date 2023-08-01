from antlr4 import Token

class listaErros():

    def __init__(self):
        self.listaErrosSemanticos = []

    def adicionarErroSemantico(self, t:Token, mensagem):
        self.listaErrosSemanticos.append(f'Linha {t.line}: {mensagem}')

    def adicionarErroVarNaoDecl(self, t:Token):
        self.listaErrosSemanticos.append(f'Linha {t.line}: identificador {t.text} nao declarado')

    def printarErros(self):
        for erro in self.listaErrosSemanticos:
            print(erro)
    
    def printarArquivo(self, arquivo):
        for erro in self.listaErrosSemanticos:
            arquivo.write(erro + '\n')
        arquivo.write('Fim da compilacao\n')
        

