from enum import Enum

class tipo_simbolo(Enum):
    DATABASE = 1,
    TABLE = 2,
    INTEGER = 3,
    TEXT = 4,
    SMALLINT = 5,
    BEGINT = 6,
    DECIMAL = 7,
    REAL = 8,
    D_PRECISION = 9,
    MONEY = 10,
    CHARACTER_V = 11,
    VARCHR = 12,
    CHARACTER = 13,
    CHAR = 14,
    TIMESTAMP = 15,
    DATA = 16,
    TIME = 17,
    INTERVAL = 18

class Simbolo(): 

#los tipos de los simbolos ayudan a idetificar que tipo de simbolo es
#1-base de datos , 2-tablas , 3-columnas , 4-pk , 5-fk , 6-check , 7-constraint , 8-enum de types

    def __init__(self,id, tipo, valor, base,longitud,pk,fk,referencia): 
        self.id = id
        self.tipo = tipo
        if tipo == tipo_simbolo.TABLE or tipo != tipo_simbolo.DATABASE: # si es uno inicializa la lista que contrndra los valores 
            self.valor = []
        else:
            self.valor = None
            
        self.base = base
        self.longitud = longitud
        self.pk = pk
        self.fk = fk
        self.referencia = referencia



class tabla_simbolos():
    def __init__(self, list_simbolos = []): #constructor 
        self.lis_simbolos = list_simbolos
 
    def agregar_simbolo(self, new_simbolo):  #agrega tablas y bases de datoos
        self.lis_simbolos.append(new_simbolo)

        
    #gets_simbols
    def get_simbol(self,id): #devuelve los simbolos 
        for simbolo in self.lis_simbolos:
            if simbolo.id == id:
                return simbolo
        return None

    def get_table(self,db,id_tabla):
        for Simbolo in self.lis_simbolos:
            if Simbolo.id == id_tabla:
                if Simbolo.base == db:
                    return Simbolo
        return None #no se encontro la tabla en la base de datos indicada

    def get_column(self,db,table,id_column):
        tabla= get_table(db,table)
        if(tabla != None):
            for columna in tabla.valor:
                if columna.id == id_column:
                    return columna
            return None
        else: # la tabla no existe 
            return None

    def agregar_columna(self,table, db,columna): 
        # agrega un simbolo columna a un simbolo tabla en la lista de valores de la misma
        if(get_simbol(db) == None):
            return None #la base de datos no existe en la ts
        tabla = get_simbol(tabla)
        if tabla == None:
            return None #la tabla no existe en la ts
        else:
            if tabla.base == db: #si existe la db y la tabla pero la tabla no pertenese a esa base
                tabla.valor.append(columna)
            else:
                #si existe la db y la tabla pero la tabla no pertenese a esa base
                return None

    def add_const(self,db,tabla,colum, ob_const):
        if(get_simbol(db) == None):
            return None #la base de datos no existe en la ts
        tabla = get_simbol(tabla)
        if tabla == None:
            return None #la tabla no existe en la ts
        else:
            if tabla.base == db: #si existe la db y la tabla pero la tabla no pertenese a esa base
                tabla.valor.append(ob_const)
            else:
                #si existe la db y la tabla pero la tabla no pertenese a esa base
                return None

    def graficar(self):
        for simbolos in self.lis_simbolos:
            print(simbolos.id)


class const():
    #esta clase servira para almacenar los constraints de las columnas de las tablas
    def __init__(self,id,valor,condicion):
        self.id = id
        self.valor = valor
        self.condicion = condicion # <,>,>=,<=,=,<>, 
    
    def get_condicion(self):
        return self.condicion

    def get_valor(self):
        return self.valor

    