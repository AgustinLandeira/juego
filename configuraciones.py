
import pygame
from POO import *


def obtener_rectangulos(principal):
    
    diccionario = {}
    
    diccionario['main'] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 8, principal.width, 8)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)
    
    return diccionario
    
                                                #sonic
def aplicar_gravedad(pantalla,personaje_animacion,sonic:pygame.Rect,pisos:list):
    
    global esta_saltando,desplazamiento_y
    
    if esta_saltando:
        animar_personaje(pantalla,sonic["main"],personaje_animacion)
        
        for lado in sonic:
            sonic[lado].y += desplazamiento_y
        
        if desplazamiento_y + gravedad < limite_velocidad_caida:
            desplazamiento_y += gravedad
        
    for plataforma in pisos: 
        if sonic["bottom"].colliderect(plataforma["top"]):
            esta_saltando = False
            desplazamiento_y = 0
            sonic["main"].bottom = plataforma["main"].top + 1
            break
        else:
            esta_saltando = True
            

def reescalar_imagen(lista_animaciones,w,h):
    
    for lista in lista_animaciones:
        
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale( imagen, (w,h) )
        
        
        

def girar_imagenes(lista_orginal,flip_x,flip_y):
    lista_girada = []
    
    for imagen in lista_orginal:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
        
    return lista_girada
    
    
def mover_personaje(sonic,velocidad):
    for lado in sonic:
        sonic[lado].x += velocidad

def animar_personaje(pantalla,sonic,accion_personaje): #accion de una array de imagenes
    global contador_pasos
    
    largo = (len(accion_personaje))
    
    if contador_pasos >= largo:
        contador_pasos = 0
        
    pantalla.blit(accion_personaje[contador_pasos],sonic) 
    contador_pasos += 1

                                                         #piso     #mi_plataforma
def actualizar_pantalla(pantalla,que_hace,sonic,fondo,plataformas,mi_plataforma,lados_personaje): # lista_plataforma,fondo,mi_plataforma):
    
    global direccion,desplazamiento_y,esta_saltando
    
    pantalla.blit(fondo,(0,0)) 
    
    pantalla.blit(mi_plataforma.plataforma,(mi_plataforma.rectangulo.x,mi_plataforma.rectangulo.y))

    if que_hace == "derecha":
        
        direccion = "derecha"
        
        if esta_saltando == False:
            animar_personaje(pantalla,lados_personaje["main"],personaje_corriendo)#,personaje_corriendo)
        mover_personaje(lados_personaje,sonic.velocidad)
        
    elif que_hace == "izquierda":
        
        direccion = "izquierda"
        
        if esta_saltando == False:
            animar_personaje(pantalla,lados_personaje["main"],personaje_corriendo_izquierda)
        
        mover_personaje(lados_personaje,sonic.velocidad*-1)
        
    elif que_hace == "salta":
        if not esta_saltando:
            esta_saltando = True
            desplazamiento_y = potencia_salto
            
        
    elif esta_saltando == False:
        if direccion == "derecha":
            
            animar_personaje(pantalla,lados_personaje["main"],personaje_quieto)
            
        else: 
            animar_personaje(pantalla,lados_personaje["main"],personaje_quieto_izquierda)
            
    if direccion == "derecha":
        
        aplicar_gravedad(pantalla,personaje_saltando,lados_personaje,plataformas)
    else:
        aplicar_gravedad(pantalla,personaje_saltando_izquierda,lados_personaje,plataformas)
        
    

contador_pasos = 0
direccion = "ninguna"

##SALTO

gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15
desplazamiento_y = 0
esta_saltando = False
###########

personaje_corriendo_izquierda = girar_imagenes(personaje_corriendo,True,False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True,False)
personaje_saltando_izquierda =girar_imagenes(personaje_saltando,True,False)