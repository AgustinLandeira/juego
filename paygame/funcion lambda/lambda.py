
#suma = lambda x,y : x+y

#print(suma(5,9))

lista_nombres=[
    
    {
        "nombre":"agus"
        
    },
    {
        "nombre":"tomi"
        
    }
    
]

lista_numeros=[5,4,3,2,6,8]

'''lista_modificada = []

for numeros in lista_numeros:
    doble = numeros*2
    lista_modificada.append(doble)
print(lista_numeros)    
print(lista_modificada)    '''


#lista = list(map(lambda nombre: nombre["nombre"].upper(),lista_nombres))
#print(lista)
#
#pares = list(filter(lambda numero : numero %2 == 0, lista_numeros)) # te establece una condicion

#print(pares)

#reduce no es nativa por eso hay que importarla

from functools import reduce

#total = reduce(lambda anterior, actual: anterior + actual , lista_numeros,0)#suma todo los numeros de la lista

#print(total)
maximo = reduce(lambda maximo, numero: numero if  numero > maximo else maximo , lista_numeros,0)
print(maximo)
a=5
b=3

#print("a es mayor que b") if a > b else print("b es mayor que a") # operador ternario

#mensaje = if a > b 

'''def my_reduce(funcion, lista, valor_inicial = 0):
    maximo = valor_inicial

    for numero in lista:
        maximo = funcion(maximo,numero)

    return maximo
'''