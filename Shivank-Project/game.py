import time, pygame, sys, random
from pygame.locals import *

FPS = 50
windowwidth = 640
windowheight = 480
cellsize = 20
assert windowwidth % cellsize == 0
assert windowheight & cellsize == 0
cellwidth = int(windowwidth / cellsize)
cellheigth = int(windowheight / cellsize)



def main():
	global FPSCLOCK, displaysurf, lives

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	lives = 1
	displaysurf = pygame.display.set_mode((windowwidth, windowheight))
	pygame.display.set_caption("Space Invaders")
	start_screen() 
	
	running = True
	global startx,starty,alienlist,bullets
	alienlist = []
	bullets = []
	startx = 320
	starty = 460

	while running:
	

		draw_bullets(bullets)
		 


		move_alien()
		
		for event in pygame.event.get():

			if event.type == QUIT:
				running = False

			if event.type == KEYDOWN:

				if event.key == K_RETURN:
					draw_grid()
					
					draw_turret (startx,starty)

					draw_alien()
					

				if event.key == K_SPACE: 
					generate_bullet(bullets)
				
			key = pygame.key.get_pressed()

			if key[pygame.K_LEFT] or key[pygame.K_a]:
				startx -= 5
				draw_turret(startx,starty)

			if key[pygame.K_d] or key[pygame.K_RIGHT]:
				startx += 5
				draw_turret(startx,starty)


def kill_alien():
	for i in range(len(alienlist)):
		alienx = alienlist[i][0]
		alieny = alienlist[i][1]
		for j in range(len(bullets)):
			bulletx = bullets[j][0]
			bullety = bullets[j][1]
			if alienx == bulletx:
				if alieny == bullety:
					rect = pygame.Rect(alienx,alieny,30,30)
					pygame.draw.rect(displaysurf,"black",rect)
					rect2 = pygame.Rect(bulletx,bullety,10,20)
					pygame.draw.rect(displaysurf,"black",rect2)
					pygame.display.update()


def move_alien():
	if len(alienlist) != 0:
		#
		draw_turret(startx,starty)
		count = -1
		for coord in alienlist:
			count = count+1
			var = coord[1]
			coord[1] = var+0.1
			if var == 460:
				alienlist.pop(count)
			

			rect = pygame.Rect(coord[0],coord[1],30,30)
			
			pygame.draw.rect(displaysurf,"green",rect)

		pygame.display.update()			 


					
def draw_alien():
	aliens =  random.randint(1,8)
	xlist = [90,150,210,270,330,390,450,510]
	for i in range(aliens):
		rect = pygame.Rect(xlist[i],40,30,30)
		alienlist.append([xlist[i],40])
		pygame.draw.rect(displaysurf,"green",rect)
	pygame.display.update()

def draw_bullets(bullets):
	if len(bullets) != 0:
		# displaysurf.fill("black")
		draw_turret(startx,starty)
		draw_alien
		count = -1
		for coord in bullets:
			count = count+1
			var = coord[1]
			coord[1] = var-1
			if var == 0:
				bullets.pop(count)
			
			
			rect = pygame.Rect(coord[0]+5,coord[1],10,20)
			
			pygame.draw.rect(displaysurf,"red",rect)

		pygame.display.update()			 


def start_screen():
	displaysurf.fill("black")

	img = pygame.image.load("alien (1).png")
	img = pygame.transform.scale(img, (250,250))
	img_rect = img.get_rect()
	img_rect.center = (320, 190)
	displaysurf.blit(img, img_rect)

	titleFont = pygame.font.Font("freesansbold.ttf", 32)
	titleSurf1 = titleFont.render("Press enter to play", True, "purple")
	titleSurf2 = titleFont.render("Earthling...", True, "purple")
	Rect1 = titleSurf1.get_rect()
	Rect2 = titleSurf2.get_rect()
	Rect1.center = (windowwidth / 2, (windowheight / 2) + 100)
	Rect2.center = (windowwidth / 2, (windowheight / 2) + 150)
	displaysurf.blit(titleSurf1,Rect1)
	displaysurf.blit(titleSurf2,Rect2)
	
	pygame.display.update()

def draw_grid():
	displaysurf.fill("black")
	for x in range(0,windowwidth,cellsize):
		pygame.draw.line(displaysurf,"grey",(x,0),(x,windowheight))
	for y in range(0,windowheight,cellsize):
		pygame.draw.line(displaysurf,"grey",(0,y),(windowwidth,y))
	pygame.display.update()

def draw_turret(startx,starty):
	global turretcoords

	turretcoords = [(startx,starty),(startx-20,starty),(startx,starty-20), (startx+20,starty)]

	displaysurf.fill("black")
	for coord in turretcoords:

		x = coord[0]
		y = coord[1]
		rect = pygame.Rect(x,y,cellsize,cellsize)
		pygame.draw.rect(displaysurf,"white",rect)
		
	pygame.display.update()

def generate_bullet(bullets):
	displaysurf.fill("black")
	bullets.append([startx,415])
	rect = pygame.Rect(startx,415,10,20)
	pygame.draw.rect(displaysurf,"red",rect)
	pygame.display.update()

main()