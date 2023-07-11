
import pygame
from  listas import *
from editar import obtener_rectangulos


class enemigo:
    def __init__(self,x,y,velocidad,lista_recibida,derecha,limite_izquierda,limite_derecha):
        
        self.rectangulo = lista_recibida[0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.velocidad = velocidad
        self.direccion_derecha = derecha[0]
        self.direccion_izquierda = lista_recibida[0]
        self.limite_izquierda = limite_izquierda
        self.limite_derecha = limite_derecha
        self.bandera = False
        self.direccion = "ninguna"
    
    def obtener_diccionario(self):
        return{
            'rectangulo': self.rectangulo,
            'velocidad': self.velocidad,
            'direccion_izquierda':self.direccion_izquierda,
            'direccion_derecha': self.direccion_derecha,
            'limite_derecha': self.limite_derecha,
            'limite_izquierda': self.limite_izquierda,
            'bandera': self.bandera,
            'direccion': self.direccion,
            'lados': obtener_rectangulos(self.rectangulo)  
        }
        
