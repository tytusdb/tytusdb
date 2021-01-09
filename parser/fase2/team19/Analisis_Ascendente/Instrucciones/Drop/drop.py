#from Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
#from storageManager.jsonMode import *
from Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales

#DROP
class Drop(Instruccion):
    '''#1 database
       #2 table'''
    def __init__(self, caso, exists, id,fila,columna):
        self.caso = caso
        self.exists = exists
        self.id = id
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
                        consola.append(f"La bd {dropObject.id} no existe, pero no hubo error")
                    else:
                        consola.append(f"42P01	undefined_table, no existe la tabla {dropObject.id}")
                        exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la bd {dropObject.id}-fila-columna")

        else:

            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")
            exceptions.append("Error semantico-22005	error_in_assignment-No se ha seleccionado DB-fila-columna")

    def getC3D(self, lista_optimizaciones_C3D):
        temporal = GeneradorTemporales.nuevo_temporal()
        codigo_quemado = ''
        if self.caso == 2: #Drop table
            codigo_quemado = 'drop table '
        else: #Drop database
            codigo_quemado = 'drop database '
            if self.exists:
                codigo_quemado += 'if exists '
        codigo_quemado += '%s ;' % self.id
        c3d = '''
    # ----------DROP %s-----------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s
''' % ('DATABASE' if self.caso == 2 else 'TABLE---', temporal, codigo_quemado, temporal)
        return c3d







