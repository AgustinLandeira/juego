
from auto import auto 
from bicicleta import bicicleta

mi_auto = auto(4,"ford",5,170)
mi_bicicleta = bicicleta(16,24,1,50)
otro_auto = auto(5,"fiat",8,200)
'''mi_auto.mostrar()
mi_auto.frenar()'''

transportes =[mi_auto, mi_bicicleta,otro_auto]

for t in transportes:
    t.mostrar()#poliformismo

#mi_transporte = transporte(2,50) # cree una instancia de transporte en la memoria y crean un objeto en el heap
#print(mi_transporte.avanzar)


#mi_transporte.mostrar()


#mi_transporte.avanzar()
#mi_transporte.frenar() #metodos'''