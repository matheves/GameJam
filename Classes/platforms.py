import pygame
from Classes.spritesheet_functions import SpriteSheet

'''Class for platform and the differents type of platform'''

#   Name of file = (X,Y,WIDTH,HEIGHT)
BOOST                 = (  3,  3, 70, 70)
BLOCK                 = ( 75,  3, 70, 70)
SPIKE_UP              = (148,  4, 70, 70)
SPIKE_DOWN            = (222,  3, 70, 70)
FINISH                = (294,  4, 70, 70)
PORTAL_Y              = (367,  3, 70, 70)
PORTAL_B              = (440,  4, 70, 70)
SPRING                = (539, 19, 19, 27)
MINE                  = (510, 56, 70, 15)
WALL                  = (584,  5, 70,142)
FLOOR7                = (  3, 78,476, 70)

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

class GravityPortal(Platform):
    pass

class Pike(Platform):
    pass

class Boost(Platform):
    pass

class Mine(Platform):
    pass

class Finish(Platform):
    pass
