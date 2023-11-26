import pygame


class personaje:
    def __init__(self,path,width,height,x,y):
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,(width,height))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y 
        
        
'''imagen_homero = pygame.image.load("Recursos_17\derecha.png")
imagen_homero = pygame.transform.scale(imagen_homero,(width,height))
rectangulo_homero = imagen_homero.get_rect()
rectangulo_homero.x = 400
rectangulo_homero.y = 570'''