from NIVELES import Nivel
from clases.clase_personaje import personaje
from crear_objetos_enem import *

from listas import *
from sonido import *
from pantalla_original import *

from actualizar_anillos import *


class NivelUno(Nivel):
    def __init__(self,pantalla:pygame.Surface):
        
        w = pantalla.get_width()
        h = pantalla.get_height()
        
        pantalla = pygame.display.set_mode((w,h))

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
        print("estoy en enemigos")

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

        super().__init__(pantalla,sonic,lista_plataformas,fondo,lados_personaje,plataformas_creadas,
                        listas_trampas,enemigos,lista_enemigos_animaciones,lista_anillos,anillos_creados,
                        items_creados,lista_vacia,lista_vidas,lista_animaciones)
        