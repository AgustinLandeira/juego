import pygame, sys

#constantes
largo = 800
alto = 600

fps = 30

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

pygame.init()

pantalla = pygame.display.set_mode((largo,alto)) # largo y alto de la pantalla(pixeless)
clock = pygame.time.Clock()

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)

rectangulo_vertical = imagen_vertical.get_rect()
rectangulo_vertical.center = (largo/2,alto/2)

imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(AZUL_CLARO)

rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (largo-100,alto/2)


while True:
    
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pantalla.fill(NEGRO)        
    pantalla.blit(imagen_vertical,rectangulo_vertical)
    pantalla.blit(imagen_horizontal,rectangulo_horizontal)
    
    rectangulo_vertical.y +=10
    
    if rectangulo_vertical.top >alto:
        rectangulo_vertical.top = 0
        
    rectangulo_horizontal.x +=10
    
    if rectangulo_horizontal.left >largo:
        rectangulo_horizontal.right = 0
        
    if rectangulo_horizontal.colliderect(rectangulo_vertical):
        imagen_horizontal.fill(ROJO)
        imagen_vertical.fill(BLANCO)
    else:
        imagen_horizontal.fill(VERDE)
        imagen_vertical.fill(AZUL)
    
    pygame.draw.line(pantalla,AZUL,(400,0),(400,800),1)
    pygame.draw.line(pantalla,AZUL,(0,300),(800,300),1)
    pygame.display.flip()
