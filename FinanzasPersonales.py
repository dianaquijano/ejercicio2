from Ingresos import Ingresos
from Egresos import Egresos
from Finanzas import Finanzas

FinanzasAppObj = Finanzas()
IngresosObj = Ingresos()
EgresosObj = Egresos()

def NuevaCuenta():
    FinanzasAppObj.NuevaCuenta()
    
def Ingreso():
    IngresosObj.NuevoIngreso()
    
def Egreso():
    EgresosObj.NuevoEgreso()
    
def getIngreso():
    IngresosObj.getIngreso()
    
def getEgreso():
    EgresosObj.getEgreso()
    
def ReportarTransferencia():
    FinanzasAppObj.ReportarTransferencia()

def verSaldo():
    FinanzasAppObj.VerSaldo()

print("\t¡Bienvenido!\n")
while True:
    print("\t¿Qué deseas hacer?\n")
    print(" 1 - Iniciar tu cuenta\n 2 - Ingresar dinero\n 3 - Retirar dinero\n 4 - Obtener reporte de ingresos\n 5 - Obtener reporte de egresos\n 6 - Obtener reporte de las transacciones\n 7 - Ver saldo disponible\n 8 - Salir\n")
    opcion = int(input(">"))
    if opcion == 1:
        NuevaCuenta()
    elif opcion == 2:
        Ingreso()
    elif opcion == 3:
        Egreso()
    elif opcion == 4:
        getIngreso()
    elif opcion == 5:
        getEgreso()
    elif opcion == 6:
        ReportarTransferencia()
    elif opcion == 7:
        verSaldo()
    elif opcion == 8:
        print("\tGracias por su preferencia\n")
        break