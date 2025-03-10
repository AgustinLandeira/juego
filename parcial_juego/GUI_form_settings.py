import pygame
from pygame.locals import *

from GUI_form import *
from GUI_button_image import *
from GUI_label import *
from GUI_slider import *
from GUI_picture_box import * 

# Variable para almacenar el volumen actual
current_volume = 0.2

class formSettings(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active,contenedor_nivel = None):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.path = "recursos de mi juego\interfaz\HITE_sfx#11 (SFX_10_menu).wav"
        self.contenedor_nivel = contenedor_nivel
        self.volumen = current_volume  # Utiliza el volumen actual almacenado
        self.flag_play = True
        self.picture_box = PictureBox(self._slave, 0, 0, 800, 600, "recursos de mi juego\interfaz\\0.png")
        self.btn_play = Button(self._slave, x, y, 200, 150, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pausa", font="Verdana", font_size=15, font_color="White")
        self.label_volumen = Label(self._slave, 620, 260, 180, 100, f"{round(self.volumen * 100)}%", "Comic Sans", 15, "White", "recursos de mi juego\interfaz\marco.png")
        self.slider_volumen = Slider(self._slave,x,y,100,300,500,15,self.volumen,"Blue","White")
        self.btn_home = Button_Image(screen=self._slave,
                                    master_x=self._x,
                                    master_y=self._y,
                                    x=self._w-150,
                                    y=self._h-160,
                                    w=100,
                                    h=100,
                                    path_image="recursos de mi juego\\anillos\home.png",
                                    onclick=self.btn_home_click,
                                    onclick_param="",
                                    text="",
                                    font="Arial",
                                    )
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_home)           
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        
    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")
                
        self.flag_play = not self.flag_play
                    
    def update_volumen(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
        # Actualiza la variable de volumen actual
        global current_volume
        current_volume = self.volumen
            
    def update(self,lista_eventos):
        
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)
    
    def btn_home_click(self,param):
        
        self.reproducir_sonido_boton()
        
        if self.contenedor_nivel != None:
            self.contenedor_nivel.setting = False  # Establecer self.setting en False
            self.end_dialog()
        self.end_dialog()
        
    def reproducir_sonido_boton(self):
        sonido_colision = pygame.mixer.Sound(self.path)
        sonido_colision.play(0) 