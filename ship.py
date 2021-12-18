import random

import pygame
import sys
import math
class Ship:
    """ Клас для керування кораблем """

    def __init__(self, game):
        # ініціалізовуємо корабель та задаємо його початкову позицію

        # зберігаємо екран в атрибут Ship
        self.screen = game.screen
        # створюємо атрибут Settings
        self.settings = game.settings
        #  отримуємо атрибут екрана
        self.screen_rect = game.screen.get_rect()

        # завантажуємо зображення корабля та задаємо його початкову позицію

        self.image_image = pygame.image.load('images/ship.png')
        self.original_image = self.image_image
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.image_fire = pygame.image.load('images/fire.py')
        self.rect_fire = self.image_fire.get_rect()

        self.ship_hearts = self.settings.number_hearts

        # створюємо кожен новий корабель внизу екрана, по центру
        self.rect.center= self.screen_rect.center

        # зберегти десяткове значення ддля позиції
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.kyt = 0

        self.direction = pygame.math.Vector2((0, -1))
        self.position = pygame.math.Vector2(self.rect.center)

        self.direction_fire = self.direction
        self.position_fire = self.position

        self.heart = pygame.image.load('images/heart.png')
        self.rect_heart = self.heart.get_rect()


        # індикатор руху
        self.moving = False
        self.turn_left = False
        self.turn_right = False

    def point_at(self):
        # визначаємо кординати будь-якої точни на прямій
        xx = 1000000 * math.cos(-(self.kyt-90) * math.pi / 180)
        yy = 1000000 * math.sin(-(self.kyt-90) * math.pi / 180)

        # знаходимо вектор повороту
        self.direction = pygame.math.Vector2(xx, yy) - self.rect.center
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        # визначаємо кут при повороті ліворуч
        if self.turn_left:
            self.kyt += self.settings.ship_kyt
        # визначаємо кут при повороті ліворуч
        if self.turn_right:
            self.kyt -= self.settings.ship_kyt

        if self.turn_right or self.turn_left:
            # повертаємо корабень під кутом
            self.image = pygame.transform.rotate(self.original_image, self.kyt)
            self.rect = self.image.get_rect(center=self.rect.center)



    def move(self, x, y):
        # рух корабля у визначеному напрямку
        self.position += self.direction * y * self.settings.ship_speed
        self.position -= pygame.math.Vector2(-self.direction.y, self.direction.x) * x * self.settings.ship_speed
        self.rect.center = round(self.position.x), round(self.position.y)


    def update(self):
        """ оновити поточну позицію корабля """
        if self.moving:
            keys = pygame.key.get_pressed()
            self.move(0, - keys[pygame.K_UP])
            self.rect_fire = self.rect
            self.direction_fire = self.direction


    def draw_heart(self):
        if self.ship_hearts < 1:
            sys.exit()
        # виводимо всі серця корабля
        for i in range(self.ship_hearts):
            self.screen.blit(self.heart, (self.settings.screen_width - 10 - ((i + 1) * self.rect_heart.width),5))


    def blitme(self):
        # намалювати корабель у його початковуому розташування
        self.screen.blit(self.image, self.rect)
        if self.moving:
            self.screen.blit(self.image_fire,self.image_fire)