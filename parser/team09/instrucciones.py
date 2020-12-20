import tabla_simbolos as TS
import Errores as E

#Creación de la tabla de simbolos
ts_global = TS.tabla_simbolos()

'''
def drop_db(nombre, x, ts): # x es variable para saber si viene 'if exists' x = 0 -> no viene x = 1 -> si viene
    if x == 0:                              
        db = ts_global.get_simbol(nombre)                   #Va a buscar si la base de datos existe
        if isinstance(db, ):            					#Revisa si el tipo de db es igual a DATABASE
            ts_global.dropdb(nombre)                        #Si es igual DATABASE llama al método para eliminarla de la tabla de simbolos
        else:
            print('La base de datos no existe')             #
            break
    else:
        db = ts_global.get_simbol(nombre)                   #Va a buscar si la base de datos existe
        if db.tipo == 'DATABASE' :
            ts.dropdb()
        else:
            print('La base de datos no existe')
'''

def create_table(db, nombre, columnas, ts):
    nueva_tabla = TS.Simbolo(nombre, TS.tipo_simbolo.TABLE, None, db, None, None, None, None)
    x = columnas.split(",")
    for i in x:
        c = i.split(":")
        print('El nombre es -> ' + c[0] + ' y el tipo es -> ' + c[1])
        #create_column(db, nombre, c[0], c[1], ts)
    ts.agregar_simbolo(nueva_tabla)
    return ts

def create_column(db, tabla, columna, tipo, ts):
    nueva_columna = TS.Simbolo(columna,TS.tipo_simbolo.INTEGER,None,db,0,True,False,None)
    agregar = ts.agregar_columna(tabla, db, nueva_columna)