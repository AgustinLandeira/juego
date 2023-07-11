import pygame
from editar import obtener_rectangulos


class jefe:
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
        self.aumento_velocidad = False
        self.superficie_vida = pygame.image.load("recursos de mi juego\enemigos-objetos\\vidas_boss.png")
        self.superficie_vida = pygame.transform.scale(self.superficie_vida,(20,20))
        self.rectangulo_vida = self.superficie_vida.get_rect()
        self.rectangulo_vida.x = 1050
        self.rectangulo_vida.y = 70

    def obtener_vidas(self):
        self.rectangulo_vida.x += 30
        return{
            "superficie_vida": self.superficie_vida,
            "rectangulo_vida": self.rectangulo_vida,
            "posicion_x": self.rectangulo_vida.x,
            "posicion_y": self.rectangulo_vida.y
        }
    
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
            'lados': obtener_rectangulos(self.rectangulo),
            'aumento_velocidad': self.aumento_velocidad
            
        }
        
    

        
                   
        

        
        
