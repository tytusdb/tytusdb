import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')

from instruccion import *
from Lista import *
from TablaSimbolos import *

class Create(Instruccion):

    def __init__(self, type, name, list):
        self.type = type
        self.name = name
        self.list = list

    def execute(self, data):
        if self.type == 'type' :
            if data.comprobarExistencia(self.name, 'enum'):
                return 'Error(42710): duplicate_object.'
            else:
                tablaSimbolos.append(Enum(data.databaseSeleccionada, self.name, self.list))
        elif self.type == 'database' :
            description = self.list.execute()
            if data.comprobarExistencia(description.id, 'database'):
                return 'Error(42P04): duplicate_database.'
            else:
                owner = description.owner.execute()
                mode = owner.mode.execute()
                if owner.id == None : owner.id = 'CURRENT_USER'
                data.tablaSimbolos.append(DatabaseData(description.id.upper(), owner.id.upper(), mode.val, False))
        elif self.type == 'table' :
            if data.comprobarExistencia(self.name.upper(), 'table'):
                return 'Error(42P07): duplicate_table.'
            else:
                if data.databaseSeleccionada == '': return 'No ha sido seleccionada ninguna base de datos.'
                else:
                    description = self.list['table']
                    for column in description.description:
                        if column.type == 'primary':
                            ''
                        elif column.type == 'foreign':
                            ''
                        elif column.type == 'constraint':
                            ''
                        else:
                            if data.comprobarColumnaTabla(column.type.upper(), self.name.upper()) :
                                print('Error(42701): duplicate_column')
                            else :
                                type = column.id.execute()
                                banderaDef = True
                                primary = None

                                if column.list.type == 'default':
                                    banderaDef = False
                                    default = column.list.execute()
                                    ''
                                elif column.list.type == 'primary':
                                    ''
                                elif column.list.type == 'references':
                                    ''
                                if banderaDef :
                                    ''
                                foreign = None

                                null = default.list.execute()
                                unique = null.list.execute()
                                if unique.list == None : check = None
                                else : check = unique.list.execute()
                                '''print('----------Columnas inicio----------')
                                print(type)
                                print(default)
                                print(null)
                                print(unique)
                                print(check)
                                print('----------Columnas fin----------')'''
                                primaryData = None
                                foreignData = None

                                if default.extra : defaultData = ConstraintData('DFT_' + self.name.upper() + '_' + column.type.upper(), default.id)
                                else : defaultData = None

                                if null.id : nullData = ConstraintData('NULL_' + self.name.upper() + '_' + column.type.upper(), False)
                                else : nullData = ConstraintData('NULL_' + self.name.upper() + '_' + column.type.upper(), True)

                                if unique.extra :
                                    if unique.id == None: uniqueData = ConstraintData('UNQ_' + self.name.upper() + '_' + column.type.upper(), True)
                                    else: uniqueData = ConstraintData(unique.id, True)
                                else : uniqueData = ConstraintData('UNQ_' + self.name.upper() + '_' + column.type.upper(), False)

                                if check == None : checkData = None
                                else :
                                    if check.id == None : checkData = ConstraintData('CHK_' + self.name.upper() + '_' + column.type.upper(), check.list)
                                    else : checkData = ConstraintData(check.id, check.list)

                                data.tablaSimbolos.append(TableData(data.databaseSeleccionada, self.name.upper(), column.type.upper(), type.type, type.length, primaryData, foreignData, defaultData, nullData, uniqueData, checkData))

        elif self.type == 'replace' :
            comp = data.obtenerDatabase(self.name)
            if comp == None:
                'Se crea la base de datos'
            else:
                'Se debe de reemplazar la base de datos'
        return self

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

    def execute(self):
        return self

    def __repr__(self):
        return str(self.__dict__)
