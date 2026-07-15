class Settings:
    '''Uma classe para armazenar todas as configurações do jogo.'''

    def __init__(self):
        '''Inicializa as configurações do jogo.'''
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuração da velocidade da nave
        self.ship_limit = 3

        # Configurações do projétil  
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 50

        #Configuração do Alienígena
        self.fleet_drop_speed = 10

        #Rapidez com que ojogo acelara
        self.speedup_scale = 1.1

        self.initialize_dynsmic_settings()

    def initialize_dynsmic_settings(self):
        '''Inicializa as configurações que mudam ao logo do jogo'''
        self.ship_speed = 3.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        #fleet_direction de 1 representa a direita: -1 representa a esquerda
        self.fleet_direction = 1
    
    def increase_speed(self):
        '''Aumenta as configurações de velocidade'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


