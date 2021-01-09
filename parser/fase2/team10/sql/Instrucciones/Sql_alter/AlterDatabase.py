from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from sql.Instrucciones.Excepcion import Excepcion
from sql.storageManager.jsonMode import *


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

'''
instruccion = AlterDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''