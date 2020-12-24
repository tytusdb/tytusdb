from .storageManager import jsonMode
from .storageManager.TypeChecker import TCalterDatabase,TCSearchDatabase,TCalterDropPk,TCgetDatabase,TCaltertype
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

def executeAlterTableDropPK(self,table):
    database=TCgetDatabase()
    mode=TCSearchDatabase(database)
    if(mode==1):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    elif(mode==2):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    elif(mode==3):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    elif(mode==4):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    elif(mode==8):
        res=jsonMode.alterDropPK(database,table.table)
        if(res==0):
            TCalterDropPk(database,table.table)
        return res
    else:
        print_error("SEMANTIC ERROR",'Mode between 1-5')
        return 1


def executeAlterType(self,table):
    database=TCgetDatabase()
    mode=TCSearchDatabase(database)
    if(mode==1):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5
    elif(mode==2):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5 
    elif(mode==3):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5
    elif(mode==4):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5 
    elif(mode==8):
        if(len(table.newtype)>1):
            return TCaltertype(database,table.table,table.column,table.newtype[1])
        else:
            return 5
    else:
        print_error("SEMANTIC ERROR",'Mode between 1-5')
        return 1