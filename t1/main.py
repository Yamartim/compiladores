import sys
from antlr4 import *
from AlgumaLexer import AlgumaLexer


def main(argv):

    input = FileStream(argv[1], encoding='utf-8') # recebe a referencia do arquivo de entrada

    file_out = open(argv[2], 'w') # recebe a referencia do arquivo de saida

    lexer = AlgumaLexer(input) # criando um lexer com os dados do arquivo de entrada

    contador_linhas = 1 # conta as linhas do código fonte para relatorios de erro

    # lista de todos os tokens presentes
    lista_tokens = ['PalavraChave' , 'OperadorArit', 'Op_Relacional', 'OperadorLog', 'FatorLogico',
            'PontoIdent', 'Dimensao', 'ParcelaLogica']

    
    # itera por todos os tokens detectados pelo lexer
    t = lexer.nextToken()
    while (t.type != Token.EOF) :
        tokenTypeTemp = lexer.symbolicNames[t.type]
        # se é detectada uma quebra de linha no codigo atualiza o contador
        if tokenTypeTemp == 'QuebraLinha': 
            contador_linhas += 1
            t = lexer.nextToken()
            continue

        # tokens são analisados e printados no na saida até que se encontre um erro ou chegue ao final
        if tokenTypeTemp in lista_tokens:
            file_out.write(f"<'{t.text}','{t.text}'>\n")
        elif tokenTypeTemp == 'NaoIdentificado':
            file_out.write(f"Linha {contador_linhas}: {t.text} - simbolo nao identificado\n")
            return
        elif tokenTypeTemp == 'ErroComentario':
            file_out.write(f"Linha {contador_linhas}: comentario nao fechado\n")
            return
        elif tokenTypeTemp == 'CADEIANAOFECHADA':
            file_out.write(f"Linha {contador_linhas}: cadeia literal nao fechada\n")
            return
        else:
            file_out.write(f"<'{t.text}',{tokenTypeTemp}>\n")
        
        # passa para o proximo token e continua o loop
        t = lexer.nextToken()
    
if __name__ == '__main__':
    main(sys.argv)
