import tabla_simbolos as TS
import Errores as E

base_actual = None

class Instruccion():
    def __init__(self, tipo, instruccion):
        self.tipo = tipo 
        self.instruccion = instruccion

class Select():
    def __init__(self, dist, selcol, fromcol, joins, order, conditions):
        self.dist = dist
        self.selcol = selcol
        self.fromcol = fromcol
        self.joins = joins
        self.order = order
        self.conditions = conditions

    def execute():
        #Llamar metodo que realizara el select
        print('ejecutando select')

class AlterTable():
    def __init__(self, id, cols, constrain, fkey, ref):
        self.id = id
        self.cols = cols
        self.constrain = constrain
        self.fkey = fkey
        self.ref = ref

    def execute(self):
        print('ejecutando alter table')
        print('id : ' + str(self.id))
        print('cols : ' + str(self.cols))
        print('constrain : ' + str(self.constrain))
        print('foreing keys :' + str(self.fkey))
        print('references : ' + str(self.ref))

class CreateDB():
    def __init__(self, replace, ifnot, id, owner, mode):    # boolean, boolean, string, string, integer
        self.replace = replace                              # si existe, la reemplaza/modifica
        self.ifnot = ifnot                                  # si existe, no la crea
        self.id = id                                        # nombre de la base de datos
        self.owner = owner                                  # nombre/id del creador
        self.mode = mode                                    # modo de almacenamiento

    def execute(self, ts_global):
        print('----> EJECUTAR CREATE DATABASE')
        nueva_base = TS.Simbolo(self.id, TS.tipo_simbolo.DATABASE, None, None, None, None, None, None)
        existe = False                                      # bandera para comprobar si existe
        bases = ts_global.get_databases()                   # obtiene todas las bases de datos
        for base in bases:                                  # recorro la lista de bases de datos
            if base.id == self.id:                          # y verifico si existe
                existe = True                               # si existe, cambio el valor de la bandera
                break                                       # y salgo de la comprobación
        if not self.ifnot:                                  # si no viene "IF NOT EXISTS", se crea/reemplaza
            if self.replace:                                # si viene "OR REPLACE"
                if existe:                                  # si existe la base de datos
                    ts_global.drop_db(self.id)              # se elimina, luego
                ts_global.agregar_simbolo(nueva_base)       # se agrega el nuevo símbolo
            else:                                           # si no viene "OR REPLACE"
                if existe:                                  # si existe, es un error
                    nuevo_error = E.Errores('Semántico.', 'Ya existe una base de datos con el nombre \'' + self.id + '\'.')
                    #ls_error.append(nuevo_error)            #se agrega el error a la lista
                else:                                       # si no existe
                    ts_global.agregar_simbolo(nueva_base)   # se agrega el nuevo símbolo
        else:                                               # si sí viene "IF NOT EXISTS"
            if self.replace:                                # si viene "OR REPLACE", es error
                nuevo_error = E.Errores('Semántico.', 'No pueden venir conjuntamente las cláusulas \'OR REPLACE\' e \'IF NOT EXISTS\'.')
                #ls_error.append(nuevo_error)                #se agrega el error a la lista
            else:                                           # si no viene "OR REPLACE"
                if not existe:                              # si no existe la base de datos
                    ts_global.agregar_simbolo(nueva_base)   # se agrega el nuevo símbolo, de lo contrario no se hace nada

class UseDB():
    def __init__(self, id):                                 # string
        self.id = id                                        # nombre de la base de datos

    def execute(self, ts_global):
        print('----> EJECUTAR USE')
        bases = ts_global.get_databases()                   # obtiene todas las bases de datos
        for base in bases:                                  # verifico si existe:
            if base.id == self.id:                          # si sí existe, retorno el id
                ts_global.agregar_simbolo((TS.Simbolo(base.id,TS.tipo_simbolo.DB_ACTUAL,None,None,None,None,None,None))) #se agrega el simbolo db_actual
                return self.id                              # si no, es error
        new_error = E.Errores('Semántico.', 'La base de datos \'' + self.id + '\' no existe.')
        print('******************************')
        #ls_error.append(new_error)                          #se agrega el error a la lista
        return None                                         # y retorno None

class ShowDB():
    def __init__(self):
        print('show')

    def execute(self, ts_global):
        bases = ts_global.get_databases()                   # obtiene todas las bases de datos
        if len(bases) == 0:                                 # si no hay bases de datos
            return '\n\tNo hay bases de datos creadas.\n'   # se retorna un mensaje
        respuesta = '\n'                                    # de lo contrario,
        for base in bases:                                  # recorre la lista,
            respuesta = respuesta + '\t' + base.id + '\n'   # se concatenan los nombres
        return respuesta + '\n'                             # y los retorna

class Drop():
    def __init__(self, id):
        self.id = id

    def execute(self):
        print('Ejecutando Drop')
        print('id : ' + self.id)

class CreateTable():
    def __init__(self, id, base, cols, inh,cont_key):
        self.id = id
        self.base = base
        self.cols = cols
        self.inh = inh
        self.cont_key = cont_key
        
    def execute(self,ts):
        print('----> EJECUTAR CREATE TABLE * '+str(self.id))
        self.base = ts.get_dbActual().id
        if(isinstance(self.base,E.Errores)):
            #no hay base Activa
            print('***************************error - no hay base activa********************')
            return
        #creamos la tabla
        new_tabla = TS.Simbolo(self.id,TS.tipo_simbolo.TABLE,None,self.base,None,None,None,None)
        #insertamos la tabla a la ts
        verificar_tabla=ts.agregar_tabla(str(self.base), new_tabla)
        if(isinstance(verificar_tabla,E.Errores)):
            print('***************************error********************')
        else:
            print('se agrego')
        #agregamos las columnas a la tabla
        for columna in self.cols:
            columna.base = self.base
            print(columna.id +' - '+ str(columna.tipo))
            for const in columna.valor:
                if(const.tipo == TS.t_constraint.PRIMARY):
                    columna.pk = True
                    columna.valor.remove(const)
                elif (const.tipo == TS.t_constraint.FOREIGN):
                    columna.fk = True
                    columna.referencia = str(const.id)+','+str(const.valor)
                    columna.valor.remove(const)

                if columna.longitud == None:
                    columna.longitud =0
            
            ts.agregar_columna(self.id,self.base,columna)


class Insert():
    def __init__(self, id, vals):
        print('init')
        self.id = id
        self.vals = vals

    def execute(self):
        print('Ejecutando Insert')
        print('id : ' + str(self.id))
        for val in self.vals:
            print('value : ' + str(val))

class Delete():
    def __init__(self, id, cond):
        self.id = id
        self.cond = cond

    def execute(self):
        print('Ejecutando Delete')
        print('id : ' + str(self.id))

class Update():
    def __init__(self, id, vals):
        self.id = id
        self.vals = vals

    def execute(self):
        print('Ejecutando Update')
        print('id : ' + str(id))

'''
import tabla_simbolos as TS
import Errores as E
#Creación de la tabla de simbolos
ts_global = TS.tabla_simbolos()
#Creación de lista de errores
ls_error = []
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
'''