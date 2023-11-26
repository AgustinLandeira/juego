import pygame
import random
from donas import *
from clase_personaje import *
from configuracion import *

FPS = 60
#constantes del rectangulo boca de homero
x = 493
y = 658
z = 40
##########################################
score = 0

#tamaño de homero
width = 200
height = 250
######################

TAMAÑO_PANTALLA = (800,800)

flag = True

pygame.init()

reloj = pygame.time.Clock()

#evento

tick = pygame.USEREVENT + 0 # se crea el evento
pygame.time.set_timer(tick,100) # se lanza cada milisegundos


screen = configurar_pantalla(TAMAÑO_PANTALLA,"homero","Recursos_17\ico.png")
fondo = configurar_fondo("Recursos_17\mondo.png",(800,800),screen)
configurar_musica("Recursos_17\musica.mp3",0.2)

#FUENTE
fuente = pygame.font.SysFont("helvetica",50)


homero = personaje("Recursos_17\derecha.png",200,250,400,570)

rectangulo_boca = pygame.Rect(x,y,z,z)

personaje = {"superficie":homero.imagen,"rectangulo":homero.rectangulo,"rectangulo_boca":rectangulo_boca,"puntaje":score}
#                         imagen homero              rectangulo_homero

#DONAS
lista_donas = crear_lista_dona(50)

while flag:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.USEREVENT:
            if evento.type == tick:
                update(lista_donas)
    
    lista_teclas = pygame.key.get_pressed()
    
    if lista_teclas[pygame.K_LEFT]:
        homero.imagen = pygame.image.load("Recursos_17\izquierda.png") #imagen_homero
        homero.imagen = pygame.transform.scale(homero.imagen,(width,height)) #imagen_homero
        screen.blit(homero.imagen,homero.rectangulo)#imagen_homero,rectangulo_homero
        nueva_x = homero.rectangulo.x + -10 # rectangulo_homero
        
        if nueva_x > 0 and nueva_x <600:
            homero.rectangulo.x = homero.rectangulo.x +- 10 # rectangulo_homero
            rectangulo_boca.x = rectangulo_boca.x +- 10
        
        
    elif lista_teclas[pygame.K_RIGHT]:
        homero.imagen = pygame.image.load("Recursos_17\derecha.png") # imagen_homero
        homero.imagen = pygame.transform.scale(homero.imagen,(width,height))
        screen.blit(homero.imagen,homero.rectangulo) #rectangulo_homero
        nueva_x = homero.rectangulo.x + 10 #rectangulo_homero
        
        if nueva_x < 600:
            homero.rectangulo.x = homero.rectangulo.x + 10 #rectangulo_homero
            rectangulo_boca.x = rectangulo_boca.x + 10
        
    screen.blit(fondo,(0,0)) 
    screen.blit(homero.imagen,homero.rectangulo) #imagen_homero,rectangulo_homero
    
    for dona in lista_donas:
        screen.blit(dona["superficie"],dona["rectangulo"])
    
    actualizar_pantalla(lista_donas,personaje,screen)
    
    puntaje = fuente.render(f"SCORE:{personaje['puntaje']}",True,(255,0,0))
    
    screen.blit(puntaje,(0,0))
        
    pygame.draw.rect(screen,(255,0,0),homero.rectangulo,2) #rectangulo_homero
    pygame.draw.rect(screen,(255,0,0),rectangulo_boca,2)
    pygame.display.flip()

