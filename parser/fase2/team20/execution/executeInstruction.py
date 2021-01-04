from .AST.instruction import *
from .AST.expression import *
from .AST.error import * 

def executeInstruction(self, instruction):
    if isinstance(instruction, CreateFunction):
        # def alterDatabase(databaseOld: str, databaseNew) -> int:
        if(instruction.params==None):self.plcode+="\ndef "+instruction.name+"():\n"
        else: 
            self.plcode+="\ndef "+instruction.name+"("
            textparams = ""
            for param in instruction.params:
                paramtype = ""
                if(param.type!="ANYELEMENT" or param.type!="ANYCOMPATIBL"):
                    paramtype = getType(param.type[0])
                if(paramtype==""):textparams+=param.name+", "
                else: textparams+=param.name+": "+paramtype+", "
            self.plcode+= textparams[:-2]
            if(instruction.returnValue==None):self.plcode+="):\n"
            elif(instruction.returnValue.type != None):
                returntype = ""
                if(instruction.returnValue.type!="ANYELEMENT" or instruction.returnValue.type!="ANYCOMPATIBL"):
                    returntype = getType(instruction.returnValue.type[0])
                if(returntype==""):self.plcode+="):\n"
                else: self.plcode+=") ->"+returntype+":\n"
        # Body function
        self.plcode+="\tprint(1)" 
    elif isinstance(instruction, CreateParam):
        print(instruction.name)
    elif isinstance(instruction, CreateReturn):
        print(instruction.type)
        print(instruction.paramsTable)
    elif isinstance(instruction, BlockFunction):
        print(instruction.declarations)
        print(instruction.statements)

def getType(sqltype):
    if(sqltype=="TEXT" 
    or sqltype=="CHAR"
    or sqltype=="CHARACTER"
    or sqltype=="VARCHAR"):
        return "str"
    if(sqltype=="SMALLINT"
    or sqltype=="INTEGER" 
    or sqltype=="BIGINT"):
        return "int"
    if(sqltype=="DECIMAL"
    or sqltype=="NUMERIC" 
    or sqltype=="DOUBLE" 
    or sqltype=="REAL"):
        return "float"
    return ""
    
