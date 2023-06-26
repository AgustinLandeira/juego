import pygame
import time

pygame.init()
clock = pygame.time.Clock()

previous_time = pygame.time.get_ticks()
def crear_sonido_fondo(path,duracion,volumen):
    
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(duracion)
    pygame.mixer.music.set_volume(volumen)

def crear_sonido_coalicion_anillo(path,duracion):
    
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(duracion)
        
    
def sonido_saltando(path,duracion):
        
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(duracion)
        
    
    
def sonido_advertencia(path,duracion):
    
    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(duracion)

      

