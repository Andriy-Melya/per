import pygame
from pygame.sprite import Sprite
from ship import Ship
from settings import Settings

class Bullet(Sprite):
    """ Клас для керування кулями """

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.ship = game.ship

        # СТВОРЕННЯ ОБЄКТІВ bullet

        self.original_bullet = pygame.image.load('images/laz.png')
        self.bullet = self.original_bullet
        self.rect = self.bullet.get_rect()
        self.rect.center = self.ship.rect.center

        self.direction = self.ship.direction
        self.position = self.rect.center
        self.kyt = self.ship.kyt

        # поворот кулі в напрямку корабля
        self.bullet = pygame.transform.rotate(self.original_bullet, self.kyt)
        self.rect = self.bullet.get_rect(center=self.rect.center)

    def update(self):
        # рух кулі в напрямку корабля
        self.position += self.direction * (-1) * self.settings.bullet_speed
        self.position -= pygame.math.Vector2(-self.direction.y, self.direction.x) * 0 * self.settings.bullet_speed
        self.rect.center = round(self.position.x), round(self.position.y)

    def draw_bullet(self):
        # вивід пулі на екран
        self.screen.blit(self.bullet, self.rect)