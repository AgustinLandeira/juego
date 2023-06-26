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
        #self.mover_y(pantalla.get_height())
        self.draw(pantalla)

class pelota:
    
    def mover_x(self,ancho_pantalla):
        self.rectangulo.x += self.velocidad * self.orientacion_x 
        
        if self.rectangulo.right >ancho_pantalla or self.rectangulo.right < 0:
            self.rectangulo.center = self.pos_inicial
    
    def __init__(self,tamaño,velocidad,tamaño_pantalla):
        self.surface = pygame.Surface(tamaño)   
        self.surface.fill("white")
        self.pos_inicial = (tamaño_pantalla[0]/2,tamaño_pantalla[1]/2) 
        self.rectangulo = self.surface.get_rect()
        self.rectangulo.center = self.pos_inicial
        self.velocidad = velocidad
        self.orientacion_x = 1
        
    def draw(self,pantalla:pygame.Surface): 
        pantalla.blit(self.surface,self.rectangulo)
        
    def update_pelota(self,pantalla,paletas):
        self.draw(pantalla)
        self.mover_x(pantalla.get_width())
        self.verificar_colision(paletas)
        
    def verificar_colision(self,paletas):
        for paleta in paletas:
            if self.rectangulo.colliderect(paleta.rectangulo):
                self.orientacion_x = -1 #self.orientacion_x * -1





pygame.init()
reloj = pygame.time.Clock()
fps = 60
ancho = 1200
alto = 600

pantalla=pygame.display.set_mode((ancho,alto))


paleta_uno = paleta((30,alto/2),(25,150),5,"red")
paleta_dos = paleta((ancho - 30 ,alto/2),(25,150),5,"blue")

paletas = [paleta_uno,paleta_dos]

mi_pelota = pelota((25,25),5,(ancho,alto))
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
    
    mi_pelota.update_pelota(pantalla,paletas)
    
    pygame.display.update()
        