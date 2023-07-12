import pygame

from listas import *


def girar_imagenes(lista_orginal:list,flip_x:bool,flip_y:bool)->list:
    
    """
    gira las imagenes de izquierda a drecha o viceversa
    parametros: una lista con x y y
    
    """
    
    lista_girada = []
    
    for imagen in lista_orginal:
        lista_girada.append(pygame.transform.flip (imagen,flip_x,flip_y) )
        
    return lista_girada

def obtener_rectangulos(principal:pygame.rect.Rect)->dict:
        
        """
        hace lados del rectangulo en cuestion ya sea plataformas,personaje etc
        parametros: recibe el rectangulo
        """
        diccionario = {}
        
        diccionario['main'] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 15, principal.width, 15)
        diccionario["right"] = pygame.Rect(principal.right -9, principal.top, 9, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 14, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 18) 
        
        return diccionario
    
def reescalar_imagen(lista_animaciones:list,w:int,h:int):
    
    """
    aumenta el ancho y alto de una imagen 
    parametro: recibe una lista con imagenes,ancho y alto
    """
    
    for lista in lista_animaciones:
        
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale( imagen, (w,h) )

def obtener_rectangulos_boss(principal:pygame.rect.Rect):
    diccionario = {}
        
    diccionario['main'] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 15, principal.width, 15)
    diccionario["right"] = pygame.Rect(principal.right -7, principal.top, 7, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 14, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6) 
    
    return diccionario




pez_mirando_derecha = girar_imagenes(personaje_enemigo,True,False)
cangrejo_derecha = girar_imagenes(cangrejo,True,False)
pelota_fuego_derecha = girar_imagenes(pelota_fuego,True,False)
pez_nivel2_derecha = girar_imagenes(pez_nivel2,True,False)
orbinaut_derecha = girar_imagenes(orbinaut,True,False)
pistolero_izquierda = girar_imagenes(pistolero,True,False)
the_boss_izquierda = girar_imagenes(the_boss,True,False)
boss_mas_velocidad_izquierda = girar_imagenes(boss_mas_velocidad,True,False)
tirador_izquierda = girar_imagenes(pistolero,True,False)


personaje_corriendo_izquierda = girar_imagenes(personaje_corriendo,True,False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True,False)
personaje_saltando_izquierda =girar_imagenes(personaje_saltando,True,False)