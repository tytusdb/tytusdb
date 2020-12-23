from models.instructions.shared import Instruction
from controllers.type_checker import TypeChecker
from controllers.error_controller import ErrorController
from controllers.symbol_table import SymbolTable
from models.instructions.Expression.type_enum import *
from models.instructions.DDL.column_inst import *
from controllers.data_controller import *
from models.database import Database
from models.column import Column
from models.table import Table
import json
import datetime
import re
from controllers.error_controller import ErrorController
from views.data_window import DataWindow

class CreateTB(Instruction):

    def __init__(self, table_name, column_list, inherits_from):
        self._table_name = table_name
        self._column_list = column_list
        self._inherits_from = inherits_from
        self._can_create_flag = True

    def __repr__(self):
        return str(vars(self))

    def process(self,instruction):
        typeChecker = TypeChecker()
        nombreTabla = self._table_name.alias
        noCols = self.numberOfColumns(self._column_list)

        resTab = typeChecker.createTable(nombreTabla,noCols,0,0) #TODO add line and column
        
        #Si devuelve None es porque ya existe la tabla
        if resTab == None:
            return

        # Agrega las propiedades que agrupan a varias columnas
        self.generetaExtraProp()
        # Genera las tablas ya con todas sus propiedades
        self.generateColumns(nombreTabla,typeChecker)

        # Si tiene inherits la manoseamos
        if self._inherits_from != None:
            self.addInherits(nombreTabla,self._inherits_from)

        # Si ocurrio algun error en todo el proceso mato la tabla
        if self._can_create_flag == False:
            typeChecker.deleteTable(nombreTabla,0,0)
            return

        # Verifico si tiene llave primaria la tabla o si le meto una escondida
        if self.existsPK(nombreTabla) == 0:
            self.generateHiddenPK(nombreTabla)

        # Agrego llaves primarias a la base de datos si no hubo clavo con la tabla
        self.addPKToDB(nombreTabla)


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
                self.addUnique(columna._column_list)

            elif isinstance(columna,Check):
                self.addCheck(columna._column_condition)

            elif isinstance(columna,PrimaryKey):
                self.addPrimaryKey(columna._column_list)

            elif isinstance(columna,ForeignKey):
                self.addForeignKey(columna._column_list,columna._table_name,columna._table_column_list)

            elif isinstance(columna,Constraint):
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
                validateCol = typeChecker.createColumnTable(tableToInsert,columnaFinal,0,0)

                # if return None an error ocurrio
                if validateCol == None:
                    self._can_create_flag = False
                    return
                
    def addPropertyes(self, prop,columnaFinal):
        if prop['default_value'] != None:
            validation = self.validateType(columnaFinal._dataType,prop['default_value'], True)
            if validation == None:
                return
            else:
                columnaFinal._default = prop['default_value'].alias

        if prop['is_null'] != None:
            if prop['is_null'] == True:
                print('El apartado de null será true')
                columnaFinal._notNull = False
            else:
                print('El apartado de null será false')
                columnaFinal._notNull = True

        if prop['constraint_unique'] != None:
            columnaFinal._unique = True         

        if prop['unique'] != None:
            columnaFinal._unique = True

        if prop['constraint_check_condition'] != None:
            columnaFinal._check =  {
                                    '_constraint_alias' : None,
                                    '_condition_check' : prop['constraint_check_condition'].alias
                                    }
            #prop['constraint_check_condition']  #TODO este es un check que tiene condicional

        if prop['check_condition'] != None:
            columnaFinal._check = {
                                    '_constraint_alias' : None,
                                    '_condition_check' : prop['check_condition'].alias
                                    }
            #prop['check_condition']  #TODO este es un check que tiene condicional

        if prop['pk_option'] != None:
            columnaFinal._primaryKey = True

        if prop['fk_references_to'] != None:
            columnaFinal._foreignKey = prop['fk_references_to']

        return columnaFinal   

    #Agrego un True al atributo unique de la lista de columnas especificadas
    #Si bandera es False quiere decir que hay una fila desconocida en el Unique(col1,...coln)
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
                desc = f": Undefined column in Unique ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return
            bandera = False

    #Agrego un True al atributo pk_option de la lista de columnas especificadas
    #Si bandera es False quiere decir que hay una fila desconocida en el Unique(col1,...coln)
    def addPrimaryKey(self,listaCols):
        bandera = False
        for col in listaCols:
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == col):
                        if columna._properties != None:
                            bandera = True
                            columna._properties[0]['pk_option']  = True
                            break
            if not bandera:
                desc = f": Undefined column in primary key ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return
            bandera = False

    #          foreign key (     ) references id (             ) 
    def addForeignKey(self,listaCols,nombreTabla,listaTablasCols):
        
        # the len of the cols must be de same
        if len(listaCols) != len(listaTablasCols):
            desc = f": cant of params in foreign() != "
            ErrorController().add(36, 'Execution', desc, 0, 0)
            self._can_create_flag = False
            return

        typeChecker = TypeChecker()
        existForeingTable = typeChecker.searchTable(SymbolTable().useDatabase,nombreTabla)

        #validate if the foreign table exists
        if existForeingTable == None:
            desc = f": Undefined table in foreign key ()"
            ErrorController().add(27, 'Execution', desc, 0, 0)
            self._can_create_flag = False
            return

        #validate if the columns exists in the foreign table
        for coli in listaTablasCols:
            if typeChecker.searchColumn(existForeingTable,coli) == None:
                desc = f": Undefined col in table in foreign key ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return

        bandera = False
        for x in range(0,len(listaCols)):
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == listaCols[x]):
                        if columna._properties != None:
                            bandera = True
                            columna._properties[0]['fk_references_to'] = {
                                                                    '_refTable' : nombreTabla,
                                                                    '_refColumn' : listaTablasCols[x]
                                                                        }
                            break
            if not bandera:
                desc = f": Undefined column in foreign key ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return
            bandera = False

    # Used in [CONSTRAINT name] CHECK (condition_many_columns)
    def addConstraint(self,nombreColumna,condicionColumna):
        #                           L (L|D)*
        whatColumnIs = re.search('[a-zA-z]([a-zA-z]|[0-9])*',condicionColumna.alias)
        bandera = False
        if whatColumnIs != None:
            whatColumnIs = whatColumnIs.group(0)
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == whatColumnIs):
                        if columna._properties != None:
                            bandera = True
                            columna._properties[0]['constraint_check_condition'] = condicionColumna
                            break
            if not bandera:
                desc = f": Undefined column in constraint check ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return
            bandera = False

        else:
            desc = f": column not given in constraintcheck()"
            ErrorController().add(26, 'Execution', desc, 0, 0)
            self._can_create_flag = False
            return

    # Used in CHECK (condition_many_columns)
    def addCheck(self,conditionColumn):
        #                           L (L|D)*
        whatColumnIs = re.search('[a-zA-z]([a-zA-z]|[0-9])*',conditionColumn.alias)
        bandera = False
        if whatColumnIs != None:
            whatColumnIs = whatColumnIs.group(0)
            for columna in self._column_list:
                if isinstance(columna,CreateCol):
                    if(columna._column_name == whatColumnIs):
                        if columna._properties != None:
                            bandera = True
                            columna._properties[0]['check_condition'] = conditionColumn
                            break
            if not bandera:
                desc = f": Undefined column in check ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return
            bandera = False

        else:
            desc = f": column not given in check()"
            ErrorController().add(26, 'Execution', desc, 0, 0)
            self._can_create_flag = False
            return


    def validateType(self,columnInfo,defaulValue, process_data):

        columnType = columnInfo['_tipoColumna']
        paramOne = columnInfo['_paramOne']
        paramTwo = columnInfo['_paramTwo']

        valorDef = None

        if process_data:
            valorDef = defaulValue.process(0)

            if valorDef != None:
                valorDef = valorDef.value
            else:
                valorDef = defaulValue.reference_column.value
        else:
            valorDef = defaulValue
        #-->
        if columnType == 'ColumnsTypes.BIGINT':
            try:
                valorDef = int(valorDef)
                if valorDef < 9223372036854775807 and valorDef > -9223372036854775808:
                    pass
                else:
                    desc = f": out of range value in bigint"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False
            except:
                desc = f": invalid default value to bigint column"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                return False

        #-->
        elif columnType == 'ColumnsTypes.BOOLEAN':
            if valorDef == 'True' or valorDef == 'False':
                pass
            else:
                desc = f": invalid default value to boolean column"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                return False


        #-->
        elif columnType == 'ColumnsTypes.CHAR':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    desc = f": invalid length in char column, limit is {str(paramOne)}"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False
            else:
                if len(valorDef) > 1:
                    desc = f": invalid length in char column, limit is 1"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False
                    

        #-->
        elif columnType == 'ColumnsTypes.CHARACTER':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    desc = f": invalid len in character column, limit is {str(paramOne)}"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False
            else:
                if len(valorDef) > 1:
                    desc = f": invalid length in char column, limit is 1"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False

        #-->
        elif columnType == 'ColumnsTypes.CHARACTER_VARYING':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    desc = f": invalid len in varying column, limit is {str(paramOne)}"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False
            else:
                pass

        #-->
        elif columnType == 'ColumnsTypes.DATE':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef,'%Y-%m-%d')
            except:
                desc = f": invalid format in date column"
                ErrorController().add(17, 'Execution', desc, 0, 0)
                return False

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
                            desc = f": overflow in decimal or numeric column"
                            ErrorController().add(6, 'Execution', desc, 0, 0)
                            return False
                else:
                    strValorDef = str(valorDef)
                    if strValorDef.find('.') != -1:
                        division = strValorDef.split('.')
                        parteEntera = int(division[0])
                        if len(str(parteEntera)) > paramOne and parteEntera != 0:
                            desc = f": overflow in decimal or numeric column"
                            ErrorController().add(6, 'Execution', desc, 0, 0)
                            return False

            except:
                desc = f": invalid default value in decimal or numeric"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                return False

        elif columnType == 'ColumnsTypes.DOUBLE_PRECISION' or columnType == 'ColumnsTypes.REAL':
            try:
                float(valorDef)
            except:
                desc = f": invalid default value in double or real"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                return False

        #-->
        elif columnType == 'ColumnsTypes.INTEGER':
            try:
                valorDef = int(valorDef)
                if valorDef < 2147483647 and valorDef > -2147483648:
                    pass
                else:
                    desc = f": default value out of range in integer col"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False
            except:
                desc = f": invalid default value in integer col"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                return False

        #-->
        elif columnType == 'ColumnsTypes.INTERVAL':
            pass

        #-->
        elif columnType == 'ColumnsTypes.MONEY':
            try:
                float(valorDef)
            except:
                desc = f": invalid default value in money col"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                return False

        #-->
        elif columnType == 'ColumnsTypes.SMALLINT':
            try:
                valorDef = int(valorDef)
                if valorDef < 32727 and valorDef > -37767:
                    pass
                else:
                    desc = f": default value out of range in small col"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False
            except:
                desc = f": invalid default value in smallint col"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                return False
        
        #-->
        elif columnType == 'ColumnsTypes.TEXT':
            try:
                valorDef = str(valorDef)
            except:
                desc = f": invalid default value in text col"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                return False
        
        #-->
        elif columnType == 'ColumnsTypes.TIMESTAMP':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef,'%Y-%m-%d %H:%M:%S')
            except:
                desc = f": invalid format timpestamp, yyyy-mm-dd h:m:s"
                ErrorController().add(17, 'Execution', desc, 0, 0)
                return False
        
        #-->
        elif columnType == 'ColumnsTypes.TIME':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef,'%H:%M:%S')
            except:
                desc = f": invalid format time, h:m:s"
                ErrorController().add(17, 'Execution', desc, 0, 0)
                return False

        elif columnType == 'ColumnsTypes.VARCHAR':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    desc = f":  out of range value in varchar col"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    return False
            else:
                pass
        return True


    def addInherits(self,nameChildTable,nameParentTable):
        typeChecker = TypeChecker()
        tablaPadre = typeChecker.searchTable(SymbolTable().useDatabase, nameParentTable)
        tablaHija = typeChecker.searchTable(SymbolTable().useDatabase, nameChildTable)
        
        #La tabla de la que hereda no existe
        if tablaPadre == None:
            desc = f": parent table dont exists"
            ErrorController().add(27, 'Execution', desc, 0, 0)
            self._can_create_flag = False
            return

        for colPar in tablaPadre._colums:
            #Vamos a insertar en la hija
            validarCol = typeChecker.createColumnTable(tablaHija,colPar,0,0)
            #Si es una columna repetida entonces no puede crear la tabla
            if validarCol == None:
                self._can_create_flag = False
                return

    def addPKToDB(self,tableCreated):
        indicesPrimarios = []
        typeChecker = TypeChecker()
        tablaToExtract = typeChecker.searchTable(SymbolTable().useDatabase, tableCreated)    

        for colExt in tablaToExtract._colums:
            if colExt._primaryKey == True:
                indicesPrimarios.append(colExt._number)
            
        
        DataController().alterAddPK(tableCreated,indicesPrimarios,0,0)

    def existsPK(self,tableCreated):
        indicesPrimarios = 0
        typeChecker = TypeChecker()
        tablaToExtract = typeChecker.searchTable(SymbolTable().useDatabase, tableCreated)    

        for colExt in tablaToExtract._colums:
            if colExt._primaryKey == True:
                indicesPrimarios += 1

        return indicesPrimarios

    def generateHiddenPK(self,nombreTabla):
        typeChecker = TypeChecker()
        tipoEscondido = {
            '_tipoColumna' : 'HIDDEN',
            '_paramOne' : None,
            '_paramTwo' : None
        }
        columnaEscondida = Column('HIDDEN',tipoEscondido)
        columnaEscondida._primaryKey = True
        tableToInsert = typeChecker.searchTable(SymbolTable().useDatabase, nombreTabla)
        typeChecker.createColumnTable(tableToInsert,columnaEscondida,0,0)
        print('### SE HA GENERADO UNA LLAVE PRIMARIA ESCONDIDA')

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
