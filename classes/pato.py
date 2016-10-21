# -*- coding: utf-8 -*-
from pygame.locals import *
import pygame, sys, os, time, random
from random import randint
from objeto import *
from tela import *
#from classes import *

#Inicia o PyGame
#pygame.init()
lvl_velocidade = 3
lvl_tamanho = 100

class Pato:
	patoSprite = [(82, 246, 66, 40),(82, 246, 66, 40),(82, 246, 66, 40)]
	sprite = 0
	def __init__(self):
		self.velocidade = 3 * randint(1,3)
		self.cor = 0
		self.ponto_de_vida = 1 #Número de balas que o pato precisará para morrer
		self.tamanho = lvl_tamanho * float(randint(7,13)/float(10))
		#posição do pato
		self.x_pos = randint(0+66,1280-48)
		self.y_pos = 600
		caminho = os.path.join("sprites", "sprite.png")
		self.surface = pygame.image.load(caminho).convert_alpha()
		self.xFly = lvl_velocidade
		self.yFly = lvl_velocidade
		self.xNext = 0
		self.yNext = 0
		self.cor = randint(0,2)
		self.hit = False

	def getPosicao(self):
		return (self.x_pos, self.y_pos)
	def getVelocidade(self):
		return self.velocidade
	def stringVelocidade(self):
		return "Pato tem {} de velocidade".format(self.getVelocidade)
	def area(self,x,y):
		if(x>self.x_pos-(66/2) and x<self.x_pos+(66/2) and y>self.y_pos-(40/2) and y<self.y_pos+(40/2)):
			return True
		else:
			return False


	def nextSprite(self, tempo):
		#print self.x_pos
		#print self.y_pos
		tolerancia = 9 #quando o nível de avanço para  que o sprite mude?
		#x++
		##if(x1>x2 and y1>y2+tolerancia):
		if(self.hit == False):
			if(self.cor==0 and tempo<60):
				return (82, 246, 66, 40) #(82, 246, 66, 40),(82, 246, 66, 40)
			elif(self.cor==0 and 60<=tempo<=120):
				return (82, 246, 66, 40)
			elif(self.cor==0 and 120<tempo<=180):
				return (82, 246, 66, 40)
			if(self.cor==1):
				return (262, 242, 66, 48)
			else:
				return (522, 242, 66, 48)
		else:
			return (6, 476, 54, 58)
		#if(x1>x2)
		#[82, 246, 66, 40],[82, 246, 66, 40],[82, 246, 66, 40]
		#y++
		#[82, 246, 66, 40],[82, 246, 66, 40],[82, 246, 66, 40]
		#x++, y++
		#[82, 246, 66, 40],[82, 246, 66, 40],[82, 246, 66, 40]
	def movimentar(self, tela):
		#especifica o tamanho do pato (com as bordas da imagem).
		#se não estiver tocando na borda, então movimente, se tocar na aborda, mude a direção.
		#aumente o contador para tirar o pato da tela.
		
		#comportamentos do voo do pato
		move = randint(0,400)
		'''
		if(move==15):
			self.xFly *= -1
		elif(move==20):
			self.yFly *= -1
		elif(move==25):
			self.xFly *= -1
			self.yFly *= -1
		elif(move==30):
			self.xFly += lvl_velocidade
		elif(move==35):
			self.yFly += lvl_velocidade
		elif(move==40):
			self.xFly += lvl_velocidade
			self.yFly += lvl_velocidade
		'''
		if(self.hit==False):
			if(self.x_pos<=0):
				self.xFly = lvl_velocidade
			elif(self.x_pos>=tela.width-15):
				self.xFly = (lvl_velocidade * -1)
				
			if(self.y_pos<=0):
				self.yFly = lvl_velocidade  * randint(1,2)
			elif(self.y_pos>=tela.height-15):
				self.yFly = (lvl_velocidade * -1) * randint(1,2)
				pygame.transform.flip(self.surface, False, True)
			self.x_pos += self.xFly
			self.y_pos += self.yFly
			return (self.x_pos, self.y_pos)
		else:
			if(self.yFly<0):
				self.yFly*= -1
			self.yFly == 30
			self.y_pos += self.yFly
			return (self.x_pos, self.y_pos)

	def kill(self):
		self.hit = True
