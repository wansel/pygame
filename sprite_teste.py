# -*- coding: utf-8 -*-
#from pygame.locals import *
from random import randint
#Inicia o PyGame
#pygame.init()
lvl_velocidade = 3
lvl_tamanho = 100

class Pato:
	#velocidade
	#tamanho
	#ponto_de_vida
	#cor
	def __init__(self,velocidade, cor, ponto_de_vida, tamanho):
		self.velocidade = lvl_velocidade * randint(1,3)
		self.cor = 0
		self.ponto_de_vida = 1
		self.tamanho = lvl_tamanho * float(randint(7,13)/float(10))
	def getVelocidade():
		return self.velocidade
	def stringVelocidade():
		return "Pato tem {} de velocidade".format(self.getVelocidade)

patoA = Pato(lvl_velocidade, 0, 1, lvl_tamanho)
patoB = Pato(lvl_velocidade, 0, 1, lvl_tamanho)
patoC = Pato(lvl_velocidade, 0, 1, lvl_tamanho)

print patoA.velocidade
print patoA.tamanho
print patoA.cor

print patoB.velocidade
print patoB.tamanho
print patoB.cor

print patoC.velocidade
print patoC.tamanho
print patoC.cor

