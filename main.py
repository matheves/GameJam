import pygame
import Classes.levels
import Classes.constants
from Classes.player import Player
import random

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

    #Set the current level
    current_level = selectRandomLevel(player)

    active_sprite_list = pygame.sprite.Group()
    generateLevel(player, current_level)
    active_sprite_list.add(player)
#test
    done = False

    clock = pygame.time.Clock()

    #Game Loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
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
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
