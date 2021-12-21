import random
import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from asteroid import Asteroid
from large_asteroid import Large_asteroid
from button import Button
from green_wrench import Green_wrench


class Program:
    """ Загальний клас який керує ресурсами та поведінеою гри """

    def __init__(self):
        # ініціалізувати гру та створити ресурси гри
        pygame.init()
        pygame.font.init()

        # створюємо екземпляр Settings та присвоюємо йому атрибуту self.settings
        self.settings = Settings()

        # створюємо вікно
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Program')



        self.f = pygame.font.Font(None,100)

        self.ship = Ship(self)
        self.green_wrench = Green_wrench(self)
        self.play_button = Button(self, 'Play')
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.large_asteroids = pygame.sprite.Group()




    def run_game(self):
        """ головний цикл гри """
        while True:
            self._check_events()

            if self.settings.game_active:
                self.ship.point_at()
                self.time()
                self.ship.update()
                self._update_bullets()
                self._update_asteroid()
                if self.settings.print_green_wrench:
                    self._update_green_wrench()
            self._update_screen()


    def _check_events(self):
        """ реагування на натискання клавіш та подій миші """
        # слідкування за подіями миші та клавіатури
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        # реагування на  натиснення клавіш
        if event.key == pygame.K_UP:
            self.ship.moving = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_LEFT:
            self.ship.turn_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.turn_right = True


    def _check_keyup_events(self, event):
        # реагування на відпускання клавіш
        if event.key == pygame.K_UP:
            self.ship.moving = False
        if event.key == pygame.K_RIGHT:
            self.ship.turn_right = False
        if event.key == pygame.K_LEFT:
            self.ship.turn_left = False

    def time(self):
        t = pygame.time.get_ticks()
        if len(self.asteroids) < self.settings.asteroid_allower and t % 100 == 0:
            self._create_asteroid()
        if t % 10000 == 0 and self.settings.print_green_wrench == False:
            self.green_wrench.position_green_wrench()
            self.settings.print_green_wrench = True


    def _print_bals(self):
        # вивід очок
        text = self.f.render(str(self.settings.bals),True,(0, 0, 0))
        self.screen.blit(text, (15, 15))

    def _check_play_button(self, mouse_pos):
        # почати гру при натисненні кнопки
        if self.play_button.rect.collidepoint(mouse_pos):
            self.settings.game_active = True

    def _create_asteroid(self):
        k = random.randint(1, 5)
        if k != 5:
            asteroid = Asteroid(self)
            # задання його позиції та повороту
            asteroid.placing()
            asteroid.point_at()
            self.asteroids.add(asteroid)
        else:
            asteroid = Large_asteroid(self)
            # задання його позиції та повороту
            asteroid.placing()
            asteroid.point_at()
            self.large_asteroids.add(asteroid)

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """ оновити зображення на екрані """
        # наново намалювати екран мна кожній ітерації циклу
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
        if self.ship.moving or self.ship.turn_left or self.ship.turn_right:
            self.ship.blitm_fire()

        self.ship.draw_heart()

        self._print_bals()

        if self.settings.print_green_wrench:
            self.green_wrench._print_green_wrench()

        if not self.settings.game_active:
            self.play_button.draw_button()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for asteroid in self.asteroids.sprites():
            asteroid.draw_asteroid()

        for asteroid in self.large_asteroids.sprites():
            asteroid.draw_asteroid()


        # показ останнього намалбованого екрану
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets:
            if not(bullet.rect.x > 0 and bullet.rect.x < self.settings.screen_width) \
                    or not(bullet.rect.y > 0 and bullet.rect.y < self.settings.screen_hight):
                self.bullets.remove(bullet)

        hit = pygame.sprite.groupcollide(self.asteroids, self.bullets, True, True)
        self.settings.bals += len(hit)

        hit = pygame.sprite.groupcollide(self.large_asteroids, self.bullets, False, True)
        for i in hit:
            if i.xp == 1:
                self.large_asteroids.remove(i)
                self.settings.bals += 2
            elif i.xp == 2:
                i.xp -= 1
                i.original_image = i.damaged_asteroid
                i.image = i.damaged_asteroid
                i.turn()


    def _update_asteroid(self):
        self.asteroids.update()
        self.large_asteroids.update()


        for asteroid in self.asteroids:
            if not(asteroid.rect.centerx > 0 and asteroid.rect.centerx < self.settings.screen_width) \
                    or not(asteroid.rect.centery > 0 and asteroid.rect.centery < self.settings.screen_hight):
                self.asteroids.remove(asteroid)

        # видалення астероїдів які вийшли за межі гри
        for asteroid in self.large_asteroids:
            if not(asteroid.rect.centerx > 0 and asteroid.rect.centerx < self.settings.screen_width) \
                    or not(asteroid.rect.centery > 0 and asteroid.rect.centery < self.settings.screen_hight):
                self.large_asteroids.remove(asteroid)

        # зіткнення великих астероїдів з кораблем
        for asteroid in self.large_asteroids.sprites():
            if pygame.sprite.collide_mask(self.ship, asteroid):
                self.large_asteroids.remove(asteroid)
                if asteroid.xp ==1:
                    self.settings.ship_hearts -= 1
                    # пауза
                    sleep(0.08)
                else:
                    self.ship.ship_hearts -= 2
                    # пауза
                    sleep(0.08)

        # зіткнення астероїдів з кораблем
        for asteroid in self.asteroids.sprites():
            if pygame.sprite.collide_mask(self.ship, asteroid):
                # пауза
                sleep(0.08)
                self.asteroids.remove(asteroid)
                self.ship.ship_hearts -= 1

    def _update_green_wrench(self):
        if pygame.sprite.collide_mask(self.ship, self.green_wrench):
            self.settings.print_green_wrench = False
            if self.settings.max_hearts >= self.ship.ship_hearts:
                self.ship.ship_hearts += 1


if __name__ == '__main__':

    pr = Program()
    pr.run_game()