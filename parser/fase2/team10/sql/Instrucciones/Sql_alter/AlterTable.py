from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Excepcion import Excepcion
from sql.storageManager.jsonMode import *

class AlterTable(Instruccion):
    def __init__(self, id, tipo, tipos, opcion, id2, listaId, listaId2, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.TablaAntigua = id
        self.TablaNueva = id2
        self.tipos = tipos
        self.opcion = opcion
        self.listaId = listaId
        self.listaId = listaId2
       

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.tipos)
        if(arbol.getBaseDatos() != None):
            #aqui vamos a renombrar el alter
            alterTable(arbol.getBaseDatos(),self.TablaAntigua,self.TablaNueva)
        else:
            Excepcion(3,"Semántico","No se encuentra la base de datos",self.linea,self.columna)

'''
instruccion = AlterDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''