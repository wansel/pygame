# -*- coding: utf-8 -*-
#from pygame.locals import *
from random import randint
from objeto import *
from tela import *
#from classes import *
#Inicia o PyGame
#pygame.init()
lvl_velocidade = 1
lvl_tamanho = 100


class Pato:
	#velocidade = None # recurso não implementado
	#tamanho = None #recurso não implementado
	#ponto_de_vida = None #recurso não implementado
	#cor = None #recurso não implementado
	#x_pos = randint(0,1280) #posição do pato no eixo x
	#y_pos = 600 #posição do pato no eixo y
	#xFly = lvl_velocidade # variável que controla a direção do pato
	#yFly = lvl_velocidade # variável que controla a direção do pato no eixo X
	#aux = None
	'''imagem = Objeto("pato_exemplo.png")'''

	def __init__(self):
		self.velocidade = lvl_velocidade * randint(1,3)
		self.cor = 0
		self.ponto_de_vida = 1 #Número de balas que o pato precisará para morrer
		self.tamanho = lvl_tamanho * float(randint(7,13)/float(10))
		#posição do pato
		self.x_pos = randint(0,1280)
		self.y_pos = 600
		caminho = os.path.join("imagens", "pato_exemplo.png")
		self.aux = pygame.image.load(caminho).convert_alpha()
		self.xFly = lvl_velocidade
		self.yFly = lvl_velocidade
		#caminho = os.path.join("imagens", "pato_exemplo.png")
		#pato = pygame.image.load(caminho).convert_alpha()

	'''def __init__(self ,velocidade, cor, ponto_de_vida, tamanho):
		self.velocidade = velocidade * randint(1,3)
		self.cor = cor
		self.ponto_de_vida = ponto_de_vida #Número de balas que o pato precisará para morrer
		self.tamanho = tamanho * float(randint(7,13)/float(10))
		#posição do pato
		self.x_pos = randint(0,600)
		self.y_pos = 0'''
	def getVelocidade():
		return self.velocidade
	def stringVelocidade():
		return "Pato tem {} de velocidade".format(self.getVelocidade)

	def movimentar(self, tela):
		#especifica o tamanho do pato (com as bordas da imagem).
		#se não estiver tocando na borda, então movimente, se tocar na aborda, mude a direção.
		#aumente o contador para tirar o pato da tela.
		move = randint(0,100)
		#if(move==15):
		#	self.xFly *= -1
		if(self.x_pos<=0):
			self.xFly = lvl_velocidade
		elif(self.x_pos>=tela.width):
			self.xFly = (lvl_velocidade * -1)
		if(self.y_pos<=0):
			self.yFly = lvl_velocidade
		elif(self.y_pos>=tela.height):
			self.yFly = (lvl_velocidade * -1)
		self.x_pos += self.xFly
		self.y_pos += self.yFly
		return (self.x_pos, self.y_pos)
'''
PatoA = Pato()
tela = Tela()

for x in range(700):
	print PatoA.movimentar(tela),

'''