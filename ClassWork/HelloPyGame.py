import pygame
import sys

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Hello World')

pygame.init()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	

	pygame.display.update()