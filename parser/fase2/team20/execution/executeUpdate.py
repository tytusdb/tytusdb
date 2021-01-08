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
    if(type(fieldnames) is str):
        print_error("SEMANTIC ERROR","Table does not exist",2)
        return
    for value in update_.values:
        res = executeExpression(self,value[1])
        if(not isinstance(res,Error)):   
            try:
                position = fieldnames.index(value[0])
                temp = {position:res.value}
                register = register | temp
            except:
                print_error("SEMANTIC ERROR","The column does not exist",2)    
    try:
        where = executeExpression(self,update_.expression)
        if(isinstance(where,Error)): 
            self.errors.append(where)
            print_error("SEMANTIC ERROR",str(where),2)
            return
        pos = fieldnames.index(where.id) #GET PK position
        res = 0
        count = 0
        for tup in tabledata:
            if(where.op == '='):
                if(tup[pos]==where.value):
                    res=update(db,table,register,[str(tup[pos])]) #update
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
            print_success("QUERY",str(count) + " rows updated successfully",2)
        elif res==1:
            print_error("SEMANTIC ERROR","Operation error",2)
        elif res==2:
            print_error("SEMANTIC ERROR","The database does not exist",2)
        elif res==3:
            print_error("SEMANTIC ERROR","Table does not exist",2)
        elif res==4:
            print_error("SEMANTIC ERROR","Primary key does not exist in table",2)
        else:
            print_error("UNKNOWN ERROR", "Operation error",2)
    except Exception as e:
        print_error("UNKNOWN ERROR", "instruction not executed",2)
        #print(e)
    