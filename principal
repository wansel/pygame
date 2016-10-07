#-*- coding: latin1 -*-
import pygame, sys, os, time, random
from pygame.locals import *

running = True
branco = (255, 255, 255)

clock = pygame.time.Clock()

#iniciando os modulos do pygame
pygame.init()

#definindo a resolução da tela
janela = pygame.display.set_mode((1280, 600))

#colocando o plano de fundo do jogo
caminho = os.path.join("images", "sky.png")
ceu = pygame.image.load(caminho).convert_alpha()

caminho = os.path.join("images", "duck1.gif")
pato = pygame.image.load(caminho).convert_alpha()

janela.fill(branco)
pygame.display.flip()

pygame.display.set_caption("Duck Hunt")
    
x = 640 #talvez editar os valores de x e y
y = 150
parede = 1
teto = 1    

musica = pygame.mixer.music
musica.load("shotgun.mp3")

segurar = False



while running:
    global running
    for event in pygame.event.get():
        if (event.type == QUIT):
	    running = False
	if (event.type == pygame.MOUSEBUTTONDOWN):
	    segurar = True
	if (event.type == pygame.MOUSEBUTTONUP):
	    segurar = False

    if(x < 0):
        parede = 1
    elif(x > 1237):
        parede = -1
    if(y < 0):
	    teto = 1
    elif(y > 500):
	    teto = -1
	
    x += parede
    y += teto	
    janela.blit(ceu, (0, 0))
    janela.blit(pato, (x, y))
    
    if segurar:
        musica.play()
    
    pygame.display.flip()

   
pygame.mixer.music.stop()
pygame.display.quit()
sys.exit()
