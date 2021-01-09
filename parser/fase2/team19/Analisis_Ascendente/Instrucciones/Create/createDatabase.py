#from Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
#from storageManager.jsonMode import *
from Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes


#CREATE [OR REPLACE] DATABASE
class CreateReplace(Instruccion):
    '''#1 create
       #2 create or replace'''
    def __init__(self, caso, exists, id, complemento,fila,columna):
        self.caso = caso
        self.exists = exists
        self.id = id
        self.complemento = complemento
        self.fila = fila
        self.columna = columna


    def ejecutar(createDataBase, ts,consola,exceptions):
        if createDataBase.complemento is not None:
            if createDataBase.complemento.mode is not None:
                if createDataBase.complemento.mode > 5 or createDataBase.complemento.mode < 1:
                    consola.append(f"El modo para la base de datos {createDataBase.id} debe estar entre 1 y 5\n")
                    return
        lb = showDatabases()
        if createDataBase.id in lb:
            if createDataBase.exists:
                #print("no pasa nada")
                return
            elif createDataBase.caso == 2:
                # se borra a nivel de memoria en disco
                dropDatabase(str(createDataBase.id))
                # se quita el id de la tabla de simbolos
                ts.eliminar_sim(str(createDataBase.id))
            else:
                consola.append(f"La Base de Datos {createDataBase.id} ya existe, error al crear\n")
                return

        createDatabase(str(createDataBase.id))
        entorno_bd = {}
        ts_local = TS.TablaDeSimbolos(entorno_bd)
        # simbolo (self, categoria,id, tipo, valor,Entorno):
        simbolo = TS.Simbolo(TS.TIPO_DATO.BASEDEDATOS, createDataBase.id, None, 0, ts_local)  # inicializamos con 0 como valor por defecto
        ts.agregar_sim(simbolo)
        if (createDataBase.id in lb) and createDataBase.caso == 2:
            consola.append(f"Replace, la base de datos {createDataBase.id} se ha creado exitosamente\n")
        else:
            consola.append(f"Se creo la base de datos {createDataBase.id} exitosamente\n")
        #print(ts.simbolos)

    def getC3D(self, lista_optimizaciones_C3D):

        etiqueta = GeneradorTemporales.nuevo_temporal()
        instruccion_quemada = 'create '
        if self.caso == 2:
            instruccion_quemada += 'or replace '
        instruccion_quemada += 'database '
        if self.exists:
            instruccion_quemada += 'if not exists '
        instruccion_quemada += '%s ' % self.id
        if self.complemento is not None:
            instruccion_quemada += self.complemento.getC3D()
        instruccion_quemada += ';'
        c3d = '''
    # ---------CREATE DATABASE-----------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s
 
''' % (etiqueta, instruccion_quemada, etiqueta)

        return c3d




#complemento de create or replace
class ComplementoCR(Instruccion):
    def __init__(self, idOwner, mode,fila,columna):
        self.idOwner = idOwner
        self.mode = mode
        self.fila = fila
        self.columna = columna

    def getC3D(self):
        instruccion_quemada = ''
        if self.idOwner is not None:
            instruccion_quemada = "owner = '%s' " % self.idOwner
        if self.mode is not None:
            instruccion_quemada += 'mode = %s ' % self.mode
        return instruccion_quemada

