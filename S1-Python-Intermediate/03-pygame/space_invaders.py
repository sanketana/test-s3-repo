import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))

# Add the player sprite
backgroundImg = pygame.image.load('backdrop.jpg')
playerImg = pygame.image.load('player.png')
enemyImg = pygame.image.load('enemy.png')

playerX = 400
playerY = 510
playerX_change = 0

enemyX = random.randint(0, 735)
enemyY = random.randint(20, 300)
enemyX_change = 3
enemyY_change = 0

while True:
    # Fetch list of events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RIGHT):
            playerX_change = 3
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT):
            playerX_change = -3
        if (event.type == pygame.KEYUP) and (event.key == pygame.K_LEFT):
            playerX_change = 0
        if (event.type == pygame.KEYUP) and (event.key == pygame.K_RIGHT):
            playerX_change = 0

    playerX = playerX + playerX_change
    enemyX = enemyX + enemyX_change

    screen.blit(backgroundImg, (0, 0))
    screen.blit(playerImg, (playerX, playerY))
    screen.blit(enemyImg, (enemyX, enemyY))

    # Update display window
    pygame.display.update()
