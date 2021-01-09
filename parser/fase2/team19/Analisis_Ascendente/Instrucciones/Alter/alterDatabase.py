#from Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
#from storageManager.jsonMode import *
from Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
from Analisis_Ascendente.Instrucciones.expresion import Primitivo
from Analisis_Ascendente.Instrucciones.Time import Time

#ALTER
class AlterDatabase(Instruccion):
    '''#1 rename
       #2 owner'''
    def __init__(self, caso, name, newName,fila,columna):
        self.caso = caso
        self.name = name
        self.newName = newName
        self.fila = fila
        self.columna = columna

    def ejecutar(alterdatabase,ts,consola,exceptions):

        #por el momemnto solo renombrar

        if ts.validar_sim(alterdatabase.name) == 1 and alterdatabase.caso == 1:

            anterior = ts.buscar_sim(alterdatabase.name)
            nuevo = TS.Simbolo(anterior.categoria,alterdatabase.newName, anterior.tipo,anterior.valor,anterior.Entorno)
            ts.agregar_sim(nuevo)
            ts.eliminar_sim(alterdatabase.name)
            alterDatabase(alterdatabase.name,alterdatabase.newName)
            consola.append(f"BD {alterdatabase.name} renombrada a {alterdatabase.newName}")
        else:

            consola.append(f"42P01	undefined_table, Error alter no existe la tabla {alterdatabase.name}")
            exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la tabla {alterdatabase.name}-fila-columna")
        #caso 1


    def getC3D(self, lista_optimizaciones_C3D):
        temporal = GeneradorTemporales.nuevo_temporal()
        codigo_quemado = "alter database %s " % self.name
        if self.caso == 1:
            codigo_quemado += 'rename to %s ;' % self.newName
        else:
            codigo_quemado += 'owner to '
            nombre = ''
            if isinstance(self.newName, Primitivo):
                nombre = self.newName.valor
            else:
                nombre = Time.resolverTime(self.newName)
            codigo_quemado += '\'%s\' ;' % nombre

        c3d = '''
    # ----------ALTER DATABASE-----------
    top_stack = top_stack + 1
    %s = "%s"
    stack[top_stack] = %s
''' % (temporal, codigo_quemado, temporal)

        return c3d
