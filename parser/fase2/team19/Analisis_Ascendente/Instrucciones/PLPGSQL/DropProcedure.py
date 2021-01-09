from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes

class DropProcedure(Instruccion):

    def __init__(self, id ,fila, columna):
        self.id = id
        self.fila = fila
        self.columna = columna

    def ejecutar(dropObject, ts, consola, exceptions):
        bdactual = ts.buscar_sim("usedatabase1234")
        # se busca el simbolo y por lo tanto se pide el entorno de la bd
        BD = ts.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno
        try:
            if entornoBD.validar_sim(dropObject.id) == 1:

                entornoBD.eliminar_sim(dropObject.id)

                consola.append(f"Procedure {dropObject.id}, eliminado exitosamente")

            else:

                consola.append(f"42P01	undefined_procedure, no existe {dropObject.id}")
                exceptions.append(
                    f"Error semantico-42P01- 42P01	undefined_procedure, no existe {dropObject.id}-fila-columna")
        except:
            consola.append("XX000 : internal_error")

    def getC3D(self, lista_optimizaciones_C3D):

        etiqueta = GeneradorTemporales.nuevo_temporal()
        temporal2 = GeneradorTemporales.nuevo_temporal()
        instruccion_quemada = 'drop procedure '
        instruccion_quemada += '%s ' % self.id
        instruccion_quemada += '();'
        c3d = '''
    # ---------Drop Procedure-----------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s
    try:
        del %s
    except:
        %s = "No existe para eliminar el stored procedure %s"
        salida = salida + %s
        salida = salida + '\\n'
    ''' % (etiqueta, instruccion_quemada, etiqueta, self.id, temporal2, self.id, temporal2)

        '''optimizacion1 = Reportes.ListaOptimizacion("c3d original", "c3d que entra", Reportes.TipoOptimizacion.REGLA1)
        lista_optimizaciones_C3D.append(optimizacion1)'''

        return c3d