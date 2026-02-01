import arcade
import constants
from arcade import Rect

CHARACTER_SCALING = 4

class BubblekeyGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)        
        # Listas para organizar nuestros sprites
        self.player_list = None
        self.wall_list = None        
        # arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        arcade.set_background_color(arcade.csscolor.BLUE_VIOLET)

    def setup(self):
        self.player_list = arcade.SpriteList()

        full_texture = arcade.load_texture(str(constants.SPRITES_PATH / "spritesbubble.png"))

        sub_texture = full_texture.crop(328, 15, 18, 18)

        self.player_sprite = arcade.Sprite(sub_texture)
        
        self.player_sprite.scale = CHARACTER_SCALING
        self.player_sprite.center_x = constants.SCREEN_WIDTH / 2
        self.player_sprite.center_y = constants.SCREEN_HEIGHT / 2        
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """ Renderizar la pantalla """
        self.clear()        
        self.player_list.draw()

def main():
    window = BubblekeyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()