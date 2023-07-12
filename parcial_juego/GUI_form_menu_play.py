import pygame
from pygame.locals import *
import os
import json
from GUI_form import *
#from GUI_form_contenedor_nivel import ContenedorNivel
from GUI_button_image import *
from manejador_niveles import Manejador_niveles
from GUI_form_contenedor_niveles import formcontenedorNivel
from editar import reescalar_imagen


class formMenuPlay(Form):
    
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w, h))
        self._slave = aux_image
        self.nivel1_desbloqueado = True
        self.nivel2_desbloqueado = False
        self.nivel3_desbloqueado = False #
        self.primera_vuelta = False
        self.path = "recursos de mi juego\interfaz\HITE_sfx#11 (SFX_10_menu).wav"
        
        candado_bloqueado = [pygame.image.load("recursos de mi juego\\interfaz\\locked.png")]
        candado_desbloqueado = [pygame.image.load("recursos de mi juego\\interfaz\\unlocked.png")]
        self.lista_candado = []
        self.lista_candado.append(candado_bloqueado)
        
        self.lista_candado.append(candado_desbloqueado)
        
        reescalar_imagen(self.lista_candado,50,60)
        
        self.dibujar_candado()
        
        if self.primera_vuelta == False:
            un_dato = {}
            un_dato = ({"puntos":0,
                        "muertes": 0,
                        "segundos en obtener el puntaje requerido":0,
                        "tiempo jugado":0})
            
            try:
                with open("parcial_juego\datos_partida\\nivel_1.json","w") as file:
                    json.dump(un_dato,file,indent = 4)
                
            except:
                print("hubo un error al escribir los datos de la partida")
            
            try:
                with open("parcial_juego\datos_partida\\nivel_2..json","w") as file:
                    json.dump(un_dato,file,indent = 4)
                
            except:
                print("hubo un error al escribir los datos del segundo nivel de la partida")
                
            self.primera_vuelta = True
            
        self.btn_nivel_uno = Button_Image(screen=self._slave,
                                        x=200,
                                        y=50,
                                        master_x = x,
                                        master_y = y,
                                        w=200,
                                        h=150,
                                        onclick=self.entrar_nivel,
                                        onclick_param="nivel uno",
                                        path_image="recursos de mi juego\interfaz\level_1.png",
                                        text="",
                                        font="Arial")

        self.btn_nivel_dos = Button_Image(screen=self._slave,
                                        x=500,
                                        y=50,
                                        master_x=x,
                                        master_y=y,
                                        w=200,
                                        h=150,
                                        path_image="recursos de mi juego\interfaz\level_2.png",
                                        onclick=self.entrar_nivel,
                                        onclick_param="nivel dos", 
                                        text="",
                                        font="Arial")

        self.btn_nivel_tres = Button_Image(screen=self._slave,
                                        x=800,
                                        y=50,   
                                        master_x=x,
                                        master_y=y,
                                        w=200,
                                        h=150,
                                        color_background=(255, 0, 0),
                                        color_border=(255, 0, 255),
                                        path_image="recursos de mi juego\interfaz\level_3.png",
                                        onclick=self.entrar_nivel,
                                        onclick_param="nivel tres",
                                        text="",
                                        font="Arial",
                                        font_size=15,
                                        font_color=(0, 255, 0))

        self.btn_home = Button_Image(screen=self._slave,
                                    master_x=x,
                                    master_y=y,
                                    x=1100,
                                    y=500,
                                    w=100,
                                    h=100,
                                    path_image="recursos de mi juego\\anillos\home.png",
                                    onclick=self.btn_home_click,
                                    onclick_param="",
                                    text="",
                                    font="Arial")

        self.lista_widgets.append(self.btn_nivel_uno)
        self.lista_widgets.append(self.btn_nivel_dos)
        self.lista_widgets.append(self.btn_nivel_tres)
        
        self.lista_widgets.append(self.btn_home)
     
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def entrar_nivel(self, nombre_nivel):
        
        self.reproducir_sonido_boton()
        
        if nombre_nivel == "nivel uno" and self.nivel1_desbloqueado == True:
            
            nivel = self.manejador_niveles.get_nivel(nombre_nivel)
            frm_contenedor_nivel = formcontenedorNivel(self._master,nivel)
            self.show_dialog(frm_contenedor_nivel)
           
        with open("parcial_juego\datos_partida\\nivel_1.json","r") as archivo:
            
            datos = json.load(archivo)
            resultado = datos['segundos en obtener el puntaje requerido']
            self.tiempo_jugado = datos["tiempo jugado"]
            
            if resultado != "no cuenta porque no pudo sobrevivir a  el nivel" and self.tiempo_jugado == 60:
                self.nivel2_desbloqueado = True
                self.dibujar_candado()
                
        if nombre_nivel == "nivel dos" and self.nivel2_desbloqueado == True: 
            
            nivel = self.manejador_niveles.get_nivel(nombre_nivel)
            frm_contenedor_nivel = formcontenedorNivel(self._master,nivel)
            self.show_dialog(frm_contenedor_nivel)
        
        with open("parcial_juego\datos_partida\\nivel_2..json","r") as archivo:
            
            datos = json.load(archivo)
            resultado = datos['segundos en obtener el puntaje requerido']
            self.tiempo_jugado = datos["tiempo jugado"]
            
            if resultado != "no cuenta porque no pudo sobrevivir a  el nivel" and self.tiempo_jugado == 60:
                self.nivel3_desbloqueado = True
                self.dibujar_candado()
        
        if nombre_nivel == "nivel tres" and self.nivel3_desbloqueado == True: 
            
            nivel = self.manejador_niveles.get_nivel(nombre_nivel)
            frm_contenedor_nivel = formcontenedorNivel(self._master,nivel)
            self.show_dialog(frm_contenedor_nivel)
    

    def btn_home_click(self, param):
       
        self.reproducir_sonido_boton()
        
        self.end_dialog()
    
    def reproducir_sonido_boton(self):
        sonido_colision = pygame.mixer.Sound(self.path)
        sonido_colision.play(0)
        
    def dibujar_candado(self):
        
        if self.nivel1_desbloqueado == True:
            candado = self.lista_candado[1]
            self._slave.blit(candado[0],(230,200))
        
        if self.nivel2_desbloqueado == False:
            candado = self.lista_candado[0]
            self._slave.blit(candado[0],(550,200))
        
        else:
            candadoo = self.lista_candado[1]
            self._slave.blit(candadoo[0],(550,200))
            
        if self.nivel3_desbloqueado == False:
            candado = self.lista_candado[0]
            self._slave.blit(candado[0],(840,200))
        
        else:
            candadoo = self.lista_candado[1]
            self._slave.blit(candadoo[0],(840,200))
            
    
    