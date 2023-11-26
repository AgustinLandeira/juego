import pygame, sys

ROJO = (255,0,0)
AZUL_CLARO = (0,150,255)

ancho = 900
alto = 480

class homero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("icono_homero.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho /2
        self.rect.centery = alto - 30
        
        self.lista_disparo = []
        self.disparo = True
        
    def dispara(self):
        pass
    
    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)

def space_invader():
    pygame.init()

    ventana = pygame.display.set_mode((ancho,alto)) #largo y ancho
    pygame.display.set_caption("bievenido a mi proyecto")
    fondo = pygame.image.load("fondo_casa.jpg")
    jugador = homero()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # para que pare todos los modulos de python
                sys.exit()
        
        ventana.blit(fondo,(0,0))
        jugador.dibujar(ventana)
               
        pygame.display.update()
        
space_invader()