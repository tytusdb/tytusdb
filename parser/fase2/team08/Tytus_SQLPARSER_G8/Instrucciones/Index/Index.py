from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
from Instrucciones.Sql_select.OrderBy import OrderBy
from Instrucciones.Sql_select.GroupBy import GroupBy
from Instrucciones.Sql_select.Having import Having
from Instrucciones.Sql_select.Limit import Limit
from Instrucciones.Identificador import Identificador
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_select import SelectLista 
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.Tablas.Indice import Indice
import numpy as np
import pandas as pd
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.PL.Llamada import Llamada

class Index(Instruccion):
                       #dist  tipo  lcol  lcol  linners where lrows
    def __init__(self, idIndex, idTabla , lcol, where, tipoIndex ,strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,strGram)
        self.idIndex = idIndex
        self.idTabla = idTabla
        self.lcol = lcol
        self.where = where
        self.tipoIndex = tipoIndex

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        val = self.idTabla.devolverTabla(tabla, arbol)

        if(val == 0):
            error = Excepcion("42P01", "Semantico", "La tabla " + str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            print('Error tabla no existe')
            return error

        tablaIndex = extractTable(arbol.getBaseDatos(), val)
        arbol.setTablaActual(tablaIndex)
        columnas = arbol.devolverColumnasTabla(val)
        
        data = np.array((tablaIndex))
        res = []
        # vamos a mostrar todos
        for x in range(0, len(columnas)):
            col = columnas[x].obtenerNombre()
            res.append(col)

        arbol.setColumnasActual(res)

        ## solo me quedaria buscar entre las columnas si existe la columnas 
        #print(res) 

        listaMods = []

        if self.where:
            listaMods = self.where.ejecutar(tabla, arbol)
        
        for x in range(0, len(self.lcol)):
            variable = self.lcol[x]
            #print("CONTENIDO DE LCOL")
            #print(variable)
            #print(variable.parseindex(tabla,arbol))
            objetoTabla = arbol.devolviendoTablaDeBase(val)
            if isinstance(variable, Llamada):
                idcol = variable.parseindex(tabla, arbol)
                if self.buscarColumna(idcol, res):
                    if objetoTabla:
                        for indices in objetoTabla.lista_de_indices:
                            if indices.obtenerNombre == idcol :
                                error = Excepcion('42P01',"Semántico","el indice «"+idcol+"» ya existe",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                                return error
                        
                    ind = Indice(self.idIndex, "Indice")
                    ind.lRestricciones.append("Columna: "+ idcol)
                    if self.tipoIndex:
                        ind.lRestricciones.append(self.tipoIndex)
                    
                    for indi in objetoTabla.lista_de_indices:
                        if indi.nombre == self.idIndex:
                                error = Excepcion('42P07',"Semántico","la relación «"+self.idIndex+"» ya existe.",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                                return error

                    objetoTabla.lista_de_indices.append(ind)
                    arbol.consola.append(f"Indice: {self.idIndex} insertado correctamente.\n")    

                    #print("ingresar a memoria")

                else:
                    print("error la columna no existe")
            if isinstance(variable, Identificador):
                idcol = variable.id
                if self.buscarColumna(variable.id, res):
                    if objetoTabla:
                        for indices in objetoTabla.lista_de_indices:
                            if indices.obtenerNombre == variable.id :
                                error = Excepcion('42P01',"Semántico","el indice «"+variable.id+"» ya existe",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                                return error
                        
                    ind = Indice(self.idIndex, "Indice")
                    ind.lRestricciones.append("Columna: "+ variable.id)
                    if self.tipoIndex:
                        ind.lRestricciones.append(self.tipoIndex)
                    
                    for indi in objetoTabla.lista_de_indices:
                        if indi.nombre == self.idIndex:
                                error = Excepcion('42P07',"Semántico","la relación «"+self.idIndex+"» ya existe.",self.linea,self.columna)
                                arbol.excepciones.append(error)
                                arbol.consola.append(error.toString())
                                return error
                                
                    objetoTabla.lista_de_indices.append(ind)
                    arbol.consola.append(f"Indice: {self.idIndex} insertado correctamente.\n")    

                    #print("ingresar a memoria")

                else:
                    print("error la columna no existe")

    def buscarColumna(self, nombre, listacolumnas):
        for i in range(0, len(listacolumnas)):
            if listacolumnas[i] == nombre:
                return True

        return False


    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        #self.idIndex = idIndex
        #self.idTabla = idTabla
        #self.lcol = lcol
        #self.where = where
        #self.tipoIndex = tipoIndex        
        cadena = "\"CREATE"
        if self.tipoIndex == "UNIQUE":
            cadena += " UNIQUE"
        cadena += f" INDEX {self.idIndex} ON {self.idTabla.concatenar(tabla,arbol)} "
        if self.tipoIndex == "HASH":
            cadena += "USING HASH "
        cadena += "("
        for col in self.lcol:
            #print(col)

            if isinstance(col, Identificador):
                cadena += f"{col.concatenar(tabla,arbol)}"
            elif isinstance(col, Llamada):
                cadena += f"{col.concatenar2(tabla, arbol)}"
            
            if self.tipoIndex == "NULLS FIRST":
                cadena += " NULLS FIRST"
            elif self.tipoIndex == "DESC NULLS LAST":
                cadena += " DESC NULLS LAST"
            if(self.lcol.index(col)< (len(self.lcol)-1)):
                cadena +=", "
        cadena += ")"
        if(self.where !=None):
            if isinstance(self.where, str):
                cadena+= f" {self.where}"
            else:
                cadena += f" {self.where.traducir(tabla,arbol)}"
        cadena += ";\""

        


        arbol.addComen("Asignar cadena")
        temporal1 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = { cadena }")

        arbol.addComen("Entrar al ambito")
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal2} = P+2")
        temporal3 = tabla.getTemporal()
        arbol.addComen("parametro 1")
        arbol.addc3d(f"{temporal3} = { temporal2}+1")
        arbol.addComen("Asignacion de parametros")
        arbol.addc3d(f"Pila[{temporal3}] = {temporal1}")

        arbol.addComen("Llamada de funcion")
        arbol.addc3d(f"P = P+2")
        arbol.addc3d(f"funcionintermedia()")
        
        arbol.addComen("obtener resultado")
        temporalX = tabla.getTemporal()
        arbol.addc3d(f"{temporalX} = P+2")
        temporalR = tabla.getTemporal()
        arbol.addc3d(f"{temporalR} = Pila[{ temporalX }]")

        arbol.addComen("Salida de funcion")
        arbol.addc3d(f"P = P-2")
'''
columnas y filas
matrix = np.array(([[1,"k","t"],[2,"L","a"],[3,"N","y"]]))
nueva_Fila = lista[2]
nueva_Columna2 = matrix[:, [0, 2]]    
Numero de Filas
a.shape[0]
Numero de columnas
a.shape[1]
limite
a = sorted(a, key=lambda a_entry: a_entry[2])

'''    