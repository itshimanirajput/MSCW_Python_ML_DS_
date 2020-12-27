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
pygame.display.set_caption(Message)
GameWindow.fill(White)
pygame.display.update()


exit_Game = False
gameOver = False

while not exit_Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_Game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("You are pressing Left Arrow key")
                GameWindow.fill(Red)
                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                print("You are pressing Right Arrow key")
                GameWindow.fill(White)
                pygame.display.update()
pygame.quit()
quit()


