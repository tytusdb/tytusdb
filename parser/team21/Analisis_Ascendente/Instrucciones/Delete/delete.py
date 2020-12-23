#from Instrucciones.instruccion import Instruccion
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.expresion import Id
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
#from storageManager.jsonMode import *
from Compi2RepoAux.team21.Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import Compi2RepoAux.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS



#DELETE
class Delete(Instruccion):
    def __init__(self,caso, id, where,fila,columna):
        self.caso = caso
        self.id = id
        self.where = where
        self.fila = fila
        self.columna = columna

    def ejecutar(delete,ts,consola,exceptions):


        insert('test','tbventa',[1,4,'2020-10-12',450,'False','Venta de bomba de agua para toyota'])
        insert('test','tbventa',[2,4,'2020-10-12',450,'False','Venta de bomba de agua para toyota'])

        if ts.validar_sim("usedatabase1234") == 1:

            # nombre de la bd
            bdactual = ts.buscar_sim("usedatabase1234")
            # se busca el simbolo y por lo tanto se pide el entorno de la bd
            BD = ts.buscar_sim(bdactual.valor)
            entornoBD = BD.Entorno

            if entornoBD.validar_sim(delete.id) == 1:

                simbolo_tabla = entornoBD.buscar_sim(delete.id)

                if delete.where == None:

                    truncate(BD.id,simbolo_tabla.id)
                else:

                    print(delete.where)

                    datoiz= delete.where.iz
                    datodr = delete.where.dr
                    operador = delete.where.operador
                    print(datoiz.id)
                    print(operador)
                    print(datodr)
                    resultado = Expresion.Resolver(datodr,ts,consola,exceptions)
                    consola.append(f" El resultado es: {str(resultado)}")





                    print(resultado)
                    print("en construccion")




            else:
                consola.append(f"42P01	undefined_table, no existe la tabla {delete.id}")
                exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la tabla {delete.id}-{delete.fila}-{delete.columna}")


        else:
            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")
            consola.append(
                f"Error semantico-22005-error_in_assignment No se ha seleccionado DB-{delete.fila}-{delete.columna}")

            exceptions.append(f"Error semantico-22005-error_in_assignment No se ha seleccionado DB-{delete.fila}-{delete.columna}")

        print("ejecuntando un delete")