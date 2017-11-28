import time
import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    pygame.display.set_caption('Alien Invasion')

    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
