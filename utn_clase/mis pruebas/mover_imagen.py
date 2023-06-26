import pygame, sys
from pygame.locals import *
ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)

pygame.init()
ventana = pygame.display.set_mode((600,300)) #largo y ancho
pygame.display.set_caption("bievenido a mi proyecto")

imagen = pygame.image.load("Gunner_Jump.png") # cargar la imagen 
x,y = 200,100

velocidad = 5 # 5 pixeles de movimiento

derecha = True

while True:
    
    ventana.fill(ROJO)
    ventana.blit(imagen,(x,y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # para que pare todos los modulos de python
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            
            if event.key == K_LEFT:
                if x > 1:
                    x -= velocidad
                
            elif event.key == K_RIGHT:
                if x < 500:
                    x += velocidad
                
        elif event.type == pygame.KEYUP:
                
            if event.key == K_LEFT:
                print("FLECHA IZQUIERDA LIBERADA")
                
            elif event.key == K_RIGHT:
                print("FLECHA DERECHA LIBERADA")
                
    '''x,y = pygame.mouse.get_pos() # para mover la imagen con el mouse
    x = x -100
    y = y-50           '''
                
                    
            
            
    pygame.display.update()