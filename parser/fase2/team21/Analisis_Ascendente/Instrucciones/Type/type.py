from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import Primitivo
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
#TYPE
class CreateType(Instruccion):
    def __init__(self, id, lista,concatena,fila,columna):
        self.id = id
        self.lista = lista
        self.concatena = concatena
        self.fila = fila
        self.columna = columna

    def ejecutar(createType,ts,consola,exceptions):


        if ts.validar_sim(createType.id) == -1:

            datavalidada = []

            for data in createType.lista:
                resultado = Expresion.Resolver(data,ts,consola,exceptions)
                datavalidada.append(resultado)

            nuevo_tipo = TS.Simbolo(TS.TIPO_DATO.CLASEENUMERADA,createType.id,"Enum",datavalidada,None)
            ts.agregar_sim(nuevo_tipo)
            consola.append(f"Se añadio una clase enum llamada  {createType.id}")

        else:

            consola.append(f"Ya existe esta clase enumerada")
    def traducir(instr, ts, consola, exceptions,tv):
        # info = ""
        # print("concatena \n")
        # print(instr.concatena)
        # for data in instr.concatena:
        #   info += " " + data

        # consola.append(info)
        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{instr.concatena}\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")

        #contador = tv.Temp()
        #consola.append(f"\n\t{contador} = \"{instr.concatena}\"")
        #contador2 = tv.Temp()
        #consola.append(f"\n\t{contador2} = T({contador})")
        #consola.append(f"\n\tstack.append({contador2})\n")