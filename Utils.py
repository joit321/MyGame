import os
import pygame
from Colours import Colours
from Constants import Constants
from Sprites.GravitySprite import GravitySprite

class Utils:
    @staticmethod
    def LoadImage(imageName : str, width: int, heigth : int):
        player_img = pygame.image.load(os.path.join(Constants.RECOURCES_PATH, imageName)).convert()
        player_img = pygame.transform.scale(player_img, (heigth, width))
        return player_img
    
    # Применение гравитации к спрайту.
    @staticmethod
    def ApplyGravity(gravitySprite : GravitySprite):
        gravitySprite.isFalling = False

        # Если находимся в прыжке, гравитацию не применяем.
        if gravitySprite.isMovingUp == True:
            return
        
        if Utils.IsOnSurface(gravitySprite):
            return
        
        gravitySprite.isFalling = True
        gravitySprite.rect.bottom += gravitySprite.speedy
        gravitySprite.speedy += 0.4 # скорость ускорения падения
    
    # Применение гравитации к спрайту.
    @staticmethod
    def IsOnSurface(gravitySprite : GravitySprite):
        # Если находимся на земле, не падаем :)
        if gravitySprite.rect.bottom >= Constants.HEIGHT:
            gravitySprite.rect.bottom = Constants.HEIGHT

        # Если находимся на земле, не падаем :)
        if gravitySprite.rect.bottom == Constants.HEIGHT:
            gravitySprite.speedy = 0 # Обнуляем скорость падения
            return True

        # Если спрайт лежит на ком-то, не падаем :)
        colidedSprites = pygame.sprite.spritecollide(gravitySprite, Constants.all_props, False)
        if colidedSprites:
            #gravitySprite.rect.bottom = 
            #print(colidedSprites[0])
            gravitySprite.speedy = 0 # Обнуляем скорость падения
            return True

        return False
        


        

