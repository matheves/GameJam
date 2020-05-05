"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame

import constants

class SpriteSheet(object):
    # Grab images out of a sprite
    sprite_sheet = None

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # Black works as the transparent color, can change
        image.set_colorkey(constants.BLACK)
        return image
