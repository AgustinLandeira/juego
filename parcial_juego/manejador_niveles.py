from nivel_1 import NivelUno
from nivel_2 import NivelDos
from nivel_3 import NivelTres

class Manejador_niveles:
    
    def __init__(self,pantalla)->None:
        self._slave = pantalla
        self.niveles = {"nivel uno":NivelUno, "nivel dos":NivelDos, "nivel tres": NivelTres}
    
    def get_nivel(self,nombre_nivel):
        
        return self.niveles[nombre_nivel](self._slave)
    
    