import pygame

class Button:

    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # властивості і розміри кнопки
        self.width, self.height = 400, 100
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 56)

        # створення обєкту rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # перетворюємо текст на зображення та розміщуємо його
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

