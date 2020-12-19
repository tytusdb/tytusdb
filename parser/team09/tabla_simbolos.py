from enum import Enum
import Errores as E

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

class t_constraint(Enum):
    NOT_NULL    = 1,
    NULL        = 2,
    UNIQUE      = 3,
    DEFOULT     = 4,
    CHECK       = 5

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
    
    #agregar simbolos: bases, tablas, columnas y constraints

    def agregar_simbolo(self, new_simbolo):  #agrega tablas y bases de datoos
        self.lis_simbolos.append(new_simbolo)


    def agregar_columna(self,table, db,columna): 
        # agrega un simbolo columna a un simbolo tabla en la lista de valores de la misma
        database = self.get_simbol(db)
        if(isinstance(database,E.Errores)):
            return database #la base de datos no existe en la ts, database ya trae el error
        tabla = self.get_table(db,table)
        if isinstance(tabla,E.Errores):
            return tabla #la tabla no existe en la ts, table ya trae el error
        else:
            #validar que no exista una columna con el mismo nombre
            for columna  in tabla.valor:
                if columna.id == columna:
                    msj_error = 'La columna -'+columna+' ya existe en la tabla -'+tabla+'-.'
                    error = E.Errores('EROOR', msj_error)
                    return error
            tabla.valor.append(columna)
            return columna

    def add_const(self,db,tabla,colum, ob_const):
        validar_columna = self.get_column(db,tabla,colum)
        if(isinstance(validar_columna),E.Errores):
            return validar_columna # el error lo trae el metodo 
        else:
            #validar que el nombre del constrint 
            for const in validar_columna.valor:
                if const.id == ob_const.id:
                    msj_error = 'El constraint -'+ob_const.id+' ya existe en la columna -'+colum+'-.'
                    error = E.Errores('EROOR', msj_error)
                    return error
            #se agrega el constraint a la lista de la columna 
            validar_columna.valor.append(ob_const)
            return ob_const

    #gets_simbols
    def get_simbol(self,id): #devuelve los simbolos 
        for simbolo in self.lis_simbolos:
            if simbolo.id == id:
                return simbolo
        #no encuentra la base, retorna error
        msj_error = 'la base de datos -'+id+'- no existe.'
        error = E.Errores('ERROR', msj_error)
        return error

    def get_table(self,db,id_tabla):
        for Simbolo in self.lis_simbolos:
            if Simbolo.id == id_tabla:
                if Simbolo.base == db:
                    return Simbolo
                else: #la tabla no pertenece a esa base
                    msj_error = 'la tabla -'+id_tabla+'- no se encuentra en la base de datos -'+db+'-.'
                    error = E.Errores('EROOR', msj_error)
                    return error
        #No se encontro la tabla
        msj_error = 'La tabla -'+id_tabla+' no existe.'
        error = E.Errores('EROOR', msj_error)
        return error


    def get_column(self,db,table,id_column):
        tabla= self.get_table(db,table)
        if( not isinstance(tabla,E.Errores)):
            for columna in tabla.valor:
                if columna.id == id_column:
                    return columna
            #no existe la columna en esa tabla
            msj_error = 'La columna -'+id_column+' no existe en la tabla -',tabla,'-.'
            error = E.Errores('EROOR', msj_error)
            return error
        else: # la tabla no existe, la variable tabla tare el error 
            return tabla


    def get_constraint(self,db,table,column,id_const):
        columna = self.get_column(db,table,column)
        if(isinstance(columna,E.Errores)):
            #la variable columna trae el error, si la db, la tabla o la columna no existe
            return columna
        
        #buscar el constrint por id 
        for const in columna.valor:
            if const.id == id_const:
                return const
        
        #no se encontro el constraint
        msj_error = 'No se encontro el constrint -'+id_const+'-.'
        
    def get_databases(self):
        databases = []
        for simbolo in self.lis_simbolos:
            if simbolo.tipo == tipo_simbolo.DATABASE:
                databases.append(simbolo)
        return databases
    
    #funciones para borrar simbolos
    def drop_db(self,db):
        #verificar que exista la db
        database = self.get_simbol(db)
        if(isinstance(database,E.Errores)): #la base no existe
            return database
        
        #si existe eliminamos el simbolo base de datos
        self.lis_simbolos.remove(database)
        return True

        #eliminar todas las tablas que perteneces a esa base de datos
        for Sim in self.lis_simbolos:
            if Sim.tipo == tipo_simbolo.TABLE and Sim.base == db :
                self.lis_simbolos.remove(Sim)


    def graficar(self):
        for simbolos in self.lis_simbolos:
            print(simbolos.id)


class const():
    #esta clase servira para almacenar los constraints de las columnas de las tablas
    def __init__(self,id,valor,condicion,tipo):
        self.id = id
        self.tipo = tipo #el tipo sera un valor en el enum
        self.valor = valor
        self.condicion = condicion # <,>,>=,<=,=,<>, 
    
    def get_condicion(self):
        return self.condicion

    def get_valor(self):
        return self.valor

    