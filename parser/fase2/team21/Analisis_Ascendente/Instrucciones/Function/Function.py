from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import tytus.parser.fase2.team21.Analisis_Ascendente.ascendente as tr
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS

class Function(Instruccion):
    #replace sube True o False
    #parametros puede ser None
    def __init__(self, caso, replace, id, parametros, tipo, E, declareInst, beginInst, linea, columna):
        self.caso = caso
        self.replace = replace
        self.id = id
        self.parametros = parametros
        self.tipo = tipo
        self.E = E
        self.declareInst = declareInst
        self.beginInst = beginInst
        self.linea = linea
        self.columna = columna


    def traducir(func, ts, consola, exceptions, tv, concatena):
        consola.append("\n@with_goto  # Decorador necesario.\n")
        consola.append(f"def {func.id}(")
        params = ""
        if func.parametros != None and len(func.parametros) != 0:
            if len(func.parametros) == 1:
                if func.parametros[0] != None:
                    #tiene parametros
                    for param in func.parametros:
                        params += param.id
            else:
                #no tiene parametros
                print(func.parametros)
                i = 0
                for param in func.parametros:
                    params += param.id
                    if i + 1 != len(func.parametros):
                        params += ', '
                    i = i + 1

        consola.append(f"{params}):\n")
        if func.declareInst != None:
            consola.append("\tlabel .declare\n")
            tr.traduccion(func.declareInst, ts, consola, consola, exceptions, concatena, tv)
        if func.beginInst != None:
            consola.append("\tlabel .begin\n")
            tr.traduccion(func.beginInst, ts, consola, consola, exceptions, concatena, tv)


    def ejecutar (func,ts):

        entorno = {}
        nuevo = TS.Simbolo(TS.TIPO_DATO.FUNCION,"nombrefuncion","",func,entorno)
        ts.agregar_sim(nuevo)