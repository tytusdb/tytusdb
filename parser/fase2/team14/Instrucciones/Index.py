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
                            nuevoSym.baseDatos = dbActual
                            idIdex += "_" + nombreCol.valor + "_" + self.iden
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
        
    def traducir(self,ent:Entorno):
        cad:str = "ci.ejecutarsql('create "
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

        cad += ");')"

        self.codigo3d = cad
        return self