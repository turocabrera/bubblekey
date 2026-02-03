import arcade
import constants
from arcade import Rect

CHARACTER_SCALING = 3
VELOCIDAD_DRAGON=5
GRAVEDAD = 0.5
FUERZA_SALTO = 12

class BubblekeyGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)        
        # Solo declaramos las variables como None
        self.player_list = None
        self.dragon = None 
        self.scene = None
        self.tile_map = None
        self.motor_fisica = None # <--- No lo creamos aquí
        
        arcade.set_background_color(arcade.csscolor.BLUE_VIOLET)
        self.score = 0
        self.velocidad = VELOCIDAD_DRAGON
       
        nombreMapa = "escenarios.tmx"

        self.score = 0
        self.velocidad=VELOCIDAD_DRAGON



    def setup(self):
        """ Configuración inicial del juego """
        # Cargar el mapa Tiled
        nombre_mapa = "escenarios.tmx"
        self.tile_map = arcade.load_tilemap(str(constants.MAPS_PATH / nombre_mapa), scaling=1)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Preparar el Sprite del Dragón
        full_texture = arcade.load_texture(str(constants.SPRITES_PATH / "spritesbubble.png"))
        sub_texture = full_texture.crop(328, 15, 18, 18)        
        self.dragon = arcade.Sprite(sub_texture, scale=CHARACTER_SCALING)
        self.dragon.center_x = constants.SCREEN_WIDTH / 2
        self.dragon.center_y = 150 # Un poco más arriba de los 105 para que caiga
        
        # CREAR LA CAPA "Jugador" (esto soluciona el SceneKeyError)
        self.scene.add_sprite("Jugador", self.dragon)

        # RECIÉN AHORA creamos el motor de física
        self.motor_fisica = arcade.PhysicsEnginePlatformer(
            self.dragon,
            platforms=self.scene["tierra"], #este nombre lo damos desde tiled app
            gravity_constant=GRAVEDAD
        )
        
    def on_draw(self):
        """ Renderizar la pantalla """
        self.clear()                
        self.scene.draw()           
        arcade.draw_text(
            f"Score: {self.score}",
            10,                         # Posición X
            580,                         # Posición Y
            arcade.color.WHITE,
            font_size=18
        )

    def on_key_press(self, key, modifiers):
        """Se ejecuta cada vez que presionas una tecla"""
        comandosPermitidos = [65361, 65362, 65363, 65364]
    
        if key in comandosPermitidos:
            print(key)            
            if key == 65362: # ARRIBA (Salto)
                if self.motor_fisica.can_jump():
                    self.dragon.change_y = FUERZA_SALTO
            elif key == 65361: # IZQUIERDA
                self.dragon.change_x = -self.velocidad
            elif key == 65363: # DERECHA
                self.dragon.change_x = self.velocidad        
            # El puntaje sumando siempre
            self.score += 10
        else:
            print(f"Tecla {key} bloqueada: No es un comando permitido para el bubble.")

        # Por ahora, vamos a sumar puntos con cualquier tecla para probar
        self.score += 10        

    def on_key_release(self, key, modifiers):
        """ Se ejecuta cuando sueltas la tecla para que el dragón se detenga """
        if key in [65361, 65363]:
            self.dragon.change_x = 0
        # if key in [65361, 65362, 65363, 65364]:
        #     if key in [65362, 65364]:
        #         self.dragon.change_y = 0
        #         if self.dragon.center_y>550:
        #             self.dragon.center_y=550
        #         elif self.dragon.center_y<50:
        #             self.dragon.center_y=50
        #     elif key in [65361, 65363]:
        #         self.dragon.change_x = 0
        #         if self.dragon.center_x>750:
        #             self.dragon.center_x=750
        #         elif self.dragon.center_x<50:
        #             self.dragon.center_x=50


    def on_update(self, delta_time):
        """Se ejecuta unas 60 veces por segundo para actualizar la lógica"""
        # EL MOTOR SE ENCARGA DE TODO: gravedad, colisiones y posición.
        self.motor_fisica.update()

        # Si el dragón se cae del mapa (por debajo de Y=0), lo reseteamos
        if self.dragon.bottom < 0:
            if self.dragon.center_x<50:
                self.dragon.center_x = 50
            elif self.dragon.center_x>750:
                self.dragon.center_x = 750
            self.dragon.center_y = 115
            self.dragon.change_y = 0
        




def main():
    window = BubblekeyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()