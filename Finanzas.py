from Ingresos import Ingresos
from Egresos import Egresos

IngresosObj = Ingresos()
EgresosObj = Egresos()

def Ingreso():
    IngresosObj.NuevoIngreso()
    
def Egreso():
    EgresosObj.NuevoEgreso()
    
def getIngreso():
    IngresosObj.getIngreso()
    
def getEgreso():
    EgresosObj.getEgreso()
    
class Finanzas:
    def __init__(self):
        pass
    def NuevaCuenta(self):
        nombreCuenta = input("Ingresa tu nombre para poder abrir una nueva cuenta: ")
        print("")
        print("Esta cuenta pertenece a: " +nombreCuenta)
        print("Saldo actual: $0.00\n") 
    def ReportarTransferencia (self):
        ingresos = getIngreso()
        egresos = getIngreso()
        transferencias = {
            "Ingresos" : ingresos,
            "Egresos": egresos 
        }
        for x in transferencias:
            print(transferencias[x])
    def VerSaldo(self):
        ingresos = getIngreso()
        egresos = getIngreso()
        transferencias = {
            "Ingresos" : ingresos,
            "Egresos": egresos 
        }
        total = 0
        for x in transferencias:
            total += int(x)
        print(total)