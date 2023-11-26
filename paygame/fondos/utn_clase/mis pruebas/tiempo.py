import pygame, sys
from pygame.locals import *

ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)
BLANCO = (255,255,255)

pygame.init()
ventana = pygame.display.set_mode((500,400)) #largo y ancho
pygame.display.set_caption("bievenido a mi proyecto")

fuente = pygame.font.SysFont("Arial",30)


aux = 1
while True:
    ventana.fill(BLANCO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # para que pare todos los modulos de python
            sys.exit()
    
    tiempo = pygame.time.get_ticks()/1000  # nos devuelve milisegundos
    
    if aux == tiempo:
        aux +=1
        
    
    contador = fuente.render(f"TIEMPO: {tiempo}",0,ROJO)
    ventana.blit(contador,(100,100))
    pygame.display.update()
