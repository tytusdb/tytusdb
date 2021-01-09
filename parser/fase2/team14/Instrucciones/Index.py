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

    def ejecutar(self, ent: Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            tablaIndex: Simbolo = ent.buscarSimbolo(self.tabla + "_" + dbActual)
            if tablaIndex != None:
                for nombreCol in self.columnas:
                    i = 0
                    fin = len(tablaIndex.valor)
                    while i < fin:
                        if nombreCol.valor == tablaIndex.valor[i].nombre:
                            # IDX_database_tabla
                            idIdex: str = "IDX_" + dbActual + "_" + self.tabla + "_" + self.iden + "_" + nombreCol.valor
                            nuevoSym: Simbolo = Simbolo(TipoSimbolo.INDEX,idIdex,{})
                            nuevoSym.tabla = self.tabla
                            nuevoSym.indexId = self.iden
                            nuevoSym.baseDatos = dbActual
                            nuevoSym.valor.update({'id': self.iden, 'columna': nombreCol.valor})
                            if self.unique:
                                nuevoSym.valor.update({'unique': True})
                            if self.hash:
                                nuevoSym.valor.update({'hash': True})
                            if self.orden != None:
                                nuevoSym.valor.update({'orden': self.orden})
                            tablaIndex.valor[i].atributos.update({'index': idIdex})
                            res = ent.nuevoSimbolo(nuevoSym)
                            if res == "ok":
                                variables.consola.insert(INSERT,
                                                     "Se agregó nuevo index '" + self.iden + "' a la columna '" + nombreCol.valor + "'\n")
                            else:
                                variables.consola.insert(INSERT,
                                                     "El nuevo index '" + self.iden + "' no se puede agregar porque ya existe.\n")
                                reporteerrores.append(Lerrores("Semántico",
                                    "El nuevo index '" + self.iden + "' no se puede agregar porque ya existe.\n","",""))
                            break

                        i = i + 1
            else:
                variables.consola.insert(INSERT,
                                         "La tabla '" + self.tabla + "' a la que se le desea agregar el índice '" + self.iden + "' no existe.\n")
                reporteerrores.append(Lerrores("Semántico",
                                               "La tabla '" + self.tabla + "' a la que se le desea agregar el índice '" + self.iden + "' no existe",
                                               "", ""))

    def traducir(self, ent: Entorno):
        cad: str = "ci.ejecutarsql(\"create "
        if self.unique:
            cad += "unique "
        cad += "index " + self.iden + " on " + self.tabla
        if self.hash:
            cad += " using hash"
        cad += " (" + str(self.columnas[0].valor)
        if self.orden != None:
            cad += " " + self.orden
        for x in range(1, len(self.columnas), 1):
            cad += "," + str(self.columnas[x].valor)

        cad += ");\")\n"

        self.codigo3d = cad
        return self


class AlterIndex(Instruccion):
    def __init__(self, id, ifExist: bool, palabraColumn: bool, colIdx):
        self.iden = id
        self.ifExist = ifExist
        self.colIdx = colIdx
        self.palabraColumn = palabraColumn

    def ejecutar(self, ent: Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            sym: Simbolo = ent.buscarIndex(self.iden)
            if sym != None:
                tabla: Simbolo = ent.buscarSimbolo(sym.tabla + "_" + dbActual)
                if tabla != None:
                    columna = self.colIdx
                    if isinstance(self.colIdx, int):
                        if self.colIdx <= len(tabla.valor):
                            columna = tabla.valor[self.colIdx - 1].nombre
                        else:
                            variables.consola.insert(INSERT,
                                                     "El número '" + str(
                                                         self.colIdx) + "' de columna en la tabla '" + sym.tabla + "' no existe.\n")
                            reporteerrores.append(Lerrores("Semántico", "El número '" + str(
                                self.colIdx) + "' de columna en la tabla '" + sym.tabla + "' no existe.", "", ""))
                            return

                    for col in tabla.valor:
                        if col.nombre == columna:
                            sym.valor.update({'columna': columna})
                            variables.consola.insert(INSERT,
                                                     "El index '" + self.iden + "' ahora pertenece a la columna '" + columna + "'\n")
                            return

                    variables.consola.insert(INSERT,
                                             "La columna '" + columna + "' a la que desea cambiar el índice '" + self.iden + "' no existe.\n")
                    reporteerrores.append(Lerrores("Semántico",
                                                   "La columna '" + columna + "' a la que desea cambiar el índice '" + self.iden + "' no existe.",
                                                   "", ""))
            else:
                variables.consola.insert(INSERT, "El index '" + self.iden + "' no existe \n")
                reporteerrores.append(Lerrores("Semántico", "El index '" + self.iden + "' no existe", "", ""))

    def traducir(self, ent: Entorno):
        self.codigo3d = 'ci.ejecutarsql("alter index '
        if self.ifExist:
            self.codigo3d += 'if exists '
        self.codigo3d += self.iden + ' alter '
        if self.palabraColumn:
            self.codigo3d += 'column '
        self.codigo3d += str(self.colIdx) + ';")\n'

        return self


class DropIndex(Instruccion):
    def __init__(self, id):
        self.iden = id

    def ejecutar(self, ent: Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            res = ent.eliminarIndex(self.iden)
            if res:
                variables.consola.insert(INSERT, "El índice '" + self.iden + "' se ha eliminado. \n")
            else:
                variables.consola.insert(INSERT, "El índice '" + self.iden + "' que desea eliminar no existe.\n")
                reporteerrores.append(
                    Lerrores("Semántico", "El índice '" + self.iden + "' que desea eliminar no existe.", "", ""))

    def traducir(self, ent: Entorno):
        self.codigo3d = 'ci.ejecutarsql("drop index ' + self.iden + ';")\n'
        return self