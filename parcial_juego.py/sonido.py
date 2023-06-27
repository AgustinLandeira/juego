import pygame
import time

pygame.init()

def crear_sonido_fondo(path,duracion,volumen):
    
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(duracion)
    pygame.mixer.music.set_volume(volumen)
        
def crear_sonido_coalicion_anillo(path,duracion):

    sonido_colision = pygame.mixer.Sound(path)
    sonido_colision.play(duracion)
    
    
def sonido_saltando(path,duracion):
    
    primera_vuelta = False
    
    if primera_vuelta == False:
        ultima_produccion = 0
        retraso_sonido = 2
    
    tiempo_actual = time.time()
    
    if tiempo_actual - ultima_produccion >= retraso_sonido:
           
        sonido_colision = pygame.mixer.Sound(path)
        sonido_colision.play(duracion)
        primera_vuelta = True
        ultima_produccion = tiempo_actual
    
def sonido_advertencia(path,duracion):
    
    primera_vuelta = False
    
    if primera_vuelta == False:
        ultima_produccion = 0
        retraso_sonido = 3.0
    
    tiempo_actual = time.time()
    
    if tiempo_actual - ultima_produccion >= retraso_sonido:
        
        sonido_colision = pygame.mixer.Sound(path)
        sonido_colision.play(duracion)
        primera_vuelta = True
        ultima_produccion = tiempo_actual
 

