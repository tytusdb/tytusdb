from storageManager.jsonMode import *
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.TablaSimbolos.Tipo import Tipo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tabla import Tabla

class AlterIndex(Instruccion):
    def __init__(self,num,nombre,tipo,col,opcion,rest,linea,columna):
        Instruccion.__init__(self,tipo,nombre,linea,columna)
        self.num = num
        self.nombre = nombre
        self.tipo = tipo
        self.col = col
        self.opcion = opcion
        self.rest = rest
        self.linea = linea 
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(self.num == 1):
            #arbol.consola.append("SE EJECUTO ALTER  INDEX TIPO: "+ str(self.tipo))
            arbol.setIndex([self.nombre,self.tipo,self.col,self.opcion,self.rest,self.linea]) 
                       
    def getCodigo(self, tabla, arbol):
        if(self.num == 1):
            #arbol.consola.append("SE EJECUTO ALTER  INDEX TIPO: "+ str(self.tipo))
            arbol.setIndex([self.nombre,self.tipo,self.col,self.opcion,self.rest,self.linea]) 