from class_personaje import Personaje
from clase_extraterrestre import PersonajeExtraterrestre


un_Personaje = Personaje(1,"ironman","no","si" )
otro_Personaje = Personaje(2,"ironspider","si","no")

#un_Personaje.nombre = "super ironman"

un_Personaje.set_nombre("    superior-ironman") # para modificar el nombre que esta en privado

#print(un_Personaje.__nombre) # no podes ingresar al nombre pq esta en privado 

'''print(un_Personaje.get_nombre())
print(un_Personaje.retornar_descripcion())'''



#################################################################################################

personaje_extr = PersonajeExtraterrestre(5,"thor","no","si","asgardiano")

print(personaje_extr.retornar_descripcion())