from .storageManager import jsonMode
from .storageManager.TypeChecker import TCalterDatabase,TCSearchDatabase
from .AST.error import * 
from .executeExpression import executeExpression,Relational

import os 
import json

import sys
sys.path.append("../")
from console import * 

def executeAlterDatabaseRename(self,database):
    mode=TCSearchDatabase(database)
    if(mode==1):
        return jsonMode.alterDatabase(database.oldname,database.newname)
    elif(mode==2):
        return jsonMode.alterDatabase(database.oldname,database.newname)
    elif(mode==3):
        return jsonMode.alterDatabase(database.oldname,database.newname)
    elif(mode==4):
        return jsonMode.alterDatabase(database.oldname,database.newname) 
    elif(mode==8):
        return jsonMode.alterDatabase(database.oldname,database.newname)
    else:
        print_error("SEMANTIC ERROR",'Mode between 1-5')
        return 1