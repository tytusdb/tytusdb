from Optimizacion.Instrucciones.instruccion import *
class Asignacion(object):
    def __init__(self,tem,izq,op,der):
        self.tem = tem
        self.izq = izq
        self.op = op
        self.der = der

    def setTemporal(self, tem):
        self.tem = tem
    def setIzquierda(self, izq):
        self.izq = izq
    def getIzquierda(self):
        return self.izq

    def getOperacion(self):
        return self.op
    def setOperacion(self, op):
        self.op = op

    def getDerecha(self):
        return self.der
    def setDerecha(self, der):
        self.der = der

    def execute(self):
        if self.op != None:
            return {'temp': self.tem, 'izq': self.izq, 'op': self.op, 'der': self.der }
        else:
            return {'temp': self.tem, 'val': self.izq}

    def toString(self,tab):
        if self.op != None:
            return  '\t'*tab + self.tem + ' = ' + str(self.izq) + ' ' + self.op + ' ' + str(self.der) 
        else:
            if isinstance(self.izq,Instruccion):
                return  '\t'*tab + self.tem + ' = ' + self.izq.toString(0)
            return  '\t'*tab + self.tem + ' = ' + str(self.izq)
