from Sprites.Items.BaseItem import BaseItem
from Utility.ImageUtils import ImageUtils
from settings import *
import os


class Pokeball(BaseItem):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        pathToFile = os.path.join(RECOURCES_PATH, "Tiles", "pokeball.png")
        self.image = ImageUtils.LoadImage(pathToFile, TILESIZE, TILESIZE)