import json
from pathlib import Path

class GameStats:
    '''Rastreia as estatísticas de Invasão Alienígina'''
    def __init__(self,ai_game):
        '''Inicia as estatísticas'''
        self.settings = ai_game.settings
        self.reset_stats()
        #A pontuação máxima nunca deve ser redefinida
        self.high_score = 0
        self.level = 1

        #A pontuação máxima não deve ser zerada, então buscamos o arquivo
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        '''Lê o recorde do arquivo JSON, se ele existir'''
        path = Path('high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            #Se o arquivo não existir, o recorde é o
            return 0

    def reset_stats(self):
        '''Inicializa as estatísticas que podem mudar durante o jogo'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
    
