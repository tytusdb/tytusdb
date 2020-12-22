import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/execution/querie')
sys.path.append('../tytus/storage')
sys.path.append('../tytus/parser/team27/G-27/TypeChecker')
from querie import * 
from environment import *
from table import *
from column import *
from typ import *
from storageManager import jsonMode as admin
from checker import check

class Select(Querie):
    '''
    parametros:
    distinct: recibe un booleano, para saber si viene la palabra reservada distinct
    columnList: puede recibir un singo'*' o una lista de ids de columnas
    tableList: recibe una lista de id de tablas, puede ser una o mas tablas
    '''
     # select columna1, calomna2 from tabla1,tabla2,tabla3,tabla4
     # where columna1 > columna2
     
    def __init__(self,distinct,columnList,tableList,where,row,column):
        Querie.__init__(self, row, column)
        self.distinct = distinct
        self.columnList = columnList
        self.tableList = tableList

    def execute(self,environment):
        #declaracion de un select simple a una sola tabla
        tableArray = [] # almacenara los objetos Tabla a los que hace referencia el select
        columnsArray = [] # almacenara las columnas a las que hace referencia el select
        
        #buscamos la base de datos actual
        db_name = environment.getActualDataBase()
        database = environment.readDataBase(db_name)

        # recorremos el tableList para ver si todas las tablas pertenecen a la base de datos y las almacenamos en table Array
        for item in self.tableList:
            table = database.getTable(item)
            if table == None:
                if len(self.tableList) > 1:
                    return {'Error': 'La tabla: '+item+' no existe en la base de datos', 'Linea':self.row, 'Columna': self.column}
                else:
                    return {'Error': 'La tabla: '+item+' no existe en la base de datos', 'Linea':self.row, 'Columna': self.column}
            val = admin.extractTable(db_name,table.name)
            if  val == None:
                return {'Error': 'La tabla: '+item+' no existe en la base de datos', 'Linea':self.row, 'Columna': self.column}

            valor = {'table': table,'data': val}
            tableArray.append(valor)
        
         
        



        # ahora recorremos el columnList para ver si todas las columnas existen en las tablas especificadas
        if isinstance(self.columnList,list):
            exist = False
            for item in self.columnList:
                for item2 in tableArray:
                    index = 0
                    for item3 in item2['table'].columns:
                        if item3.name == item:
                            exist = True
                            listaValores =[]
                            for item4 in item2['data']:
                                listaValores.append(item4[index])
                            columnaSelect = {'column':item3,'data':listaValores}
                            columnsArray.append(columnaSelect)
                            break
                        index = index + 1
                    if exist == True:
                        break
                if exist == False:
                    return {'Error': 'La columna: '+item+ ' no existe en ninguna de las tablas especificadas', 'Linea':self.row, 'Columna': self.column}
                    break
            
        else:
            if self.columnList == '*':
                for item in self.columnList:
                    for item2 in tableArray:
                        index = 0
                        for item3 in item2['table'].columns:
                            listaValores = []
                            for item4 in item2['data']:
                                listaValores.append(item4[index])
                            columnaSelect ={'column':item3,'data':listaValores}
                            columnsArray.append(columnaSelect)
                            index = index + 1

            else:
                return {'Error': 'Error desconocido en el select', 'Linea':self.row, 'Columna': self.column}

        result = ''
        for item in columnsArray:
            result += item['column'].name+': '
            for item2 in item['data']:
                if isinstance(item2,str):
                    result += item2+','
                else:
                    result += str(item2)+','
            result+='\n'
        return result







       


   
            