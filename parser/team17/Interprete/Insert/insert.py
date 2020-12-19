from Interprete.Insert.InsertReturn import InsertReturn
from Interprete.Insert.HeadTYpes import HEAD
from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as j
from Interprete.Primitivos.TIPO import TIPO

#############################
# Patrón intérprete: INSERT #
#############################

# UPDATE: modificar atributos de una tabla

class Insert(NodoArbol):

    def __init__(self,tableName,listColumn,listValues,line,column):
        super().__init__(line, column)
        self.tableName:str   = tableName
        self.listColumn:list = listColumn
        self.listValues:list = listValues


    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        databaseName = entorno.getBD()
        if entorno.BDisNull() == True:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            borra el print de abajo o comentalo xd
            Descripcion: BD %databaseName% no existe ("BD " + databaseName + " no existe")
            '''
            print('BD'+databaseName+'no existe')
            return

        if not self.listColumn:
            self.insertNormal(databaseName,entorno,arbol)
        else:
            self.insertWithListId(databaseName,entorno,arbol)
    #================================================================================================

    # insert into countries values('COL','Colombia','Sur America',0256);
    def insertNormal(self,databaseName:str,entorno,arbol):

        if self.exist(databaseName,self.tableName)== True:

            table:list = j.extractTable(databaseName,self.tableName)
            headColumns = table[0]

            if self.checkLen(headColumns,self.listValues)==True and \
               self.TypesCompare(headColumns,self.listValues,entorno,arbol)==True:

                values:list = self.getValues(self.listValues,entorno,arbol)

                j.insert(databaseName, self.tableName,values)
                print(self.tableName, '1 una fila a sido afectada')

    # 	   | INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
    def insertWithListId(self,databaseName:str,entorno,arbol):

        if self.exist(databaseName,self.tableName)== True and \
            self.checkLen(self.listColumn,self.listValues)==True  :
            table:list = j.extractTable(databaseName,self.tableName)
            headColumns = table[0]

            if self.existColumn(self.tableName, self.listColumn,headColumns):

                #todo:3. obtener solo las columnas indicadas
                #todo:4. Se pondra '' como valor nulo
                #todo:1. verficar tipo de datos
                #todo:2. verificar resctriccion  unique
                #todo:5. Usar Default si no viene
                #todo:6. verificar restriccion check


                listvalues:list = self.getValues(self.listValues,entorno,arbol)
                newRow = self.getRowByValues(self.listColumn,listvalues,headColumns)

                j.insert(databaseName, self.tableName,newRow)
                print(self.tableName, '1 una fila a sido afectada')

                pass
    #================================================================================================

    def contains(self,value,array) -> bool:
        for item in array:
            if value == item:
                return True
        return  False
    #================================================================================================


    def getRowByValues(self,listColumns:list,listvalues:list,headColumns:list):
        newRow = []
        listNumberColumns:list = self.getListNumberColumns(listColumns,headColumns)
        # LLenando de null
        for i in range(len(headColumns)):
            newRow.append('')

        for i in range(len(listNumberColumns)):
            numberColumn =listNumberColumns[i]
            value = listvalues[i]
            newRow[numberColumn] = value

        #print(newRow)
        return newRow
    #================================================================================================

    def getListNumberColumns(self,listColumnNames,headColumns) ->list:
        result = []
        headColumnNames = self.getNameColumns(headColumns)
        for columnName in listColumnNames:
            for i in range(len(headColumnNames)):
                headColumnName = headColumnNames[i]
                if columnName == headColumnName:
                    result.append(i)

        #result = sorted(result)
        return result
    #================================================================================================

    def searchColumn(self,tableName:str,columnName:str,headColumns:list) -> bool:
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
        print('La columna'+columnName+' no existe en la tabla ->'+tableName)

        return  False
    #================================================================================================

    def getNameColumns(self,headColumns) -> list:
        '''
        :param headColumns: lista de encabezados
        :return: lista de nombres encabezado
        '''
        result = []
        for  i in range(len(headColumns)):
            head   = headColumns[i].split(',')
            headName:str = str(head[HEAD.nameColumn.value])
            result.append(headName)
        return result
    #================================================================================================


    def getTypeHeadColumns(self, headColumns) -> list:
        '''
        :param headColumns: lista de encabezados
        :return: lista con los tipos de dato de los encabezados
        '''
        result = []
        for  i in range(len(headColumns)):
            head   = headColumns[i].split(',')
            headName:int = int(head[HEAD.typeColumn.value])
            result.append(headName)

        result = self.filterType(result)
        return result
    #================================================================================================

    def existColumn(self,tableName,listcolumn,headColumns) -> bool:

        namesColumns = self.getNameColumns(headColumns)
        aux  = []
        for namecolumn in listcolumn:
            existColumn:bool = self.searchColumn(tableName,namecolumn,namesColumns)

            if existColumn == True:
                if  not self.contains(namecolumn,aux):
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
                    print('la columna: "'+namecolumn+'" ya se ha ingresado.')

                    return False
            else:
                return False

        return True
    #================================================================================================

    def getTypes(self,listValues,entorno,arbol) -> list:
        result:list = []
        for v in listValues:
            value = v.execute(entorno, arbol)
            typeValue:int  = value.tipo.value
            result.append(typeValue)

        return result
    #================================================================================================

    def filterType(self,listTypes:list) -> list:
        for i in range(len(listTypes)):
            tipe = listTypes[i]
            if  tipe == TIPO.TEXT.value:
                listTypes[i] = TIPO.CADENA.value
            if  tipe == TIPO.VARCHAR.value:
                listTypes[i] = TIPO.CADENA.value
            if  tipe == TIPO.CHARACTER_VARYING.value:
                listTypes[i] = TIPO.CADENA.value
            pass
        return listTypes
    #================================================================================================

    def getValues(self,listValues,entorno,arbol) -> list:
        result:list = []
        for v in listValues:
            value = v.execute(entorno, arbol).data
            result.append(value)
        return result
    #================================================================================================

    def checkLen(self,columns:list,values:list) -> bool:
        lengthColumn = len(columns)
        lengthValues = len(values)

        if lengthValues > lengthColumn:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            borra el print de abajo o comentalo xd
            Descripcion: Insert Demasiados Parametros
            '''
            print('Hay Mas valores de los permitidos')
            return False
        elif lengthValues < lengthColumn:
            '''
              ______ _____  _____   ____  _____  
             |  ____|  __ \|  __ \ / __ \|  __ \ 
             | |__  | |__) | |__) | |  | | |__) |
             |  __| |  _  /|  _  /| |  | |  _  / 
             | |____| | \ \| | \ \| |__| | | \ \ 
             |______|_|  \_\_|  \_\\____/|_|  \_\
            borra el print de abajo o comentalo xd
            Descripcion: Faltan parametros en el insert
            '''
            print('Faltan valores para ingresar')
            return  False
        #si no es mayor ni tampoco menor entonces es igual
        else:
            return  True
    #================================================================================================

    #todo: Mejorar metodo separar en varios metodos
    def TypesCompare(self,headColumns,listValues,entorno,arbol) -> bool:

        result:bool = True

        typeColumns = self.getTypeHeadColumns(headColumns)
        typeValues  = self.getTypes(listValues,entorno,arbol)
        nameColumns = self.getNameColumns(headColumns)
        for i in range(len(typeColumns)):
            nameColumn:str = nameColumns[i]
            typeColumn:int = typeColumns[i]
            typeValue:int  = typeValues[i]

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
                print(' la columna: '+nameColumn+' No acepta el '+typeValue.tipo)
                result = False

        return  result
    #================================================================================================

    def exist(self,database:str,table:str) -> bool:
        tables_: list = j.showTables(database)
        #La Base de datos existe
        if tables_!=None:
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
            print('La tabla no existe en ' + database)
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
            print('La '+database+' de datos no existe')
            return False
    #================================================================================================



    def obtenerIndex(self, tabla:list, index:str):
        encabezados = tabla[0]
        for i in len(encabezados):
            if encabezados[i] == index:
                return i
    #================================================================================================



#================================================================================================
#================================================================================================
#========================================headBoard========================================================
#================================================================================================
#================================================================================================


class HeadBoard:
    pass