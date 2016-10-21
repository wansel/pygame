# -*- coding: utf-8 -*-

#import pygame, sys, os, time, random
from pygame.locals import *
from random import randint
from mira import *
from tela import *
from pato import *
from objeto import *
#Classe manager
'''
responsável por todas as interações do jogo:

'''
class Manager:
	Manager = None
	nome = "Wansel"
	tela = Tela()
	objetos = []
	def __init__(self):
		pass

	def jogo():
		pygame.init()
		pygame.mouse.set_visible(False)
		pygame.display.set_caption('Duck Hunt')
		janela = pygame.display.set_mode(tela.getSize())
		mira = Mira()
		caminho = os.path.join("imagens", "stage_01.png")
		fundo = pygame.image.load(caminho).convert_alpha()
		objetos.append(fundo)
		patos = []
		janela.fill(branco)

		seconds = 0
		clock = pygame.time.Clock()

	def add(self,objeto):
		self.objetos.append(objeto)

	def new(self, string):
		if(string == "Pato"):
			novoPato = Pato()
			self.add(novoPato)
		else:
			pass