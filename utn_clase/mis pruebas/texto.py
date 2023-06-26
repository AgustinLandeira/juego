import pygame, sys

ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)
BLANCO = (255,255,255)

pygame.init()
ventana = pygame.display.set_mode((500,400)) #largo y ancho
pygame.display.set_caption("bievenido a mi proyecto")

miFuente = pygame.font.Font(None,30) # permite crear una fuenta indeterminada
texto = miFuente.render(f"prueba:",0,AZUL_CLARO,BLANCO) # recibe el texto que queramos poner

segunda_fuente = pygame.font.SysFont("Arial",30) # estrae de nuetsro sistema una fuente
textooo = segunda_fuente.render(f"prueba:",0,AZUL_CLARO,BLANCO) # recibe el texto que queramos poner
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # para que pare todos los modulos de python
            sys.exit()
    
    ventana.blit(texto,(0,0))
    ventana.blit(textooo,(100,100))
    pygame.display.update()


