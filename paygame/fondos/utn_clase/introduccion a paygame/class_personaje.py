import pygame, sys

class personaje: #constructor,atributos(getters,setter) y metodos
    
    def __init__(self,tamaño,origen,path_imagen):
        # self.superficie = pygame.Surface((tamaño))
        self.superficie = pygame.image.load(path_imagen)
        self.superficie = pygame.transform.scale(self.superficie,tamaño)
        self.sonido_colicion = pygame.mixer.Sound("musica\ñam.mp3")
        self.sonido_colicion.set_volume(0.5)
        
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
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.sonido_colicion.play()