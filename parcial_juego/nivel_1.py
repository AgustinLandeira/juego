import pygame,sys

from listas import *

from pantalla_original import *
from modo import *

from actualizar_enemigo import actualizar_enemigo
from actualizar_enemigo import coalicion_enemigo

from sonido import *

from actualizar_anillos import *

from crear_objetos_enem import *

from clases.clase_personaje import personaje


w,h = 1200,600

fps = 20 

pygame.init()

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((w,h))

#fuente
font = pygame.font.Font(None, 30)
fuente_final = pygame.font.SysFont("pixel-font", 100)


#tiempo
tiempo_transcurrido = pygame.time.get_ticks()
clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()

#fondo
fondo = pygame.image.load("recursos de mi juego\\background\mi mapa.png")
fondo =pygame.transform.scale(fondo,(w,h))

pantalla.blit(fondo,(0,0))

#SONIDO PARA EL FONDO
crear_sonido_fondo("recursos de mi juego\sonidos\sonic-gumball.mp3",-1,0.1)

#PERSONAJE   

lista_animaciones = [personaje_quieto,personaje_quieto_izquierda,personaje_corriendo,
                    personaje_corriendo_izquierda,personaje_saltando,personaje_saltando_izquierda,
                    personaje_muriendo,celebracion,perdio]

reescalar_imagen(lista_animaciones,50,60) 

sonic = personaje(h/2 - 120,465,20,0,-35,35,5,"quieto")



lados_personaje = obtener_rectangulos(sonic.rectangulo)

#SUPERFICIE
#piso
piso = pygame.Rect(0,0,w,20)
piso.top = sonic.rectangulo.bottom

lados_piso = obtener_rectangulos(piso)

##plataforma y trampas#

lista_plataformas,plataformas_creadas,listas_trampas = crear_plataformas_nivel1(lados_piso)


####ENEMIGOS#############################################################

enemigos,lista_enemigos_animaciones = crear_enemigo_nivel1()

#################################################################################

#ANILLOS

lista_anillos = crear_anillos("nivel uno")
anillos_creados,items_creados = hacer_lluvia_objetos(30,5)
lista_vacia = False

#VIDAS
lista_vidas = []
for i in range(3):
    una_vida = sonic.obtener_vidas()
    lista_vidas.append(una_vida)

#eventos
tick = pygame.USEREVENT + 0 # se crea el evento
pygame.time.set_timer(tick,100) # se lanza cada milisegundos

tiempo = "no termino"
running = True

while running:
    
    segundos = (pygame.time.get_ticks() - tiempo_transcurrido) // 1000  # Tiempo transcurrido en segundos
    text = font.render(f"Tiempo: {segundos} segundos", True, ("black"))
    
    reloj.tick(fps)
    
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
                
    if tiempo != "terminado":
        
        lista_eventos = pygame.key.get_pressed()
        
        
        if (lista_eventos[pygame.K_RIGHT] and sonic.rectangulo.right < w - sonic.velocidad):
            sonic.accion = "derecha"  
        
        elif  (lista_eventos[pygame.K_LEFT] and sonic.rectangulo.left >  20 ):
            sonic.accion = "izquierda" 
        
        elif (lista_eventos[pygame.K_UP]):
            sonic.accion = "salta"
        
        else :
            sonic.accion = "quieto" 
            
        pantalla.blit(fondo,(0,0))
        
        murio = coalicion_enemigo(enemigos,lados_personaje,listas_trampas) 
        
        if murio == True:
            
            sonic.accion = "muriendo"
            
        if segundos == 60:
            tiempo = "terminado"
            
            if sonic.puntaje > 300 and len(lista_vidas) > 0:
                sonic.accion = "gano"
                crear_sonido_fondo("recursos de mi juego\sonidos\\victory-sonic.mp3",1,0.1) 
                
            else:
                sonic.accion = "perdio"  
           
        actualizar_pantalla(pantalla,sonic,fondo,lista_plataformas,plataformas_creadas,
            lados_personaje,lista_vidas,tiempo)
                                               
        actualizar_enemigo(enemigos,pantalla)
        
        animar_anillos(pantalla,lista_anillos,anillos,items_creados,item_recuperar_vida)
        
        verificar_coalicion(lista_anillos,lados_personaje,sonic,items_creados,lista_vidas)
        
        if get_mode():
            mostrar_lados_1(lista_plataformas,enemigos,lados_personaje,listas_trampas,pantalla)
        
        score = font.render(f"puntaje: {sonic.puntaje} puntos", True, ("black"))
        vidas_restantes = font.render(f"vidas:",True, ("black"))
        
        pantalla.blit(text, (0, 0))
        pantalla.blit(score, (1020, 10))
        pantalla.blit(vidas_restantes,(1020,50))
        
        if segundos >= 15 and segundos < 30 or segundos > 40 and segundos <59:
            mover_objeto(anillos_creados,items_creados)
            
            for un_anillo in anillos_creados:
                pantalla.blit(un_anillo["superficie"],un_anillo["rectangulo"])
                
        if not anillos_creados:
           
            lista_vacia = True
        
        if lista_vacia  == True:
            anillos_creados,items_creados = hacer_lluvia_objetos(35,2)
            lista_vacia = False
    
        verificar_coalicion(anillos_creados,lados_personaje,sonic,items_creados,lista_vidas)
        
        if lista_vidas == []:
            tiempo = "terminado"
                        
        pygame.display.update()
    
    elif sonic.puntaje > 300 and len(lista_vidas) > 0:
        
        mensaje_final = fuente_final.render(f"YOU WIN",True,("white"))
        
        pantalla.blit(mensaje_final,(h/2 + 100, 200))
        
    else:
        
        mensaje_final = fuente_final.render(f"YOU LOSE",True,("white"))
            
        pantalla.blit(mensaje_final,(h/2 + 100, 200))
        
    
    pygame.display.flip()
        



