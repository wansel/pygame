# -*- coding: utf-8

from pygame.locals import *
import os
import pygame

class Mira:
	def __init__(self):
		self.caminho = os.path.join("sprites", "mira.png")
		self.aux = pygame.image.load(self.caminho).convert_alpha()
		self.x = 0
		self.y = 0
		#x,y = pygame.mouse.get_pos()
		#x -= mira.get_width()/2
		#y -= mira.get_height()/2
	def atualizaPosicao(self, (x,y)):
		x-= self.aux.get_width()/2
		y-= self.aux.get_height()/2
		return (x,y)
