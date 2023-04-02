import pygame
import os
class Constants():
    WIDTH = 480
    HEIGHT = 600
    FPS = 60 #GAME_PATH 
    score = 0
    timeofgame = 0
    GAME_PATH = os.path.dirname(__file__)
    RECOURCES_PATH = os.path.join(GAME_PATH, 'Texture')
    all_sprites = pygame.sprite.Group()