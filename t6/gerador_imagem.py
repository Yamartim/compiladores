from email.mime import image
from PIL import Image
from os import listdir
from random import randint

class GeradorImagem:
    def __init__(self, tam_tile:int, dimensoes:tuple[int, int]) -> None:
        self.tam_tile = tam_tile
        self.dimensoes = dimensoes

        self.tamanho_total = (dimensoes[0]*tam_tile, dimensoes[1]*tam_tile)

        self.imagem = Image.new("RGBA", self.tamanho_total, color=(255,255,255,255))

        self.dict_tiles = dict()
        self.dict_tiles['_'] = Image.new("RGBA", (self.tam_tile, self.tam_tile), color=(255,255,255,0))

        self.dict_estruturas = dict()

    def AddTile(self, nome_tile:str, path:str):
        nova_tile = Image.open(path).convert("RGBA").resize((self.tam_tile, self.tam_tile))
        self.dict_tiles[nome_tile] = nova_tile

    def AddEstrutura(self, nome:str, estrutura:list, dimensoes:tuple[int, int]):
        
        tamanho_est = (dimensoes[0]*self.tam_tile, dimensoes[1]*self.tam_tile)

        img_est = Image.new("RGBA", tamanho_est, color=(255,255,255,255))

        for i in range(0,dimensoes[0]):
            for j in range(0,dimensoes[1]):
                tile = self.dict_tiles[estrutura[i][j]]
                #print(tile, i, j)
                img_est.paste(tile, (j*self.tam_tile, i*self.tam_tile))

        self.dict_estruturas[nome] = img_est

        

    def PreencherImagem(self, nome_tile:str = '_'):
        for i in range(0, self.dimensoes[0]):
            for j in range(0, self.dimensoes[1]):
                self.PreencherPonto(nome_tile, (i, j))
    
    def PreencherRetangulo(self, nome_tile:str, ponto_init:tuple[int, int] = None, ponto_fim:tuple[int, int] = None, lado_x:int = None, lado_y:int = None):

        if ponto_init is None:
            print('não é possivel criar um retangulo sem um ponto')
            return
        
        desenho_pontos = ponto_fim is not None
        desenho_lados = lado_x is not None and lado_y is not None

        if not desenho_pontos and not desenho_lados:
            print('são precisos mais parametros para desenhar retangulo')
            return

        if desenho_pontos:

            menor_x, maior_x, menor_y, maior_y = self.RegularizarPontos(ponto_init, ponto_fim)
                

        elif desenho_lados:
            menor_x = ponto_init[0] - lado_x/2
            maior_x = ponto_init[0] + lado_x/2
            menor_y = ponto_init[1] - lado_y/2
            maior_y = ponto_init[1] + lado_y/2
        
        for i in range(menor_x, maior_x):
            for j in range(menor_y, maior_y):
                self.PreencherPonto(nome_tile, (i, j))

    
    def PreencherCirculo(self, nome_tile:str, centro:tuple[int, int] = None, raio:int = 0):

        if centro is None:
            print('não é possivel criar um circulo sem um ponto')
            return
        
        menor_x = centro[0] - raio
        maior_x = centro[0] + raio
        menor_y = centro[1] - raio
        maior_y = centro[1] + raio
        
        for i in range(menor_x, maior_x):
            for j in range(menor_y, maior_y):
                #print((i-centro[0])**2, (j-centro[1])**2, (raio ** 2))
                if ((i-centro[0]) ** 2) + ((j-centro[1]) ** 2) < (raio ** 2):
                    self.PreencherPonto(nome_tile, (i, j))

    def PreencherLinha(self, nome_tile:str, ponto_init:tuple[int, int], ponto_fim:tuple[int, int]):
        menor_x, maior_x, menor_y, maior_y = self.RegularizarPontos(ponto_init, ponto_fim)

        if not maior_x == menor_x:
            m = (maior_y - menor_y) / (maior_x - menor_x)

            for x in range(menor_x, maior_x+1):

                y = round(m*x)

                self.PreencherPonto(nome_tile, (x, y))
        
        else:
            x = menor_x
            for y in range(menor_y, maior_y+1):
                self.PreencherPonto(nome_tile, (x, y))


    def PreencherPonto(self, nome_tile:str, ponto:tuple[int, int]):
        self.imagem.paste(self.dict_tiles[nome_tile], (ponto[0]*self.tam_tile, ponto[1]*self.tam_tile))

    #preencher poligononlados

    def RegularizarPontos(self, ponto_init:tuple[int, int], ponto_fim:tuple[int, int]):
        if ponto_init[0] < ponto_fim[0]:
            menor_x = ponto_init[0]
            maior_x = ponto_fim[0]
        else:
            menor_x = ponto_fim[0]
            maior_x = ponto_init[0]

        if ponto_init[1] < ponto_fim[1]:
            menor_y = ponto_init[1]
            maior_y = ponto_fim[1]
        else:
            menor_y = ponto_fim[1]
            maior_y = ponto_init[1]

        return menor_x, maior_x, menor_y, maior_y
    
    def PreencherEstrutura(self, nome:str, ponto:tuple[int, int]):
        
        img_est = self.dict_estruturas[nome]
        self.imagem.paste(img_est, (ponto[0]*self.tam_tile, ponto[1]*self.tam_tile), img_est)

    def EspalharEstrutura(self, nome:str, ponto_init:tuple[int, int], ponto_fim:tuple[int, int], ocorrencia:int = 0):
        
        menor_x, maior_x, menor_y, maior_y = self.RegularizarPontos(ponto_init, ponto_fim)

        tam_estrut_x = int(self.dict_estruturas[nome].size[0]/self.tam_tile)
        tam_estrut_y = int(self.dict_estruturas[nome].size[1]/self.tam_tile)

        counter_rep = 0
        for i in range(menor_x+1, maior_x-tam_estrut_x-1, tam_estrut_x+1):
            for j in range(menor_y+1, maior_y-tam_estrut_y-1):
                #print(counter_rep)
                
                if counter_rep != 0:
                    counter_rep -= 1
                elif randint(0, ocorrencia) == 0:
                    self.PreencherEstrutura(nome, (i, j))
                    counter_rep = tam_estrut_y
                

    def MostrarImagem(self):
        self.imagem.show()

    def SalvarImagem(self, nome:str):
        if nome.endswith('.png'):
            self.imagem.save(nome)
        else:
            self.imagem.save(nome+'.png')

#pra testar
def main():
    dimensoes = (30, 30)
    tam_tile = 32

    gen = GeradorImagem(tam_tile, dimensoes)

    lst = ['assets/' + path for path in listdir('assets/')]
    #print(lst)

    for path in lst:
        gen.AddTile(path[7:-4], path)

    gen.PreencherImagem('agua')

    #gen.PreencherRetangulo('areia', (10, 10), (20, 20))
    gen.PreencherCirculo('areia', (15, 15), 5)

    gen.PreencherLinha('terra', (13, 13), (15, 15))

    arvoretiles = [
        ['_'     , 'folhas' , '_'],
        ['folhas', 'folhas' , 'folhas'],
        ['_'     , 'madeira', '_']]
    
    gen.AddEstrutura('arvore', arvoretiles, (3,3))
    #gen.PreencherEstrutura('arvore', (12, 12))
    #gen.PreencherEstrutura('arvore', (16, 16))
    gen.EspalharEstrutura('arvore', (10, 10), (20, 20), 1)

    gen.MostrarImagem()


if __name__ == '__main__':
    main()
