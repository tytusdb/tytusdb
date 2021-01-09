from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import C3D.GeneradorFileC3D as GeneradorFileC3D

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

class CreateFunction(Instruccion):
    def __init__(self,id,parametros,returns,declare,begin):
        self.id = id
        self.parametros = parametros            #[Parametro(id,tipo),...]
        self.returns = returns.tipo             #returns = Tipo(tipo,longitud,fila,columna)
        self.declare = declare
        self.begin = begin

    def ejecutar(CreateFunction,ts,consola,exceptions):
        try:
            bdactual = ts.buscar_sim("usedatabase1234")
            BD = ts.buscar_sim(bdactual.valor)
            entornoBD = BD.Entorno
            paramcorrectos = True
            if entornoBD.validar_sim(CreateFunction.id) == -1:
                dicci = {}
                if CreateFunction.parametros is not None:
                    for parametro in CreateFunction.parametros:
                        existe = dicci.get(parametro.id,False)
                        if existe == False:
                            dicci[parametro.id] = parametro.tipo.tipo
                        else:
                            consola.append(f"Existe parametros con el mismo nombre en la función: {CreateFunction.id}\n No se pudo crear la función.")
                            paramcorrectos = False
                            break
                if paramcorrectos:
                    entornoFuncion = TS.TablaDeSimbolos({})
                    if CreateFunction.declare != None:
                        simdeclare = TS.Simbolo(TS.TIPO_DATO.DECLARE, "DECLARE", None, CreateFunction.declare, None)
                        entornoFuncion.agregar_sim(simdeclare)
                    #Esto siempre se realiza
                    simbegin = TS.Simbolo(TS.TIPO_DATO.BEGIN, "BEGIN", None, CreateFunction.begin, None)
                    entornoFuncion.agregar_sim(simbegin)
                    #Agregamos las variables de parametros al entorno de la función de una vez
                    for clave,valor in dicci.items():   #id,tipo
                        nuevaVariable = TS.Simbolo(TS.TIPO_DATO.PARAMETRO,clave,valor,None,None)
                        entornoFuncion.agregar_sim(nuevaVariable)
                    #Creamos la nuevafuncion en el entorno global de la base de datos
                    nuevaFuncion = TS.Simbolo(TS.TIPO_DATO.FUNCTION,CreateFunction.id,CreateFunction.returns,None,entornoFuncion)
                    entornoBD.agregar_sim(nuevaFuncion)
                    consola.append(f"Se añadio una nueva funcion llamada: {CreateFunction.id}")
            else:
                consola.append(f"Ya existe esta función en la base de datos")

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
        returns = ''
        lista_tipo = self.returns.split('-')
        if len(lista_tipo) == 1:
            returns = self.returns
        elif len(lista_tipo) == 2:
            if lista_tipo[0] == 'CHARACTERVARYING':
                returns = 'CHARACTER VARYING ( %s )' % lista_tipo[1]
            else:
                returns = '%s ( %s )' % (lista_tipo[0], lista_tipo[1])
        else:
            returns = '%s ( %s, %s )' % (lista_tipo[0], lista_tipo[1], lista_tipo[2])

        c3d_funcion = '''
def %s ( %s ):
    pass
''' % (self.id, parametros_para_funcion)

        c3d = '''
    # ---------CREATE FUNCTION-----------
    top_stack = top_stack + 1
    %s = 'create function %s ( %s ) returns %s as $$\\n'
''' % (temporal1, self.id, parametros_para_quemados, returns)

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
        temporal3 = GeneradorTemporales.nuevo_temporal()
        sentencias_quemados = ''
        for sentencia in self.begin:
            sentencias_quemados += sentencia.get_quemado() + ';\n'
        c3d += '''    %s = \'\'\'BEGIN 
%s 
end; 
$$ language plpgsql;\\n\'\'\'
    %s = %s + %s
    stack[top_stack] = %s
''' % (temporal3, sentencias_quemados, temporal3, temporal1, temporal3, temporal3)

        GeneradorFileC3D.funciones_extra += c3d_funcion
        return c3d
