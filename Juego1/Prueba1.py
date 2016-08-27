import pygame 
import sys 

#Colors
white = (255,255,255)
red = (200,20,50)
blue = (70,70,190)
green = (124, 252, 0)
brown = (210, 180, 140)


class jugador(object):
	"""Clase que define todo conrespecto al jugador 
	   su inicializacion, coliciones y movimiento"""
	J = pygame.image.load("pacman.png")
	spriteJ = pygame.sprite.Sprite()
	def __init__(self, x, y, screen):
		#super(jugador, self).__init__()
		self.spriteJ.image = self.J
		self.spriteJ.rect = self.J.get_rect()
		self.spriteJ.rect.top, self.spriteJ.rect.left = y, x
		screen.blit(self.spriteJ.image,self.spriteJ.rect)

	def movimiento(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.spriteJ.rect.move_ip(-10,0)

		if keys[pygame.K_RIGHT]:
			self.spriteJ.rect.move_ip(10,0)

		if keys[pygame.K_DOWN]:
			self.spriteJ.rect.move_ip(0,10)

		if keys[pygame.K_UP]:
			self.spriteJ.rect.move_ip(0,-10)			


class fondo(object):
	"""Clase que define un elemento del fondo del
	   juego, aqui se define la imagen del elemento,
	   su ubicacion y se realiza su rectangulo de 
	   colision"""
	def __init__(self, x, y, tipo = 1):
		super(fondo, self).__init__()
		if tipo == 1 :
			T = pygame.image.load("V.png")
		else:
			T = pygame.image.load("H.png")
		spriteF = pygame.sprite.Sprite()
		spriteF.image = T
		spriteF.rect = T.get_rect()
		spriteF.rect.top, spriteF.rect.left = y, x

		
class enemigos(object):
	"""Clase que define los enemigos del juego,
	   por el momento todos son inguales"""
	def __init__(self, x,y):
		super(enemigos, self).__init__()
		E = pygame.image.load("fantasma.png")
		spriteE = pygame.sprite.Sprite()
		spriteE.image = E
		spriteE.rect = E.get_rect()
		spriteE.rect.top, spriteE.rect.left = y, x
		
		

def main():
	global white, red, blue, green, brown
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((400,300))
	pygame.display.set_caption('Ejemplo IA videoGames')
	watch1 = pygame.time.Clock()
	DISPLAYSURF.fill(white)

	jugador1 = jugador(100,100,DISPLAYSURF)

	while True:
		jugador1.movimiento()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		watch1.tick(20)
		pygame.display.update()


main()

