
from pantalla_original import *
from listas import *
#from crear_objetos_enem import *
#from imagenes_giradas import *
import time

def coalicion_enemigo(lista_enemigo:list,lados_personaje:dict,lados_trampas:dict)->bool:
    
    """
    verifica si colisiono con un enemigo o una trampa
    parametros: una lista de enemigos,los lados del personaje y los lados de las trampas
    retorna un booleano que va a decir si colisiono o no
    """
    booleano = False
    
    for enemigo in lista_enemigo:  
        
        if lados_personaje["main"].colliderect(enemigo["lados"]["main"]):
            
            booleano = True
            break
        for lado in lados_trampas:
            if lados_personaje["main"].colliderect(lado["main"]):
                
                booleano = True
                
    return booleano                

def animar_enemigo(pantalla:pygame.Surface,accion,enemigo):
    """
    se va a encargar de animar las acciones del enemigo
    parametro: una pantalla en donde se va a blitear, la accion del enemigo y el rectangulo del enemigo
    
    """
    pantalla.blit(accion,enemigo)

def mover_enemigo(enemigo:list,pantalla:pygame.Surface):
    """
    mueve al enemigo en eje x
    parametros: recibe una lista de enemigos con sus caracteristicas
    """
    for enemy in enemigo:
        
        if enemy["rectangulo"].x > enemy["limite_izquierda"] and enemy["bandera"] == False:
            
            for lado in enemy["lados"]:
                enemy["lados"][lado].x -= enemy["velocidad"]
                
            enemy["direccion"] = "izquierda"
            
        else:
            enemy["bandera"] = True
                
        if enemy["rectangulo"].x < enemy["limite_derecha"] and enemy["bandera"] == True:  
              
            for lado in enemy["lados"]:
                
                enemy["lados"][lado].x += enemy["velocidad"]  
            enemy["direccion"] = "derecha"
            
        else:
            enemy["bandera"] = False
                
        if enemy["direccion"] == "izquierda":
            
            animar_enemigo(pantalla, enemy["direccion_izquierda"], enemy["rectangulo"])
            
        else:
            animar_enemigo(pantalla, enemy["direccion_derecha"], enemy["rectangulo"])
                
def actualizar_enemigo(enemigos:list,pantalla:pygame.Surface):
    """ empieza a actualizar al  enemigo mediante una funcion """
    mover_enemigo(enemigos,pantalla)

def disparo(lista_proyectiles:list,pantalla:pygame.Surface,lados_personaje:dict,sonic,lista_vidas:list,bombarderos:list):
    
    """
    se encarga de mover los proyectiles en eje x o eje y,ademas si choca con el personaje
    parametros: una lista de proyectiles, la pantalla en donde se blitea,lados del personaje,una lista
    de vidas y lista de bombarderos que serian los enemigos que disparan
    
    """

    for bombardero,proyectil in zip(bombarderos,lista_proyectiles):                
                   
        if proyectil["personaje"] == "bombardero":
            
            proyectil["rectangulo"].y += proyectil["velocidad"]
            
            if proyectil["rectangulo"].y >proyectil["limite"]:
                
                proyectil["rectangulo"].x = bombardero["rectangulo"].x
                proyectil["rectangulo"].y = bombardero["rectangulo"].y + 10
            
            pantalla.blit(proyectil["superficie"],proyectil["rectangulo"])
            
            if proyectil["rectangulo"].colliderect(lados_personaje["main"]):
                
                mover_personaje(lados_personaje,sonic.velocidad,True)
                
                proyectil["rectangulo"].x = bombardero["rectangulo"].x
                proyectil["rectangulo"].y = bombardero["rectangulo"].y + 10
                sacar_vida(lista_vidas)
                sonido_daño("recursos de mi juego\sonidos\daño.wav")
        
        elif proyectil["personaje"] == "tirador":
            
            proyectil["rectangulo"].x -= proyectil["velocidad"]
            
            if proyectil["rectangulo"].x < proyectil["limite"]:
                
                proyectil["rectangulo"].x = bombardero["rectangulo"].x
                proyectil["rectangulo"].y = bombardero["rectangulo"].y + 10
            
            pantalla.blit(proyectil["superficie"],proyectil["rectangulo"])
            
            if proyectil["rectangulo"].colliderect(lados_personaje["main"]):
                
                mover_personaje(lados_personaje,sonic.velocidad,True)
                
                proyectil["rectangulo"].x = bombardero["rectangulo"].x
                proyectil["rectangulo"].y = bombardero["rectangulo"].y + 10
                sacar_vida(lista_vidas)
                sonido_daño("recursos de mi juego\sonidos\daño.wav")
                
def actualizar_boss(pantalla:pygame.Surface,segundos:int,vidas_boss,lados_personaje:dict,lista_boss:list,
                    lista_vidas:list,sonic):
    
    """
    empieza a actualizar el boss llamando funciones
    parametros: una pantalla en donde se va a blitear,los segundos,las vidas del jefe,lados del personaje
    una lista que contiene al jefe adentro y otra de vidas
    """
    
    crear_vida_boss(pantalla,vidas_boss)
    mover_boss(pantalla,segundos,lados_personaje,lista_boss,vidas_boss,lista_vidas,sonic)

def animar_boss(pantalla:pygame.Surface,accion,enemigo):
    
    """
    anima la accion del jefe
    parametro: l pantalla en donde se blitea todo, la accion del jefe y el rectangulo
    """
    pantalla.blit(accion,enemigo)
        
def mover_boss(pantalla:pygame.Surface,segundos:int,lados_personaje:dict,lista_boss:list,vidas_boss,
            lista_vidas:list,sonic):
    
    """
    se encarga de mover al boss en eje x
    parametros: recibe una pantalla en donde se blitea,lados del personaje,lista con el jefe,
    vidas del jefe y una lista con sus vidas
    """
    
    colisiono = False
    
    if colisiono == False:
        
        for malo in lista_boss:
            
            if malo["rectangulo"].x > malo["limite_izquierda"] and malo["bandera"] == False:
                
                for lado in malo["lados"]:
                    malo["lados"][lado].x -= malo["velocidad"]
        
                malo["direccion"]= "izquierda"
                
            else:
                malo["bandera"] = True
            
            if malo["rectangulo"].x < malo["limite_derecha"] and malo["bandera"] == True:
                
                for lado in malo["lados"]:
                    malo["lados"][lado].x += malo["velocidad"]
    
                malo["direccion"] = "derecha"
                
            else:
                malo["bandera"] = False
                
            if malo["direccion"] == "izquierda":
                
                if malo["aumento_velocidad"] != True:
                    
                    animar_boss(pantalla,malo["direccion_izquierda"],malo["rectangulo"])
                    
                else:
                    animar_boss(pantalla,boss_mas_velocidad_izquierda[0],malo["rectangulo"])
                
            elif malo["direccion"] == "derecha":
                
                if malo["aumento_velocidad"] != True:
                    
                    animar_boss(pantalla,malo["direccion_derecha"],malo["rectangulo"])
                    
                else:
                    animar_boss(pantalla,boss_mas_velocidad[0],malo["rectangulo"])
                    
                if segundos >=10 and segundos <15 or segundos >= 26 and segundos < 50:
                    
                    malo["velocidad"] = 45
                    malo["aumento_velocidad"] = True
                    
                else:
                    malo["velocidad"] = 20
                    malo["aumento_velocidad"] = False
                
                colisiono = verificar_coalicion_con_boss(lista_boss,lados_personaje,colisiono,vidas_boss,
                                                        lista_vidas,sonic)
    
                if colisiono == True:
                    
                    animar_boss(pantalla,vida_perdida_boss[0],malo["rectangulo"])
        
                    for lado in malo["lados"]:
                        malo["lados"][lado].x = 850
        
def crear_vida_boss(pantalla:pygame.Surface,vidas_boss:list):
    
    """
    muestra las vidas que tiene el jefe
    parametro: recibe la pantalla en donde se blitea y las vidas del jefe
    """
    
    for vida in vidas_boss:
        pantalla.blit(vida["superficie_vida"],(vida["posicion_x"],vida["posicion_y"]))
        
def verificar_coalicion_con_boss(lista_boss:list,lados_personaje:dict,colisiono:bool,
                                vidas_boss,lista_vidas:list,sonic):
    
    """
    verifica si el boss choco con el personaje
    parametro: una lista que contendra al jefe,lados del personaje, si colisiono,vidas del jefe,
    lista con vidas
    
    """
    
    
    global ultima_colision,retraso_colision
    
    murio = False
    
    for clave in lista_boss:
        
        if lados_personaje["bottom"].colliderect(clave["lados"]["top"]):
            
            print("choco arriba")
            colisiono = True
            sacar_vida_boss(vidas_boss,lista_boss)
            
            break
        
        elif lados_personaje["main"].colliderect(clave["lados"]["main"]):
            
            murio = True
            tiempo_actual = time.time()
    
            if tiempo_actual - ultima_colision >= retraso_colision:
                
                sacar_vida(lista_vidas)
                mover_personaje(lados_personaje,sonic.velocidad,murio)
                
                ultima_colision = tiempo_actual
                
                daño_del_boss("recursos de mi juego\sonidos\hahah.wav")
                sonido_daño("recursos de mi juego\sonidos\daño.wav")
                
                break
        
            
            
    return colisiono

def sacar_vida_boss(vidas_boss,lista_boss):
    """
    saca las vidas del jefe 
    parametro: recibe una lista con las vidas restantes que temndra el jefe
    """
    if len(vidas_boss) != 1 :
        
        vidas_boss.pop(-1)
        
        daño_al_boss("recursos de mi juego\sonidos\daño_uno.wav")
    else:
        
        eliminar_boss(lista_boss)
          
def eliminar_boss(lista_boss:list):
    
    """ elimina al boss si pierde todas las vidas """
    
    muerte_boss("recursos de mi juego\sonidos\\negacion.wav")
    
    for boss in lista_boss:
        
        lista_boss.remove(boss)
    
### tiempo entre colisiones ####

ultima_colision = 0
retraso_colision = 4.0

pez_mirando_derecha = girar_imagenes(personaje_enemigo,True,False)
cangrejo_derecha = girar_imagenes(cangrejo,True,False)
pelota_fuego_derecha = girar_imagenes(pelota_fuego,True,False)
pez_nivel2_derecha = girar_imagenes(pez_nivel2,True,False)
orbinaut_derecha = girar_imagenes(orbinaut,True,False)
pistolero_izquierda = girar_imagenes(pistolero,True,False)
the_boss_izquierda = girar_imagenes(the_boss,True,False)
boss_mas_velocidad_izquierda = girar_imagenes(boss_mas_velocidad,True,False)
tirador_izquierda = girar_imagenes(pistolero,True,False)

