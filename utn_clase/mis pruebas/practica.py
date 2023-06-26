import pygame, sys

ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)

pygame.init()
                    #red green blue
#color = pygame.Color(255,120,9)
ventana = pygame.display.set_mode((500,400)) #largo y ancho
pygame.display.set_caption("bievenido a mi proyecto")
ventana.fill(ROJO)
pygame.draw.line(ventana,AZUL_CLARO,(100,100),(200,100),9)

while True:
    
    #ventana.fill(ROJO) # rellena nuestra ventana reciebiendo como parametro el color
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # para que pare todos los modulos de python
            sys.exit()
    
    
    pygame.display.update()


