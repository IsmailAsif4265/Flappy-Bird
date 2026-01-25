import pygame
import random
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
temp_w=screen_width//2
temp_h=screen_height//2
gameWindow=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game Test")
pygame.display.update()

#Game Specific Variables
exit_game=False
game_over=False
snake_x=45
snake_y=55
snake_size=10
velocity_x=0
velocity_y=0
init_velocity=5
fps=30
clock=pygame.time.Clock()
font=pygame.font.SysFont(None, 55)
food_x=random.randint(20, temp_w)
food_y=random.randint(20, temp_h)
score=0
pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


def textScreen(text, color, x, y):
    screen_text=font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

#Game Loop
while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x+=init_velocity
                velocity_y=0

            if event.key==pygame.K_LEFT:
                velocity_x-=init_velocity
                velocity_y=0

            if event.key==pygame.K_DOWN:
                velocity_y+=init_velocity
                velocity_x=0

            if event.key==pygame.K_UP:
                velocity_y-=init_velocity
                velocity_x=0

    snake_x+=velocity_x
    snake_y+=velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=1
        print("Score:", score)
        food_x=random.randint(20, temp_w)
        food_y=random.randint(20, temp_h)

    gameWindow.fill(white)
    textScreen("Score:"+str(score), red, 5, 5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
        