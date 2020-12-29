from enum import Enum

class TIPO(Enum) :
    DATABASE = 1
    TABLE = 2
    COLUMN = 3
    SMALLINT = 4
    INTEGER = 5
    BIGINT = 6
    DECIMAL = 7
    NUMERIC = 8
    REAL = 9
    DOUBLE_PRECISION = 10
    CHARACTER_VARYING = 11
    VARCHAR = 12
    CHARACTER = 13
    CHAR = 14
    TEXT = 15
    TIMESTAMP = 16
    DATE = 17
    TIME = 18
    INTERVAL = 19
    BOOLEAN = 20
    

class Simbolo() :
    
    def __init__(self, id, tipo, valor ,ambito,indice) :
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.ambito =  ambito
        self.indice = indice

class Tabla() :
    
    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        if not id in self.simbolos :
            print('Error: variable ', id, ' no definida.')

        return self.simbolos[id]

    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos :
            print('Error: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id] = simbolo

    def getTabla(self,nombre):
        for simbolo in self.simbolos.values():
            if simbolo.valor ==nombre:
                #Verificar si es tabla
                #results = []
                if simbolo.tipo == TIPO.COLUMN:
                    ambito = simbolo.ambito
                    tablaaa = self.simbolos[ambito]
                    # El nombre de la tabla es
                    tabla = tablaaa.valor
                    # La base de datos es 
                    dbambito = tablaaa.ambito
                    #DB
                    dbb = self.simbolos[dbambito]
                    db = dbb.valor
                    return tabla , db

        return None

    def getColumns(self,db,table):
        #Buscamos el ambito de la DB
        iddb = -1
        for simbolo in self.simbolos.values():  
            
            if simbolo.valor == db and simbolo.tipo == TIPO.DATABASE : 
                iddb = simbolo.id
        #Buscamos el ambito de la tabla        
        idtable = -1
        for simbolo in self.simbolos.values():
            if simbolo.valor == table and simbolo.tipo == TIPO.TABLE and simbolo.ambito == iddb : 
                idtable = simbolo.id
        columns = []        
        for simbolo in self.simbolos.values() :
            if simbolo.tipo == TIPO.COLUMN and simbolo.ambito == idtable:
                columns.append(simbolo.valor)
        return columns        


    def getIndice(self,db,table,col):

        #Buscamos el ambito de la DB
        iddb = -1
        for simbolo in self.simbolos.values():  
            
            if simbolo.valor == db and simbolo.tipo == TIPO.DATABASE : 
                iddb = simbolo.id
        #Buscamos el ambito de la Tabla
        
        idtable = -1
        for simbolo in self.simbolos.values():
            if simbolo.valor == table and simbolo.tipo == TIPO.TABLE and simbolo.ambito == iddb : 
                idtable = simbolo.id

        #Buscamos el indice de la columna
        idcol = -1
        for simbolo in self.simbolos.values():
            if simbolo.valor == col and simbolo.tipo == TIPO.COLUMN and simbolo.ambito == idtable : 
                idcol = simbolo.indice
                return idcol
        return idcol
        
        



                    