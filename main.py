import pygame
import Classes.levels
import Classes.constants
from Classes.player import Player

def main():
    pygame.init()

    # Set the resolution
    size = [Classes.constants.SCREEN_WIDTH, Classes.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Paspal OP")

    #init player
    player = Player()

    #create levels
    level_list = []
    level_list.append(Classes.levels.Level_0(player))

    #Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = Classes.constants.SCREEN_HEIGHT - player.rect.height - 118
    active_sprite_list.add(player)

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
