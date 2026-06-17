import sys
import pygame
from configuracoes import Configuracoes
from espaconave import Espaconave

class InvasaoAlienigena:
    '''Classe geral para gerenciar ativos e comportamento do jogo'''
    def __init__(self):
        '''Inicializa o jogo e cria recurssos do jogo'''
        pygame.init()
        self.configuracoes = Configuracoes()

        self.relogio = pygame.time.Clock()
        self.tela = pygame.display.set_mode((self.configuracoes.largura_tela,
                                             self.configuracoes.altura_tela,
                                             ))
        pygame.display.set_caption("Invasão Agienigena!")
        self.espaconave = Espaconave(self)

        #Define a dor do Fundo.
        self.bg_cor = (self.configuracoes.bg_cor)

    def executar_jogo(self):
        '''Inicia o loop principal do jogo'''
        while True:
            self._verificar_evento()
            self._atualizar_eventos()
            self.relogio.tick(60)

    def _verificar_evento(self):
        '''Responde as teclas pressionadas e a eventos de mouse'''
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()

    def _atualizar_eventos(self):
            self.tela.fill(self.bg_cor)
            self.espaconave.me_carregue()
            #Deixa a tela desenhada mais recente visivel.
            pygame.display.flip()
           

if __name__ == '__main__':
    #cria uma instância do jogo e executa o jogo.
    ai = InvasaoAlienigena()
    ai.executar_jogo()


