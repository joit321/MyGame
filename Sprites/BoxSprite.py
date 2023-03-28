import pygame
from Constants import Constants
from Utils import Utils

class BoxSprite(pygame.sprite.Sprite):
    def __init__(self, x : int, y : int, size : int):
        pygame.sprite.Sprite.__init__(self)        
        self.image = Utils.LoadImage("anonymous.png", size , size)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
       
           
     