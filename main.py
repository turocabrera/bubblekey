import arcade
import constants

class BubblekeyGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        
        # Listas para organizar nuestros sprites
        self.player_list = None
        self.wall_list = None
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Configuración inicial del juego (se llama al empezar o reiniciar) """
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Aquí es donde cargarías tu mapa de Tiled en el futuro:
        # self.tile_map = arcade.load_tilemap(constants.MAPS_PATH / "nivel1.tmx")

    def on_draw(self):
        """ Renderizar la pantalla """
        self.clear()
        # Aquí dibujaríamos las listas
        # self.wall_list.draw()
        # self.player_list.draw()

def main():
    window = BubblekeyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()