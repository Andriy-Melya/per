import pygame
import random
from pygame.sprite import Sprite


class Asteroid(Sprite):
    # клас що представляє одного прибульця
    def __init__(self, game, speed):
        super().__init__()
        self.screen = game.screen
        self.ship = game.ship
        self.settings = game.settings

        self.original_image = pygame.image.load('images/asteroid.png')
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.direction = pygame.math.Vector2((0, -1))
        self.position = self.rect.center
        self.speed = speed

    def placing(self):
        s = random.randint(1, 4)
        if s == 1:
            self.rect.x = 5
            self.rect.y = random.randint(0, self.settings.screen_hight - self.rect.height)
        elif s == 2:
            self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
            self.rect.y = 5
        elif s == 3:
            self.rect.x = self.settings.screen_width - self.rect.width
            self.rect.y = random.randint(0, self.settings.screen_hight - self.rect.height)
        elif s == 4:
            self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
            self.rect.y = self.settings.screen_hight - self.rect.height

        self.position = self.rect.center


    def point_at(self):
        self.direction = pygame.math.Vector2(random.randint(100, self.settings.screen_width-100), random.randint(100, self.settings.screen_hight-100)) - self.rect.center
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        angle = self.direction.angle_to((0, -1))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.position += self.direction  * self.speed
        #self.position -= pygame.math.Vector2(-self.direction.y, self.direction.x) * 0 * self.settings.asteroid_speed
        self.rect.center = round(self.position.x), round(self.position.y)

    def draw_asteroid(self):
        self.screen.blit(self.image, self.rect)


