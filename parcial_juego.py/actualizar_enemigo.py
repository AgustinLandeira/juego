
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
                
def actualizar_boss(pantalla,boss,segundos,vidas_boss,lados_personaje,lista_boss):
    
    crear_vida_boss(pantalla,vidas_boss)
    mover_boss(pantalla,boss,segundos,lados_personaje,lista_boss)

def mover_boss(pantalla,boss,segundos,lados_personaje,lista_boss):
    
    colisiono = False
    
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
                
                animar_enemigo(pantalla,malo["direccion_izquierda"],malo["rectangulo"])
                
            else:
                animar_enemigo(pantalla,boss_mas_velocidad_izquierda[0],malo["rectangulo"])
            
        elif malo["direccion"] == "derecha":
            
            if malo["aumento_velocidad"] != True:
                
                animar_enemigo(pantalla,malo["direccion_derecha"],malo["rectangulo"])
                
            else:
                animar_enemigo(pantalla,boss_mas_velocidad[0],malo["rectangulo"])
        
        if segundos >=10 and segundos <15 or segundos >= 26 and segundos < 50:
            
            malo["velocidad"] = 60
            malo["aumento_velocidad"] = True
            
        else:
            malo["velocidad"] = 20
            malo["aumento_velocidad"] = False
        
        colisiono = verificar_coalicion_con_boss(lista_boss,lados_personaje,colisiono)

    
def crear_vida_boss(pantalla,vidas_boss):
    
    for vida in vidas_boss:
        pantalla.blit(vida["superficie_vida"],(vida["posicion_x"],vida["posicion_y"]))
        
def verificar_coalicion_con_boss(lista_boss,lados_personaje,colisiono):
    
    for clave in lista_boss:
        
        if lados_personaje["bottom"].colliderect(clave["lados"]["top"]):
            print("colisiono arriba")
            colisiono = True
            break
            
        
        elif lados_personaje["main"].colliderect(clave["lados"]["left"]):
            print("colisiono con la parte izquierda del jefe")
            colisiono = True
            break
            
            
    return colisiono
    
            
            

    
                
                    
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
