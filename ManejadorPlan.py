import csv
from ClasePlanAhorro import PlanAhorro
class Planes:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarPlan(self,plan):
         self.__lista.append(plan)

    def inicializar(self):
        
        archivo=open("planes.csv")
        band=True
        reader=csv.reader(archivo,delimiter=";")
        print("agregar planes a lista")
        for fila in reader:
            codigo=fila[0]
            modelo=fila[1]
            version=fila[2]
            valor=fila[3]
            catidadcuotas=fila[4]
            licitar=fila[5]
            unPlan=PlanAhorro(codigo,modelo,version,valor,catidadcuotas,licitar)  
            print(unPlan)                  
            self.__lista.append(unPlan)
                
        archivo.close()

    def __str__(self):
        s = ""
        for plan in self.__lista:
            s += str(plan) + '\n'
        return s
    

    def buscarCodigo(self, codigo):
        print("entre en la busqueda")
        unPlan=self.__lista[0]
        i=0
        uncodigo=unPlan.getCodigo()
        while(i<(len(self.__lista)-1)and(codigo!=uncodigo)):
            print("codigo {}".format(uncodigo))
            i+=1
            unPlan=self.__lista[i]
            uncodigo=unPlan.getCodigo()

        if codigo==uncodigo:
            return i
        else:
            print("no se encontro el codigo")
            return False
        


    def mostrarDespuesValor(self):
        valor=input("ingrese el valor a buscar. ")
        for plan in self.__lista:
            if float(valor)>float(plan.calculaValor()):
                print("codigo {}, modelo {}, version {}".format(plan.getCodigo(),plan.getValor(),plan.getVersion()) )

    
    def mostrarValorLicitar(self):
        codigo=input("Ingrese el codigo")
        i=self.buscarCodigo(codigo)
        print("el monto que se debe haber pagado para licitar el vehiculo es {}".format(self.__lista[i].calcularLicitar()))



    def modificarCantCuotas(self):
        codigo=input("Ingrese el codigo")
        i=self.buscarCodigo(codigo)
        print("La cantidad de cuotas actual es {}".format(self.__lista[i].getCatidad()))
        cantidad=input("ingrese la nueva cantidad de cuotas")
        self.__lista[i].modificarCuotas(cantidad)
        print("La cantidad de cuotas nueva es {}".format(self.__lista[i].getCatidad()))

