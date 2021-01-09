#from Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import Id
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
#from storageManager.jsonMode import *
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS



#DELETE
class Delete(Instruccion):
    def __init__(self,caso, id, where,concatena,fila,columna):
        self.caso = caso
        self.id = id
        self.where = where
        self.concatena = concatena
        self.fila = fila
        self.columna = columna

    def ejecutar(deleteData, ts, consola, exceptions):


        #insert('test','tbventa',[1,4,'2020-10-12',450,'False','Venta de bomba de agua para toyota'])
        #insert('test','tbventa',[2,4,'2020-10-12',450,'False','Venta de bomba de agua para toyota'])

        if ts.validar_sim("usedatabase1234") == 1:

            # nombre de la bd
            bdactual = ts.buscar_sim("usedatabase1234")
            # se busca el simbolo y por lo tanto se pide el entorno de la bd
            BD = ts.buscar_sim(bdactual.valor)
            entornoBD = BD.Entorno
            print(deleteData.id," -> nombre tabla")
            if entornoBD.validar_sim(deleteData.id) == 1:

                simbolo_tabla = entornoBD.buscar_sim(deleteData.id)

                if deleteData.where == None:

                    truncate(BD.id,simbolo_tabla.id)
                else:

                    datoiz= deleteData.where.iz
                    datodr = deleteData.where.dr
                    operador = deleteData.where.operador

                    resultado = Expresion.Resolver(datodr,ts,consola,exceptions)
                    #consola.append(f" El resultado es: {str(resultado)}")
                    print("el nombre del campo es: ",datoiz.id)
                    if simbolo_tabla.Entorno.validar_sim(datoiz.id) == 1:
                        campos = simbolo_tabla.Entorno.simbolos
                        i =0
                        data = []
                        data.append(resultado)
                        if delete(BD.id,simbolo_tabla.id,data) == 0:
                            consola.append(f"Delete from {simbolo_tabla.id} exitosamente")
                        else:
                            consola.append(
                                f"22005-error_in_assignment no existe la llave en tabla {simbolo_tabla.id}-{deleteData.fila}-{deleteData.columna}")

                            exceptions.append(
                                f"Error semantico-22005-error_in_assignment no existe la columna  en tabla {simbolo_tabla.id}-{deleteData.fila}-{deleteData.columna}")

                    else:
                        consola.append(
                            f"Error semantico-22005-error_in_assignment no existe la columna en tabla {simbolo_tabla.id}-{deleteData.fila}-{deleteData.columna}")

                        exceptions.append(
                            f"Error semantico-22005-error_in_assignment no existe la columna  en tabla {simbolo_tabla.id}-{deleteData.fila}-{deleteData.columna}")

                    print("ejecuntando un delete")





            else:
                consola.append(f"42P01	undefined_table, no existe la tabla {deleteData.id}")
                exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la tabla {deleteData.id}-{deleteData.fila}-{deleteData.columna}")


        else:
            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")
            consola.append(
                f"Error semantico-22005-error_in_assignment No se ha seleccionado DB-{deleteData.fila}-{deleteData.columna}")

            exceptions.append(f"Error semantico-22005-error_in_assignment No se ha seleccionado DB-{deleteData.fila}-{deleteData.columna}")

        print("ejecuntando un delete")

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