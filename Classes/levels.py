import pygame
import constants
import platforms

class Level():
    # Initialization
    platform_list = None
    background = None
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        # Manage collision and removable platform
        self.platform_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        # Update everything in the level
        self.platform_list.update()

    def draw(self, screen):
        # Draw the background
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw sprite list
        self.platform_list.draw(screen)

    def shift_world(self, shift_x):
        # Movement of the scenery when the player moves
        self.world_shift += shift_x
        # Sprite movement
        for platform in self.platform_list:
            platform.rect.x += shift_x

class Level_0(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("background_00.png").convert()
        self.level_limit = -2500

        level = [ [platforms.STONE_PLATFORM_MIDDLE, 50, 620],
                  [platforms.STONE_PLATFORM_MIDDLE, 50, 590],
                  [platforms.STONE_PLATFORM_MIDDLE, 50, 560],
                  [platforms.STONE_PLATFORM_MIDDLE, 50, 530],
                  [platforms.STONE_PLATFORM_MIDDLE, 50, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 50, 470],
                  [platforms.GRASS_LEFT, 0, 650],
                  [platforms.GRASS_MIDDLE, 70, 650],
                  [platforms.GRASS_MIDDLE, 140, 650],
                  [platforms.GRASS_MIDDLE, 210, 650],
                  [platforms.GRASS_MIDDLE, 280, 650],
                  [platforms.GRASS_MIDDLE, 350, 650],
                  [platforms.GRASS_MIDDLE, 420, 650],
                  [platforms.GRASS_MIDDLE, 490, 650],
                  [platforms.GRASS_MIDDLE, 560, 650],
                  [platforms.GRASS_MIDDLE, 630, 650],
                  [platforms.GRASS_MIDDLE, 700, 650],
                  [platforms.GRASS_MIDDLE, 770, 650],
                  [platforms.GRASS_MIDDLE, 840, 650],
                  [platforms.GRASS_MIDDLE, 910, 650],
                  [platforms.GRASS_MIDDLE, 980, 650],
                  [platforms.GRASS_MIDDLE, 1050, 650],
                  [platforms.GRASS_MIDDLE, 1120, 650],
                  [platforms.GRASS_MIDDLE, 1190, 650],
                  [platforms.GRASS_MIDDLE, 1260, 650],
                  [platforms.GRASS_MIDDLE, 1330, 650],
                  [platforms.GRASS_MIDDLE, 1400, 650],
                  [platforms.GRASS_MIDDLE, 1470, 650],
                  [platforms.GRASS_MIDDLE, 1540, 650],
                  [platforms.GRASS_MIDDLE, 1610, 650],
                  [platforms.GRASS_MIDDLE, 1680, 650],
                  [platforms.GRASS_MIDDLE, 1750, 650],
                  [platforms.GRASS_MIDDLE, 1820, 650],
                  [platforms.GRASS_MIDDLE, 1890, 650],
                  [platforms.GRASS_MIDDLE, 1960, 650],
                  [platforms.STONE_PLATFORM_MIDDLE, 2050, 620],
                  [platforms.STONE_PLATFORM_MIDDLE, 2050, 590],
                  [platforms.STONE_PLATFORM_MIDDLE, 2050, 560],
                  [platforms.STONE_PLATFORM_MIDDLE, 2050, 530],
                  [platforms.STONE_PLATFORM_MIDDLE, 2050, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 2050, 470],
                  [platforms.GRASS_MIDDLE, 2030, 650],
                  [platforms.GRASS_RIGHT, 2100, 650],
                  ]

        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
