from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes

class Parametro():
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

class CreateProcedure(Instruccion):

    def __init__(self, id, parametros,declare,sentencias, fila, columna):
        self.id = id
        self.parametros = parametros
        self.declare = declare
        self.sentencias = sentencias
        self.fila = fila
        self.columna = columna

    def ejecutar(self, ts, consola, exceptions):
        bdactual = ts.buscar_sim("usedatabase1234")
        BD = ts.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno


        if self.parametros == None:
            if entornoBD.validar_sim(self.id) == -1:
                entornoP = TS.TablaDeSimbolos({})

                if self.declare != None:

                    simdeclare = TS.Simbolo(TS.TIPO_DATO.DECLARE, "DECLARE", None, self.declare, None)
                    entornoP.agregar_sim(simdeclare)

                print(self.sentencias)
                simbegin = TS.Simbolo(TS.TIPO_DATO.BEGIN, "BEGIN", None, self.sentencias, None)
                entornoP.agregar_sim(simbegin)

                nuevoP = TS.Simbolo(TS.TIPO_DATO.PROCEDURE, self.id, None, None, entornoP)
                entornoBD.agregar_sim(nuevoP)
                consola.append(f"Se añadio un nuevo procedimiento : {self.id}")

        else:
            paramcorrectos = True
            if entornoBD.validar_sim(self.id) == -1:
                dicci = {}
                for parametro in self.parametros:
                    existe = dicci.get(parametro.id, False)
                    if existe == False:
                        dicci[parametro.id] = parametro.tipo.tipo
                    else:
                        consola.append(
                            f"Existe parametros con el mismo nombre en la función: {self.id}\n No se pudo crear la función.")
                        paramcorrectos = False
                        break
                if paramcorrectos:
                    entornoP = TS.TablaDeSimbolos({})
                    if self.declare != None:
                        simdeclare = TS.Simbolo(TS.TIPO_DATO.DECLARE, "DECLARE", None, self.declare, None)
                        entornoP.agregar_sim(simdeclare)
                    simbegin = TS.Simbolo(TS.TIPO_DATO.BEGIN, "BEGIN", None, self.sentencias, None)
                    entornoP.agregar_sim(simbegin)
                    for clave, valor in dicci.items():  # id,tipo
                        nuevaVariable = TS.Simbolo(TS.TIPO_DATO.PARAMETRO, clave, valor, None, None)
                        entornoP.agregar_sim(nuevaVariable)

                    nuevoP = TS.Simbolo(TS.TIPO_DATO.PROCEDURE, self.id, None, None,
                                              entornoP)
                    entornoBD.agregar_sim(nuevoP)
                    consola.append(f"Se añadio una nuevo procedimiento : {self.id}")
            else:
                consola.append(f"Ya existe el procedimiento ")


