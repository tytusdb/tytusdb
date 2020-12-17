from .AST.sentence import *
from .executeCreate import executeCreateDatabase
from .executeShow import executeShowDatabases
from .executeDrop import executeDropDatabase
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase

def executeSentence(self, sentence):
    if isinstance(sentence, CreateDatabase):
        result= executeCreateDatabase(self,sentence)
        if(result==0):
            TCcreateDatabase(sentence.name)
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

    #Resto de sentencias posibles
    
    