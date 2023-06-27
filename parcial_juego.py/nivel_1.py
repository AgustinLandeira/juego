import pygame,sys

from listas import *
from POO import *
from pantalla_original import *
from modo import *
from clase_enemigo import *
from actualizar_enemigo import *
from sonido import *
from clase_anillo import *
from actualizar_anillos import *

w,h = 1200,600

fps = 150 

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

sonic = personaje(h/2 - 120,465,20,0,-35,35,5)#h/2 - 250,460,20,0 
que_hace = "quieto"
posicion_Actual =0

lados_personaje = obtener_rectangulos(sonic.rectangulo)

#SUPERFICIE
#piso
piso = pygame.Rect(0,0,w,20)
piso.top = sonic.rectangulo.bottom

lados_piso = obtener_rectangulos(piso)

#plataforma
mi_plataforma = plataforma("recursos de mi juego\plataformas\\1_plataforma.png",300,75,430,410)
mi_plataforma_dos = plataforma("recursos de mi juego\plataformas\\0.png",40,40,1050,380)
mi_plataforma_tercera = plataforma("recursos de mi juego\plataformas\plataforma alta.png",150,210,830,317)
mi_plataforma_cuatro = plataforma("recursos de mi juego\plataformas\\1_plataforma.png",550,50,1,200)
mi_plataforma_cinco = plataforma("recursos de mi juego\plataformas\\0.png",50,50,700,190)

#TRAMPAS

primer_trampa = plataforma("recursos de mi juego\enemigos-objetos\puas.png",230,70,980,459) 
segunda_trampa = plataforma("recursos de mi juego\enemigos-objetos\puas.png",100,70,730,459)

lados_mi_plataforma = obtener_rectangulos(mi_plataforma.rectangulo)
lados_plataforma_dos = obtener_rectangulos(mi_plataforma_dos.rectangulo)
lados_plataformas_tres = obtener_rectangulos(mi_plataforma_tercera.rectangulo)
lados_plataforma_cuatro = obtener_rectangulos(mi_plataforma_cuatro.rectangulo)
lados_plataforma_cinco = obtener_rectangulos(mi_plataforma_cinco.rectangulo)
lados_primer_trampa = obtener_rectangulos(primer_trampa.rectangulo)
lados_segunda_trampa = obtener_rectangulos(segunda_trampa.rectangulo)

lista_plataformas = [lados_piso,lados_mi_plataforma,lados_plataforma_dos,lados_plataformas_tres,
                    lados_plataforma_cuatro,lados_plataforma_cinco,lados_primer_trampa,
                    lados_segunda_trampa]

plataformas_creadas = [mi_plataforma,mi_plataforma_dos,mi_plataforma_tercera,mi_plataforma_cuatro,
                    mi_plataforma_cinco,primer_trampa,segunda_trampa]

listas_trampas = [lados_primer_trampa,lados_segunda_trampa]

####ENEMIGOS#############################################################3

enemigos = []

lista_enemigos_animaciones = [personaje_enemigo,pez_mirando_derecha,cangrejo,cangrejo_derecha]
reescalar_imagen(lista_enemigos_animaciones,40,35)

pez_pinches = enemigo(300,430,10,personaje_enemigo,pez_mirando_derecha,20,300)
enemigos.append(pez_pinches.obtener_diccionario())

pez_pinches_dos = enemigo(312,110,12,personaje_enemigo,pez_mirando_derecha,5,300)
enemigos.append(pez_pinches_dos.obtener_diccionario())

pez_pinches_tres = enemigo(700,110,12,personaje_enemigo,pez_mirando_derecha,700,900)
enemigos.append(pez_pinches_tres.obtener_diccionario())
 
mi_cangrejo = enemigo(436,375,15,cangrejo,cangrejo_derecha,436,600)
enemigos.append(mi_cangrejo.obtener_diccionario())

mi_cangrejo_dos = enemigo(310,165,10,cangrejo,cangrejo_derecha,10,400)
enemigos.append(mi_cangrejo_dos.obtener_diccionario())

mi_cangrejo_tres = enemigo(860,290,10,cangrejo,cangrejo_derecha,810,940)
enemigos.append(mi_cangrejo_tres.obtener_diccionario())


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
            que_hace = "derecha"  
        
        elif  (lista_eventos[pygame.K_LEFT] and sonic.rectangulo.left >  20 ):
            que_hace = "izquierda" 
        
        elif (lista_eventos[pygame.K_UP]):
            que_hace = "salta"
        
        else :
            que_hace = "quieto" 
            
        pantalla.blit(fondo,(0,0))
        
        murio = coalicion_enemigo(enemigos,lados_personaje,listas_trampas) 
        
        if murio == True:
            
            que_hace = "muriendo"
            
        if segundos == 60:
            tiempo = "terminado"
            
            if sonic.puntaje > 300 and len(lista_vidas) > 0:
                que_hace = "gano" 
            else:
                que_hace = "perdio"  
           
        actualizar_pantalla(pantalla,que_hace,sonic,fondo,lista_plataformas,plataformas_creadas,
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
        crear_sonido_fondo("recursos de mi juego\sonidos\\victory-sonic.mp3",1,0.1)
        
         
    else:
        
        mensaje_final = fuente_final.render(f"YOU LOSE",True,("white"))
            
        pantalla.blit(mensaje_final,(h/2 + 100, 200))
        
    
    pygame.display.flip()    



