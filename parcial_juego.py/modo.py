import pygame

debug = False

def cambiar_modo():
    
    """cambia el modo de debug"""
    
    global debug
    
    debug = not debug
    
    return debug


def get_mode():
    
    return debug

def mostrar_lados_2(lista_lados:list,enemigos,lados_personaje,listas_trampas:list,pantalla:pygame.Surface):
    
    """muestra los lados de los rectangulos del nivel dos"""
    
    for una_plataforma in lista_lados:
        for lado in una_plataforma:
            pygame.draw.rect(pantalla,"red", una_plataforma[lado],2)
                
    for lado_enemigo in enemigos:
        for lado in lado_enemigo["lados"]:
            lado_rect = lado_enemigo["lados"][lado]
            pygame.draw.rect(pantalla, (255, 0, 0), lado_rect,2)
        
    for lado in lados_personaje:
        pygame.draw.rect(pantalla,"orange", lados_personaje[lado],2)
            
    for trampa in listas_trampas:
        for lado in trampa:
            pygame.draw.rect(pantalla,"red", trampa[lado],2)

def mostrar_lados_1(lista_plataformas:list,enemigos,lados_personaje,
                    listas_trampas:list,pantalla:pygame.Surface):
    
    """muestra los lados de los rectangulos del nivel uno"""
    
    for una_plataforma in lista_plataformas:
        for lado in una_plataforma:
            pygame.draw.rect(pantalla,"red", una_plataforma[lado],2)
                    
    for lado_enemigo in enemigos:
        for lado in lado_enemigo["lados"]:
            lado_rect = lado_enemigo["lados"][lado]
            pygame.draw.rect(pantalla, (255, 0, 0), lado_rect,2)
    
    for lado in lados_personaje:
        pygame.draw.rect(pantalla,"orange", lados_personaje[lado],2)
            
        
    for trampa in listas_trampas:
        for lado in trampa:
            pygame.draw.rect(pantalla,"red", trampa[lado],2)

def mostrar_lados_3(lista_plataformas:list,enemigos,lados_personaje,listas_trampas:list,
                    pantalla:pygame.Surface,lista_boss:list):
    
    
    """muestra los lados de los rectangulos del nivel tres"""
    
    for una_plataforma in lista_plataformas:
        
        for lado in una_plataforma:
            pygame.draw.rect(pantalla,"red", una_plataforma[lado],2)
                    
    for lado_enemigo in enemigos:
        
        for lado in lado_enemigo["lados"]:
            
            lado_rect = lado_enemigo["lados"][lado]
            pygame.draw.rect(pantalla, (255, 0, 0), lado_rect,2)
    
    for lado in lados_personaje:
        
        pygame.draw.rect(pantalla,"orange", lados_personaje[lado],2)
            
        
    for trampa in listas_trampas:
        
        for lado in trampa:
            
            pygame.draw.rect(pantalla,"red", trampa[lado],2)
            
    for clave in lista_boss:
        
        for lado in clave["lados"]:
            
            lado_rectangulo = clave["lados"][lado]
            pygame.draw.rect(pantalla, (255, 0, 0), lado_rectangulo,2)
