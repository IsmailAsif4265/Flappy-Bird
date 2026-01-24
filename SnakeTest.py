import pygame
x=pygame.init()

#colors
white= (255, 255, 255)
red= (255, 0 , 0)
green= (0, 255, 0)
blue=(0, 0, 255)
black=(0, 0, 0)

#Screen Properties
screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game Test")
pygame.display.update()

#Game Specific Variables
exit_game=False
game_over=False

#Game Loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            exit_game=True

    gameWindow.fill(white)
    pygame.display.update()
        