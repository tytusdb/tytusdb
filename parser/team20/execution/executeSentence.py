from .AST.sentence import *
from .executeCreate import executeCreateDatabase,executeCreateTable
from .executeShow import executeShowDatabases
from .executeDrop import executeDropDatabase
from .executeUse import executeUse
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase

def executeSentence(self, sentence):
    if isinstance(sentence, CreateDatabase):
        result= executeCreateDatabase(self,sentence)
        if(result==0):
            mode=1
            if(sentence.OwnerMode[1]!= None ):
                mode= sentence.OwnerMode[1].value
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
        print(ColumnId.name)
        
    #Resto de sentencias posibles
    
    