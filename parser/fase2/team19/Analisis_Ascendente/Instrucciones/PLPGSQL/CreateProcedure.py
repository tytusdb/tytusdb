from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes
import C3D.GeneradorFileC3D as GeneradorFileC3D
import Analisis_Ascendente.Instrucciones.Insert.insert as InsertInto

class Parametro():
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

    def getC3D(self, lista_optimizaciones_C3D):
        tipo = ''
        lista_tipo = self.tipo.tipo.split('-')
        if len(lista_tipo) == 1:
            tipo = self.tipo.tipo
        elif len(lista_tipo) == 2:
            if lista_tipo[0] == 'CHARACTERVARYING':
                tipo = 'CHARACTER VARYING ( %s )' % lista_tipo[1]
            else:
                tipo = '%s ( %s )' % (lista_tipo[0], lista_tipo[1])
        else:
            tipo = '%s ( %s, %s )' % (lista_tipo[0], lista_tipo[1], lista_tipo[2])
        return '%s %s' % (self.id, tipo)

class CreateProcedure(Instruccion):

    def __init__(self, id, parametros,declare,sentencias, fila, columna):
        self.id = id
        self.parametros = parametros
        self.declare = declare
        self.sentencias = sentencias
        self.fila = fila
        self.columna = columna

    def ejecutar(self, ts, consola, exceptions):
        try:
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
        except:
            consola.append("XX000 : internal_error")

    def getC3D(self, lista_optimizaciones_C3D):
        GeneradorFileC3D.agregar_a_global_funciones_extra(self.id)
        temporal1 = GeneradorTemporales.nuevo_temporal()
        parametros_para_funcion = ''
        parametros_para_quemados = ''
        if self.parametros is not None:
            for param in self.parametros:
                parametro_id_tipo = param.getC3D(lista_optimizaciones_C3D)
                id_parametro = param.id
                if parametros_para_quemados == '':
                    parametros_para_quemados = parametro_id_tipo
                    parametros_para_funcion = id_parametro
                else:
                    parametros_para_quemados += ', %s' % parametro_id_tipo
                    parametros_para_funcion += ', %s' % id_parametro

        sentencias_funcion = ''
        for sentencia in self.sentencias:
            if isinstance(sentencia, InsertInto.InsertInto):
                sentencias_funcion += '''%s    funcion_intermedia()\n''' % sentencia.getC3D(lista_optimizaciones_C3D)
            else:
                sentencias_funcion += sentencia.getC3D(lista_optimizaciones_C3D)
        c3d_funcion = '''
def %s ( %s ):
    global stack
    global top_stack 
%s
''' % (self.id, parametros_para_funcion, sentencias_funcion)

        c3d = '''
    # ---------CREATE PROCEDURE----------
    top_stack = top_stack + 1
    %s = 'create procedure %s ( %s ) language plpgsql as $$\\n'
''' % (temporal1, self.id, parametros_para_quemados)

        if self.declare is not None:
            temporal2 = GeneradorTemporales.nuevo_temporal()
            declare_quemado = ''
            for declare in self.declare:
                if declare_quemado == '':
                    declare_quemado = 'declare %s' % declare.getC3D(lista_optimizaciones_C3D)
                else:
                    declare_quemado += ' %s' % declare.getC3D(lista_optimizaciones_C3D)
            c3d += '''    %s = '%s\\n'
    %s = %s + %s
    %s = %s
''' % (temporal2, declare_quemado, temporal2, temporal1, temporal2, temporal1, temporal2)
        sentencias_quemados = ''
        for sentencia in self.sentencias:
            sentencias_quemados += sentencia.get_quemado() + ';\n'
        temporal3 = GeneradorTemporales.nuevo_temporal()
        c3d += '''    %s = \'\'\'BEGIN 
    %s 
    end; $$\\n\'\'\'
    %s = %s + %s
    stack[top_stack] = %s
''' % (temporal3, sentencias_quemados, temporal3, temporal1, temporal3, temporal3)

        GeneradorFileC3D.funciones_extra += c3d_funcion
        return c3d

