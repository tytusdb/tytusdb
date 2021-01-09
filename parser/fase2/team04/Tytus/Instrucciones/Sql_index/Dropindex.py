from storageManager.jsonMode import *
from Instrucciones.Tablas.Tablas import Tablas
from Instrucciones.TablaSimbolos.Tipo import Tipo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tabla import Tabla

class DropIndex(Instruccion):
    def __init__(self,num,nombre,tipo,col,opcion,rest,linea,columna,strGram):
        Instruccion.__init__(self,tipo,linea,columna,strGram)
        self.num = num
        self.nombre = nombre
        self.tipo = tipo
        self.col = col
        self.opcion = opcion
        self.rest = rest
        self.linea = linea 
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        db = arbol.getBaseDatos()
        bandera = 0
        index = 0
        lista_index = arbol.getIndex()
        for x in range(0,len(lista_index)):
            for item in lista_index[x]:
                if item['Base'] == db:
                    if item['Nombre'] == self.col:
                            bandera = 1
                            index = x
                            break 
            if(bandera == 1):
                break                  
        if bandera == 1 :
            lista_index.pop(index)
            print(f"DROP INDEX : {self.col} SE ELIMINO CORRECTAMENTE")
        else:     
            print(f"ERROR DROP: El index no existe o es una base de datos equivocada")

    def getCodigo(self, tabla, arbol):
        db = arbol.getBaseDatos()
        bandera = 0
        index = 0
        lista_index = arbol.getIndex()
        for x in range(0,len(lista_index)):
            for item in lista_index[x]:
                if item['Base'] == db:
                    if item['Nombre'] == self.col:
                            bandera = 1
                            index = x
                            break 
            if(bandera == 1):
                break                  
        if bandera == 1 :
            lista_index.pop(index)
            print(f"DROP INDEX : {self.col} SE ELIMINO CORRECTAMENTE")
        else:     
            print(f"ERROR DROP: El index no existe o es una base de datos equivocada")
        return ""

