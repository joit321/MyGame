# define some colors (R, G, B)
import os


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 120
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 300

GAME_PATH = os.path.dirname(__file__)
RECOURCES_PATH = os.path.join(GAME_PATH, 'Res')
MAPS_PATH = os.path.join(GAME_PATH, 'Maps')
TILE_RESOURCES_PATH = os.path.join(RECOURCES_PATH, 'Tiles')
ITEMS_RESOURCES_PATH = os.path.join(RECOURCES_PATH, 'Items')
CREATURES_RESOURCES_PATH = os.path.join(RECOURCES_PATH, 'Creatures')