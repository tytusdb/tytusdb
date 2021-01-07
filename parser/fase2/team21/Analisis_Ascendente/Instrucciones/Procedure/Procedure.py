from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import tytus.parser.fase2.team21.Analisis_Ascendente.ascendente as tr

#from tytus.parser.team21.Analisis_Ascendente.ascendente import procesar_instrucciones


class Procedure(Instruccion):
    '''en replace sube True o False
    parametros puede ser None'''
    def __init__(self, caso, replace, id, parametros, languageE, asE, inst, id2, declareInst, beginInst, linea, columna):
        self.caso = caso
        self.replace = replace
        self.id = id
        self.parametros = parametros
        self.languageE = languageE
        self.asE = asE
        self.inst = inst
        self.id2 = id2
        self.declareInst = declareInst
        self.beginInst = beginInst
        self.linea = linea
        self.columna = columna

    def ejecutar(procedure, ts, consola, exceptions):

        #tr.procesar_instrucciones(procedure.beginInst,ts)

        print("mm->")



        print("mm->")



    def traducir(proc, ts, consola, exceptions, tv, concatena):
        consola.append("\n@with_goto  # Decorador necesario.\n")
        consola.append(f"def {proc.id}(")
        params = ""
        if proc.parametros != None and len(proc.parametros) != 0:
            if len(proc.parametros) == 1:
                if proc.parametros[0] != None:
                    # tiene parametros
                    for param in proc.parametros:
                        params += param.id
            else:
                # no tiene parametros
                print(proc.parametros)
                i = 0
                for param in proc.parametros:
                    params += param.id
                    if i + 1 != len(proc.parametros):
                        params += ', '
                    i = i + 1

        consola.append(f"{params}):\n")
        if proc.inst != None:
            tr.traduccion(proc.inst, ts, consola, consola, exceptions, concatena, tv)

        if proc.declareInst != None:
            consola.append("\tlabel .declare\n")
            tr.traduccion(proc.declareInst, ts, consola, consola, exceptions, concatena, tv)
        if proc.beginInst != None:
            consola.append("\tlabel .begin\n")
            tr.traduccion(proc.beginInst, ts, consola, consola, exceptions, concatena, tv)