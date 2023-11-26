from class_imagen import imagen
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

color_vertical = {"color_inicial":VERDE,"color_colision":ROJO}
imagen_vertical = imagen((100,100),color_vertical,(largo/2,alto/2))
color_horizontal = {"color_inicial":AZUL_CLARO,"color_colision":BLANCO}
imagen_horizontal = imagen((100,100),color_horizontal,(largo-100,alto/2))

while True:
    
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pantalla.fill(NEGRO)        
    pantalla.blit(imagen_vertical.superficie,imagen_vertical.rectangulo)
    pantalla.blit(imagen_horizontal.superficie,imagen_horizontal.rectangulo)
    # movimiento
    
    imagen_horizontal.mover_imagen("horizontal",10,(largo,alto))
    imagen_vertical.mover_imagen("vertical",10,(largo,alto))
    
    #colecion    
    imagen_horizontal.detectar_colicion(imagen_vertical)
    
    pygame.draw.line(pantalla,AZUL,(400,0),(400,800),1)
    pygame.draw.line(pantalla,AZUL,(0,300),(800,300),1)
    pygame.display.flip()
