import pygame
import time
import random
firstValue = pygame.init()
print(firstValue)

# Defining Colors
White = (255, 255, 255)
Red = (255, 0, 0)
Black = (0, 0, 0)

Message = "*MY FIRST SNAKE GAME*"
screenWidth = 500
screenHight = 500
GameWindow = pygame.display.set_mode((screenWidth, screenHight))

Score = 0

food_x = random.randint(0, screenWidth/2)
food_y = random.randint(0, screenWidth/2)
snake_x = 40
snake_y = 30
snake_Size = 10
snake_Velocity_X = 0
snake_Velocity_Y = 0

pygame.display.set_caption(Message)
GameWindow.fill(White)
pygame.display.update()
speed = 5

exit_Game = False
gameOver = False

fps = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color , x, y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, [x, y])
    pass
# Creating game loop
while not exit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_Game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("You are pressing Down Arrow key")
                snake_Velocity_Y += speed
                snake_Velocity_X = 0

            if event.key == pygame.K_UP:
                print("You are pressing Up Arrow key")
                snake_Velocity_Y -= speed
                snake_Velocity_X = 0

            if event.key == pygame.K_LEFT:
                print("You are pressing Left Arrow key")
                snake_Velocity_X -= speed
                snake_Velocity_Y = 0
                GameWindow.fill(White)

                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                print("You are pressing Right Arrow key")
                snake_Velocity_X += speed
                snake_Velocity_Y = 0
                GameWindow.fill(White)
        snake_x += snake_Velocity_X
        snake_y += snake_Velocity_Y

        if abs((snake_x-food_x)) < 10 and abs((snake_y-food_y)) < 10:
            Score += 10
            food_x = random.randint(0, screenWidth/2)
            food_y = random.randint(0, screenHight/2)
            text_screen("Score: " + str(Score), Red, 5, 5)

        pygame.draw.rect(GameWindow, Black, [snake_x, snake_y, snake_Size, snake_Size])
        pygame.draw.rect(GameWindow, Red, [food_x, food_y, snake_Size, snake_Size])
        pygame.display.update()
        clock.tick(fps)
        pygame.display.update()

        message("You Lost", Red)
        pygame.display.update()
        time.sleep(2)

pygame.quit()
quit()

