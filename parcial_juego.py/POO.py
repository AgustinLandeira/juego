import pygame
from listas import *
from pantalla_original import *


class personaje:
    def __init__(self,x_inicial,y_inicial,velocidad,puntaje,potencia_salto,limite_caida,gravedad,accion):
        
        self.x = x_inicial
        self.y = y_inicial
        self.velocidad = velocidad
        self.rectangulo = personaje_corriendo[0].get_rect()
        self.rectangulo.x = self.x
        self.rectangulo.y = self.y
        self.puntaje = puntaje
        self.superficie_vida = pygame.image.load("recursos de mi juego\enemigos-objetos\\vidas.png")
        self.superficie_vida = pygame.transform.scale(self.superficie_vida,(20,20))
        self.rectangulo_vida = self.superficie_vida.get_rect()
        self.rectangulo_vida.x = 1050
        self.rectangulo_vida.y = 50
        self.contador_de_pasos = 0
        self.direccion = "ninguna"
        self.potencia_salto = potencia_salto
        self.limite_velocidad_caida = limite_caida
        self.gravedad = gravedad
        self.accion = accion
        
    def obtener_vidas(self):
        self.rectangulo_vida.x += 30
        return{
            "superficie_vida": self.superficie_vida,
            "rectangulo_vida": self.rectangulo_vida,
            "posicion_x": self.rectangulo_vida.x,
            "posicion_y": self.rectangulo_vida.y
        }
                  
class plataforma:
    def __init__(self,path,ancho,alto,x,y):
        self.plataforma = pygame.image.load(path)
        self.plataforma = pygame.transform.scale(self.plataforma,(ancho,alto))
        self.rectangulo = self.plataforma.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.lados  = obtener_rectangulos(self.rectangulo)
    
    
    
        