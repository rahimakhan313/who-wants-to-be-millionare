import pygame
import time
import Tectonicsq1,Tectonicsq3,Tectonicsq4 , Tectonicsq5, Tectonicsq6, Tectonicsq7, Tectonicsq8, Tectonicsq9, Tectonicsq10
import Tectonicsq11, Tectonicsq12, Tectonicsq13, Tectonicsq14, Tectonicsq15, Tectonicsq16 , Tectonicsq17, Tectonicsq18, Tectonicsq19, Tectonicsq20
import Tectonicsq21, Tectonicsq22, Tectonicsq23, Tectonicsq24, Tectonicsq25, Tectonicsq26, Tectonicsq27, Tectonicsq28, Tectonicsq29, Tectonicsq30

def q1():
    pygame.init()
    display_width = 600
    display_height = 400
    bg = pygame.image.load('audiance1.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)
    def button(msg, x, y, w, h, ic,ac , action='None'):
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

        
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq1.q1)
    
                pygame.display.update()
                clock.tick(15)
    game_loop()
    pygame.quit()
    quit()
def q2():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance2.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()

    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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

   
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq2.q2)
    
                pygame.display.update()
                clock.tick(15)
     
    
   
    game_loop()
    pygame.quit()
    quit()
def q3():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance3.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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

    
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq3.q3)
    
                pygame.display.update()
                clock.tick(15)
              
    
    game_loop()
    pygame.quit()
    quit()                        
def q4():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance4.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq4.q4)
    
                pygame.display.update()
                clock.tick(15)        
    
    game_loop()
    pygame.quit()
    quit()
def q5():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance5.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
             
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq5.q5)
    
                pygame.display.update()
                clock.tick(15)        
    
            
  
    game_loop()
    pygame.quit()
    quit()
def q6():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance6.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq6.q6)
    
                pygame.display.update()
                clock.tick(15)        
    
    
    game_loop()
    pygame.quit()
    quit()
def q7():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance7.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq7.q7)
    
                pygame.display.update()
                clock.tick(15)          
   
    game_loop()
    pygame.quit()
    quit()
def q8():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance8.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq8.q8)
    
                pygame.display.update()
                clock.tick(15)             
    
    game_loop()
    pygame.quit()
    quit()
def q9():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance9.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq9.q9)
    
                pygame.display.update()
                clock.tick(15)        
   
    game_loop()
    pygame.quit()
    quit()
def q10():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance10.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq10.q10)
    
                pygame.display.update()
                clock.tick(15)        
            
    game_loop()
    pygame.quit()
    quit()
def q11():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance1.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
             
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
 
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq11.q11)
    
                pygame.display.update()
                clock.tick(15)        
    
    game_loop()
    pygame.quit()
    quit()
                
def q12():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance2.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq12.q12)
    
                pygame.display.update()
                clock.tick(15)        
    
            
    game_loop()
    pygame.quit()
    quit()
def q13():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance3.jpg')
    x=0
    t=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq13.q13)
    
                pygame.display.update()
                clock.tick(15)        
            
    
    game_loop()
    pygame.quit()
    quit()
def q14():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance4.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq14.q14)
    
                pygame.display.update()
                clock.tick(15)        
            
    
            
    game_loop()
    pygame.quit()
    quit()
def q15():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance5.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq15.q15)
    
                pygame.display.update()
                clock.tick(15)         
    game_loop()
    pygame.quit()
    quit()
def q16():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance6.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

        
    def button(msg, x, y, w, h, ic,ac , action='None'):
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
        
    
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq16.q16)
    
                pygame.display.update()
                clock.tick(15)           
    
    
    game_loop()
    pygame.quit()
    quit()
def q17():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance7.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq17.q17)
    
                pygame.display.update()
                clock.tick(15)           
    
    game_loop()
    pygame.quit()
    quit()
def q18():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance8.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq18.q18)
    
                pygame.display.update()
                clock.tick(15)        
    game_loop()
    pygame.quit()
    quit()
def q19():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance9.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

        
    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq19.q19)
    
                pygame.display.update()
                clock.tick(15)        
            
    
    game_loop()
    pygame.quit()
    quit()
def q20():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance10.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq20.q20)
    
                pygame.display.update()
                clock.tick(15)        
            
    
            
    game_loop()
    pygame.quit()
    quit()
def q21():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance1.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq21.q21)
    
                pygame.display.update()
                clock.tick(15)        
            
    
            
            
    game_loop()
    pygame.quit()
    quit()
  
def q22():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance2.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq22.q22)
    
                pygame.display.update()
                clock.tick(15)        
                
    game_loop()
    pygame.quit()
    quit()
def q23():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance3.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq23.q23)
    
                pygame.display.update()
                clock.tick(15)        
    game_loop()
    pygame.quit()
    quit()
def q24():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance4.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
        
    
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq24.q24)
    
                pygame.display.update()
                clock.tick(15)        
    game_loop()
    pygame.quit()
    quit()
def q25():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance5.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq25.q25)
    
                pygame.display.update()
                clock.tick(15)        
            
    game_loop()
    pygame.quit()
    quit()
def q26():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance6.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
        
    
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq26.q26)
    
                pygame.display.update()
                clock.tick(15)        
            
           
    game_loop()
    pygame.quit()
    quit()
def q27():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance7.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq27.q27)
    
                pygame.display.update()
                clock.tick(15)        
            
    game_loop()
    pygame.quit()
    quit()
def q28():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance8.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    
        
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq28.q28)
    
                pygame.display.update()
                clock.tick(15)        
    game_loop()
    pygame.quit()
    quit()
def q29():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance9.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq29.q29)
    
                pygame.display.update()
                clock.tick(15)        
            
    game_loop()
    pygame.quit()
    quit()
def q30():
    pygame.init()
    display_width = 600
    display_height = 400
    bg=pygame.image.load('audiance10.jpg')
    x=0
    y=0

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('who wants to be millionaire')

    black = (0,0,0)
    white = (255,255,255)
    golden = (234 , 215 , 83)
    red = (249, 152, 138)
    green = (118, 255, 122)
    clock = pygame.time.Clock()
    def img(x,y):
            gameDisplay.blit(bg , (x, y))
            
    def text_objects(text, font):
            textSurface = font.render(text, True, black)
            return textSurface, textSurface.get_rect()
         
    def message_display(text):
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(text, largeText)
            TextRect.center = (250,230)
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)

    def button(msg, x, y, w, h, ic,ac , action='None'):
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
    
    def game_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    pass
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                img(x , y)
                largeText = pygame.font.Font('freesansbold.ttf',70)
                TextSurf, TextRect = text_objects(" ", largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)        
                button('Back',180 , 300 , 200 , 60 , golden , green ,Tectonicsq30.q30)
    
                pygame.display.update()
                clock.tick(15)        
            
            
    
    game_loop()
    pygame.quit()
    quit()
