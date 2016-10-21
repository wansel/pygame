# -*- coding: utf-8 -*-
import pygame, sys, os, time, random
from pygame.locals import *
from classes.tela import *


class Sprite:
	def __init__(self):
		self.x_pos = 50
		self.y_pos = 50
		self.width = 50
		self.height = 50

		pass


pygame.init()
tela = Tela()
janela = pygame.display.set_mode(tela.getSize())

caminho = os.path.join("imagens", "stage_01.png")
fundo = pygame.image.load(caminho).convert_alpha()

caminho = os.path.join("sprites", "sprite.png")
pato = pygame.image.load(caminho).convert_alpha()



#pato = pygame.image.load("sprites/sprite.png").convert_alpha()
print pato
running = True
x = Sprite()
while running:
	#clock.tick(60) #dentro do loop
	for event in pygame.event.get():
		
		if (event.type == pygame.KEYDOWN):
			pygame.transform.flip(pato, True, True)
		if (event.type == QUIT):
			running = False
	janela.blit(fundo, (0, 0))

	janela.blit(pato, (100,100), (82, 246, 66, 40))
	
	#pygame.transform.flip(pato, True, False)
	pygame.display.flip()
