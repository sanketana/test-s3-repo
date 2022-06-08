import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Hello World')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill((255, 255, 255))

	pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

	pygame.display.update()