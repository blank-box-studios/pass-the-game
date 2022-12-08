import pygame
from sys import exit

pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
GAME_TITLE = "Pass the game"

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the game
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()


surface = pygame.Surface((50, 50))
# set the color of the surface to white
player = pygame.image.load("assets/player.png")
x = 0
y = 0

x_speed = 0
y_speed = 0

# Find a good way to set up the game loop

# Loop until the user clicks the close button.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
            if event.type == pygame.K_SPACE: # TODO: Figure out how to make this work
                x = 0
                y = 0
    
    #draw the surface onto the screen
    x += x_speed
    y += y_speed
    screen.blit(player, (x , y ))

    pygame.display.update()


    # Limit to 60 frames per second - TODO: Not sure how this works
    # https://stackoverflow.com/questions/34383559/pygame-clock-tick-vs-framerate-in-game-main-loop
    clock.tick(60)


    #Unfinished player class
    #TODO: Refactor player movement into player class
    class Player:
        def __init__(self, x, y):
            # Random player image from https://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/b7d1a56ea265a5a.png
            player = pygame.image.load("assets/player.png")
            self.x = x
            self.y = y
