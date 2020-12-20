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
    def __init__(self, id, owner, mode):
        self.id = id
        self.owner = owner
        self.mode = mode

    def execute(self):
        print('Ejecutando Create DB')
        print('db id : ' + str(self.id))
        print('owner : ' + str(self.owner))
        print('mode : ' + str(self.mode))

class ShowDB():
    def __init__(self):
        print('show')

    def execute(self):
        print('Ejecutando ShowDB')

class Drop():
    def __init__(self, id):
        self.id = id

    def execute(self):
        print('Ejecutando Drop')
        print('id : ' + self.id)

class CreateTable():
    def __init__(self, id, cols, inh):
        self.id = id
        self.cols = cols
        self.inh = inh
        
    def execute(self):
        print('Ejecutando Creare Table')
        print('id : ' + str(self.id))
        aux = True
        for col in self.cols :
            if aux:
                print('col id : ' + str(col))
            else: 
                print('col type : ' + str(col))

            aux = not aux


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

class UseDB():
    def __init__(self, id):
        self.id = id

    def execute(self):
        print('Ejecutando Use DB')
        print('id : ' + self.id)

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
class CreateDB():
    def __init__ (self, replace, ifnot, iden, owner, mode): # boolean, boolean, string, string, integer
        self.replace = replace                              # si existe, la reemplaza/modifica
        self.ifnot = ifnot                                  # si existe, no la crea
        self.iden = iden                                    # nombre de la base de datos
        self.owner = owner                                  # nombre/id del creador
        self.mode = mode                                    # modo de almacenamiento
    
    def ejecutar(self):
        nueva_base = TS.Simbolo(self.iden, TS.tipo_simbolo.DATABASE, None, None, None, None, None, None)
        existe = False
        bases = ts_global.get_databases()                   # obtiene todas las bases de datos
        for base in bases:
            if base.id == self.iden:                        # verifico si existe
                existe = True
                break
        if not self.ifnot:                                  # si no viene "IF NOT EXISTS", se crea
            if self.replace:                                # si viene "OR REPLACE"
                if existe:                                  # si existe la base de datos, se elimina
                    ts_global.drop_db(self.iden)
                ts_global.agregar_simbolo(nueva_base)              # se agrega el nuevo símbolo
            else:                                           # si no viene "OR REPLACE"
                if existe:                                  # si existe, es un error
                    nuevo_error = E.Errores('Semántico.', 'Ya existe una base de datos con el nombre \'' + self.iden + '\'.')
                    #ls_error.append(nuevo_error)
                    print(nuevo_error.error)
                else:                                       # si no existe
                    ts_global.agregar_simbolo(nueva_base)          # se agrega el nuevo símbolo
        else:                                               # si viene "IF NOT EXISTS"
            if self.replace:                                # si viene "OR REPLACE", es error
                nuevo_error = E.Errores('Semántico.', 'No pueden venir conjuntamente las cláusulas \'OR REPLACE\' e \'IF NOT EXISTS\'.')
                #ls_error.append(nuevo_error)
                print(nuevo_error.error)
            else:
                if not existe:                              # si existe la base de datos, no se crea, si no
                    ts_global.agregar_simbolo(nueva_base)          # se agrega el nuevo símbolo
class UseDB():
    def __init__(self, iden):                               # string
        self.iden = iden                                    # nombre de la base de datos
    def ejecutar(self):
        bases = ts_global.get_databases()                   # obtiene todas las bases de datos
        for base in bases:
            if base.id == self.iden:                        # verifico si existe
                return self.iden
        new_error = E.Errores('Semántico.', 'La base de datos \'' + self.iden + '\' no existe.')
        #ls_error.append(new_error)
        print(new_error.error)
        return None
class ShowDB():
    def ejecutar(self):
        bases = ts_global.get_databases()                   # obtiene todas las bases de datos
        respuesta = '\n'
        for base in bases:
            respuesta = respuesta + '\t' + base.id + '\n'   # concatena los nombres y los retorna
        return respuesta + '\n'
class InsertT():
    def __init__(self, tabla, base, campos, valores):       # string, string, [string], [string]
        self.tabla = tabla
        self.base = base
        self.campos = campos
        self.valores = valores
    def ejecutar(self):
        if self.base == None:
            nuevo_error = E.Errores('Semántico.', 'No se ha seleccionado una base de datos.')
            #ls_error.append(nuevo_Error)
            return
        tabla = ts_global.get_table(self.base, self.tabla)
        if tabla == None:
            nuevo_error = E.Errores('Semántico.', 'No se ha encontrado la tabla solicitada.')
            ls_error.append(nuevo_Error)
            return
        c_campos = -1
        if self.campos != None:
            columna = None
            errores = False
            c_campos = 0
            for campo in self.campos:
                columna = ts_global.get_column(self.base, self.tabla, campo)
                c_campos = c_campos + 1
                if columna == None:
                    new_error = E.Errores('Semántico.', 'No existe el campo \'' + columna.id + '\' en la tabla \'' + self.tabla + '\'.')
                    #ls_error.append(nuevo_Error)
                    print(new_error.error)
                    errores = True
                elif columna.error != None:
                    #ls_error.append(nuevo_Error)
                    print(columna.error)
                    errores = True
            if errores:
                return
        c_valores = 0
        for valor in self.valores:
            c_valores = c_valores + 1
        if c_campos == -1:
            print('no trae campos, verifica cantidad de campos e inserta en todos')
        elif c_campos == 0:
            print('error al obtener los campos')
        elif c_campos != c_valores:
            new_error = E.Errores('Semántico.', 'La cantidad de campos a ingresar no coincide con la cantidad de valores.')
            #ls_error.append(nuevo_Error)
            print(new_error.error)
        else:
            print('inserción')
'''