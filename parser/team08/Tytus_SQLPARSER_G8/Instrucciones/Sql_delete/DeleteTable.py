from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *

class DeleteTable(Instruccion):
    def __init__(self, valor, tipo, insWhere, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor
        self.insWhere = insWhere

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(self.valor != None):
            if(self.insWhere != None):
                #delete(database: str, table: str, columns: list)
                
                #primero vamos a extraer la tabla
                if(arbol.getBaseDatos()!= None):
                    #resE = extractTable(arbol.getBaseDatos(),self.valor) 
                    print("Entro al delete")
                else:
                    #error no hay base de datos
                    print("error")
'''
instruccion = DeleteTable("hola mundo",None, 1,2)

                    # countries tabla
                    # id columnas
                    # nombre columnas
                    if(resE == )
                    where = self.insWhere.ejecutar(tabla,arbol)
                    val = devolverOrden(where.nombre) # devolveria el orden 1
                    lista = [val+ ":" + where.expDer] # [1 = 10] [2 = "kathy"]
                    delete(arbol.getBaseDatos(),self.valor,lista)
                    
instruccion.ejecutar(None,None)
'''