import pygame, sys

pygame.init()
#constantes
largo = 500
ancho = 400

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)


pantalla = pygame.display.set_mode((largo,ancho)) # largo y ancho de la pantalla(pixeless)
pantalla.fill(BLANCO)

#(x,y,ancho,largo)
pygame.draw.rect(pantalla,VERDE, (100,50,100,50),5)
pygame.draw.line(pantalla,ROJO,(100,86),(199,86),2)

#pygame.draw.circle(pantalla,AZUL_CLARO,(125,250),25,2)
#pygame.draw.ellipse(pantalla,NEGRO,(275,200,40,80),2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
