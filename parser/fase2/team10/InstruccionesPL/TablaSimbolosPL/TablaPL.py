class TablaPL():
    'Esta clase representa la tabla de simbolos del lenguaje PL'
    def __init__(self, anterior):
        self.anterior = anterior
        self.variables = []
        self.funciones = []
    
    def setVariable(self, simbolo):
        tablaPL = self
        for variable in tablaPL.variables:
            if variable.id == simbolo.id:
                return "La variable" + variable.id + " ya ha sido declarada."
        self.variables.append(simbolo)
        return None

    def getVariable(self, id):
        tabla = self
        while tabla != None:
            for variable in tabla.variables:
                if variable.id == id:
                    if variable.id  == id:
                        return variable
            tabla = tabla.anterior
        return None

    def setFuncion(self, funcion):
        tabla = self
        for f in tabla.funciones:
            if f.id == funcion.id:
                print("La funcion "+ f.id + " ya ha sido declarada")
                return "La variable" + f.id + " ya ha sido declarada"
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

