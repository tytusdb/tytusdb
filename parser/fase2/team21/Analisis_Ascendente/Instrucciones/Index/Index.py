from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

class Index(Instruccion):
    def __init__(self, caso, id1, id2, listaId, concatena,fila, columna):
        self.caso = caso
        self.id1 = id1
        self.id2 = id2
        self.listaId = listaId
        self.concatena = concatena
        self.fila = fila
        self.columna = columna

    def ejecutar(index, ts, consola, exceptions):


        if ts.validar_sim(index.id1) == -1:
            if index.caso == 1:
                concatena = []
                for data in index.listaId:
                    concatena.append(data.id)
                simbolo = TS.Simbolo(TS.TIPO_DATO.INDEX, index.id1, "SIMPLE INDEX"+":"+index.id2, concatena, None)
                ts.agregar_sim(simbolo)
                consola.append(f"\nIndex {index.id1} creado exitosamente")
            elif index.caso == 2:
                concatena = []
                for data in index.listaId:
                    concatena.append(data.id)
                simbolo = TS.Simbolo(TS.TIPO_DATO.INDEX, index.id1, "USING HASH"+":"+index.id2, concatena, None)
                ts.agregar_sim(simbolo)
                consola.append(f"\nIndex {index.id1} creado exitosamente")
            elif index.caso == 3:
                concatena = []
                for data in index.listaId:
                    concatena.append(data.id)
                simbolo = TS.Simbolo(TS.TIPO_DATO.INDEX, index.id1, "UNIQUE"+":"+index.id2, concatena, None)
                ts.agregar_sim(simbolo)
                consola.append(f"\nIndex {index.id1} creado exitosamente")

            elif index.caso == 4:
                concatena = []
                for data in index.listaId:
                    concatena.append(data.id)
                simbolo = TS.Simbolo(TS.TIPO_DATO.INDEX, index.id1, "NULLS"+":"+index.id2, concatena, None)
                ts.agregar_sim(simbolo)
                consola.append(f"\nIndex {index.id1} creado exitosamente")
            elif index.caso == 5:
                concatena = []
                for data in index.listaId:
                    concatena.append(data.id)
                simbolo = TS.Simbolo(TS.TIPO_DATO.INDEX, index.id1, "NULLS"+":"+index.id2, concatena,  None)
                ts.agregar_sim(simbolo)
                consola.append(f"\nIndex {index.id1} creado exitosamente")
        else:
            consola.append(f"\nYa existe el indice {index.id1} ")
            exceptions.append(f"Error Semantico-fdw_invalid_option_index-HV00C-{index.fila},{index.columna}")

    def traducir(index, consola, tv):
        #iniciar traduccion
        info = "" #info contiene toda el string a mandar como parametros
        print("concatena \n")
        print(index.concatena)
        for data in index.concatena:
            info += " " +data

        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{info};\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")
