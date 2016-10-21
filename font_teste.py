# -*- coding: utf-8 -*-
from pygame.locals import *
import pygame, os, sys
from classes.tela import *

#Cores
branco = (255,255,255)
preto = (0,0,0)

pygame.init()
pygame.display.set_caption('Font test')

tela = Tela()
janela = pygame.display.set_mode(tela.getSize())

caminho = os.path.join("fonte", "duckhunt.ttf")
fonte = pygame.font.Font(caminho, 32)

texto = fonte.render("Teste", True, (255,255,255))
#tela.blit(texto, (X, Y))
running = True
while running:
	for event in pygame.event.get():
		if (event.type == QUIT):
			running = False
	janela.blit(texto, (50,50))
	pygame.display.flip()
    #novoPato = None
    

pygame.display.quit()
sys.exit()