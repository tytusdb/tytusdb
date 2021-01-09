from .AST.sentence import *
from .executeCreate import executeCreateDatabase,executeCreateTable,executeCreateType
from .executeShow import executeShowDatabases
from .executeUpdate import executeUpdate
from .executeSelect import executeSelect
from .executeDrop import executeDropDatabase,executeDropTable
from .executeUse import executeUse, executeUseAlter
from .executeExpression import executeExpression
from .executeInsert import executeInsertAll, executeInsert
from .executeDelete import executeDelete
from .executeAlter import executeAlterDatabaseRename,executeAlterTableDropPK,executeAlterType, executeAlterTableAddColumn, executeAlterTableDropColumn
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase,TCgetDatabase,TCdropTable,TCalterDatabase
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
            print_warning("RUNTIME ERROR",'Database '+sentence.name+' already exists Query returned successfully')
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
            print_warning("RUNTIME ERROR", "Database "+sentence.name+" does not exist, skipping Query returned successfully with no result")
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
        if(result==0):
            print_success("QUERY"," Type "+sentence.name+" has been created in the database")
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation")
        elif(result==2):
            print_error("SEMANTIC ERROR","DataBase not exists")
        elif(result==3):
            print_error("SEMANTIC ERROR","Type "+sentence.name+" already exists in the database")
        else:
            print_error("SEMANTIC ERROR",'error in the operation')
    elif isinstance(sentence, InsertAll):
        executeInsertAll(self, sentence)
    elif isinstance(sentence, Insert):
        executeInsert(self, sentence)
    elif isinstance(sentence, Delete):
        executeDelete(self, sentence)
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
    elif isinstance(sentence,AlterDatabaseRename):
        result= executeAlterDatabaseRename(self,sentence)
        if(result==0):
            print(TCalterDatabase(sentence.oldname,sentence.newname))
            #Verificar si es una base de datos que esta en uso
            database=TCgetDatabase()
            if(database == sentence.oldname):
                result=executeUseAlter(self,sentence.newname)
            print_success("QUERY","Database "+sentence.oldname+" has been renamed")
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation")
        elif(result==2):
            print_error("SEMANTIC ERROR","Database "+sentence.oldname+" does not exist")
        elif(result==3):
            print_error("SEMANTIC ERROR","Database "+sentence.newname+" already exist")
        else:
            print_error("SEMANTIC ERROR",'error in the operation')
    elif isinstance(sentence,Update):
       executeUpdate(self,sentence)
    elif isinstance(sentence,AlterTableDropConstraint):
        if(len(sentence.constraint)>2):
            if(sentence.constraint[len(sentence.constraint)-2:len(sentence.constraint)]=='PK'):
                result=executeAlterTableDropPK(self,sentence)    
                if(result==0):
                    print_success("QUERY","Primary key has been dropped")
                elif(result==2):
                    print_error("SEMANTIC ERROR","Database "+database+" does not exist")
                elif(result==3):
                    print_error("SEMANTIC ERROR","Table "+sentence.table+" does not exist")
                elif (result==4):
                    print_error("SEMANTIC ERROR","Pk does not exist")
                else:
                    print_error("SEMANTIC ERROR",'error in the operation')
    elif isinstance(sentence,AlterTableAlterColumnType):
        result=executeAlterType(self,sentence)
        if(result==0):
            print_success("QUERY","Type has been changed")
        elif(result==2):
            print_error("SEMANTIC ERROR","Database does not exist")
        elif(result==3):
            print_error("SEMANTIC ERROR","Table "+sentence.table+" does not exist")
        elif (result==4):
            print_error("SEMANTIC ERROR","Column "+sentence.column+" does not exist")
        elif (result==5):
            print_error("SEMANTIC ERROR","Type can not change")
        else:
            print_error("SEMANTIC ERROR",'error in the operation')
    elif isinstance(sentence, AlterTableAddColumn):
        executeAlterTableAddColumn(self, sentence)
    elif isinstance(sentence, AlterTableDropColumn):
        executeAlterTableDropColumn(self, sentence)
