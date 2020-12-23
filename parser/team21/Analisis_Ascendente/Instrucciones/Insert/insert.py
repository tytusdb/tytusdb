from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Compi2RepoAux.team21.Analisis_Ascendente.storageManager.jsonMode import *
import Compi2RepoAux.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

#INSERT INTO
class InsertInto(Instruccion):
    def __init__(self,caso, id, listaId, values,fila,columna):
        self.caso=caso
        self.id = id
        self.listaId = listaId
        self.values = values
        self.fila = fila
        self.columna = columna


    def ejecutar(insertinto,ts,consola,exceptions):


        if ts.validar_sim("usedatabase1234") == 1:

            if insertinto.caso==1:
                for data in insertinto.listaId:
                    print("-> ",data.id)

                for data in insertinto.values:
                    print("val :",data.valor)

                consola.append(f"insert en la tabla {insertinto.id}, exitoso\n")
            else:
                print("caso 2")
                for data in insertinto.values:
                    print("val :",data.valor)
                consola.append(f"insert en la tabla {insertinto.id}, exitoso\n")

        else:
            consola.append("42P12	invalid_database_definition, Error al insertar\n")
            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")
            exceptions.append("Error semantico-22005	error_in_assignment-No se ha seleccionado DB-fila-columna")