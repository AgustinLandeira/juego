import pygame,sys
import random
pygame.init()
#constantes

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ancho = 800
largo = 800


pantalla = pygame.display.set_mode((ancho,largo)) # largo y ancho de la pantalla(pixeless)
pygame.display.set_caption("prueba fps")

fuente = pygame.font.SysFont("consolas",25)
texto = fuente.render("hola 1c",False,VERDE,AZUL)

circulos = []

for i  in range(1150):
    x = random.randint(1,ancho-1) # ubicaciones aleatorias de la ventaa
    y = random.randint(1,largo-1) 
    circulos.append([x,y])

bandera = True
while bandera:
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            bandera = False
    
    #pantalla.blit(texto,(0,0))
    pantalla.fill(NEGRO)
    
    for c in circulos:
        
        pygame.draw.circle(pantalla,ROJO,(c[0],c[1]),5,10)
    
    for circulo in circulos:
        circulo[0] += 1
        circulo[1] += 2
        if circulo [0] > ancho:
            c[0] = 0
        if circulo[1]  > largo :
            circulo[1] = 0
    
        
    pygame.display.update()
    pygame.time.delay(10)
pygame.quit()
    
    







