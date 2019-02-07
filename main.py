import pygame
import Classes.levels
import Classes.constants
from Classes.inputBox import InputBox
from Classes.player import Player
from Classes.levels import Level_0
import random
from operator import itemgetter
from time import time


def createRandomNum(list_no):
    return list_no[random.randrange(1, len(list_no), 1)]

def selectRandomLevel(player, list_no, noLevel):
    level_list = []
    level = "level_list.append(Classes.levels.Level_" + str(noLevel) + "(player))"
    exec(level)
    return level_list[0]

def generateLevel(player, level):
    player.level = level
    player.rect.x = Classes.constants.levelStart_x
    player.rect.y = Classes.constants.levelStart_y
    level.__init__(player)

def launchMusic():
    pygame.mixer.music.load("Musiques/Level_music.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

def generateClasssement():
    classement = []
    file = open("classement.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        phrase = line.split(" ")
        classement.append([phrase[0],int(phrase[1][0:-1])])

    return classement

def printScore(screen, player):
    font = pygame.font.SysFont("comicsansms", 32)
    background = pygame.image.load("Images/score.jpg").convert()
    score = font.render(str(player.score), True, (255,255,255))
    screen.blit(background, (0,0))
    screen.blit(score, (360, 440))

def ajouterScore(player, text):
    if str(text) == "":
        player.pseudo="Unknow"
    else:
        player.pseudo = str(text)
    file = open("classement.txt", "a")
    file.write("{} {}".format(player.pseudo, player.score))
    file.close()

def printClassement(screen, classement):
    background = pygame.image.load("Images/classement.jpg").convert()
    screen.blit(background, (0,0))
    classement.sort(key = itemgetter(1), reverse = True)
    for i in range(0,5):
        font = pygame.font.SysFont("PHOSPHATE", 40)
        pseudo = font.render(classement[i][0], True, (255, 255, 0))
        score = font.render(str(classement[i][1]), True, (255, 255, 0))
        screen.blit(pseudo, (370, 290 + (93 * i)))
        screen.blit(score, (690, 290 + (93 *i)))

def main():
    pygame.init()

    # Set the resolution
    size = [Classes.constants.SCREEN_WIDTH, Classes.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Galactik Hold Up")

    #init player
    player = Player()

    done = False

    isMusic = True

    inputBox = InputBox(360, 600, 325, 40)

    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Impact', 40)

    launchMusic()

    #Game Loop
    while not done:

        counter, text = 180, '180'.rjust(3)

        accueil = pygame.image.load("Images/accueil.jpg").convert()
        screen.blit(accueil, (0,0))
        soundoff = pygame.image.load("Images/soundoff.png").convert_alpha()
        screen.blit(soundoff, (30,30))
        soundoff = pygame.image.load("Images/soundon.png").convert_alpha()
        screen.blit(soundoff, (120,30))

        pygame.display.flip()

        continuer_accueil = 1
        continuer_jeu = 0
        continuer_classement = 0
        continuer_credits = 0
        continuer_score = 0

        while continuer_accueil:
            player.score = 0
            player.multiplicateur = 1

            for event in pygame.event.get():

                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    continuer_accueil = 0
                    continuer_jeu = 0
                    done = True
                    choix = 0

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        continuer_accueil = 0
                        continuer_jeu = 1
                        choix = "tuto"

                    elif event.key == pygame.K_F2:
                        continuer_accueil = 0
                        continuer_jeu = 1
                        choix = "ramdom"

                    elif event.key == pygame.K_F3:
                        continuer_accueil = 0
                        continuer_classement = 1
                        choix = "classement"

                    elif event.key == pygame.K_F4:
                        continuer_accueil = 0
                        continuer_credits = 1
                        choix = "credits"

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 94 and event.pos[1] > 30 and event.pos[0] < 94 and event.pos[0] > 30:
                    if isMusic:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.play(-1)
                    isMusic = not isMusic


                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 94 and event.pos[1] > 30 and event.pos[0] < 184 and event.pos[0] > 120:
                    pygame.mixer.music.unpause()


        if choix != 0:
            if choix == "tuto":
                current_level = Classes.levels.Level_0(player)
                active_sprite_list = pygame.sprite.Group()
                generateLevel(player, current_level)
                active_sprite_list.add(player)

            elif choix == 'ramdom':
                list_no = []
                for i in range(1, Classes.constants.nbLevel+1):
                    list_no.append(i)
                noLevel = createRandomNum(list_no)
                current_level = selectRandomLevel(player, list_no, noLevel)
                active_sprite_list = pygame.sprite.Group()
                generateLevel(player, current_level)
                active_sprite_list.add(player)

            elif choix == "classement":
                classement = generateClasssement()

            elif choix == "credits":
                credits = pygame.image.load("Images/Credits.jpg").convert()
                screen.blit(credits, (0,0))

        while continuer_classement:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                          continuer_classement = 0
                          continuer_accueil = 1
                if event.type == pygame.QUIT:
                    done = True
                    continuer_classement = 0

            printClassement(screen, classement)
            pygame.display.flip()

        while continuer_credits:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                          continuer_credits = 0
                          continuer_accueil = 1
                if event.type == pygame.QUIT:
                    done = True
                    continuer_credits = 0
            pygame.display.flip()

        while continuer_jeu:

            print(player.gravity)

            score = "Score : " + format(player.score)
            multiplicateur = "Multiplicateur : x" + format(player.multiplicateur)

            for event in pygame.event.get():

                if event.type == pygame.USEREVENT:
                    if type(current_level) != Level_0:
                        counter -= 1
                        text = "Timer : " + str(counter).rjust(3)
                        if counter == 15:
                            son = pygame.mixer.Sound("Musiques/minuteur.wav")
                            son.play()
                        elif counter <= 0:
                            son = pygame.mixer.Sound("Musiques/temps.wav")
                            son.play()
                            continuer_jeu = 0
                            choix = 0
                            continuer_score = 1

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
                    if (type(player.level) != Level_0):
                        noLevel = createRandomNum(list_no)
                        current_level = selectRandomLevel(player, list_no, noLevel)
                        player.pos = Classes.constants.levelStart_x
                        generateLevel(player, current_level)
                    else:
                        generateLevel(player, current_level)


                if event.type == Classes.constants.BOOST:
                    player.go_boost()

                if event.type == Classes.constants.FINISH:
                    if (type(player.level) != Level_0):
                        list_no.remove(noLevel)
                        noLevel = createRandomNum(list_no)
                        current_level = selectRandomLevel(player, list_no, noLevel)
                        player.pos = Classes.constants.levelStart_x
                        generateLevel(player, current_level)
                    else :
                        continuer_accueil = 1
                        continuer_jeu = 0

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

            if type(current_level) != Level_0:
                screen.blit(font.render(text, True, (255, 255, 255)), (10, 0))
                screen.blit(font.render(score, True, (255, 255, 255)), (380, 0))
                screen.blit(font.render(multiplicateur, True, (255, 255, 255)), (720, 0))

            pygame.display.flip()

        while continuer_score:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    continuer_score = 0
                    ajouterScore(player, inputBox.text)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continuer_score = 0
                        ajouterScore(player, inputBox.text)

            inputBox.handle_event(event)
            printScore(screen, player)
            inputBox.update()
            inputBox.draw(screen)
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
