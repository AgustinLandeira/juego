
import pygame,sys
from pygame.locals import *
from gui_form_prueba import *

w,h = 1200,600

fps = 7

pygame.init()

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((w,h))

running = True


form_prueba = formPrueba(pantalla,0,0,1200,600,"gold","Magenta",5,True)
while running:
    
    lista_eventos = pygame.event.get()
    reloj.tick(fps)
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    form_prueba.update(lista_eventos)

    
    pygame.display.flip()
        


