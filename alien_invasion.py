import time
import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.set_caption('Alien Invasion')

    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)


run_game()
