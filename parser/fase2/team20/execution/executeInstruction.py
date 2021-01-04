from .AST.instruction import *
from .AST.expression import *
from .AST.error import * 

def executeInstruction(self, instruction):
    if isinstance(instruction, CreateFunction):
        print(instruction.name)   
        #if(instruction.params!=None):
            #for node in instruction.params:
                #executeInstruction(self,node)    
        executeInstruction(self,instruction.returnValue)               
    elif isinstance(instruction, CreateParam):
        print(instruction.name)
    elif isinstance(instruction, CreateReturn):
        print(instruction.type)
        print(instruction.paramsTable)