class Personaje:
    def __init__(self,id,nombre,nano,vuela):
        self._id = id #(+ publico)
        self._nombre = nombre #(___privado: no se puede ver y solamente se puede ver dentro de la clase)
        self._usa_nanotecnologia = nano
        self._puede_volar = vuela
        
    def set_id(self,id):
        if id > 0:
            self._id = id
    
        
    def set_nombre(self,nombre): # entre el set para modificar el nombre
        
        self._nombre = nombre.strip().capitalize()
        
    def get_nombre(self): # solo lectura de la variable
        return self._nombre
        
    def retornar_descripcion(self):
        descripcion_personaje =  f"{self._id} - {self._nombre} - {self._usa_nanotecnologia} - {self._puede_volar}"
        return descripcion_personaje