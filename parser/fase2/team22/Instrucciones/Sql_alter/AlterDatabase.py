from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.Excepcion import Excepcion
from storageManager.jsonMode import *
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d

class AlterDatabase(Instruccion):
    def __init__(self, id, tipo, opcion, id2, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.nombreAntiguo = id
        self.nombreNuevo = id2
        self.opcion = opcion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #aqui vamos a renombrar el alter
        res = alterDatabase(self.nombreAntiguo, self.nombreNuevo)
        if( res == 1):
            Excepcion(3,"Semántico","No se pudo renombrar la base de datos",self.linea,self.columna)
        elif(res == 2):
            error = Excepcion("100","Semantico","La bd no existe.",self.linea,self.columna)
        elif(res == 3):
            error = Excepcion("100","Semantico","La bd nueva ya existe.",self.linea,self.columna)
        else:
            if(len(arbol.listaBd)==0):
                #aqui vamos a renombrar en memoria
                Instruccion = ShowDatabases(None, None, self.linea, self.columna)
                Instruccion.ejecutar(tabla,arbol)
                '''
                import os

                archivo = "/home/decodigo/Documentos/python/archivos/archivo.txt"
                nombre_nuevo = "/home/decodigo/Documentos/python/archivos/archivo_renombrado.txt"

                os.rename(archivo, nombre_nuevo)
                '''
                arbol.consola.append(f"La base de datos se cambio: {self.nombreNuevo} correctamente.")
            else:
                #aqui vamos a renombrar en memoria
                arbol.renombrarBd(self.nombreAntiguo,self.nombreNuevo)
                arbol.consola.append(f"La base de datos se cambio: {self.nombreNuevo} correctamente.")

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "ALTER DATABASE " + self.nombreAntiguo + " RENAME TO " + self.nombreNuevo + ";"))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code

    def generar3DV2(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append('h = p')
        code.append('h = h + 1')
        t0 = c3d.getTemporal()
        code.append(t0 + ' = "' + self.nombreAntiguo + '"')
        code.append('heap[h] = ' + t0)
        code.append('h = h + 1')
        t1 = c3d.getTemporal()
        code.append(t1 + ' = "' + self.opcion + '"')
        code.append('heap[h] = ' + t1)
        code.append('h = h + 1')
        t2 = c3d.getTemporal()
        code.append(t2 + ' = "' + self.nombreNuevo + '"')
        code.append('heap[h] = ' + t2)
        code.append('p = h')
        code.append('call_alter_database()')
        
        return code

'''
instruccion = AlterDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''