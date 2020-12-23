from .AST.sentence import *
from .executeCreate import executeCreateDatabase,executeCreateTable,executeCreateType
from .executeShow import executeShowDatabases
from .executeSelect import executeSelect
from .executeDrop import executeDropDatabase,executeDropTable
from .executeUse import executeUse
from .executeExpression import executeExpression
from .executeInsert import executeInsertAll
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase,TCgetDatabase,TCdropTable
from .AST.error import * 
import sys
sys.path.append("../")
from console import *

def executeSentence(self, sentence):
    if isinstance(sentence, CreateDatabase):
        result= executeCreateDatabase(self,sentence)
        if(result==0):
            mode=1
            if(sentence.OwnerMode[1]!= None ):
                res = executeExpression(self,sentence.OwnerMode[1])
                if(isinstance(res,Error)): 
                    print(res.toString())
                    print_error('SEMANTIC ERROR','owner mode out of range')
                else: mode = res.value
            TCcreateDatabase(sentence.name,mode)
            print_success('QUERY',"Database "+sentence.name+" has been created Query returned successfully")
        elif(result==2 and sentence.ifNotExistsFlag):
            print_warning("NOTICE",'Database '+sentence.name+' already exists Query returned successfully')
        elif(result==2 and not sentence.ifNotExistsFlag):
            print_error('SEMANTIC ERROR','Database '+sentence.name+' already exists')
        else:
            print_error("SEMANTIC ERROR",'error in the operation')
            
    elif isinstance(sentence, ShowDatabases):
        executeShowDatabases(self)
    elif isinstance(sentence, DropDatabase):
        result= executeDropDatabase(self,sentence)
        if(result==0):
            TCdropDatabase(sentence.name)
            print_success("QUERY","DataBase "+sentence.name+" has been dropped")
        elif(result==2 and sentence.ifExistsFlag): 
            print_warning("NOTICE:", "Database "+sentence.name+" does not exist, skipping Query returned successfully with no result")
        elif(result==2 and not sentence.ifExistsFlag): 
            print_error("SEMANTIC ERROR","Database "+sentence.name+" does not exist")
        else:
            print_error("SEMANTIC ERROR",'error in the operation')
    elif isinstance(sentence,Use):
        result=executeUse(self,sentence)
        if(result==0):
            print_success("QUERY", "Database "+sentence.name+" has been selected")
        elif(result==1):
            print_error("SEMANTIC ERROR",'Database '+sentence.name+' does not exist')
        else:
            print_error("SEMANTIC ERROR",'error in the operation')
    elif isinstance(sentence,CreateTable):
        result=executeCreateTable(self,sentence)
        if(result==0):
            print_success("QUERY"," Table "+sentence.name+" has been created")
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation")
        elif(result==2):
            print_error("SEMANTIC ERROR","DataBase not exists")
        elif(result==3):
            print_error("SEMANTIC ERROR","Table "+sentence.name+" already exists")
        else:
            print_error("SEMANTIC ERROR",'error in the operation')
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
    elif isinstance(sentence, InsertAll):
        executeInsertAll(self, sentence)
    # #Resto de sentencias posibles
    elif isinstance(sentence,Select):
        executeSelect(self,sentence) 
    elif isinstance(sentence,DropTable):
        database=TCgetDatabase()
        result= executeDropTable(self,sentence)
        if(result==0):
            print(TCdropTable(database,sentence.name))
            print_success("QUERY","Table "+sentence.name+" has been dropped")
        elif(result==2):
            print_error("SEMANTIC ERROR","Database "+database+" does not exist")
        elif(result==3):
            print_error("SEMANTIC ERROR","Table "+sentence.name+" does not exist")
        else:
            print_error("SEMANTIC ERROR",'error in the operation')

    