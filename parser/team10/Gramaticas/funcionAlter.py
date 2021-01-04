from instruccion import *
from funcionesTS import *
from expresiones import *
from conexionDB import *
from VerificarDatos import *
from funcionesNativas import * 






class ejecutarAlter():

    def __init__(self, tablaActual, baseActual, conectar, ts , listaTablas):
        self.conectar = conectar
        self.ts  = ts
        self.tablaActual = tablaActual
        self.baseActual = baseActual
        self.listaTablas = listaTablas

    def inicialAlter(self, instru):
        getInstru = instru.alterObjeto

        if isinstance(getInstru, tabla):
            idTabla = getInstru.identificador
            alterns = getInstru.alterno

            if isinstance(alterns, conAdd):
                getAdds = alterns.tipo
                if isinstance(getAdds, columnas):
                    id1= getAdds.identificador
                    tiposs= getAdds.tipo
                    campo = self.ts.devolverCampo(self.baseActual,self.tablaActual,id1)
                    self.conectar.cmd_alterAddColumn(self.baseActual,self.tablaActual,id1,tiposs,campo)
                    
                elif isinstance(getAdds , checks):
                    chequeo = getAdds.tipo
                    id1= getAdds.identificador
                    tiposs= getAdds.tipo
                    campo = self.ts.devolverCampo(self.baseActual,self.tablaActual,id1)
                    campo.setCheck(chequeo)

                elif isinstance(getAdds, foreingKey):
                    llaveF = getAdds.tipo


            elif isinstance(alterns , conDrop ):
                tiposs = alterns.tipo
                id1 = alterns.identificador
                if tiposs == 'column':
                    self.conectar.cmd_alterDropColumn(self.baseActual,self.tablaActual,id1)
                elif tiposs == 'constraint':
                    print('constraint reconocido')
                                    

            elif isinstance(alterns, conRename):
                id1 = alterns.identificador
                id2 = alterns.identificador2
                self.conectar.cmd_alterTable(self.baseActual, id1, id2)
                self.tablaActual = id2


            elif isinstance(alterns, ConAlter):
                id1 = alterns.identificador
                opcNull = alterns.setNull



        elif isinstance(getInstru, dataBase):
            id1 = getInstru.identificador
            id2 = getInstru.identificador2
            opcion = getInstru.usuario
            if opcion=='rename':
                self.conectar.cmd_alterDatabase(id1, id2)
                self.baseActual = id2

            elif opcion == 'owner':
                self.conectar.cmd_alterDatabase(id1, id2)
                self.baseActual = id2

    def devolverTabla(self):
        return self.tablaActual

    def devolverBase(self):
        return self.baseActual


