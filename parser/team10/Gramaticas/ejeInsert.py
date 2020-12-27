from instruccion import *
from funcionesTS import *
from expresiones import *
from conexionDB import *
from VerificarDatos import *
from funcionesNativas import * 
import EjecutarOperacion as operadores


class analisisInsert():
    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas

    def iniciarInsert(self, instru):
        ops1 = instru.identificador
        inseCont = instru.insertCont

        if isinstance(inseCont , InsertarCont):
            obValues = inseCont.values
            lisInsert = inseCont.listaInsertar
            listaInsertaran =[]
            oper = operadores.ExecOperacion(self.conectar,self.ts)
            for opers in lisInsert:
                obOpers = oper.ejecutar_operacion(opers)
                listaInsertaran.append(obOpers)

            self.conectar.cmd_insert(self.baseActual,self.tablaActual, listaInsertaran)

        elif isinstance(inseCont, InsertarCont2):
            listCam = inseCont.lista_campos
            obValues = inseCont.values
            lisInsert = inseCont.listaInsertar
            listCamps =[]
            oper = operadores.ExecOperacion(self.conectar,self.ts)
            for campss in listCam:
                if isinstance(campss, ids):
                    listCamps.append(campss.ids)

            listaInseraran = []
            for opers in lisInsert:
                obOpers = oper.ejecutar_operacion(opers)
                listaInseraran.append(obOpers)


