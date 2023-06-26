import pygame, sys
from pygame.locals import *

ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)
VERDE = (0,255,0)

pygame.init()
ventana = pygame.display.set_mode((600,300)) #largo y ancho
pygame.display.set_caption("bievenido a mi proyecto")

numero = 0

fuente = pygame.font.Font(None,30)
texto = fuente.render(f"COALICIONES: {numero} ",0,VERDE)


rectangulo_dos = pygame.Rect(200,200,100,50)
x,y = 200,100

velocidad = 1 # 2 pixeles de movimiento
derecha = True

rectangulo = pygame.Rect(0,0,100,50)

while True:
    
    ventana.fill(ROJO)
    ventana.blit(texto,(0,0))
    
    pygame.draw.rect(ventana,VERDE,rectangulo_dos)
    pygame.draw.rect(ventana,AZUL_CLARO,rectangulo)
    rectangulo.left,rectangulo.top = pygame.mouse.get_pos()
    
    if rectangulo.colliderect(rectangulo_dos):
        velocidad = 0
        print("colision")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # para que pare todos los modulos de python
            sys.exit()
            
    if derecha == True:
        if x <500:
            x += velocidad
            rectangulo_dos.x = x 
            
        else:
            derecha = False
    else :
        if x > 1:
            x -=velocidad
            rectangulo_dos.x = x
            
        else:
            derecha = True
    
    pygame.display.update()
    
