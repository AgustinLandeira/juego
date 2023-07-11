import pygame
from pygame.locals import *
from GUI_button import *
#from gui.GUI_button import *
from GUI_textbox import *
from GUI_slider import *
from GUI_label import *
from GUI_button_image import *
from GUI_form import *
from gui_form_menu_score import *
from GUI_form_menu_play import *
from GUI_picture_box import PictureBox
from GUI_form_settings import *



class formPrueba(Form):
    def __init__(self,screen,x,y,w,h,color_background,color_border = "black",border_size = -1,active = True):
        super().__init__(screen,x,y,w,h,color_background,color_border,border_size,active)
        
        self.volumen = 0.2
        self.flag_play = True
    
        ####################controles######
        #self.txtbox = TextBox(self._slave,x,y,50,50,150,30,"gray","white","red","blue",2,font = "Comic Sans",font_size=15,font_color="black")
        #self.btn_play = Button(self._slave,x,y,100,100,100,50,"red","blue",self.btn_play_click,"Nombre","pause",font="Verdana",font_size=15,font_color="White")
        
        self.btn_settings = Button_Image(self._slave,x,y,900,500,150,100,"recursos de mi juego\interfaz\settings.png",self.btn_setting,"lalaala")
        self.btn_tabla = Button_Image(self._slave,x,y,530,500,150,100,"recursos de mi juego\interfaz\play.png",self.btn_tabla_click,"lalaala")
        self.btn_ranking = Button_Image(self._slave,x,y,200,500,150,100,"recursos de mi juego\interfaz\\ranking.png",self.btn_tabla_click,"lalaala")
        self.picture_box = PictureBox(self._slave, 0, 0, 1200, 600, "recursos de mi juego\interfaz\pantalla_inicio.png")
        
        
        ##########################
        
        ##### agrego los controles a la lista
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_settings)
        self.lista_widgets.append(self.btn_ranking)
        #self.lista_widgets.append(self.txtbox)
        #self.lista_widgets.append(self.btn_play)
        #self.lista_widgets.append(self.lebel_volumen)
        #self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla )
        ############################################
        pygame.mixer.music.load("recursos de mi juego\interfaz\sonic_1_intro.mp3")
        
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
         
        self.render()
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)    
                #self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
    def render(self):
        self._slave.fill(self._color_background) 
    
    def btn_play_click(self,texto):
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
    
    def btn_setting(self,lista_eventos):
        
        formulario_setting = formSettings(self._master,100,25,800,550,"Black","Black",True)
        self.show_dialog(formulario_setting)
        
        ''' self.volumen = self.slider_volumen.value
        #self.lebel_volumen.update(lista_eventos)
        self.lebel_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)'''
    
    '''def update_volumen(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        #self.lebel_volumen.update(lista_eventos)
        self.lebel_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)'''
        
    def btn_tabla_click(self,texto):
        '''dic_store = [{"jugador":"gio","score":1000},
                    {"jugador":"fausto","score":500},
                    {"jugador":"gonza","score":750}
                    ]   '''
        fmr_jugar = formMenuPlay(screen = self._master,
                    x = 0, 
                    y = 0, 
                    w = 1200,
                    h = 600,
                    color_background=(220,0,220),
                    color_border=(255,255,255),
                    active = True,path_image="recursos de mi juego\interfaz\menu_play_1.png")
        self.show_dialog(fmr_jugar)
        '''form_puntaje =  FormMenuScore(self._master,
                                    250,
                                    25,
                                    500,
                                    550,
                                    (220,0,220),
                                    "white",
                                    True,
                                    "recursos de mi juego\Window.png",
                                    dic_store,
                                    100,
                                    10,
                                    10
                                    )
        
        self.show_dialog(form_puntaje)'''
     