import pygame
from Classes.spritesheet_functions import SpriteSheet

#   Name of file = (X,Y,WIDTH,HEIGHT)
GRASS_LEFT            = (576, 720, 70, 70)
GRASS_MIDDLE          = (504, 576, 70, 70)
GRASS_RIGHT           = (576, 576, 70, 70)
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)
FLOOR28               = (  0, 990,1930,70)
SKY28                 = (  0,1075,1930,70)
WALL                  = (1029,412, 70,200)
SPIKE_UP              = (940, 480, 70, 70)
SPIKE_DOWN            = (940, 554, 70, 70)
SPIKE_RIGHT           = (720, 144, 70, 70)
SPIKE_LEFT            = (940, 626, 70, 70)
MINE                  = (432, 127, 70, 15)
SPRING                = (967, 347, 19, 27)
PORTAL_Y_DOWN         = (648, 432, 70, 70)
PORTAL_Y_UP           = (648, 390, 70, 40)
PORTAL_B_DOWN         = (648, 288, 70, 70)
PORTAL_B_UP           = (648, 174, 70, 40)

class Platform(pygame.sprite.Sprite):
    # Platform to jump
    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("Images/tiles_spritesheet.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()

class Spring(Platform):
    pass
