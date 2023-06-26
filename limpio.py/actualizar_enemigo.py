
from pantalla_original import *
from listas import *

def coalicion_enemigo(lista_enemigo,lados_personaje,lados_trampas):
    
    booleano = False
    
    for enemigo in lista_enemigo:  
        
        if lados_personaje["main"].colliderect(enemigo["lados"]["main"]):
            print("colisiono con el enemigo")
            booleano = True
            break
        for lado in lados_trampas:
            if lados_personaje["main"].colliderect(lado["main"]):
                print("colisiono con la trampa")
                booleano = True
                
    return booleano                

def animar_enemigo(pantalla,accion,enemigo):
    
    pantalla.blit(accion,enemigo)

def mover_enemigo(enemigo,pantalla):
    
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
                
def actualizar_enemigo(enemigos,pantalla):
    
    mover_enemigo(enemigos,pantalla)

def disparo(lista_proyectiles,pantalla,lados_personaje,sonic,lista_vidas,bombarderos):

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
                crear_sonido_coalicion_anillo("recursos de mi juego\sonidos\daño.wav",1)
        
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
                crear_sonido_coalicion_anillo("recursos de mi juego\sonidos\daño.wav",1)
                
def actualizar_boss(pantalla,boss,segundos):
    
    mover_boss(pantalla,boss,segundos)

def mover_boss(pantalla,boss,segundos):
    
    
    if boss.rectangulo.x > boss.limite_izquierda and boss.bandera == False:
        
        boss.rectangulo.x -= boss.velocidad
        boss.direccion = "izquierda"
    else:
        boss.bandera = True
    
    if boss.rectangulo.x < boss.limite_derecha and boss.bandera == True:
        
        boss.rectangulo.x += boss.velocidad
        boss.direccion = "derecha"
    else:
        boss.bandera = False
        
    if boss.direccion == "izquierda":
        if boss.aumento_velocidad != True:
            animar_enemigo(pantalla,boss.direccion_izquierda,boss.rectangulo)
        else:
            animar_enemigo(pantalla,boss_mas_velocidad_izquierda[0],boss.rectangulo)
        
    elif boss.direccion == "derecha":
        if boss.aumento_velocidad != True:
            animar_enemigo(pantalla,boss.direccion_derecha,boss.rectangulo)
        else:
            animar_enemigo(pantalla,boss_mas_velocidad[0],boss.rectangulo)
    
    if segundos >=10 and segundos <15 or segundos >= 26 and segundos < 50:
        boss.velocidad = 60
        boss.aumento_velocidad = True
        
    else:
        boss.velocidad = 20
        boss.aumento_velocidad = False
    


    
                
                    
    ###################################################################3


pez_mirando_derecha = girar_imagenes(personaje_enemigo,True,False)
cangrejo_derecha = girar_imagenes(cangrejo,True,False)
pelota_fuego_derecha = girar_imagenes(pelota_fuego,True,False)
pez_nivel2_derecha = girar_imagenes(pez_nivel2,True,False)
orbinaut_derecha = girar_imagenes(orbinaut,True,False)
pistolero_izquierda = girar_imagenes(pistolero,True,False)
the_boss_izquierda = girar_imagenes(the_boss,True,False)
boss_mas_velocidad_izquierda = girar_imagenes(boss_mas_velocidad,True,False)
tirador_izquierda = girar_imagenes(pistolero,True,False)
