# -*- coding: utf-8 -*-
import pygame, sys, os, time, random
from pygame.locals import *

#importando random para gerar algumas variáveis
from random import randint

#importando a classe "Pato"
from classes.pato import *
from classes.objeto import *

#Cores
branco = (255, 255, 255)


#Iniciando o PyGame
pygame.init()

#definindo a resolução da tela
janela = pygame.display.set_mode((1280, 600))

#Definindo o plano de fundo do jogo
caminho = os.path.join("imagens", "stage_01.png")
fundo = pygame.image.load(caminho).convert_alpha()
patoA = Pato()
janela.fill(branco)


running = True
while running:
    for evento in pygame.event.get():
        if (evento.type == QUIT):
	    	running = False
	if (evento.type == pygame.MOUSEBUTTONDOWN):
		pass
	if (evento.type == pygame.MOUSEBUTTONUP):
	  	pass
	janela.blit(fundo, (0, 0))
    janela.blit(patoA.aux, patoA.movimentar())
    pygame.display.flip()

pygame.display.quit()
sys.exit()
