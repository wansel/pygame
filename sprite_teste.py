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
#pygame.time.set_timer(USEREVENT + 1, 1000)

pygame.init()
pygame.display.set_caption('Duck Hunt')

tela = Tela()
#definindo a resolução da tela
janela = pygame.display.set_mode(tela.getSize())
#tela = Tela()
#Definindo o plano de fundo do jogo
caminho = os.path.join("imagens", "stage_01.png")
fundo = pygame.image.load(caminho).convert_alpha()
patos = []
#patoA = Pato()
#patos.append(patoA)
janela.fill(branco)

seconds = 0
running = True
while running:
	for event in pygame.event.get():
		if(pygame.time.set_timer(1, 1000)):
			patos.append(Pato())
		if (event.type == pygame.KEYDOWN):
			novoPato = Pato()
			patos.append(novoPato)
		if (event.type == QUIT):
			running = False	
		if event.type == USEREVENT + 1:
			seconds+=1
	janela.blit(fundo, (0, 0))
	for x in patos:
		aux2 = x.movimentar(tela)
		janela.blit(x.aux, aux2)
		print seconds
    #janela.blit(patoA.aux, patoA.movimentar(Tela))
	pygame.display.flip()
    #novoPato = None
    

pygame.display.quit()
sys.exit()
