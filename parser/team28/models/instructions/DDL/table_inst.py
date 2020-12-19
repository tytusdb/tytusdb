from models.instructions.shared import Instruction
from controllers.type_checker import TypeChecker
from controllers.error_controller import ErrorController
from controllers.symbol_table import SymbolTable
from models.instructions.DDL.column_inst import *
from models.database import Database
from models.column import Column
from models.table import Table
import json

class CreateTB(Instruction):

    def __init__(self, table_name, column_list, inherits_from):
        self._table_name = table_name
        self._column_list = column_list
        self._inherits_from = inherits_from

    def __repr__(self):
        return str(vars(self))

    def process(self,instruction):
        #print(str(self._table_name))
        #print('================================================================')
        typeChecker = TypeChecker()
        nombreTabla = self._table_name.value
        noCols = self.numberOfColumns(self._column_list)
        typeChecker.createTable(nombreTabla,noCols,0,0) #TODO add name of Database, line and column

        #Agrega las propiedades extras a las columnas especificadas
        for columna in self._column_list:
            #print(str(columna))
            #print('()()()()()()()()()()()()()()()')
            #print('================================================================')
            if isinstance(columna,Unique):
                print('Add Unique in Table')
                self.addUnique(columna._column_list)

            elif isinstance(columna,Check):
                print('Add Check in Table')
                self.addCheck(columna._column_condition)

            elif isinstance(columna,PrimaryKey):
                print('Add Primary Key in Table')
                self.addPrimaryKey(columna._column_list)

            elif isinstance(columna,ForeignKey):
                print('Add Foreign Keys in Table')
                self.addForeignKey(columna._column_list,columna._table_name,columna._table_column_list)

            elif isinstance(columna,Constraint):
                print('Add Constraint in Table')
                self.addConstraint(columna._column_name,columna._column_condition)

        # Genera las tablas ya con todas sus propiedades
        self.generateColumns(nombreTabla,typeChecker)

    def generateColumns(self,nombreTabla,typeChecker):
        for columna in self._column_list:
            if isinstance(columna,CreateCol):
                #print('El nombre de la columna es: ' + str(columna._column_name))
                #print('El tipo de la columna es: ' + str(columna._type_column._tipoColumna))
                print('===================================================================')
                columnaFinal = Column(columna._column_name,columna._type_column)
                if columna._properties != None:
                    print('-------------------------------------------------------------------->')
                    for prop in columna._properties:
                        columnaFinal = self.addPropertyes(prop,columnaFinal)
                typeChecker.createColumnTable(Table(nombreTabla),columnaFinal,0,0) #TODO add name of Database, line and column
                print((columnaFinal).__dict__)

    def numberOfColumns(self, arrayColumns):
        count = 0
        for columna in arrayColumns:
            if isinstance(columna,CreateCol):
                count += 1
        return count

    def addPropertyes(self, prop,columnaFinal):
        if prop['default_value'] != None:
            print('El valor por defecto será: ' + str(prop['default_value'].value))
            columnaFinal._default = prop['default_value'].value

        if prop['is_null'] != None:
            if prop['is_null'] == True:
                print('El apartado de null será true')
                columnaFinal._notNull = False
            else:
                print('El apartado de null será false')
                columnaFinal._notNull = True

        if prop['constraint_unique'] != None:
            columnaFinal._unique = True         #TODO Columna podria tener el atributo constraint unique para darle un alias

        if prop['unique'] != None:
            columnaFinal._unique = True

        if prop['constraint_check_condition'] != None:
            columnaFinal._check = prop['constraint_check_condition']  #TODO este es un check que tiene condicional

        if prop['check_condition'] != None:
            columnaFinal._check = prop['check_condition']  #TODO este es un check que tiene condicional

        if prop['pk_option'] != None:
            columnaFinal._primaryKey = True

        if prop['fk_references_to'] != None:
            print(str(prop['fk_references_to']))
            columnaFinal._foreignKey = prop['fk_references_to']

        return columnaFinal   

    #Agrego un True al atributo unique de la lista de columnas especificadas
    def addUnique(self,listaCols):
        for col in listaCols:
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == col):
                        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        if columna._properties != None:
                            columna._properties[0]['unique'] = True

    def addCheck(self,conditionColumn):
        pass

    def addPrimaryKey(self,listaCols):
        for col in listaCols:
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == col):
                        if columna._properties != None:
                            columna._properties[0]['pk_option']  = True
                            return
        pass

    def addForeignKey(self,listaCols,nombreTabla,listaTablasCols):
        pass

    def addConstraint(self,nombreColumna,condicionColumna):
        pass


class DropTB(Instruction):

    def __init__(self, table_name, noLine, noColumn):
        self._table_name = table_name
        self._noLine = noLine
        self._noColumn = noColumn

    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        typeChecker = TypeChecker()
        typeChecker.deleteTable(self._table_name,
                                self._noLine, self._noColumn)


class AlterTable(Instruction):
    '''
        ALTER TABLE cambia una tabla con diversas opciones de alterar
    '''

    def __init__(self, tablaAModificar, listaCambios):
        self._tablaAModificar = tablaAModificar
        self._listaCambios = listaCambios

    def execute(self):
        pass

    def __repr__(self):
        return str(vars(self))


class AlterTableAdd(AlterTable):
    '''
        puedo agregar una columna
        puedo agregar un check
        puedo agregar  un constraint
        puedo agregar un foreing
    '''

    def __init__(self, changeContent):
        self._changeContent = changeContent

    def __repr__(self):
        return str(vars(self))


class AlterTableAlter(AlterTable):
    '''
        puedo alterar una columna colocandole not null
        puedo alterar una columna asignandole otro tipo     
    '''

    def __init__(self, changeContent):
        self._changeContent = changeContent

    def __repr__(self):
        return str(vars(self))


class AlterTableDrop(AlterTable):
    '''
        puedo eliminar una columna
        puedo eliminar un constraint   
    '''

    def __init__(self, changeContent):
        self._changeContent = changeContent

    def __repr__(self):
        return str(vars(self))


class AlterTableRename(AlterTable):
    '''
        puedo cambiarle el nombre a una tabla  
    '''

    def __init__(self, oldName, newName):
        self._oldName = oldName
        self._newName = newName

    def __repr__(self):
        return str(vars(self))
