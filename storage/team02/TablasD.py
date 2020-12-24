
from Tablas import *

class TablasArboles:  
    def __init__(self,bd) :
        self.bd=bd

    def agregarColumna(self,val,tabla) :
        for i in range(len(tabla.elementosAB.listRegister)) :
            tabla.elementosAB.listRegister[i].register.append(val)
        return True

    def eliminarColumna(self,num,tabla) :
        for i in range(len(tabla.elementosAB.listRegister)):
            del tabla.elementosAB.listRegister[i].register[num]
        return True