import pygame, sys

from pygame.locals import *
from gui_form_prueba import *

pygame.init()

ancho = 1200
alto = 600
fps = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((ancho,alto))

form_prueba = formPrueba(pantalla,200,100,900,350,"gold","Magenta",5,True)

while True:
    reloj.tick(fps)
    
    eventos = pygame.event.get()
    
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pantalla.fill("black")
    
    form_prueba.update(eventos)
    
    pygame.display.flip()
