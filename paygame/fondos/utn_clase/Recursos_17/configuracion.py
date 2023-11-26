import pygame

def configurar_pantalla(TAMAÑO_PANTALLA:tuple,texto:str,path:str):
    # CONFIGURACIONes
    #PANTALLA
    screen = pygame.display.set_mode(TAMAÑO_PANTALLA)
    pygame.display.set_caption(texto)
    icono = pygame.image.load(path)
    pygame.display.set_icon(icono)
    
    return screen
    
def configurar_fondo(path,TAMAÑO_PANTALLA,screen):
    #FONDO
    fondo = pygame.image.load(path)
    fondo_final = pygame.transform.scale(fondo,TAMAÑO_PANTALLA)
    screen.blit(fondo_final,(0,0))
    
    return fondo
    
def configurar_musica(path,volumen):
    #MUSICA
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(path)
    sonido_fondo.set_volume(volumen)
    sonido_fondo.play()

