# from .storageManager.jsonMode import extractTable, showDatabases
# from .storageManager.TypeChecker import TCgetDatabase,TCSearchDatabase,TCgetTableColumns
# from .executeExpression import executeExpression
# from console import print_table 
# from prettytable import PrettyTable
# from .AST.error import * 
# def executeSelect(self,select):
#     db = TCgetDatabase()
#     mode = TCSearchDatabase(db)
#     x = PrettyTable()
#     columns = []
#     for column in select.columns:
#         columns.append(executeExpression(self,column).value)
#     if(len(columns) == 1 and columns[0]=="*" and select.options==None): #SELECT ALL NO OPTIONS
#         if(mode==1):
#             for table in select.tables:
#                 tb = executeExpression(self,table)
#                 if(not isinstance(table,Error)):
#                     res = extractTable(db,tb.value)
#                     x = PrettyTable()
#                     fieldnames = TCgetTableColumns(db,tb.value)
#                     if(type(fieldnames) is not str): x.field_names = fieldnames
#                     else: 
#                         self.errors.append(Error('Semantic','La tabla '+tb.value+' no existe',0,0))
#                         continue
#                     for row in res:
#                         x.add_row(row)
#                     print(x)
#                     print_table(x.get_string())
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