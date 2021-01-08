from .AST.sentence import *
from .AST.instruction import Instruction
from .executeCreate import executeCreateDatabase,executeCreateTable,executeCreateType,executeCreateUnique
from .executeShow import executeShowDatabases
from .executeUpdate import executeUpdate
from .executeSelect import executeSelect
from .executeDrop import executeDropDatabase,executeDropTable,executeDropIndex
from .executeUse import executeUse, executeUseAlter
from .executeExpression import executeExpression
from .executeInsert import executeInsertAll, executeInsert
from .executeDelete import executeDelete
from .executeAlter import executeAlterDatabaseRename,executeAlterTableDropPK,executeAlterType, executeAlterTableAddColumn, executeAlterTableDropColumn,executeAlterIndex
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase,TCgetDatabase,TCdropTable,TCalterDatabase,TCDropIndex
from .AST.error import * 
import sys
sys.path.append("../")
from console import *

def executeSentence(self, sentence):

    if isinstance(sentence, CreateDatabase):
        result= executeCreateDatabase(self,sentence)
        if(result==0):
            mode=1
            if(sentence.OwnerMode[1]!= None):
                res = executeExpression(self,sentence.OwnerMode[1])
                print(res.value)
                if(isinstance(res,Error)): 
                    print(res.toString())
                    print_error('SEMANTIC ERROR','owner mode out of range',2)
                else: mode = res.value
            TCcreateDatabase(sentence.name,mode)
            print_success('QUERY',"Database "+sentence.name+" has been created Query returned successfully",2)
        elif(result==2 and sentence.ifNotExistsFlag):
            print_warning("RUNTIME ERROR",'Database '+sentence.name+' already exists Query returned successfully',2)
        elif(result==2 and not sentence.ifNotExistsFlag):
            print_error('SEMANTIC ERROR','Database '+sentence.name+' already exists',2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
            
    elif isinstance(sentence, ShowDatabases):
        executeShowDatabases(self)
    elif isinstance(sentence, DropDatabase):
        result= executeDropDatabase(self,sentence)
        if(result==0):
            TCdropDatabase(sentence.name)
            print_success("QUERY","DataBase "+sentence.name+" has been dropped",2)
        elif(result==2 and sentence.ifExistsFlag): 
            print_warning("RUNTIME ERROR", "Database "+sentence.name+" does not exist, skipping Query returned successfully with no result",2)
        elif(result==2 and not sentence.ifExistsFlag): 
            print_error("SEMANTIC ERROR","Database "+sentence.name+" does not exist",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence,Use):
        result=executeUse(self,sentence)
        if(result==0):
            print_success("QUERY", "Database "+sentence.name+" has been selected",2)
        elif(result==1):
            print_error("SEMANTIC ERROR",'Database '+sentence.name+' does not exist',2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence,CreateTable):
        result=executeCreateTable(self,sentence)

        if(result==0):
            print_success("QUERY"," Table "+sentence.name+" has been created",2)
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation",2)
        elif(result==2):
            print_error("SEMANTIC ERROR","DataBase not exists",2)
        elif(result==3):
            print_error("SEMANTIC ERROR","Table "+sentence.name+" already exists",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence, CreateType):
        result= executeCreateType(self,sentence)
        if(result==0):
            print_success("QUERY"," Type "+sentence.name+" has been created in the database",2)
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation",2)
        elif(result==2):
            print_error("SEMANTIC ERROR","DataBase not exists",2)
        elif(result==3):
            print_error("SEMANTIC ERROR","Type "+sentence.name+" already exists in the database",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence, InsertAll):
        executeInsertAll(self, sentence)
    elif isinstance(sentence, Insert):
        executeInsert(self, sentence)
    elif isinstance(sentence, Delete):
        executeDelete(self, sentence)
    elif isinstance(sentence,Select):
        try:
            res = executeSelect(self,sentence)
            return res
            #print(res)
        except:
            executeSelect(self,sentence) 
    elif isinstance(sentence,DropTable):
        database=TCgetDatabase()
        result= executeDropTable(self,sentence)
        if(result==0):
            print(TCdropTable(database,sentence.name))
            print_success("QUERY","Table "+sentence.name+" has been dropped",2)
        elif(result==2):
            print_error("SEMANTIC ERROR","Database "+database+" does not exist",2)
        elif(result==3):
            print_error("SEMANTIC ERROR","Table "+sentence.name+" does not exist",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence,AlterDatabaseRename):
        result= executeAlterDatabaseRename(self,sentence)
        if(result==0):
            print(TCalterDatabase(sentence.oldname,sentence.newname))
            #Verificar si es una base de datos que esta en uso
            database=TCgetDatabase()
            if(database == sentence.oldname):
                result=executeUseAlter(self,sentence.newname)
            print_success("QUERY","Database "+sentence.oldname+" has been renamed",2)
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation",2)
        elif(result==2):
            print_error("SEMANTIC ERROR","Database "+sentence.oldname+" does not exist",2)
        elif(result==3):
            print_error("SEMANTIC ERROR","Database "+sentence.newname+" already exist",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence,Update):
        executeUpdate(self,sentence)
    elif isinstance(sentence,AlterTableDropConstraint):
        if(len(sentence.constraint)>2):
            if(sentence.constraint[len(sentence.constraint)-2:len(sentence.constraint)]=='PK'):
                result=executeAlterTableDropPK(self,sentence)    
                if(result==0):
                    print_success("QUERY","Primary key has been dropped",2)
                elif(result==2):
                    print_error("SEMANTIC ERROR","Database "+database+" does not exist",2)
                elif(result==3):
                    print_error("SEMANTIC ERROR","Table "+sentence.table+" does not exist",2)
                elif (result==4):
                    print_error("SEMANTIC ERROR","Pk does not exist",2)
                else:
                    print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence,AlterTableAlterColumnType):
        result=executeAlterType(self,sentence)
        if(result==0):
            print_success("QUERY","Type has been changed",2)
        elif(result==2):
            print_error("SEMANTIC ERROR","Database does not exist",2)
        elif(result==3):
            print_error("SEMANTIC ERROR","Table "+sentence.table+" does not exist",2)
        elif (result==4):
            print_error("SEMANTIC ERROR","Column "+sentence.column+" does not exist",2)
        elif (result==5):
            print_error("SEMANTIC ERROR","Type can not change",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence, AlterTableAddColumn):
        executeAlterTableAddColumn(self, sentence)
    elif isinstance(sentence, AlterTableDropColumn):
        executeAlterTableDropColumn(self, sentence)
    elif isinstance(sentence, CreateIndex):
        result=executeCreateUnique(self,sentence)
        
        if(result==0):
            print_success("QUERY"," Index into"+sentence.table+" has been created",2)
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation",2)
        elif(result==2):
            print_error("SEMANTIC ERROR","DataBase not exists",2)
        elif(result==3):
            print_error("SEMANTIC ERROR","Table "+sentence.table+" dont exists",2)
        elif(result==4):
            print_error("SEMANTIC ERROR","Column "+sentence.ascdesc[0]+" dont exists",2)
        elif(result==5):
            print_error("SEMANTIC ERROR","Index "+sentence.name+" already exists",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence, DropIndex):
        result=executeDropIndex(self,sentence)
        
        if(result==0):
            print_success("QUERY"," Index "+sentence.name+" has been dropped",2)
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation",2)
        elif(result==2):
            print_error("SEMANTIC ERROR","DataBase not exists",2)
        elif(result==3):
            print_error("SEMANTIC ERROR","Any Index was found",2)
        elif(result==4):
            if(sentence.ifExistsFlag):
                print_success("WARNING","Index "+sentence.name+" dont exists Query returned sucessfuly",2)
            else:
                print_error("SEMANTIC ERROR","Index "+sentence.name+" dont exists",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)
    elif isinstance(sentence, AlterIndex):
        result=executeAlterIndex(self,sentence)
        
        if(result==0):
            print_success("QUERY"," Index "+sentence.index+" has been alter",2)
        elif(result==1):
            print_error("SEMANTIC ERROR","error in the operation",2)
        elif(result==2):
            print_error("SEMANTIC ERROR","DataBase not exists",2)
        elif(result==3):
            print_error("SEMANTIC ERROR","Any Index was found",2)
        elif(result==4):
            print_error("SEMANTIC ERROR","Index "+sentence.index+" dont exists",2)
        elif(result==5):
            print_error("SEMANTIC ERROR","Column "+sentence.oldname+" dont exists",2)
        elif(result==6):
            print_error("SEMANTIC ERROR","Column "+sentence.newname+" dont exists",2)
        else:
            print_error("SEMANTIC ERROR",'error in the operation',2)