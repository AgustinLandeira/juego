import pygame, sys

ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)

pygame.init()
ventana = pygame.display.set_mode((400,300)) #largo y ancho
pygame.display.set_caption("bievenido a mi proyecto")

imagen = pygame.image.load("sonic (2).jpg") # cargar la imagen 
pygame.draw.circle(ventana,ROJO,(129,69),10)
x,y = 130,70
ventana.blit(imagen,(x,y))


while True:
    
    #ventana.fill(ROJO) # rellena nuestra ventana reciebiendo como parametro el color
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # para que pare todos los modulos de python
            sys.exit()
    
    pygame.display.update()
    
