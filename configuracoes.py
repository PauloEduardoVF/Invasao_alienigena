class Configuracoes:
    def __init__(self):
        '''Inicia as cofigurações do jogo'''
        #Configurações da tela
        self.largura_tela = 1200
        self.altura_tela = 800
        self.bg_cor = (230, 230, 230)

         #Configuração da velocidade da nave.
        self.nave_velocidade = 1.5

        #Configurações do projétil
        self.bala_velocidade = 2.0
        self.bala_largura = 3
        self.bala_altura = 15
        self.bala_cor = (60, 60, 60)