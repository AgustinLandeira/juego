import pygame, sys

ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)

pygame.init()
ventana = pygame.display.set_mode((600,300)) #largo y ancho
pygame.display.set_caption("bievenido a mi proyecto")

imagen = pygame.image.load("icono_homero.png") # cargar la imagen 
x,y = 200,100

velocidad = 2 # 2 pixeles de movimiento
derecha = True

while True:
    
    ventana.fill(ROJO)
    ventana.blit(imagen,(x,y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # para que pare todos los modulos de python
            sys.exit()
            
    if derecha == True:
        if x <500:
            x += velocidad
        else:
            derecha = False
    else :
        if x > 1:
            x -=velocidad
        else:
            derecha = True
    
    pygame.display.update()
    
