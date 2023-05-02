from Sprites.Tiles.BaseTile import BaseTile
from Utility.ImageUtils import ImageUtils
from settings import *
import os

class Water(BaseTile):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        pathToFile = os.path.join(RECOURCES_PATH, "Tiles", "земля.png")
        self.image = ImageUtils.LoadImage(pathToFile, TILESIZE, TILESIZE)