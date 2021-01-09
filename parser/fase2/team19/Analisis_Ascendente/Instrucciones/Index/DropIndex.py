from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes

class DropIndex(Instruccion):

    def __init__(self, id ,fila, columna):
        self.id = id
        self.fila = fila
        self.columna = columna

    def ejecutar(dropObject, ts, consola, exceptions):
        bdactual = ts.buscar_sim("usedatabase1234")
        # se busca el simbolo y por lo tanto se pide el entorno de la bd
        BD = ts.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno

        if entornoBD.validar_sim(dropObject.id) == 1:

            entornoBD.eliminar_sim(dropObject.id)

            consola.append(f"Index {dropObject.id}, eliminada exitosamente")

        else:

            consola.append(f"42P01	undefined_index, no existe el index {dropObject.id}")
            exceptions.append(
                f"Error semantico-42P01- 42P01	undefined_Index, no existe el index {dropObject.id}-fila-columna")

    def getC3D(self, lista_optimizaciones_C3D):

        etiqueta = GeneradorTemporales.nuevo_temporal()
        instruccion_quemada = 'drop index '
        instruccion_quemada += '%s ' % self.id
        instruccion_quemada += ';'
        c3d = '''
    # ---------Drop Index-----------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s

    ''' % (etiqueta, instruccion_quemada, etiqueta)

        '''optimizacion1 = Reportes.ListaOptimizacion("c3d original", "c3d que entra", Reportes.TipoOptimizacion.REGLA1)
        lista_optimizaciones_C3D.append(optimizacion1)'''

        return c3d