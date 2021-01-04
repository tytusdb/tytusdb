from .storageManager.jsonMode import extractTable, showDatabases
from .storageManager.TypeChecker import TCgetDatabase,TCSearchDatabase,TCgetTableColumns
from .executeExpression import executeExpression
from console import print_success, print_table
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
        #print(select.columns)
        columnsNames = []
        columnsValues = []

        for column in select.columns:
            print(column)
            #Nombre columna
            if isinstance(column, Alias):
                columnsNames.append(column.alias)
                print(column.alias)

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
        print_success("QUERY","Query carried out successfully")
        print_table("QUERY TABLE",x.get_string())
    else:
        for column in select.columns:
            columns.append(executeExpression(self,column).value)
        if(select.options==None):
            if(len(columns) == 1 and columns[0]=="*"):#SELECT ALL NO OPTIONS
                if(mode==1):
                    print("s all no opt")
                    for table in select.tables:
                        tb = executeExpression(self,table)
                        if(not isinstance(table,Error)):
                            res = extractTable(db,tb.value)
                            x = PrettyTable()
                            fieldnames = TCgetTableColumns(db,tb.value)
                            if(type(fieldnames) is not str): x.field_names = fieldnames
                            else: 
                                print_error("SEMANTIC ERROR",str(tb.value) + ' table does not exist')
                                self.errors.append(Error('Semantic',str(tb.value) + ' table does not exist',0,0))
                                continue
                            for row in res:
                                x.add_row(row)
                            print(x)
                            print_success("QUERY","Query carried out successfully")
                            print_table("QUERY TABLE",x.get_string())
            else: #SELECT SOME NO OPTIONS
                print("s some no opt")
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
                                        print_error("SEMANTIC ERROR",'The ' + str(column) + ' field does not belong to the ' + str(tb.value) + ' table')
                                        self.errors.append(Error('Semantic','The ' + str(column) + ' field does not belong to the ' + str(tb.value) + ' table',0,0))
                                        break
                                if(bad): continue
                                x.field_names = columns
                            else:
                                print_error("SEMANTIC ERROR",'Table ' + str(tb.value) + ' does not exist')
                                self.errors.append(Error('Semantic','Table ' + str(tb.value) + ' does not exist',0,0))
                                continue

                            for row in res:
                                selectrow = []
                                for index in selectcolumns: selectrow.append(row[index])
                                x.add_row(selectrow)
                            print(x)
                            print_success("QUERY","Query carried out successfully")
                            print_table("QUERY TABLE",x.get_string())
        else:
            if(len(columns) == 1 and columns[0]=="*"):
                if(mode==1):
                    print("s all opt")
                    tables = []
                    for table in select.tables:
                        tb = executeExpression(self,table)
                        if(not isinstance(table,Error)):
                            res = extractTable(db,tb.value)
                            x = PrettyTable()
                            fieldnames = TCgetTableColumns(db,tb.value)
                            rawdata = []
                            if(type(fieldnames) is str):
                                print_error("SEMANTIC ERROR",'Table ' + str(tb.value) + ' does not exist')
                                self.errors.append(Error('Semantic','Table ' + str(tb.value) + ' does not exist',0,0))
                                continue
                            for row in res:
                                rawdata.append(row)
                            temp = {"nombre":tb.value,"columns":fieldnames,"data":rawdata}
                            tables.append(temp)
                            #x.field_names = fieldnames
                    if(len(tables)==1):#select all de una sola tabla
                        # where -> Expression
                        # orderby -> SortExpressionList
                            # sortExpressionList -> lista de expresiones de la forma [Expression,ASC/DESC]
                        # limit -> Expression/ALL ALL is the same as omitting the LIMIT clause
                        # offset -> Expression OFFSET says to skip that many rows before beginning to return rows. OFFSET 0 is the same as omitting the OFFSET clause. 
                            # If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
                        # groupby -> ExpressionList
                        # having -> Expression
                        print(select.options)
                        try:
                            select.options['where']
                            temp = []
                            where = executeExpression(self,select.options['where'])
                            pos = fieldnames.index(where.id)
                            for tup in tables[0]["data"]:
                                if(where.op == '='):
                                    if(tup[pos]==where.value):
                                        temp.append(tup)
                                elif(where.op == '!=' or where.op == '<>'):
                                    if(tup[pos]!=where.value):
                                        temp.append(tup)
                                elif(where.op == '>'):
                                    if(tup[pos]>where.value):
                                        temp.append(tup)
                                elif(where.op == '<'):
                                    if(tup[pos]<where.value):
                                        temp.append(tup)
                                elif(where.op == '>='):
                                    if(tup[pos]>=where.value):
                                        temp.append(tup)
                                elif(where.op == '<='):
                                    if(tup[pos]<=where.value):
                                        temp.append(tup)
                            tables[0]["data"] = temp
                        except:
                            pass
                        try:
                            select.options['orderby']
                        except:
                            pass
                        try:
                            select.options['limit']
                            select.options['offset']
                            offset = executeExpression(self,select.options['offset'])
                            if(not isinstance(offset,Error) and offset.value!=0):
                                del tables[0]["data"][:offset.value]
                            if select.options['limit']!='ALL':
                                limit = executeExpression(self,select.options['limit'])
                                if(not isinstance(limit,Error)):
                                    del tables[0]["data"][limit.value:]
                            #both limit and offset
                        except:
                            try:
                                select.options['limit']
                                if select.options['limit']!='ALL':
                                    limit = executeExpression(self,select.options['limit'])
                                    if(not isinstance(limit,Error)):
                                        del tables[0]["data"][limit.value:]
                            except:
                                pass
                            try:
                                select.options['offset']
                                offset = executeExpression(self,select.options['offset'])
                                if(not isinstance(offset,Error) and offset.value!=0):
                                    del tables[0]["data"][:offset.value]
                            except:
                                pass
                        x.field_names = tables[0]["columns"]
                        for row in tables[0]["data"]:
                            x.add_row(row)
                        print(x)
                        print_success("QUERY","Query carried out successfully")
                        print_table("QUERY TABLE",x.get_string())

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