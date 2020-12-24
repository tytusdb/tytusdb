from enum import Enum
import Errores as E

class tipo_simbolo(Enum):
    DATABASE = 1,
    TABLE = 2,
    INTEGER = 3,
    TEXT = 4,
    SMALLINT = 5,
    BIGINT = 6,
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
    INTERVAL = 18,
    NUMERIC = 19,
    DB_ACTUAL = 20,
    BOOLEAN = 21,
    DATE = 22

class t_constraint(Enum):
    NOT_NULL    = 1,
    NULL        = 2,
    UNIQUE      = 3,
    DEFOULT     = 4,
    CHECK       = 5,
    PRIMARY     = 6,
    FOREIGN     = 7

class Simbolo():

    #los tipos de los simbolos ayudan a idetificar que tipo de simbolo es
    #1-base de datos , 2-tablas , 3-columnas , 4-pk , 5-fk , 6-check , 7-constraint , 8-enum de types

    def __init__(self,id, tipo, valor, base,longitud,pk,fk,referencia): 
        self.id = id
        self.tipo = tipo
        if tipo != tipo_simbolo.DATABASE : # si es uno inicializa la lista que contrndra los valores 
            self.valor = []
        else:
            self.valor = valor
            
        self.base = base
        self.longitud = longitud
        self.pk = pk
        self.fk = fk
        self.referencia = referencia



class tabla_simbolos():
    def __init__(self, list_simbolos = []): #constructor 
        self.lis_simbolos = list_simbolos
    
    #agregar simbolos: bases, tablas, columnas y constraints

    def set_dbActual(self,id):
        db = self.get_simbol(id)
        if( isinstance(db,E.Errores)):
            return db
        
        #buscar si hay alguna activa 
        for simbolo in self.lis_simbolos:
            if simbolo.tipo == tipo_simbolo.DB_ACTUAL:
                simbolo.id = id #si encuentra una activa la reemplaza
                return simbolo
        
        #si no crea el simbolo tipo db_actual y lo retorna
        simb = Simbolo(id,tipo_simbolo.DB_ACTUAL,None,None,None,None,None,None)
        self.lis_simbolos.append(simb)
        

    def agregar_simbolo(self, new_simbolo):  #agrega tablas y bases de datoos
        self.lis_simbolos.append(new_simbolo)
        
    def agregar_tabla(self,db,tabla):
        verficar_db = self.get_simbol(db)
        if(isinstance(verficar_db,E.Errores)):
            return verficar_db #la base de datos no existe en la ts, database ya trae el error
        else:
            self.agregar_simbolo(tabla)

        return tabla

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
            for col in tabla.valor:
                if col.id == columna.id:
                    msj_error = 'La columna -'+columna.id+' ya existe en la tabla -'+tabla.id+'-.'
                    error = E.Errores('EROOR', msj_error)
                    return error
                    
            tabla.valor.append(columna)
            return columna

    def add_const(self,db,tabla,colum, ob_const):
    
        validar_columna = self.get_column(db,tabla,colum)
        if(isinstance(validar_columna,E.Errores)):
            return validar_columna
        else:
            print('columna en metodo -->> ' +validar_columna.id)
            validar_columna.valor.append(ob_const)
            return ob_const

    #gets_simbols
    def get_simbol(self,id): #devuelve los simbolos 
        for simbolo in self.lis_simbolos:
            if simbolo.id == id:
                return simbolo
        #no encuentra la base, retorna error
        msj_error = 'la base de datos -'+ str(id) + '- no existe.'
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
    
    def get_dbActual(self):
        encontrada = False
        for simbol in self.lis_simbolos:
            if simbol.tipo == tipo_simbolo.DB_ACTUAL:
                encontrada = True
                return simbol

        if encontrada == False:
            error = E.Errores('Error','no existe ninguna base de datos activa')
        
        return error

    #funciones para borrar simbolos
    def drop_db(self,db):
        #verificar que exista la db
        database = self.get_simbol(db)
        if(isinstance(database,E.Errores)): #la base no existe
            return database
        
        #si existe eliminamos el simbolo base de datos
        self.lis_simbolos.remove(database)
        #eliminar todas las tablas que perteneces a esa base de datos
        for Sim in self.lis_simbolos:
            #print('simbolo ->  ' +Sim.id)
            if Sim.base == db :
                self.lis_simbolos.remove(Sim)

        #eliminar base acutial
        db_actual = self.get_dbActual()
        try:
            if(db_actual.id == db):
                self.lis_simbolos.remove(db_actual)
        except:
            return True

        return True

    def drop_table(self,db,id_tabla):
        obtener_tabla = self.get_table(db,id_tabla)
        #verificar si encontro la tabla
        if (isinstance(obtener_tabla,E.Errores)):
            #el error viene en obrener tabla
            return obtener_tabla

        #si no se elimina de la ts
        self.lis_simbolos.remove(obtener_tabla)
        return True

    def drop_colum(self,db,table,id_columna):
        obtener_tabla = self.get_table(db,table)
        #verificar si encontro la tabla
        if (isinstance(obtener_tabla,E.Errores)):
            #el error viene en obrener tabla
            return obtener_tabla

        #buscar columna 
        for colum in obtener_tabla.valor :
            if colum.id == id_columna :
                obtener_tabla.valor.remove(colum)
                return True

        #si llega aqui no se encontro la columna 
        msj_error = 'La columna -'+id_columna+' no existe en la tabla -',table,'-.'
        error = E.Errores('EROOR', msj_error)
        return error

    def drop_const(self,db,table,id_constraint):
        obtener_tabla = self.get_table(db,table)
        if(isinstance(obtener_tabla,E.Errores)):
            #viene el errore en obtener_table
            return obtener_tabla
        #buscar el contraint en todas las tablas de la columna
        for col in obtener_tabla.valor:
            for const in col.valor:
                if(const.id == id_constraint):
                    col.valor.remove(const)
                    return True
        #no encontro el constraint 
        msj_error = 'el constrint -'+id_constraint+' no existe en la tabla -',table,'-.'
        error = E.Errores('EROOR', msj_error)
        return error

    def get_column_name(self, db,table):
        tabla = self.get_table(db,table)
        if(isinstance(tabla,E.Errores)):
            #no encontro la tabla 
            return tabla #la variable tabla ya trae el error del metodo al que llamo

        #si encuentra la tabla, recorre las columnas y las concatena a una lista
        list_columnas = []

        for columna in tabla.valor:
            list_columnas.append(columna.id)

        return list_columnas

    def get_pos_column(self, table, column):
        try:
            return table.valor.index(column)
        except:
            return -1
 
    def graficar(self):
        cont = 0
        
        f = open('Tabla_simbolos.html', 'w')
        f.write("<html>")
        f.write("<BODY style= \"background: -webkit-linear-gradient(45deg,  #ffffff, #b4b4b4);\" >")
        f.write("<div class=\"articulo\"><H3>Universidad de San Carlos de Guatemala<BR>Facultad de Ingenieria<BR>Escuela de Ciencias y Sistemas<BR>Grupo 09<BR>COMPI2<BR>TABLA DE SIMBOLOS</H3>")
        f.write("<CENTER><H2>PROYECTO 1 <BR>TABLA DE SIMBOLOS</H2></CENTER></div>")
        f.write("<table border=""1"" style=""width:100%""><tr><th>No.</th><th>ID</th><th>Tipo Simbolo</th><th>TIPO DATO</th><th>LONGITUD</th><th>VALOR</th><th>BASE</th><th>TABLA</th><th>PK</th><th>FK</th><th>REFERENCIA</th></tr>")
        for sim in self.lis_simbolos:
            cont = cont+1
            if sim.tipo == tipo_simbolo.DATABASE:
                f.write("<tr><td align=""center""><font color=""black"">" + str(cont) + "<td align=""center""><font color=""black"">" + sim.id + "<th>BASE DE DATOS</th><th>---</th><th>---</th><th>---</th><th>---</th><th>---</th><th>---</th><th>---</th><th>---</th></tr>" + '\n')
            elif sim.tipo == tipo_simbolo.TABLE:
                f.write("<tr><td align=""center""><font color=""black"">" + str(cont) + "<td align=""center""><font color=""black"">" + str(sim.id) + "<th>TABLA</th><th>---</th><th>---</th><th>---</th><th>"+str(sim.base)+"</th><th>---</th><th>---</th><th>---</th><th>---</th></tr>" + '\n')
                #imprimir columnas de la tabla
                cont = cont+1
                for col in sim.valor:
                    cont = cont+1
                    f.write("<tr><td align=""center""><font color=""black"">" + str(cont) + "<td align=""center""><font color=""black"">" + col.id + "<th>COLUMNA</th><th>"+str(col.tipo)+"</th><th>"+str(col.longitud)+"</th><th>constraints</th><th>"+col.base+"</th><th>"+sim.id+"</th><th>"+str(col.pk)+"</th><th>"+str(col.fk)+"</th><th>"+str(col.referencia)+"</th></tr>" + '\n')
                    #imprimir constrints de la columna
                    cont2 =1 
                    for constr in col.valor:
                        f.write("<tr><td align=""center""><font color=""black"">" + str(cont)+"."+str(cont2) + "<td align=""center""><font color=""black"">" + str(constr.id)+ "<th>"+str(constr.tipo)+"</th><th>"+str(constr.condicion)+"</th><th>----</th><th>"+str(constr.valor)+"</th><th>"+col.base+"</th><th>"+sim.id+"</th><th>---</th><th>---</th><th>---</th></tr>" + '\n')
            
            elif sim.tipo == tipo_simbolo.DB_ACTUAL:
                f.write("<tr><td align=""center"" bgcolor = ""yellow""><font color=""red"">" + str(cont) + "<td align=""center"" bgcolor = ""yellow""><font color=""black"">" + sim.id + "<th>BASE DE DATOS ACTIVA</th><th>---</th><th>---</th><th>---</th><th>---</th><th>---</th><th>---</th><th>---</th><th>---</th></tr>" + '\n')
            
        f.write("</table>")
        f.write("</body>")
        f.write("</html>")
        f.close()


class const():
    #esta clase servira para almacenar los constraints de las columnas de las tablas

    def __init__(self,id,valor,condicion,tipo,columna):
        self.id = id
        self.tipo = tipo #el tipo sera un valor en el enum
        self.valor = valor
        self.condicion = condicion # <,>,>=,<=,=,<>, 
        self.columna = columna

    def get_condicion(self):
        return self.condicion

    def get_valor(self):
        return self.valor

    