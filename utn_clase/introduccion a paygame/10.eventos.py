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

ancho = 600
largo = 600


pantalla = pygame.display.set_mode((ancho,largo)) # largo y ancho de la pantalla(pixeless)
pygame.display.set_caption("prueba fps")

flag = True


while flag:
    
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
            
    lista_teclas = pygame.key.get_pressed() # me devuelve la las teclas que presione
    
    if lista_teclas[pygame.K_0]:
        print("0")
        
    if lista_teclas[pygame.K_LEFT]:
        print("LEFT")
    if lista_teclas[pygame.K_SPACE]:
        print("espacio")
    