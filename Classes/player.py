import pygame
import Classes.platforms
from Classes.platforms import Platform
from Classes.platforms import Spring
from Classes.spritesheet_functions import SpriteSheet
import constants

class Player(pygame.sprite.Sprite):
    """ATTRIBUTES"""

    change_x = 0
    change_y = 0

    #List of images for animation
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    walking_frames_d = []

    #direction player is facing0
    direction = "R"

    level = None

    """CONSTRUCTOR"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("Images\\astronaut_move.png")

        #Load all right faces into a list
        image = sprite_sheet.get_image(0, 128, 64, 64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(64, 128, 64, 64)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(128, 128, 64, 64)
        self.walking_frames_r.append(image)

        #Load all left faces into a list
        image = sprite_sheet.get_image(0, 64, 64, 64)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(64, 64, 64, 64)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(128, 64, 64, 64)
        self.walking_frames_l.append(image)

        #load all front fasces into list
        image = sprite_sheet.get_image(0, 0, 64, 64)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(64, 0, 64, 64)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(128, 0, 64, 64)
        self.walking_frames_u.append(image)

        #load all back faces into list
        image = sprite_sheet.get_image(0, 192, 64, 64)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(64, 192, 64, 64)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(64, 192, 64, 64)
        self.walking_frames_d.append(image)

        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

    def jump(self):
        """ Called when user jump """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    def update(self):
        """Move the player"""

        #gravity
        self.calc_grav()

        #Move Left/Right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        #Collision management
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            if type(block) == Spring:
                self.rect.y += 2
                platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
                self.rect.y -= 2

                # If it is ok to jump, set our speed upwards
                if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
                    self.change_y = -10

            # Stop our vertical movement
            self.change_y = 0


    def calc_grav(self):
        """ Calculate effect of gravity """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        #Check if we are on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >=0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """" Called when user jump """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    #Player Movement
    def go_left(self):
        """ Called when the user go left """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user go right """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the users don't move """
        self.change_x = 0
