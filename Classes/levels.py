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

    def checkBlock(self, level):
        for platform in level:
            if platform[0] == Classes.platforms.SPRING:
                block = Classes.platforms.Spring(platform[0])
            elif platform[0] == Classes.platforms.PORTAL_Y or platform[0] == Classes.platforms.PORTAL_B:
                block = Classes.platforms.GravityPortal(platform[0])
            elif platform[0] == Classes.platforms.SPIKE_UP or platform[0] == Classes.platforms.SPIKE_DOWN:
                block = Classes.platforms.Pike(platform[0])
            elif platform[0] == Classes.platforms.BOOST:
                block = Classes.platforms.Boost(platform[0])
            elif platform[0] == Classes.platforms.MINE:
                block = Classes.platforms.Mine(platform[0])
            elif platform[0] == Classes.platforms.FINISH:
                block = Classes.platforms.Finish(platform[0])
            else :
                block = Classes.platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
#test
class Level_0(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],
                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.MINE, 560, 638],
                  [Classes.platforms.SPIKE_UP, 840, 580],
                  [Classes.platforms.SPIKE_UP, 840, 260],
                  [Classes.platforms.PORTAL_B, 125, 48],
                  [Classes.platforms.PORTAL_Y, 1680, 650],
                  [Classes.platforms.SPRING, 1209, 625],
                  [Classes.platforms.BOOST, 1430, 650],
                  [Classes.platforms.FINISH, 260, 650],
                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  ]

        self.checkBlock(level)

class Level_1(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.SPIKE_UP, 600, 330],
                  [Classes.platforms.SPIKE_UP, 1150, 580],
                  [Classes.platforms.SPIKE_UP, 1420, 580],
                  [Classes.platforms.SPIKE_DOWN, 1290, 420],
                  [Classes.platforms.SPRING, 390, 625],
                  [Classes.platforms.BLOCK,70,650],
                  [Classes.platforms.BLOCK,140,650],
                  [Classes.platforms.BLOCK,210,650],
                  [Classes.platforms.BLOCK,280,650],
                  [Classes.platforms.BLOCK,350,650],
                  [Classes.platforms.BLOCK,600,400],
                  [Classes.platforms.BLOCK,670,400],
                  [Classes.platforms.BLOCK,740,400],
                  [Classes.platforms.FLOOR7, 1000, 650],
                  [Classes.platforms.FLOOR7, 1476, 650],

                  [Classes.platforms.WALL, 77, 118],
                  [Classes.platforms.WALL, 77, 260],
                  [Classes.platforms.WALL, 77, 368],
                  [Classes.platforms.WALL, 77, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],
                  [Classes.platforms.FINISH, 1700, 650],
                  ]

        self.checkBlock(level)

class Level_2(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.SPIKE_UP, 980, 580],
                  [Classes.platforms.SPIKE_UP, 910, 580],
                  [Classes.platforms.SPIKE_UP, 1050, 580],
                  [Classes.platforms.SPIKE_UP, 770, 580],
                  [Classes.platforms.MINE, 1335, 638],
                  [Classes.platforms.MINE, 1405, 638],
                  [Classes.platforms.MINE, 1475, 638],
                  [Classes.platforms.MINE, 1520, 638],
                  [Classes.platforms.BLOCK,700,580],
                  [Classes.platforms.BLOCK,840,580],
                  [Classes.platforms.BLOCK,840,510],
                  [Classes.platforms.BLOCK,840,440],
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],
                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.FINISH, 1770, 650],

                  ]

        self.checkBlock(level)

class Level_3(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.SPRING, 450, 625],
                  [Classes.platforms.SPRING, 1620, 625],
                  [Classes.platforms.SPIKE_UP, 550, 580],
                  [Classes.platforms.SPIKE_UP, 800, 580],
                  [Classes.platforms.SPIKE_UP, 1000, 580],
                  [Classes.platforms.SPIKE_UP, 1690, 380],
                  [Classes.platforms.SPIKE_DOWN, 400, 188],
                  [Classes.platforms.SPIKE_DOWN, 470, 188],
                  [Classes.platforms.SPIKE_DOWN, 540, 188],
                  [Classes.platforms.MINE, 1335, 638],
                  [Classes.platforms.BLOCK,400,118],
                  [Classes.platforms.BLOCK,470,118],
                  [Classes.platforms.BLOCK,540,118],
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],
                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.FINISH, 1770, 650],
                  [Classes.platforms.WALL, 1690, 450],
                  [Classes.platforms.WALL, 1690, 510],
                  ]

        self.checkBlock(level)

class Level_4(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 70, 118],
                  [Classes.platforms.WALL, 70, 260],
                  [Classes.platforms.WALL, 70, 368],
                  [Classes.platforms.WALL, 70, 510],
                  [Classes.platforms.SPRING, 1225, 625],
                  [Classes.platforms.SPIKE_UP, 750, 580],
                  [Classes.platforms.SPIKE_UP, 960, 580],
                  [Classes.platforms.SPIKE_DOWN, 750, 350],
                  [Classes.platforms.SPIKE_DOWN, 960, 350],
                  [Classes.platforms.BLOCK,70,650],
                  [Classes.platforms.BLOCK,140,650],
                  [Classes.platforms.BLOCK,210,650],
                  [Classes.platforms.BLOCK,280,650],
                  [Classes.platforms.BLOCK,350,650],
                  [Classes.platforms.BLOCK,420,650],
                  [Classes.platforms.BLOCK,490,650],
                  [Classes.platforms.BLOCK,750,650],
                  [Classes.platforms.BLOCK,820,650],
                  [Classes.platforms.BLOCK,890,650],
                  [Classes.platforms.BLOCK,960,650],
                  [Classes.platforms.BLOCK,1200,650],
                  [Classes.platforms.FINISH, 1770, 650],

                  [Classes.platforms.WALL, 750, 118],
                  [Classes.platforms.WALL, 960, 210],
                  [Classes.platforms.WALL, 960, 118],
                  [Classes.platforms.WALL, 750, 210],
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],
                  ]

        self.checkBlock(level)

class Level_5(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.WALL, 70, 118],
                  [Classes.platforms.WALL, 70, 260],
                  [Classes.platforms.WALL, 70, 368],
                  [Classes.platforms.WALL, 70, 510],
                  [Classes.platforms.MINE, 1335, 638],
                  [Classes.platforms.BLOCK,70,650],
                  [Classes.platforms.BLOCK,140,650],
                  [Classes.platforms.BLOCK,210,650],
                  [Classes.platforms.BLOCK,280,650],
                  [Classes.platforms.BLOCK,350,650],
                  [Classes.platforms.BLOCK,420,650],
                  [Classes.platforms.BLOCK,490,650],
                  [Classes.platforms.BLOCK,870,650],
                  [Classes.platforms.BLOCK,1000,500],
                  [Classes.platforms.BLOCK,1335,650],
                  [Classes.platforms.BLOCK,1400,650],
                  [Classes.platforms.BLOCK,1100,650],
                  [Classes.platforms.FINISH, 1770, 650],

                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],
                  ]

        self.checkBlock(level)

class Level_6(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ [Classes.platforms.SPIKE_UP, 570, 580],
                  [Classes.platforms.SPIKE_UP, 1100, 640],
                  [Classes.platforms.SPIKE_UP, 1150, 640],
                  [Classes.platforms.SPIKE_UP, 1400, 640],
                  [Classes.platforms.SPIKE_DOWN, 500, 60],


                  [Classes.platforms.WALL, 950, 450],
                  [Classes.platforms.WALL, 950, 510],
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],
                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.PORTAL_Y, 500, 650],
                  [Classes.platforms.PORTAL_Y, 850, 650],
                  [Classes.platforms.PORTAL_B, 1100, 48],
                  [Classes.platforms.PORTAL_B, 1400, 48],
                  [Classes.platforms.PORTAL_B, 700, 48],
                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_7(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],

                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.BOOST, 440, 650],
                  [Classes.platforms.SPIKE_UP, 570, 650],
                  [Classes.platforms.SPIKE_UP, 800, 580],
                  [Classes.platforms.SPRING, 900, 625],
                  [Classes.platforms.SPIKE_UP, 1050, 330],
                  [Classes.platforms.BLOCK, 1120, 330],
                  [Classes.platforms.BOOST, 1400, 650],

                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_8(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],
                  [Classes.platforms.FLOOR7, 880, 650],

                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.BOOST, 810, 650],
                  [Classes.platforms.SPIKE_UP, 600, 650],
                  [Classes.platforms.SPIKE_UP, 1000, 650],
                  [Classes.platforms.SPIKE_DOWN, 485, 450],
                  [Classes.platforms.SPIKE_DOWN, 885, 450],
                  [Classes.platforms.BOOST, 465, 650],
                  [Classes.platforms.BOOST, 1200, 650],
                  [Classes.platforms.SPRING, 1550, 670],

                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_9(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],

                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.PORTAL_B, 1770, 48],
                  [Classes.platforms.PORTAL_Y, 600, 650],
                  [Classes.platforms.SPIKE_UP, 530, 650],
                  [Classes.platforms.SPIKE_UP, 755, 220],
                  [Classes.platforms.WALL, 680, 510],
                  [Classes.platforms.WALL, 680, 400],
                  [Classes.platforms.BOOST, 790, 48],
                  [Classes.platforms.SPIKE_DOWN, 890, 48],
                  [Classes.platforms.WALL, 1300, 178],
                  [Classes.platforms.WALL, 1300, 118],
                  [Classes.platforms.SPIKE_DOWN, 1400, 48],
                  [Classes.platforms.SPIKE_DOWN, 1550, 48],
                  [Classes.platforms.SPRING, 1100, 118],


                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_10(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],

                  [Classes.platforms.FLOOR7, 1428, 650],

                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.BOOST, 882, 650],
                  [Classes.platforms.PORTAL_Y, 750, 650],
                  [Classes.platforms.PORTAL_B, 1400, 48],
                  [Classes.platforms.SPIKE_DOWN, 980, 260],
                  [Classes.platforms.SPIKE_DOWN, 1300, 260],
                  [Classes.platforms.WALL, 980, 118],
                  [Classes.platforms.WALL, 1300, 118],
                  [Classes.platforms.SPIKE_DOWN, 1230, 260],
                  [Classes.platforms.WALL, 1230, 118],
                  [Classes.platforms.SPRING, 1100, 118],
                  [Classes.platforms.SPRING, 900, 118],
                  [Classes.platforms.SPIKE_UP, 1470, 650],

                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_11(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],

                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.SPRING, 430, 625],
                  [Classes.platforms.BOOST, 970, 650],
                  [Classes.platforms.SPIKE_UP, 1090, 650],
                  [Classes.platforms.SPIKE_UP, 1250, 650],
                  [Classes.platforms.SPIKE_UP, 1310, 650],
                  [Classes.platforms.PORTAL_Y, 1170, 650],
                  [Classes.platforms.PORTAL_B, 1770, 48],
                  [Classes.platforms.SPIKE_DOWN, 1300, 48],
                  [Classes.platforms.SPIKE_DOWN, 1370, 48],
                  [Classes.platforms.SPIKE_DOWN, 1440, 48],
                  [Classes.platforms.SPIKE_DOWN, 1510, 48],
                  [Classes.platforms.SPIKE_DOWN, 1580, 48],
                  [Classes.platforms.SPIKE_DOWN, 1650, 48],
                  [Classes.platforms.SPIKE_DOWN, 1680, 48],
                  [Classes.platforms.SPRING, 1250, 118],

                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_12(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],

                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.SPRING, 430, 625],
                  [Classes.platforms.SPRING, 970, 625],
                  [Classes.platforms.SPRING, 1470, 625],
                  [Classes.platforms.MINE, 500, 640],
                  [Classes.platforms.MINE, 570, 640],
                  [Classes.platforms.MINE, 640, 640],
                  [Classes.platforms.MINE, 710, 640],
                  [Classes.platforms.MINE, 780, 640],
                  [Classes.platforms.MINE, 850, 640],
                  [Classes.platforms.MINE, 1000, 640],
                  [Classes.platforms.MINE, 1070, 640],
                  [Classes.platforms.MINE, 1140, 640],
                  [Classes.platforms.MINE, 1210, 640],
                  [Classes.platforms.MINE, 1280, 640],
                  [Classes.platforms.MINE, 1350, 640],
                  [Classes.platforms.MINE, 1500, 640],
                  [Classes.platforms.MINE, 1570, 640],
                  [Classes.platforms.MINE, 1640, 640],
                  [Classes.platforms.MINE, 1700, 640],


                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_13(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],


                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.PORTAL_Y, 406, 650],
                  [Classes.platforms.PORTAL_B, 1650, 48],
                  [Classes.platforms.BOOST, 476, 48],

                  [Classes.platforms.SPIKE_DOWN, 540, 48],
                  [Classes.platforms.SPIKE_DOWN, 610, 48],
                  [Classes.platforms.SPIKE_DOWN, 680, 48],
                  [Classes.platforms.SPRING, 760, 118],
                  [Classes.platforms.SPRING, 920, 118],
                  [Classes.platforms.SPRING, 1080, 118],
                  [Classes.platforms.SPRING, 1240, 118],
                  [Classes.platforms.SPRING, 1400, 118],
                  [Classes.platforms.WALL, 800, 118],
                  [Classes.platforms.WALL, 800, 218],
                  [Classes.platforms.SPIKE_DOWN, 800, 338],
                  [Classes.platforms.WALL, 980, 118],
                  [Classes.platforms.WALL, 980, 218],
                  [Classes.platforms.SPIKE_DOWN, 980, 338],
                  [Classes.platforms.WALL, 1150, 118],
                  [Classes.platforms.WALL, 1150, 218],
                  [Classes.platforms.SPIKE_DOWN, 1150, 338],
                  [Classes.platforms.WALL, 1320, 118],
                  [Classes.platforms.WALL, 1320, 218],
                  [Classes.platforms.SPIKE_DOWN, 1320, 338],
                  [Classes.platforms.WALL, 1500, 118],
                  [Classes.platforms.WALL, 1500, 218],
                  [Classes.platforms.SPIKE_DOWN, 1500, 338],



                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_14(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 470, 500],
                  [Classes.platforms.PORTAL_Y, 406, 650],
                  [Classes.platforms.PORTAL_Y, 1050, 650],
                  [Classes.platforms.PORTAL_Y, 1400, 650],
                  [Classes.platforms.PORTAL_B, 800, 118],
                  [Classes.platforms.PORTAL_B, 1000, 118],
                  [Classes.platforms.PORTAL_B, 1600, 118],
                  [Classes.platforms.SPRING, 410, 118],
                  [Classes.platforms.SPRING, 665, 625],
                  [Classes.platforms.SPRING, 1150, 625],
                  [Classes.platforms.SPRING, 1404, 118],

                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_15(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],


                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.BOOST, 406, 650],
                  [Classes.platforms.BOOST, 800, 650],
                  [Classes.platforms.BOOST, 1200, 650],
                  [Classes.platforms.BOOST, 1270, 650],
                  [Classes.platforms.BOOST, 1340, 650],
                  [Classes.platforms.SPRING, 1770, 650],
                  [Classes.platforms.FLOOR7, 1200, 350],
                  [Classes.platforms.FLOOR7, 800, 350],


                  [Classes.platforms.BOOST, 1350, 350],
                  [Classes.platforms.SPIKE_UP, 1410, 350],
                  [Classes.platforms.SPIKE_UP, 1480, 350],
                  [Classes.platforms.SPIKE_UP, 1530, 350],
                  [Classes.platforms.SPIKE_UP, 1000, 350],
                  [Classes.platforms.SPIKE_UP, 930, 350],
                  [Classes.platforms.SPRING, 1100, 325],
                  [Classes.platforms.SPIKE_DOWN, 1000, 48],
                  [Classes.platforms.SPIKE_DOWN, 930, 48],
                  [Classes.platforms.SPIKE_UP, 640, 350],
                  [Classes.platforms.SPIKE_UP, 580, 350],
                  [Classes.platforms.SPIKE_UP, 510, 350],
                  [Classes.platforms.BLOCK, 710, 350],
                  [Classes.platforms.BLOCK, 750, 350],
                  [Classes.platforms.BLOCK, 195, 350],
                  [Classes.platforms.BLOCK, 265, 350],
                  [Classes.platforms.BLOCK, 335, 350],

                  [Classes.platforms.FINISH, 125, 350],
                  ]

        self.checkBlock(level)

class Level_16(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],
                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],

                  [Classes.platforms.SPRING, 125, 623],
                  [Classes.platforms.PORTAL_Y, 476, 650],
                  [Classes.platforms.FLOOR7, 546, 490],
                  [Classes.platforms.SPIKE_UP, 520, 490],
                  [Classes.platforms.SPRING, 750, 464],
                  [Classes.platforms.SPIKE_DOWN, 750, 48],
                  [Classes.platforms.SPIKE_DOWN, 820, 48],
                  [Classes.platforms.MINE, 820, 477],
                  [Classes.platforms.MINE, 890, 477],
                  [Classes.platforms.MINE, 960, 477],
                  [Classes.platforms.BOOST, 1172, 650],
                  [Classes.platforms.SPIKE_UP, 1428, 650],
                  [Classes.platforms.SPIKE_UP, 1468, 650],
                  [Classes.platforms.BOOST, 1549, 650],
                  [Classes.platforms.SPIKE_UP, 1700, 650],
                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_17(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],


                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.BOOST, 406, 650],
                  [Classes.platforms.BOOST, 800, 650],
                  [Classes.platforms.BOOST, 1200, 650],
                  [Classes.platforms.BOOST, 1270, 650],
                  [Classes.platforms.BOOST, 1340, 650],
                  [Classes.platforms.FLOOR7, 476, 350],
                  [Classes.platforms.FLOOR7, 952, 350],
                  [Classes.platforms.FLOOR7, 1428, 350],


                  [Classes.platforms.BOOST, 1340, 350],
                  [Classes.platforms.SPIKE_UP, 1420, 350],
                  [Classes.platforms.SPIKE_UP, 1480, 350],
                  [Classes.platforms.SPIKE_UP, 1530, 350],
                  [Classes.platforms.SPIKE_UP, 1000, 350],
                  [Classes.platforms.SPIKE_UP, 930, 350],
                  [Classes.platforms.SPRING, 1100, 325],
                  [Classes.platforms.SPRING, 1650, 325],
                  [Classes.platforms.SPRING, 900, 325],
                  [Classes.platforms.SPRING, 120, 625],
                  [Classes.platforms.SPIKE_DOWN, 1000, 48],
                  [Classes.platforms.SPIKE_DOWN, 940, 48],
                  [Classes.platforms.SPIKE_DOWN, 1070, 48],
                  [Classes.platforms.SPIKE_DOWN, 1140, 48],
                  [Classes.platforms.SPIKE_DOWN, 1210, 48],
                  [Classes.platforms.SPIKE_DOWN, 1250, 48],
                  [Classes.platforms.SPIKE_UP, 640, 350],
                  [Classes.platforms.SPIKE_UP, 580, 350],
                  [Classes.platforms.SPIKE_UP, 510, 350],
                  [Classes.platforms.BLOCK, 720, 350],
                  [Classes.platforms.BLOCK, 750, 350],
                  [Classes.platforms.BLOCK, 195, 350],
                  [Classes.platforms.BLOCK, 265, 350],
                  [Classes.platforms.BLOCK, 335, 350],
                  [Classes.platforms.SPIKE_DOWN, 1770, 48],
                  [Classes.platforms.SPIKE_DOWN, 1700, 48],

                  [Classes.platforms.FINISH, 1770, 350],
                  ]

        self.checkBlock(level)

class Level_18(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  #toit
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.PORTAL_Y, 476, 650],
                  [Classes.platforms.PORTAL_Y, 1428, 650],
                  [Classes.platforms.PORTAL_B, 952, 48],
                  [Classes.platforms.SPRING, 485, 98],
                  [Classes.platforms.SPIKE_DOWN, 546, 118],
                  [Classes.platforms.SPIKE_DOWN, 616, 118],
                  [Classes.platforms.SPIKE_DOWN, 686, 118],
                  [Classes.platforms.SPIKE_DOWN, 746, 118],
                  [Classes.platforms.SPIKE_DOWN, 816, 118],
                  [Classes.platforms.SPIKE_DOWN, 846, 118],
                  [Classes.platforms.SPRING, 1438, 98],
                  [Classes.platforms.SPIKE_DOWN, 1492, 118],
                  [Classes.platforms.SPIKE_DOWN, 1562, 118],
                  [Classes.platforms.SPIKE_DOWN, 1632, 118],
                  [Classes.platforms.SPIKE_DOWN, 1682, 118],
                  [Classes.platforms.SPRING, 980, 625],
                  [Classes.platforms.SPIKE_UP, 1022, 580],
                  [Classes.platforms.SPIKE_UP, 1092, 580],
                  [Classes.platforms.SPIKE_UP, 1162, 580],
                  [Classes.platforms.SPIKE_UP, 1232, 580],
                  [Classes.platforms.SPIKE_UP, 1302, 580],
                  [Classes.platforms.SPIKE_UP, 1342, 580],

                  [Classes.platforms.FINISH, 1770, 48],

                  ]

        self.checkBlock(level)

class Level_19(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],
                  [Classes.platforms.FLOOR7, 952, 48],
                  [Classes.platforms.FLOOR7, 1428, 48],

                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.BLOCK, 476, 650],
                  [Classes.platforms.SPRING, 496, 625],
                  [Classes.platforms.FLOOR7, 620, 350],
                  [Classes.platforms.SPIKE_UP, 620, 350],
                  [Classes.platforms.MINE, 800, 337],
                  [Classes.platforms.MINE, 850, 337],
                  [Classes.platforms.MINE, 920, 337],
                  [Classes.platforms.SPRING, 1500, 625],

                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)

class Level_20(Level):
    # Tutorial's creation
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("Images/background_00.png").convert()
        self.level_limit = -2500

        level = [ #sol
                  [Classes.platforms.FLOOR7, 0, 650],
                  [Classes.platforms.FLOOR7, 476, 650],
                  [Classes.platforms.FLOOR7, 952, 650],
                  [Classes.platforms.FLOOR7, 1428, 650],
                  #toit
                  [Classes.platforms.FLOOR7, 0, 48],
                  [Classes.platforms.FLOOR7, 476, 48],


                  [Classes.platforms.WALL, 55, 118],
                  [Classes.platforms.WALL, 55, 260],
                  [Classes.platforms.WALL, 55, 368],
                  [Classes.platforms.WALL, 55, 510],
                  [Classes.platforms.WALL, 1835, 118],
                  [Classes.platforms.WALL, 1835, 260],
                  [Classes.platforms.WALL, 1835, 368],
                  [Classes.platforms.WALL, 1835, 510],
                  [Classes.platforms.PORTAL_Y, 1120, 650],
                  [Classes.platforms.MINE, 600, 637],
                  [Classes.platforms.MINE, 670, 637],
                  [Classes.platforms.SPRING, 800, 625],
                  [Classes.platforms.SPIKE_UP, 900, 650],
                  [Classes.platforms.SPIKE_UP, 970, 650],
                  [Classes.platforms.SPIKE_UP, 1020, 650],
                  [Classes.platforms.SPIKE_UP, 1220, 650],
                  [Classes.platforms.SPIKE_UP, 1290, 650],
                  [Classes.platforms.SPIKE_UP, 1320, 650],
                  [Classes.platforms.PORTAL_B, 1700, 48],
                  [Classes.platforms.BLOCK, 1125, 48],
                  [Classes.platforms.BLOCK, 1195, 48],
                  [Classes.platforms.SPRING, 1225, 118],

                  [Classes.platforms.FINISH, 1770, 650],
                  ]

        self.checkBlock(level)
