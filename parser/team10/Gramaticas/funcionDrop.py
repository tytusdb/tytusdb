from instruccion import *
from funcionesTS import *
from expresiones import *
from conexionDB import *
from VerificarDatos import *
from funcionesNativas import * 

class ejecutarDrop():
    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas


    def iniciarDrop(self, instru):
        objs1 = instru.objeto
        sentIf=  instru.if_exist

        if objs1.var == 'table':

            if isinstance(sentIf, IfExist):
                self.conectar.cmd_dropTable(self.baseActual, sentIf.identificador)
            elif isinstance(sentIf, ids):
                self.conectar.cmd_dropTable(self.baseActual, sentIf.ids)

        elif objs1.var == 'database':
            if isinstance(sentIf, IfExist):
                self.conectar.dropDatabase(sentIf.identificador)
            elif isinstance(sentIf, ids):
                self.conectar.dropDatabase(sentIf.ids)


class ejecutarTruncate():
    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas

    def iniciarTruncate(self, instru):
        idss= instru.identificador
        self.conectar.cmd_truncate(self.baseActual, idss)





