import pygame, sys, os, time, random
from pygame.locals import *


screen=pygame.display.set_mode((1280,600),0,0)
caminho = os.path.join("images", "sky.png")
ceu = pygame.image.load(caminho).convert_alpha()

caminho = os.path.join("images", "mira.png")
mira = pygame.image.load(caminho).convert_alpha()

pygame.init()
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(ceu, (0,0))

    x,y = pygame.mouse.get_pos()
    x -= mira.get_width()/2
    y -= mira.get_height()/2

    screen.blit(mira,(x,y))

    pygame.display.update()
