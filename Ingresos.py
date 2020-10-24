class Ingresos:
    def __init__(self):
        self.ingresos = []

    def AgregarIngreso(self):
        agregarIngreso = int(input("Cuánto deseas ingresar? $"))
        sumaIngreso = 0
        sumaIngreso +=agregarIngreso
        self.ingresos.append(agregarIngreso)

    def getIngreso(self):
        print("Registro de ingresos hasta el momento: ") 
        for x in self.ingresos:
            print(x)