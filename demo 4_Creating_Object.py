import pygame
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

snake_x = 40
snake_y = 30
snake_Size = 10

pygame.display.set_caption(Message)
GameWindow.fill(White)
pygame.display.update()


exit_Game = False
gameOver = False

fps = 30
clock = pygame.time.Clock()

while not exit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_Game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("You are pressing Down Arrow key")
                snake_y += 5
            if event.key == pygame.K_UP:
                print("You are pressing Up Arrow key")
                snake_y -= 5
            if event.key == pygame.K_LEFT:
                print("You are pressing Left Arrow key")
                GameWindow.fill(White)
                snake_x -= 5
                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                print("You are pressing Right Arrow key")
                GameWindow.fill(White)
                snake_x += 5
        pygame.draw.rect(GameWindow, Black, [snake_x, snake_y, snake_Size, snake_Size])
        pygame.display.update()
        clock.tick(fps)
        pygame.display.update()
pygame.quit()
quit()

