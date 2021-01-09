import sys
sys.path.append('../team01/G26/Instrucciones')
sys.path.append('../team01/G26/Utils')
sys.path.append('../team01/G26/Librerias/storageManager')

from jsonMode import *
from instruccion import *
from Lista import *
from TablaSimbolos import *
from Error import *

class Create(Instruccion):

    def __init__(self, type, name, list):
        self.type = type
        self.name = name
        self.list = list

    def execute(self, data):
        if self.type == 'type' :
            #if data.comprobarExistencia(self.name, 'enum'):
            #    return 'Error(42710): duplicate_object.'
            #else:
            #    tablaSimbolos.append(Enum(data.databaseSeleccionada, self.name, self.list))
            data.tablaSimbolos[data.databaseSeleccionada]['enum'][self.name.upper()] = self.list
            return 'Se ha creado el enum ' + self.name.upper() + ' correctamente.'
        elif self.type == 'database' :
            description = self.list.execute()
            valRetorno = createDatabase(description.id.upper())
            if valRetorno == 0:
                owner = description.owner.execute()
                mode = owner.mode.execute()
                if owner.id == None : owner.id = 'CURRENT_USER'
                data.tablaSimbolos[description.id.upper()] = {'tablas' : {}, 'enum' : {}, 'owner' : owner.id, 'mode' : mode.val}
                return 'Se ha creado la base de datos ' + description.id.upper() + ' correctamente.'
            elif valRetorno == 1:
                return 'Error(42P12): invalid_database_definition.'
            elif valRetorno == 2:
                return 'Error(42P04): duplicate_database.'
            else:
                return 'Error(???): unknown_error'
        elif self.type == 'table' :
            contColumnas = 0
            description = self.list['table']
            for column in description.description:
                if column.type == 'primary':
                    ''
                elif column.type == 'foreign':
                    ''
                elif column.type == 'constraint':
                    ''
                elif column.type == 'check':
                    ''
                elif column.type == 'unique':
                    ''
                else:
                    contColumnas = contColumnas + 1
            #--------------validaciones de inherits
            tbinhe = description.inherit
            if not tbinhe == None :
                'validaciones inherits'
                if not tbinhe.column.upper() in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
                    error = Error('Semántico', 'Error(???): no existe la tabla ' + tbinhe.column.upper(), 0, 0)
                    return error
                
                for column in description.description:
                    if column.type == 'primary' or column.type == 'foreign' or column.type == 'constraint' or column.type == 'check' or column.type == 'unique' :
                        continue
                    else :
                        for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbinhe.column.upper()]['columns'] :
                            if col.name == column.type.upper() :
                                error = Error('Semántico', 'Error(???): ya existe la columna ' + column.type.upper()+' en la tabla padre.', 0, 0)
                                return error

                contColumnas += len(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbinhe.column.upper()]['columns'])
                #print(contColumnas)
                #print(description.description)
            #--------------
            valRetorno = createTable(data.databaseSeleccionada, self.name.upper(), contColumnas)
            if valRetorno == 1:
                return 'Error(42P16): invalid_table_definition.'
            elif valRetorno == 2:
                return 'Error(???): No existe la base de datos.'
            elif valRetorno == 3:
                return 'Error(42P07): duplicate_table.'
            elif valRetorno == 0:
                contadorColumnas = 0
                ListaColumnasPK = []
                data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.name.upper()] = {'columns' : [], 'constraint' : []}
                for column in description.description:
                    if column.type == 'primary':
                        for columnsPK in column.id:
                            valCont = 0
                            for columnasCreadas in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.name.upper()]['columns']:
                                if columnasCreadas.name.upper() == columnsPK.column.upper() :
                                    ListaColumnasPK.append(valCont)
                                    columnasCreadas.pk = ConstraintData('PK_' + self.name.upper() + '_' + columnsPK.column.upper(), True, 'pk')
                                    break
                                valCont = valCont + 1
                        resPK = alterAddPK(data.databaseSeleccionada, self.name.upper(), ListaColumnasPK)
                        if resPK == 1: print('Error(???): Error de operacion.')
                        elif resPK == 2: print('Error(???): La base de datos no existe.')
                        elif resPK == 3: print('Error(???): La tabla no existe.')
                        elif resPK == 4: print('Error(???): Llave primaria existente.')
                        elif resPK == 5: print('Error(42P10): invalid_column_reference.')
                    elif column.type == 'foreign':
                       foreign = column.execute(data)
                       if isinstance(foreign, Error):
                           return foreign
                    elif column.type == 'constraint':
                        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.name.upper()]['constraint'].append(ConstraintData(column.id, column.list, 'check'))
                    else:
                        banderaDef = True
                        if column.list.type == 'primary':
                            banderaDef = False
                            primary = column.list.execute(data)
                            default = primary.list.execute(data)
                            references = None
                        elif column.list.type == 'references':
                            banderaDef = False
                            primary = None
                            references = column.list.execute(data)
                            default = references.extra.execute(data)
                        if banderaDef :
                            default = column.list.execute(data)
                            primary = None
                            references = None
                        type = column.id.execute()
                        if type.type == 'id':
                            if type.length.upper() in data.tablaSimbolos[data.databaseSeleccionada]['enum']:
                                type.type = type.length.upper()
                                type.length = len(data.tablaSimbolos[data.databaseSeleccionada]['enum'][type.type])
                            else:
                                dropTable(data.databaseSeleccionada, self.name.upper())
                                return 'Error(???): El tipo ' + type.length.upper() + ' no se encuentra declarado en los ENUMS.'

                        null = default.list.execute(data)
                        unique = null.list.execute(data)
                        if unique.list == None : check = None
                        else : check = unique.list.execute(data)

                        '''print('----------Columnas inicio----------')
                        print(primary)
                        print(references)
                        print(type)
                        print(default)
                        print(null)
                        print(unique)
                        print(check)
                        print('----------Columnas fin----------')'''

                        if primary != None:
                            primaryData = ConstraintData('PK_' + self.name.upper() + '_' + column.type.upper(), True, 'pk')
                            ListaColumnasPK.clear()
                            ListaColumnasPK.append(contadorColumnas)
                            resPK = alterAddPK(data.databaseSeleccionada, self.name.upper(), ListaColumnasPK)
                            if resPK == 1: print('Error(???): Error de operacion.')
                            elif resPK == 2: print('Error(???): La base de datos no existe.')
                            elif resPK == 3: print('Error(???): La tabla no existe.')
                            elif resPK == 4: print('Error(???): Llave primaria existente.')
                            elif resPK == 5: print('Error(42P10): invalid_column_reference.')
                        else: primaryData = None

                        if references != None: foreignData = ConstraintData('FK_' + self.name.upper() + '_' + column.type.upper(), references.list, 'fk')
                        else: foreignData = None

                        if default.extra : defaultData = ConstraintData('DFT_' + self.name.upper() + '_' + column.type.upper(), default.id, 'dft')
                        else : defaultData = None

                        if null.id : nullData = False
                        else :
                            if null.extra: nullData = True
                            else : nullData = True

                        if unique.extra :
                            if unique.id == None: uniqueData = ConstraintData('UNQ_' + self.name.upper() + '_' + column.type.upper(), True, 'null')
                            else: uniqueData = ConstraintData(unique.id, True, 'unique')
                        else : uniqueData = None

                        if check == None : checkData = None
                        else :
                            if check.id == None : checkData = ConstraintData('CHK_' + self.name.upper() + '_' + column.type.upper(), check.list, 'check')
                            else : checkData = ConstraintData(check.id, check.list, 'check')

                        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.name.upper()]['columns'].append(TableData(column.type.upper(), type.type, type.length, primaryData, [foreignData], defaultData, nullData, uniqueData, [checkData]))
                        contadorColumnas = contadorColumnas + 1

                #-----------hacer inherits
                if not tbinhe == None :
                    for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbinhe.column.upper()]['columns'] :
                        colmn = TableData(col.name, col.type, col.size, col.pk, col.fk, col.default, col.null, col.unique, col.check)
                        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.name.upper()]['columns'].append(colmn)
                    
                    for const in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbinhe.column.upper()]['constraint'] :
                        con = ConstraintData(const.name, const.val, const.tipo)
                        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.name.upper()]['constraint'].append(con)
                #-----------------------

                return 'Se ha creado la tabla ' + self.name.upper() + ' correctamente.'
        elif self.type == 'replace' :
            dbase = self.list.id.upper()
            if dbase in data.tablaSimbolos :
                'Replace'
                retorno = dropDatabase(dbase)
                if retorno == 0 :
                    'Éxito'
                    #Buscar en la tabla de simbolos si existe
                    if dbase in data.tablaSimbolos :
                        del data.tablaSimbolos[dbase]
                        
                    'DB Eliminada éxitosamente'

                elif retorno == 1:
                    'Error'
                    error = Error('Semántico', 'Error(???): unknown_error', 0, 0)
                    return error

                elif retorno == 2:
                    'No existe'
                    error = Error('Semántico', 'Error(???): no existe la base de datos', 0, 0)
                    return error


            'Create'
            description = self.list.execute()
            valRetorno = createDatabase(description.id.upper())
            if valRetorno == 0:
                owner = description.owner.execute()
                mode = owner.mode.execute()
                if owner.id == None : owner.id = 'CURRENT_USER'
                data.tablaSimbolos[description.id.upper()] = {'tablas' : {}, 'enum' : {}, 'owner' : owner.id, 'mode' : mode.val}
                return 'Se ha creado la base de datos ' + description.id.upper() + ' correctamente.'
            elif valRetorno == 1:
                error = Error('Semántico', 'Error(42P12): invalid_database_definition.', 0, 0)
                return error
            elif valRetorno == 2:
                error = Error('Semántico', 'Error(42P04): duplicate_database.', 0, 0)
                return error
            else:
                error = Error('Semántico', 'Error(???): unknown_error', 0, 0)
                return error
        return '1'

    def __repr__(self):
        return str(self.__dict__)

class Exists(Instruccion):

    def __init__(self, exist, id, owner):
        self.exist = exist
        self.id = id
        self.owner = owner

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class Owner(Instruccion):

    def __init__(self, id, mode):
        self.id = id
        self.mode = mode

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class Table(Instruccion):

    def __init__(self, description, inherit):
        self.description = description
        self.inherit = inherit

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)

class TableDescription(Instruccion):

    def __init__(self, type, id, list, extra):
        self.type = type
        self.id = id
        self.list = list
        self.extra = extra

    def execute(self, data, tbname = 'NADA'):
        if self.type == 'foreign':
            if self.tableExists(data):
                
                #validando que ambas listas tengan el mismo tamaño
                if len(self.list) != len(self.extra) :
                    error = Error('Semántico', 'Error(FK): El númmero de FK especificadas no coincide con el de columnas de referencia.', 0, 0)
                    return error

                #validando si las colunas de la lista extra existen
                tabla = self.id.upper()
                for col in self.extra :
                    found = False
                    for column in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tabla]['columns'] :
                        if col.column.lower() == column.name.lower() :
                            found = True
                    if not found :
                        error = Error('Semántico', 'Error(FK): La columna: ' +  col.column.upper() +' no existe.', 0, 0)
                        return error

                #validando que las columnas de la lista list existan
                colindex = []
                for col in self.list :
                    found = False
                    i = 0
                    for column in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname.upper()]['columns'] :
                        if col.column.lower() == column.name.lower() :
                            found = True
                            colindex.append(i)
                        i += 1

                    if not found :
                        error = Error('Semántico', 'Error(FK): La columna: ' +  col.column.upper() +' no existe.', 0, 0)
                        return error

                #agregando a tabla de simbolos
                referenceslist = []
                for id in self.extra :
                    referenceslist.append(Identificador(self.id.upper(), id.column.upper())) 
                
                print(referenceslist)

                i = 0
                for index in colindex :
                    idconst = 'FK_'+tbname+'_'+data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][index].name
                    checkData = ConstraintData(idconst, referenceslist[i], 'fk')
                    data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns'][index].fk.append(checkData)
                    i += 1

                print(self)
                    
            else:
                error = Error('Semántico', 'Error(FK): La tabla: ' + self.id +' no existe.', 0, 0)
                return error

        elif self.type == 'references' :
            print(self)
                
        return self


    def tableExists(self, data):
        for table in data.tablaSimbolos[data.databaseSeleccionada]['tablas']:
            if self.id.lower() == table.lower():
                return True
        
        return True

    def __repr__(self):
        return str(self.__dict__)
