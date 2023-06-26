from transporte import transporte

class bicicleta(transporte): #heredar 
    def __init__(self,ruedas,marca,cantidad,velocidad):
        super().__init__(cantidad,velocidad) #llamando al constructor padre
        self.cantidad_ruedas = ruedas
        self.marca = marca
        
    def frenar(self):
        print(f"""marca: {self.marca}""")
        super().frenar()
    def mostrar(self):
        
        super().mostrar()
        print(f"""
              ruedas: {self.cantidad_ruedas}--- marca: {self.marca}
             
              """)