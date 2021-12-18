import pygame
import random

from pygame.sprite import Sprite

class Green_wrench:
    def __init__(self, game):
        # зберігаємо екран в атрибут Green_wrench
        self.screen = game.screen
        # створюємо атрибут Settings
        self.settings = game.settings
        #  отримуємо атрибут екрана

        self.image = pygame.image.load('images/xp.png')
        self.rect = self.image.get_rect()

        #self.print_green_wrench = False

    def position_green_wrench(self):
        self.rect.center = (random.randint(1, self.settings.screen_width - self.rect.width),
                                  random.randint(1, self.settings.screen_hight - self.rect.height))

    def _print_green_wrench(self):
        self.screen.blit(self.image, self.rect)