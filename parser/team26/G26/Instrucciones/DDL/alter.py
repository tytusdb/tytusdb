import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Librerias/storageManager')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Expresiones')

from instruccion import *
from Error import *
from jsonMode import *
from TablaSimbolos import *
from Condicionales import *
from Identificador import *

class Alter(Instruccion):
    #altertipo:
    #   False: alter database
    #   True: alter table
    def __init__(self, id, alteropts, altertipo):
        self.altertipo = altertipo
        self.id = id
        self.alteropts = alteropts
        
    def execute(self, data):
        
        if self.altertipo :
            'table'
            tbname = self.id.id.upper()
            if not self.id.id.upper() in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
                error = Error('Semántico', 'Error(???): no existe la tabla ' + self.id.id.upper(), 0, 0)
                return error

            for alter in self.alteropts :
                al = alter.execute(data, tbname, False)

                if isinstance(al, Error) :
                    return al
                
        else :
            'database'
            dbname = self.id.id.upper()
            if not dbname in data.tablaSimbolos :
                error = Error('Semántico', 'Error(???): no existe la DB ' + self.id.id.upper(), 0, 0)
                return error

            for alter in self.alteropts :
                al = alter.execute(data, dbname)

                if isinstance(al, Error) :
                    return al

            return 'Alter realizado con éxito.'

        return self.id

    def __repr__(self):
        return str(self.__dict__)

class AlterDB(Instruccion):
    #altertipo:
    #   False: owner
    #   True: rename
    def __init__(self, id, altertipo):
        self.altertipo = altertipo
        self.id = id

    def execute(self, data, dbname):

        if self.altertipo :
            'rename'
            ndb = self.id.id.upper()

            data.tablaSimbolos[ndb] = data.tablaSimbolos.pop(dbname)  

            if data.databaseSeleccionada == dbname :
                data.databaseSeleccionada = ndb
            
            'OJO: FALTA LA ESPINO FUNCIÓN'

            return 'rename exitoso'

        else :
            'owner'
            nowner = self.id.id.upper()
            data.tablaSimbolos[dbname]['owner'] = nowner
            return 'owner exitoso'

    def __repr__(self):
        return str(self.__dict__)



#-------------------------------------------------------------------------------------------alter table-------------------------

#-----------------------------------------------------------------------------------------------add------

class AlteraddConstraint(Instruccion):
    def __init__(self, id, alterop):
        self.id = id
        self.alterop = alterop

    def execute(self, data, tbname, cons, idconst = 'ALTER'):
        ncons = self.alterop.execute(data, tbname, True, self.id.upper())
        print(ncons)
        return self.alterop

    def __repr__(self):
        return str(self.__dict__)
 

class AlterTableAddCol(Instruccion):
    def __init__(self, id, tipo):
        self.tipo = tipo
        self.id = id

    def execute(self, data, tbname, cons, idconst = 'ALTER'):

        default = 0     #default value, send to Espino-función

        #validations of default value for Espino-Function
        tip = self.tipo.type.lower()
        siz = self.tipo.length
        if tip == 'integer' or tip == 'smallint' or tip == 'bigint' or tip == 'numeric' or tip == 'real' or tip == 'double' or tip == 'money':
            default = 0
        elif tip == 'character' or tip == 'varchar' or tip == 'char' or tip == 'text' :
            default = 'a'
        elif tip == 'date' :
            default = '28-01-2000'
        elif tip == 'time' :
            default = '10:52:23'
        elif tip == 'boolean' : 
            default = True
        else :
            tip = self.tipo.length.upper()
            if tip in data.tablaSimbolos[data.databaseSeleccionada]['enum'] :
                default = data.tablaSimbolos[data.databaseSeleccionada]['enum'][tip][0].val
                siz = len(data.tablaSimbolos[data.databaseSeleccionada]['enum'][tip])
            else : 
                error = Error('Semántico', 'Error(???): no existe el enum ' + tip.upper(), 0, 0)
                return error
            
        #dictionary for new column
        col = TableData(self.id.upper(), tip, siz, None, None, None, None, None, None)
        #col = {'name':self.id.upper(), 'type':tip, 'size':siz, 'pk':None, 'fk':None, 'default':None, 'null':None, 'check':None, 'unique':None}       

        for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
            if colu.name == self.id.upper() :
                error = Error('Semántico', 'Error(???): ya existe la columna ' + self.id.upper(), 0, 0)
                return error
        
        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'].append(col)

        #FUNCIÓN DE ESPINO
        ret = alterAddColumn(data.databaseSeleccionada, tbname, default)
        if ret == 0 :
            print('Storage: Operación exitosa')
            return 'Storage: Operación exitosa'
        elif ret == 1 :
            error = Error('Storage', 'Error(1): error en la operación.', 0, 0)
            return error
        elif ret == 2 :
            error = Error('Storage', 'Error(2): database no existente.', 0, 0)
            return error
        else : 
            error = Error('Storage', 'Error(3): table no existente.', 0, 0)
            return error

    def __repr__(self):
        return str(self.__dict__)

class AlterTableAddChe(Instruccion):
    def __init__(self, condiciones):
        self.condiciones = condiciones

    def execute(self, data, tbname, cons, idconst = 'ALTER'):
        
        #validar si existe la columna de las condiciones del check
        existe = self.condiciones.validarcondicion(data, tbname)
        if not existe[0] : 
            error = Error('Semántico', 'Error(???): No existe la columna especificada en el check', 0, 0)
            return error

        if idconst == 'ALTER' : #generating new constraint ID
            i = 0
            while True :
                found = False
                idconst = 'CHK_' + 'ALTER' + '_' + tbname + str(i)
                for const in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][existe[1]].check :
                    if const == None :
                        continue
                    if str(const.name) == str(idconst) :
                        found = True
                        break
                if not found:
                    break         
                i += 1
        else :#validate if the constraint exists
            for const in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'] :
                if const.name == idconst.upper() :
                    error = Error('Semántico', 'Error(???): El constraint ' + idconst.upper() + ' ya existe.', 0, 0)
                    return error   

        checkData = ConstraintData(idconst, self.condiciones, 'check')
        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][existe[1]].check.append(checkData)
        colname = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][existe[1]].name
        checkData = ConstraintData(idconst, [colname], 'check')
        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'].append(checkData)
        #print(data)
        #FUNCIÓN DE ESPINO, NO TIENE
        #ret = alterAddColumn(data.databaseSeleccionada, tbname, default)
        #print('check done.')
        print('Alter table add check exitoso.')
        return 'Alter table add check exitoso.'

    def __repr__(self):
        return str(self.__dict__)

class AlterTableAddUnique(Instruccion):
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def execute(self, data, tbname, cons, idconst = 'ALTER'):

        #validate if exists constrain
        for const in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'] :
            if const.name == self.id1.upper() :
                error = Error('Semántico', 'Error(???): El constraint ' + self.id1.upper() + ' ya existe.', 0, 0)
                return error

        #validate if the columns exists and if the is already unique
        colindex = []
        colname = []
        
        for id in self.id2 :
            found = False
            i = 0
            for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
                if colu.name == id.column.upper() :
                    colindex.append(i)
                    found = True

                    if not colu.unique == None :
                        error = Error('Semántico', 'Error(???): La columna ' + id.column.upper() + ' ya es unique.', 0, 0)
                        return error
                
                i += 1
            
            if not found :
                error = Error('Semántico', 'Error(???): No existe la columna ' + id.column.upper(), 0, 0)
                return error
            
            colname.append(id.column.upper())
            
        #validate if the table haves registers already
        filas = extractTable(str(data.databaseSeleccionada), str(tbname))
        if not filas == [] :
            error = Error('Semántico', 'Error(???): La tabla ' + tbname.upper() + ' ya tiene registros guardados.', 0, 0)
            return error  

        for col in colindex:
            checkData = ConstraintData(self.id1.upper(), True, 'unique')
            data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][col].unique = checkData

        checkData = ConstraintData(self.id1.upper(), colname, 'unique')
        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'].append(checkData)

        #print(data)
        print('Alter table add cons unique exitoso.')

        return 'Alter table add cons unique exitoso.'

    def __repr__(self):
        return str(self.__dict__)

class AlterTableAddFor(Instruccion):
    def __init__(self, listaid1, tbid, listaid2):
        self.listaid1 = listaid1
        self.listaid2 = listaid2
        self.tbid = tbid

    def execute(self, data, tbname, cons, idconst = 'ALTER'):
        
        #validate if exists the columns1
        colindex = []   #saves the column index of a valid column
        for id in self.listaid1 :
            found = False
            o = 0
            for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
                if colu.name == id.column.upper() :
                    found = True
                    colindex.append(o)
                o += 1
            
            if not found :
                error = Error('Semántico', 'Error(???): No existe la columna ' + id.column.upper(), 0, 0)
                return error

        #validate if the destiny table exists
        if not self.tbid.upper() in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
            error = Error('Semántico', 'Error(???): La tabla ' + self.tbid.upper() + ' no existe.', 0, 0)
            return error

        #validate if exists the columns2 and are unique or primary keys
        for id in self.listaid2 :
            found = False
            for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.tbid.upper()]['columns']:
                if colu.name == id.column.upper() :
                    found = True
                    if colu.pk == None :
                        error = Error('Semántico', 'Error(???): La columna ' + id.column.upper() + ' no es PK o UNIQUE', 0, 0)
                        return error
            
            if not found :
                error = Error('Semántico', 'Error(???): No existe la columna ' + id.column.upper(), 0, 0)
                return error

        #validate if both list1 and list2 have the same length
        if not len(self.listaid1) == len(self.listaid2) :
            error = Error('Semántico', 'Error(???): El número de columnas especificadas no es el mismo que el número de columnas referenciadas.', 0, 0)
            return error  


        #validate if the table have data already
        filas = extractTable(str(data.databaseSeleccionada), str(tbname))
        if not filas == [] :
            error = Error('Semántico', 'Error(???): La tabla ' + tbname.upper() + ' ya tiene registros guardados.', 0, 0)
            return error  



        if idconst == 'ALTER' : #generating new constraint ID
            i = 0
            while True :
                found = False
                idconst = 'FK_' + 'ALTER' + '_' + tbname + str(i)
                
                for index in colindex :
                    for const in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][index].fk :
                        if const == None :
                            continue
                        if str(const.name) == str(idconst) :
                            found = True
                            break
                    
                if not found:
                    break         
                i += 1
        else :#validate if the constraint exists
            for const in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'] :
                if const.name == idconst.upper() :
                    error = Error('Semántico', 'Error(???): El constraint ' + idconst.upper() + ' ya esta definido.', 0, 0)
                    return error   

        #adding foreign keys
        referenceslist = []
        for id in self.listaid2 :
            referenceslist.append(Identificador(self.tbid.upper(), id.column.upper())) 

        i = 0
        for index in colindex :
            checkData = ConstraintData(idconst, referenceslist[i], 'fk')
            data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][index].fk.append(checkData)
            i += 1
        
        colss = []
        for id in self.listaid1 :
            colss.append(id.column.upper())

        checkData = ConstraintData(idconst, colss, 'fk')
        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'].append(checkData)

        #print(data)
        print('Foreign key agregada con éxito.')

        #Espino-Función -> Se implementa hasta la segunda fase :0
        #alterAddFK(database: str, table: str, references: dict)

        return 'Alter add FK successfully done.'

    def __repr__(self):
        return str(self.__dict__)

class AlterTableAddPK(Instruccion):

    def __init__(self, listaid1):
        self.listaid1 = listaid1

    def execute(self, data, tbname, cons, idconst = 'ALTER'):

        #validate if listaid1 exists
        colindex = []
        for id in self.listaid1 :
            found = False
            i = 0
            for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
                if colu.name == id.column.upper() :
                    found = True
                    colindex.append(i)
                if not colu.pk == None :
                    error = Error('Semántico', 'Error(???): La columna ' + colu.name + ' ya esta definida como PK.', 0, 0)
                    return error
                i += 1
            
            if not found :
                error = Error('Semántico', 'Error(???): No existe la columna ' + id.column.upper(), 0, 0)
                return error

        if idconst == 'ALTER' : #generating new constraint ID
            i = 0
            while True :
                found = False
                idconst = 'PK_' + 'ALTER' + '_' + tbname + str(i)
                
                for index in colindex :
                    const = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][index].pk
                    if const == None :
                        continue
                    if str(const.name) == str(idconst) :
                        found = True
                    
                if not found:
                    break         
                i += 1
        else :#validate if the constraint exists
            for const in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'] :
                if const.name == idconst.upper() :
                    error = Error('Semántico', 'Error(???): El constraint ' + idconst.upper() + ' ya esta definido.', 0, 0)
                    return error  

        #validate if the table haves duplicated keys
        filas = extractTable(str(data.databaseSeleccionada), str(tbname))
        if not filas == [] :
            valpk = {}
            for fila in filas :
                key = ''
                for index in colindex : 
                    key += str(fila[index])

                if not key in valpk:
                    valpk[key] = 'G26'
                else:
                    error = Error('Semántico', 'Error(23505): La nueva llave tiene registros duplicados.', 0, 0)
                    return error
                

        checkData = ConstraintData(idconst, True, 'pk')
        for index in colindex :
            data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][index].pk = checkData

        colss = []
        for id in self.listaid1 :
            colss.append(id.column.upper())

        checkData = ConstraintData(idconst, colss, 'pk')
        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'].append(checkData)
        #print('\n\n')
        #print(data)
        #Espino-Función -> Se implementa hasta la segunda fase :0
        retor = alterAddPK(str(data.databaseSeleccionada), str(tbname), colindex)

        if retor == 0 :
            print('Éxito')
            return 'Storage: Operación exitosa'
        elif retor == 1 :
            error = Error('Storage', 'Error(1): error en la operación.', 0, 0)
            return error
        elif retor == 2 :
            error = Error('Storage', 'Error(2): database no existente.', 0, 0)
            return error
        elif retor == 3 :
            error = Error('Storage', 'Error(3): table no existente.', 0, 0)
            return error
        elif retor == 4 :
            error = Error('Storage', 'Error(4): llave primaria existente.', 0, 0)
            return error
        elif retor == 5 :
            error = Error('Storage', 'Error(5): columnas fuera de límites.', 0, 0)
            return error

        #return self.listaid1

    def __repr__(self):
        return str(self.__dict__)



#---------------------------------------------------------------------------------------------------alter------
class AlterTableAlterNull(Instruccion):
    #alter column set:
    #   False: NOT NULL
    #   True: NULL
    def __init__(self, id, option):
        self.id = id
        self.option = option

    def execute(self, data, tbname, cons, idconst = 'ALTER'):
        
        #validate if listaid1 exists
        colindex = 0
        found = False
        for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
            if colu.name == self.id.upper() :
                found = True
                if not colu.pk == None or not colu.unique == None:
                    error = Error('Semántico', 'Error(???): La primary key o unique no puede modificarse.', 0, 0)
                    return error
                break

            colindex += 1
        
        if not found :
            error = Error('Semántico', 'Error(???): No existe la columna ' + self.id.upper(), 0, 0)
            return error

        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][colindex].null = self.option

        print('Cambio Not null / null exitoso')
        return 'Cambio Not null / null exitoso'

    def __repr__(self):
        return str(self.__dict__)

class AlterTableAlterTipo(Instruccion):
    #alter column set:
    #   False: NOT NULL
    #   True: NULL
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    def execute(self, data, tbname, cons, idconst = 'ALTER'):
        print(self.id)
        print(self.tipo)

        #validate if listaid1 exists
        colindex = 0
        found = False
        for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
            if colu.name == self.id.upper() :
                found = True
                if not colu.pk == None :
                    error = Error('Semántico', 'Error(???): La primary key no puede modificarse.', 0, 0)
                    return error
                if not colu.type == self.tipo.type:
                    error = Error('Semántico', 'Error(???): El tipo del campo no es igual al nuevo tipo.', 0, 0)
                    return error
                if colu.type == 'varchar' or colu.type == 'char':
                    ''
                else:
                    error = Error('Semántico', 'Error(???): El tipo del campo no puede cambiarse.', 0, 0)
                    return error
                break

            colindex += 1

        if not found :
            error = Error('Semántico', 'Error(???): No existe la columna ' + self.id.upper(), 0, 0)
            return error

        #validate new type
        if self.tipo.type == 'varchar' or self.tipo.type == 'char':
            ''
        else:
            error = Error('Semántico', 'Error(???): El tipo nuevo no es valido.', 0, 0)
            return error

        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][colindex].size = self.tipo.length

        #print(data)

        print('Tipo alterado exitoso')
        return 'Tipo alterado exitoso'

    def __repr__(self):
        return str(self.__dict__)

#--------------------------------------------------------------------------------------------------------------drop------
class AlterTableDropCol(Instruccion):

    def __init__(self, id):
        self.id = id

    def execute(self, data, tbname, cons, idconst = 'ALTER'):

        print(self.id.upper())
        #validate if listaid1 exists
        colindex = 0
        found = False
        for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
            if colu.name == self.id.upper() :
                found = True
                if not colu.pk == None:
                    error = Error('Semántico', 'Error(???): No se pueden elminar columnas que sean PK.', 0, 0)
                    return error
                break

            colindex += 1

        if not found :
            error = Error('Semántico', 'Error(???): No existe la columna ' + self.id.upper(), 0, 0)
            return error

        del data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][colindex]

        #print(data)

        #La Espino-Función
        retor = alterDropColumn(data.databaseSeleccionada, tbname, colindex) #al parcer da problemas

        if retor == 0 :
            print('Éxito')
            return 'Storage: Operación exitosa'
        elif retor == 1 :
            error = Error('Storage', 'Error(1): error en la operación.', 0, 0)
            return error
        elif retor == 2 :
            error = Error('Storage', 'Error(2): database no existente.', 0, 0)
            return error
        elif retor == 3 :
            error = Error('Storage', 'Error(3): tableold no existente.', 0, 0)
            return error
        elif retor == 4 :
            error = Error('Storage', 'Error(4): tablenew no existente.', 0, 0)
            return error

    def __repr__(self):
        return str(self.__dict__)

class AlterTableDropCons(Instruccion):

    def __init__(self, id):
        self.id = id

    def execute(self, data, tbname, cons, idconst = 'ALTER'):
        print(data)
        print(self.id)
        if data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'] == [] :
            error = Error('Semántico', 'Error(???): No existe el constraint ' + self.id.upper()+' en la tabla.', 0, 0)
            return error

        found = False
        consttipo = ''
        constindex = 0
        idpks = []
        for const in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'] :
            if const.name == self.id.upper() :
                found = True
                consttipo = const.tipo
                idpks = const.val
                break
            constindex += 1

        if not found :
            error = Error('Semántico', 'Error(???): No existe el constraint ' + self.id.upper()+' en la tabla.', 0, 0)
            return error

        print(consttipo)
        if consttipo == 'pk' :
            for id in idpks :
                for table in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] : 
                    for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][table]['columns'] :
                        for fk in col.fk:
                            if fk == None : 
                                continue
                            if fk.tipo == 'fk' :
                                if fk.val.column == id.upper() :
                                    error = Error('Semántico', 'Error(???): La llave es FK en la tabla ' + table, 0, 0)
                                    return error

        for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'] :
            if consttipo == 'check' :
                i = 0
                foundc = False
                for chk in col.check:
                    if chk == None :
                        ''
                    elif chk.name == self.id.upper() :
                        foundc = True
                        break
                    i+=1
                if foundc:
                    print(str(i))
                    del col.check[i]

            elif consttipo == 'fk':
                i = 0
                foundc = False
                for fk in col.fk:
                    if fk == None :
                        ''
                    elif fk.name == self.id.upper() :
                        foundc = True
                        break
                    i+=1
                if foundc:
                    print(str(i))
                    del col.fk[i]


            elif consttipo == 'pk' :
                if col.pk == None :
                    ''
                elif col.pk.name == self.id.upper() :
                    col.pk = None
            elif consttipo == 'unique':
                if col.unique == None :
                    ''
                elif col.unique.name == self.id.upper() :
                    col.unique = None

        del data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['constraint'][constindex]
            
        #print(data)
        print('Constraint eliminado exitosamente.')

        return self.id

    def __repr__(self):
        return str(self.__dict__)

class AlterTableDropPK(Instruccion):
    
    def __init__(self, ids):
        self.ids = ids

    def execute(self, data, tbname, cons, idconst = 'ALTER'):
        
        colindex = []
        for id in self.ids :
            found = False
            i = 0
            for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'] :
                if not col.pk == None : 
                    if col.name == id.column.upper() :
                        found = True
                        colindex.append(i)
                i += 1
                        
            if not found :
                error = Error('Semántico', 'Error(???): El campo '+id.column.upper()+' no es llave primaria.', 0, 0)
                return error

        contpk = 0
        for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'] :
            if not col.pk == None : 
                contpk += 1

        if not len(self.ids) == contpk:
            error = Error('Semántico', 'Error(???): El número de llaves primarias es diferente al ingresado.', 0, 0)
            return error

        for id in self.ids :
            for table in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] : 
                for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][table]['columns'] :
                    for fk in col.fk:
                        if fk == None : 
                            continue
                        if fk.tipo == 'fk' :
                            if fk.val.column == id.column.upper() :
                                error = Error('Semántico', 'Error(???): La PK es FK en la tabla ' + table, 0, 0)
                                return error
        
        for index in colindex :
            data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][index].pk = None

        #print(data)

        #La Espino-Función
        retor = alterDropPK(data.databaseSeleccionada, tbname)

        if retor == 0 :
            print('Éxito')
            return 'Storage: Operación exitosa'
        elif retor == 1 :
            error = Error('Storage', 'Error(1): error en la operación.', 0, 0)
            return error
        elif retor == 2 :
            error = Error('Storage', 'Error(2): database no existente.', 0, 0)
            return error
        elif retor == 3 :
            error = Error('Storage', 'Error(3): tableold no existente.', 0, 0)
            return error
        elif retor == 4 :
            error = Error('Storage', 'Error(4): tablenew no existente.', 0, 0)
            return error

        return self.ids

    def __repr__(self):
        return str(self.__dict__)

class AlterTableDropFK(Instruccion):
    
    def __init__(self, ids):
        self.ids = ids

    def execute(self, data, tbname, cons, idconst = 'ALTER'):
        print(self.ids)

        colindex = []
        for id in self.ids :
            found = False
            i = 0
            for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'] :
                if not col.fk == None : 
                    if col.name == id.column.upper() :
                        found = True
                        colindex.append(i)
                i += 1
                        
            if not found :
                error = Error('Semántico', 'Error(???): El campo '+id.column.upper()+' no es llave foranea.', 0, 0)
                return error

        for index in colindex :
            data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][index].fk = [None]

        #print('\n\n')
        #print(data)
        print('Foreign key eliminada con éxito.')

        #La Espino-Función
        #retor = alterDropPK(data.databaseSeleccionada, tbname)

        return self.ids

    def __repr__(self):
        return str(self.__dict__)

#----------------------------------------------------------------------------------------------------------------rename------
class AlterTableRenameTB(Instruccion):
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def execute(self, data, tbname, cons, idconst = 'ALTER'):

        #validate if listaid1 exists
        if not self.id1.upper() in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
            error = Error('Semántico', 'Error(???): No existe la tabla ' + self.id1.upper(), 0, 0)
            return error

        #validate if listaid2 exists
        if self.id2.upper() in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
            error = Error('Semántico', 'Error(???): Ya existe la tabla ' + self.id2.upper(), 0, 0)
            return error

        for table in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] : 
            for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][table]['columns'] :
                for fk in col.fk:
                    if fk == None : 
                        continue
                    if fk.tipo == 'fk' :
                        if fk.val.table == self.id1.upper() :
                            fk.val.table = self.id2.upper()


        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.id2.upper()] = data.tablaSimbolos[data.databaseSeleccionada]['tablas'].pop(self.id1.upper())

        #print(data)

        #La Espino-Función
        retor = alterTable(data.databaseSeleccionada, self.id1.upper(), self.id2.upper())

        if retor == 0 :
            print('Éxito')
            return 'Storage: Operación exitosa'
        elif retor == 1 :
            error = Error('Storage', 'Error(1): error en la operación.', 0, 0)
            return error
        elif retor == 2 :
            error = Error('Storage', 'Error(2): database no existente.', 0, 0)
            return error
        elif retor == 3 :
            error = Error('Storage', 'Error(3): tableold no existente.', 0, 0)
            return error
        elif retor == 4 :
            error = Error('Storage', 'Error(4): tablenew no existente.', 0, 0)
            return error

    def __repr__(self):
        return str(self.__dict__)



class AlterTableRenameCol(Instruccion):
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def execute(self, data, tbname, cons, idconst = 'ALTER'):

        #validate if id2 doesn't exists
        found = False
        for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
            if colu.name == self.id1.upper() :
                found = True
                break

        if found :
            error = Error('Semántico', 'Error(???): Ya existe la columna ' + self.id2.upper(), 0, 0)
            return error

        #validate if listaid1 exists
        colindex = 0
        found = False
        for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
            if colu.name == self.id1.upper() :
                found = True
                break

            colindex += 1

        if not found :
            error = Error('Semántico', 'Error(???): No existe la columna ' + self.id1.upper(), 0, 0)
            return error
            
        #Can't rename columns
        error = Error('Semántico', 'Error(???): No se permite renombrar columnas.', 0, 0)
        return error
            
        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][colindex].name = self.id2.upper()

        print('Rename column exitoso')
        return 'Rename column exitoso'

    def __repr__(self):
        return str(self.__dict__)