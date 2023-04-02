import pygame
import random
from Constants import Constants
from Colours import Colours


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Colours.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (Constants.WIDTH / 2, Constants.HEIGHT / 2)
        
    def update(self):
        if self.rect.left > Constants.WIDTH:
            self.rect.right = 0