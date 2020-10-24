class Egresos:
    def __init__(self):
        self.egresos = []

    def NuevoEgreso(self):
        agregarEgreso = int(input("Cuánto deseas egresar? $"))
        self.egresos.append(agregarEgreso)
        sumaEgreso = 0
        sumaEgreso += agregarEgreso

    def getEgreso(self):
        for x in self.egresos:
            print(x)