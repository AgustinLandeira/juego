import pygame
import time
import json

from listas import *
from sonido import *
from actualizar_enemigo import *
from actualizar_anillos import *
from modo import * 
from editar import *

class Nivel:
    
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo,lados_personaje,
                plataformas_creadas,lista_trampas,enemigos,lista_enemigos_animaciones,lista_anillos
                ,anillos_creados,items_creados,lista_vacia,lista_vidas,lista_animaciones, tiempo,muertes,
                lista_de_bombarderos,lista_proyectiles,boss,lista_boss,vidas_boss,path):
        
        self._slave = pantalla
        self.jugador = personaje_principal
        self.lista_plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.lados_personaje = lados_personaje
        self.plataformas_creadas = plataformas_creadas
        self.listas_trampas = lista_trampas
        self.enemigos = enemigos
        self.lista_enemigos_animaciones = lista_enemigos_animaciones
        self.lista_anillos = lista_anillos
        self.anillos_creados = anillos_creados
        self.items = items_creados
        self.lista_vacia = lista_vacia
        self.lista_vidas = lista_vidas
        self.lista_animaciones = lista_animaciones
        self.tiempo_transcurrido = pygame.time.get_ticks()
        self.segundos = (pygame.time.get_ticks() - self.tiempo_transcurrido) // 1000  # Tiempo transcurrido en segundos
        self.font = pygame.font.Font(None, 30)
        self.fuente_final = pygame.font.SysFont("pixel-font", 100)
        self.text = self.font.render(f"Tiempo: {self.segundos} segundos", True, ("red"))
        self.tiempo = tiempo
        self.ultima_colision = 0
        self.retraso_colision = 2.0
        self.contador_muertes = muertes
        self.aclaracion = pygame.font.SysFont("pixel-font", 20)
        self.lista_vacia = False
        self.segundos_pasados = ""
        self.lista_proyectiles = lista_proyectiles
        self.lista_de_bombarderos = lista_de_bombarderos
        self.boss = boss
        self.lista_boss = lista_boss
        self.vidas_boss = vidas_boss
        self.path = path
    
       
    def update(self,lista_eventos):
        
        if self.tiempo != "terminado":
            obtener_puntaje_limite = False
            
            for evento in lista_eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_TAB:
                        cambiar_modo()
            
            self.segundos = (pygame.time.get_ticks() - self.tiempo_transcurrido) // 1000
            
            ##fuente
            text = self.font.render(f"Tiempo: {self.segundos} segundos", True, ("orange"))
            vidas_restantes = self.font.render(f"vidas:",True, ("orange"))
            score = self.font.render(f"puntaje: {self.jugador.puntaje} puntos", True, ("orange"))
            
            self.leer_input(lista_eventos)
            self.actualizar_pantalla()
            
            if self.boss != None:
                vidas_del_boss = self.font.render(f"boss:",True, ("red"))
                self._slave.blit(vidas_del_boss,(1020,70))
            
            self._slave.blit(text,(0,0))
            self._slave.blit(score, (1020, 10))
            self._slave.blit(vidas_restantes,(1020,50))
            
            
            self.dibujar_rectangulos()
            
            if self.lista_proyectiles != None:
                disparo(self.lista_proyectiles,self._slave,self.lados_personaje,self.jugador,self.lista_vidas,self.lista_de_bombarderos)
            
            animar_anillos(self._slave,self.lista_anillos,anillos,self.items,item_recuperar_vida)
            verificar_coalicion(self.lista_anillos,self.lados_personaje,self.jugador,self.items,self.lista_vidas)
            actualizar_enemigo(self.enemigos,self._slave)
            
            if self.boss != None:
                actualizar_boss(self._slave,self.segundos,self.vidas_boss,self.lados_personaje,self.lista_boss,self.lista_vidas,self.jugador)
            
            if  self.segundos < 11 :
            
                objetivo = self.aclaracion.render(f"""Mision: agarra los anillos para llegar a 300 puntos como minimo para pasar al siguiente nivel""",True,("black"))
                self._slave.blit(objetivo,(300,10))

            if self.segundos >= 15 and self.segundos < 30 or self.segundos > 40 and self.segundos <59:
                mover_objeto(self.anillos_creados,self.items)

            for un_anillo in self.anillos_creados:
                self._slave.blit(un_anillo["superficie"],un_anillo["rectangulo"])
                
            if not self.anillos_creados:

                self.lista_vacia = True

            if self.lista_vacia  == True:
                self.anillos_creados,self.items = hacer_lluvia_objetos(35,2)
                self.lista_vacia = False
            
            verificar_coalicion(self.anillos_creados,self.lados_personaje,self.jugador,self.items,self.lista_vidas)

            if self.lista_vidas == []:
                self.tiempo = "terminado"
                self.segundos_pasados = "no cuenta porque no pudo sobrevivir a  el nivel"
                
            elif self.jugador.puntaje == 300 and obtener_puntaje_limite == False :
                self.segundos_pasados = self.segundos
                obtener_puntaje_limite = True 
        
        else:
            self.mostrar_resultado()
        
    def actualizar_pantalla(self):
    
        colision = False
        
        self._slave.blit(self.img_fondo,(0,0)) 
        
        for objeto in self.plataformas_creadas:
            
            self._slave.blit(objeto.plataforma,(objeto.rectangulo.x,objeto.rectangulo.y))
        
        if self.jugador.accion == "muriendo":
            
            tiempo_actual = time.time()
            
            if tiempo_actual - self.ultima_colision >= self.retraso_colision:
            
                self.jugador.mover_personaje(self.lados_personaje,self.jugador.velocidad,True)
                self.jugador.sacar_vida(self.lista_vidas)
                sonido_daño("recursos de mi juego\sonidos\daño.wav")
                
                self.ultima_colision = tiempo_actual
                
        elif self.jugador.accion == "derecha":
        
            self.jugador.direccion = "derecha"
            
            if self.jugador.esta_saltando == False and self.tiempo != "terminado":
                
                self.jugador.animar_personaje(self._slave,self.lados_personaje["main"],self.lista_animaciones[2],self.jugador)
                
            for lado in self.lista_plataformas:#?
                
                if self.lados_personaje["right"].colliderect(lado["left"]):
                    sonido_advertencia("recursos de mi juego\sonidos\\no.wav")
                    colision = True
                    break
                
            if  colision == False:    
                self.jugador.mover_personaje(self.lados_personaje,self.jugador.velocidad,False)
                
        elif self.jugador.accion == "izquierda":
        
            colision = False
        
            self.jugador.direccion = "izquierda"
        
            if self.jugador.esta_saltando == False and self.tiempo != "terminado":
                self.jugador.animar_personaje(self._slave,self.lados_personaje["main"],self.lista_animaciones[3],self.jugador)
                
            for lado in self.lista_plataformas:
                if self.lados_personaje["left"].colliderect(lado["right"]):
                    sonido_advertencia("recursos de mi juego\sonidos\\no.wav")
                    colision = True
                    break
                
            if not colision:  
                self.jugador.mover_personaje(self.lados_personaje,self.jugador.velocidad*-1,False)
        
        elif self.jugador.accion == "salta" and self.tiempo != "terminado" :
        
            if not self.jugador.esta_saltando:
                
                self.jugador.esta_saltando = True
                
                self.jugador.desplazamiento_y = self.jugador.potencia_salto
                
                sonido_saltando("recursos de mi juego\sonidos\SN_Act008.wav")
        
        elif self.jugador.accion == "gano":
            self.jugador.animar_personaje(self._slave,self.lados_personaje["main"],self.lista_animaciones[7],self.jugador)
    
        elif self.jugador.accion == "perdio":
            self.jugador.animar_personaje(self._slave,self.lados_personaje["main"],self.lista_animaciones[8],self.jugador)
                        
        elif self.jugador.esta_saltando == False and  self.tiempo != "terminado":
            
            if self.jugador.direccion == "derecha":
                
                self.jugador.animar_personaje(self._slave,self.lados_personaje["main"],self.lista_animaciones[0],self.jugador)
                
            else: 
                self.jugador.animar_personaje(self._slave,self.lados_personaje["main"],self.lista_animaciones[1],self.jugador)
        
        if self.jugador.direccion == "derecha" and  self.tiempo != "terminado":
        
            self.jugador.aplicar_gravedad(self.lista_animaciones[4],self.jugador,
                    self.lista_plataformas,self.lados_personaje,self._slave)
        else:
            if self.tiempo != "terminado":
                
                self.jugador.aplicar_gravedad(self.lista_animaciones[5],
                    self.jugador,self.lista_plataformas,self.lados_personaje,self._slave)
        
        self.jugador.vidas_personaje(self.lista_vidas,self._slave)        
        
    def leer_input(self,lista_eventos):
        
        lista_eventos = pygame.key.get_pressed()

        if (lista_eventos[pygame.K_RIGHT] and self.jugador.rectangulo.right < 1180 - self.jugador.velocidad):
            self.jugador.accion = "derecha"  

        elif (lista_eventos[pygame.K_LEFT] and self.jugador.rectangulo.left >  20 ):
            self.jugador.accion = "izquierda" 

        elif (lista_eventos[pygame.K_UP]):
            self.jugador.accion = "salta"

        else :
            self.jugador.accion = "quieto" 

        self.jugador.murio = coalicion_enemigo(self.enemigos,self.lados_personaje,self.listas_trampas)
        
        if self.jugador.murio == True:

            self.jugador.accion = "muriendo"
            self.contador_muertes += 1
        
        if self.segundos == 60 or self.lista_vidas == []:
            self.tiempo = "terminado"

            if self.jugador.puntaje > 300 and len(self.lista_vidas) > 0:
                
                self.jugador.accion = "gano"
                crear_sonido_fondo("recursos de mi juego\sonidos\\victory-sonic.mp3",1,0.1) 
                
            else:
                self.jugador.accion = "perdio"
            
    def dibujar_rectangulos(self):
        
        if get_mode() == True:
            
            mostrar_lados_1(self.lista_plataformas,self.enemigos,self.lados_personaje,self.listas_trampas,self._slave)

    def mostrar_resultado(self):
        
        if self.jugador.puntaje > 300 and len(self.lista_vidas) > 0:
        
            mensaje_final = self.fuente_final.render(f"YOU WIN",True,("white"))
            
            self._slave.blit(mensaje_final,(600/2 + 100, 200))

        else:
            
            mensaje_final = self.fuente_final.render(f"YOU LOSE",True,("white"))
                
            self._slave.blit(mensaje_final,(600/2 + 100, 200))
        
        pygame.display.flip()
        
        un_dato = {}
        un_dato = ({"puntos":self.jugador.puntaje,
                                        "muertes": self.contador_muertes,
                                        "segundos en obtener el puntaje requerido":self.segundos_pasados,
                                        "tiempo jugado":self.segundos})
        
        try:
            with open(self.path,"w") as file:
                json.dump(un_dato,file,indent = 4)
            
        except:
            print("hubo un error al escribir los datos de la partida")
  



###########


personaje_corriendo_izquierda = girar_imagenes(personaje_corriendo,True,False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True,False)
personaje_saltando_izquierda =girar_imagenes(personaje_saltando,True,False)           
                
