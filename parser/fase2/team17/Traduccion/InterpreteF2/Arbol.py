from typing import List
from InterpreteF2.Reporteria.ReporteTS_Indice import ReportIndice


class Arbol:

    def __init__(self, instructions):
        self.instrucciones:list = instructions
        self.console:list = []
        self.ErroresSemanticos:list = []
        self.ErroresLexicos: list = []
        self.ErroresSintacticos: list = []
        self.ReporteTS: list = []
        self.ReporteTS_Funciones: list = []
        self.ReporteTS_Indice:List[ReportIndice] = []
        self.ReporteOptimizacion: list = []

        # Soporte de temporales
        self.noTemp:int = 0
        self.ultimoTemp = ""

        # Soporte de labels
        self.noLabel:int = 0
        self.ultimoLabel = ""

        self.C3D = ""
        self.C3Dfunciones = ""
        self.C3D_inficador = 0 # <-- 0 = C3D and 1 = codigo externo de funciones
        self.contadorIdentacion:int = 1
        self.contadorIdentacion_funciones:int = 0

    def getTemp(self) -> str:
        temporal = "t" + str(self.noTemp)
        self.ultimoTemp = temporal
        self.noTemp = self.noTemp + 1
        return str(temporal)

    def getLabel(self) -> str:
        label = "L" + str(self.noLabel)
        self.ultimoLabel = label
        self.noLabel = self.noLabel + 1
        return str(label)

    def addC3D(self, data):
        if data != None:
            if self.C3D_inficador == 0:
                self.C3D = self.C3D + self.getIdentacion() + str(data) + "\n"
            else:
                self.C3Dfunciones = self.C3Dfunciones + self.getIdentacion() + str(data) + "\n"
        else:
            pass

    def getC3D(self):
        return self.C3D

    def addIdentacion(self):
        if self.C3D_inficador == 0:
            self.contadorIdentacion = self.contadorIdentacion + 1
        else:
            self.contadorIdentacion_funciones = self.contadorIdentacion_funciones + 1

    def popIdentacion(self):
        if self.C3D_inficador == 0:
            self.contadorIdentacion = self.contadorIdentacion - 1
        else:
            self.contadorIdentacion_funciones = self.contadorIdentacion_funciones - 1

    def getIdentacion(self):
        indentacion = ''
        if self.C3D_inficador == 0:
            iterador = range(self.contadorIdentacion)
            for i in iterador:
                indentacion = indentacion + '\t'
        else:
            iterador = range(self.contadorIdentacion_funciones)
            for i in iterador:
                indentacion = indentacion + '\t'
        return indentacion

    # ---------------- Soporte de acesos
    def switchC3Dmain(self):
        self.C3D_inficador = 0
    def switchC3Dfunciones(self):
        self.C3D_inficador = 1

    #--- funcones
    def getC3D_funciones(self):
        return self.C3Dfunciones

    def getIdentacion_funciones(self):
        indentacion = ''
        iterador = range(self.contadorIdentacion_funciones)
        for i in iterador:
            indentacion = indentacion + '\t'
        return indentacion

    def resetIdentacion_funciones(self):
        self.contadorIdentacion_funciones = 0
        self.C3Dfunciones = self.C3Dfunciones + "\n"

    # soporte para simulacion de funciones
    def dropFuncione(self, id):
        #contador:int = 0
        #for i in self.ReporteTS_Funciones:
        #    if str(i.nombre) == str(id):
        #        self.ReporteTS_Funciones.pop(contador)
        #        return
        #    contador = contador + 1

        for i in self.ReporteTS_Funciones:
            if str(i.nombre) == str(id):
                i.estado = 'INACTIVO'
                return
        return

    def existFun(self, id):
        for i in self.ReporteTS_Funciones:
            if str(i.nombre) == str(id):
                return True
        return False

    def lFun_isINACTIVE(self, id):
        for i in self.ReporteTS_Funciones:
            if str(i.nombre) == str(id):
                if str(i.estado) == 'INACTIVO':
                    return True
        return False

    def covertInactivaeTOactivate(self, id):
        for i in self.ReporteTS_Funciones:
            if str(i.nombre) == str(id):
                i.estado = 'ACTIVO'
                return
        return
