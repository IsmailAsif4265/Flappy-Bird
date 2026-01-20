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
        print(event)
        if event.type == pygame.QUIT:
            exit_game=True

pygame.quit()
quit()