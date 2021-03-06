import time
import pygame
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard


from setting import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStatus

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    stats = GameStatus(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, "Go")
    life_rewards = Group()


    while True:
        gf.check_event(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.check_rewards(ship, life_rewards, stats)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, life_rewards)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, life_rewards)

run_game()
