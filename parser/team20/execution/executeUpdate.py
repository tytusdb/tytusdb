from .AST.sentence import Update
from .storageManager.TypeChecker import TCgetDatabase,TCSearchDatabase,TCgetTableColumns
from .storageManager.jsonMode import *
from .executeExpression import executeExpression
from .AST.error import *
from console import print_success, print_error

# class Update(Sentence):
#     def __init__(self, table, values, expression):
#         self.table = table
#         self.values = values #values = [value1,value2,...,valuen] -> value = [id,expression]  
#         self.expression = expression

def executeUpdate(self, update_):
    db = TCgetDatabase()
    mode = TCSearchDatabase(db)
    table = update_.table
    register = {} # {#columna:[nuevo valor]}
    columns = [] # PK 
    tabledata = extractTable(db,table)
    fieldnames = TCgetTableColumns(db,table)
    for value in update_.values:
        res = executeExpression(self,value[1])
        if(not isinstance(res,Error)):
            temp = {value[0]:res.value}
            register = register | temp
    try:
        where = executeExpression(self,update_.expression)
        pos = fieldnames.index(where.id) #GET PK position
        res = 0
        count = 0
        for tup in tabledata:
            if(where.op == '='):
                if(tup[pos]==where.value):
                    res=update(db,table,register,[tup[pos]]) #update
                    count+=1
            elif(where.op == '!=' or where.op == '<>'):
                if(tup[pos]!=where.value):
                    res=update(db,table,register,[tup[pos]])
                    count+=1
            elif(where.op == '>'):
                if(tup[pos]>where.value):
                    res=update(db,table,register,[tup[pos]])
                    count+=1
            elif(where.op == '<'):
                if(tup[pos]<where.value):
                    res=update(db,table,register,[tup[pos]])
                    count+=1
            elif(where.op == '>='):
                if(tup[pos]>=where.value):
                    res=update(db,table,register,[tup[pos]])
                    count+=1
            elif(where.op == '<='):
                if(tup[pos]<=where.value):
                    res=update(db,table,register,[tup[pos]])
                    count+=1
        if res==0:
            print_success("QUERY",str(count) + " rows updated successfully")
        elif res==1:
            print_error("SEMANTIC ERROR","Operation error")
        elif res==2:
            print_error("SEMANTIC ERROR","The database does not exist")
        elif res==3:
            print_error("SEMANTIC ERROR","Table does not exist")
        elif res==4:
            print_error("SEMANTIC ERROR","Primary key does not exist in table")
    except Exception as e:
        print(e)
    