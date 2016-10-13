# -*- coding: utf-8 -*-
#from pygame.locals import *
from random import randint
from objeto import *
from classes import *
#Inicia o PyGame
#pygame.init()
lvl_velocidade = 3
lvl_tamanho = 100

class Pato:
	velocidade = None
	tamanho = None
	ponto_de_vida = None
	cor = None
	x_pos = randint(0,)
	y_pos = None
	aux = None
	'''imagem = Objeto("pato_exemplo.png")'''

	def __init__(self):
		self.velocidade = lvl_velocidade * randint(1,3)
		self.cor = 0
		self.ponto_de_vida = 1 #Número de balas que o pato precisará para morrer
		self.tamanho = lvl_tamanho * float(randint(7,13)/float(10))
		#posição do pato
		self.x_pos = randint(0,600)
		self.y_pos = 0
		caminho = os.path.join("imagens", "pato_exemplo.png")
		self.aux = pygame.image.load(caminho).convert_alpha()
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
		if(self.x_pos<tela.width):
			self.x_pos += velocidade
		else:
			self.x_pos += (velocidade * -1)
		if(self.y_pos<tela.height):
			self.y_pos += velocidade
		else:
			self.y_pos += (velocidade * -1)
	return (self.x_pos, self.y_pos)


'''
#instanciação dos patos teste
patoA = Pato(lvl_velocidade, 0, 1, lvl_tamanho)
patoB = Pato(lvl_velocidade, 0, 1, lvl_tamanho)
patoC = Pato(lvl_velocidade, 0, 1, lvl_tamanho)

#verificação dos atributos dos patos
print patoA.velocidade
print patoA.tamanho
print patoB.cor
print "x=",patoA.x_pos,"  y=",patoA.y_pos

print patoB.velocidade
print patoB.tamanho
print patoB.cor
print "x=",patoB.x_pos,"  y=",patoB.y_pos

print patoC.velocidade
print patoC.tamanho
print patoC.cor
print "x=",patoC.x_pos,"  y=",patoC.y_pos
'''
