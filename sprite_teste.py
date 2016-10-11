# -*- coding: utf-8 -*-
#from pygame.locals import *

#importando random para gerar algumas variáveis
from random import randint

#importando a classe "Pato"
from classes.pato import *

#Inicia o PyGame
pygame.init()

patoA = Pato(lvl_velocidade, 0, 1, lvl_tamanho)
patoB = Pato(lvl_velocidade, 0, 1, lvl_tamanho)
patoC = Pato(lvl_velocidade, 0, 1, lvl_tamanho)

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

