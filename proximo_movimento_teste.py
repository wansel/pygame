# -*- coding:utf-8 -*-
from random import randint

def proximoMovimento(x,y):
	return (randint(x-1,x+1), randint(y-1,y+1))

inicio = 10
for i in range(10):
	print proximoMovimento(inicio,inicio) 