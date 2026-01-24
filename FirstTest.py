import pygame

x=pygame.init()

#Creating Window
gameWindow=pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

#Necessary Variables
exit_game=False
game_over=False

#Game Loop
while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("You have pressed the Right Key") 
            if event.key==pygame.K_LEFT:
                print("You have pressed the Left Key") 
            if event.key==pygame.K_UP:
                print("You have pressed the Up Key") 
            if event.key==pygame.K_DOWN:
                print("You have pressed the Down Key") 


pygame.quit()
quit()