from models.instructions.shared import Instruction
from controllers.type_checker import TypeChecker
from controllers.error_controller import ErrorController
from controllers.symbol_table import SymbolTable
from models.instructions.Expression.type_enum import *
from models.instructions.DDL.column_inst import *
from models.database import Database
from models.column import Column
from models.table import Table
import json
import datetime

class CreateTB(Instruction):

    def __init__(self, table_name, column_list, inherits_from):
        self._table_name = table_name
        self._column_list = column_list
        self._inherits_from = inherits_from

    def __repr__(self):
        return str(vars(self))

    def process(self,instruction):
        typeChecker = TypeChecker()
        nombreTabla = self._table_name.value
        noCols = self.numberOfColumns(self._column_list)
        typeChecker.createTable(nombreTabla,noCols,0,0) #TODO add line and column
        # Agrega las propiedades que agrupan a varias columnas
        self.generetaExtraProp()
        # Genera las tablas ya con todas sus propiedades
        self.generateColumns(nombreTabla,typeChecker)


    def numberOfColumns(self, arrayColumns):
        count = 0
        for columna in arrayColumns:
            if isinstance(columna,CreateCol):
                count += 1
        return count

    def generetaExtraProp(self):
        #Agrega las propiedades extras a las columnas especificadas
        for columna in self._column_list:

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

    def generateColumns(self,nombreTabla,typeChecker):
        for columna in self._column_list:
            if isinstance(columna,CreateCol):
                #columna._paramOne
                #columna._paraTwos
                #columna._tipoColumna
                tipoFinal = {
                    '_tipoColumna' : str(columna._type_column._tipoColumna),
                    '_paramOne' : columna._type_column._paramOne,
                    '_paramTwo' : columna._type_column._paramTwo
                }
                columnaFinal = Column(columna._column_name,tipoFinal)
                if columna._properties != None:
                    for prop in columna._properties:
                        columnaFinal = self.addPropertyes(prop,columnaFinal)

                tableToInsert = typeChecker.searchTable(SymbolTable().useDatabase, nombreTabla)
                typeChecker.createColumnTable(tableToInsert,columnaFinal,0,0) #TODO add name of Database, line and column 
                #print((columnaFinal).__dict__)

    def addPropertyes(self, prop,columnaFinal):
        if prop['default_value'] != None:
            self.validateType(columnaFinal._dataType,prop['default_value'])
            #columnaFinal._default = prop['default_value'].value

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
            columnaFinal._check = True
            #prop['constraint_check_condition']  #TODO este es un check que tiene condicional

        if prop['check_condition'] != None:
            columnaFinal._check = True
            #prop['check_condition']  #TODO este es un check que tiene condicional

        if prop['pk_option'] != None:
            columnaFinal._primaryKey = True

        if prop['fk_references_to'] != None:
            print(str(prop['fk_references_to']))
            columnaFinal._foreignKey = prop['fk_references_to']

        return columnaFinal   

    #Agrego un True al atributo unique de la lista de columnas especificadas
    def addUnique(self,listaCols):
        bandera = False
        for col in listaCols:
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == col):
                        if columna._properties != None:
                            bandera = True
                            columna._properties[0]['unique'] = True
                            break
            if not bandera:
                print(' ')
                print('!!!ERROR!!!, Columna desconocida en el Unique') #TODO add Error
                print(' ')
                return
            bandera = False

    def addCheck(self,conditionColumn):
        pass

    def addPrimaryKey(self,listaCols):
        for col in listaCols:
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == col):
                        if columna._properties != None:
                            columna._properties[0]['pk_option']  = True
                            break


    def addForeignKey(self,listaCols,nombreTabla,listaTablasCols):
        for x in range(0,len(listaCols)):
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == listaCols[x]):
                        if columna._properties != None:
                            columna._properties[0]['fk_references_to'] = listaTablasCols[x]
                            #TODO ver si le envio solo la tabla o la columna{'refTable':None,'refColumn':None}

    def addConstraint(self,nombreColumna,condicionColumna):
        pass

    def validateType(self,columnInfo,defaulValue):

        columnType = columnInfo['_tipoColumna']
        paramOne = columnInfo['_paramOne']
        paramTwo = columnInfo['_paramTwo']

        valorDef = defaulValue.process(0)

        if valorDef != None:
            valorDef = valorDef.value
        else:
            valorDef = defaulValue.reference_column.value

        #-->
        if columnType == 'ColumnsTypes.BIGINT':
            try:
                valorDef = int(valorDef)
                if valorDef < 9223372036854775807 and valorDef > -9223372036854775808:
                    pass
                else:
                    print('!!!ERROR!!!, El tamanio del default es muy grande para el bigint')
            except:
                print('!!!ERROR!!!, La columna de tipo bigint no puede aceptar ese valor default')

        #-->
        elif columnType == 'ColumnsTypes.BOOLEAN':
            if valorDef == 'True' or valorDef == 'False':
                pass
            else:
                print('!!!ERROR!!!, La columna de tipo boolean no puede aceptar ese valor default')


        #-->
        elif columnType == 'ColumnsTypes.CHAR':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    print('!!!ERROR!!!, El tamanio default del char sobrepasa el tamanio permitido')
            else:
                if len(valorDef) > 1:
                    print('!!!ERROR!!!, El tamanio default del char sobrepasa el tamanio permitido')

        #-->
        elif columnType == 'ColumnsTypes.CHARACTER':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    print('!!!ERROR!!!, El tamanio default del character sobrepasa el tamanio permitido')
            else:
                if len(valorDef) > 1:
                    print('!!!ERROR!!!, El tamanio default del character sobrepasa el tamanio permitido')

        #-->
        elif columnType == 'ColumnsTypes.CHARACTER_VARYING':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    print('!!!ERROR!!!, El tamanio default del character varying sobrepasa el tamanio permitido')
            else:
                pass

        #-->
        elif columnType == 'ColumnsTypes.DATE':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef,'%Y-%m-%d')
            except:
                print('!!!ERROR!!!, El formato de fecha es invalido, debe ser yyyy-mm-dd')

        #-->
        elif columnType == 'ColumnsTypes.DECIMAL' or columnType == 'ColumnsTypes.NUMERIC':
            try:
                valorDef = float(valorDef)
                if paramOne != None and paramTwo != None:
                    strValorDef = str(valorDef)
                    if strValorDef.find('.') != -1:
                        division = strValorDef.split('.')
                        parteEntera = int(division[0])
                        parteDecimal = int(division[1])
                        conteo = 0
                        if parteEntera != 0:
                            conteo += len(str(parteEntera))
                        conteo += paramTwo
                        if conteo > paramOne:
                            print('!!!ERROR!!!, El dato por default en decimal no corresponde por overflow')
                else:
                    strValorDef = str(valorDef)
                    if strValorDef.find('.') != -1:
                        division = strValorDef.split('.')
                        parteEntera = int(division[0])
                        if len(str(parteEntera)) > paramOne and parteEntera != 0:
                            print('!!!ERROR!!!, El dato por default en decimal no corresponde por overflow')

            except Exception as e:
                print('!!!ERROR!!!, El dato por default en decimal no corresponde')
                print(e)

        elif columnType == ColumnsTypes.DOUBLE_PRECISION or columnType == ColumnsTypes.REAL:
            try:
                float(valorDef)
            except:
                print('!!!ERROR!!!, La columna de tipo double precision or real no puede aceptar ese valor default')

        #-->
        elif columnType == 'ColumnsTypes.INTEGER':
            try:
                valorDef = int(valorDef)
                if valorDef < 2147483647 and valorDef > -2147483648:
                    pass
                else:
                    print('!!!ERROR!!!, El tamanio del default es muy grande para el integer')
            except:
                print('!!!ERROR!!!, La columna de tipo integer no puede aceptar ese valor default')


        #-->
        elif columnType == 'ColumnsTypes.INTERVAL':
            pass

        #-->
        elif columnType == 'ColumnsTypes.MONEY':
            try:
                float(valorDef)
            except:
                print('!!!ERROR!!!, La columna de tipo money no puede aceptar ese valor default')

        #-->
        elif columnType == 'ColumnsTypes.SMALLINT':
            try:
                valorDef = int(valorDef)
                if valorDef < 32727 and valorDef > -37767:
                    pass
                else:
                    print('!!!ERROR!!!, El tamanio del default es muy grande para el smallint')
            except:
                print('!!!ERROR!!!, La columna de tipo smallint no puede aceptar ese valor default')
        
        #-->
        elif columnType == 'ColumnsTypes.TEXT':
            try:
                valorDef = str(valorDef)
            except:
                print('!!!ERROR!!!, El tamanio default del character varying sobrepasa el tamanio permitido')
        
        #-->
        elif columnType == 'ColumnsTypes.TIMESTAMP':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef,'%Y-%m-%d %H:%M:%S')
            except:
                print('!!!ERROR!!!, El formato de timestamp es invalido, debe ser yyyy-mm-dd h:m:s')
        
        #-->
        elif columnType == 'ColumnsTypes.TIME':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef,'%H:%M:%S')
            except:
                print('!!!ERROR!!!, El formato de time es invalido, debe ser h:m:s')

        elif columnType == 'ColumnsTypes.VARCHAR':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    print('!!!ERROR!!!, El tamanio default del varchar sobrepasa el tamanio permitido')
            else:
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
