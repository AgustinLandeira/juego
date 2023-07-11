import pygame
import random

#from parcial_juego.listas import *
from editar import obtener_rectangulos


class anillo:
    def __init__(self,path,ancho,alto,x,y):
        self.superficie = pygame.image.load(path)
        self.superficie = pygame.transform.scale(self.superficie,(ancho,alto))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.lados = obtener_rectangulos(self.rectangulo)
        self.velocidad = random.randrange(10,25,1)
        
    def obtener_diccionario(self):
        return{
                'superficie': self.superficie,
                'rectangulo':self.rectangulo,
                'lados': self.lados["main"],
                "velocidad": self.velocidad
            }

