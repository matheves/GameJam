import pygame
import Classes.platforms
from Classes.platforms import *
from Classes.spritesheet_functions import SpriteSheet
import constants

class Player(pygame.sprite.Sprite):
    """ATTRIBUTES"""

    #attribute changing the position of the player after a move
    change_x = 0
    change_y = 0

    #List of images for animation
    walking_frames_LG = [] #Left with gravity
    walking_frames_RG = []  #right with gravity
    walking_frames_LAG = [] #Left with antigravity
    walking_frames_RAG = [] #right with antigravity

    #direction player is facing
    direction = "R"

    #level
    level = None

    #distance over wich the player will have a speed boost
    boost_x = 0

    #distance the player as traveled
    distance = 0

    gravity = True # True = gravity / False = antigravity

    score = 0 #score of the player

    multiplicateur = 1 #multpicator of the score

    """CONSTRUCTOR"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #load the file containing all the player sprites
        sprite_sheet = SpriteSheet("Images/astronaut_move.png")

        #Load all right faces into a list with gravity
        image = sprite_sheet.get_image(0, 128, 64, 64)
        self.walking_frames_RG.append(image)
        image = sprite_sheet.get_image(64, 128, 64, 64)
        self.walking_frames_RG.append(image)
        image = sprite_sheet.get_image(128, 128, 64, 64)
        self.walking_frames_RG.append(image)

        #Load all left faces into a list with gravity
        image = sprite_sheet.get_image(0, 64, 64, 64)
        self.walking_frames_LG.append(image)
        image = sprite_sheet.get_image(64, 64, 64, 64)
        self.walking_frames_LG.append(image)
        image = sprite_sheet.get_image(128, 64, 64, 64)
        self.walking_frames_LG.append(image)

        #load all right faces into list with antigravity
        image = sprite_sheet.get_image(0, 128, 64, 64)
        image = pygame.transform.flip(image, False, True)
        self.walking_frames_RAG.append(image)
        image = sprite_sheet.get_image(64, 128, 64, 64)
        image = pygame.transform.flip(image, False, True)
        self.walking_frames_RAG.append(image)
        image = sprite_sheet.get_image(128, 128, 64, 64)
        image = pygame.transform.flip(image, False, True)
        self.walking_frames_RAG.append(image)

        #load all back faces into list with antigravity
        image = sprite_sheet.get_image(0, 64, 64, 64)
        image = pygame.transform.flip(image, False, True)
        self.walking_frames_LAG.append(image)
        image = sprite_sheet.get_image(64, 64, 64, 64)
        image = pygame.transform.flip(image, False, True)
        self.walking_frames_LAG.append(image)
        image = sprite_sheet.get_image(64, 64, 64, 64)
        image = pygame.transform.flip(image, False, True)
        self.walking_frames_LAG.append(image)

        #define the start sprite
        self.image = self.walking_frames_RG[0]

        #transform the player into a rectangle for the hitbox
        self.rect = self.image.get_rect()

    def update(self):
        """Move the player"""

        #gravity
        self.calc_grav()

        #Move Left/Right
        self.distance += abs(self.change_x) #increment the distance
        self.rect.x += self.change_x #move the player
        pos = self.rect.x + self.level.world_shift #set player position

        #animation part
        if self.direction == "R" and self.gravity == True:
            frame = (pos // 30) % len(self.walking_frames_RG)
            self.image = self.walking_frames_RG[frame]
        elif self.direction == "R" and self.gravity == False:
            frame = (pos // 30) % len(self.walking_frames_RAG)
            self.image = self.walking_frames_RAG[frame]
        elif self.direction == "L" and self.gravity == True:
            frame = (pos // 30) % len(self.walking_frames_LG)
            self.image = self.walking_frames_LG[frame]
        else :
            frame = (pos // 30) % len(self.walking_frames_LAG)
            self.image = self.walking_frames_LAG[frame]

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

        #Check if we are out of the map
        if self.rect.y < 50 or self.rect.y > 700:
            son = pygame.mixer.Sound("Musiques/boom.wav")
            son.play()
            self.death()

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            #Send event for different situations
            if type(block) == Spring: #when he is on a spring
                son = pygame.mixer.Sound("Musiques/ressort.wav")
                son.play()
                springEvent = pygame.event.Event(Classes.constants.SPRING)
                pygame.event.post(springEvent)

            if type(block) == GravityPortal: #when he takes a gravity portal
                son = pygame.mixer.Sound("Musiques/grav.wav")
                son.play()
                gravityEvent = pygame.event.Event(Classes.constants.ANTIGRAVITY)
                pygame.event.post(gravityEvent)

            if type(block) == Pike or type(block) == Mine: #when a platform kill him
                son = pygame.mixer.Sound("Musiques/boom.wav")
                son.play()
                self.death()

            if type(block) == Boost: #when he takes a speed boost
                pygame.time.set_timer(Classes.constants.BOOST, 20)
                self.boost_x = self.distance + 280 #280 is corresponding to 4 blocks

            if type(block) == Finish: #when he finish the level
                son = pygame.mixer.Sound("Musiques/victory.wav")
                son.play()
                self.score += self.distance * self.multiplicateur
                self.multiplicateur += 1
                self.resetBoost()
                finishEvent = pygame.event.Event(Classes.constants.FINISH)
                pygame.event.post(finishEvent)

            # Stop our vertical movement
            self.change_y = 0

        #stop the boost when player has traveled 4 blocks
        if(self.boost_x != 0 and self.distance > self.boost_x):
            self.resetBoost()

    def calc_grav(self):
        """ Calculate effect of gravity """
        #check if we are in normal gravity
        if self.gravity == True :
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += .35

            #Check if we are on the ground
            if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >=0:
                self.change_y = 0
                self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
        else: #if we are in antigravity
            if self.change_y == 0 :
                self.change_y = -1
            else:
                self.change_y -= 0.35

            if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >=0:
                self.change_y = 0
                self.rect.y = constants.SCREEN_HEIGHT - self.rect.height


    def jump(self):
        """" Called when user jump """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.

        if self.gravity == True: #check if we are in normal gravity
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 2

            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
                self.change_y = -10

        else: #if we are in antigravity
            self.rect.y -= 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y += 2

            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
                self.change_y = 10




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

    #stop the effect of the boost
    def resetBoost(self):
        pygame.time.set_timer(Classes.constants.BOOST, 0)
        self.boost_x = 0
        self.stop()

    #same like jump but with bigger value
    def springJump(self):
        if self.gravity == True:
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 2

            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
                self.change_y = -15

        else:
            self.rect.y -= 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y += 2

            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
                self.change_y = 15

    def changeGravity(self):
        if self.gravity == True:
            self.change_y = -468
        else:
            self.rect.y = 468

        self.gravity = not self.gravity

    #call when the player is on a boost
    def go_boost(self):
        self.change_x = 12
        self.direction = "R"

    #call when the player die
    def death(self):
        #reset movement
        self.change_x = 0
        self.change_y = 0
        #calcul score
        self.score += self.distance * self.multiplicateur
        #reset distance and multiplicateur
        self.multiplicateur = 1
        self.distance = 0
        #reset eventually a boost effect
        self.resetBoost()
        #send a deathEvent
        deathEvent = pygame.event.Event(Classes.constants.DEATH)
        pygame.event.post(deathEvent)
