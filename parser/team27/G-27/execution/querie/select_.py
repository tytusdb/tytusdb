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
from checker import getPrimitivo
import pandas as pd
import copy

class Select(Querie):
    '''
    parametros:
    distinct: recibe un booleano, para saber si viene la palabra reservada distinct
    columnList: puede recibir un singo'*' o una lista de ids de columnas
    tableList: recibe una lista de id de tablas, puede ser una o mas tablas
    '''
     # select columna1, calomna2 from tabla1,tabla2,tabla3,tabla4
     # select columna1, calomna2 from (select columna1, calomna2 from tabla1,tabla2,tabla3,tabla4) group by columna1 having columna1 > 5 order by columna1,columna2
     # where columna1 > columna2
     
    def __init__(self,distinct,columnList,tableList,where,groupby, aggregates, having, orderby,row,column):
        Querie.__init__(self, row, column)
        self.distinct = distinct
        self.columnList = columnList
        self.tableList = tableList
        self.where = where
        self.groupby = groupby
        self.aggregates = aggregates
        self.having = having
        self.orderby = orderby

    def execute(self,environment):
        #declaracion de un select simple a una sola tabla
        tableArray = [] # almacenara los objetos Tabla a los que hace referencia el select
        columnsArray = [] # almacenara las columnas a las que hace referencia el select
        
        #buscamos la base de datos actual
        db_name = environment.getActualDataBase()
        database = copy.copy(environment.readDataBase(db_name))
        
        '''FROM'''
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
        
        '''WHERE'''
        if self.where != None:
            whereArray = []
            for tabla in tableArray:
                whereArray.append({'table':tabla['table'], 'data': []})

            for i in range(len(tableArray[0]['data'])):#POR CADA TUPLA

                for item in tableArray:#DECLARACION EN LA TABLA DE SIMBOLOS PARA CADA TUPLA
                    for index in range(len(item['table'].columns)):
                        environment.guardarVariable(item['table'].columns[index].name, getPrimitivo(item['table'].columns[index].tipo), item['data'][i][index], item['table'].name)
                
                isValid = self.where.execute(environment) #SE CONSULTA SI SE CUMPLE LA CONSULTA WHERE
                environment.vaciarVariables()
                if isValid['value'] == True:#REALIZAR PUSH A CADA TABLA CORRESPONDIENTE DE LA POSICIÓN i 
                    for index in range(len(whereArray)): #RECORREMOS WHEREARRAY Y TABLEARRAY
                        whereArray[index]['data'].append( tableArray[index]['data'][i] )

            tableArray = whereArray
        
        '''GROUP BY'''
        # Recolectar los id con los que se quiere agrupar
        # Hacer diccionario con la estructura {nombreColumna: [todos los valores]}
        # Llamar group by con pandas GROUP BY nombre, pais
        if isinstance(self.groupby, list) and len(tableArray) == 1:
            #input
            dataDict = {}
            for item2 in tableArray:
                index = 0
                for item3 in item2['table'].columns:
                    listaValores = []
                    for item4 in item2['data']:
                        listaValores.append(item4[index])
                    dataDict[item3.name] = listaValores
                    index = index + 1
            encabezados = []
            for v in tableArray[0]['table'].columns:
                encabezados.append(v.name)
            df = pd.DataFrame(tableArray[0]['data'],columns=encabezados)
            grouped = df.groupby(by = self.groupby).groups

            #split
            split = []
            for key,value in grouped.items():
                tempTable = []
                for pk in value:
                    tempTable.append(tableArray[0]['data'][pk])
                split.append(tempTable)

            #Agregate functions
            if self.aggregates !=None:
                for iter in range(len(split)):
                    for op in self.aggregates:
                        newVal = op.execute(split[iter], tableArray[0]['table']) 
                        split[iter] = newVal['data']
            

            #Combine
            data = []
            for t in split:
                data.append(t[0])
            tableArray[0]['data'] = data
                    
            '''HAVING'''
            if self.having != None:
                havingArray = []
                for tabla in tableArray:
                    havingArray.append({'table':tabla['table'], 'data': []})

                for i in range(len(tableArray[0]['data'])):#POR CADA TUPLA

                    for item in tableArray:#DECLARACION EN LA TABLA DE SIMBOLOS PARA CADA TUPLA
                        for index in range(len(item['table'].columns)):
                            v1 = item['table'].columns[index].name
                            v2 =  getPrimitivo(item['table'].columns[index].tipo)
                            v3 = item['data'][i][index]
                            v4 = item['table'].name
                            environment.guardarVariable(v1,v2, v3, v4)

                    isValid = self.having.execute(environment) #SE CONSULTA SI SE CUMPLE LA CONSULTA WHERE
                    environment.vaciarVariables()
                    if isValid['value'] == True:#REALIZAR PUSH A CADA TABLA CORRESPONDIENTE DE LA POSICIÓN i 
                        for index in range(len(havingArray)): #RECORREMOS WHEREARRAY Y TABLEARRAY
                            havingArray[index]['data'].append( tableArray[index]['data'][i] )
                tableArray = havingArray

        '''SELECT'''
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
       
        '''ORDER BY'''
        tabla =  []
        if self.orderby != None:
            dict = {}
            for obj in columnsArray:
                dict[obj['column'].name] = obj['data']
            ff = pd.DataFrame(dict)
            ff.sort_values(by=['nombre', 'id'])
            value = ff.sort_values(by =self.orderby).to_dict('records')
            for item in value:
                dictL = []
                for val in item.items():
                    dictL.append(val[1])
                tabla.append(dictL)
        else:
            for i in range(len(columnsArray[0]['data'])):#tupla
                tupla = []
                for val in columnsArray:
                    tupla.append(val['data'][i])
                tabla.append(tupla)
        return tabla   