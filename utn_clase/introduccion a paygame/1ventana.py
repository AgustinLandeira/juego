import pygame, sys

pygame.init()

largo = 500
ancho = 400


pantalla = pygame.display.set_mode((largo,ancho)) # largo y ancho de la pantalla

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

