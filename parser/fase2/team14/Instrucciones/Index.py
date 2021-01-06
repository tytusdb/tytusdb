from Instrucciones.Instruccion import Instruccion
from Instrucciones.AtrColumna import AtributosColumna
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.variablesestaticas import variables
from tkinter import *
from reportes import *

class Index(Instruccion):
    def __init__(self, iden, tabla, columnas):
        self.iden = iden
        self.tabla = tabla
        self.columnas = columnas
        self.unique = False
        self.orden = None
        self.hash = False

    def ejecutar(self,ent:Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            tablaIndex:Simbolo = ent.buscarSimbolo(self.tabla + "_" + dbActual)
            if tablaIndex != None:
                #IDX_database_tabla
                idIdex:str = "IDX_" + dbActual + "_" + self.tabla
                for nombreCol in self.columnas:
                    i = 0
                    fin = len(tablaIndex.valor)
                    while i < fin:
                        if nombreCol.valor == tablaIndex.valor[i].nombre:
                            nuevoSym:Simbolo = Simbolo(TipoSimbolo.INDEX)
                            nuevoSym.tabla = self.tabla
                            nuevoSym.indexId = self.iden
                            nuevoSym.baseDatos = dbActual
                            idIdex += "_" + self.iden + "_" + nombreCol.valor
                            nuevoSym.nombre = idIdex
                            nuevoSym.valor = {}
                            nuevoSym.valor.update({'id':self.iden,'columna':nombreCol.valor})
                            if self.unique:
                                nuevoSym.valor.update({'unique':True})
                            if self.hash:
                                nuevoSym.valor.update({'hash':True})
                            if self.orden != None:
                                nuevoSym.valor.update({'orden':self.orden})
                            tablaIndex.valor[i].atributos.update({'index':idIdex})
                            ent.nuevoSimbolo(nuevoSym)
                            variables.consola.insert(INSERT,"Se agregó nuevo index '" + self.iden + "' a la columna '" + nombreCol.valor + "'\n")
                            break
                        
                        i = i + 1
            else:
                variables.consola.insert(INSERT,"La tabla '" + self.tabla + "' a la que se le desea agregar el índice '" + self.iden +"' no existe.\n")
                reporteerrores.append(Lerrores("Semántico","La tabla '" + self.tabla + "' a la que se le desea agregar el índice '" + self.iden +"' no existe","",""))
        
    def traducir(self,ent:Entorno):
        cad:str = "ci.ejecutarsql(\"create "
        if self.unique:
            cad += "unique "
        cad += "index " + self.iden + " on " + self.tabla
        if self.hash:
            cad += " using hash"
        cad += " (" + str(self.columnas[0].valor)
        if self.orden != None:
            cad += " " + self.orden
        for x in range(1, len(self.columnas),1):
            cad += "," + str(self.columnas[x].valor)

        cad += ");\")\n"

        self.codigo3d = cad
        return self

class AlterIndex(Instruccion):
    def __init__(self,id,ifExist:bool,palabraColumn:bool,colIdx):
        self.iden = id
        self.ifExist = ifExist
        self.colIdx = colIdx
        self.palabraColumn = palabraColumn
    
    def ejecutar(self, ent:Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            sym = ent.buscarIndex(self.iden)
            if sym != None:
                sym.valor.update({'columna':self.colIdx})
                variables.consola.insert(INSERT,"El index '" + self.iden + "' ahora pertenece a la columna '" + self.colIdx + "'\n")
            else: 
                variables.consola.insert(INSERT,"El index '" + self.iden + "' no existe \n")
                reporteerrores.append(Lerrores("Semántico","El index '" + self.iden + "' no existe","",""))
    
    def traducir(self,ent:Entorno):
        self.codigo3d = 'ci.codigosql("alter index '
        if self.ifExist:
            self.codigo3d += 'if exists '
        self.codigo3d += self.iden + ' alter '
        if self.palabraColumn:
            self.codigo3d += 'column '
        self.codigo3d += self.colIdx + ';")\n'

        return self


class DropIndex(Instruccion):
    def __init__(self,id):
        self.iden = id
    
    def ejecutar(self, ent:Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            res = ent.eliminarIndex(self.iden)
            if res:
                variables.consola.insert(INSERT,"El índice '" + self.iden + "' se ha eliminado. \n")
    
    def traducir(self, ent:Entorno):
        self.codigo3d = 'ci.ejecutarsql("drop index ' + self.iden + ';")\n'
        return self