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

    def reset(self,player):
        pygame.display.flip()
#test
class Level_0(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 50, 450],
                  [Classes.platforms.MINE, 560, 638],
                  [Classes.platforms.SPIKE_UP, 840, 580],
                  [Classes.platforms.SPIKE_DOWN, 840, 260],
                  [Classes.platforms.SPRING, 1209, 625],
                  [Classes.platforms.WALL, 1840, 450],
                  [Classes.platforms.FLOOR28, 0, 650],
                  [Classes.platforms.PORTAL_Y, 1680, 650],
                  [Classes.platforms.BOOST, 1430, 650],
                  [Classes.platforms.FINISH, 260, 650],

                  [Classes.platforms.WALL, 50, 118],
                  [Classes.platforms.WALL, 1840, 118],
                  [Classes.platforms.SKY28, 0, 48],
                  [Classes.platforms.PORTAL_B, 125, 48],
                  ]

        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            elif platform[0] == Classes.platforms.PORTAL_Y or platform[0] == Classes.platforms.PORTAL_B:
                block = Classes.platforms.GravityPortal(platform[0])
            elif platform[0] == Classes.platforms.SPIKE_UP or platform[0] == Classes.platforms.SPIKE_DOWN:
                block = Classes.platforms.Pike(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

class Level_1(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 50, 450],
                  [Classes.platforms.WALL, 50, 300],
                  [Classes.platforms.SPIKE_UP, 600, 330],
                  [Classes.platforms.SPIKE_UP, 1150, 580],
                  [Classes.platforms.SPIKE_UP, 1420, 580],
                  [Classes.platforms.SPIKE_DOWN, 1290, 420],
                  [Classes.platforms.SPRING, 390, 625],
                  [Classes.platforms.GRASS_LEFT,0,650],
                  [Classes.platforms.GRASS_MIDDLE,70,650],
                  [Classes.platforms.GRASS_MIDDLE,140,650],
                  [Classes.platforms.GRASS_MIDDLE,210,650],
                  [Classes.platforms.GRASS_MIDDLE,280,650],
                  [Classes.platforms.GRASS_MIDDLE,350,650],
                  [Classes.platforms.GRASS_MIDDLE,600,400],
                  [Classes.platforms.GRASS_MIDDLE,670,400],
                  [Classes.platforms.GRASS_MIDDLE,740,400],
                  [Classes.platforms.FLOOR28, 1000, 650],

                  [Classes.platforms.WALL, 50, 118],
                  [Classes.platforms.SKY28, 0, 48],
                  [Classes.platforms.FINISH, 1900, 650],
                  ]

        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            elif platform[0] == Classes.platforms.PORTAL_Y or platform[0] == Classes.platforms.PORTAL_B:
                block = Classes.platforms.GravityPortal(platform[0])
            elif platform[0] == Classes.platforms.SPIKE_UP or platform[0] == Classes.platforms.SPIKE_DOWN:
                block = Classes.platforms.Pike(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

class Level_2(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 50, 450],
                  [Classes.platforms.WALL, 50, 300],
                  [Classes.platforms.SPIKE_UP, 980, 580],
                  [Classes.platforms.SPIKE_UP, 910, 580],
                  [Classes.platforms.SPIKE_UP, 1050, 580],
                  [Classes.platforms.SPIKE_UP, 770, 580],
                  [Classes.platforms.MINE, 1335, 638],
                  [Classes.platforms.MINE, 1405, 638],
                  [Classes.platforms.MINE, 1475, 638],
                  [Classes.platforms.MINE, 1520, 638],
                  [Classes.platforms.GRASS_MIDDLE,700,580],
                  [Classes.platforms.GRASS_MIDDLE,840,580],
                  [Classes.platforms.GRASS_MIDDLE,840,510],
                  [Classes.platforms.GRASS_MIDDLE,840,440],
                  [Classes.platforms.FLOOR28, 0, 650],
                  [Classes.platforms.FINISH, 1770, 650],

                  [Classes.platforms.WALL, 50, 118],
                  [Classes.platforms.SKY28, 0, 48],
                  ]

        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            elif platform[0] == Classes.platforms.PORTAL_Y or platform[0] == Classes.platforms.PORTAL_B:
                block = Classes.platforms.GravityPortal(platform[0])
            elif platform[0] == Classes.platforms.SPIKE_UP or platform[0] == Classes.platforms.SPIKE_DOWN:
                block = Classes.platforms.Pike(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

class Level_3(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 50, 450],
                  [Classes.platforms.WALL, 50, 300],
                  [Classes.platforms.SPRING, 450, 625],
                  [Classes.platforms.SPRING, 1620, 625],
                  [Classes.platforms.SPIKE_UP, 550, 580],
                  [Classes.platforms.SPIKE_UP, 800, 580],
                  [Classes.platforms.SPIKE_UP, 1000, 580],
                  [Classes.platforms.SPIKE_UP, 1690, 380],
                  [Classes.platforms.SPIKE_UP, 1850, 380],
                  [Classes.platforms.SPIKE_DOWN, 400, 188],
                  [Classes.platforms.SPIKE_DOWN, 470, 188],
                  [Classes.platforms.SPIKE_DOWN, 540, 188],
                  [Classes.platforms.MINE, 1335, 638],
                  [Classes.platforms.GRASS_MIDDLE,400,118],
                  [Classes.platforms.GRASS_MIDDLE,470,118],
                  [Classes.platforms.GRASS_MIDDLE,540,118],
                  [Classes.platforms.FLOOR28, 0, 650],
                  [Classes.platforms.FINISH, 1770, 650],

                  [Classes.platforms.WALL, 50, 118],
                  [Classes.platforms.WALL, 1690, 450],
                  [Classes.platforms.WALL, 1850, 450],
                  [Classes.platforms.SKY28, 0, 48],
                  ]

        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            elif platform[0] == Classes.platforms.PORTAL_Y or platform[0] == Classes.platforms.PORTAL_B:
                block = Classes.platforms.GravityPortal(platform[0])
            elif platform[0] == Classes.platforms.SPIKE_UP or platform[0] == Classes.platforms.SPIKE_DOWN:
                block = Classes.platforms.Pike(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

class Level_4(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 50, 450],
                  [Classes.platforms.WALL, 50, 300],
                  [Classes.platforms.SPRING, 1225, 625],
                  [Classes.platforms.SPIKE_UP, 750, 580],
                  [Classes.platforms.SPIKE_UP, 960, 580],
                  [Classes.platforms.SPIKE_DOWN, 750, 350],
                  [Classes.platforms.SPIKE_DOWN, 960, 350],
                  [Classes.platforms.GRASS_LEFT,0,650],
                  [Classes.platforms.GRASS_MIDDLE,70,650],
                  [Classes.platforms.GRASS_MIDDLE,140,650],
                  [Classes.platforms.GRASS_MIDDLE,210,650],
                  [Classes.platforms.GRASS_MIDDLE,280,650],
                  [Classes.platforms.GRASS_MIDDLE,350,650],
                  [Classes.platforms.GRASS_MIDDLE,420,650],
                  [Classes.platforms.GRASS_MIDDLE,490,650],
                  [Classes.platforms.GRASS_MIDDLE,750,650],
                  [Classes.platforms.GRASS_MIDDLE,820,650],
                  [Classes.platforms.GRASS_MIDDLE,890,650],
                  [Classes.platforms.GRASS_MIDDLE,960,650],
                  [Classes.platforms.GRASS_MIDDLE,1200,650],
                  [Classes.platforms.FINISH, 1770, 650],

                  [Classes.platforms.WALL, 50, 118],
                  [Classes.platforms.WALL, 750, 118],
                  [Classes.platforms.WALL, 960, 160],
                  [Classes.platforms.WALL, 960, 118],
                  [Classes.platforms.WALL, 750, 160],
                  [Classes.platforms.SKY28, 0, 48],
                  ]

        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            elif platform[0] == Classes.platforms.PORTAL_Y or platform[0] == Classes.platforms.PORTAL_B:
                block = Classes.platforms.GravityPortal(platform[0])
            elif platform[0] == Classes.platforms.SPIKE_UP or platform[0] == Classes.platforms.SPIKE_DOWN:
                block = Classes.platforms.Pike(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

class Level_5(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 50, 450],
                  [Classes.platforms.WALL, 50, 300],
                  [Classes.platforms.MINE, 1335, 638],
                  [Classes.platforms.GRASS_LEFT,0,650],
                  [Classes.platforms.GRASS_MIDDLE,70,650],
                  [Classes.platforms.GRASS_MIDDLE,140,650],
                  [Classes.platforms.GRASS_MIDDLE,210,650],
                  [Classes.platforms.GRASS_MIDDLE,280,650],
                  [Classes.platforms.GRASS_MIDDLE,350,650],
                  [Classes.platforms.GRASS_MIDDLE,420,650],
                  [Classes.platforms.GRASS_MIDDLE,490,650],
                  [Classes.platforms.GRASS_MIDDLE,870,650],
                  [Classes.platforms.GRASS_MIDDLE,1000,500],
                  [Classes.platforms.GRASS_MIDDLE,1335,650],
                  [Classes.platforms.GRASS_MIDDLE,1400,650],
                  [Classes.platforms.GRASS_MIDDLE,1100,650],
                  [Classes.platforms.FINISH, 1770, 650],

                  [Classes.platforms.WALL, 50, 118],
                  [Classes.platforms.SKY28, 0, 48],
                  ]

        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            elif platform[0] == Classes.platforms.PORTAL_Y or platform[0] == Classes.platforms.PORTAL_B:
                block = Classes.platforms.GravityPortal(platform[0])
            elif platform[0] == Classes.platforms.SPIKE_UP or platform[0] == Classes.platforms.SPIKE_DOWN:
                block = Classes.platforms.Pike(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

class Level_6(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 50, 450],
                  [Classes.platforms.WALL, 50, 300],
                  [Classes.platforms.SPIKE_UP, 570, 580],
                  [Classes.platforms.SPIKE_UP, 1100, 640],
                  [Classes.platforms.SPIKE_UP, 1150, 640],
                  [Classes.platforms.SPIKE_UP, 1400, 640],
                  [Classes.platforms.SPIKE_DOWN, 500, 60],

                  [Classes.platforms.FLOOR28, 0, 650],
                  [Classes.platforms.FINISH, 1770, 650],

                  [Classes.platforms.WALL, 50, 118],
                  [Classes.platforms.WALL, 950, 450],
                  [Classes.platforms.WALL, 1850, 118],
                  [Classes.platforms.SKY28, 0, 48],
                  [Classes.platforms.PORTAL_Y, 500, 650],
                  [Classes.platforms.PORTAL_Y, 850, 650],
                  [Classes.platforms.PORTAL_B, 1100, 48],
                  [Classes.platforms.PORTAL_B, 1400, 48],
                  [Classes.platforms.PORTAL_B, 700, 48],
                  ]

        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            elif platform[0] == Classes.platforms.PORTAL_Y or platform[0] == Classes.platforms.PORTAL_B:
                block = Classes.platforms.GravityPortal(platform[0])
            elif platform[0] == Classes.platforms.SPIKE_UP or platform[0] == Classes.platforms.SPIKE_DOWN:
                block = Classes.platforms.Pike(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
