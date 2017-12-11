import pygame
from pygame.sprite import  Sprite
import random

class LifeReward(Sprite):
    def __init__(self, ai_setting, screen):
        super(LifeReward, self).__init__()

        self.screen = screen
        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = 500
            #random.randint(0, ai_setting.screen_width)
        self.rect.y = 0
        self.speed = 1
        print(self.rect)


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def moving(self):
        self.rect.y += self.speed
