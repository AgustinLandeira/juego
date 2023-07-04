import pygame,sys
from prueba1 import NivelUno
from modo import *


pygame.init()

fps = 20

w,h = 1200,600
tamaño_pantalla = (w,h)

pantalla = pygame.display.set_mode(tamaño_pantalla)
nivel_actual = NivelUno(pantalla)

#fuente
font = pygame.font.Font(None, 30)
fuente_final = pygame.font.SysFont("pixel-font", 100)


#tiempo
tiempo_transcurrido = pygame.time.get_ticks()
clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()
reloj = pygame.time.Clock()

#eventos
tick = pygame.USEREVENT + 0 # se crea el evento
pygame.time.set_timer(tick,100) # se lanza cada milisegundos



tiempo = "no termino"
running = True

while running:
    
    segundos = (pygame.time.get_ticks() - tiempo_transcurrido) // 1000  # Tiempo transcurrido en segundos
    text = font.render(f"Tiempo: {segundos} segundos", True, ("black"))
    
    reloj.tick(fps)
    
    eventos = pygame.event.get()
    
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            runnin = False
            
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
                
    if tiempo != "terminado":
        
        nivel_actual.update(tiempo,segundos,text,font,fuente_final)    
       
        pygame.display.update()
      



