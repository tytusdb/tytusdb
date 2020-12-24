from .AST.sentence import Update
from .storageManager.TypeChecker import TCgetDatabase,TCSearchDatabase
from .storageManager.jsonMode import *
from .executeExpression import executeExpression
from .AST.error import *

# class Update(Sentence):
#     def __init__(self, table, values, expression):
#         self.table = table
#         self.values = values #values = [value1,value2,...,valuen] -> value = [id,expression]  
#         self.expression = expression

def executeUpdate(self, update):
    db = TCgetDatabase()
    mode = TCSearchDatabase(db)
    table = update.table
    register = {} # {#columna:[nuevo valor]}
    columns = [] # PK 
    for value in update.values:
        res = executeExpression(self,value[1])
        if(not isinstance(res,Error)):
            temp = {value[0]:res.value}
            register = register | temp
    