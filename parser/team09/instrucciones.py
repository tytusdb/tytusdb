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
        bases = ts_global.get_databases()                   # obtiene todas las bases de datos
        for base in bases:                                  # verifico si existe:
            if base.id == self.id:                          # si sí existe, retorno el id
                return self.id                              # si no, es error
        new_error = E.Errores('Semántico.', 'La base de datos \'' + self.id + '\' no existe.')
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
    def __init__(self, id, base, cols, inh):
        self.id = id,
        self.base = base
        self.cols = cols
        self.inh = inh
        
    def execute(self,ts):
        print('Ejecutando Creare Table')
        print('id : ' + str(self.id))
        for col in self.cols :
            print('col id : ' + str(col.id))
            print('col type : ' + str(col.tipo))


        if self.inh != None :
            print('Inherit : ' + self.inh)

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