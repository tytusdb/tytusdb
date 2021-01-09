class Tabla():
    'Esta clase representa la tabla de símbolos.'

    def __init__(self, anterior):
        self.anterior = anterior
        self.variables = []
        self.funciones = []
        self.reporte = []
        self.temporal = 0
        self.etiqueta = 0
        self.heap = 0
        self.stack = 0
        
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

    def getTemporal(self):
        t = "t" + str(self.temporal)
        self.temporal += 1
        return t
    
    def getTemporalActual(self):
        return "t" + str(self.temporal)
    
    def getEtiqueta(self):
        l = "l" + str(self.etiqueta)
        self.etiqueta += 1
        return l
    
    def getEtiquetaActual(self):
        return "l" + str(self.etiqueta)

    def agregarReporteSimbolo(self,simbolo):
        tabla = self
        while tabla != None:
            if tabla.anterior == None:
                tabla.reporte.append(simbolo)
            tabla = tabla.anterior
        return None

    def agregarSimbolo(self,simbolo):
        self.variables.append(simbolo)
        return None

    def getSimboloVariable(self,id):
        tabla = self
        while tabla != None:
            for variable in tabla.variables:
                if variable.id == id and variable.rol != "Metodo":
                    return variable 
            tabla = tabla.anterior
        return None

    def getSimboloFuncion(self,id):
        tabla = self
        while tabla != None:
            for variable in tabla.variables:
                if variable.id == id and variable.rol == "Metodo":
                    return variable 
            tabla = tabla.anterior
        return None

    def dropSimboloFuncion(self,id):
        tabla = self
        while tabla != None:
            for variable in tabla.variables:
                if variable.id == id and variable.rol == "Metodo":
                    tabla.variables.remove(variable)
                    return True
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