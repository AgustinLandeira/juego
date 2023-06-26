import pygame, sys

ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)
w,h = 1000,600

fps = 500

reloj = pygame.time.Clock()

pygame.init()
# pantalla-ventana             
ventana = pygame.display.set_mode((w,h)) #largo y ancho

pygame.display.set_caption("exterminadores")
#icono = pygame.image.load("Gunner_Black_Crouch.png")
#pygame.display.set_icon(icono)

fondo = pygame.image.load("mis pruebas\Background city Seamless.png")#mis pruebas\Background city Seamless.png
fondo_escalado = pygame.transform.scale(fondo,(w,h))
x = 0

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # para que pare todos los modulos de python
            sys.exit()
    x_relativa = x % fondo_escalado.get_rect().width # para move imagen
    ventana.blit(fondo_escalado,(x_relativa-fondo_escalado.get_rect().width,0))# para mover la imagen
    
    if x_relativa < w :
        ventana.blit(fondo_escalado,(x_relativa,0))
    
    x -= 1
    pygame.display.update()
    reloj.tick(fps)