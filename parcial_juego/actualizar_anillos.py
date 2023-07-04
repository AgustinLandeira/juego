import random
import pygame
#clase_anillo e item
from clases.clase_anillo import anillo
from clases.clase_item import item_vida
from pantalla_original import agregar_vida
from sonido import * 


def crear_anillos(nivel:str):
    
    """
    ordena los anillos segun el ordenamiento que tenga la lista de cada nivel
    parametro: recibe el tipo de nivel 1,2 o 3
    """
    
    lista_anillos = []
    if nivel == "nivel uno":
        
        anillos = [
            (15,20,20,436,365),  # Cantidad, ancho, alto, x, y 0
            (10, 20, 20, 900, 140),#1
            (9, 20, 20, 940, 140),#2
            (8, 20, 20, 860, 140),#3
            (16, 20, 20, 1, 180),#4
            (17, 20, 20, 1, 140),#5
            (18, 20, 20, 1, 100),#6
            (5, 20, 20, 580, 140),#7
            (5, 20, 20, 630, 140),#8
            (6, 20, 20, 1060, 250)#9
        ]
        
    elif nivel == "nivel dos":
        anillos = [
            (15,20,20,400,270),
            (10, 20, 20, 900, 30),#1
            (10, 20, 20, 940, 30),#2
            (8, 20, 20, 860, 50),#3
            (16, 20, 20, 1, 180),#4
            (17, 20, 20, 1, 140),#5
            (18, 20, 20, 1, 80),#6
            (5, 20, 20, 580, 140),#7
            (5, 20, 20, 630, 140),#8
            (6, 20, 20, 1100, 100)#9
        ]
    else:
        anillos = [
            (15,20,20,400,350),
            (10, 20, 20, 1000, 200),#1
            (10, 20, 20, 1050, 200),#2
            (5, 20, 20, 860, 210),#3
            (16, 20, 20, 1, 180),#4
            (17, 20, 20, 1, 140),#5
            (18, 20, 20, 1, 100),#6
            (5, 20, 20, 580, 140),#7
            (5, 20, 20, 630, 140),#8
            (10, 20, 20, 1100, 200)#9
        ]
    
    cantidad, ancho, alto,x,y = anillos[0]
    mover_x = 0
    mover_y = 0

    for i in range(cantidad):
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png", ancho, alto, x + mover_x, y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        mover_x += 20
        
    cantidad, ancho, alto,x,y = anillos[1] 
       
    for f in range(cantidad):
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x,y + mover_y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        mover_y += 20    
        
    mover_y = 0
    cantidad, ancho, alto,x,y = anillos[2]
    
    for j in range(cantidad):
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x,y + mover_y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        mover_y += 20
        
    mover_y = 0
    cantidad, ancho, alto,x,y = anillos[3]
    
    for h in range(cantidad):
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x,y + mover_y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        mover_y += 20
        
    mover_x = 0
    cantidad, ancho, alto,x,y = anillos[4]
    
    for i in range(cantidad):
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x + mover_x,y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        mover_x += 20
        
    mover_x = 0
    cantidad, ancho, alto,x,y = anillos[5]
    
    for i in range(cantidad):
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x + mover_x,y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        mover_x += 20
            
    mover_x = 0
    cantidad, ancho, alto,x,y = anillos[6]
    
    for i in range(cantidad):
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x + mover_x,y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        mover_x += 20
        
    mover_y = 0
    cantidad, ancho, alto,x,y = anillos[7]
    
    for j in range(cantidad):
        
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x,y + mover_y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        
        mover_y += 20
        
    mover_y = 0
    cantidad, ancho, alto,x,y = anillos[8]
    
    for j in range(cantidad):
        
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x,y + mover_y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        
        mover_y += 20
        
    mover_y = 0
    cantidad, ancho, alto,x,y = anillos[9]
    
    for j in range(cantidad):
        
        mi_anillo = anillo("recursos de mi juego\\anillos\\anillo_1.png",ancho,alto,x,y + mover_y)
        lista_anillos.append(mi_anillo.obtener_diccionario())
        
        mover_y += 20

    return lista_anillos    

def animar_anillos(pantalla:pygame.Surface,lista_anillos:list,anillos:list,lista_items:list,item:list):
    
    """
    blitea los anillos e items
    parametro: pantalla en donde se va a blitear,una lista con anillos,lista de items
    """
    global contador
    
    for ring in lista_anillos:
        
        if contador >= len(anillos):
            
            contador = 0
        
        pantalla.blit(anillos[0],ring["rectangulo"])
    
    for items in lista_items:
        
        pantalla.blit(item[0],items["rectangulo"])
    
        
contador = 0

def verificar_coalicion(lista_anillos:list,lados_personaje:dict,sonic,lista_items:list,lista_vidas:list):
    
    """
    verifica si hay una colision de items o anillos con el personaje y lo elimina
    parametros: 
    """   
        
    for anillo in lista_anillos:
        
        if lados_personaje["main"].colliderect(anillo["rectangulo"]):
            lista_anillos.remove(anillo)
            crear_sonido_coalicion_anillo("recursos de mi juego\sonidos\sonic.mp3")
            sonic.puntaje += 10
            
        elif anillo["rectangulo"].y > 600:
            
            lista_anillos.remove(anillo)
            
    
    if sonic.puntaje == 100:
        
        crear_sonido_coalicion_anillo("recursos de mi juego\sonidos\yes.wav")
    
    for item in lista_items:
        
        if lados_personaje["main"].colliderect(item["rectangulo"]):
            lista_items.remove(item)
            agregar_vida(lista_vidas,sonic)
            
        elif item["rectangulo"].y > 600:
            lista_items.remove(item)
            
                

def mover_objeto(anillos_creados:list,lista_items:list):
    
    """
    mueve los objetos ya sea anillos o items en el eje y
    parametros: recibe dos listas
    """
    
    for anillo in anillos_creados:
        
        rectangulo = anillo["rectangulo"]
        rectangulo.y += anillo["velocidad"]
    
    for item in lista_items:
        
        rectangulo = item["rectangulo"]
        rectangulo.y += item["velocidad"]

def hacer_lluvia_objetos(cantidad_anillos,cantidad_items)->list:
    
    """
    se encarga de hacer la lluvia de anillos e items para que el personaje pueda agarrarlos
    """
    
    anillos_creados = []
    items_creados = []
    
    for i in range(cantidad_anillos):
        
        x = random.randrange(-200, 1400 )
        y = random.randrange(-200, 0 )
        
        anillo_creado = anillo("recursos de mi juego\\anillos\\anillo_1.png",20,20,x,y)
        diccionario = anillo_creado.obtener_diccionario()
        anillos_creados.append(diccionario)
    
    for i in range(cantidad_items):
        
        x = random.randrange(-200, 1400 )
        y = random.randrange(-200, 0 )
        
        item = item_vida("recursos de mi juego\enemigos-objetos\\recuperar vida.png",20,20,x,y)
        diccionario = item.obtener_diccionario()
        items_creados.append(diccionario)
        
        
    return anillos_creados,items_creados


        

