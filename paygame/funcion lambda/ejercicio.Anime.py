from anime import series

#1.Obtener una lista con los nombres de todas las series de anime.

nombres = list(map(lambda anime: anime["nombre"],series))

for anime in nombres:
    print(f"el nombre del anime es : {anime}")

####################################################################################################    
#2. Obtener las series de anime lanzadas después de 1995.

'''def my_filter(criterio,lista):
    filtrada = []
    
    for elemento in lista:
        if criterio(elemento):
            filtrada.append(elemento)
    return filtrada'''
 # segunda opcion

lista_filtrada = list(filter(lambda serie: serie["año"] > 1995, series ))

#lista_filtrada = my_filter(lambda serie: serie["año"] > 1995, series) segunda opcion

#print(lista_filtrada)

#######################################################################################################

#3. Obtener la suma de los años de lanzamiento de las series.

from functools import reduce

'''acumulacion = reduce(lambda año,contador: contador["año"] + año,series,0)
print(acumulacion)'''

##########################################################################################################

#4.Realizar una copia superficial de la lista de series.

lista_copiada = series.copy() #shallow copy

print(id(lista_copiada))
print("-----------------------------------------------------------------------------------------------\n")
print(id(series))

###################################################################################

#5. Realizar una copia profunda de la lista de series.
#6.Obtener el año de lanzamiento de una serie utilizando una función de diccionario.

from copy import deepcopy

lista_1 = [["Marty","McFly"], "Emmett", "Biff"]

lista_copy = deepcopy(lista_1)

print(lista_copy[1])

###########################################################################################

print(series.get("año","no hay"))



