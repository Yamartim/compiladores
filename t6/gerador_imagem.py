from email.mime import image
from PIL import Image
from os import listdir


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
                self.imagem.paste(self.dict_tiles[nome_tile], (i*self.tam_tile,j*self.tam_tile))
    
    def PreencherRetangulo(self, nome_tile:str, ponto_init:tuple[int, int], ponto_fim:tuple[int, int]):

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
            
        for i in range(menor_x, maior_x):
            for j in range(menor_y, maior_y):
                self.imagem.paste(self.dict_tiles[nome_tile], (i*self.tam_tile,j*self.tam_tile))

    #preencher linha
    #preencher circulo
    #preencher poligononlados

    def PreencherEstrutura(self, nome:str, ponto:tuple[int, int]):
        
        img_est = self.dict_estruturas[nome]
        self.imagem.paste(img_est, (ponto[0]*self.tam_tile, ponto[1]*self.tam_tile), img_est)


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

    gen.PreencherRetangulo('areia', (10, 10), (20, 20))

    arvoretiles = [
        ['_'     , 'folhas' , '_'],
        ['folhas', 'folhas' , 'folhas'],
        ['_'     , 'madeira', '_']]
    
    gen.AddEstrutura('arvore', arvoretiles, (3,3))
    gen.PreencherEstrutura('arvore', (12, 12))
    gen.PreencherEstrutura('arvore', (16, 16))

    gen.MostrarImagem()


if __name__ == '__main__':
    main()
