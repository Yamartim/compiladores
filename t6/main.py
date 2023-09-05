from ast import arg
from sys import argv
from antlr4 import FileStream, CommonTokenStream, Token
from TileMapLexer import TileMapLexer
from TileMapParser import TileMapParser
from MyTileMapVisitor import TileMapVisitor
from ErrosListener import ErroSintaticoListener, ErrosLexicos
from listaErros import listaErros 

def main(argv):
    input = FileStream(argv[1], encoding='utf-8') #lendo arquivo

    erros = listaErros()


    #file_out = open(argv[2], 'w')

    lexer = TileMapLexer(input)
    verificarLexico = False

    vocabulary = lexer.ruleNames
    #vocabulary.remove('Letra')
    #vocabulary.remove('Digito')
    
    #ErrosLexicos(lexer, erros)
    

    stream = CommonTokenStream(lexer)

    parser = TileMapParser(stream)
    parser.addErrorListener( ErroSintaticoListener(erros)) #(ile_out))
    #try:
    tree = parser.programa()
    visitor = TileMapVisitor()
    visitor.visitPrograma(tree, parser, erros, argv[1], argv[2])
        
    # printar erros

    return

    
if __name__ == '__main__':
    main(argv)
    #main(('_', '.\\teste\\input\\teste01.tilemap', '.\\teste\\output\\teste01.png'))
