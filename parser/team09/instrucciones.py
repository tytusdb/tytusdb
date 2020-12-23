import tabla_simbolos as TS
import Errores as E

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
        base = ts_global.set_dbActual(self.id)              # trato de actualizar la base de datos actual
        if isinstance(base, E.Errores):                     # si no existe, retorna error
            #ls_error.append(base)                           # se agrega el error a la lista
            print('')

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
    def __init__(self, id, cols, inh,cont_key):
        self.id = id
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

class InsertT():
    def __init__(self, tabla, campos, valores):             # string, [string], [string]
        self.tabla = tabla                                  # nombre de la tabla a insertar
        self.campos = campos                                # lista de campos en los que se va a insertar
        self.valores = valores                              # lista de valores a insertar en los campos

    def execute(self, ts_global):
        self.base = ts_global.get_dbActual().id             # se obtiene la base que se usa actualmente
        if isinstance(self.base, E.Errores):                # si no hay base de datos en uso es error
            nuevo_error = E.Errores('Semántico.', 'No se ha seleccionado una base de datos.')
            #ls_error.append(nuevo_Error)                    # se agrega el error a la lista
            return                                          # y termina la ejecución
        tabla = ts_global.get_table(self.base, self.tabla)  # busca si existe la tabla
        if isinstance(tabla, E.Errores):                    # si no existe, es error
            #ls_error.append(tabla)                          # se agrega el error a la lista
            return                                          # y termina la ejecución
        c_campos = -1                                       # variable para llevar conteo de campos
        if self.campos is not None:                         # si la instrucción si trae campos
            columna = None                                  # variable para obtener columnas
            errores = False                                 # bandera para saber si hubieron errores
            c_campos = 0                                    # se cambia el valor del contador para saber que venían campos
            for campo in self.campos:                       # se recorre la lista de campos y se buscan en la tabla de símbolos
                columna = ts_global.get_column(self.base, self.tabla, campo)
                if isinstance(columna, E.Errores):          # si la columna queda en None, hubo error
                    #ls_error.append(columna)                # se agrega el error a la lista
                    errores = True                          # se actualiza que hubo errores
                c_campos = c_campos + 1                     # se aumenta el contador de campos
            if errores:                                     # si hay errores
                return                                      # se retorna y termina la ejecución
        c_valores = len(self.valores)                       # variable para llevar conteo de valores
        if c_campos == 0:                                   # si el contador de campos está en 0, hay errores al reconocerlos
            return                                          # entonces, se sale de la ejecución
        elif c_campos == -1:                                # si el contador de campos está en -1, se inserta en todos los campos
            print('no trae campos, verifica cantidad de campos e inserta en todos')
        elif c_campos != c_valores:                         # si la cantidad de campos es diferente a la cantidad de valores, es error
            new_error = E.Errores('Semántico.', 'La cantidad de campos a ingresar no coincide con la cantidad de valores.')
            #ls_error.append(nuevo_Error)                    # se agrega el error a la lista
            return                                          # y se sale de la ejecución
        else:                                               # si son iguales los contadores, se incerta en los campos
            campo = None                                    # variable para seleccionar un campo de la lista de campos
            valor = None                                    # variable para seleccionar un valor de la lista de valores
            columna = None                                  # variable para obtener la columna de la tabla de símbolos
            tipo_c = False                                  # variable para verificar los tipos de datos
            errores = False                                 # variable para verificar si hay errores
            anterior = 0                                    # variable para llevar el índice anterior
            inserciones = []                                # arreglo para llevar las insercinoes
            for i in range(c_campos):                       # se recorre la lista de campos y se buscan en la tabla de símbolos
                if anterior != i:                           # si la lista de inserciones ya está llena
                    for valor in inserciones:               # se recorre la lista de valores por campo
                        tipo_c = self.verifyType(columna.tipo, valor)
                        if not tipo_c:                      # se verifica el valor del campo, si no coincide es error
                            new_error = E.Errores('Semántico.', 'No se puede insertar \'' + valor + '\' en la columna \'' + columna.id + '\'.')
                            #ls_error.append(nuevo_Error)   # se agrega el error a la lista
                            return                          # sale de la ejecución
                    for constraint in columna.valor:        # se recorre la lista de constraints si tuviera
                        if constraint.tipo == TS.t_constraint.NOT_NULL:
                            tipo_c = self.isNull(columna.tipo, inserciones)
                            if tipo_c:                      # si es nuleable, es error
                                new_error = E.Errores('Semántico.', 'No puede venir null un campo con el constraint \'NOT NULL\'.')
                                #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                errores = True
                        elif constraint.tipo == TS.t_constraint.UNIQUE:
                            tipo_c = self.isUnique(columna.tipo, inserciones)
                            if not tipo_c:                  # si no es único, es error
                                new_error = E.Errores('Semántico.', 'No pueden venir valores repetidos en un campo con el constraint \'UNIQUE\'.')
                                #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                errores = True
                        elif constraint.tipo == TS.t_constraint.PRIMARY:
                            tipo_c = self.isNull(columna.tipo, inserciones)
                            if tipo_c:                      # si es nulleable, es error
                                new_error = E.Errores('Semántico.', 'La llave primaria no puede ser nula.')
                                #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                errores = True
                                break
                            tipo_c = self.isUnique(columna.tipo, inserciones)
                            if not tipo_c:                  # si no es único, es error
                                new_error = E.Errores('Semántico.', 'La llave primaria debe ser única.')
                                #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                errores = True
                                break
                        elif constraint.tipo == TS.t_constraint.DEFOULT:
                            print('')
                        elif constraint.tipo == TS.t_constraint.CHECK:
                            for valor in inserciones:
                                if constraint.condicion == '<':
                                    if valor >= constraint.valor:
                                        new_error = E.Errores('Semántico.', 'Violación del constraint check.')
                                        #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                        errores = True
                                elif constraint.condicion == '>':
                                    if valor <= constraint.valor:
                                        new_error = E.Errores('Semántico.', 'Violación del constraint check.')
                                        #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                        errores = True
                                elif constraint.condicion == '>=':
                                    if valor < constraint.valor:
                                        new_error = E.Errores('Semántico.', 'Violación del constraint check.')
                                        #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                        errores = True
                                elif constraint.condicion == '<=':
                                    if valor > constraint.valor:
                                        new_error = E.Errores('Semántico.', 'Violación del constraint check.')
                                        #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                        errores = True
                                elif constraint.condicion == '=' or constraint.condicion == '==':
                                    if valor != constraint.valor:
                                        new_error = E.Errores('Semántico.', 'Violación del constraint check.')
                                        #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                        errores = True
                                elif constraint.condicion == '<>' or constraint.condicion == '<>':
                                    if valor == constraint.valor:
                                        new_error = E.Errores('Semántico.', 'Violación del constraint check.')
                                        #ls_error.append(nuevo_Error)# se agrega el error a la lista
                                        errores = True
                        elif constraint.tipo == TS.t_constraint.FOREIGN:
                            print('')
                    if errores:
                        return
                    #print(inserciones)
                    # se insertan los datos
                    inserciones = []
                anterior = i                                # se actualiza el anterior
                campo = self.campos[i]                      # se obtiene un campo en el que se va a insertar
                valor = self.valores[i]                     # se obtiene su valor a insertar
                inserciones.append(valor)                   # se agrega el valor a insertar
                columna = ts_global.get_column(self.base, self.tabla, campo)
                print(i, campo, valor, columna, inserciones)

    def verifyType(self, tipo_dato, valor):
        if tipo_dato == TS.tipo_simbolo.BOOLEAN:
            try:
                valor = int(valor)
                if valor == 1:
                    valor = True
                elif valor == 0:
                    valor = False
                else:
                    return False
                return True
            except:
                try:
                    bool(valor)
                    return True
                except:
                    return False
        elif tipo_dato == TS.tipo_simbolo.SMALLINT or tipo_dato == TS.tipo_simbolo.INTEGER or tipo_dato == TS.tipo_simbolo.BIGINT:
            try:
                int(valor)
                return True
            except:
                return False
        elif tipo_dato == TS.tipo_simbolo.DECIMAL or tipo_dato == TS.tipo_simbolo.NUMERIC or tipo_dato == TS.tipo_simbolo.REAL or tipo_dato == TS.tipo_simbolo.D_PRECISION or tipo_dato == TS.tipo_simbolo.MONEY:
            try:
                float(valor)
                return True
            except:
                return False
        elif tipo_dato == TS.tipo_simbolo.TEXT or tipo_dato == TS.tipo_simbolo.CHARACTER_V or tipo_dato == TS.tipo_simbolo.VARCHR or tipo_dato == TS.tipo_simbolo.CHARACTER or tipo_dato == TS.tipo_simbolo.CHAR or tipo_dato == TS.tipo_simbolo.INTERVAL or tipo_dato == TS.tipo_simbolo.TIMESTAMP or tipo_dato == TS.tipo_simbolo.DATA or tipo_dato == TS.tipo_simbolo.TIME:
            if '\'' in valor or '"' in valor:
                return True
            else:
                return False
        else:
            return False

    def isNull(self, tipo_dato, valores):
        for valor in valores:                               # se recorre la lista de valores
            if tipo_dato == TS.tipo_simbolo.TIME:
                cad = (valor.split('\'').split('"'))[1]
                cad = cad.split(':')
                if len(cad) != 3:
                    return True
            elif tipo_dato == TS.tipo_simbolo.TIMESTAMP or tipo_dato == TS.tipo_simbolo.DATA:
                cad = (valor.split('\'').split('"'))[1]
                cad = cad.split('/').split('-')
                if len(cad) != 3:
                    return True
            elif tipo_dato == TS.tipo_simbolo.TEXT or tipo_dato == TS.tipo_simbolo.CHARACTER_V or tipo_dato == TS.tipo_simbolo.VARCHR or tipo_dato == TS.tipo_simbolo.CHARACTER or tipo_dato == TS.tipo_simbolo.CHAR or tipo_dato == TS.tipo_simbolo.INTERVAL:
                cad = valor.split('\'').split('"')
                if len(cad) != 3:
                    return True
            elif tipo_dato == TS.tipo_simbolo.SMALLINT or tipo_dato == TS.tipo_simbolo.INTEGER or tipo_dato == TS.tipo_simbolo.BIGINT or tipo_dato == TS.tipo_simbolo.BOOLEAN or tipo_dato == TS.tipo_simbolo.DECIMAL or tipo_dato == TS.tipo_simbolo.NUMERIC or tipo_dato == TS.tipo_simbolo.REAL or tipo_dato == TS.tipo_simbolo.D_PRECISION or tipo_dato == TS.tipo_simbolo.MONEY:
                return False
            else:                                           # si no es ningún tipo es error
                return True
        return False                                        # si recorre todos los valores, no hay valores nulos

    def isUnique(self, tipo_dato, valores):
        val_verify = []                                     # variable para almacenar los valores verificados
        pos = -1                                            # posición del valor buscado
        for valor in valores:                               # se recorre la lista de valores
            if len(val_verify) == 0:                        # si está vacía la lista de verificados,
                val_verify.append(valor)                    # se inserta el valor
            else:                                           # en caso contrario
                try:                                        # se intenta buscar el valor en la lista
                    pos = val_verify.index(valor)           # si se encuentra,
                    return False                            # significa que no son valores únicos
                except:                                     # si no se encuentra,
                    val_verify.append(valor)                # se agrega a la lista de verificados
                    pos = -1                                # se reinicia la posición
        return True                                         # si recorre toda la lista, sí son datos únicos

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