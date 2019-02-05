import pygame

import constants

import Classes.platforms

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
        screen.fill(constants.RED)
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
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 620],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 590],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 560],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 530],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 500],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 470],
                  [Classes.platforms.MINE, 560, 638],
                  [Classes.platforms.SPIKE_UP, 840, 580],
                  [Classes.platforms.SPIKE_DOWN, 840, 440],
                  [Classes.platforms.SPIKE_RIGHT, 1050, 580],
                  [Classes.platforms.GRASS_MIDDLE, 1120, 650],
                  [Classes.platforms.GRASS_MIDDLE, 1190, 650],
                  [Classes.platforms.SPIKE_LEFT, 1190, 580],
                  [Classes.platforms.SPRING, 1353, 625],
                  [Classes.platforms.PORTAL_Y_DOWN, 1890, 580],
                  [Classes.platforms.PORTAL_Y_UP, 1890, 510],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 620],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 590],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 560],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 530],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 500],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 470],
                  [Classes.platforms.FLOOR28, 0, 650],

                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 118],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 148],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 178],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 208],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 238],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 50, 268],
                  [Classes.platforms.PORTAL_B_DOWN, 140, 118],
                  [Classes.platforms.PORTAL_B_UP, 139, 156],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 118],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 148],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 178],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 208],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 238],
                  #[Classes.platforms.STONE_PLATFORM_MIDDLE, 2050, 268],
                  [Classes.platforms.FLOOR28, 0, 48],
                  ]

        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
