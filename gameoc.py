import pygame
import random
firstValue = pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
print(firstValue)
# reading window
speed = 4
screen_width = 1200
screen_hight = 600
screen_caption = "Snack Game"
Gamewindow = pygame.display.set_mode((600, 600))
pygame.display.set_caption("*My First Snake Game*")
exit_Game = False
gameOver = False
while 1:
    print("Gaming is on...")