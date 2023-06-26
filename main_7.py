import pygame,sys
from listas import *
from POO import *
from pantalla_original import *
from modo import *

w,h = 1200,600

fps = 60 #18

pygame.init()
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((w,h))

#fondo
fondo = pygame.image.load("recursos de mi juego\\background\mi mapa.png")
fondo =pygame.transform.scale(fondo,(w,h))

pantalla.blit(fondo,(0,0))

#PERSONAJE

lista_animaciones = [personaje_quieto,personaje_quieto_izquierda,personaje_corriendo,
                    personaje_corriendo_izquierda,personaje_saltando,personaje_saltando_izquierda]

reescalar_imagen(lista_animaciones,75,85)

sonic = personaje(h/2 - 250,440,20) #20
que_hace = "quieto"
posicion_Actual =0

lados_personaje = obtener_rectangulos(sonic.rectangulo)

#SUPERFICIE
#piso
piso = pygame.Rect(0,0,w,20)
piso.top = sonic.rectangulo.bottom

lados_piso = obtener_rectangulos(piso)

#plataforma
mi_plataforma = plataforma("recursos de mi juego\plataformas\\1_plataforma.png",300,75,430,400)
mi_plataforma_dos = plataforma("recursos de mi juego\plataformas\\0.png",30,30,100,100)

lados_mi_plataforma = obtener_rectangulos(mi_plataforma.rectangulo)

lista_plataformas = [lados_piso,lados_mi_plataforma]
plataformas_creadas = [mi_plataforma,mi_plataforma_dos]

print(type(mi_plataforma.rectangulo))

while True:
    reloj.tick(fps)
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
    
    lista_eventos = pygame.key.get_pressed()
    
    if (lista_eventos[pygame.K_RIGHT] and sonic.rectangulo.right < w - sonic.velocidad):
        que_hace = "derecha"  
       
    elif  (lista_eventos[pygame.K_LEFT] and sonic.rectangulo.left >  20 ):
        que_hace = "izquierda" 
    
    elif (lista_eventos[pygame.K_UP]):
        que_hace = "salta"
       
    else :
        que_hace = "quieto" 
        reloj.tick(10)
        
    pantalla.blit(fondo,(0,0))     
    
    actualizar_pantalla(pantalla,que_hace,sonic,fondo,lista_plataformas,mi_plataforma,lados_personaje)
    #actualizar_pantalla(pantalla,que_hace,sonic,fondo,piso,mi_plataforma)
    if get_mode():
        
        for lado in lados_personaje:
            pygame.draw.rect(pantalla,"yellow",lados_personaje[lado],2)  
             
        for lado in lados_mi_plataforma:
            pygame.draw.rect(pantalla,"green",lados_mi_plataforma[lado],2)  
              
        for lado in lados_piso:
            pygame.draw.rect(pantalla,"red",lados_piso[lado],2)
            
    pygame.display.update()   



