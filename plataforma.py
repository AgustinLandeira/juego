import pygame
def crear_plataforma(path,largo,alto,x,y):
    plataforma = pygame.image.load(path)
    plataforma = pygame.transform.scale(plataforma,(largo,alto))
    rectangulo_plataforma = plataforma.get_rect()
    rectangulo_plataforma.x = x
    rectangulo_plataforma.y = y
    
    return rectangulo_plataforma,plataforma

#
'''plataforma = pygame.image.load("recursos de mi juego\plataformas\\1_plataforma.png")
plataforma = pygame.transform.scale(plataforma,(200,75))

rectangulo_plataforma = plataforma.get_rect()
rectangulo_plataforma.x = 500
rectangulo_plataforma.y = 400'''



'''rectangulo_plataforma,plataforma = crear_plataforma("recursos de mi juego\plataformas\\1_plataforma.png",
                                        200,75,500,400)
rectangulo_plataforma_2,plataforma_2 =crear_plataforma("recursos de mi juego\plataformas\\0.png",50,20,200,350)

lista_de_plataformas = [rectangulo_plataforma,rectangulo_plataforma_2]
'''

