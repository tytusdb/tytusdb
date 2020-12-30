#from Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
#from storageManager.jsonMode import *
from Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

#ALTER
class AlterDatabase(Instruccion):
    '''#1 rename
       #2 owner'''
    def __init__(self, caso, name, newName,fila,columna):
        self.caso = caso
        self.name = name
        self.newName = newName
        self.fila = fila
        self.columna = columna

    def ejecutar(alterdatabase,ts,consola,exceptions):

        #por el momemnto solo renombrar
        print("Estoy aqui")

        if ts.validar_sim(alterdatabase.name) == 1 and alterdatabase.caso== 1:

            anterior = ts.buscar_sim(alterdatabase.name)
            nuevo = TS.Simbolo(anterior.categoria,alterdatabase.newName, anterior.tipo,anterior.valor,anterior.Entorno)
            ts.agregar_sim(nuevo)
            ts.eliminar_sim(alterdatabase.name)
            alterDatabase(alterdatabase.name,alterdatabase.newName)
            consola.append(f"BD {alterdatabase.name} renombrada a {alterdatabase.newName}")
        else:

            consola.append(f"42P01	undefined_table, Error alter no existe la tabla {alterdatabase.name}")
            exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la tabla {alterdatabase.name}-fila-columna")
        #caso 1
        print("")