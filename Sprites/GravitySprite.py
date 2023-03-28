import pygame

class GravitySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()

        #Собственное:
        self.speedy = 0
        self.isFalling = False
        self.isMovingUp = False
        self.isOnJump = False