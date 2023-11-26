from class_personaje import Personaje
class PersonajeExtraterrestre(Personaje):
    def __init__(self,id,nombre,nano,vuela,raza):
        super().__init__(id,nombre,nano,vuela)
        self._raza = raza
    
    def retornar_descripcion(self):
        
        descripcion = "{0} - {1}".format(super().retornar_descripcion(),self._raza)
        
        return descripcion
        
        