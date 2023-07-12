from pygame.locals import *

from GUI_form import *
from GUI_button_image import *
from GUI_form_settings import formSettings

class formcontenedorNivel(Form):
    
    def __init__(self,pantalla:pygame.Surface,nivel):
        super().__init__(pantalla,0,0,pantalla.get_width(),pantalla.get_height())
        self.path = "recursos de mi juego\interfaz\HITE_sfx#11 (SFX_10_menu).wav"
        nivel._slave = self._slave
        self.nivel = nivel
        self.setting = False
        
        self.btn_home = Button_Image(screen=self._slave,
                                    master_x = self._x,
                                    master_y = self._y , 
                                    x = self._w-50,
                                    y =  self._h-50, 
                                    w=50,
                                    h=50,
                                    path_image="recursos de mi juego\\anillos\home.png",
                                    onclick=self.btn_home_click,
                                    onclick_param="",
                                    text="",
                                    font="Arial")
        
        self.btn_settings_game = Button_Image(screen = self._slave,
                                            master_x = self._x,
                                            master_y = self._y,
                                            x = 1160,
                                            y = 520,
                                            w = 30,
                                            h= 30,
                                            path_image = "recursos de mi juego\interfaz\configuracion.png",
                                            onclick=self.btn_setting,
                                            onclick_param="lalaala")
                                            #text="",
                                            #font="Arial")
                                            
        
        #self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self.btn_settings_game)
        self.lista_widgets.append(self.btn_home)
        
        
    def update(self,lista_eventos):
        if self.setting == False:
            self.nivel.update(lista_eventos)
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            if self.verificar_dialog_result():
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
            else:
                self.hijo.update(lista_eventos)
    
    def btn_setting(self,text):
        
        self.reproducir_sonido_boton()
        
        formulario_setting = formSettings(self._master,100,25,800,550,"Black","Black",True, self)
        self.setting = True
        self.show_dialog(formulario_setting)
        
    def btn_home_click(self, param):
        
        self.reproducir_sonido_boton()
        self.end_dialog()
        
    def reproducir_sonido_boton(self):
        sonido_colision = pygame.mixer.Sound(self.path)
        sonido_colision.play(0)

