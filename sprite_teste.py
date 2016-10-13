# -*- coding: utf-8 -*-
import pygame, sys, os, time, random
from pygame.locals import *

#importando random para gerar algumas variáveis
from random import randint

#importando a classe "Pato"
from classes.tela import *
from classes.pato import *
from classes.objeto import *

#Cores
branco = (255, 255, 255)


#Iniciando o PyGame
pygame.init()


tela = Tela()
#definindo a resolução da tela
janela = pygame.display.set_mode(tela.getSize())
#tela = Tela()
#Definindo o plano de fundo do jogo
caminho = os.path.join("imagens", "stage_01.png")
fundo = pygame.image.load(caminho).convert_alpha()
patos = []
patoA = Pato()
patos.append(patoA)
janela.fill(branco)


running = True
while running:
	for evento in pygame.event.get():
		if (evento.type == QUIT):
			running = False	
	'''if (evento.type == pygame.MOUSEBUTTONDOWN):
		novoPato = Pato()
		patos.append(novoPato)
	if (evento.type == pygame.MOUSEBUTTONUP):
		novoPato = Pato()
		patos.append(novoPato)
	if (evento.type == pygame.KEYDOWN):
		novoPato = Pato()
		patos.append(novoPato)
	pygame.display.flip()'''
	janela.blit(fundo, (0, 0))
	for x in patos:
		aux2 = x.movimentar(tela)
		janela.blit(x.aux, aux2)
    #janela.blit(patoA.aux, patoA.movimentar(Tela))
	pygame.display.flip()
    #novoPato = None
    

pygame.display.quit()
sys.exit()
