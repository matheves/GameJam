"""
Constants for the game
"""

import pygame
import Classes.platforms

# Screen dimensions
SCREEN_WIDTH  = 1024
SCREEN_HEIGHT = 768

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)

#player size
playerHeight = 64
playerWidth = 64

#Player Cordinate at level start
levelStart_x = 340
levelStart_y = SCREEN_HEIGHT - playerHeight - 118

#level informations
bottomBorder = 704
topBorder = 118
nbLevel = 24

# Events
SPRING = pygame.USEREVENT + 1
DEATH = pygame.USEREVENT + 2
ANTIGRAVITY = pygame.USEREVENT + 3
ENDLEVEL = pygame.USEREVENT + 4
BOOST = pygame.USEREVENT + 5
FINISH = pygame.USEREVENT + 6
ENTER_PSEUDO = pygame.USEREVENT + 7
