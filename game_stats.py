import pygame

class GameStats:
    ''' Відстеження статистики гри '''

    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_health = self.settings.number_heart