import pygame
import random
firstValue = pygame.init()
print(firstValue)

# Defining Colors
White = (255, 255, 255)
Red = (255, 0, 0)
Black = (0, 0, 0)

Message = "*****MY FIRST SNAKE GAME*****"
screenWidth = 500
screenHight = 500

Gamewindow = pygame.display.set_mode((screenWidth, screenHight))
pygame.display.update()

Score = 0

food_x = random.randint(0, screenWidth/2)
food_y = random.randint(0, screenWidth/2)
snake_x = 40
snake_y = 30
snake_Size = 10
snake_Velocity_X = 0
snake_Velocity_Y = 0
speed = 5
pygame.display.set_caption(Message)
Gamewindow.fill(White)

exit_Game = False
gameOver = False
fps = 30
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    Gamewindow.blit(screen_text, [x, y])
    pass


while not exit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         exit_Game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake_Velocity_Y += 10
                snake_Velocity_X = 0

                if event.key == pygame.K_UP:
                    snake_Velocity_Y -= 10
                    snake_Velocity_X = 0

            if event.key == pygame.K_LEFT:
                snake_Velocity_X -= 10
                snake_Velocity_Y = 0
                snake_x -= 5
                pygame.display.update()

                if event.key == pygame.K_RIGHT:
                    snake_Velocity_X += 10
                    snake_Velocity_Y = 0
                    snake_x += 5
                    snake_x += snake_Velocity_X
                    snake_y += snake_Velocity_Y

                    if abs((snake_x-food_x)) < 10 and abs((snake_y-food_y)) < 10:
                        Score += 10
                        food_x = random.randint(0, screenWidth/2)
                        food_y = random.randint(0, screenHight/2)
                        text_screen("Score: " + str(Score), Red, 5, 5)

                    Gamewindow.fill(White)
        pygame.draw.rect(Gamewindow, Black, [snake_x, snake_y, snake_Size, snake_Size])
        pygame.draw.rect(Gamewindow, Red, [food_x, food_y, snake_Size, snake_Size])

        pygame.display.update()
        clock.tick(fps)

pygame.quit()
quit()