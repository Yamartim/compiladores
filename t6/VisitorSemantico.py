# Generated from TileMap.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TileMapParser import TileMapParser
else:
    from TileMapParser import TileMapParser
from TabelaDeSimbolos import TabelaDeSimbolos
from listaErros import listaErros


# This class defines a complete generic visitor for a parse tree produced by TileMapParser.

class TileMapVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TileMapParser#nada.
    def visitNada(self, ctx:TileMapParser.NadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#programa.
    def visitPrograma(self, ctx:TileMapParser.ProgramaContext):
        self.arquivo = None
        self.tabela = TabelaDeSimbolos()
        return self.visitChildren(ctx)
    
    def verificarIdent(self, ctx, multiplos, modo, inicio, fim, tipo):
        #modo determina qual comparação será feita,
        #há momentos que precisamos que não existem identificadores
        #e há momentos que precisamos que todos os identificadores existam
        #modo True adiciona erro se existir algum identificador com o mesmo nome
        #modo False adiciona erro se não existir algum identificador com aquele nome
        
        flag = True
        if modo:
            string = ' já existe'
        else:
            string = ' não existe'

        if multiplos:
            i = inicio
            while ctx.Identificador(i) != None and i != fim:
                ident = ctx.Identificador(i).getText()
                existe = self.tabela.existe(ident)
                if (existe and modo) or (not existe and not modo): #porta XNOR ou equivalencia para controle da verificacao
                    print(i)
                    listaErros.adicionarErro(ctx.start, 'identificador ' + ident + string)
                    flag = False
                elif tipo != None and self.tabela.verificar(ident) != None:
                    temp = self.tabela.verificar(ident)
                    if temp[0] != tipo:
                        listaErros.adicionarErro(ctx.start, 'identificador ' + ident + ' nao é do tipo ' + tipo)
                i += 1
        else:
            ident = ctx.Identificador().getText()
            existe = self.tabela.existe(ident)
            if (existe and modo) or (not existe and not modo):
                listaErros.adicionarErro(ctx.start, 'identificador ' + ident + string)
                flag = False
            elif tipo != None and self.tabela.verificar(ident) != None:
                temp = self.tabela.verificar(ident)
                if temp[0] != tipo:
                    listaErros.adicionarErro(ctx.start, 'identificador ' + temp[0] + 'nao eh do tipo ' + tipo)

        return flag



    # Visit a parse tree produced by TileMapParser#declMapa.
    def visitDeclMapa(self, ctx:TileMapParser.DeclMapaContext):
        ident = ctx.Identificador().getText()

        self.arquivo = open(ident, 'w')

        #estabelecer algumas regras para inserção,
        #inserir o identificador como key,
        #inserir uma lista com o primeiro elemento como o tipo do identificador
        #inserção livre para a segunda posição em diante
            
        self.tam_tiles = int(ctx.Num_Inteiro(0).getText())
        self.dimensao = (int(ctx.Num_Inteiro(1).getText()), int(ctx.Num_Inteiro(2).getText()))

        self.tabela.inserir(ident, ['mapa'])


        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declaracoes.
    def visitDeclaracoes(self, ctx:TileMapParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#regioes.
    def visitRegioes(self, ctx:TileMapParser.RegioesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declRegiao.
    def visitDeclRegiao(self, ctx:TileMapParser.DeclRegiaoContext):

        
        if self.verificarIdent(ctx, True, True, 0, 1, None) and self.verificarIdent(ctx, True, False, 1, -1, 'area'):
            self.tabela.inserir(ctx.Identificador(0).getText(), ['regiao', ctx])

            

        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#biomas.
    def visitBiomas(self, ctx:TileMapParser.BiomasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declBioma.
    def visitDeclBioma(self, ctx:TileMapParser.DeclBiomaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#areas.
    def visitAreas(self, ctx:TileMapParser.AreasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declArea.
    def visitDeclArea(self, ctx:TileMapParser.DeclAreaContext):

        if self.verificarIdent(ctx, False, True, 0, -1, None):
            self.tabela.inserir(ctx.Identificador().getText(), ['area', ctx])

        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#tiles.
    def visitTiles(self, ctx:TileMapParser.TilesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declTile.
    def visitDeclTile(self, ctx:TileMapParser.DeclTileContext):
        
        if self.verificarIdent(ctx, False, True, 0, -1, None):
            self.tabela.inserir(ctx.Identificador().getText(), ['tile', ctx.CADEIA().getText()])

        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#tipoArea.
    def visitTipoArea(self, ctx:TileMapParser.TipoAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#ponto.
    def visitPonto(self, ctx:TileMapParser.PontoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#linha.
    def visitLinha(self, ctx:TileMapParser.LinhaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#retang.
    def visitRetang(self, ctx:TileMapParser.RetangContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#polign.
    def visitPolign(self, ctx:TileMapParser.PolignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#circulo.
    def visitCirculo(self, ctx:TileMapParser.CirculoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declEstrutura.
    def visitDeclEstrutura(self, ctx:TileMapParser.DeclEstruturaContext):

        self.verificarIdent(ctx, False, True, 0, -1, None)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#serieTiles.
    def visitSerieTiles(self, ctx:TileMapParser.SerieTilesContext):

        self.verificarIdent(ctx, True, False, -1)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#comandos.
    def visitComandos(self, ctx:TileMapParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#cmdDesenhe.
    def visitCmdDesenhe(self, ctx:TileMapParser.CmdDesenheContext):
        return self.visitChildren(ctx)



del TileMapParser