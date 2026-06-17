import sys
import pygame
from configurações import cofiguracoes

class InvasaoAlienigena:
    '''Classe geral para gerenciar ativos e comportamento do jogo'''
    def __init__(self):
        '''Inicializa o jogo e cria recurssos do jogo'''
        pygame.init()
        self.configuracoes = cofiguracoes()

        self.relogio = pygame.time.Clock()
        self.tela = pygame.display.set_mode((self.configuracoes.largura_tela,
                                             self.configuracoes.autura_dela,
                                             ))
        pygame.display.set_caption("Invasão Agienigena!")

        #Define a dor do Fundo.
        self.bg_cor = (self.configuracoes.bg_cor)

    def executar_jogo(self):
        '''Inicia o loop principal do jogo'''
        while True:
            #Observa eventos de teclado e mouse.
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
            #Redesenha a tela durante casa passagem pelo loop.
            self.tela.fill(self.bg_cor)

            #Deixa a tela desenhada mais recente visivel.
            pygame.display.flip()
            self.relogio.tick(60)

if __name__ == '__main__':
    #cria uma instância do jogo e executa o jogo.
    ai = InvasaoAlienigena()
    ai.executar_jogo()


