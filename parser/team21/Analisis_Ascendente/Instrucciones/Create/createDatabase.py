
from Instrucciones.instruccion import Instruccion
#from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from storageManager.jsonMode import *
#from Compi2RepoAux.team21.Analisis_Ascendente.storageManager.jsonMode import *
import Tabla_simbolos.TablaSimbolos as ts
#import Compi2RepoAux.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS



from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Compi2RepoAux.team21.Analisis_Ascendente.storageManager.jsonMode import *
import Compi2RepoAux.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as ts


#CREATE [OR REPLACE] DATABASE
class CreateReplace(Instruccion):
    '''#1 create
       #2 create or replace'''
    def __init__(self, caso, exists, id, complemento):
        self.caso = caso
        self.exists = exists
        self.id = id
        self.complemento = complemento

    def ejecutar(createDataBase, ts,consola):

        if createDataBase.caso==1 and createDataBase.exists==False or createDataBase.exists==True:
            #create database
            lb = showDatabases()
            for bd in lb:
                if bd == createDataBase.id:
                    consola.append(f"La Base de Datos {createDataBase.id} ya existe, error al crear\n")
                    return

            createDatabase(str(createDataBase.id))
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            # simbolo (self, categoria,id, tipo, valor,Entorno):
            simbolo = TS.Simbolo(None, createDataBase.id, TS.TIPO_DATO.BASEDEDATOS, 0,ts_local)  # inicializamos con 0 como valor por defecto
            ts.agregar_sim(simbolo)
            consola.append(f"Se creo la base de datos {createDataBase.id} exitosamente\n")
            print(ts.simbolos)


        elif createDataBase.caso== 2 and createDataBase.exists==False:
            #create or replace
            lb = showDatabases()
            for bd in lb:
                if bd == createDataBase.id:

                    # se borra a nivel de memoria en disco
                    dropDatabase(str(createDataBase.id))
                    # se quita el id de la tabla de simbolos
                    ts.eliminar_sim(str(createDataBase.id))
                    # simbolo (self, categoria,id, tipo, valor,Entorno):
                    # se vuelve a crear un entorno para agregar de nuevo la base de datos
                    createDatabase(str(createDataBase.id))
                    ts_local = TS.TablaDeSimbolos(ts.simbolos)
                    simbolo = TS.Simbolo(None, createDataBase.id, TS.TIPO_DATO.BASEDEDATOS, 0,ts_local)  # inicializamos con 0 como valor por defecto
                    ts.agregar_sim(simbolo)
                    consola.append(f"Replace, la base de datos {createDataBase.id} se ha creado exitosamente\n")
                    print(ts.simbolos)
                    return


            createDatabase(str(createDataBase.id))
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            # simbolo (self, categoria,id, tipo, valor,Entorno):
            simbolo = TS.Simbolo(None, createDataBase.id, TS.TIPO_DATO.BASEDEDATOS, 0,ts_local)  # inicializamos con 0 como valor por defecto
            ts.agregar_sim(simbolo)
            consola.append(f"Se creo la base de datos {createDataBase.id} exitosamente\n")
            print(ts.simbolos)

        elif createDataBase.caso == 2 and createDataBase.exists == True:
            #create or replace if not exists
            lb = showDatabases()
            for bd in lb:
                if bd == createDataBase.id:
                    consola.append("La Base de Datos ya existe no se puede reemplazar")

                    return


            createDatabase(str(createDataBase.id))
            ts_local = TS.TablaDeSimbolos(ts.simbolos)
            # simbolo (self, categoria,id, tipo, valor,Entorno):
            simbolo = TS.Simbolo(None, createDataBase.id, TS.TIPO_DATO.BASEDEDATOS, 0,ts_local)  # inicializamos con 0 como valor por defecto
            ts.agregar_sim(simbolo)
            consola.append(f"Se creo la base de datos {createDataBase.id} exitosamente\n")
            print(ts.simbolos)







#complemento de create or replace
class ComplementoCR(Instruccion):
    def __init__(self, idOwner, mode):
        self.idOwner = idOwner
        self.mode = mode

