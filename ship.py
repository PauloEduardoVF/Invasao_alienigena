import pygame

class Ship:
    '''Uma classe que cuida da espaçonave'''

    def __init__(self, ai_game):
        '''Inicializa a espaçonave e define sua posição inicial'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Carrega a imagem da espaçonave e obtém seu retângulo
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um float para a posição horizontal exata da espaçonave
        self.x = float(self.rect.x)

        # Flag de movimento: começa com uma espaçonave que não está se movendo
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Atualiza a posição da espaçonave com base nas flags de movimento'''
        # Move para a direita se a flag for True e a borda da nave estiver dentro da tela
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        # Move para a esquerda se a flag for True e a borda da nave for maior que 0
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Atualiza o objeto rect a partir de self.x 
        self.rect.x = self.x

    def blitme(self):
        '''Desenha a espaçonave em sua localização atual'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Centraliza a espaçonave na tela'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)