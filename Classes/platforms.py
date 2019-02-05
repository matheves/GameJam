import pygame
from spritesheet_functions import SpriteSheet

#   Name of file = (X,Y,WIDTH,HEIGHT)
GRASS_LEFT            = (576, 720, 70, 70)
GRASS_MIDDLE          = (504, 576, 70, 70)
GRASS_RIGHT           = (576, 576, 70, 70)
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)

class Platform(pygame.sprite.Sprite):
    # Platform to jump
    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("tiles_spritesheet.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()
