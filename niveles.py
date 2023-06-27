import pygame
from modo import *

class Nivel:
    
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo):
        
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
    
    def update(self,lista_eventos):
        
        for evento in lista_eventos:#for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        
        self.leer_inputs()
        self.actualizar_pantalla()
    
    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo,(0,0))
        
        for plataforma in self.plataformas:
            plataforma.draw(self._slave,self.plataformas)
        
        self.jugador.update(self._slave,self.plataformas)
    
    def leer_input(self):
        
        lista_eventos = pygame.key.get_pressed()
        
        if (lista_eventos[pygame.K_RIGHT] and sonic.rectangulo.right < w - sonic.velocidad):
            que_hace = "derecha"  
        
        elif  (lista_eventos[pygame.K_LEFT] and sonic.rectangulo.left >  20 ):
            que_hace = "izquierda" 
        
        elif (lista_eventos[pygame.K_UP]):
            que_hace = "salta"
        else :
            que_hace = "quieto" 
            
        if (lista_eventos[pygame.K_UP]) and (lista_eventos[pygame.K_RIGHT]):
            que_hace = "salta" 
           
        elif (lista_eventos[pygame.K_UP]) and (lista_eventos[pygame.K_RIGHT]):
            que_hace = "salta"  
    
    def dibujar_rectangulos(self):
        
        if get_mode() == True:
            
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave,"orange", self.jugador.lados[lado],2)
            
            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self.slave,"red", plataforma.lados[lado],2)
            
                