from .storageManager import jsonMode
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase,TCgetDatabase,TCcreateTable,TCcreateType
from .executeExpression import executeExpression
from .AST.sentence import *
from .AST.error import * 

import os 
import json

def executeCreateDatabase(self, database):
    # crear en base a la condicion FALTA AGREGAR REPLACE Y OWNERMODE
    mode=1
    if(database.OwnerMode[1]!= None):
        res = executeExpression(self,database.OwnerMode[1])
        if(isinstance(res,Error)): 
            print(res.toString())
            self.errors.append(res)
        else: mode = res.value
        
    if(database.ifNotExistsFlag and not(database.OrReplace)):
        if mode==1:
            return jsonMode.createDatabase(database.name)
        elif mode==2:
            return jsonMode.createDatabase(database.name)
        elif mode==3:
            return jsonMode.createDatabase(database.name)
        elif mode==4:
            return jsonMode.createDatabase(database.name)
        else:
            print("ERROR: Mode between 1-5")
            self.errors.append(
            Error("Semántico","ERROR: Mode between 1-5",0,0)
            ) # voy a intentar agregar el numero de linea a cada sentencia
            return 1

    elif(database.ifNotExistsFlag and database.OrReplace):
        res=TCSearchDatabase(database.name)

        if(res==8):
            mode=1
            if(database.OwnerMode[1]!= None ):
                res = executeExpression(self,database.OwnerMode[1])
                if(isinstance(res,Error)): 
                    print(res.toString())
                    self.errors.append(res)
                else: mode = res.value
            if mode==1:
                return jsonMode.createDatabase(database.name)
            elif mode==2:
                return jsonMode.createDatabase(database.name)
            elif mode==3:
                return jsonMode.createDatabase(database.name)
            elif mode==4:
                return jsonMode.createDatabase(database.name)
            else:
                print("ERROR: Mode between 1-5")
                return 1
        else:
            TCdropDatabase(database.name)
            if res==1:
                jsonMode.dropDatabase(database.name)
            elif res==2:
                jsonMode.dropDatabase(database.name)
            elif res==3:
                jsonMode.dropDatabase(database.name)
            elif res==4:
                jsonMode.dropDatabase(database.name)
            else:
                print("ERROR: Mode between 1-5")
                return 1
            
            mode=1
            if(database.OwnerMode[1]!= None ):
                res = executeExpression(self,database.OwnerMode[1])
                if(isinstance(res,Error)): 
                    print(res.toString())
                    self.errors.append(res)
                else: mode = res.value
            if mode==1:
                return jsonMode.createDatabase(database.name)
            elif mode==2:
                return jsonMode.createDatabase(database.name)
            elif mode==3:
                return jsonMode.createDatabase(database.name)
            elif mode==4:
                return jsonMode.createDatabase(database.name)
            else:
                print("ERROR: Mode between 1-5")
                return 1

    elif(not(database.ifNotExistsFlag) and not(database.OrReplace)):
       
        if mode==1:
            return jsonMode.createDatabase(database.name)
        elif mode==2:
            return jsonMode.createDatabase(database.name)
        elif mode==3:
            return jsonMode.createDatabase(database.name)
        elif mode==4:
            return jsonMode.createDatabase(database.name)
        else:
            print("ERROR: Mode between 1-5")
            return 1

    else:
        res=TCSearchDatabase(database.name)

        if(res==8):            
            if mode==1:
                return jsonMode.createDatabase(database.name)
            elif mode==2:
                return jsonMode.createDatabase(database.name)
            elif mode==3:
                return jsonMode.createDatabase(database.name)
            elif mode==4:
                return jsonMode.createDatabase(database.name)
            else:
                print("ERROR: Mode between 1-5")
                return 1
        else:
            TCdropDatabase(database.name)
            if res==1:
                jsonMode.dropDatabase(database.name)
            elif res==2:
                jsonMode.dropDatabase(database.name)
            elif res==3:
                jsonMode.dropDatabase(database.name)
            elif res==4:
                jsonMode.dropDatabase(database.name)
            else:
                print("ERROR: Mode between 1-5")
                return 1
            
            if mode==1:
                return jsonMode.createDatabase(database.name)
            elif mode==2:
                return jsonMode.createDatabase(database.name)
            elif mode==3:
                return jsonMode.createDatabase(database.name)
            elif mode==4:
                return jsonMode.createDatabase(database.name)
            else:
                print("ERROR: Mode between 1-5")
                return 1

    return 1

def executeCreateTable(self, table):
    
    return 1
            
            
          
    
    #{"Type":,type,"Name":,"MaxLength":,"DefaultFlag":,"PrimaryKeyFlag":,"NullFlag":,"Constrains":[]}
    #
        
def executeCreateType(self, typeEnum):
    data=TCgetDatabase()
    array={}
    if(typeEnum.expressions!=None):
        i = 0
        for node in typeEnum.expressions:
            res=executeExpression(self,node)
            if(res.type == 5):
                res.value = res.value.replace("'","")
                new={str(i):res.value}
                array.update(new)
                i=i+1
        #print(array)
    return TCcreateType(data,typeEnum.name,array) 
    