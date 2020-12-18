from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
class UpdateTable(Instruccion):
    def __init__(self, id, tipo, lCol, insWhere, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.identificador = id
        self.listaDeColumnas = lCol
        self.insWhere = insWhere

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("UPDATE_SET_TABLA")
        if(self.identificador != None):
            if(self.listaDeColumnas != None):
                if(self.insWhere != None):
                    update(arbol.database())
        '''
        def update(database: str, table: str, register: dict, columns: list) -> int:
            '''


'''
instruccion = UpdateTable("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)
'''