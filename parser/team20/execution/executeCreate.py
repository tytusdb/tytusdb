from .storageManager import jsonMode
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase,TCgetDatabase,TCcreateTable
from .executeExpression import *
from .AST.sentence import *
import os 
import json

def executeCreateDatabase(self, database):
    # crear en base a la condicion FALTA AGREGAR REPLACE Y OWNERMODE
    mode=1
    if(database.OwnerMode[1]!= None ):
        mode= database.OwnerMode[1].value
        
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
            return 1

    elif(database.ifNotExistsFlag and database.OrReplace):
        res=TCSearchDatabase(database.name)

        if(res==8):
            mode=1
            if(database.OwnerMode[1]!= None ):
                mode= database.OwnerMode[1].value
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
                mode= database.OwnerMode[1].value
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
    print('algo1')
    
    data=TCgetDatabase()
    array={}
    if(table.columns!=None):
        for node in table.columns:
            print(node.options)
            print(node.type[0])
            
            if(node.options!=None):
                new={'type':node.type[0]}
                print(new)
                node.options.update(new)
                new={node.name:node.options}
            else:
                new={node.name:{'type':node.type[0]}}
            array.update(new)
            
            #
    print(array)
    return TCcreateTable(data,table.name,array)
            
            
          
    
    #{"Type":,type,"Name":,"MaxLength":,"DefaultFlag":,"PrimaryKeyFlag":,"NullFlag":,"Constrains":[]}
    #
        


    