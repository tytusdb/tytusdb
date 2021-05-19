import json
import datetime
import re

from parserT28.models.instructions.shared import Instruction
from parserT28.controllers.type_checker import TypeChecker
from parserT28.controllers.error_controller import ErrorController
from parserT28.controllers.symbol_table import SymbolTable
from parserT28.models.instructions.Expression.type_enum import *
from parserT28.models.instructions.DDL.column_inst import *
from parserT28.controllers.data_controller import *
from parserT28.models.database import Database
from parserT28.models.column import Column
from parserT28.models.table import Table
from parserT28.models.instructions.DDL.column_inst import *
from parserT28.controllers.error_controller import ErrorController
from parserT28.controllers.three_address_code import ThreeAddressCode
from parserT28.views.data_window import DataWindow


class CreateTB(Instruction):

    def __init__(self, table_name, column_list, inherits_from, tac):
        self._table_name = table_name
        self._column_list = column_list
        self._inherits_from = inherits_from
        self._can_create_flag = True
        self._tac = tac

    def __repr__(self):
        return str(vars(self))

    def process(self, instruction):
        typeChecker = TypeChecker()
        nombreTabla = self._table_name.alias
        noCols = self.numberOfColumns(self._column_list)

        resTab = typeChecker.createTable(
            nombreTabla, noCols, 0, 0)  # TODO add line and column

        # Si devuelve None es porque ya existe la tabla
        if resTab == None:
            return

        # Agrega las propiedades que agrupan a varias columnas
        self.generetaExtraProp()
        # Genera las tablas ya con todas sus propiedades
        self.generateColumns(nombreTabla, typeChecker)

        # Si tiene inherits la manoseamos
        if self._inherits_from != None:
            self.addInherits(nombreTabla, self._inherits_from)

        # Si ocurrio algun error en todo el proceso mato la tabla
        if self._can_create_flag == False:
            typeChecker.deleteTable(nombreTabla, 0, 0)
            return

        # Verifico si tiene llave primaria la tabla o si le meto una escondida
        # if self.existsPK(nombreTabla) == 0:
        #     self.generateHiddenPK(nombreTabla)

        # Agrego llaves primarias a la base de datos si no hubo clavo con la tabla
        self.addPKToDB(nombreTabla)

    def compile(self, instrucction):
        # CREANDO C3D
        temp = ThreeAddressCode().newTemp()
        database_id = SymbolTable().useDatabase
        if database_id is not None:
            ThreeAddressCode().addCode(
                f"{temp} = \"USE {database_id}; {self._tac}\"")
        else:
            ThreeAddressCode().addCode(f"{temp} = \"{self._tac}\"")
        # LLAMANDO A FUNCION PARA ANALIZAR ESTA COCHINADA
        temp1 = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp1} = parse({temp})")

    def numberOfColumns(self, arrayColumns):
        count = 0
        for columna in arrayColumns:
            if isinstance(columna, CreateCol):
                count += 1
        return count

    def generetaExtraProp(self):
        # Agrega las propiedades extras a las columnas especificadas
        for columna in self._column_list:

            if isinstance(columna, Unique):
                self.addUnique(columna._column_list)

            elif isinstance(columna, Check):
                self.addCheck(columna._column_condition)

            elif isinstance(columna, PrimaryKey):
                self.addPrimaryKey(columna._column_list)

            elif isinstance(columna, ForeignKey):
                self.addForeignKey(
                    columna._column_list, columna._table_name, columna._table_column_list)

            elif isinstance(columna, Constraint):
                self.addConstraint(columna._column_name,
                                   columna._column_condition)

    def generateColumns(self, nombreTabla, typeChecker):
        for columna in self._column_list:
            if isinstance(columna, CreateCol):
                # columna._paramOne
                # columna._paraTwos
                # columna._tipoColumna
                tipoFinal = {
                    '_tipoColumna': str(columna._type_column._tipoColumna),
                    '_paramOne': columna._type_column._paramOne,
                    '_paramTwo': columna._type_column._paramTwo
                }
                columnaFinal = Column(columna._column_name, tipoFinal)
                if columna._properties != None:
                    for prop in columna._properties:
                        columnaFinal = self.addPropertyes(prop, columnaFinal)

                tableToInsert = typeChecker.searchTable(
                    SymbolTable().useDatabase, nombreTabla)
                validateCol = typeChecker.createColumnTable(
                    tableToInsert, columnaFinal, 0, 0)

                # if return None an error ocurrio
                if validateCol == None:
                    self._can_create_flag = False
                    return

    def addPropertyes(self, prop, columnaFinal):
        if prop['default_value'] != None:
            validation = self.validateType(
                columnaFinal._dataType, prop['default_value'], True)
            if validation == None or validation == False:
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
            columnaFinal._check = {
                '_constraint_alias': None,
                '_condition_check': prop['constraint_check_condition'].alias
            }
            # prop['constraint_check_condition']  #TODO este es un check que tiene condicional

        if prop['check_condition'] != None:
            columnaFinal._check = {
                '_constraint_alias': None,
                '_condition_check': prop['check_condition'].alias
            }
            # prop['check_condition']  #TODO este es un check que tiene condicional

        if prop['pk_option'] != None:
            columnaFinal._primaryKey = True

        if prop['fk_references_to'] != None:
            columnaFinal._foreignKey = prop['fk_references_to']

        return columnaFinal

    # Agrego un True al atributo unique de la lista de columnas especificadas
    # Si bandera es False quiere decir que hay una fila desconocida en el Unique(col1,...coln)
    def addUnique(self, listaCols):
        bandera = False
        for col in listaCols:
            for columna in self._column_list:
                if isinstance(columna, CreateCol):
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

    # Agrego un True al atributo pk_option de la lista de columnas especificadas
    # Si bandera es False quiere decir que hay una fila desconocida en el Unique(col1,...coln)
    def addPrimaryKey(self, listaCols):
        bandera = False
        for col in listaCols:
            for columna in self._column_list:
                if isinstance(columna, CreateCol):
                    if(columna._column_name == col):
                        if columna._properties != None:
                            bandera = True
                            columna._properties[0]['pk_option'] = True
                            break
            if not bandera:
                desc = f": Undefined column in primary key ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return
            bandera = False

    #          foreign key (     ) references id (             )
    def addForeignKey(self, listaCols, nombreTabla, listaTablasCols):

        # the len of the cols must be de same
        if len(listaCols) != len(listaTablasCols):
            desc = f": cant of params in foreign() != "
            ErrorController().add(36, 'Execution', desc, 0, 0)
            self._can_create_flag = False
            return

        typeChecker = TypeChecker()
        existForeingTable = typeChecker.searchTable(
            SymbolTable().useDatabase, nombreTabla)

        # validate if the foreign table exists
        if existForeingTable == None:
            desc = f": Undefined table in foreign key ()"
            ErrorController().add(27, 'Execution', desc, 0, 0)
            self._can_create_flag = False
            return

        # validate if the columns exists in the foreign table
        for coli in listaTablasCols:
            if typeChecker.searchColumn(existForeingTable, coli) == None:
                desc = f": Undefined col in table in foreign key ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return

        bandera = False
        for x in range(0, len(listaCols)):
            for columna in self._column_list:
                if isinstance(columna, CreateCol):
                    if(columna._column_name == listaCols[x]):
                        if columna._properties != None:
                            bandera = True
                            columna._properties[0]['fk_references_to'] = {
                                '_refTable': nombreTabla,
                                '_refColumn': listaTablasCols[x]
                            }
                            break
            if not bandera:
                desc = f": Undefined column in foreign key ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return
            bandera = False

    # Used in [CONSTRAINT name] CHECK (condition_many_columns)
    def addConstraint(self, nombreColumna, condicionColumna):
        #                           L (L|D)*
        whatColumnIs = re.search(
            '[a-zA-z]([a-zA-z]|[0-9])*', condicionColumna.alias)
        bandera = False
        if whatColumnIs != None:
            whatColumnIs = whatColumnIs.group(0)
            for columna in self._column_list:
                if isinstance(columna, CreateCol):
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
    def addCheck(self, conditionColumn):
        #                           L (L|D)*
        whatColumnIs = re.search(
            '[a-zA-z]([a-zA-z]|[0-9])*', conditionColumn.alias)
        bandera = False
        if whatColumnIs != None:
            whatColumnIs = whatColumnIs.group(0)
            for columna in self._column_list:
                if isinstance(columna, CreateCol):
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

    def validateType(self, columnInfo, defaulValue, process_data):

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
        # -->
        if columnType == 'ColumnsTypes.BIGINT':
            try:
                valorDef = int(valorDef)
                if valorDef < 9223372036854775807 and valorDef > -9223372036854775808:
                    pass
                else:
                    desc = f": out of range value in bigint"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False
            except:
                desc = f": invalid default value to bigint column"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        # -->
        elif columnType == 'ColumnsTypes.BOOLEAN':
            valorDef = str(valorDef)
            if valorDef.lower() == 'True'.lower() or valorDef.lower() == 'False'.lower():
                pass
            else:
                desc = f": invalid default value to boolean column"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        # -->
        elif columnType == 'ColumnsTypes.CHAR':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    desc = f": invalid length in char column, limit is {str(paramOne)}"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False
            else:
                if len(valorDef) > 1:
                    desc = f": invalid length in char column, limit is 1"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False

        # -->
        elif columnType == 'ColumnsTypes.CHARACTER':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    desc = f": invalid len in character column, limit is {str(paramOne)}"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False
            else:
                if len(valorDef) > 1:
                    desc = f": invalid length in char column, limit is 1"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False

        # -->
        elif columnType == 'ColumnsTypes.CHARACTER_VARYING':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    desc = f": invalid len in varying column, limit is {str(paramOne)}"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False
            else:
                pass

        # -->
        elif columnType == 'ColumnsTypes.DATE':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef, '%Y-%m-%d')
            except:
                try:
                    datetime.datetime.strptime(valorDef, '%Y/%m/%d  %H:%M:%S')
                except:
                    desc = f": invalid format in date column"
                    ErrorController().add(17, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False

        # -->
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
                            self._can_create_flag = False
                            return False
                else:
                    strValorDef = str(valorDef)
                    if strValorDef.find('.') != -1:
                        division = strValorDef.split('.')
                        parteEntera = int(division[0])
                        if len(str(parteEntera)) > paramOne and parteEntera != 0:
                            desc = f": overflow in decimal or numeric column"
                            ErrorController().add(6, 'Execution', desc, 0, 0)
                            self._can_create_flag = False
                            return False

            except:
                desc = f": invalid default value in decimal or numeric"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        elif columnType == 'ColumnsTypes.DOUBLE_PRECISION' or columnType == 'ColumnsTypes.REAL':
            try:
                float(valorDef)
            except:
                desc = f": invalid default value in double or real"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        # -->
        elif columnType == 'ColumnsTypes.INTEGER':
            try:
                valorDef = int(valorDef)
                if valorDef < 2147483647 and valorDef > -2147483648:
                    pass
                else:
                    desc = f": default value out of range in integer col"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False
            except:
                desc = f": invalid default value in integer col"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        # -->
        elif columnType == 'ColumnsTypes.INTERVAL':
            pass

        # -->
        elif columnType == 'ColumnsTypes.MONEY':
            try:
                float(valorDef)
            except:
                desc = f": invalid default value in money col"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        # -->
        elif columnType == 'ColumnsTypes.SMALLINT':
            try:
                valorDef = int(valorDef)
                if valorDef < 32727 and valorDef > -37767:
                    pass
                else:
                    desc = f": default value out of range in small col"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False
            except:
                desc = f": invalid default value in smallint col"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        # -->
        elif columnType == 'ColumnsTypes.TEXT':
            try:
                valorDef = str(valorDef)
            except:
                desc = f": invalid default value in text col"
                ErrorController().add(6, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        # -->
        elif columnType == 'ColumnsTypes.TIMESTAMP':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef, '%Y-%m-%d %H:%M:%S')
            except:
                desc = f": invalid format timpestamp, yyyy-mm-dd h:m:s"
                ErrorController().add(17, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        # -->
        elif columnType == 'ColumnsTypes.TIME':
            valorDef = str(valorDef)
            try:
                datetime.datetime.strptime(valorDef, '%H:%M:%S')
            except:
                desc = f": invalid format time, h:m:s"
                ErrorController().add(17, 'Execution', desc, 0, 0)
                self._can_create_flag = False
                return False

        elif columnType == 'ColumnsTypes.VARCHAR':
            valorDef = str(valorDef)
            if paramOne != None:
                if len(valorDef) > paramOne:
                    desc = f":  out of range value in varchar col"
                    ErrorController().add(6, 'Execution', desc, 0, 0)
                    self._can_create_flag = False
                    return False
            else:
                pass

        return True

    def addInherits(self, nameChildTable, nameParentTable):
        typeChecker = TypeChecker()
        tablaPadre = typeChecker.searchTable(
            SymbolTable().useDatabase, nameParentTable)
        tablaHija = typeChecker.searchTable(
            SymbolTable().useDatabase, nameChildTable)

        # La tabla de la que hereda no existe
        if tablaPadre == None:
            desc = f": parent table dont exists"
            ErrorController().add(27, 'Execution', desc, 0, 0)
            self._can_create_flag = False
            return

        for colPar in tablaPadre._colums:
            # Vamos a insertar en la hija
            validarCol = typeChecker.createColumnTable(tablaHija, colPar, 0, 0)
            # Si es una columna repetida entonces no puede crear la tabla
            if validarCol == None:
                self._can_create_flag = False
                return

    def addPKToDB(self, tableCreated):
        indicesPrimarios = []
        typeChecker = TypeChecker()
        tablaToExtract = typeChecker.searchTable(
            SymbolTable().useDatabase, tableCreated)

        for colExt in tablaToExtract._colums:
            if colExt._primaryKey == True:
                indicesPrimarios.append(colExt._number)
        if len(indicesPrimarios) == 0:
            pass
        else:
            DataController().alterAddPK(tableCreated, indicesPrimarios, 0, 0)

    def existsPK(self, tableCreated):
        indicesPrimarios = 0
        typeChecker = TypeChecker()
        tablaToExtract = typeChecker.searchTable(
            SymbolTable().useDatabase, tableCreated)

        for colExt in tablaToExtract._colums:
            if colExt._primaryKey == True:
                indicesPrimarios += 1

        return indicesPrimarios

    def generateHiddenPK(self, nombreTabla):
        typeChecker = TypeChecker()
        tipoEscondido = {
            '_tipoColumna': 'HIDDEN',
            '_paramOne': None,
            '_paramTwo': None
        }
        columnaEscondida = Column('HIDDEN', tipoEscondido)
        columnaEscondida._primaryKey = True
        tableToInsert = typeChecker.searchTable(
            SymbolTable().useDatabase, nombreTabla)
        typeChecker.createColumnTable(tableToInsert, columnaEscondida, 0, 0)
        print('### SE HA GENERADO UNA LLAVE PRIMARIA ESCONDIDA')


class DropTB(Instruction):

    def __init__(self, table_name, tac, noLine, noColumn):
        self._table_name = table_name
        self._noLine = noLine
        self._noColumn = noColumn
        self._tac = ''

    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        typeChecker = TypeChecker()
        typeChecker.deleteTable(self._table_name,
                                self._noLine, self._noColumn)

    def compile(self, instrucction):
        # CREANDO C3D
        temp = ThreeAddressCode().newTemp()
        database_id = SymbolTable().useDatabase
        if database_id is not None:
            ThreeAddressCode().addCode(
                f"{temp} = \"USE {database_id}; {self._tac}\"")
        else:
            ThreeAddressCode().addCode(f"{temp} = \"{self._tac}\"")
        # LLAMANDO A FUNCION PARA ANALIZAR ESTA COCHINADA
        temp1 = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp1} = parse({temp})")


class AlterTable(Instruction):
    '''
        ALTER TABLE cambia una tabla con diversas opciones de alterar
    '''

    def __init__(self, tablaAModificar, listaCambios, tac):
        self._tablaAModificar = tablaAModificar
        self._listaCambios = listaCambios
        self._tac = ''

    def compile(self, instrucction):
        # CREANDO C3D
        temp = ThreeAddressCode().newTemp()
        database_id = SymbolTable().useDatabase
        if database_id is not None:
            ThreeAddressCode().addCode(
                f"{temp} = \"USE {database_id}; {self._tac}\"")
        else:
            ThreeAddressCode().addCode(f"{temp} = \"{self._tac}\"")
        # LLAMANDO A FUNCION PARA ANALIZAR ESTA COCHINADA
        temp1 = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp1} = parse({temp})")

    def process(self, instruction):
        typeChecker = TypeChecker()

        print('')
        print('VAMOS A MODIFICAR LA SIGUIENTE TABLA')
        print(self._tablaAModificar)

        existTable = typeChecker.searchTable(
            SymbolTable().useDatabase, self._tablaAModificar)

        # validate if the table to alter exists
        if existTable == None:
            desc = f": Undefined table in alter table"
            ErrorController().add(27, 'Execution', desc, 0, 0)
            return

        print('y estos son los cambios')
        #  Cambio puede ser un add    (column,check,constraint_unique,foreign_key)
        #                   un alter
        #                   un drop
        #                   un rename
        for cambio in self._listaCambios:
            cambio.process(self._tablaAModificar)

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
        self._tac = ''

    def __repr__(self):
        return str(vars(self))

    def process(self, instruction):

        if isinstance(self._changeContent, CreateCol):
            print('VAMOS A AGREGAR UNA COLUMNA')
            self.agregarCol(self._changeContent, instruction)

        elif isinstance(self._changeContent, Check):
            print('VAMOS A AGREGAR UN CHECK')
            self.agregarCheck(
                self._changeContent._column_condition, instruction)

        elif isinstance(self._changeContent, Constraint):
            print('VAMOS A AGREGAR UN CONSTRAINT_UNIQUE')
            self.agregarUnique(
                self._changeContent._column_condition._column_list, instruction)

        elif isinstance(self._changeContent, ForeignKey):
            print('VAMOS A AGREGAR UN FOREIGN_KEY')
            self.agregarFk(self._changeContent._column_list, self._changeContent._table_name,
                           self._changeContent._table_column_list, instruction)

    def agregarCol(self, columna, nombreTabla):
        typeChecker = TypeChecker()

        tipoFinal = {
            '_tipoColumna': str(columna._type_column._tipoColumna),
            '_paramOne': columna._type_column._paramOne,
            '_paramTwo': columna._type_column._paramTwo
        }

        columnaFinal = Column(columna._column_name, tipoFinal)
        tableToInsert = typeChecker.searchTable(
            SymbolTable().useDatabase, nombreTabla)
        validateCol = typeChecker.createColumnTable(
            tableToInsert, columnaFinal, 0, 0)
        # if return None an error ocurrio
        if validateCol == None:
            return

    def agregarFk(self, listaCols, nombreTabla, listaTablasCols, tablaAAlter):

        typeChecker = TypeChecker()

        # the len of the cols must be de same
        if len(listaCols) != len(listaTablasCols):
            desc = f": cantidad of params in foreign() != "
            ErrorController().add(36, 'Execution', desc, 0, 0)
            return

        existForeingTable = typeChecker.searchTable(
            SymbolTable().useDatabase, nombreTabla)
        tableToAlter = typeChecker.searchTable(
            SymbolTable().useDatabase, tablaAAlter)

        # validate if the foreign table exists
        if existForeingTable == None:
            desc = f": Undefined table in foreign key ()"
            ErrorController().add(27, 'Execution', desc, 0, 0)
            return

        # validate if the columns exists in the foreign table
        for coli in listaTablasCols:
            if typeChecker.searchColumn(existForeingTable, coli) == None:
                desc = f": Undefined col in table in foreign key ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                return

        bandera = False
        for x in range(0, len(listaCols)):
            for columna in tableToAlter.columns:
                if(columna._name == listaCols[x]):
                    bandera = True
                    columna._foreignKey = {
                        '_refTable': nombreTabla,
                        '_refColumn': listaTablasCols[x]
                    }
                    break
            if not bandera:
                desc = f": Undefined column in alter foreign key ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                return
            bandera = False

        typeChecker.writeFile()

    def agregarUnique(self, columnaToUnique, tablaAAlter):
        typeChecker = TypeChecker()
        bandera = False
        tableToAlter = typeChecker.searchTable(
            SymbolTable().useDatabase, tablaAAlter)

        for columna in tableToAlter.columns:
            if(columna._name == columnaToUnique):
                bandera = True
                columna._unique = True
                break

        if not bandera:
            desc = f": Undefined column in alter Unique ()"
            ErrorController().add(26, 'Execution', desc, 0, 0)
            return
        bandera = False
        typeChecker.writeFile()

    def agregarCheck(self, conditionColumn, tablaId):
        typeChecker = TypeChecker()
        bandera = False
        tableToAlter = typeChecker.searchTable(
            SymbolTable().useDatabase, tablaId)

        #                           L (L|D)*
        whatColumnIs = re.search(
            '[a-zA-z]([a-zA-z]|[0-9])*', conditionColumn.alias)

        if whatColumnIs != None:
            whatColumnIs = whatColumnIs.group(0)
            for columna in tableToAlter.columns:
                if(columna._name == whatColumnIs):
                    bandera = True
                    columna._check = conditionColumn.alias
                    break
            if not bandera:
                desc = f": Undefined column in alter check ()"
                ErrorController().add(26, 'Execution', desc, 0, 0)
                return
            bandera = False

        else:
            desc = f": column not given in check()"
            ErrorController().add(26, 'Execution', desc, 0, 0)
            return
        typeChecker.writeFile()


class AlterTableAlter(AlterTable):
    '''
        puedo alterar una columna colocandole not null
        puedo alterar una columna asignandole otro tipo     
    '''

    def __init__(self, changeContent):
        self._changeContent = changeContent
        self._tac = ''

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        # CREANDO C3D
        temp = ThreeAddressCode().newTemp()
        database_id = SymbolTable().useDatabase
        if database_id is not None:
            ThreeAddressCode().addCode(
                f"{temp} = \"USE {database_id}; {self._tac}\"")
        else:
            ThreeAddressCode().addCode(f"{temp} = \"{self._tac}\"")
        # LLAMANDO A FUNCION PARA ANALIZAR ESTA COCHINADA
        temp1 = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp1} = parse({temp})")

    # instrucction trae el valor de la tabla
    def process(self, instrucction):

        if self._changeContent['change'] == 'not_null':
            print('LE VAMOS A DAR UN SET NOT NULL A LA COLUMNA')
            self.agregarNotNull(instrucction, self._changeContent['id_column'])

        elif self._changeContent['change'] == 'type_column':
            print('LE VAMOS A DAR UN CAMBIO DE TIPO A LA COLUMNA')
            self.agregarNuevoTipo(
                instrucction, self._changeContent['id_column'], self._changeContent['type'])

        pass

    def agregarNotNull(self, tablaAMod, colAMod):
        typeChecker = TypeChecker()
        bandera = False
        tableToAlter = typeChecker.searchTable(
            SymbolTable().useDatabase, tablaAMod)

        for columna in tableToAlter.columns:
            if(columna._name == colAMod):
                bandera = True
                columna._notNull = True
                break

        if not bandera:
            desc = f": Undefined column in alter not null ()"
            ErrorController().add(26, 'Execution', desc, 0, 0)
            return
        bandera = False
        typeChecker.writeFile()

    def agregarNuevoTipo(self, tablaAMod, colAMod, nuevoTipo):
        typeChecker = TypeChecker()
        bandera = False
        tableToAlter = typeChecker.searchTable(
            SymbolTable().useDatabase, tablaAMod)

        tipoFinal = {
            '_tipoColumna': str(nuevoTipo._tipoColumna),
            '_paramOne': nuevoTipo._paramOne,
            '_paramTwo': nuevoTipo._paramTwo
        }

        for columna in tableToAlter.columns:
            if(columna._name == colAMod):
                bandera = True
                columna._dataType = tipoFinal
                break

        if not bandera:
            desc = f": Undefined column in alter type ()"
            ErrorController().add(26, 'Execution', desc, 0, 0)
            return
        bandera = False
        typeChecker.writeFile()
        pass


class AlterTableDrop(AlterTable):
    '''
        puedo eliminar una columna
        puedo eliminar un constraint   
    '''

    def __init__(self, changeContent):
        self._changeContent = changeContent
        self._tac = ""

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        # CREANDO C3D
        temp = ThreeAddressCode().newTemp()
        database_id = SymbolTable().useDatabase
        if database_id is not None:
            ThreeAddressCode().addCode(
                f"{temp} = \"USE {database_id}; {self._tac}\"")
        else:
            ThreeAddressCode().addCode(f"{temp} = \"{self._tac}\"")
        # LLAMANDO A FUNCION PARA ANALIZAR ESTA COCHINADA
        temp1 = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp1} = parse({temp})")
        return temp1

    # instrucction trae el valor de la tabla
    def process(self, instrucction):
        if self._changeContent['change'] == 'column':
            print('HARE UNA ELIMINACION DE UNA COLUMNA')
            self.eliminarColumna(instrucction, self._changeContent['id'])

        elif self._changeContent['change'] == 'constraint':
            print(' **DEBERIA ESTAR ELIMINANDO ALGUN CONSTRAINT **')

    def eliminarColumna(self, nombreTabla, nombreColumna):
        typeChecker = TypeChecker()
        bandera = False
        tableToAlter = typeChecker.searchTable(
            SymbolTable().useDatabase, nombreTabla)

        for columna in tableToAlter.columns:
            if(columna._name == nombreColumna):
                bandera = True
                # typeChecker.deleteColumn(tableToAlter,columna,0,0)
                break

        if not bandera:
            desc = f": Undefined column in alter drop column ()"
            ErrorController().add(26, 'Execution', desc, 0, 0)
            return
        bandera = False
        pass


class AlterTableRename(AlterTable):
    '''
        puedo cambiarle el nombre a una tabla  
    '''

    def __init__(self, oldName, newName):
        self._oldName = oldName
        self._newName = newName
        self._tac = ''

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        # CREANDO C3D
        temp = ThreeAddressCode().newTemp()
        database_id = SymbolTable().useDatabase
        if database_id is not None:
            ThreeAddressCode().addCode(
                f"{temp} = \"USE {database_id}; {self._tac}\"")
        else:
            ThreeAddressCode().addCode(f"{temp} = \"{self._tac}\"")
        # LLAMANDO A FUNCION PARA ANALIZAR ESTA COCHINADA
        temp1 = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp1} = parse({temp})")

    # instrucction tiene el valor de la tabla
    def process(self, instrucction):

        typeChecker = TypeChecker()
        bandera = False
        tableToAlter = typeChecker.searchTable(
            SymbolTable().useDatabase, instrucction)

        for columna in tableToAlter.columns:
            if(columna._name == self._oldName):
                bandera = True
                columna._name = self._newName
                break

        if not bandera:
            desc = f": Undefined column in rename column ()"
            ErrorController().add(26, 'Execution', desc, 0, 0)
            return
        bandera = False
        typeChecker.writeFile()
