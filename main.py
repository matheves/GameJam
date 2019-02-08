import pygame
import Classes.levels
import Classes.constants
from Classes.inputBox import InputBox
from Classes.player import Player
from Classes.levels import Level_0
import random
from operator import itemgetter
from time import time

#create a random number correspind to a level
def createRandomNum(list_no):
    return list_no[random.randrange(1, len(list_no), 1)]

#select a level with our random number
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

def launchMusic(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

#open the file classement.txt into a list of a list
def generateClasssement():
    classement = []
    file = open("classement.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        phrase = line.split(" ")
        classement.append([phrase[0],int(phrase[1])])

    return classement

#print the score at the end of the game
def printScore(screen, player):
    font = pygame.font.SysFont("PHOSPHATE", 50)
    background = pygame.image.load("Images/score.jpg").convert()
    score = font.render(str(player.score), True, (221,246,65))
    screen.blit(background, (0,0))
    screen.blit(score, (450, 430))

#add the score and pseudo in classement.txt
def ajouterScore(player, text):
    if str(text) == "":
        player.pseudo="Unknow"
    else:
        player.pseudo = str(text)
    file = open("classement.txt", "a")
    file.write("{} {} {}".format(player.pseudo, player.score, " \n"))
    file.close()

#print the classement when the player want to see it
def printClassement(screen, classement):
    background = pygame.image.load("Images/classement.jpg").convert()
    screen.blit(background, (0,0))
    classement.sort(key = itemgetter(1), reverse = True)
    for i in range(0,5):
        font = pygame.font.SysFont("PHOSPHATE", 40)
        pseudo = font.render(classement[i][0], True, (255, 255, 0))
        score = font.render(str(classement[i][1]), True, (255, 255, 0))
        screen.blit(pseudo, (370, 305 + (90 * i)))
        screen.blit(score, (690, 305 + (90 *i)))

#main function of the game
def main():
    pygame.init() #init pygame

    # Set the resolution
    size = [Classes.constants.SCREEN_WIDTH, Classes.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Galactik Hold Up")

    #init player
    player = Player()

    #boolean for the program loop
    done = False

    #boolean if music is enable or not
    isMusic = True

    #entry field for enter the pseudo
    inputBox = InputBox(500, 540, 310, 60)

    #game clock
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Impact', 40)

    #launch the menu music
    launchMusic("Musiques/menu_music.wav")

    #Game Loop
    while not done:

        #time counter of the game set on 3 minutes
        counter, text = 180, '180'.rjust(3)

        #load and put on the screen the accueil ressources
        accueil = pygame.image.load("Images/accueil.jpg").convert()
        screen.blit(accueil, (0,0))
        #load the music icon
        if isMusic:
            sound = pygame.image.load("Images/soundon.png").convert_alpha()
        else:
            sound = pygame.image.load("Images/soundoff.png").convert_alpha()

        #put the music icon on the screen
        screen.blit(sound, (30,30))

        #display the screen
        pygame.display.flip()

        #loop variables
        continuer_accueil = 1
        continuer_jeu = 0
        continuer_classement = 0
        continuer_credits = 0
        continuer_score = 0

        #accueil loop
        while continuer_accueil:
            player.score = 0
            player.multiplicateur = 1

            for event in pygame.event.get(): #check every event

                #Quit event
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    continuer_accueil = 0
                    continuer_jeu = 0
                    done = True
                    choix = 0

                #keyboard event
                elif event.type == pygame.KEYDOWN:
                    #F1 for launch the tuto
                    if event.key == pygame.K_F1:
                        continuer_accueil = 0
                        continuer_jeu = 1
                        choix = "tuto"
                        if isMusic:
                            launchMusic("Musiques/Level_music.wav") #launch the level music

                    #F2 for launch the game
                    elif event.key == pygame.K_F2:
                        continuer_accueil = 0
                        continuer_jeu = 1
                        choix = "ramdom"
                        if isMusic:
                            launchMusic("Musiques/Level_music.wav")

                    #F3 for launch the classement
                    elif event.key == pygame.K_F3:
                        continuer_accueil = 0
                        continuer_classement = 1
                        choix = "classement"

                    #F4 for launch the credits
                    elif event.key == pygame.K_F4:
                        continuer_accueil = 0
                        continuer_credits = 1
                        choix = "credits"

                #for disable/enable the music click on the music icon
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 94 and event.pos[1] > 30 and event.pos[0] < 94 and event.pos[0] > 30:
                    if isMusic:
                        pygame.mixer.music.pause()
                        sound = pygame.image.load("Images/soundoff.png").convert_alpha()
                    else:
                        pygame.mixer.music.play(-1)
                        sound = pygame.image.load("Images/soundon.png").convert_alpha()
                    isMusic = not isMusic #change the boolean for music
                    #refreh the display
                    screen.blit(accueil, (0,0))
                    screen.blit(sound, (30,30))
                    pygame.display.flip()

        if choix != 0:
            if choix == "tuto": #load the tuto
                current_level = Classes.levels.Level_0(player)
                active_sprite_list = pygame.sprite.Group()
                generateLevel(player, current_level)
                active_sprite_list.add(player)

            elif choix == 'ramdom': #launch the game
                #create a list containing all the level id
                list_no = []
                for i in range(1, Classes.constants.nbLevel+1):
                    list_no.append(i)

                noLevel = createRandomNum(list_no) #generate a random level id
                current_level = selectRandomLevel(player, list_no, noLevel) #select the random level
                active_sprite_list = pygame.sprite.Group() #create sprites list
                generateLevel(player, current_level) #generate the level
                active_sprite_list.add(player) #add the player to the sprites list

            #load the classement
            elif choix == "classement":
                classement = generateClasssement()

            #load the credits
            elif choix == "credits":
                credits = pygame.image.load("Images/Credits.jpg").convert()
                screen.blit(credits, (0,0))

        #classement loop
        while continuer_classement:
            for event in pygame.event.get(): #event management
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                          continuer_classement = 0
                          continuer_accueil = 1
                if event.type == pygame.QUIT:
                    done = True
                    continuer_classement = 0

            printClassement(screen, classement) #put classement element on the screen
            pygame.display.flip() #display the screen

        #credits loop
        while continuer_credits:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                          continuer_credits = 0
                          continuer_accueil = 1
                if event.type == pygame.QUIT:
                    done = True
                    continuer_credits = 0
            pygame.display.flip() #display credits

        #Game loop
        while continuer_jeu:

            #set variables for displaying score and multiplicateur
            score = "Score : " + format(player.score)
            multiplicateur = "Multiplicateur : x" + format(player.multiplicateur)

            for event in pygame.event.get(): #event management

                if event.type == pygame.USEREVENT: #event for managingthe time and update it
                    if type(current_level) != Level_0: #if we are not in the tuto level
                        counter -= 1
                        text = "Timer : " + str(counter).rjust(3) #variable for displaying lefting time
                        if counter == 15: #put a minuteur sound when 15 seconds left
                            son = pygame.mixer.Sound("Musiques/minuteur.wav")
                            son.play()
                        elif counter <= 0: #when the timer is over
                            son = pygame.mixer.Sound("Musiques/temps.wav")
                            son.play()
                            continuer_jeu = 0
                            choix = 0
                            continuer_score = 1

                elif event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop
                    continuer_jeu = 0

                elif event.type == pygame.KEYDOWN: #keyboard event
                    if event.key == pygame.K_ESCAPE: #return to the menu
                       continuer_jeu = 0
                       if isMusic:
                            launchMusic("Musiques/menu_music.wav")
                    elif event.key == pygame.K_LEFT:
                        player.go_left()
                    elif event.key == pygame.K_RIGHT:
                        player.go_right()
                    elif event.key == pygame.K_UP:
                        player.jump()

                #stop the player when the user don't move him
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()

                #when the player take a spring
                if event.type == Classes.constants.SPRING:
                    player.springJump()

                #when the player cross a gravity portal
                if event.type == Classes.constants.ANTIGRAVITY:
                    player.changeGravity()

                #when the player die
                if event.type == Classes.constants.DEATH:
                    if (type(player.level) != Level_0): #if it's not the tuto
                        #generate a new level
                        noLevel = createRandomNum(list_no)
                        current_level = selectRandomLevel(player, list_no, noLevel)
                        player.pos = Classes.constants.levelStart_x
                        generateLevel(player, current_level)
                    else: #if it's the tuto regenerate the tuto
                        generateLevel(player, current_level)

                #when the player take a boost
                if event.type == Classes.constants.BOOST:
                    player.go_boost()

                #when the player finish a level
                if event.type == Classes.constants.FINISH:
                    if (type(player.level) != Level_0): #if it's not the tuto
                        list_no.remove(noLevel) #remove this level from level id list
                        #generate a new level
                        noLevel = createRandomNum(list_no)
                        current_level = selectRandomLevel(player, list_no, noLevel)
                        player.pos = Classes.constants.levelStart_x
                        generateLevel(player, current_level)
                    else : #if it's the tuto back to the menu
                        continuer_accueil = 1
                        continuer_jeu = 0
                        if isMusic:
                            launchMusic("Musiques/menu_music.wav")

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

            #draw the modification on the screen
            current_level.draw(screen)
            active_sprite_list.draw(screen)
            clock.tick(60) #the game run in 60FPS

            if type(current_level) != Level_0: #if it's not the tuto update the game information(time, score and multiplicateur)
                screen.blit(font.render(text, True, (255, 255, 255)), (10, 0))
                screen.blit(font.render(score, True, (255, 255, 255)), (380, 0))
                screen.blit(font.render(multiplicateur, True, (255, 255, 255)), (720, 0))

            #display the screen
            pygame.display.flip()

        #score loop when the game is finish
        while continuer_score:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    continuer_score = 0
                    ajouterScore(player, inputBox.text) #add the score and the pseudo in classement.txt

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continuer_score = 0
                        ajouterScore(player, inputBox.text)
                        if isMusic:
                            launchMusic("Musiques/menu_music.wav")

                elif event.type == Classes.constants.ENTER_PSEUDO:
                    continuer_score = 0
                    ajouterScore(player, inputBox.text)
                    if isMusic:
                        launchMusic("Musiques/menu_music.wav")

                inputBox.handle_event(event) #manage event of the inputBox
            printScore(screen, player) #put the score on the screen
            #update and draw the input box
            inputBox.update()
            inputBox.draw(screen)
            #display screen
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
