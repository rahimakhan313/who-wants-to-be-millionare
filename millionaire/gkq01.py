import pygame
import time
import webbrowser
import os
import gkq02
import graphgk
import file
import random
import g_score

def gkq01():
    pygame.init()
    display_width = 1200
    display_height = 700

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    gold = (250 , 246 , 139)

    clock = pygame.time.Clock()
    crashed = False
    bg = pygame.image.load('question_bg.png')
    x = 0
    y = 0

    def img(x,y):
        gameDisplay.blit(bg , (x, y))

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
     
    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf',70)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)

    def quit_game():
        pygame.quit()
        quit()


    def button(msg, x, y, w, h, ic,ac, action=None ):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

            if click [0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)
 
    def music():
        done = False
        a=["tick.mp3"]
        pygame.mixer.music.load(a[0])
        pygame.mixer.music.play()
    
    def play():
        pass

    def a():
                a='wrought iron'   #RA
                if a=='wrought iron':
                    button('  $ 10000  ',900 , 80 , 200 , 60 ,  golden , green,play )
                    gkq02.gkq02()
                else:
                    score.q1()
    def b():
                b='steel'
                if b=='iron':
                    button('  $ 10000  ',900 , 80 , 200 , 60 ,  golden , green,play )
                    gkq02.gkq02()
                else:
                    g_score.q1()
    def c():
                c='nickel steel'
                if c=='copper':
                    button('  $ 10000  ',900 , 80 , 200 , 60 ,  golden , green,play )
                    gkq02.gkq02()
                else:
                    g_score.q1()
    def d():
                d='pig iron'
                if d=='grass':
                    button('  $ 10000  ',900 , 80 , 200 , 60 ,  golden , green,play )
                    gkq02.gkq02()
                else:
                    g_score.q1()
    
    def game_intro():

        intro = True

        while intro:
            for event in pygame.event.get():
                pass
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            music()        
            img(x , y)
            largeText = pygame.font.Font('freesansbold.ttf',70)
            TextSurf, TextRect = text_objects(" ", largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)

            button('The purest form of iron is?',350 , 460 , 600 , 40 , golden , golden, play)
            button('A-  wrought iron ',170 , 550 , 300 , 30 ,  golden , green , a)
            button('B-  steel  ',800 , 550 , 300 , 30 ,  golden , green,b )
            button('D-  pig iron  ',800 , 615 , 300 , 30 ,  golden , green,d )
            button('C-  nickel steel  ',170 , 615 , 300 , 30 ,  golden , green ,c)
            button('  $ 0  ',900 , 80 , 200 , 60 ,  golden , golden,play )
            button('  CALL  ', 50 , 120 , 150 , 50 ,  golden , green,file.call)
            button('  AUDIENCE  ',50 , 50 , 150 , 50 ,  golden , green,graphgk.q1)  #left,up,length,width
            pygame.display.update()
            clock.tick(15)

    music()            
    game_intro()
    pygame.quit()
    quit()
