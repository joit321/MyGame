import pygame

class ImageUtils:
    @staticmethod
    def LoadImage(imagePath : str, width: int, heigth : int):
        player_img = pygame.image.load(imagePath).convert()
        player_img = pygame.transform.scale(player_img, (heigth, width))
        return player_img