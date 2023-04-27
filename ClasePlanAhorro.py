class PlanAhorro:
    __Codigo=""
    __modelo=""
    __version=""
    __valor=0
    __cantidadCuotas=0
    __cuotasLicitar=0


    def __init__ (self,cod,modelo,version,valor,cuotas,licitar):
        self.__Codigo=cod
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
        self.__cantidadCuotas=cuotas
        self.__cuotasLicitar=licitar

    def __str__ (self):
        return  ("codigo: {},modelo: {},version: {},valor: {},cantidad de cuotas: {},catidad para licitar: {}".format(self.__Codigo,self.__modelo,self.__version,self.__valor,self.__cantidadCuotas,self.__cuotasLicitar))
    

    def getValor(self):
        return self.__valor
    

    def getCodigo(self):
        return self.__Codigo
    
    def getVersion(self):
        return self.__version
    

    def calculaValor(self):
        valor=float(float(self.__valor)/float(self.__cantidadCuotas)+(float(self.__valor)*0.10))
        return valor
    

    def calcularLicitar(self):
        valor=int(self.__cuotasLicitar)*int(self.__valor)
        return valor
    

    def modificarCuotas(self,cant):
        self.__cantidadCuotas=cant


    def getCatidad(self):
        return self.__cantidadCuotas

    