# -*- coding: utf-8 -*-
from pygame.locals import *
from tela import *
import os
import pygame

class Texto:
	
	#self.surface = pygame.font.Font(caminho, tamanho)
	#self.texto = fonte.render(mensagem, True, (255,255,255))
	def __init__(self, mensagem, tamanho, cor, posicao):
		self.xPos = 0
		self.yPos = 0
		self.tamanho = tamanho
		self.cor = cor
		caminho = os.path.join("fonte", "duckhunt.ttf")
		self.fonte = pygame.font.Font(caminho, 32)
		self.surface = self.fonte.render(mensagem, True, cor)

	def setPositionInTime(x,y, tempo):
		if(time>10 and time<15):
			pass
		elif(time>5):
			pass
		elif (time>0):
			pass
	def update(self,string):
		self.surface = self.fonte.render(string, True, self.cor)
	def setPosition(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos


