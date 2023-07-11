import pygame
from editar import *

class plataforma:
    def __init__(self,path,ancho,alto,x,y):
        self.plataforma = pygame.image.load(path)
        self.plataforma = pygame.transform.scale(self.plataforma,(ancho,alto))
        self.rectangulo = self.plataforma.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.lados  = obtener_rectangulos(self.rectangulo)