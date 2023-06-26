import pygame
import random

def crear(x,y,ancho,alto,path):   #constructor
    imagen_dona = pygame.image.load(path) 
    imagen_dona = pygame.transform.scale(imagen_dona,(alto,ancho))
    rectangulo = imagen_dona.get_rect()
    rectangulo.x= x # coordenadas
    rectangulo.y = y
    
    diccionario_dona = {}
    diccionario_dona["superficie"] = imagen_dona
    diccionario_dona["rectangulo"] = rectangulo
    diccionario_dona["velocidad"] = random.randrange(10,20,1)
    
    return diccionario_dona

def crear_lista_dona(cantidad):
    lista_donas = []
    for i in range(cantidad):
        x = random.randrange(0,740,60)
        y = random.randrange(-1000,0,60)
        
        diccionario = crear(x,y,60,60,"Recursos_17\dona.png")
        lista_donas.append(diccionario)
        
    return lista_donas



'''def update(lista_donas):
    for dona in lista_donas:
        rect = dona["rectangulo"]
        rect.y += dona["velocidad"]'''
    

def actualizar_pantalla(lista_donas,personaje,ventana):
    for dona in lista_donas:
        
        if personaje["rectangulo_boca"].colliderect(dona["rectangulo"]):
            personaje["puntaje"] += 100
            sonido_coalicion = pygame.mixer.Sound("Recursos_17\eat2.mp3")
            sonido_coalicion.set_volume(0.2)
            sonido_coalicion.play()
            
            desaparecer_dona(dona)
            
        elif dona["rectangulo"].y > 720:
            desaparecer_dona(dona)
            
def desaparecer_dona(dona):
    dona["rectangulo"].x = random.randrange(0,740,60)    
    dona["rectangulo"].y = random.randrange(-1000,0,60) 
    