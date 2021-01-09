from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from Analisis_Ascendente.Instrucciones.expresion import Primitivo
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.storageManager.jsonMode import *
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
#TYPE
class CreateType(Instruccion):
    def __init__(self, id, lista,fila,columna):
        self.id = id
        self.lista = lista
        self.fila = fila
        self.columna = columna

    def ejecutar(createType,ts,consola,exceptions):


        if ts.validar_sim(createType.id) == -1:

            datavalidada = []

            for data in createType.lista:
                resultado = Expresion.Resolver(data,ts,consola,exceptions)
                datavalidada.append(resultado)

            nuevo_tipo = TS.Simbolo(TS.TIPO_DATO.CLASEENUMERADA, createType.id, "Enum", datavalidada, None)
            ts.agregar_sim(nuevo_tipo)
            consola.append(f"Se añadio una clase enum llamada  {createType.id}")

        else:

            consola.append(f"Ya existe esta clase enumerada")

    def getC3D(self, lista_optimizaciones_C3D):
        etiqueta = GeneradorTemporales.nuevo_temporal()
        listado = None
        for data in self.lista:
            id = Expresion.Resolver(data, None, None, None)
            if listado is None:
                listado = "'%s'" % id
            else:
                listado += ", '%s'" % id
        instruccion_quemada = 'CREATE TYPE %s AS ENUM (%s);' % (self.id, listado)
        c3d = '''
    # ---------CREATE TYPE---------------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s

        ''' % (etiqueta, instruccion_quemada, etiqueta)

        return c3d
