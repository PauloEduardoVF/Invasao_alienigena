import pygame

class Espaconave:
    '''Classe para cuidar da espaçonave'''

    def __init__(self, ai_jogo):
        '''Inicializa a espaconave e define sua posição inicial'''
        self.tela = ai_jogo.tela
        self.tela_react = ai_jogo.tela.get_rect()

        #Sobre a imagem da espaçonave e obter seu rect = retângulo
        self.imagem = pygame.image.load('imagens/ship.bmp')
        self.retangulo = self.imagem.get_rect()

        #Começa cada espaçonave nova no centro inferior da tela
        self.retangulo.midbottom = self.tela_react.midbottom

        #Flag de movimento: começa com uma espacinave que não está se movento
        self.mover_direita = False

    def atualizar(self):
        '''Atualiza a pasição da espacionave que não esta se movendo'''
        if self.mover_direita:
            self.retangulo.x += 1

    def me_carregue(self):
        '''Desenha uma espaçonave em sua localização atual'''
        self.tela.blit(self.imagem, self.retangulo)
    