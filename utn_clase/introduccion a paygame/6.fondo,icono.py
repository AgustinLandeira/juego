import pygame, sys

pygame.init()

largo = 1000
ancho = 600

screen_size = (largo,ancho)

pantalla = pygame.display.set_mode(screen_size) # largo y ancho de la pantalla

# icono

icono = pygame.image.load("icono_homero.png")
pygame.display.set_caption("esto es el de homero")
pygame.display.set_icon(icono)

#fondo
fondo = pygame.image.load("fondo_casa.jpg")
fondo_escalado = pygame.transform.scale(fondo,screen_size)
pantalla.blit(fondo_escalado,(0,0))

#musica

pygame.mixer.music.load("intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
