import pygame,sys
from NIVELES import Nivel
from listas import *
from sonido import *
from actualizar_anillos import *
from crear_objetos_enem import *

from clases.clase_personaje import personaje
class NivelUno(Nivel):
    def __init__(self, pantalla):
        w,h = 1200,600

        pantalla = pygame.display.set_mode((w,h))

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

        personaje_principal = personaje(h/2 - 120,465,20,0,-35,35,5,"quieto",False)



        lados_personaje = obtener_rectangulos(personaje_principal.rectangulo)

        #SUPERFICIE
        #piso
        piso = pygame.Rect(0,0,w,20)
        piso.top = personaje_principal.rectangulo.bottom

        lados_piso = obtener_rectangulos(piso)

        ##plataforma y trampas#

        lista_plataformas,plataformas_creadas,listas_trampas = crear_plataformas_nivel1(lados_piso)


        ####ENEMIGOS#############################################################

        enemigos,lista_enemigos_animaciones = crear_enemigo_nivel1()
        lista_de_bombarderos = None
        lista_proyectiles = None

        #################################################################################
        
        ##BOSS###
        boss = None
        lista_boss = None
        vidas_boss = None

        #ANILLOS

        lista_anillos = crear_anillos("nivel uno")
        anillos_creados,items_creados = hacer_lluvia_objetos(30,5)
        lista_vacia = False

        #VIDAS
        lista_vidas = []
        for i in range(3):
            una_vida = personaje_principal.obtener_vidas()
            lista_vidas.append(una_vida)

        #eventos
        tick = pygame.USEREVENT + 0 # se crea el evento
        pygame.time.set_timer(tick,100) # se lanza cada milisegundos

        tiempo = "no termino"
        muertes = 0
        
        path = "parcial_juego\datos_partida\\nivel_1.json"
            
        super().__init__(pantalla, personaje_principal, lista_plataformas, fondo, lados_personaje,
                        plataformas_creadas, listas_trampas, enemigos, lista_enemigos_animaciones, 
                        lista_anillos,anillos_creados, items_creados, lista_vacia, lista_vidas, 
                        lista_animaciones,tiempo,muertes,lista_de_bombarderos,lista_proyectiles,boss,
                        lista_boss,vidas_boss,path)       
                
