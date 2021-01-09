from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes
from Analisis_Ascendente.Instrucciones.PLPGSQL.Ifpl import *
from Analisis_Ascendente.Instrucciones.expresion import Primitivo
from Analisis_Ascendente.Instrucciones.Time import Time

class plCall(Instruccion):

    def __init__(self, id, parametros,fila, columna):
        self.id = id
        self.parametros = parametros
        self.fila = fila
        self.columna = columna

    def ejecutar(plCall, ts, consola, exceptions):
        try:
            bdactual = ts.buscar_sim("usedatabase1234")
            # se busca el simbolo y por lo tanto se pide el entorno de la bd
            BD = ts.buscar_sim(bdactual.valor)
            entornoBD = BD.Entorno

            if entornoBD.validar_sim(plCall.id) == 1:
                simboloP = entornoBD.buscar_sim(plCall.id)

                if plCall.parametros == None:
                    #Ifpl.procesar_instrucciones(Ifpl,simboloP.valor,ts,consola,exceptions)
                    print('arreglar')
                else:
                    pass

                consola.append(f"Si se encontro el procedimiento {plCall.id}")

            else:

                consola.append(f"42P01	undefined_Procedure, no existe  {plCall.id}")
                exceptions.append(
                    f"Error semantico-42P01- 42P01	undefined_Procedure, no existe  {plCall.id}-fila-columna")
        except:
            consola.append("XX000 : internal_error")



    def getC3D(self, lista_optimizaciones_C3D):
        temporal = GeneradorTemporales.nuevo_temporal()
        parametros = ''
        if self.parametros is not None:
            for parametro in self.parametros:
                if isinstance(parametro, Primitivo):
                    if isinstance(parametro.valor, str):
                        parametro_texto = "'%s'" % parametro.valor
                    else:
                        parametro_texto = parametro.valor
                elif isinstance(parametro, Time):
                    parametro_texto = parametro.resolverTime()
                else:
                    parametro_texto = parametro
                if parametros == '':
                    parametros = parametro_texto
                else:
                    parametros += ', %s' % parametro_texto
        c3d = '''
    # --------- Execute -----------
    funcion_intermedia()
    try:
        %s(%s)
    except:
        %s = "El stored procedure %s, no existe"
        salida = salida + %s
        salida = salida + '\\n'
    ''' % (self.id, parametros, temporal, self.id, temporal)

        '''optimizacion1 = Reportes.ListaOptimizacion("c3d original", "c3d que entra", Reportes.TipoOptimizacion.REGLA1)
        lista_optimizaciones_C3D.append(optimizacion1)'''

        return c3d