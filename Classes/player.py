import pygame
import Classes.platforms
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

        sprite_sheet = SpriteSheet("..\Images\\astronaut_move.png")

        #Load all right faces into a list
        image = sprite_sheet.get_image(0, 64, 32, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(32, 64, 32, 32)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(64, 64, 32, 32)
        self.walking_frames_r.append(image)

        #Load all left faces into a list
        image = sprite_sheet.get_image(0, 32, 32, 32)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(32, 32, 32, 32)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(64, 32, 32, 32)
        self.walking_frames_l.append(image)

        #load all front fasces into list
        image = sprite_sheet.get_image(0, 0, 32, 32)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(32, 0, 32, 32)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(64, 0, 32, 32)
        self.walking_frames_u.append(image)

        #load all back faces into list
        image = sprite_sheet.get_image(0, 96, 32, 32)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(32, 96, 32, 32)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(64, 96, 32, 32)
        self.walking_frames_d.append(image)

        self.image = self.walking_frames_r[0]

        self.image = self.image.get_rect()

    def update(self):
        """Move the player"""

        #gravity
        self.calc_grav()

        #Move Left/Right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r[frame])
            self.image = self.walking_frame_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        #Collision management
        block_hit_list = pygame.sprite.spritecollide(self, self.level.plateform_list, False)
        for block in block_hit_list:
            #Reset position of top/bottom
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = self.rect.bottom

            # Stop vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect += block.change_x


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

    def jump():
        """ Called when user jump """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.

        self.rect.y += 2
        plateform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        #if it is okay go jump
        if len(plateform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
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
