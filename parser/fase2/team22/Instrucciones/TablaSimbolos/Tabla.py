class Tabla():
    'Esta clase representa la tabla de símbolos.'

    def __init__(self, anterior):
        self.anterior = anterior
        self.variables = []
        self.funciones = []
        
    def setVariable(self,simbolo):
        tabla = self
        for variable in tabla.variables:
            if variable.id == simbolo.id:
                return "La variable " + variable.id + " ya ha sido declarada."
        self.variables.append(simbolo)
        return None
    
    def getVariable(self,id):
        tabla = self
        while tabla != None:
            for variable in tabla.variables:
                if variable.id == id:
                    return variable 
            tabla = tabla.anterior
        return None

    def setFuncion(self, funcion):
        tabla = self
        for f in tabla.funciones:
            if f.id == funcion.id:
                print("La variable " + f.id + " ya ha sido declarada.")
                return "La variable " + f.id + " ya ha sido declarada."
        print("se agrego la funcion")
        self.funciones.append(funcion)
        return None
    
    def getFuncion(self, nombre):
        tabla = self
        while tabla != None:
            for funcion in tabla.funciones:
                if funcion.id == id:
                    return funcion 
            tabla = tabla.anterior
        return None


'''
from Simbolo import Simbolo

s1 = Simbolo("a","int","aa",1,1)
s2 = Simbolo("b","int","aa",2,1)
s3 = Simbolo("c","int","aa",3,1)

tablaGlobal = Tabla(None)

tablaGlobal.variables.append(s1)
tablaGlobal.variables.append(s2)
tablaGlobal.variables.append(s3)


s4 = Simbolo("a1","int","aa",1,1)
s5 = Simbolo("a1","int","aa",2,1)
s6 = Simbolo("c3","int","aa",3,1)


local1 = Tabla(tablaGlobal)

local1.setVariable(s4)
resultado = local1.setVariable(s5)
local1.setVariable(s6)

print(resultado)

encontro = local1.getVariable("a")
if encontro != None:
    print("encontro! " +encontro.id)
else:
    print("Error semántico!")

'''