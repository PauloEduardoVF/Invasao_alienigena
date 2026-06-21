import pygame

class Espaconave:
    '''Classe para cuidar da espaçonave'''

    def __init__(self, ai_jogo):
        '''Inicializa a espaconave e define sua posição inicial'''
        self.tela = ai_jogo.tela
        self.tela_react = ai_jogo.tela.get_rect()
        self.configuracoes = ai_jogo.configuracoes

        #Sobre a imagem da espaçonave e obter seu rect = retângulo
        self.imagem = pygame.image.load('imagens/ship.bmp')
        self.retangulo = self.imagem.get_rect()

        #Começa cada espaçonave nova no centro inferior da tela
        self.retangulo.midbottom = self.tela_react.midbottom

        #armasena um floot para a posição horizontal exata da espaçonave
        self.x = float(self.retangulo.x)

        #Flag de movimento: começa com uma espaçonave que não está se movento
        self.mover_direita = False
        self.mover_esquerda = False

    def atualizar(self):
        '''Atualiza a posição da espacionave que não esta se movendo'''
        #atualiza o valor x da espaçonave, não o rect
        if self.mover_direita and self.retangulo.right < self.tela_react.right:
            self.x += self.configuracoes.nave_velocidade
        if self.mover_esquerda and self.retangulo.left > 0:
            self.x -= self.configuracoes.nave_velocidade

        #Atualiza o objeto retangulo de self.x 
        self.retangulo.x = self.x

    def me_carregue(self):
        '''Desenha uma espaçonave em sua localização atual'''
        self.tela.blit(self.imagem, self.retangulo)
    