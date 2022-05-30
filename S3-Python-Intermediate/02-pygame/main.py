import pygame
import sys

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Importing player image
playerImg = pygame.image.load(
    '/Users/apple/Documents/Sanketana/PythonDev/S3-Python-Intermediate/02-pygame/player.png')


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(playerImg, (100, 100))
    pygame.display.update()
