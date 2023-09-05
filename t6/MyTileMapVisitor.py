# Generated from TileMap.g4 by ANTLR 4.13.0
from itertools import count
from mimetypes import init
import token
from antlr4 import *
if "." in __name__:
    from .TileMapParser import TileMapParser
else:
    from TileMapParser import TileMapParser

from gerador_imagem import GeradorImagem
from TabelaDeSimbolos import TabelaDeSimbolos
from listaErros import listaErros

from os.path import join, normpath

# This class defines a complete generic visitor for a parse tree produced by TileMapParser.

class TileMapVisitor(ParseTreeVisitor):

    def verificarIdent(self, ctx, multiplos:bool, ja_existe:bool, inicio = 0, fim = -1, tipo = None):
        #modo determina qual comparação será feita,
        #há momentos que precisamos que não existem identificadores
        #e há momentos que precisamos que todos os identificadores existam
        #modo True adiciona erro se existir algum identificador com o mesmo nome
        #modo False adiciona erro se não existir algum identificador com aquele nome
        
        flag = True
        if ja_existe:
            string = ' já existe'
        else:
            string = ' não existe'

        if multiplos:
            i = inicio
            while ctx.Identificador(i) != None and i != fim:
                ident = ctx.Identificador(i).getText()
                existe = self.tabela.existe(ident)
                if (existe and ja_existe) or (not existe and not ja_existe): #porta XNOR ou equivalencia para controle da verificacao
                    #print(i)
                    self.erros.adicionarErro(ctx.start, 'identificador ' + ident + string)
                    flag = False
                elif tipo != None and self.tabela.verificar(ident) != None:
                    temp = self.tabela.verificar(ident)
                    if temp[0] != tipo:
                        self.erros.adicionarErro(ctx.start, 'identificador ' + ident + ' nao é do tipo ' + tipo)
                i += 1
        else:
            ident = ctx.Identificador().getText()
            existe = self.tabela.existe(ident)
            if (existe and ja_existe) or (not existe and not ja_existe):
                self.erros.adicionarErro(ctx.start, 'identificador ' + ident + string)
                flag = False
            elif tipo != None and self.tabela.verificar(ident) != None:
                temp = self.tabela.verificar(ident)
                if temp[0] != tipo:
                    self.erros.adicionarErro(ctx.start, 'identificador ' + temp[0] + 'nao eh do tipo ' + tipo)

        return flag


    # Visit a parse tree produced by TileMapParser#programa.
    def visitPrograma(self, ctx:TileMapParser.ProgramaContext, parser, lista_erros: listaErros, path_fonte, output):

        self.tabela = TabelaDeSimbolos()

        self.parser = parser
        self.erros = lista_erros

        self.source = path_fonte
        self.output = output

        return self.visitChildren(ctx)
    

    # Visit a parse tree produced by TileMapParser#declMapa.
    def visitDeclMapa(self, ctx:TileMapParser.DeclMapaContext):
        ident = ctx.Identificador().getText()

        #print('DECLAREI UM MAPAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

        #self.arquivo = open(ident, 'w')

        #estabelecer algumas regras para inserção,
        #inserir o identificador como key,
        #inserir uma lista com o primeiro elemento como o tipo do identificador
        #inserção livre para a segunda posição em diante
            
        tam_tiles = int(ctx.Num_Inteiro(0).getText())
        dimensao = (int(ctx.Num_Inteiro(1).getText()), int(ctx.Num_Inteiro(2).getText()))

        self.tabela.inserir(ident, ['mapa'])

        self.geradorimg = GeradorImagem(tam_tiles, dimensao)


        return self.visitChildren(ctx)

    # Visit a parse tree produced by TileMapParser#declRegiao.
    def visitDeclRegiao(self, ctx:TileMapParser.DeclRegiaoContext):

        
        if self.verificarIdent(ctx, True, True, 0, 1, None) and self.verificarIdent(ctx, True, False, 1, 2, 'bioma') and self.verificarIdent(ctx, True, False, 2, -1, 'area'):

            dados_regiao = ['regiao', ctx.Identificador(1).getText(), ctx.Identificador(2).getText()]


            self.tabela.inserir(ctx.Identificador(0).getText(), dados_regiao)

            print(ctx.Identificador(0).getText(), dados_regiao)


        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#declBioma.
    def visitDeclBioma(self, ctx:TileMapParser.DeclBiomaContext):

        if self.verificarIdent(ctx, True, True, 0, 1, None) and self.verificarIdent(ctx, True, False, 1, -1, None):

            dados_bioma = ['bioma', ctx.Identificador(1).getText()]
            
            self.tabela.inserir(ctx.Identificador(0).getText(), dados_bioma)

            print(ctx.Identificador(0).getText(), dados_bioma)
        
        return self.visitChildren(ctx)



    # Visit a parse tree produced by TileMapParser#areas.
    def visitAreas(self, ctx:TileMapParser.AreasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TileMapParser#declArea.
    def visitDeclArea(self, ctx:TileMapParser.DeclAreaContext):

        if self.verificarIdent(ctx, False, True, 0, -1, None):

            dados_area = ['area']
            tipoarea : TileMapParser.TipoAreaContext = ctx.tipoArea()
            if ctx.tipoArea().retang() is not None:
                retang = tipoarea.retang()
                if tipoarea.retang().Num_Inteiro(0) is None:
                    dados_area.append('retang1')
                    dados_area.append(pontonode2int(retang.ponto(0)))
                    dados_area.append(pontonode2int(retang.ponto(1)))
                else:
                    dados_area.append('retang2')
                    dados_area.append(pontonode2int(retang.ponto()))
                    dados_area.append(intnode2int(retang.Num_Inteiro(0)))
                    dados_area.append(intnode2int(retang.Num_Inteiro(1)))
            if ctx.tipoArea().ponto() is not None:
                dados_area.append('ponto')
                dados_area.append((pontonode2int(ctx.tipoArea().ponto().Num_Inteiro(0)),ctx.tipoArea().ponto().Num_Inteiro(1)))
            if ctx.tipoArea().linha() is not None:
                linha = tipoarea.linha()
                dados_area.append('linha')
                dados_area.append(pontonode2int(linha.ponto(0)))
                dados_area.append(pontonode2int(linha.ponto(1)))
                
            if ctx.tipoArea().circulo() is not None:
                circulo = tipoarea.circulo()
                dados_area.append('circulo')
                dados_area.append(pontonode2int(circulo.ponto()))
                dados_area.append(intnode2int(circulo.Num_Inteiro()))
                
            if ctx.tipoArea().polign() is not None:
                raise ("POLIGONO NAO IMPLEMENTADO")

            #print(ctx.Identificador(), dados_area)

            self.tabela.inserir(ctx.Identificador().getText(), dados_area)


        return self.visitChildren(ctx)

    # Visit a parse tree produced by TileMapParser#declTile.
    def visitDeclTile(self, ctx:TileMapParser.DeclTileContext):
        
        if self.verificarIdent(ctx, False, True, 0, -1, None):
            self.tabela.inserir(ctx.Identificador().getText(), ['tile', ctx.CADEIA().getText()])

            #caminho a tile relativo ao visitor
            path = normpath(join(self.source, ctx.CADEIA().getText().strip("'")))
            self.geradorimg.AddTile(ctx.Identificador().getText(), path)
            #print(type(ctx.Identificador()), path)

        return self.visitChildren(ctx)



    # Visit a parse tree produced by TileMapParser#declEstrutura.
    def visitDeclEstrutura(self, ctx:TileMapParser.DeclEstruturaContext):

        if self.verificarIdent(ctx, False, True, 0, -1, None):

            #print(ctx.Identificador())

            lista_estrutura = [] #lista de listas que representa matriz de tiles pra estrutura
            count_x, count_y = 0, 0 #contagens das dimensoes da matriz

            itter_y = 0
            for serie in ctx.serieTiles():
                itter_y += 1
                if itter_y > count_y:
                    count_y = itter_y

                itter_x = 0
                lista_aux = []
                for tipotile in serie.unidadeSerie():
                    itter_x += 1
                    if itter_x > count_x:
                        count_x = itter_x
                    
                    if tipotile.Nada() is None:
                        lista_aux.append(tipotile.Identificador().getText())
                    else:
                        lista_aux.append('_')
                lista_estrutura.append(lista_aux)
            #print(lista_estrutura, count_y, count_x)

            self.geradorimg.AddEstrutura(ctx.Identificador().getText(), lista_estrutura, (count_x, count_y))
            self.tabela.inserir(ctx.Identificador().getText(), ['estrutura', lista_estrutura])

        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#serieTiles.
    def visitSerieTiles(self, ctx:TileMapParser.SerieTilesContext):


        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#unidadeSerie.
    def visitUnidadeSerie(self, ctx:TileMapParser.UnidadeSerieContext):

        if ctx.Nada() is None:
            self.verificarIdent(ctx, False, False, 0,0)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by TileMapParser#declaracoes.
    def visitDeclaracoes(self, ctx:TileMapParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#biomas.
    def visitBiomas(self, ctx:TileMapParser.BiomasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TileMapParser#tiles.
    def visitTiles(self, ctx:TileMapParser.TilesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#regioes.
    def visitRegioes(self, ctx:TileMapParser.RegioesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#estruturas.
    def visitEstruturas(self, ctx:TileMapParser.EstruturasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#tipoArea.
    def visitTipoArea(self, ctx:TileMapParser.TipoAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#ponto.
    def visitPonto(self, ctx:TileMapParser.PontoContext):
        return ctx.Num_Inteiro(0),ctx.Num_Inteiro(1)


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
        return ctx.ponto(), ctx.Num_Inteiro()


    # Visit a parse tree produced by TileMapParser#comandos.
    def visitComandos(self, ctx:TileMapParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#cmdDesenhe.
    def visitCmdDesenhe(self, ctx:TileMapParser.CmdDesenheContext):

        ident = ctx.Identificador().getText()
        valores = self.tabela.verificar(ident)

        #print(ident)
        #print(valores)

        if self.verificarIdent(ctx, multiplos=False, ja_existe=False, inicio=0, fim=1, tipo='regiao'):

            bioma = self.tabela.verificar(valores[1])
            area = self.tabela.verificar(valores[2])
            #print(bioma)
            #print(area)

            if area[1] == 'retang1':
                self.geradorimg.PreencherRetangulo(bioma[1], area[2], area[3])
            elif area[1] == 'retang2':
                self.geradorimg.PreencherRetangulo(bioma[1], area[2], area[3], area[4])
            elif area[1] == 'circulo':
                self.geradorimg.PreencherCirculo(bioma[1], area[2], area[3])
            elif area[1] == 'ponto':
                self.geradorimg.PreencherPonto(bioma[1], area[2])
            elif area[1] == 'linha':
                self.geradorimg.PreencherLinha(bioma[1], area[2], area[3])

        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#cmdEspalharEstruturas.
    def visitCmdEspalharEstruturas(self, ctx:TileMapParser.CmdEspalharEstruturasContext):

        if self.verificarIdent(ctx, multiplos=True, ja_existe=False, inicio=0, fim=1, tipo='estrutura') and self.verificarIdent(ctx, multiplos=True, ja_existe=False, inicio=1, fim=2, tipo='regiao'):
            
            estr_a_espalhar = ctx.Identificador(0).getText()
            ident = ctx.Identificador(1).getText()
            valores = self.tabela.verificar(ident)

            bioma = self.tabela.verificar(valores[1])
            area = self.tabela.verificar(valores[2])

            if area[1] == 'retang1':
                self.geradorimg.EspalharEstrutura(estr_a_espalhar, area[2], area[3])
            else:
                raise("ESTRUTURAS NAO IMPLEMENTADAS PARA ESSE TIPO DE AREA")





        return self.visitChildren(ctx)

    # Visit a parse tree produced by TileMapParser#cmdMostrarDesenho.
    def visitCmdMostrarDesenho(self, ctx:TileMapParser.CmdMostrarDesenhoContext):

        self.geradorimg.MostrarImagem()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#cmdSalvarDesenho.
    def visitCmdSalvarDesenho(self, ctx:TileMapParser.CmdSalvarDesenhoContext):

        self.geradorimg.SalvarImagem(self.output)

        self.erros.printarErros()

        return self.visitChildren(ctx)

def pontonode2int(node):
    x = int(node.Num_Inteiro(0).getText())
    y = int(node.Num_Inteiro(1).getText())
    return x, y

def intnode2int(node):
    return int(node.getText())

del TileMapParser