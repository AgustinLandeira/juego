import pygame
from modo import *
import time
from listas import *
from sonido import *
from pantalla_original import *
from actualizar_enemigo import *
from actualizar_anillos import *

class Nivel:
    
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo,lados_personaje,
                plataformas_creadas,lista_trampas,enemigos,lista_enemigos_animaciones,lista_anillos
                ,anillos_creados,items_creados,lista_vacia,lista_vidas):
        
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.lados_personaje = lados_personaje
        self.plataformas_creadas = plataformas_creadas
        self.lista_trampas = lista_trampas
        self.enemigos = enemigos
        self.lista_enemigos_animaciones = lista_enemigos_animaciones
        self.lista_anillos = lista_anillos
        self.anillos_creados = anillos_creados
        self.items = items_creados
        self.lista_vacia = lista_vacia
        self.lista_vidas = lista_vidas
        
       
    def update(self,lista_eventos,tiempo,segundos,text,font):
        
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        
        
        self.leer_input(segundos)
        self.actualizar_pantalla(tiempo,segundos)
        
        actualizar_enemigo(self.enemigos,self._slave)
        
        animar_anillos(self._slave,self.lista_anillos,anillos,self.items,item_recuperar_vida)
        
        verificar_coalicion(self.lista_anillos,self.lados_personaje,self.jugador,self.items,self.lista_vidas)
        
        score = font.render(f"puntaje: {self.jugador.puntaje} puntos", True, ("black"))
        vidas_restantes = font.render(f"vidas:",True, ("black"))
        
        self._slave.blit(text, (0, 0))
        self._slave.blit(score, (1020, 10))
        self._slave.blit(vidas_restantes,(1020,50))
        
        if segundos >= 15 and segundos < 30 or segundos > 40 and segundos <59:
            mover_objeto(self.anillos_creados,self.items)
            
            for un_anillo in self.anillos_creados:
                self._slave.blit(un_anillo["superficie"],un_anillo["rectangulo"])
        
        if not self.anillos_creados:
           
            lista_vacia = True
        
        if lista_vacia  == True:
            
            anillos_creados,items_creados = hacer_lluvia_objetos(35,2)
            lista_vacia = False
    
        verificar_coalicion(anillos_creados,self.lados_personaje,self.jugador,items_creados,self.lista_vidas)
        
        if self.lista_vidas == []:
            
            tiempo = "terminado"
        
        if segundos == 60 or self.lista_vidas == []:
            pass
            #mostrar_resultado()
    
    def mover_personaje(self,velocidad,murio):
    
        if murio == False:
            
            for lado in self.lados_personaje:
                self.lados_personaje[lado].x += velocidad
                
        else:
            for lado in self.lados_personaje:
                self.lados_personaje[lado].x = 600/2 - 250
    
    def actualizar_pantalla(self,tiempo,segundos):
        
        global esta_saltando,desplazamiento_y,ultima_colision,retraso_colision
    
        colision = False
        
        self._slave.blit(self.img_fondo,(0,0))
        
        for plataforma in self.plataformas:
            plataforma.draw(self._slave,self.plataformas)
        
        self.jugador.update(self._slave,self.plataformas)
        self._slave.blit(self.img_fondo,(0,0)) 
        
        for objeto in self.plataformas_creadas:
            
            self._slave.blit(objeto.plataforma,(objeto.rectangulo.x,objeto.rectangulo.y))
        
        if self.jugador.accion == "muriendo":
            
            tiempo_actual = time.time()
            
            if tiempo_actual - ultima_colision >= retraso_colision:
            
                mover_personaje(self.lados_personaje,self.jugador.velocidad,True)
                sacar_vida(self.lista_vidas)
                crear_sonido_coalicion_anillo("recursos de mi juego\sonidos\daño.wav",1)
                
                ultima_colision = tiempo_actual
            
        elif self.jugador.accion == "derecha":
            
            self.jugador.direccion = "derecha"
            
            if esta_saltando == False and tiempo != "terminado":
                
                animar_personaje(self._slave,self.lados_personaje["main"],personaje_corriendo,self.jugador)
                
            for lado in self.plataformas:
                
                if self.lados_personaje["right"].colliderect(lado["left"]):
                    sonido_advertencia("recursos de mi juego\sonidos\\no.wav",1)
                    colision = True
                    break
                
            if  colision == False:    
                mover_personaje(self.lados_personaje,self.jugador.velocidad,False)
            
        elif self.jugador.accion == "izquierda":
            
            colision = False
            
            self.jugador.direccion = "izquierda"
            
            if esta_saltando == False and tiempo != "terminado":
                animar_personaje(self._slave,self.lados_personaje["main"],personaje_corriendo_izquierda,self.jugador)
                
            for lado in self.plataformas:
                if self.lados_personaje["left"].colliderect(lado["right"]):
                    sonido_advertencia("recursos de mi juego\sonidos\\no.wav",1)
                    colision = True
                    break
                
            if not colision:  
                mover_personaje(self.lados_personaje,self.jugador.velocidad*-1,False)
            
        elif self.jugador.accion == "salta" and tiempo != "terminado" :
            
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = self.jugador.potencia_salto
                
                sonido_saltando("recursos de mi juego\sonidos\SN_Act008.wav",1)
        
        elif self.jugador.accion == "gano":
            animar_personaje(self._slave,self.lados_personaje["main"],celebracion,self.jugador)
        
        elif self.jugador.accion == "perdio":
            animar_personaje(self._slave,self.lados_personaje["main"],perdio,self.jugador)
                        
        elif esta_saltando == False and  tiempo != "terminado":
            if self.jugador.direccion == "derecha":
                
                animar_personaje(self._slave,self.lados_personaje["main"],personaje_quieto,self.jugador)
                
            else: 
                animar_personaje(self._slave,self.lados_personaje["main"],personaje_quieto_izquierda,self.jugador)
                
        if self.jugador.direccion == "derecha" and  tiempo != "terminado":
            
            aplicar_gravedad(self._slave,personaje_saltando,self.lados_personaje,self.plataformas,self.jugador)
        else:
            if tiempo != "terminado":
                aplicar_gravedad(self._slave,personaje_saltando_izquierda,self.lados_personaje,self.plataformas,self.jugador)
            
        vidas_personaje(self.lista_vidas,self._slave)
    
    def leer_input(self,segundos):
        
        lista_eventos = pygame.key.get_pressed()

        if (lista_eventos[pygame.K_RIGHT] and self.jugador.rectangulo.right < 1200 - self.jugador.velocidad):
            self.jugador.accion = "derecha"  
        
        elif  (lista_eventos[pygame.K_LEFT] and self.jugador.rectangulo.left >  20 ):
            self.jugador.accion = "izquierda" 
        
        elif (lista_eventos[pygame.K_UP]):
            self.jugador.accion = "salta"
        
        else :
            self.jugador.accion = "quieto"
        
        murio = coalicion_enemigo(self.enemigos,self.lados_personaje,self.lista_trampas) 
        
        if murio == True:
            
            self.jugador.accion = "muriendo"
            
        if segundos == 60:
            
            tiempo = "terminado"
            
            if self.jugador.puntaje > 300 and len(self.lista_vidas) > 0:
                self.jugador.accion = "gano" 
            else:
                self.jugador.accion = "perdio"
    
    def dibujar_rectangulos(self,lista_plataformas,enemigos,lados_personaje,listas_trampas):
        
        if get_mode():
            mostrar_lados_1(lista_plataformas,enemigos,lados_personaje,listas_trampas,self._slave)

    def mostrar_resultado(self,fuente_final):
        if self.jugador.puntaje > 300 and len(self.lista_vidas) > 0:
        
            mensaje_final = fuente_final.render(f"YOU WIN",True,("white"))
            
            self._slave.blit(mensaje_final,(600/2 + 100, 200))
            crear_sonido_fondo("recursos de mi juego\sonidos\\victory-sonic.mp3",1,0.1)

        else:
            
            mensaje_final = fuente_final.render(f"YOU LOSE",True,("white"))
                
            self._slave.blit(mensaje_final,(600/2 + 100, 200))
            
    
        pygame.display.flip()  


     
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
                