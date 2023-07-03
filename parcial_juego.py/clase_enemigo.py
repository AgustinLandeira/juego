
from listas import *
from pantalla_original import *


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

class jefe:
    def __init__(self,x,y,velocidad,lista_recibida,derecha,limite_izquierda,limite_derecha):
        
        self.rectangulo_boss = lista_recibida[0].get_rect()
        self.rectangulo_boss.x = x
        self.rectangulo_boss.y = y
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
    
    def atributos_bosss(self):
        
        return{
            'rectangulo': self.rectangulo_boss,
            'velocidad': self.velocidad,
            'direccion_izquierda':self.direccion_izquierda,
            'direccion_derecha': self.direccion_derecha,
            'limite_derecha': self.limite_derecha,
            'limite_izquierda': self.limite_izquierda,
            'bandera': self.bandera,
            'direccion': self.direccion,
            'lados': obtener_rectangulos(self.rectangulo_boss),
            'aumento_velocidad': self.aumento_velocidad
            

            
        }
        
    

        
                   
        

        
        
