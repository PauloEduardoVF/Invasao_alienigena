class Settings:
    '''Uma classe para armazenar todas as configurações do jogo.'''

    def __init__(self):
        '''Inicializa as configurações do jogo.'''
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuração da velocidade da nave
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Configurações do projétil
        self.bullet_speed = 3.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 50

        #Configuração do Alienígena
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20

        #fleet_direction de 1 representa a direita: -1 representa a esquerda
        self.fleet_direction = 1

