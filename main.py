import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 600
# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((WIDTH, HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()