from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes

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
                    Expresion.ejecutarSentencias(ts,simboloP,consola,exceptions)
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

        etiqueta = GeneradorTemporales.nuevo_temporal()
        instruccion_quemada = 'Execute '
        instruccion_quemada += '%s ' % self.id + '('
        instruccion_quemada += ') ;'
        c3d = '''
    # --------- Execute -----------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s
    funcion_intermedia()

    ''' % (etiqueta, instruccion_quemada, etiqueta)

        optimizacion1 = Reportes.ListaOptimizacion("c3d original", "c3d que entra", Reportes.TipoOptimizacion.REGLA1)
        lista_optimizaciones_C3D.append(optimizacion1)

        return c3d