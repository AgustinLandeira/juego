import pygame
from listas import *
from sonido import *
from listas import *
from NIVELES import*
from editar import *



class personaje:
    def __init__(self,x_inicial,y_inicial,velocidad,puntaje,potencia_salto,limite_caida,gravedad,accion,murio):
        
        self.x = x_inicial
        self.y = y_inicial
        self.velocidad = velocidad
        self.rectangulo = personaje_corriendo[0].get_rect()
        self.rectangulo.x = self.x
        self.rectangulo.y = self.y
        self.puntaje = puntaje
        self.superficie_vida = pygame.image.load("recursos de mi juego\enemigos-objetos\\vidas.png")
        self.superficie_vida = pygame.transform.scale(self.superficie_vida,(20,20))
        self.rectangulo_vida = self.superficie_vida.get_rect()
        self.rectangulo_vida.x = 1050
        self.rectangulo_vida.y = 50
        self.contador_de_pasos = 0
        self.direccion = "ninguna"
        self.potencia_salto = potencia_salto
        self.limite_velocidad_caida = limite_caida
        self.gravedad = gravedad
        self.accion = accion
        self.murio = murio
        self.desplazamiento_y = 0
        self.esta_saltando = False
        self.lados_personaje = obtener_rectangulos(self.rectangulo)
        
    def obtener_vidas(self):
        
        self.rectangulo_vida.x += 30
        return{
            "superficie_vida": self.superficie_vida,
            "rectangulo_vida": self.rectangulo_vida,
            "posicion_x": self.rectangulo_vida.x,
            "posicion_y": self.rectangulo_vida.y
        }
    
    def agregar_vida(self,lista_vidas:list,sonic):
        
        """
        agrega una vida al personaje
        parametro: recibe la lista con vidas y el personaje al cual se le agregara las vidas  
        """ 
        
        if len(lista_vidas) < 3:
            
            una_vida = sonic.obtener_vidas()
            lista_vidas.append(una_vida)

    def vidas_personaje(self,lista_de_vidas:list,pantalla:pygame.Surface):
        
        """
        muestra las vidas del personaje durante el juego
        parametros reciba una lista de las vidas que va a mostrar y una pantalla en donde las mostrara
        """
        
        for vida in lista_de_vidas:
            
            pantalla.blit(vida['superficie_vida'],(vida["posicion_x"], vida["posicion_y"]))

    def sacar_vida(self,lista_vidas:list):
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

    def aplicar_gravedad(self,personaje_animacion,jugador,pisos,lados_personaje,pantalla):
        '''pantalla:pygame.Surface,personaje_animacion,lados_personaje:pygame.Rect
                        ,pisos:list,sonic'''
        
        """
        le aplica la gravedad al personaje en donde le permitira saltar y desplazarse por el eje y
        parametros: recibe la pantalla,una animacion del personaje,sus lados,el piso y el personaje en cuestion
        """
        
        if jugador.esta_saltando:
            
            self.animar_personaje(pantalla,lados_personaje["main"],personaje_animacion,jugador)
                
            for lado in lados_personaje: 
                lados_personaje[lado].y += jugador.desplazamiento_y            
                    
            if jugador.desplazamiento_y + jugador.gravedad < jugador.limite_velocidad_caida:
                
                jugador.desplazamiento_y += jugador.gravedad
                    
        for plataforma in pisos: 
            if lados_personaje["bottom"].colliderect(plataforma["top"]):
                jugador.esta_saltando = False
                jugador.desplazamiento_y = 0
                lados_personaje["main"].bottom = plataforma["main"].top + 5
                break 
            
            elif lados_personaje["top"].colliderect(plataforma["bottom"]):
            
                jugador.desplazamiento_y = 2
                break       
            else:
                jugador.esta_saltando = True               

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
        
    def mover_personaje(self,lados_personaje,velocidad,murio):
        
        """
        se encarga de mover el personaje segun como le ordenenmos
        parametros: recibe los lados del personaje, su velocidad al que se va a mover y un booleano
        
        """
        
        if murio == False:
            
            for lado in lados_personaje:
                lados_personaje[lado].x += velocidad
                
        else:
            for lado in lados_personaje:
                lados_personaje[lado].x = 600/2 - 250

    def animar_personaje(self,pantalla:pygame.Surface,lados_del_personaje,accion_personaje,sonic):
        
        largo = (len(accion_personaje))
        
        if sonic.contador_de_pasos >= largo:
            sonic.contador_de_pasos = 0
            
        pantalla.blit(accion_personaje[sonic.contador_de_pasos],lados_del_personaje) 
        sonic.contador_de_pasos += 1


###################


##SALTO

esta_saltando = False


personaje_corriendo_izquierda = girar_imagenes(personaje_corriendo,True,False)
personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True,False)
personaje_saltando_izquierda =girar_imagenes(personaje_saltando,True,False)
                    

        
        
        
            