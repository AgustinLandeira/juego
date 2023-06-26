# caracteristicas(atributos variables) esto seria estatica
"""cantidad de pasajeros y velocidad 
kilometros y distancia recorrida"""

#_protegido privado (afuera publico para adentro)
#__privado
#sin gion es publico

#comportamientos (lo que puede hacer un objeto) tiene un constructor y se usa un metofo llamado init

class transporte:
    def __init__(self,cantidad,velocidad):#self es la instancia de la que estoy trabajando
        self.cantidad_pasajeros = cantidad #publico y protegido
        self.velocidad = velocidad                
        self.k_totales = 0
        self.distancia_recorridos = 0
    
    def avanzar(self):
        print("esto avanza")
        
    def frenar(self):
        print("esta frenando")
    
    
    def mostrar(self): #metodo
        print(f"--------------------{type(self)}--------------------------------------------------------")
        print(f"""
            cantidad de pasajeros: {self.cantidad_pasajeros} - velocidad: {self.velocidad}
            destino: {self.k_totales}""")
        