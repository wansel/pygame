# -*- coding: utf-8 -*-

#Padrão Singleton na tela, para garatir que exista apenas uma instância da mesma
class Tela:
	width = 1280
	height = 600
	def __init__(self):
		pass
	def getSize(self):
		return (self.width, self.height)
	def getWidth():
		return self.width
	def getHeight():
		return self.height