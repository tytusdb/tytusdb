#from Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
#from storageManager.jsonMode import *
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

#ALTER
class AlterDatabase(Instruccion):
    '''#1 rename
       #2 owner'''
    def __init__(self, caso, name, newName,concatena,fila,columna):
        self.caso = caso
        self.name = name
        self.newName = newName
        self.concatena = concatena
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

    def traducir(alter,consola,tv):

        #iniciar traduccion
        info = "" #info contiene toda el string a mandar como parametros
        print("concatena \n")
        print(alter.concatena)
        for data in alter.concatena:
            info += " " +data

        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{info}\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")
        #contador = tv.Temp()
        #consola.append(f"\n\t{contador} = \"{info}\"")

        #consola.append(f"\n\tarbol = obtener_arbol({contador})")
        #consola.append(f"\n\tstack.append(arbol)\n")
