#enconding: UTF-8

import pygame, sys, os
import random
import math
import time

######################

# inicializa modulo da pygame (sempre tem que chamar)
pygame.init()
# inicializa modulo de audio (apenas se for usar sons)
pygame.mixer.init()

######################

# usado para definir uma taxa de fps
clock = pygame.time.Clock()
######################

# resolucao do nosso display: largura e altura
RESOLUCAO = (800, 600)
# criando janela e superficie
tela = pygame.display.set_mode(RESOLUCAO)


##### cores RGB ##########
BRANCO 	= (255, 255, 255)
ROSA	= (255, 170, 255)

		  
######## imagens ###########
# os.path.join p/ carregar o conteudo independente do Sistema operacional usado.
# aquele problema de \ ou / no sistema de diretorio
 
# convert p/ convert formato de pixel
# convert_alpha caso a imagem tenha transparencia

# imagem do asteroide
caminho = os.path.join("images", "bomber.png")
bomber = pygame.image.load(caminho).convert_alpha()

# imagem do espaco
caminho = os.path.join("images", "sky.jpg")
ceu = pygame.image.load(caminho).convert()

# imagem da nave (sprite sheet)
caminho = os.path.join("images", "nave.png")
sprite_sheet = pygame.image.load(caminho).convert()

# serve para ignorar a cor rosa (fundo da imagem)
sprite_sheet.set_colorkey(ROSA)

######### sons ############
# musica de fundo
caminho = os.path.join("sons", "trilha.ogg")
som = pygame.mixer.Sound(caminho)
som.set_volume(0.05)
# som de tiro
caminho = os.path.join("sons", "laser.wav")
laser = pygame.mixer.Sound(caminho)
laser.set_volume(0.1)


######## fontes ###########
# caminho da fonte e tamanho
caminho = os.path.join("fontes", "gta.ttf")
fonte	= pygame.font.Font(caminho, 32)
fonte2	= pygame.font.Font(caminho, 120)


###### colisao ########
# distancia euclidiana entre dois pontos
def distancia(x1, y1, x2, y2):
	distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	return distancia


########## Inimigo ###############

x	= 0
y 	= 0
criar 	= True
i_raio  = 22.5

def inimigo():
	global criar, y, x

	if criar:
		x = random.randint(20, 780) # posicao aleatoria entre 20 e 780
		y = 0
		criar = False

	# atingiu o final da tela	
	if y > 600:
		criar = True
	
	y += 2 # incrementa y para deslocar o asteroide
	
	# desenhar o asteroide na tela
	# ajustei o raio para desenhar na posicao correta
	tela.blit(bomber, (x - i_raio, y - i_raio))

######### Nave ##################

x2	= 430
y2	= 530
a	= 0 	# posicao x da janela em relacao a imagem
b	= 0 	# posicao y da janela em relacao a imagem
larg	= 93 	# largura da janela
alt	= 100	# altura da janela
frame	= 0.0
n_raio  = 50

vida 	= 3	# vida do jogador
pontos	= 0	# pontos do jogador

def nave():
	global x2, a, frame
	
	# lista de teclas pressionadas
	key = pygame.key.get_pressed()

	# verifica se foi seta esquerda	
	if key[pygame.K_LEFT]:
		x2 -= 5
	# verifica se foi seta direita
	elif key[pygame.K_RIGHT]:
		x2 += 5

	# apenas para atrasar a animacao da nave
	if frame >= 1.0:
		a += 95 # desloca a 'janela' p/ direita
		frame = 0.0

	frame += 0.1

	if a >= (95 * 2):
		a = 0
	
	# neste caso, uma parte da image sera desenhada, aquela onde a 'janela' estiver por cima
	# nome da imagem, (posicao), (posicao e tamanho) 
	tela.blit(sprite_sheet, (x2 - n_raio, y2 - n_raio), (a, b, larg, alt)) 


########## Tiro ################

x3	= 0
y3	= 0
t_raio	= 2.5
shot	= pygame.Surface((5, 5)) # tiro vai ser um quadrado de 5 x 5 pixels
shot	= shot.convert()
shot.fill(BRANCO)	# quadrado sera branco
pronto	= True

def tiro():
	global x3, y3, pronto

	if pronto:
		x3 = x2
		y3 = 470

	if y3 < 0:
		pronto = True

	# disparar se barra de espaco for pressionada
	key = pygame.key.get_pressed()
	if key[pygame.K_SPACE] and pronto:
		pronto = False
		laser.play(0) # executa som do tiro

	# desenhar o tiro
	if not pronto:
		tela.blit(shot, (x3 - t_raio, y3 - t_raio))
		y3 -= 6


def GUI():
	# texto a ser impresso + cor
	surface = fonte.render("Vida " + str(vida), True, BRANCO)
	tela.blit(surface, (10, 10))
	surface = fonte.render("Pontos " + str(pontos), True, BRANCO)
	tela.blit(surface, (10, 40))


# condicao do nosso loop
running = True

# condicao p/ executar trilha do jogo
audio = False

# loop principal do nosso jogo
while running:
	clock.tick(60) # taxa de fps

	# mostrar fps no titulo da janela
	pygame.display.set_caption('FPS %.2f' %(clock.get_fps()) )
	
	# executa trilha sonora
	if not audio:
		som.play(-1)
		audio = True

	# trata eventos
	for event in pygame.event.get():
		# evento de clicar no X da janela
		if event.type == pygame.QUIT:
			running = False

	
	# elementos desenhandos no jogo (atencao a ordem)	


	tela.blit(ceu, (0, 0)) # ceu

	nave()	# nave
	tiro()	# tiro
	inimigo() # asteroide


	GUI() # ponto e vida

	######## Colisoes #######
	# nave <-> inimigo	
	if distancia(x, y, x2, y2) < (i_raio + n_raio):
		vida -= 1
		criar = True

	# tiro <-> inimigo
	if distancia(x, y, x3, y3) < (i_raio + t_raio) and not pronto:
		criar = True
		pronto = True
		pontos += 1
		

	# game over
	if vida <= 0:
		surface = fonte2.render("Game Over!", True, BRANCO)
		tela.blit(surface, (200, 200))
		running = False
	

	# ao final, atualiza a tela
	pygame.display.update()


# aguardar 5 segundos antes de fechar o jogo
if vida < 1: time.sleep(5)	
pygame.display.quit() # fecha a janela
sys.exit() # encerra o python
