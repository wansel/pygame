# -*- coding: utf-8 -*-
from pygame.locals import *
import pygame, os
from classes.tela import *

#Cores
branco = (255,255,255)
preto = (0,0,0)

pygame.init()
pygame.display.set_caption('Font test')

tela = Tela()
janela = pygame.display.set_mode(tela.getSize())

caminho = os.path.join("fonte", "duckhunt.ttf")
font_path = 'data/coders_crux.ttf'