# -*- coding: utf-8 -*-
#import pygame, sys, os, time, random
from pygame.locals import *
from random import randint
from classes.mira import *
#importando a classe "Pato"
from classes.tela import *
from classes.pato import *
from classes.objeto import *

#Cores
branco = (255, 255, 255)

#Iniciando o PyGame
#pygame.time.set_timer(USEREVENT + 1, 1000)

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption('Duck Hunt')

tela = Tela()
#definindo a resolução da tela
janela = pygame.display.set_mode(tela.getSize())
mira = Mira()
#tela = Tela()
#Definindo o plano de fundo do jogo
caminho = os.path.join("imagens", "stage_01.png")
fundo = pygame.image.load(caminho).convert_alpha()
patos = []
#patoA = Pato()
#patos.append(patoA)
janela.fill(branco)

seconds = 0
clock = pygame.time.Clock()

running = True
while running:
	clock.tick(60) #dentro do loop
	for event in pygame.event.get():
		if (event.type == pygame.KEYDOWN):
			novoPato = Pato()
			patos.append(novoPato)
		if (event.type == QUIT):
			running = False
		if event.type == USEREVENT + 1:
			seconds+=1
	janela.blit(fundo, (0, 0))
	janela.blit(mira.aux, mira.atualizaPosicao(pygame.mouse.get_pos()))
	print seconds
	for x in patos:
		aux2 = x.movimentar(tela)
		janela.blit(x.aux, (50,50), (82, 246, 66, 40))
	pygame.display.flip()


pygame.display.quit()
sys.exit()
