import pygame,sys
from pygame.locals import *

class paleta:
    def __init__(self,pos_inicial,tamaño,velocidad_y,color):
        self.surface = pygame.Surface(tamaño)
        self.surface.fill(color)
        self.rectangulo = self.surface.get_rect()
        
        self.rectangulo.center = pos_inicial
        
        self.velocidad = velocidad_y
    
    def mover_y(self,alto_pantalla):
        self.rectangulo.y += self.velocidad
    
        if self.rectangulo.top> alto_pantalla:
            self.rectangulo.bottom = 0
        elif self.rectangulo.bottom < 0:
            self.rectangulo.top = alto_pantalla
    
    def verificar_colisiones(self,otra_paleta,paleta):
        if self.rectangulo.colliderect(otra_paleta.rectangulo):
            self.surface.fill("green")
            otra_paleta.surface.fill("yellow")
        
    def draw(self,pantalla):
        pantalla.blit(self.surface,self.rectangulo)
    
    def update(self,pantalla):
        self.mover_y(pantalla.get_height())
        self.draw(pantalla)
        




pygame.init()
reloj = pygame.time.Clock()
fps = 60
ancho = 1200
alto = 600

pantalla=pygame.display.set_mode((ancho,alto))


paleta_uno = paleta((ancho/2,alto/2),(50,50),5,"red")
paleta_dos = paleta((ancho/2,500),(50,50),5,"blue")


def verificar_colision(superficie_rectangulo,rectangulo:pygame.Rect,superficie_otro_rectangulo,otro_rectangulo):
    
    if rectangulo.colliderect(otro_rectangulo):
        superficie_rectangulo.fill("yellow")
        superficie_otro_rectangulo.fill("green")
    else:
        superficie_rectangulo.fill("red")
        superficie_otro_rectangulo.fill("blue")

while True:
    
    reloj.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pantalla.fill("black")
    
    paleta_uno.update(pantalla)
    paleta_dos.update(pantalla)
    pygame.display.update()
        