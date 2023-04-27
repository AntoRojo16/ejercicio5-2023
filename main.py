from ManejadorPlan import Planes
from ClasePlanAhorro import PlanAhorro
import csv
if __name__=="__main__":
    unosPlanes=Planes()
    unosPlanes.inicializar()
    print("Hola")
    print(unosPlanes)
    #unosPlanes.mostrarDespuesValor()    
    #unosPlanes.mostrarValorLicitar()
    unosPlanes.modificarCantCuotas()