class TabelaDeSimbolos:
    #Usar strings como tipos: 'INTEIRO', 'REAL' ou 'INVALIDO' para tipos
    #estabelecer algumas regras para inserção,
    #inserir o identificador como key,
    #inserir uma lista com o primeiro elemento como o tipo do identificador
    #inserção livre para a segunda posição em diante
    
    def __init__(self):
        self.Tabela = {}
    
    def inserir(self, nome, tipo):
        #insere o nome da variavel na tabela
        self.Tabela[nome] = tipo

    def existe(self, nome):
        #verifica se o nome já está na tabela
        if nome in self.Tabela:
            return True
        else:
            return False
        
    def verificar(self, nome):
        #retorna o tipo da variavel
        if nome in self.Tabela:
            return self.Tabela[nome]
        else:
            return None
    
    def concatenar(self, tabela2):
        self.Tabela = {**self.Tabela, **tabela2}
    
    def retornarTabela(self):
        return self.Tabela