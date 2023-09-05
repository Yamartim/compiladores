# Generated from TileMap.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TileMapParser import TileMapParser
else:
    from TileMapParser import TileMapParser

# This class defines a complete generic visitor for a parse tree produced by TileMapParser.

class TileMapVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TileMapParser#programa.
    def visitPrograma(self, ctx:TileMapParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declMapa.
    def visitDeclMapa(self, ctx:TileMapParser.DeclMapaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declaracoes.
    def visitDeclaracoes(self, ctx:TileMapParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#regioes.
    def visitRegioes(self, ctx:TileMapParser.RegioesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declRegiao.
    def visitDeclRegiao(self, ctx:TileMapParser.DeclRegiaoContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#tiles.
    def visitTiles(self, ctx:TileMapParser.TilesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declTile.
    def visitDeclTile(self, ctx:TileMapParser.DeclTileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#estruturas.
    def visitEstruturas(self, ctx:TileMapParser.EstruturasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declEstrutura.
    def visitDeclEstrutura(self, ctx:TileMapParser.DeclEstruturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#unidadeSerie.
    def visitUnidadeSerie(self, ctx:TileMapParser.UnidadeSerieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#serieTiles.
    def visitSerieTiles(self, ctx:TileMapParser.SerieTilesContext):
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


    # Visit a parse tree produced by TileMapParser#comandos.
    def visitComandos(self, ctx:TileMapParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#cmdDesenhe.
    def visitCmdDesenhe(self, ctx:TileMapParser.CmdDesenheContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#cmdEspalharEstruturas.
    def visitCmdEspalharEstruturas(self, ctx:TileMapParser.CmdEspalharEstruturasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#cmdMostrarDesenho.
    def visitCmdMostrarDesenho(self, ctx:TileMapParser.CmdMostrarDesenhoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#cmdSalvarDesenho.
    def visitCmdSalvarDesenho(self, ctx:TileMapParser.CmdSalvarDesenhoContext):
        return self.visitChildren(ctx)



del TileMapParser