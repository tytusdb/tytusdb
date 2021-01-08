from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes

class AlterIndex(Instruccion):

    def __init__(self,caso, ifIndice,id , columnas ,noCol, fila, columna):
        self.caso = caso
        self.ifIndice = ifIndice
        self.id = id
        self.columnas = columnas
        self.noCol = noCol
        self.fila = fila
        self.columna = columna

    def ejecutar(AlterIndex, ts, consola, exceptions):

        try:
            if AlterIndex.caso == 1:
                bdactual = ts.buscar_sim("usedatabase1234")
                # se busca el simbolo y por lo tanto se pide el entorno de la bd
                BD = ts.buscar_sim(bdactual.valor)
                entornoBD = BD.Entorno

                if entornoBD.validar_sim(AlterIndex.id) == 1:
                    simbolo = entornoBD.buscar_sim(AlterIndex.id)
                    #print(simbolo.valor)
                    cadena = str(simbolo.valor)
                    cadena1 = cadena.replace(str(AlterIndex.noCol),str(AlterIndex.columnas))
                    nuevo = TS.Simbolo(simbolo.categoria, simbolo.id, simbolo.tipo, cadena1,simbolo.Entorno)

                    entornoBD.eliminar_sim(AlterIndex.id)
                    entornoBD.agregar_sim(nuevo)

                    consola.append(f"Index {AlterIndex.id}, actualizado exitosamente")

                else:

                    consola.append(f"42P01	undefined_index, no existe el index {AlterIndex.id}")
                    exceptions.append(
                        f"Error semantico-42P01- 42P01	undefined_Index, no existe el index {AlterIndex.id}-fila-columna")
            else:
                pass
                    # agregar alter si viene el no de columna
        except:
            consola.append("XX000 : internal_error")

    def getC3D(self, lista_optimizaciones_C3D):

        etiqueta = GeneradorTemporales.nuevo_temporal()
        instruccion_quemada = 'Alter index '
        instruccion_quemada += '%s ' % self.id
        instruccion_quemada += 'ALTER COLUMN '
        instruccion_quemada += '%s ' % self.columna + ' '
        instruccion_quemada += '%s ' % self.noCol + ';'
        c3d = '''
    # ---------Alter Index-----------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s

    ''' % (etiqueta, instruccion_quemada, etiqueta)

        '''optimizacion1 = Reportes.ListaOptimizacion("c3d original", "c3d que entra", Reportes.TipoOptimizacion.REGLA1)
        lista_optimizaciones_C3D.append(optimizacion1)'''

        return c3d