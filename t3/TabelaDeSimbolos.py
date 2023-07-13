class TabelaDeSimbolos:
    #Usar strings como tipos: 'INTEIRO', 'REAL' ou 'INVALIDO'
    Tabela = None
    def __init__(self):
        TabelaDeSimbolos.Tabela = {}
    
    def inserir(nome, tipo):
        #insere o nome da variavel na tabela
        TabelaDeSimbolos.Tabela[nome] = tipo

    def existe(nome):
        #verifica se o nome já está na tabela
        if nome in TabelaDeSimbolos.Tabela:
            return True
        else:
            return False
        
    def verificar(nome):
        #retorna o tipo da variavel
        if nome in TabelaDeSimbolos.Tabela:
            return TabelaDeSimbolos.Tabela[nome]
        else:
            return None