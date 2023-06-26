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

fps = 250 

pygame.init()

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((w,h))

#fuente
font = pygame.font.Font(None, 30)
fuente_final = pygame.font.SysFont("pixel-font", 100)

#tiempo
tiempo_transcurrido = pygame.time.get_ticks()
clock = pygame.time.Clock()

#fondo
fondo = pygame.image.load("recursos de mi juego\\background\\fondo nivel 3.png")
fondo =pygame.transform.scale(fondo,(w,h))

pantalla.blit(fondo,(0,0))

#SONIDO PARA EL FONDO
crear_sonido_fondo("recursos de mi juego\sonidos\sonic-gumball.mp3",-1,0.1)

#PERSONAJE

lista_animaciones = [personaje_quieto,personaje_quieto_izquierda,personaje_corriendo,
                    personaje_corriendo_izquierda,personaje_saltando,personaje_saltando_izquierda,
                    personaje_muriendo,celebracion,celebracion]

reescalar_imagen(lista_animaciones,36,45) 

sonic = personaje(h/2 - 120,350,20,0,-27,27,4) 
que_hace = "quieto"
posicion_Actual =0

lados_personaje = obtener_rectangulos(sonic.rectangulo)

#SUPERFICIE
#piso
piso = pygame.Rect(0,0,w,20)

lados_piso = obtener_rectangulos(piso)


#plataforma
mi_plataforma = plataforma("recursos de mi juego\plataformas\plat_nivel_2(2).png",100,30,430,250)

mi_plataforma_dos = plataforma("recursos de mi juego\plataformas\plat_nivel_2(4).png",500,30,1000,400)#

mi_plataforma_tercera = plataforma("recursos de mi juego\plataformas\plat_nivel_2(5).png",50,20,860,300)

mi_plataforma_cuatro = plataforma("recursos de mi juego\plataformas\plat_nivel_2(5).png",300,30,1,400)#

mi_plataforma_cinco = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",300,30,1,200)

mi_plataforma_seis = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",500,30,410,400)#

mi_plataforma_siete = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",50,30,680,240)


#TRAMPAS

primer_trampa = plataforma("recursos de mi juego\enemigos-objetos\lava.png",1200,90,1,500) 

#LISTA DE LAS PLATAFORMAS
plataformas_creadas = [mi_plataforma,mi_plataforma_dos,mi_plataforma_tercera,mi_plataforma_cuatro,
                    mi_plataforma_cinco,mi_plataforma_seis,mi_plataforma_siete,primer_trampa]


#LADOS
lados_mi_plataforma = obtener_rectangulos(mi_plataforma.rectangulo)
lados_plataforma_dos = obtener_rectangulos(mi_plataforma_dos.rectangulo)
lados_plataformas_tres = obtener_rectangulos(mi_plataforma_tercera.rectangulo)
lados_plataforma_cuatro = obtener_rectangulos(mi_plataforma_cuatro.rectangulo)
lados_plataforma_cinco = obtener_rectangulos(mi_plataforma_cinco.rectangulo)
lados_plataforma_seis = obtener_rectangulos(mi_plataforma_seis.rectangulo)
lados_plataforma_siete = obtener_rectangulos(mi_plataforma_siete.rectangulo)
lados_primer_trampa = obtener_rectangulos(primer_trampa.rectangulo)


lista_lados = [lados_piso,lados_mi_plataforma,lados_plataforma_dos,lados_plataformas_tres,
                    lados_plataforma_cuatro,lados_plataforma_cinco,lados_plataforma_seis,
                    lados_plataforma_siete,lados_primer_trampa]

listas_trampas = [lados_primer_trampa]

####ENEMIGOS#############################################################

enemigos = []

lista_enemigos_animaciones = [personaje_enemigo,pez_mirando_derecha,cangrejo,cangrejo_derecha,pelota_fuego,
                            pelota_fuego_derecha,bombardero]

reescalar_imagen(lista_enemigos_animaciones,37,35)

pelotita_fuego = enemigo(870,350,40,pelota_fuego,pelota_fuego_derecha,10,950)
enemigos.append(pelotita_fuego.obtener_diccionario())

mi_bombardero = enemigo(450,30,12,bombardero,bombardero,5,300)
enemigos.append(mi_bombardero.obtener_diccionario())

pez_pinches = enemigo(700,240,12,pez_nivel2,pez_nivel2_derecha,600,990)
enemigos.append(pez_pinches.obtener_diccionario())
 
mi_orbinaut = enemigo(436,300,15,orbinaut,orbinaut_derecha,200,650)
enemigos.append(mi_orbinaut.obtener_diccionario())

mi_orbinaut2 = enemigo(1100,170,20,orbinaut,orbinaut_derecha,400,900)
enemigos.append(mi_orbinaut2.obtener_diccionario())

bombardero2 = enemigo(860,30,10,bombardero,bombardero,810,940)
enemigos.append(bombardero2.obtener_diccionario())

bombardero3 = enemigo(760,30,10,bombardero,bombardero,700,800)
enemigos.append(bombardero3.obtener_diccionario())

tirador = enemigo(800,160,5,pistolero_izquierda,pistolero_izquierda,700,900)
enemigos.append(tirador.obtener_diccionario())

boss = jefe(950,350,20,the_boss_izquierda,the_boss,5,1000)

#DISPAROS
lista_proyectiles = []


fuego = proyectil(20,20,mi_bombardero.rectangulo.x,mi_bombardero.rectangulo.y,15,
        "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")
lista_proyectiles.append(fuego.obtener_diccionario())

fuego_2 = proyectil(20,20,bombardero2.rectangulo.x,bombardero2.rectangulo.y,20,
                    "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")
lista_proyectiles.append(fuego_2.obtener_diccionario())

fuego_3 = proyectil(20,20,bombardero3.rectangulo.x,bombardero3.rectangulo.y,20,
                    "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")
lista_proyectiles.append(fuego_3.obtener_diccionario())

bala = proyectil(20,20,tirador.rectangulo.x,tirador.rectangulo.y,40,
                "recursos de mi juego\enemigos-objetos\\bala.png",1,"tirador")
lista_proyectiles.append(bala.obtener_diccionario())

bombarderos = [mi_bombardero,bombardero2,bombardero3,tirador]

lista_de_bombarderos=[]

for bombarder in bombarderos:
    lista_de_bombarderos.append(bombarder.obtener_diccionario())
    
#################################################################################

#ANILLOS

lista_anillos = crear_anillos("nivel tres")
anillos_creados,items_creados = hacer_lluvia_objetos(30,10)
lista_vacia = False

#VIDAS
lista_vidas = []
for i in range(3):
    una_vida = sonic.obtener_vidas()
    lista_vidas.append(una_vida)

#eventos
tick = pygame.USEREVENT + 0 # se crea el evento
pygame.time.set_timer(tick,100) # se lanza cada milisegundos
 

animacion_hecha = False 
tiempo = "no terminado"  
running = True

while running:
    
    segundos = (pygame.time.get_ticks() - tiempo_transcurrido) // 1000  # Tiempo transcurrido en segundos
    reloj.tick(fps)
        
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
    
    lista_eventos = pygame.key.get_pressed()
        
    if tiempo != "terminado":
        
        if (lista_eventos[pygame.K_RIGHT] and sonic.rectangulo.right < w - sonic.velocidad):
            que_hace = "derecha"  
        
        elif  (lista_eventos[pygame.K_LEFT] and sonic.rectangulo.left >  20 ):
            que_hace = "izquierda" 
        
        elif (lista_eventos[pygame.K_UP]):
            que_hace = "salta"
        else :
            que_hace = "quieto" 
            
        if (lista_eventos[pygame.K_UP]) and (lista_eventos[pygame.K_RIGHT]):
            que_hace = "salta" 
        
            
        elif (lista_eventos[pygame.K_UP]) and (lista_eventos[pygame.K_RIGHT]):
            que_hace = "salta"     
            
        pantalla.blit(fondo,(0,0))
        
        murio = coalicion_enemigo(enemigos,lados_personaje,listas_trampas)
    
        
        if murio == True:
            
            que_hace = "muriendo" 
            
        if segundos == 60:
            tiempo = "terminado"
            
            if sonic.puntaje > 500 and len(lista_vidas) > 0:
                que_hace = "gano"
            else:
                que_hace = "perdio"
            
            
        actualizar_pantalla(pantalla,que_hace,sonic,fondo,lista_lados,plataformas_creadas,lados_personaje,
                            lista_vidas,tiempo)
        
        actualizar_enemigo(enemigos,pantalla)
        actualizar_boss(pantalla,boss,segundos)
        
        disparo(lista_proyectiles,pantalla,lados_personaje,sonic,lista_vidas,lista_de_bombarderos)
        
        animar_anillos(pantalla,lista_anillos,anillos,items_creados,item_recuperar_vida)
        
        verificar_coalicion(lista_anillos,lados_personaje,sonic,items_creados,lista_vidas)
        
        if get_mode():
            
            mostrar_lados_2(lista_lados,enemigos,lados_personaje,lados_primer_trampa,listas_trampas,pantalla)
                    
        text = font.render(f"Tiempo: {segundos} segundos", True, ("red"))
        
        score = font.render(f"puntaje: {sonic.puntaje} puntos", True, ("red"))
        vidas_restantes = font.render(f"vidas:",True, ("red"))
        
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
    
        
    elif sonic.puntaje > 500 and len(lista_vidas) > 0:
        
        mensaje_final = fuente_final.render(f"YOU WIN",True,("white"))
        
        pantalla.blit(mensaje_final,(h/2 + 100, 200))
        
    else:
        mensaje_final = fuente_final.render(f"YOU LOSE",True,("white"))
            
        pantalla.blit(mensaje_final,(h/2 + 100, 200))
        
    pygame.display.flip()
        











