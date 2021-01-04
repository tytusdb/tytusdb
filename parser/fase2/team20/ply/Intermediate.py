from .AST.sentence import *


def ICreateDatabase(name, ifNotExistsFlag, OrReplace, OwnerMode):

    sentence= CreateDatabase(name, ifNotExistsFlag, OrReplace, OwnerMode)

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