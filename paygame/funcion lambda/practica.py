from data_stark import lista_personajes

def calcular(a,b,operacion):
    return operacion(a,b)


#####va a mostrar el resultado segun la operacion#########################################
#funcion = sumar # gurdo l funcion sumar en la variable funcion
#resultado = calcular(5,5,sumar)
#print(resultado)

#resultado = calcular(5,5,restar)
#print(resultado)
#resultado = calcular(5,5,multiplicar)
#print(resultado)
#resultado = calcular(5,5,dividir)
#print(resultado)

'''resultado= calcular( 5,4 , lambda x , y : x + y )
print(f"la suma es: {resultado}") 

resultado= calcular( 2,2 , lambda x , y : x**2 + y )
print(f"la potencia es: {resultado}")'''

###############################################################################################

#lista_numeros = [2,4,6,8,9,3]

#lista_modifica = []

'''for numero in lista_numeros:
    doble = numero*2
    lista_modifica.append(doble)
    
print(lista_modifica)
'''

#lista_modificada = list(map(lambda numero : numero * 2,lista_numeros))

#print(lista_modificada)

######################################TRABAJAR CON LISTA##################################################

#colores = set(list(map(lambda heroe: heroe["color_ojos"],lista_personajes )))

#print(colores)
################################CONDICION LAMBDA#####################################################
lista_numeros=[1,2,3,4,5,6,7,8]

def my_filter(criterio,lista):
    filtrada =[]
    
    for elemento in lista:
        if criterio(elemento):
            filtrada.append(elemento)
    return filtrada

#pares = list(filter(lambda numero: numero % 2 == 0,lista_numeros)) #devulve true si cumple con el criterio
pares = my_filter(lambda numero: numero % 2 == 0,lista_numeros)
#print(pares)

femeninos = my_filter(lambda personajes: personajes["genero"] == "F",lista_personajes)
#femeninos = list(filter(lambda personaje: personaje["genero"] == "F" ,lista_personajes))


#print(femeninos)

########################################REDUCE#####################################################################

from functools import reduce

'''total = reduce(lambda anterior, actual: anterior + actual,lista_numeros,0)
print(total)'''

#maximo = reduce(lambda maximo, numero: numero if numero > maximo else maximo,lista_numeros,0)
#print(maximo)

for superheroe in lista_personajes:
    
    if type(superheroe["peso"]) == str  or type(superheroe["altura"]) == str:
        superheroe["peso"]= float(superheroe["peso"])
        superheroe["altura"] = float(superheroe["altura"])
        
maximo_altura = reduce(lambda maximo,heroes: heroes["altura"] if heroes["altura"] > maximo else maximo,lista_personajes,0)

print(maximo_altura)




