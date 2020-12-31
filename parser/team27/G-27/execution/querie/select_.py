from typing import cast
from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin
from TypeChecker.checker import check
from TypeChecker.checker import getPrimitivo
import pandas as pd
import copy

class Select(Querie):
     # distinct-> Boolean
     # columnnList -> [{'name':idColumna, 'father':tablaPadre, 'as': apodo},...]
     # tablelist -> [{'id':idTabla, 'as': apodo},...]
     # where -> Expression
     # groupby -> [id,id,...]
     # aggregates -> [aggregateFunction, ...]
     # having -> Expression
     # orderBy -> [ {'id':idColumna, 'father':idTabla, 'asc':True|False, 'nulls':first|last}, ...] asc si no viene True

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
        #declaracion de un select simple a una sola tabla SELECT C1 FROM (SELECT ID, C1, NOMBRE FROM TABLA)
        tableArray = [] # almacenara los objetos Tabla a los que hace referencia el select
        columnsArray = [] # almacenara las columnas a las que hace referencia el select
        
        #buscamos la base de datos actual
        db_name = environment.getActualDataBase()
        database = copy.copy(environment.readDataBase(db_name))
        
        #devolucion 
        tabla =  []
        '''FROM'''
        self.FROM(db_name,database,tableArray,environment)
    
        '''WHERE'''
        tableArray = self.WHERE(tableArray,environment)
        
        '''GROUP BY'''
        tableArray = self.GROUPBY(tableArray,environment)

        '''SELECT'''
        self.SELECT(tableArray,columnsArray)
       
        '''ORDER BY'''
        self.ORDERBY(columnsArray,tabla)

        '''AREA DE RETORNO'''
        #Lleno metadata de columnas seleccionadas
        columnas = []
        if self.columnList != '*':
            for val in columnsArray:
                idColumna = val['column'].name
                for id in self.columnList:
                    nombre = id['name']
                    if nombre== idColumna:
                        columnas.append(val) 
                        break
        else:
            for val in columnsArray:
                columnas.append(val) 
                      
        
        #Lleno columnas de funciones de agregado en la metadata 
        if self.aggregates != None:
            for function in self.aggregates:
                columnas.append(function.getColumn())       
        resultTable = Table('QUERY',columnas,None)
        return {'table':resultTable,'data':tabla }

    #===================================================== F R O M ==========================================================
    def FROM(self, db_name, database, tableArray, environment):
        # recorremos el tableList para ver si todas las tablas pertenecen a la base de datos y las almacenamos en table Array
        if isinstance(self.tableList,list): 
            for item in self.tableList:
                table = database.getTable(item['name'])
                if table == None:                
                    if len(self.tableList) > 1:
                        return {'Error': 'La tabla: '+item['name']+' no existe en la base de datos', 'Linea':self.row, 'Columna': self.column}
                    else:
                        return {'Error': 'La tabla: '+item['name']+' no existe en la base de datos', 'Linea':self.row, 'Columna': self.column}
                val = admin.extractTable(db_name,table.name)
                if  val == None:
                    return {'Error': 'La tabla: '+item['id']+' no existe en la base de datos', 'Linea':self.row, 'Columna': self.column}
                table.alias = item['as']
                valor = {'table': table,'data': val}
                tableArray.append(valor)
        elif isinstance(self.tableList, Select):
            tableArray.push(self.tableList.execute(environment))
        else:
            return {'Error':'Formato no válido en el FROM', 'Fila':self.row, 'Columna':self.column}
    

    #==================================================== W H E R E ===========================================================
    def WHERE(self,tableArray,environment):
        if self.where != None:
            whereArray = []
            for tabla in tableArray:#Se crea una copia del from pero sin tuplas
                whereArray.append({'table':tabla['table'], 'data': []})

            for i in range(len(tableArray[0]['data'])):#Obtengo un indice para cada registro

                #Preparo el entorno con las variables para la solución de cada tupla.
                for item in tableArray:#Por cada tabla en los datos eleccionados.
                    padre = item['table'].name
                    if item['table'].alias !=None:
                        padre = item['table'].alias
                    
                    for index in range(len(item['table'].columns)):#Por cada columna en la tabla
                        environment.guardarVariable(item['table'].columns[index].name, getPrimitivo(item['table'].columns[index].tipo), item['data'][i][index], padre)
                
                isValid = self.where.execute(environment) #SE CONSULTA SI SE CUMPLE LA CONSULTA WHERE
                environment.vaciarVariables()
                if isValid['value'] == True:#REALIZAR PUSH A CADA TABLA CORRESPONDIENTE DE LA POSICIÓN i 
                    for index in range(len(whereArray)): #RECORREMOS WHEREARRAY Y TABLEARRAY
                        whereArray[index]['data'].append( tableArray[index]['data'][i] )
            return whereArray
        return tableArray
    
    #===================================================== G R O U P   B Y ========================================================
    def GROUPBY(self,tableArray,environment):
        if self.groupby == None:
            return tableArray
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

            print(data)        
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
            return tableArray
        else:
            return { 'Error':'No se puede agrupar sobre multiples tablas', 'Fila': self.row, 'Columna': self.column }

    #==================================================== S E L E C T ==========================================================
    def SELECT(self,tableArray,columnsArray):
        # ahora recorremos el columnList para ver si todas las columnas existen en las tablas especificadas
        if isinstance(self.columnList,list):
            exist = False
            for item in self.columnList:
                for item2 in tableArray:
                    index = 0
                    for item3 in item2['table'].columns:
                        if (item3.name == item['name'] and item2['table'].name == item['father']) or (item3.name == item['name'] and item['father'] == None):
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

    #==================================================== O R D E R  B Y ========================================================
    def ORDERBY(self,columnsArray, tabla):
        if self.orderby != None:
            #Se extraen los id que se deben agrupar.
            ordenados = []
            asc = []
            for val in self.orderby:
                ordenados.append(val['id'])
                asc.append(val['asc'])

            for i in range(len(ordenados)):
                for item in self.columnList:
                    if ordenados[i]== item['as']:
                        ordenados[i] = item['name']
                        break

            dict = {}
            for obj in columnsArray:
                dict[obj['column'].name] = obj['data']
            ff = pd.DataFrame(dict)
            ff.sort_values(by=['nombre', 'id'])
            value = ff.sort_values(by =ordenados, ascending=asc).to_dict('records')
            for item in value:
                dictL = []
                for val in item.items():
                    dictL.append(val[1])
                tabla.append(dictL)
        else:
            try:
                for index in range(len(columnsArray)):
                    for i in range(len(columnsArray[index]['data'])):#tupla
                        tupla = []
                        for val in columnsArray:
                            tupla.append(val['data'][i])
                        tabla.append(tupla)
            except:
                print("Error")