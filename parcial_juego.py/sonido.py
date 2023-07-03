import pygame


pygame.init()

def crear_sonido_fondo(path:str,duracion:int,volumen:float):
    """
    reproduce un sonido de fondo mientras el jugador juega
    parametros: recibe el path que seria el sonido a reporducir,duracion del sonido y volumen
    """
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(duracion)
    pygame.mixer.music.set_volume(volumen)
        
def crear_sonido_coalicion_anillo(path:str):
    """
    reproduce un efecto de sonido cuando el jugador agarra un anillo
    parametro: recibe el path que seria el audio a reproducir  
    """

    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(0)
    
    
def sonido_saltando(path:str):
    
    """
    reproduce un efecto de sonido cuando el jugador agarra un anillo
    parametro: recibe el path que seria el audio a reproducir     
    """
    
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(0)
        
    
def sonido_advertencia(path:str):
    """
    reproduce un efecto de sonido cuando el jugador quiere cruzar un limite o pasar una plataforma
    parametro: recibe el path que seria el audio a reproducir     
    """
    
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(0)

def sonido_daño(path:str):
    """
    reproduce un efecto de sonido cuando el jugador recibe daño de un enemigo o proyectil
    parametro: recibe el path que seria el audio a reproducir     
    """
    
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(0) 
    
def daño_del_boss(path:str):
    """
    reproduce un efecto de sonido cuando el jugador recibe daño del boss
    parametro: recibe el path que seria el audio a reproducir     
    """
    
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(0)

def muerte_boss(path:str):
    """
    reproduce un efecto de sonido cuando el boss muere
    parametro: recibe el path que seria el audio a reproducir     
    """
   
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(0)

def daño_al_boss(path:str):
    """
    reproduce un efecto de sonido cuando el boss recibe daño del personaje
    parametro: recibe el path que seria el audio a reproducir     
    """
   
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(0)

