from .storageManager.jsonMode import extractTable, showDatabases
from .storageManager.TypeChecker import TCgetDatabase,TCSearchDatabase,TCgetTableColumns
from .executeExpression import executeExpression
from console import print_table 
from prettytable import PrettyTable
from .AST.error import * 
from .AST.expression import *

import sys
sys.path.append("../")
from console import * 

def executeSelect(self,select):
    db = TCgetDatabase()
    mode = TCSearchDatabase(db)
    x = PrettyTable()
    columns = []

    if(select.tables==None): #SELECT SOME FUNCTIONS 
        print(select.columns)
        columnsNames = []
        columnsValues = []

        for column in select.columns:
            print(column)
            #Nombre comlumna
            if isinstance(column, Alias):
                columnsNames.append(column.alias)
                #print(column.alias)

                #Valor
                res=executeExpression(self,column.expression)
                if(not isinstance(res,Error)):
                    columnsValues.append(res.value)
                else:
                    print_error("SEMANTIC ERROR",res.toString())
            else:
                #Valor
                res=executeExpression(self,column)
                if(not isinstance(res,Error)):
                    columnsNames.append(column.function)
                    columnsValues.append(res.value)
                else:
                    print_error("SEMANTIC ERROR",res.toString())
            

        x.field_names = columnsNames
        x.add_row(columnsValues) 
        print(x)    
        print_table(x.get_string())
    else:
        for column in select.columns:
            columns.append(executeExpression(self,column).value)
        if(select.options==None):
            if(len(columns) != 1 and columns[0]!="*"): #SELECT SOME NO OPTIONS
                print("s some")
                if(mode==1):
                    for table in select.tables:
                        tb = executeExpression(self,table)
                        if(not isinstance(table,Error)):
                            res = extractTable(db,tb.value)
                            x = PrettyTable()
                            fieldnames = TCgetTableColumns(db,tb.value)
                            selectcolumns = []
                            if(type(fieldnames) is not str): 
                                bad = False
                                for column in columns: 
                                    try:
                                        selectcolumns.append(fieldnames.index(column))
                                    except:
                                        bad = True
                                        self.errors.append(Error('Semantic','El campo '+ column +' no pertence a la tabla '+tb.value,0,0))
                                        break
                                if(bad): continue
                                x.field_names = columns
                            else: 
                                self.errors.append(Error('Semantic','La tabla '+tb.value+' no existe',0,0))
                                continue

                            for row in res:
                                selectrow = []
                                for index in selectcolumns: selectrow.append(row[index])
                                x.add_row(selectrow)
                            print(x)
                            print_table(x.get_string())
            else:#SELECT ALL NO OPTIONS
                if(mode==1):
                    print("s all")
                    for table in select.tables:
                        tb = executeExpression(self,table)
                        if(not isinstance(table,Error)):
                            res = extractTable(db,tb.value)
                            x = PrettyTable()
                            fieldnames = TCgetTableColumns(db,tb.value)
                            if(type(fieldnames) is not str): x.field_names = fieldnames
                            else: 
                                self.errors.append(Error('Semantic','La tabla '+tb.value+' no existe',0,0))
                                continue
                            for row in res:
                                x.add_row(row)
                            print(x)
                            print_table(x.get_string())
        else:
            if(len(columns) == 1 and columns[0]=="*"):
                print("Select all with options")
            else:
                print("Select some with options")
    # elif(select.options!=None): #SELECT ALL WITH OPTIONS
    #     if(mode==1):
    #         for table in select.tables:
    #             tb = executeExpression(self,table)
    #             if(not isinstance(table,Error)):
    #                 res = extractTable(db,tb.value)
    #                 fieldnames = TCgetTableColumns(db,tb.value)
    #                 if(type(fieldnames) is str):  
    #                     self.errors.append(Error('Semantic','La tabla '+tb.value+' no existe',0,0))
    #                     continue
    # x = PrettyTable()
    # dbs = showDatabases()
    # self.messages.append("Databases:")
    # x.field_names = ["Databases"]
    # for db in dbs:
    #     x.add_row([db])
    #     self.messages.append("\t"+db)
    # x.align = "r"
    # x.border = True
    # x.padding_width = 7
    # print(x) #show databases;