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

ancho = 800
largo = 800


pantalla = pygame.display.set_mode((largo,ancho)) # largo y ancho de la pantalla(pixeless)
pygame.display.set_caption("holaaaaaa")

fuente = pygame.font.SysFont("consolas",60)
texto = fuente.render("hola 1c",False,VERDE,AZUL)

bandera = True
while bandera:
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
    pygame.display.update()
    pantalla.blit(texto,(0,0))
    
pygame.quit()
    
    







