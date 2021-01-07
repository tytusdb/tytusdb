#from Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
#from storageManager.jsonMode import *
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

tablaSimbolosAux = None
consolaAuxiliar = None
excepcionesAux = None
#DROP
class Drop(Instruccion):
    '''#1 database
       #2 table'''
    def __init__(self, caso, exists, id,concatena,fila,columna):
        self.caso = caso
        self.exists = exists
        self.id = id
        self.concatena = concatena
        self.fila = fila
        self.columna = columna


    def ejecutar(dropObject,ts,consola,exceptions):



        if ts.validar_sim("usedatabase1234") == 1:


            if (dropObject.caso == 2):

                bdactual = ts.buscar_sim("usedatabase1234")
                # se busca el simbolo y por lo tanto se pide el entorno de la bd
                BD = ts.buscar_sim(bdactual.valor)
                entornoBD = BD.Entorno

                if entornoBD.validar_sim(dropObject.id) == 1:

                    entornoBD.eliminar_sim(dropObject.id)

                    consola.append(f"Tabla {dropObject.id}, eliminada exitosamente")
                    dropTable(BD.id,dropObject.id)

                else:

                   consola.append(f"42P01	undefined_table, no existe la tabla {dropObject.id}")
                   exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la tabla {dropObject.id}-fila-columna")

            else:

                bdactual = ts.buscar_sim("usedatabase1234")
                # se busca el simbolo y por lo tanto se pide el entorno de la bd
                BD = ts.buscar_sim(bdactual.valor)
                entornoBD = BD.Entorno

                if ts.validar_sim(dropObject.id) == 1:

                    ts.eliminar_sim(dropObject.id)

                    consola.append(f"Base datos  {dropObject.id}, eliminada exitosamente")
                    dropDatabase(dropObject.id)

                    if BD.id == dropObject.id:
                        #limpiamos y espera el llamado de otro use
                        ts.eliminar_sim("usedatabase1234")




                else:

                    if dropObject.exists:
                        print("no pasa nada")
                    else:
                        consola.append(f"42P01	undefined_table, no existe la tabla {dropObject.id}")
                        exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la tabla {dropObject.id}-fila-columna")

        else:

            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")
            exceptions.append("Error semantico-22005	error_in_assignment-No se ha seleccionado DB-fila-columna")

    def traducir(instr, ts, consola, exceptions,tv):
        info = ""
        for data in instr.concatena:
            info += " " + data

        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{info}\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")