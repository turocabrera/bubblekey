import pathlib

# Ruta base del proyecto
BASE_PATH = pathlib.Path(__file__).parent

# Rutas a tus recursos
ASSETS_PATH = BASE_PATH / "assets"
MAPS_PATH = ASSETS_PATH / "maps"
SPRITES_PATH = ASSETS_PATH / "sprites"

# Configuraciones de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bubblekey"