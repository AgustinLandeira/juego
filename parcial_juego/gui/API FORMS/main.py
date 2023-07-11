
from pygame.locals import *
from gui_form_prueba import *
import pygame,sys
from pygame.locals import *

from parcial_juego.nivel_1 import NivelUno
from parcial_juego.nivel_2 import NivelDos
from parcial_juego.nivel_3 import NivelTres


w,h = 1200,600

fps = 15 

pygame.init()

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((w,h))

running = True

niveluno = NivelUno(pantalla)
niveldos = NivelDos(pantalla)
niveltres = NivelTres(pantalla)
while running:
    lista_eventos = pygame.event.get()
    reloj.tick(fps)
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    niveltres.update(lista_eventos)

    
    pygame.display.flip()
        




'''pygame.init()

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
'''