import pygame
from niveles import Nivel


class NivelUno(Nivel):
    
    def __init__(self,pantalla: pygame.Surface):
        w = pantalla.get_width()
        h = pantalla.get_height()

        #fondo
        fondo = pygame.image.load("recursos de mi juego\\background\\fondo nivel 3.png")
        fondo =pygame.transform.scale(fondo,(w,h))

        pantalla.blit(fondo,(0,0))

        #SONIDO PARA EL FONDO
        crear_sonido_fondo("recursos de mi juego\sonidos\sonic-gumball.mp3",-1,0.1)
