class Tabla():
    'Esta clase representa la tabla de símbolos.'

    def __init__(self, anterior):
        self.anterior = anterior
        self.variables = []
        self.funciones = []
        self.indices = []
        self.procedimientos = []
        
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

    def setFuncion(self, funcion, arbol):
        tabla = self
        for f in tabla.funciones:
            if f.id == funcion.id:
                print("La funcion " + f.id + " ya ha sido declarada.")
                error = Exception("XX000", "Semantico", "Error la función ya fue declarada", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return None
        print("se agrego la funcion")
        arbol.consola.append(f"La función {funcion.id} fue creada.")
        self.funciones.append(funcion)
        return None
    
    def dropFuncion(self, funcion, arbol):
        tabla = self
        toDelete = None
        for f in tabla.funciones:
            if f.id == funcion.id:
                toDelete = f
                print(f"La función {funcion.id} fue encontrada")
                break
        if toDelete != None:
            tabla.funciones.remove(toDelete)
            print("La funcion fue eliminada")
            arbol.consola.append(f"La función {funcion.id} fue eliminada.")
        else:
            print("La funcion no fue encontrado")
            error = Exception("XX000", "Semantico", "Error la función no fue encontrada", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        return None
    
    def setProcedimiento(self, procedimiento, arbol):
        tabla = self
        for f in tabla.procedimientos:
            if f.id == procedimiento.id:
                print("El procedimiento " + f.id + " ya ha sido declarado.")
                error = Exception("XX000", "Semantico", "Error el procedimiento ya fue declarado", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return None
        print("se agrego el procedimiento")
        arbol.consola.append(f"El procedimiento {procedimiento.id} fue creado.")
        self.procedimientos.append(procedimiento)
        return None
    
    def dropProcedimiento(self, procedimiento, arbol):
        tabla = self
        toDelete = None
        for f in tabla.procedimientos:
            if f.id == procedimiento.id:
                toDelete = f
                print(f"La función {procedimiento.id} fue encontrada")
                break
        if toDelete != None:
            tabla.procedimiento.remove(toDelete)
            print("El procedimiento fue eliminado")
            arbol.consola.append(f"El procedimiento {procedimiento.id} fue eliminado.")
        else:
            print("El procedimiento no fue encontrado")
            error = Exception("XX000", "Semantico", "ErrorEl procedimiento no fue encontrado", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        return None
    
    def getFuncion(self, nombre):
        tabla = self
        while tabla != None:
            for funcion in tabla.funciones:
                if funcion.id == id:
                    return funcion 
            tabla = tabla.anterior
        return None
    
    def setIndice(self, indice, arbol):
        tabla = self
        for i in tabla.indices:
            if i.nombre == indice.nombre:
                print("El indice " + i.nombre + " ya ha sido declarado.")
                error = Exception("XX000", "Semantico", "Error el indice ya fue declarado", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return None
        print("se agrego el indice")
        arbol.consola.append(f"El indice {indice.nombre} fue creado.")
        self.indices.append(indice)
        return None
    
    def removeIndice(self, indice, arbol):
        tabla = self
        toDelete = None
        for i in tabla.indices:
            if i.nombre == indice.nombre:
                print("El indice " + i.nombre + " fue encontrado")
                toDelete = i
                break
        if toDelete != None:
            tabla.indices.remove(toDelete)
            print("El indice fue eliminado")
            arbol.consola.append(f"El indice {indice.nombre} fue eliminado.")
        else:
            print("El indice no fue encontrado")
            error = Exception("XX000", "Semantico", "Error el indice no fue encontrado", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        return None
    
    def alterIndice(self, indice, arbol):
        tabla = self
        toAlter = None
        for i in tabla.indices:
            if i.nombre == indice.nombre:
                print("El indice " + i.nombre + " fue encontrado")
                toAlter = i                
                break
        if toAlter != None:
            for db in arbol.listaBd:
                for t in db.tablas:
                    if t.nombreDeTabla == toAlter.tabla:
                        act = False
                        nw = False
                        for c in t.lista_de_campos:
                            if indice.actual == c.nombre:
                                act = True
                                break
                        for c in t.lista_de_campos:
                            if indice.reemplazo == c.nombre:
                                nw = True
                                break
                        if act and nw:
                            temp = toAlter.columnas.replace(indice.actual, indice.reemplazo)
                            toAlter.columnas = temp
                        else:
                            arbol.consola.append(f"Las columnas {indice.actual} o {indice.reemplazo} no fueron encontradas en la tabla.")
        else:
            arbol.consola.append(f"El indice {indice.nombre} no fue encontrado.")
            return None
        for j in tabla.indices:
            if j.nombre == indice.nombre:
                print("El indice " + j.nombre + " fue encontrado")
                j.columnas = toAlter.columnas
                arbol.consola.append(f"El atributo columna del indice {indice.nombre} fue actualizado")
                break
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