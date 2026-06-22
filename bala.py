import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    '''Classe para gerenciar os projéteis disparado da espaçonave'''
    def __init__(self, ai_jogo):
        super().__init__()
        '''Cria um objeto Bala na posição atual da espaçonave'''
        self.tela = ai_jogo.tela
        self.configuracoes = ai_jogo.configuracoes
        self.cor = self.configuracoes.bala_cor
        
        #cria uma bala em rect (0, 0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, self.configuracoes.bala_largura,
                                self.configuracoes.bala_altura)
        self.rect.midtop = ai_jogo.espaconave.retangulo.midtop

        #Armazena a posição do projétil como um float
        self.y = float(self.rect.y)

    def update(self):
        '''Desloca o projétil verticalmente'''
        #Atualiza a posição exata do projétil
        self.y -= self.configuracoes.bala_velocidade
        #Atualiza a posição do react
        self.rect.y = self.y

    def desenhar_bala(self):
        '''Desenha o projétil na tela'''
        pygame.draw.rect(self.tela, self.cor, self.rect)