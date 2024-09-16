import pygame # type: ignore
import sys

# Inicializar o Pygame
pygame.init()

# Dimensões da tela

largura = 800 
altura = 400
tela = pygame.display.set_mode((largura, altura)) 
pygame.display.set_caption('Pong')


#Cores 

branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 128, 255) 
verde = (0, 255, 0)
amarelo = (255, 255, 0)

#Fosições e tamannos das raquetes e bola

raquete_largura = 10
raquete_altura = 100
raquete_esquerda =  altura //2 - raquete_altura // 2 
raquete_direita_y = altura //2 - raquete_altura //2
bola_dx,  bola_y =  largura // 2, altura // 2
bola_dx, bola_dy = 5, 5

#Principal do loop
while True:
   # Processa eventos
 for evento in  pygame.event.get():
   if evento.type == pygame.QUIT:
    pygame.quit()
    sys.exit()

#Movimenta raquetes
 
 teclas = pygame.key.get_pressed()
 if teclas[pygame.K_w]:
  raquete_esquerda -= velocidade_raquete # type: ignore
 if teclas[pygame.K_s]:
  raquete_esquerda += velocidade_raquete
 if teclas[pygame.k_UP]:
  raquete_direita_y -= velocidade_raquete
 if teclas[pygame.K_DOWN]:
  raquete_direita_y += velocidade_raquete  

  #Movimenta a bola 
  bola_x += bola_dx
  bola_y += bola_dy

  #verificar colisões com o topo e o fundo 
  if bola_y <= 0 or bola_y >= altura -10:
   bola_dy = -bola_dy

  #verificar colisão com raquetes
   if bola_x  <= 20 and raquete_esquerda_y <bola_y < raquete_esquerda_y + raquete_altura:
    bola_dx = -bola_dx
    if bola_dx >= largura - 20 and raquete_direita_y < bola_y < raquete_direita_y + raquete_altura:
     bola_dx = -bola_dx

  # reiniciar a bola se ela sair da tela 
     if bola_x < 0 or bola_x > largura:
      bola_x, bola_y = largura // 2, altura // 2

  # Desenhar os elementos 
  tela.fill(preto)
  pygame.draw.rect(tela, azul, (10, raquete_esquerda_y, raquete_largura, raquete_altura)) # Raquete esquerda azul
  pygame.draw.rect(tela, verde,(largura - 20, raquete_direita_y, raquete_largura, raquete_altura)) # Raquete direita verde 
  pygame.draw.ellipse(tela,amarelo,(bola_x, bola_y,10,10)) # Bola amarela

  pygame.display.flip()

  pygame.time.Clock().tick(60)