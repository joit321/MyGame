import os
import pygame
from Sprites.GravitySprite import GravitySprite
from Colours import Colours
from Constants import Constants
from Utils import Utils

class Player(GravitySprite):
    def __init__(self):
        GravitySprite.__init__(self)       
        self.image = Utils.LoadImage("js.png", 100, 100)
        self.rect = self.image.get_rect()
        self.rect.center = (Constants.WIDTH / 2, Constants.HEIGHT / 2)

        #Собственное:
        self.jumpHeight = 200

    def update(self):
        Utils.ApplyGravity(self)

        if self.jumpHeight >= self.rect.y and self.isMovingUp:
            self.isMovingUp = False
            self.speedy = 0
        if self.isMovingUp:
            self.rect.y += self.speedy
            self.speedy -= 4 # на какую скорость прыжок ускоряется
                    
         # Применяем падение
        if Utils.IsOnSurface(self) == True:
            self.isOnJump = False
            

        # Применяем управление
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 8
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 8
        if keystate[pygame.K_UP] and not self.isOnJump:
            self.speedy = -1
            self.jumpHeight = self.rect.y - 200
            self.isMovingUp = True
            self.isOnJump = True
        
        if self.rect.right > Constants.WIDTH:
             self.rect.right = Constants.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0