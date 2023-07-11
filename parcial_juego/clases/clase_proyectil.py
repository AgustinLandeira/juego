import pygame
from editar import *


class proyectil:
    def  __init__(self,ancho,alto,x,y,velocidad,path,limite,personaje):
        
        self.superficie = pygame.image.load(path)
        self.superficie = pygame.transform.scale(self.superficie,(ancho,alto))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.lados = obtener_rectangulos(self.rectangulo)
        self.velocidad = velocidad
        self.limite = limite
        self.personaje = personaje
    
    def obtener_diccionario(self):
        return {
            "personaje": self.personaje,
            "superficie": self.superficie,
            "rectangulo": self.rectangulo,
            "lados": self.lados,
            "velocidad": self.velocidad,
            "limite": self.limite   
        }

