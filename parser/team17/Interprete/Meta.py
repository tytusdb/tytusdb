from Interprete.Arbol import Arbol
from StoreManager import jsonMode as dbms
from Interprete.Primitivos.TIPO import TIPO
from enum import Enum
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos

from Interprete.Manejo_errores.ErroresSintacticos import ErroresSintacticos


class HEAD(Enum):
    nameColumn = 0
    typeColumn = 1
    default = 2
    notnull = 3
    null = 4
    unique_name = 5
    fk = 6
    pk_state =  7
    check_name = 8
    check_opizq = 9
    check_op = 10
    check_opder = 11


class FK(Enum):
    name      = 0
    tableRef  = 1
    columnref = 2


# ================================================================================================
# ====================================META========================================================
# ================================================================================================
class Meta:
    '''
        Trata los metadatos en la base de datos
        check, unique, primary key, nameColumn
        headColumns: Se refiera al a posicion cero de cualquier Tabla table[0]
        head: 		 Se refiera a cualquier item de la lista headColumns
        name:		 Se refiera al nombre de la columna
        __Method__ : Detonan un metodo con logica interna

        Inicializar los atributos databaseName y tableName al inicio del execute
        para poder acceder a ellos
    '''

    arbol:Arbol = None
    databaseName = ''
    tableName = ''
    table = []
    headColumns = []
    entorno:Tabla_de_simbolos

    @classmethod
    def existTable(cls, database: str, table: str) -> bool:
        tables_: list = dbms.showTables(database)
        # La Base de datos existe
        if tables_ != None:
            for table_ in tables_:
                if table_ == table:
                    return True
            '''
                ______ _____  _____   ____  _____  
                |  ____|  __ \|  __ \ / __ \|  __ \ 
                | |__  | |__) | |__) | |  | | |__) |
                |  __| |  _  /|  _  /| |  | |  _  / 
                | |____| | \ \| | \ \| |__| | | \ \ 
                |______|_|  \_\_|  \_\\____/|_|  \_\
                borra el print de abajo o comentalo xd
                Descripcion: La %table% no existe en %database% 

            '''
            Error: ErroresSemanticos = ErroresSemanticos("XX5: la tabla "+table+"no existe en la base de datos "+database, 0,
                                                         0,
                                                         'Meta')
            Meta.arbol.ErroresSemanticos.append(Error)
            #print('La tabla no existe en ' + database)
            return False
        else:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            borra el print de abajo o comentalo xd
            Descripcion: La %database% no existe 
            '''
            print('La ' + database + ' de datos no existe')
            Error: ErroresSemanticos = ErroresSemanticos(
                "XX5: no existe  la base de datos " + database, 0,
                0,
                'Meta')
            Meta.arbol.ErroresSemanticos.append(Error)
            return False
    # ================================================================================================

    @classmethod
    def __filterType__(cls, listTypes: list) -> list:
        '''
         Tipo.Varchar  -> Tipo.Cadena
        :param listTypes:
        :return:
        '''
        for i in range(len(listTypes)):
            tipe = listTypes[i]

            #CADENAS
            if tipe == TIPO.TEXT.value:
                listTypes[i] = TIPO.CADENA.value

            elif tipe == TIPO.VARCHAR.value:
                listTypes[i] = TIPO.CADENA.value

            elif tipe == TIPO.CHARACTER_VARYING.value:
                listTypes[i] = TIPO.CADENA.value

            elif tipe == TIPO.DATE.value:
                listTypes[i] = TIPO.CADENA.value

            elif tipe == TIPO.TIME.value:
                listTypes[i] = TIPO.CADENA.value

            elif tipe == TIPO.TIMESTAMP.value:
                listTypes[i] = TIPO.CADENA.value

            elif tipe == TIPO.INTERVAL.value:
                listTypes[i] = TIPO.CADENA.value

            elif tipe == TIPO.CHARACTER.value:
                listTypes[i] = TIPO.CADENA.value

            elif tipe == TIPO.CHAR.value:
                listTypes[i] = TIPO.CADENA.value

            #DECIMAL
            elif tipe == TIPO.REAL.value:
                listTypes[i] = TIPO.DECIMAL.value
            elif tipe == TIPO.DOUBLE_PRECISION.value:
                listTypes[i] = TIPO.DECIMAL.value
            elif tipe == TIPO.MONEY.value:
                listTypes[i] = TIPO.DECIMAL.value
            elif tipe == TIPO.NUMERIC.value:
                listTypes[i] = TIPO.DECIMAL.value

            #ENTERO
            elif tipe == TIPO.BIGINT.value:
                listTypes[i] = TIPO.ENTERO.value
            elif tipe == TIPO.SMALLINT.value:
                listTypes[i] = TIPO.ENTERO.value

            #BOOLEANO
            else:
                pass
                #print(tipe)
                #listTypes[i] = TIPO.CADENA.value


        return listTypes
    # ================================================================================================

    @classmethod
    def getTypeHeadColumns(cls, headColumns) -> list:
        '''
        :param headColumns: lista de encabezados
        :return: lista con los tipos de dato de los encabezados
        '''
        result = []

        for head in headColumns:
            headType = Meta.getTypeByHead(head)
            if Meta.isNumber(headType)==True:
                result.append(headType)
            else:
                #obtener Datos del type
                entorno = Meta.entorno
                result.append(['a', 'b', 'c'])

        result = Meta.__filterType__(result)
        return result
    # ================================================================================================

    @classmethod
    def getValue(cls, value, entorno, arbol) :

        v = value.execute(entorno, arbol)
        Value = value.data

        return Value
    # ==========================================================================================

    @classmethod
    def getTypes(cls, listValues, entorno, arbol) -> list:
        result: list = []
        for v in listValues:
            value = v.execute(entorno, arbol)
            typeValue: int = value.tipo.value
            result.append(typeValue)
        return result
    # ==========================================================================================

    @classmethod
    def getNameColumns(cls, headColumns) -> list:
        '''
        :param headColumns: lista de encabezados
        :return: lista de nombres encabezado
        '''
        result = []
        for i in range(len(headColumns)):
            head = headColumns[i]
            result.append(Meta.getNameByHead(head))
        return result
    # ================================================================================================


    @classmethod
    def getRowByValues(cls, listColumns: list, listvalues: list, headColumns: list):
        newRow = []
        listNumberColumns: list = Meta.getListNumberColumns(listColumns, headColumns)
        # LLenando de null
        for i in range(len(headColumns)): newRow.append('')

        for i in range(len(listNumberColumns)):
            numberColumn = listNumberColumns[i]
            value = listvalues[i]
            newRow[numberColumn] = value

        print(newRow)
        return newRow
    # ================================================================================================

    @classmethod
    def getListNumberColumns(cls, listColumnNames, headColumns) -> list:
        result = []
        headColumnNames = Meta.getNameColumns(headColumns)
        for columnName in listColumnNames:
            for i in range(len(headColumnNames)):
                headColumnName = headColumnNames[i]
                if columnName == headColumnName:
                    result.append(i)

        # result = sorted(result)
        return result
    # ================================================================================================

    @classmethod
    def getNumberColumnByName(cls,columnName,headColumns) -> int:
        headColumnNames = Meta.getNameColumns(headColumns)
        for i in range(len(headColumnNames)):
            headColumnName = headColumnNames[i]
            if columnName == headColumnName:
                return i

        # result = sorted(result)
        return -1
    # ================================================================================================
    @classmethod
    def searchColumn(cls, tableName: str, columnName: str, headColumns: list) -> bool:
        '''
        :param columnName: Nombre de la columna a buscar
        :param headColumns: Columnas que existen en la tabla
        :return:  TRUE -> si lo encuentra , False -> si no lo encuentra
        '''
        for headName in headColumns:
            if headName == columnName:
                return True

        '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            borra el print de abajo o comentalo xd
            Descripcion:'La columna'+columnName+' no existe en la tabla ->'+tableName
        '''
        Error: ErroresSemanticos = ErroresSemanticos(
            "XX5: La columna"+columnName+" no existe en la tabla ->"+tableName, 0,
            0,
            'Use database')
        Meta.arbol.ErroresSemanticos.append(Error)
        print('La columna' + columnName + ' no existe en la tabla ->' + tableName)

        return False
    # ================================================================================================

    @classmethod
    def existColumn(cls, tableName, listcolumn, headColumns) -> bool:
        namesColumns = Meta.getNameColumns(headColumns)
        aux = []
        for namecolumn in listcolumn:
            existColumn: bool = Meta.searchColumn(tableName, namecolumn, namesColumns)
            if existColumn == True:
                if not Meta.contains(namecolumn, aux):
                    aux.append(namecolumn)
                else:
                    '''
                         ______ _____  _____   ____  _____  
                        |  ____|  __ \|  __ \ / __ \|  __ \ 
                        | |__  | |__) | |__) | |  | | |__) |
                        |  __| |  _  /|  _  /| |  | |  _  / 
                        | |____| | \ \| | \ \| |__| | | \ \ 
                        |______|_|  \_\_|  \_\\____/|_|  \_\
                        borra el print de abajo o comentalo xd
                         Descripcion:'la columna: '+namecolumn+'Ya se ha ingresado.'
                    '''
                    Error: ErroresSemanticos = ErroresSemanticos(
                        "XX5: la columna: " + namecolumn + " ya se ha ingresado.", 0,
                        0,
                        'Use database')
                    Meta.arbol.ErroresSemanticos.append(Error)

                    print('la columna: "' + namecolumn + '" ya se ha ingresado.')

                    return False
            else:
                return False

        return True
    # ================================================================================================

    @classmethod
    def contains(cls, value, array) -> bool:
        for item in array:
            if value == item:
                return True
        return False
    # ================================================================================================

    @classmethod
    def checkUnique(cls,listColumn,listValues,headColumns) -> bool:
        '''
        Verifica que no se  repita un campo que tenga con restrccion unique
        :param listColumn:  lista de columnas a evaluar
        :param listValues:  lista de valores de esas columnas
        :param headColumns: encabezado de la tabla
        :return: False->    si se repite algun campo con restriccion unique
        :return: True->     si ningun campo se repite
        '''
        columnsUnique = Meta.getNameColumnsUnique(headColumns)
        fields = Meta.toListFields(listColumn,listValues)

        for i in range(len(columnsUnique)):
            columnUnique = columnsUnique[i]
            for j in range(len(fields)):
                field:Field = fields[j]
                if columnUnique == field.name:
                    valuesColumn = Meta.getColumnsValues(columnUnique)
                    if Meta.contains(field.value,valuesColumn) == True:
                        '''
                             ______ _____  _____   ____  _____  
                            |  ____|  __ \|  __ \ / __ \|  __ \ 
                            | |__  | |__) | |__) | |  | | |__) |
                            |  __| |  _  /|  _  /| |  | |  _  / 
                            | |____| | \ \| | \ \| |__| | | \ \ 
                            |______|_|  \_\_|  \_\\____/|_|  \_\
                            borra el print de abajo o comentalo xd
                            Descripcion:'la columna: '+namecolumn+'Ya se ha ingresado.'
                        '''
                        Error: ErroresSemanticos = ErroresSemanticos(
                            "XX5: El campo:  "+field.name + " No adminite valores repetidos, El valor: " +str(field.value)+" Ya se ha ingresado", 0,
                            0,
                            'Use database')
                        Meta.arbol.ErroresSemanticos.append(Error)
                        print('El campo: \'' +field.name + '\' No adminite valores repetidos, El valor: \'' +str(field.value)+'\' Ya se ha ingresado')
                        return False
        return True
        pass
    # ================================================================================================


   #update column1 = 'ser'


    @classmethod
    def getColumnsValues(cls,columnName) -> list:
        values = []
        columnNumber = Meta.getNumberColumnByName(columnName,Meta.headColumns)
        for i in range(len(Meta.table)):
            rows = Meta.table[i]
            if i > 0:
                for j in range(len(rows)):
                    column = rows[j]
                    if columnNumber == j:
                        values.append(column)

        return values
    # ================================================================================================
    @classmethod
    def checkNotNull(cls, tableName, listcolumn, listvalues , headColumns) -> bool:
        '''
        :param tableName:
        :param listcolumn: Nombre de columnas A evaluar
        :param headColumns: encabezado de la tabla
        :return: False-> si no encuentra todas las columnas con restriccion not null
        :return: True->  si estan todas las columnas con restriccion not null
        '''
        notnullColumns:list = Meta.getNameColumnsNotNull(headColumns)

        for i in range(len(notnullColumns)):
            notnullColumn = notnullColumns[i]
            if Meta.contains(notnullColumn,listcolumn)==False:
                '''
                     ______ _____  _____   ____  _____  
                    |  ____|  __ \|  __ \ / __ \|  __ \ 
                    | |__  | |__) | |__) | |  | | |__) |
                    |  __| |  _  /|  _  /| |  | |  _  / 
                    | |____| | \ \| | \ \| |__| | | \ \ 
                    |______|_|  \_\_|  \_\\____/|_|  \_\
                    borra el print de abajo o comentalo xd
                    Descripcion:'la columna: '+namecolumn+'Ya se ha ingresado.'
                '''
                Error: ErroresSemanticos = ErroresSemanticos(
                    "XX5: La columna: " + notnullColumn + ", es obligatoria para la tabla: "+tableName, 0,
                    0,
                    'Use database')
                Meta.arbol.ErroresSemanticos.append(Error)
                print('La columna: "' + notnullColumn + ', es obligatoria para la tabla: '+tableName)
                return False

        listFields = Meta.toListFields(listcolumn, listvalues)

        for i in range(len(listFields)):
            field:Field = listFields[i]
            if  Meta.isNotNullByName(field.name) == True:
                if field.value == '':
                    '''
                         ______ _____  _____   ____  _____  
                        |  ____|  __ \|  __ \ / __ \|  __ \ 
                        | |__  | |__) | |__) | |  | | |__) |
                        |  __| |  _  /|  _  /| |  | |  _  / 
                        | |____| | \ \| | \ \| |__| | | \ \ 
                        |______|_|  \_\_|  \_\\____/|_|  \_\
                        borra el print de abajo o comentalo xd
                        Descripcion:'la columna: '+namecolumn+'Ya se ha ingresado.'
                    '''
                    Error: ErroresSemanticos = ErroresSemanticos(
                        "XX5: El campo: " +field.name+ ", de la tabla: "+tableName+"  no puede venir con ' ", 0,
                        0,
                        'Use database')
                    Meta.arbol.ErroresSemanticos.append(Error)
                    print('El campo: ' +field.name+ ', de la tabla: '+tableName+'  no puede venir con \'\' ')
                    return False
        return  True
    # ================================================================================================

    @classmethod
    def checkCheck(cls, tableName, listcolumn, listvalues , headColumns) -> bool:
        '''
        :param tableName:
        :param listcolumn: Nombre de columnas A evaluar
        :param headColumns: encabezado de la tabla
        :return: False-> si no encuentra todas las columnas con restriccion not null
        :return: True->  si estan todas las columnas con restriccion not null
        '''
        result = False

        columnsCheck = Meta.getNameColumnsCheck(headColumns)
        fields = Meta.toListFields(listcolumn,listvalues)

        for i in range(len(columnsCheck)):
            columnCheck = columnsCheck[i]
            if Meta.contains(columnsCheck,listcolumn) == True:
                head:str = Meta.getHeadByName(columnCheck)
                headStruct = head.split(',')

                opizq    = headStruct[HEAD.check_opizq.value]
                opder    = headStruct[HEAD.check_opder.value]
                operando = headStruct[HEAD.check_op.value]

                #Obteniendo valor de opizq
                if Meta.existColumn(tableName,[opizq],headColumns)==True:
                    for field in fields:
                        if opizq == field.name:
                            opizq = field.value

                #Obteniendo valor de opder
                if Meta.existColumn(tableName,[opder],headColumns)==True:
                    for field in fields:
                        if opizq == field.name:
                            opder = field.value


                if operando =='>':
                    result = opizq > opder
                    return result
                elif operando == '<':
                    result = opizq < opder
                    return result
                elif operando =='==':
                    result = (opizq == opder)
                    return result
                elif operando == '<=':
                    result = opizq <= opder
                    return result
                elif operando == '>=':
                    result = opizq >= opder
                    return result
                else:
                    return False


        return result
   # ================================================================================================

    @classmethod
    def getNameColumnsDefault(cls,headColumns) -> list:
        '''
        :param headColumns:Encabezados de una tabla
        :return: lista con las columnas con restriccion Default
        '''
        result = []
        for head in headColumns:
            if  Meta.isDefaultbyHead(head) == True:
                name = Meta.getNameByHead(head)
                result.append(name)
        return result
    # ================================================================================================
    @classmethod
    def getNameColumnsUnique(cls,headColumns) -> list:
        '''
        :param headColumns:Encabezados de una tabla
        :return: lista con las columnas con restriccion notnull
        '''
        result = []
        for head in headColumns:
            if  Meta.isUniqueByHead(head) == True:
                name = Meta.getNameByHead(head)
                result.append(name)
            elif Meta.isPkByHead(head) == True:
                name = Meta.getNameByHead(head)
                result.append(name)

        return result
    # ================================================================================================

    @classmethod
    def getNameColumnsCheck(cls, headColumns) -> list:
        '''
        :param headColumns:Encabezados de una tabla
        :return: lista con las columnas con restriccion notnull
        '''
        result = []
        for i in range(len(headColumns)):
            head = headColumns[i]
            if  Meta.isCheckByHeAD(head) == True:
                name = Meta.getNameByHead(head)
                result.append(name)
        return result
    # ================================================================================================

    @classmethod
    def getNameColumnsNotNull(cls, headColumns) -> list:
        '''
        :param headColumns:Encabezados de una tabla
        :return: lista con las columnas con restriccion notnull
        '''
        result = []
        for i in range(len(headColumns)):
            head = headColumns[i]
            if  Meta.isNotNullByHead(head) == True:
                name = Meta.getNameByHead(head)
                result.append(name)
            elif Meta.isPkByHead(head) == True:
                name = Meta.getNameByHead(head)
                result.append(name)
        return result
    # ================================================================================================

    @classmethod
    def isDefaultbyHead(cls, head) -> bool:
        headlist = head.split(',')
        uniqueState: str = str(headlist[HEAD.default.value])
        if uniqueState=='':
            return  False

        return True
    # ================================================================================================

    @classmethod
    def isPkByHead(cls, head) -> bool:
        headlist = head.split(',')
        pkState:int = int(headlist[HEAD.pk_state.value])
        if pkState == 0:
            return  False
        return True
    # ================================================================================================

    @classmethod
    def isUniqueByHead(cls, head) -> bool:
        headlist = head.split(',')
        uniqueState: str = str(headlist[HEAD.unique_name.value])
        if uniqueState=='':
            return  False
        return True
    # ================================================================================================

    @classmethod
    def isCheckByHeAD(cls, head) -> bool:
        headlist = head.split(',')
        check: str = str(headlist[HEAD.check_name.value])
        if check=='':
            return  False
        return True
    # ================================================================================================
    @classmethod
    def isNotNullByHead(cls, head) -> bool:
        headlist = head.split(',')
        notnull: int = int(headlist[HEAD.notnull.value])
        if notnull==1:
            return  True
        return False
    # ================================================================================================

    @classmethod
    def getDefaultByHead(cls, head) -> str:
        headlist = head.split(',')
        default:str = str(headlist[HEAD.default.value])
        return default
    # ================================================================================================

    @classmethod
    def isUniqueByName(cls,nameField) -> bool:
        head = Meta.getHeadByName(nameField)
        return Meta.isUniqueByHead(head)
    # ================================================================================================

    @classmethod
    def isDefaultByName(cls,nameField) -> bool:
        head = Meta.getHeadByName(nameField)
        return Meta.isUniqueByHead(head)
    # ================================================================================================

    @classmethod
    def isNotNullByName(cls,nameField) -> bool:
        '''
            Require que inicialices
        :param nameField:
        :return:
        '''
        head = Meta.getHeadByName(nameField)
        return Meta.isNotNullByHead(head)
    # ================================================================================================

    @classmethod
    def getDefaultByName(cls, nameField) -> str:
        result = ''
        head = Meta.getHeadByName(nameField)
        return Meta.getDefaultByHead(head)
    # ================================================================================================

    @classmethod
    def getHeadByName(cls, nameField) -> str:
        result = ''
        table: list = dbms.extractTable(Meta.databaseName,Meta.tableName)
        headColumns = table[0]
        for head in headColumns:
            headName = Meta.getNameByHead(head)
            if headName == nameField:
                result = head
                return result
        return result
    # ================================================================================================

    @classmethod
    def getNameByHead(cls, head) -> str:
        '''
        :param head:
        :return:  el nombre de la cabecera
        '''
        headlist = head.split(',')
        headName = str(headlist[HEAD.nameColumn.value])
        return headName
    # ================================================================================================

    @classmethod
    def getTypeByHead(cls, head) -> any:
        '''
        :param head:
        :return: tipo de dato de ese campo
        '''
        headlist = head.split(',')
        try:
            tipo = int(headlist[HEAD.typeColumn.value])
            return tipo
        except:
            tipo = str(headlist[HEAD.typeColumn.value])
            return tipo

    # ================================================================================================

    @classmethod
    def toListFields(cls, listcolumn, listvalues) -> list:
        result = []
        for i in range(len(listcolumn)):
            columnName = listcolumn[i]
            value = listvalues[i]
            result.append(Field(columnName,value))
        return result
    # ================================================================================================

    @classmethod
    def setDefaults(cls, listcolumn:list, listvalues:list) -> list:
        listDefault = Meta.getNameColumnsDefault(Meta.headColumns)

        for defaultColumn in listDefault:
            if Meta.contains(defaultColumn,listcolumn) == False:
                defaultValue = Meta.getDefaultByName(defaultColumn)
                listcolumn.append(defaultColumn)
                listvalues.append(defaultValue)

        listFields = Meta.toListFields(listcolumn,listvalues)

        for i in range(len(listFields)):
            field:Field = listFields[i]
            if field.value == '':
                defaultValue = Meta.getDefaultByName(field.name)
                listvalues[i] = defaultValue

        return  [listcolumn,listvalues]
    # ================================================================================================

    @classmethod
    def TypesCompare(cls, headColumns, listValues, entorno, arbol) -> bool:
        result: bool = True
        typeColumns = Meta.getTypeHeadColumns(headColumns)
        typeValues = Meta.getTypes(listValues, entorno, arbol)
        nameColumns = Meta.getNameColumns(headColumns)

        for i in range(len(typeColumns)):
            nameColumn = nameColumns[i]
            typeValue = typeValues[i]
            typeColumn = typeColumns[i]

            # Validacion Type
            if Meta.isNumber(typeColumn)==False:
                objectType = typeColumns[i]
                value = Meta.getValue(listValues[i],entorno,arbol)

                if Meta.contains(value,objectType)==False:
                    '''
                      ______ _____  _____   ____  _____  
                     |  ____|  __ \|  __ \ / __ \|  __ \ 
                     | |__  | |__) | |__) | |  | | |__) |
                     |  __| |  _  /|  _  /| |  | |  _  / 
                     | |____| | \ \| | \ \| |__| | | \ \ 
                     |______|_|  \_\_|  \_\\____/|_|  \_\
                    borra el print de abajo o comentalo xd
                    Descripcion: la columna: %nameColumn% No acepta el %value.tipo%
                    '''
                    #tipo:str = Meta.getTypeByHead(headColumns[i])
                    #Error: ErroresSemanticos = ErroresSemanticos(
                    #    "XX5:la columna: \'" + nameColumn + "\' Solo acepta valoes del tipo "+tipo, 0,
                    #    0,
                    #    'Use database')
                    #Meta.arbol.ErroresSemanticos.append(Error)

                    #print(' la columna: \'' + nameColumn + '\' Solo acepta valores del tipo: ',tipo)

                    result = True

            else:

                if typeColumn != typeValue:
                    '''
                      ______ _____  _____   ____  _____  
                     |  ____|  __ \|  __ \ / __ \|  __ \ 
                     | |__  | |__) | |__) | |  | | |__) |
                     |  __| |  _  /|  _  /| |  | |  _  / 
                     | |____| | \ \| | \ \| |__| | | \ \ 
                     |______|_|  \_\_|  \_\\____/|_|  \_\
                    borra el print de abajo o comentalo xd
                    Descripcion: la columna: %nameColumn% No acepta el %value.tipo%
                    '''
                    Error: ErroresSemanticos = ErroresSemanticos(
                        "XX5:la columna: " + nameColumn + " No acepta el tipo ingresado", 0,
                        0,
                        'Use database')
                    Meta.arbol.ErroresSemanticos.append(Error)
                    print(' la columna: \'' + nameColumn + '\' No acepta el tipo ingresado' )
                    result = False

        return result
    # ================================================================================================

    @classmethod
    def isNumber(cls,value):
        try:
            int(value)
            return True
        except:
            return False
    # ================================================================================================

    @classmethod
    def getPksIndex(cls, headcolumns) -> list:
        '''
            Devuelve el indice de las columnas que son llaves primarias
            - SI PKS ES VACIA quiere decir que no hay llaves primarias en la tabla y por tanto se manejan por indice
            - SI PKS TIENE VALORES quiere decir que si hay llaves primarias en las tablas y se manejan por su valor
        '''
        pks = []
        for index in range(len(headcolumns)):
            row = headcolumns[index].split(',')
            if row[7] == '1':
                pks.append(index)
        return pks



# ================================================================================================
# ====================================Field========================================================
# ================================================================================================


class Field():

    def __init__(self,namefield , value):
        self.name:str = namefield
        self.value = value

