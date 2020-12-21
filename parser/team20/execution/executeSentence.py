from .AST.sentence import *
from .executeCreate import executeCreateDatabase,executeCreateTable,executeCreateType
from .executeShow import executeShowDatabases
from .executeDrop import executeDropDatabase
from .executeUse import executeUse
from .executeExpression import executeExpression
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase
from .AST.error import * 

def executeSentence(self, sentence):
    if isinstance(sentence, CreateDatabase):
        result= executeCreateDatabase(self,sentence)
        if(result==0):
            mode=1
            if(sentence.OwnerMode[1]!= None ):
                res = executeExpression(self,sentence.OwnerMode[1])
                if(isinstance(res,Error)): 
                    print(res.toString())
                    self.errors.append(res)
                else: mode = res.value
            TCcreateDatabase(sentence.name,mode)
            print("Database "+sentence.name+" has been created Query returned successfully")
        elif(result==2 and sentence.ifNotExistsFlag):
            print("NOTICE: Database "+sentence.name+" already exists")
        elif(result==2 and not sentence.ifNotExistsFlag):
            print("ERROR: Database "+sentence.name+" already exists")
        else:
            print("ERROR: error in the operation")
    elif isinstance(sentence, ShowDatabases):
        executeShowDatabases(self)
    elif isinstance(sentence, DropDatabase):
        result= executeDropDatabase(self,sentence)
        if(result==0):
            TCdropDatabase(sentence.name)
            print("DataBase "+sentence.name+" has been dropped")
        elif(result==2 and sentence.ifExistsFlag): 
            print("NOTICE: Database "+sentence.name+" does not exist,skipping Query returned successfully with no result")
        elif(result==2 and not sentence.ifExistsFlag): 
            print("ERROR: Database "+sentence.name+" does not exist")
        else:
            print("ERROR: error in the operation")
    elif isinstance(sentence,Use):
        result=executeUse(self,sentence)
        if(result==0):
            print("DataBase "+sentence.name+" has been selected")
        elif(result==1):
            print("ERROR: Database "+sentence.name+" does not exist")
        else:
            print("ERROR: error in the operation")
    elif isinstance(sentence,CreateTable):
        result=executeCreateTable(self,sentence)
        if(result==0):
            print("Table "+sentence.name+" has been created")
        elif(result==1):
            print("ERROR: error in the operation")
        elif(result==2):
            print("s")
        elif(result==3):
            print("Table "+sentence.name+" already exists")
        else:
            print("ERROR: error in the operation")
    elif isinstance(sentence,ColumnId):
        #print(ColumnId.name)
        print('Hola')
    elif isinstance(sentence, CreateType):
        result= executeCreateType(self,sentence)
        ##if(result==0):
            ##print("Type "+sentence.name+" has been created")
        ##elif(result==1):
            ##return Error('xx0000', 'internal_error' , 0, 0)
        ##elif(result==2):
            ##return Error('3D00', 'invalid_catalog_name' , 0, 0)
        ##elif(result==3):
            ##return Error('42710', 'duplicate_object' , 0, 0)
        ##else:
           ##return Error('xx0000', 'internal_error' , 0, 0)
    #Resto de sentencias posibles
    
    