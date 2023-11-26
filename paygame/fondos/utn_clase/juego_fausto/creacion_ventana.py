import pygame,sys
from pygame.locals import *
pygame.init()
reloj = pygame.time.Clock()
fps = 60
ancho = 1200
alto = 600

pantalla=pygame.display.set_mode((ancho,alto))

superficie_rectangulo = pygame.Surface((50,50))
superficie_rectangulo.fill("red")
rectangulo = superficie_rectangulo.get_rect()
rectangulo.center = (ancho/2,alto/2)
#creando rectangulo

superficie_otro_rectangulo = pygame.Surface((50,50))
superficie_otro_rectangulo.fill("red")
otro_rectangulo = superficie_otro_rectangulo.get_rect()
otro_rectangulo.center = (ancho/2,alto/2)
#creando rectangulo
rectangulo = pygame.Rect(ancho/2,alto/2,50,50)
otro_rectangulo = pygame.Rect(ancho/2,500,50,50)











def mover_rectangulo(rectangulo:pygame.Rect,velocidad_y,alto_pantalla):
    rectangulo.y += velocidad_y
    
    if rectangulo.top> alto_pantalla:
        rectangulo.bottom = 0
    elif rectangulo.bottom < 0:
        rectangulo.top = alto_pantalla

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
    
    mover_rectangulo(rectangulo,5,alto)
    mover_rectangulo(otro_rectangulo,-5,alto)
    
    verificar_colision(superficie_rectangulo,rectangulo,superficie_otro_rectangulo,otro_rectangulo)
    
    pantalla.blit(superficie_rectangulo,rectangulo)
    pantalla.blit(superficie_otro_rectangulo,otro_rectangulo)

    pygame.display.update()
        