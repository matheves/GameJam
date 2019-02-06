import pygame
import Classes.levels
import Classes.constants
from Classes.player import Player
import random
from time import time


def selectRandomLevel(player):
    level_list = []
    k = random.randint(0, Classes.constants.nbLevel-1)
    level = "level_list.append(Classes.levels.Level_" + str(k) + "(player))"
    exec(level)
    return level_list[0]

def generateLevel(player, level):
    player.level = level
    player.rect.x = Classes.constants.levelStart_x
    player.rect.y = Classes.constants.levelStart_y
    level.__init__(player)

def main():
    pygame.init()

    # Set the resolution
    size = [Classes.constants.SCREEN_WIDTH, Classes.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Galactik Hold Up")

    #init player
    player = Player()

    #create levels
    #level_list = []
    #level_list.append(Classes.levels.Level_0(player))
    #level_list.append(Classes.levels.Level_1(player))
    #level_list.append(Classes.levels.Level_2(player))
    #level_list.append(Classes.levels.Level_3(player))
    #level_list.append(Classes.levels.Level_4(player))
    #level_list.append(Classes.levels.Level_5(player))
    #level_list.append(Classes.levels.Level_6(player))

    done = False

    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 60)

    #Game Loop
    while not done:

        counter, text = 180, '180'.rjust(3)

        accueil = pygame.image.load("Images/accueil.jpg").convert()
        screen.blit(accueil, (0,0))

        pygame.display.flip()

        continuer_accueil = 1
        continuer_jeu = 1

        while continuer_accueil:

            for event in pygame.event.get():

                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    continuer_accueil = 0
                    continuer_jeu = 0
                    done = True
                    choix = 0

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        continuer_accueil = 0
                        choix = "tuto"

                    elif event.key == pygame.K_F2:
                        continuer_accueil = 0
                        choix = "ramdom"

        if choix != 0:
            if choix == "tuto":
                current_level = Classes.levels.Level_0(player)
                active_sprite_list = pygame.sprite.Group()
                generateLevel(player, current_level)
                active_sprite_list.add(player)

            elif choix == 'ramdom':
                current_level = selectRandomLevel(player)
                active_sprite_list = pygame.sprite.Group()
                generateLevel(player, current_level)
                active_sprite_list.add(player)

        while continuer_jeu:


            for event in pygame.event.get():

                if event.type == pygame.USEREVENT:
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 0 else 'boom!'
                    if counter <= 0:
                        continuer_jeu = 0
                        choix = 0

                elif event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop
                    continuer_jeu = 0

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                       continuer_jeu = 0
                    elif event.key == pygame.K_LEFT:
                        player.go_left()
                    elif event.key == pygame.K_RIGHT:
                        player.go_right()
                    elif event.key == pygame.K_UP:
                        player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()

                if event.type == Classes.constants.SPRING:
                    player.springJump()

                if event.type == Classes.constants.ANTIGRAVITY:
                    player.changeGravity()

                if event.type == Classes.constants.DEATH:
                    current_level = selectRandomLevel(player)
                    player.pos = Classes.constants.levelStart_x
                    generateLevel(player, current_level)

                if event.type == Classes.constants.BOOST:
                    player.go_boost()


            # Update the player.
            active_sprite_list.update()

            # Update items in the level
            current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            if player.rect.x >= 500:
                diff = player.rect.x - 500
                player.rect.x = 500
                current_level.shift_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if player.rect.x <= 120:
                diff = 120 - player.rect.x
                player.rect.x = 120
                current_level.shift_world(diff)

            current_level.draw(screen)
            active_sprite_list.draw(screen)
            clock.tick(60)

            screen.blit(font.render(text, True, (255, 45, 0)), (32, 48))

            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
