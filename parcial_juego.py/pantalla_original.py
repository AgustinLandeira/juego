import pygame,sys
from POO import *
from sonido import *
from listas import *
import time

def agregar_vida(lista_vidas:list,sonic):
    
    """
    agrega una vida al personaje
    parametro: recibe la lista con vidas y el personaje al cual se le agregara las vidas  
    """ 
    
    if len(lista_vidas) < 3:
        
        una_vida = sonic.obtener_vidas()
        lista_vidas.append(una_vida)

def vidas_personaje(lista_de_vidas:list,pantalla:pygame.Surface):
    
    """
    muestra las vidas del personaje durante el juego
    parametros reciba una lista de las vidas que va a mostrar y una pantalla en donde las mostrara
    """
    
    for vida in lista_de_vidas:
        
        pantalla.blit(vida['superficie_vida'],(vida["posicion_x"], vida["posicion_y"]))

def sacar_vida(lista_vidas:list):
    """
    le saca una vida al personaje
    parametros: recibe una lista con las vidas en donde le sacara una
    """
    if lista_vidas:
        lista_vidas.pop(-1)
        
def obtener_rectangulos(principal:pygame.rect.Rect)->dict:
    
    """
    hace lados del rectangulo en cuestion ya sea plataformas,personaje etc
    parametros: recibe el rectangulo
    """
    diccionario = {}
    
    diccionario['main'] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 15, principal.width, 15)
    diccionario["right"] = pygame.Rect(principal.right -8, principal.top, 8, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 14, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 18) 
    
    return diccionario

def aplicar_gravedad(pantalla:pygame.Surface,personaje_animacion,lados_personaje:pygame.Rect,pisos:list,sonic):
    
    """
    le aplica la gravedad al personaje en donde le permitira saltar y desplazarse por el eje y
    parametros: recibe la pantalla,una animacion del personaje,sus lados,el piso y el personaje en cuestion
    """
    
    global esta_saltando,desplazamiento_y
    
    if esta_saltando:
        animar_personaje(pantalla,lados_personaje["main"],personaje_animacion,sonic)
               
        for lado in lados_personaje: 
            lados_personaje[lado].y += desplazamiento_y            
                
        if desplazamiento_y + sonic.gravedad < sonic.limite_velocidad_caida:
            
            desplazamiento_y += sonic.gravedad
                  
    for plataforma in pisos: 
        if lados_personaje["bottom"].colliderect(plataforma["top"]):
            esta_saltando = False
            desplazamiento_y = 0
            lados_personaje["main"].bottom = plataforma["main"].top + 5
            break 
        
        elif lados_personaje["top"].colliderect(plataforma["bottom"]):
           
            desplazamiento_y = 2
            break       
        else:
            esta_saltando = True               

def reescalar_imagen(lista_animaciones:list,w:int,h:int):
    
    """
    aumenta el ancho y alto de una imagen 
    parametro: recibe una lista con imagenes,ancho y alto
    """
    
    for lista in lista_animaciones:
        
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale( imagen, (w,h) )
        
def girar_imagenes(lista_orginal:list,flip_x:bool,flip_y:bool)->list:
    
    """
    gira las imagenes de izquierda a drecha o viceversa
    parametros: una lista con x y y
    
    """
    
    lista_girada = []
    
    for imagen in lista_orginal:
        lista_girada.append(pygame.transform.flip (imagen,flip_x,flip_y) )
        
    return lista_girada
       
def mover_personaje(sonic,velocidad:int,murio:bool):
    
    """
    se encarga de mover el personaje segun como le ordenenmos
    parametros: recibe los lados del personaje, su velocidad al que se va a mover y un booleano
    
    """
    
    if murio == False:
        
        for lado in sonic:
            sonic[lado].x += velocidad
            
    else:
        for lado in sonic:
            sonic[lado].x = 600/2 - 250

def animar_personaje(pantalla:pygame.Surface,lados_del_personaje,accion_personaje,sonic):
    
    largo = (len(accion_personaje))
    
    if sonic.contador_de_pasos >= largo:
        sonic.contador_de_pasos = 0
        
    pantalla.blit(accion_personaje[sonic.contador_de_pasos],lados_del_personaje) 
    sonic.contador_de_pasos += 1

def actualizar_pantalla(pantalla:pygame.Surface,sonic,fondo:pygame.surface.Surface
                        ,plataformas:list,plataformas_creadas:list,lados_personaje:dict,
                        lista_vidas:list,tiempo:int):
    
    """
    actualiza al personaje
    parametros: recibe una pantalla,el persona, un fondo,plataformas,los lados del personaje,vidas 
    y un tiempo
    """
    global esta_saltando,desplazamiento_y,ultima_colision,retraso_colision
    
    colision = False
    
    pantalla.blit(fondo,(0,0)) 
    
    for objeto in plataformas_creadas:
        
        pantalla.blit(objeto.plataforma,(objeto.rectangulo.x,objeto.rectangulo.y))
    
    if sonic.accion == "muriendo":
        
        tiempo_actual = time.time()
        
        if tiempo_actual - ultima_colision >= retraso_colision:
        
            mover_personaje(lados_personaje,sonic.velocidad,True)
            sacar_vida(lista_vidas)
            sonido_daño("recursos de mi juego\sonidos\daño.wav")
            
            ultima_colision = tiempo_actual
        
    elif sonic.accion == "derecha":
        
        sonic.direccion = "derecha"
        
        if esta_saltando == False and tiempo != "terminado":
            
            animar_personaje(pantalla,lados_personaje["main"],personaje_corriendo,sonic)
            
        for lado in plataformas:
            
            if lados_personaje["right"].colliderect(lado["left"]):
                sonido_advertencia("recursos de mi juego\sonidos\\no.wav")
                colision = True
                break
            
        if  colision == False:    
            mover_personaje(lados_personaje,sonic.velocidad,False)
        
    elif sonic.accion == "izquierda":
        
        colision = False
        
        sonic.direccion = "izquierda"
        
        if esta_saltando == False and tiempo != "terminado":
            animar_personaje(pantalla,lados_personaje["main"],personaje_corriendo_izquierda,sonic)
            
        for lado in plataformas:
            if lados_personaje["left"].colliderect(lado["right"]):
                sonido_advertencia("recursos de mi juego\sonidos\\no.wav")
                colision = True
                break
            
        if not colision:  
            mover_personaje(lados_personaje,sonic.velocidad*-1,False)
        
    elif sonic.accion == "salta" and tiempo != "terminado" :
        
        if not esta_saltando:
            esta_saltando = True
            desplazamiento_y = sonic.potencia_salto
            
            sonido_saltando("recursos de mi juego\sonidos\SN_Act008.wav")
    
    elif sonic.accion == "gano":
        animar_personaje(pantalla,lados_personaje["main"],celebracion,sonic)
    
    elif sonic.accion == "perdio":
        animar_personaje(pantalla,lados_personaje["main"],perdio,sonic)
                    
    elif esta_saltando == False and  tiempo != "terminado":
        if sonic.direccion == "derecha":
            
            animar_personaje(pantalla,lados_personaje["main"],personaje_quieto,sonic)
            
        else: 
            animar_personaje(pantalla,lados_personaje["main"],personaje_quieto_izquierda,sonic)
            
    if sonic.direccion == "derecha" and  tiempo != "terminado":
        
        aplicar_gravedad(pantalla,personaje_saltando,lados_personaje,plataformas,sonic)
    else:
        if tiempo != "terminado":
            aplicar_gravedad(pantalla,personaje_saltando_izquierda,lados_personaje,plataformas,sonic)
        
    vidas_personaje(lista_vidas,pantalla)
    
###################


##SALTO
desplazamiento_y = 0
esta_saltando = False

###########

### tiempo entre colisiones ####

ultima_colision = 0
retraso_colision = 2.0


personaje_corriendo_izquierda = girar_imagenes(personaje_corriendo,True,False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True,False)
personaje_saltando_izquierda =girar_imagenes(personaje_saltando,True,False)