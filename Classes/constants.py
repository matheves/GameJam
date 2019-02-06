"""
Constants
"""

import pygame

# Screen dimensions
SCREEN_WIDTH  = 1024
SCREEN_HEIGHT = 768

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)

# Events

SPRING = pygame.USEREVENT + 1
PIKE = pygame.USEREVENT + 2
ANTIGRAVITY = pygame.USEREVENT + 3
ENDLEVEL = pygame.USEREVENT + 4
