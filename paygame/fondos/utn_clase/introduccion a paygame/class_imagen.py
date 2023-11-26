import pygame, sys

class imagen: #constructor,atributos(getters,setter) y metodos
    
    def __init__(self,tamaño,colores,origen):
        
        self.superficie = pygame.Surface((tamaño))
        self.color = colores["color_inicial"]
        self.color_colision = colores["color_colision"]
        self.superficie.fill(self.color)
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.center = origen

    def mover_imagen(self,sentido:str,desplazamiento,tamaño_pantalla):#(largo,ancho)  
        if sentido == "vertical"  :
            self.rectangulo.y += desplazamiento
            if self.rectangulo.top >tamaño_pantalla[1]:
                self.rectangulo.bottom = 0
        else:
            self.rectangulo.x += desplazamiento
            if self.rectangulo.left > tamaño_pantalla[0]:
                self.rectangulo.right = 0
          
    def detectar_colicion(self,otra_imagen):
        if  self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.superficie.fill(self.color_colision)
            otra_imagen.superficie.fill(otra_imagen.color_colision)
            
        else:
            self.superficie.fill(self.color)
            otra_imagen.superficie.fill(otra_imagen.color)
