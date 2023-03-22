import os
import pygame
import time
from Colours import Colours
from Constants import Constants
from Utils import Utils

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        
        self.image = Utils.LoadImage("bread.png", 100, 170)
        self.rect = self.image.get_rect()
        self.rect.center = (Constants.WIDTH / 2, Constants.HEIGHT / 2)

        #Собственное:
        self.isOnJump = False
        self.gravity = 0
        self.groundischeck = False #высота прыжка. Придумать, как инвертировать. 654
        #т.е. сделать так, чтоб больше высота - выше прыжок, а не наоборот, как сейчас

    def update(self):
        keystate = pygame.key.get_pressed()

        #Сделать движение влево-вправо
        #Сделать прыжок более реалистичным(настроить скорость подьема и падения)
        #Добавить папку resources и положить туда внешний вид спрайта
        
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 7
        if keystate[pygame.K_RIGHT]: 
            self.rect.x += 7


        if keystate[pygame.K_UP] and self.isOnJump == False:
            self.isOnJump = True
            self.gravity = -10
        if self.isOnJump == True:
            self.rect.y += self.gravity
            self.gravity += 0.4
            if self.groundischeck == True:
                    self.isOnJump = False

        if self.isOnJump == False:
            self.gravity = 0
            if self.isOnJump == False:
                self.rect.y += self.gravity
                self.gravity += 0.4


        if self.rect.right > Constants.WIDTH:
            self.rect.right = Constants.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom >= Constants.HEIGHT:
            self.rect.bottom = Constants.HEIGHT
            self.groundischeck = True
        else:
            self.groundischeck = False


        
        