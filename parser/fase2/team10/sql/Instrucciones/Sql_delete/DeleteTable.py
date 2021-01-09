from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.storageManager.jsonMode import *
from sql.Instrucciones.Excepcion import Excepcion

class DeleteTable(Instruccion):
    def __init__(self, valor, tipo, insWhere, strGram ,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.insWhere = insWhere


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(self.valor != None):
            if(self.insWhere != None):
                #delete(database: str, table: str, columns: list)
                arregloDeColumnasAEliminar = []
                #primero vamos a extraer la tabla
                if(arbol.getBaseDatos()!= None):
                    #resE = extractTable(arbol.getBaseDatos(),self.valor) 
                    #print("Entro al delete")
                    tablaSelect = extractTable(arbol.getBaseDatos(),self.valor)
                    if(self.insWhere != None):
                        #ejecutar el inswhere que me devuelva las columnas
                        arbol.setTablaActual(tablaSelect)
                        columnas = arbol.devolverColumnasTabla(self.valor)
                        arbol.setColumnasActual(columnas)
                        arregloDeColumnasAEliminar = self.insWhere.ejecutar(tabla,arbol)
                        arregloAEliminar = self.devolverIdentificadores(tablaSelect,arregloDeColumnasAEliminar)
                        for d in arregloAEliminar:
                            res = delete(arbol.getBaseDatos(),self.valor,[d])#SI IMPRIME 0, BORRO CON EXITO
                            if(res == 0):
                                arbol.consola.append(f"Se elimino el siguiente registro { d } correctamente.")
                            else:
                                error = Excepcion("42P10","Semantico",f"No se elimino :'( ",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                else:
                    #error no hay base de datos
                    error = Excepcion("42P10","Semantico",f"No hay base de datos",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())

    def devolverColumnas(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        val = ""
        columnas = ""
        res = []
        val = self.insWhere.ejecutar(tabla,arbol)
        columnas = arbol.devolverColumnasTabla(val)
        print(columnas)
        for x in range(0,len(columnas)):
            col = columnas[x].obtenerNombre()
            res.append(col)
        return res


    def devolverIdentificadores(self, tabla, fila):
        print(tabla)
        print(fila)
        res = []
        for x in range(0,len(tabla)):
            for y in range(0,len(fila)):
                if(tabla[x] == fila[y]):
                    res.append(x)
        
        nuevo = set(res)
        return nuevo
