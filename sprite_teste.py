# -*- coding: utf-8 -*-
#import pygame, sys, os, time, random
from pygame.locals import *
from random import randint
from classes.mira import *
from classes.tela import *
from classes.pato import *
from classes.objeto import *
from classes.texto import *

#Cores
branco = (255, 255, 255)
preto = (0,0,0)
#Iniciando o PyGame
#pygame.time.set_timer(USEREVENT + 1, 1000)

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption('Duck Hunt')

tela = Tela()
janela = pygame.display.set_mode(tela.getSize())
mira = Mira()

#Definindo o plano de fundo do jogo
caminho = os.path.join("imagens", "stage_01.png")
fundo = pygame.image.load(caminho).convert_alpha()
patos = []

janela.fill(branco)

musica1 = pygame.mixer.music 
shot = pygame.mixer.music
caminho = os.path.join("sons", "errou.mp3")
musica1.load(caminho) 
caminho = os.path.join("sons", "sniper.mp3")
shot.load(caminho) 
tick = 0
segundo = 0
passo = 180
clock = pygame.time.Clock()
click = False
running = True
mousePositionX = 0
mousePositionY = 0

pontuacao = 10
textoInicial = Texto("Mate os patos ate atingir 100pts",32,branco,(100,100))
score = Texto("{}pt".format(pontuacao), 22, branco,(10,tela.getHeight()-40))
aviso = Texto("",32, branco, (0,0))
acertou = False
anima = 0
#incrementar a velocidade do pato a cada tiro?
patosNaTela = Texto("", 22, branco, (0,0))
while running:
	clock.tick(80) #dentro do loop
	for event in pygame.event.get():
		if (event.type == pygame.KEYDOWN):
			patos.append(Pato())
		if (event.type == QUIT):
			running = False
		if (event.type == pygame.MOUSEBUTTONDOWN):
			click = True
			mousePositionX,mousePositionY = pygame.mouse.get_pos()
	janela.blit(fundo, (0, 0))
	anima += 1
	tick+=1
	segundo = int(tick/float(60))
	if(segundo<5):
		aviso.update("A cada pato derrubado: +5pt")
	elif(segundo>=5 and segundo<=10):
		aviso.update("Tiro errado: -3pt")
		aviso.setPosition(tela.getWidth()/2-aviso.surface.get_width()/2 ,tela.getHeight()/2-aviso.surface.get_height()/2)
	elif(segundo>10 and segundo<=14):
		aviso.update("Chegue aos 100pt")
	elif(segundo>14):
		aviso = None
	if(tick%300==0):
		patos.append(Pato())
		tick==0
		print "passo{}".format(passo)
	if(click):
		shot.play
		for x in patos:
			#Se clicou na área do pato e pato não foi 'hitado':
			if(x.area(mousePositionX,mousePositionY) and x.hit == False):
				#mate o pato
				x.kill()
				print len(patos)
				#acertou = true
				pontuacao += 5
				#acertou = True
		if(click==True and acertou == False):
			pontuacao -= 3
		elif(click==True and acertou==True):
			#pontuacao += 5
			#acertou = False
			pass
		if(randint(0,1)==1):
			pass
			#musica1.play()
		click = False
		print "Errow"
		pontuacao -= 3
	score.update("{}pt".format(pontuacao))
	


	janela.blit(mira.aux, mira.atualizaPosicao(pygame.mouse.get_pos()))
	if(tick%60==0):
		print tick/60
	for x in patos:
		if(x.y_pos<=610):
			janela.blit(x.surface, x.movimentar(tela), x.nextSprite(anima))
			pygame.transform.flip(x.surface, True, False)
		else:
			patos.remove(x)
	patosNaTela.update("{} patos".format(len(patos)))
	janela.blit(patosNaTela.surface, (10,10))
	janela.blit(score.surface, (10,tela.getHeight()-score.surface.get_height()-5))
	#janela.blit(texto, (50,(tela.getHeight())-20))
	janela.blit(textoInicial.surface, (tela.getWidth()/2-texto2.surface.get_width()-2,tela.getHeight()/2))
	#janela.blit(patoA.aux, patoA.movimentar(Tela))
	pygame.display.set_caption('Duck Hunt - {}'.format(segundo))
	if(anima>=60):
		anima = 0
	pygame.display.flip()
	#novoPato = None

pygame.mixer.music.stop() 
pygame.display.quit()
sys.exit()