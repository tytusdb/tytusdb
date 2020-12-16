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
       # print(ts.validar_sim(createDataBase.id),"<------",createDataBase.id)

            lb = showDatabases()
            for bd in lb:
                if bd == createDataBase.id:
                    consola.append("La Base de Datos ya existe\n")
                    return

            createDatabase(str(createDataBase.id))
            consola.append(f"Se creo la base de datos {createDataBase.id} exitosamente\n")


#complemento de create or replace
class ComplementoCR(Instruccion):
    def __init__(self, idOwner, mode):
        self.idOwner = idOwner
        self.mode = mode

