from Interprete.Insert.InsertReturn import InsertReturn
from Interprete.Meta import HEAD
from Interprete.Meta import Meta
from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as j
from Interprete.Primitivos.TIPO import TIPO
from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos


from enum import Enum

#############################
# Patrón intérprete: INSERT #
#############################

# UPDATE: modificar atributos de una tabla
class Insert(NodoArbol):

    def __init__(self, tablename, listcolumn, listvalues, line, column):
        super().__init__(line, column)
        self.tableName: str = tablename
        self.listColumn: list = listcolumn
        self.listValues: list = listvalues
        self.arbol:Arbol

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        databaseName       = entorno.getBD()
        Meta.tableName     = self.tableName
        Meta.databaseName  = databaseName
        Meta.arbol         = arbol
        self.arbol         = arbol
        Meta.entorno       = entorno


        if entorno.BDisNull():
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
            Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error db is not exist",
                                                         self.linea,
                                                         self.columna,
                                                         'Insert')
            arbol.ErroresSemanticos.append(Error)
            print('BD' + databaseName + 'no existe')
            return

        if not self.listColumn:
            self.insertNormal(databaseName, entorno, arbol)
        else:
            self.insertWithListId(databaseName, entorno, arbol)
    # ================================================================================================

    # insert into countries values('COL','Colombia','Sur America',0256);
    def insertNormal(self, databaseName: str, entorno, arbol):

        if Meta.existTable(databaseName, self.tableName) == True:

            table: list = j.extractTable(databaseName, self.tableName)
            Meta.headColumns   = table[0]
            Meta.table         = table
            headColumns = table[0]
            listvalues: list = self.getValues(self.listValues, entorno, arbol)
            listcolum = Meta.getNameColumns(headColumns)

            #definimos los valores por default
            defaults = Meta.setDefaults(listcolum,listvalues)
            self.listColumn = defaults[0]
            listvalues      = defaults[1]


            if self.checkLen(headColumns, self.listValues) == True:
                if Meta.checkNotNull(self.tableName, listcolum, listvalues, headColumns) == True:
                    if Meta.checkUnique(listcolum, listvalues, headColumns) == True:
                        if Meta.TypesCompare(headColumns, self.listValues, entorno, arbol) == True:

                            values: list = self.getValues(self.listValues, entorno, arbol)
                            j.insert(databaseName, self.tableName, values)
                            print(self.tableName, '1 una fila a sido afectada')




    #| INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
    def insertWithListId(self, databaseName: str, entorno, arbol):

        #1. Verificamos si la tabla existe
        #2. Obtenemos los valores por default si no vinieran
        #3. Verificamos la longitud de los valores tiene que ser igual al de las columnas
        #4. Verificamos Que las columnas existan
        #4. Verificamos que no venga nula una columna con restriccion unique

        if Meta.existTable(databaseName, self.tableName) == True and \
                self.checkLen(self.listColumn, self.listValues) == True:

            table: list = j.extractTable(databaseName, self.tableName)
            Meta.headColumns   = table[0]
            Meta.table         = table
            headColumns = table[0]
            listvalues: list = self.getValues(self.listValues, entorno, arbol)

            #definimos los valores por default
            defaults = Meta.setDefaults(self.listColumn,listvalues)
            self.listColumn = defaults[0]
            listvalues      = defaults[1]

            if  Meta.existColumn(self.tableName, self.listColumn, headColumns) == True :
                if Meta.checkNotNull(self.tableName, self.listColumn,listvalues, headColumns) == True  :
                    if Meta.checkUnique(self.listColumn,listvalues,headColumns) == True:

                        heads = []
                        for column in self.listColumn:
                            head = Meta.getHeadByName(column)
                            heads.append(head)


                        if Meta.TypesCompare(heads,self.listValues , entorno, arbol) == True:


                            newRow = Meta.getRowByValues(self.listColumn, listvalues, headColumns)
                            j.insert(databaseName, self.tableName, newRow)

                            arbol.console.append('1 una fila a sido afectada \n')
                            print(self.tableName, '1 una fila a sido afectada')
    # ================================================================================================

    def getValues(self, listValues, entorno, arbol) -> list:
        result: list = []
        for v in listValues:
            try:
                value = v.execute(entorno, arbol).data
                result.append(value)
            except:
                pass
        return result
    # ================================================================================================

    def checkLen(self, columns: list, values: list) -> bool:
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
            Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error hay mas parametros en el insert", self.linea,
                                                         self.columna,
                                                         'Insert')
            self.arbol.ErroresSemanticos.append(Error)
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
            Error: ErroresSemanticos = ErroresSemanticos("XX00: internal_error Faltan parametros en el insert", self.linea,
                                                         self.columna,
                                                         'Insert')
            self.arbol.ErroresSemanticos.append(Error)
            print('Faltan valores para ingresar')
            return False
        # si no es mayor ni tampoco menor entonces es igual
        else:
            return True
    # ================================================================================================


