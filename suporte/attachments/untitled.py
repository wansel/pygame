#-*- coding: latin1 -*- 
import pygame, sys, os, time, random 
from pygame.locals import * 

clock = pygame.time.Clock()
running = True 
pygame.init() 
screen = pygame.display.set_mode((1280, 600)) 
 
###### imagens ######
caminho = os.path.join("images", "sky.png") 
ceu = pygame.image.load(caminho).convert_alpha() 
 
caminho = os.path.join("images", "mira.png")
mira = pygame.image.load(caminho).convert_alpha()

caminho = os.path.join("images", "sprite_2.png")
sprite_pato = pygame.image.load(caminho).convert_alpha()

######
pygame.display.set_caption("Duck Hunt") 
     
parede = 1 
teto = 1     
 
musica = pygame.mixer.music 
musica.load("errou.mp3") 
 
segurar = False 
pygame.mouse.set_visible(False)

## PATO ##
x2 = 430
y2 = 500
a = 0
b = 0
larg = 79
alt = 60
frame = 0.0

def duck():
  global a, frame

  if frame >= 1.0:
    a += 85
    frame - 0.0

  frame += 0.1

  if a >= (85 * 3):
    a = 0
  
  screen.blit(sprite_pato, (x2, y2), (a, b, larg, alt))



while running: 
    global running
    #clock.tick(60)
    for event in pygame.event.get(): 
        if (event.type == QUIT): 
            running = False 
            pygame.quit()
            sys.exit()
        if (event.type == pygame.MOUSEBUTTONDOWN): 
            segurar = True 
        if (event.type == pygame.MOUSEBUTTONUP): 
            segurar = False 
 
    if(x2 < 0): 
        parede = 1 
    elif(x2 > 1237): 
        parede = -1 
    if(y2 < 0): 
      teto = 1 
    elif(y2 > 500): 
      teto = -1 
   
    x2 += parede 
    y2 += teto   
    screen.blit(ceu, (0, 0)) 
    duck()
  
    w,z = pygame.mouse.get_pos()
    w -= mira.get_width()/2
    z -= mira.get_height()/2 

    screen.blit(mira, (w, z))
     
    pygame.display.update()
 
    if segurar:
      musica.play()
 
    
pygame.display.quit()