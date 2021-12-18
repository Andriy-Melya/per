class Settings:
    """ Клас для збереження всіх налаштувань гри """

    def __init__(self):
        # налаштування екрану
        self.screen_width = 1600
        self.screen_hight = 900
        self.bg_color = (230, 230, 230)

        self.game_active = False
        self.print_green_wrench = False

        # налаштування корабля
        self.ship_speed = 1.5
        self.ship_kyt = 0.9
        self.number_hearts = 5
        self.max_hearts = 10

        # налаштування кулі
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bellet_color = (60, 60, 60)

        # налаштування астероїду
        self.asteroid_speed = 0.5
        self.asteroid_allower = 8

        self.bals = 0
        self.max = 100
