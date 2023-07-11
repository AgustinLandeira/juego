
from clases.clase_enemigo import enemigo
from listas import *
from actualizar_enemigo import *
from clases.clase_boss import jefe
from clases.clase_proyectil import proyectil
from clases.clase_plataforma import plataforma

from editar import obtener_rectangulos
from editar import girar_imagenes
from editar import reescalar_imagen


##############PLATAFORMAS y tramas ############
def crear_plataformas_nivel1(lados_piso:dict)->list:
    
    """
    crea distintas plataformas y trampas para el nivel uno llamando a la clase plataforma
    parametro: recibe los lados del piso
    """
    
    mi_plataforma = plataforma("recursos de mi juego\plataformas\\1_plataforma.png",300,75,430,410)
    
    mi_plataforma_dos = plataforma("recursos de mi juego\plataformas\\0.png",40,40,1050,380)
    
    mi_plataforma_tercera = plataforma("recursos de mi juego\plataformas\plataforma alta.png",150,210,830,317)
    
    mi_plataforma_cuatro = plataforma("recursos de mi juego\plataformas\\1_plataforma.png",550,50,1,200)
    
    mi_plataforma_cinco = plataforma("recursos de mi juego\plataformas\\0.png",50,50,700,190)

    #TRAMPAS

    primer_trampa = plataforma("recursos de mi juego\enemigos-objetos\puas.png",230,70,980,459) 
    
    segunda_trampa = plataforma("recursos de mi juego\enemigos-objetos\puas.png",100,70,730,459)

    lados_mi_plataforma = obtener_rectangulos(mi_plataforma.rectangulo)
    
    lados_plataforma_dos = obtener_rectangulos(mi_plataforma_dos.rectangulo)
    
    lados_plataformas_tres = obtener_rectangulos(mi_plataforma_tercera.rectangulo)
    
    lados_plataforma_cuatro = obtener_rectangulos(mi_plataforma_cuatro.rectangulo)
    
    lados_plataforma_cinco = obtener_rectangulos(mi_plataforma_cinco.rectangulo)
    
    lados_primer_trampa = obtener_rectangulos(primer_trampa.rectangulo)
    
    lados_segunda_trampa = obtener_rectangulos(segunda_trampa.rectangulo)

    lista_plataformas = [lados_piso,lados_mi_plataforma,lados_plataforma_dos,lados_plataformas_tres,
                        lados_plataforma_cuatro,lados_plataforma_cinco,lados_primer_trampa,
                        lados_segunda_trampa]

    plataformas_creadas = [mi_plataforma,mi_plataforma_dos,mi_plataforma_tercera,mi_plataforma_cuatro,
                        mi_plataforma_cinco,primer_trampa,segunda_trampa]

    listas_trampas = [lados_primer_trampa,lados_segunda_trampa]
    
    return lista_plataformas,plataformas_creadas,listas_trampas

def crear_plataformas_nivel2(lados_piso:dict)->list:
    
    """
    crea distintas plataformas y trampas para el nivel dos llamando a la clase plataforma
    parametro: recibe los lados del piso
    """
    mi_plataforma = plataforma("recursos de mi juego\plataformas\plat_nivel_2(2).png",200,35,430,310)

    mi_plataforma_dos = plataforma("recursos de mi juego\plataformas\plat_nivel_2(4).png",140,150,1070,230)

    mi_plataforma_tercera = plataforma("recursos de mi juego\plataformas\plat_nivel_2(5).png",150,50,770,230)

    mi_plataforma_cuatro = plataforma("recursos de mi juego\plataformas\plat_nivel_2(5).png",300,20,1,250)

    mi_plataforma_cinco = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",300,10,1,120)

    mi_plataforma_seis = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",110,30,410,175)

    mi_plataforma_siete = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",110,30,680,125)

    #TRAMPAS

    primer_trampa = plataforma("recursos de mi juego\enemigos-objetos\pinches nivel_2.png",500,70,650,310) 

    segunda_trampa = plataforma("recursos de mi juego\enemigos-objetos\pelota_puas.png",40,40,730,200)

    #LISTA DE LAS PLATAFORMAS
    plataformas_creadas = [mi_plataforma,mi_plataforma_dos,mi_plataforma_tercera,mi_plataforma_cuatro,
                        mi_plataforma_cinco,mi_plataforma_seis,mi_plataforma_siete,primer_trampa,
                        segunda_trampa]

    #LADOS
    lados_mi_plataforma = obtener_rectangulos(mi_plataforma.rectangulo)
    
    lados_plataforma_dos = obtener_rectangulos(mi_plataforma_dos.rectangulo)
    
    lados_plataformas_tres = obtener_rectangulos(mi_plataforma_tercera.rectangulo)
    
    lados_plataforma_cuatro = obtener_rectangulos(mi_plataforma_cuatro.rectangulo)
    
    lados_plataforma_cinco = obtener_rectangulos(mi_plataforma_cinco.rectangulo)
    
    lados_plataforma_seis = obtener_rectangulos(mi_plataforma_seis.rectangulo)
    
    lados_plataforma_siete = obtener_rectangulos(mi_plataforma_siete.rectangulo)
    
    lados_primer_trampa = obtener_rectangulos(primer_trampa.rectangulo)
    
    lados_segunda_trampa = obtener_rectangulos(segunda_trampa.rectangulo)

    lista_lados = [lados_piso,lados_mi_plataforma,lados_plataforma_dos,lados_plataformas_tres,
                        lados_plataforma_cuatro,lados_plataforma_cinco,lados_plataforma_seis,
                        lados_plataforma_siete,lados_primer_trampa,lados_segunda_trampa]

    listas_trampas = [lados_primer_trampa,lados_segunda_trampa]
    
    return plataformas_creadas,lista_lados,listas_trampas

def crear_plataformas_nivel3(lados_piso:dict)->list:
    
    """
    crea distintas plataformas y trampas para el nivel tres llamando a la clase plataforma
    parametro: recibe los lados del piso
    """
    #plataforma
    mi_plataforma = plataforma("recursos de mi juego\plataformas\plat_nivel_2(2).png",100,30,430,250)

    mi_plataforma_dos = plataforma("recursos de mi juego\plataformas\plat_nivel_2(4).png",500,30,1030,400)#

    mi_plataforma_tercera = plataforma("recursos de mi juego\plataformas\plat_nivel_2(5).png",50,20,860,250)

    mi_plataforma_cuatro = plataforma("recursos de mi juego\plataformas\plat_nivel_2(5).png",300,30,1,400)#

    mi_plataforma_cinco = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",300,30,1,200)

    mi_plataforma_seis = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",500,30,410,400)#

    mi_plataforma_siete = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",50,30,680,240)
    
    mi_plataforma_ocho = plataforma("recursos de mi juego\plataformas\plat_nivel_2.png",50,20,1150,305)

    primer_trampa = plataforma("recursos de mi juego\enemigos-objetos\lava.png",1200,90,1,500) 

    #LISTA DE LAS PLATAFORMAS
    plataformas_creadas = [mi_plataforma,mi_plataforma_dos,mi_plataforma_tercera,mi_plataforma_cuatro,
                        mi_plataforma_cinco,mi_plataforma_seis,mi_plataforma_siete,mi_plataforma_ocho
                        ,primer_trampa]
    
    #LADOS
    lados_mi_plataforma = obtener_rectangulos(mi_plataforma.rectangulo)
    lados_plataforma_dos = obtener_rectangulos(mi_plataforma_dos.rectangulo)
    lados_plataformas_tres = obtener_rectangulos(mi_plataforma_tercera.rectangulo)
    lados_plataforma_cuatro = obtener_rectangulos(mi_plataforma_cuatro.rectangulo)
    lados_plataforma_cinco = obtener_rectangulos(mi_plataforma_cinco.rectangulo)
    lados_plataforma_seis = obtener_rectangulos(mi_plataforma_seis.rectangulo)
    lados_plataforma_siete = obtener_rectangulos(mi_plataforma_siete.rectangulo)
    lados_primer_trampa = obtener_rectangulos(primer_trampa.rectangulo)
    lados_plataformas_ocho = obtener_rectangulos(mi_plataforma_ocho.rectangulo)

    lista_lados = [lados_piso,lados_mi_plataforma,lados_plataforma_dos,lados_plataformas_tres,
                        lados_plataforma_cuatro,lados_plataforma_cinco,lados_plataforma_seis,
                        lados_plataforma_siete,lados_plataformas_ocho,lados_primer_trampa] 
    
    listas_trampas = [lados_primer_trampa]
    
    return plataformas_creadas,lista_lados,listas_trampas


#################ENEMIGOS########################
def crear_enemigo_nivel1()->list:
    """
    crea enemigos llamando a la clase enemigo para el nivel uno
    """
    enemigos = []

    lista_enemigos_animaciones = [personaje_enemigo,pez_mirando_derecha,cangrejo,cangrejo_derecha]
    reescalar_imagen(lista_enemigos_animaciones,40,35)

    pez_pinches = enemigo(300,430,10,personaje_enemigo,pez_mirando_derecha,20,300)
    enemigos.append(pez_pinches.obtener_diccionario())

    pez_pinches_dos = enemigo(312,110,12,personaje_enemigo,pez_mirando_derecha,5,300)
    enemigos.append(pez_pinches_dos.obtener_diccionario())

    pez_pinches_tres = enemigo(700,110,12,personaje_enemigo,pez_mirando_derecha,700,900)
    enemigos.append(pez_pinches_tres.obtener_diccionario())
    
    mi_cangrejo = enemigo(436,375,15,cangrejo,cangrejo_derecha,436,600)
    enemigos.append(mi_cangrejo.obtener_diccionario())

    mi_cangrejo_dos = enemigo(310,165,10,cangrejo,cangrejo_derecha,10,400)
    enemigos.append(mi_cangrejo_dos.obtener_diccionario())

    mi_cangrejo_tres = enemigo(860,290,10,cangrejo,cangrejo_derecha,810,940)
    enemigos.append(mi_cangrejo_tres.obtener_diccionario())
    
    
    return enemigos,lista_enemigos_animaciones

def crear_enemigo_nivel2()->list:
    
    """crea enemigos llamando a la clase enemigo para el nivel dos"""
    enemigos = []

    lista_enemigos_animaciones = [personaje_enemigo,pez_mirando_derecha,cangrejo,cangrejo_derecha,pelota_fuego,
                                pelota_fuego_derecha,bombardero]

    reescalar_imagen(lista_enemigos_animaciones,37,35)

    pelotita_fuego = enemigo(300,210,20,pelota_fuego,pelota_fuego_derecha,20,280)
    enemigos.append(pelotita_fuego.obtener_diccionario())

    mi_bombardero = enemigo(450,30,26,bombardero,bombardero,5,350)
    enemigos.append(mi_bombardero.obtener_diccionario())

    pez_pinches = enemigo(700,190,12,pez_nivel2,pez_nivel2_derecha,700,990)
    enemigos.append(pez_pinches.obtener_diccionario())
    
    mi_orbinaut = enemigo(436,250,15,orbinaut,orbinaut_derecha,400,650)
    enemigos.append(mi_orbinaut.obtener_diccionario())

    mi_orbinaut2 = enemigo(1100,70,10,orbinaut,orbinaut_derecha,800,1100)
    enemigos.append(mi_orbinaut2.obtener_diccionario())

    bombardero2 = enemigo(860,30,30,bombardero,bombardero,500,940)
    enemigos.append(bombardero2.obtener_diccionario())

    bombardero3 = enemigo(760,30,20,bombardero,bombardero,550,800)
    enemigos.append(bombardero3.obtener_diccionario())

    pelotita_fuego2 = enemigo(370,330,20,pelota_fuego,pelota_fuego_derecha,20,350)
    enemigos.append(pelotita_fuego2.obtener_diccionario())
    #DISPAROS
    lista_proyectiles = []


    fuego = proyectil(20,20,mi_bombardero.rectangulo.x,mi_bombardero.rectangulo.y,40,
            "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")

    lista_proyectiles.append(fuego.obtener_diccionario())

    fuego_2 = proyectil(20,20,bombardero2.rectangulo.x,bombardero2.rectangulo.y,35,
                        "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")

    lista_proyectiles.append(fuego_2.obtener_diccionario())

    fuego_3 = proyectil(20,20,bombardero3.rectangulo.x,bombardero3.rectangulo.y,30,
                        "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")

    lista_proyectiles.append(fuego_3.obtener_diccionario())

    bombarderos = [mi_bombardero,bombardero2,bombardero3]

    lista_de_bombarderos=[]
    for bombarder in bombarderos:
        lista_de_bombarderos.append(bombarder.obtener_diccionario())
        
    return enemigos,lista_enemigos_animaciones,lista_proyectiles,lista_de_bombarderos 

def crear_enemigo_nivel3(boss)->list:
    
    """crea enemigos llamando a la clase enemigo para el nivel tres"""
    
    enemigos = []

    lista_enemigos_animaciones = [personaje_enemigo,pez_mirando_derecha,cangrejo,cangrejo_derecha,pelota_fuego,
                                pelota_fuego_derecha,bombardero]

    reescalar_imagen(lista_enemigos_animaciones,37,35)

    pelotita_fuego = enemigo(1150,350,10,pelota_fuego,pelota_fuego_derecha,1000,1150)
    enemigos.append(pelotita_fuego.obtener_diccionario())

    mi_bombardero = enemigo(450,30,12,bombardero,bombardero,5,300)
    enemigos.append(mi_bombardero.obtener_diccionario())
    
    mi_orbinaut = enemigo(1000,350,10,orbinaut,orbinaut_derecha,100,800)
    enemigos.append(mi_orbinaut.obtener_diccionario())

    mi_orbinaut2 = enemigo(1100,170,20,orbinaut,orbinaut_derecha,400,900)
    enemigos.append(mi_orbinaut2.obtener_diccionario())

    bombardero2 = enemigo(860,30,5,bombardero,bombardero,810,940)
    enemigos.append(bombardero2.obtener_diccionario())

    bombardero3 = enemigo(760,30,5,bombardero,bombardero,700,800)
    enemigos.append(bombardero3.obtener_diccionario())

    tirador = enemigo(800,160,5,pistolero_izquierda,pistolero_izquierda,700,900)
    enemigos.append(tirador.obtener_diccionario())
    
    lista_proyectiles = []

    fuego = proyectil(20,20,mi_bombardero.rectangulo.x,mi_bombardero.rectangulo.y,15,
            "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")
    lista_proyectiles.append(fuego.obtener_diccionario())

    fuego_2 = proyectil(20,20,bombardero2.rectangulo.x,bombardero2.rectangulo.y,20,
                        "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")
    lista_proyectiles.append(fuego_2.obtener_diccionario())

    fuego_3 = proyectil(20,20,bombardero3.rectangulo.x,bombardero3.rectangulo.y,20,
                        "recursos de mi juego\enemigos-objetos\\fuego.png",550,"bombardero")
    lista_proyectiles.append(fuego_3.obtener_diccionario())

    bala = proyectil(20,20,tirador.rectangulo.x,tirador.rectangulo.y,40,
                    "recursos de mi juego\enemigos-objetos\\bala.png",1,"tirador")
    lista_proyectiles.append(bala.obtener_diccionario())
    
   
    bala_boss = proyectil(20,15,boss.rectangulo.x ,boss.rectangulo.y +20 ,30,
                            "recursos de mi juego\enemigos-objetos\\bala_boss.png",1,"tirador")
        
    lista_proyectiles.append(bala_boss.obtener_diccionario())

    bombarderos = [mi_bombardero,bombardero2,bombardero3,tirador,boss]

    lista_de_bombarderos = []

    for bombarder in bombarderos:
        lista_de_bombarderos.append(bombarder.obtener_diccionario())
        
    return enemigos,lista_enemigos_animaciones,lista_proyectiles,lista_de_bombarderos  

def crear_boss():
    
    """crea al jefe para el nivel final"""
    
    lista_boss = []
    
    boss = jefe(850,330,20,the_boss_izquierda,the_boss,5,1000)
    
    lista_boss.append(boss.obtener_diccionario()) 
    
    return lista_boss,boss    

pez_mirando_derecha = girar_imagenes(personaje_enemigo,True,False)
cangrejo_derecha = girar_imagenes(cangrejo,True,False)
pelota_fuego_derecha = girar_imagenes(pelota_fuego,True,False)
pez_nivel2_derecha = girar_imagenes(pez_nivel2,True,False)
orbinaut_derecha = girar_imagenes(orbinaut,True,False)
pistolero_izquierda = girar_imagenes(pistolero,True,False)
the_boss_izquierda = girar_imagenes(the_boss,True,False)
boss_mas_velocidad_izquierda = girar_imagenes(boss_mas_velocidad,True,False)
tirador_izquierda = girar_imagenes(pistolero,True,False)


