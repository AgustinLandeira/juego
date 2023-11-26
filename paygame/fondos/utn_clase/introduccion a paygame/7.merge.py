from class_personaje import personaje
import pygame, sys
    
largo = 1000
ancho = 600
fps = 30

pygame.init()

screen_size = (largo,ancho)

pantalla = pygame.display.set_mode(screen_size) # largo y ancho de la pantalla

# icono

icono = pygame.image.load("imagenes\icono_homero.png")
pygame.display.set_caption("esto es el de homero")
pygame.display.set_icon(icono)

#fondo
fondo = pygame.image.load("imagenes\mondo_casa.jpg")
fondo_escalado = pygame.transform.scale(fondo,screen_size)
pantalla.blit(fondo_escalado,(0,0))

#musica

pygame.mixer.music.load("musica\intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

pygame.init()

pantalla = pygame.display.set_mode((largo,ancho)) # largo y ancho de la pantalla(pixeless)
clock = pygame.time.Clock()


homero = personaje((200,200),(largo/2,ancho/2),"imagenes\homero.png")
dona = personaje((100,100),(largo/2,ancho),"imagenes\dona.png")

while True:
    
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pantalla.blit(fondo_escalado,(0,0))   
    pantalla.blit(dona.superficie,dona.rectangulo)
    pantalla.blit(homero.superficie,homero.rectangulo)
    # movimiento
    
    homero.mover_imagen("horizontal",10,(largo,ancho))
    dona.mover_imagen("vertical",10,(largo,ancho))
    
    #colecion    
    homero.detectar_colicion(dona)
    
    pygame.display.flip()
