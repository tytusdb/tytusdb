from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
import C3D.GeneradorTemporales as GeneradorTemporales

class DropFunction(Instruccion):
    def __init__(self,id):
        self.id = id


    def ejecutar(DropFunction,ts,consola,exception):
        bdactual = ts.buscar_sim("usedatabase1234")
        BD = ts.buscar_sim(bdactual.valor)
        entornoBD = BD.Entorno
        try:
            if entornoBD.validar_sim(DropFunction.id) == 1:     #verificamos si existe la función en la bd
                entornoBD.eliminar_sim(DropFunction.id)
                consola.append(f"Se elimino la funcion {DropFunction.id} exitosamente")
            else:
                consola.append(f" No existe la función {DropFunction.id} para eliminar")
        except:
            consola.append("XX000 : internal_error")

    def getC3D(self, lista_optimizaciones_C3D):
        temporal = GeneradorTemporales.nuevo_temporal()
        c3d = '''
    # ----------DROP FUNCTION-----------
    top_stack = top_stack + 1
    %s = "drop function %s ;"  
    stack[top_stack] = %s
''' % (temporal, self.id, temporal)
        return c3d