from .AST.instruction import *
from .AST.expression import *
from .AST.error import * 

def executeInstruction(self, instruction):
    if isinstance(instruction, CreateFunction):
        # def alterDatabase(databaseOld: str, databaseNew) -> int:
        if(instruction.params==None):self.plcode+="\ndef "+instruction.name+"():\n" #funcion sin parametros
        else: #funcion con parametros
            self.plcode+="\ndef "+instruction.name+"("
            textparams = ""
            for param in instruction.params:#definicion de cada parametro en la lista
                paramtype = ""
                if(param.type!="ANYELEMENT" or param.type!="ANYCOMPATIBL"):#los tipos any se ponen sin tipo en python
                    paramtype = getType(param.type[0])      # se mapea el tipo de SQL a tipo de python
                if param.name != None:
                    if(paramtype==""):textparams+=param.name+", "
                    else: textparams+=param.name+": "+paramtype+", "
                else:
                    if(instruction.block.declarations == None):
                        print("Error, no existe alias para parametro sin nombre")
                    else:
                        print("parametros sin nombre hay que recolectar el nombre del alias")
            self.plcode+= textparams[:-2]
            if(instruction.returnValue==None):self.plcode+="):\n"# sin valor de retorno
            elif(instruction.returnValue.type != None):
                returntype = ""
                if(instruction.returnValue.type!="ANYELEMENT" or instruction.returnValue.type!="ANYCOMPATIBL"):
                    returntype = getType(instruction.returnValue.type[0])# se mapea el tipo
                if(returntype==""):self.plcode+="):\n"
                else: self.plcode+=") ->"+returntype+":\n"# se asigna el tipo a la funcion de python
        # Body function
        if(instruction.block.declarations != None):
            # declarations
            for declaration in instruction.block.declarations:
                if(isinstance(declaration,VariableDeclaration)):
                    vartype = ""
                    if(instruction.returnValue.type!="ANYELEMENT" or instruction.returnValue.type!="ANYCOMPATIBL"):
                        vartype = getType(declaration.type[0])
                    if(declaration.expression == None):
                        if(vartype==""):self.plcode+="\t"+declaration.name+"\n"
                        else: self.plcode+="\t"+declaration.name+":"+vartype+"\n" # declaracion sin valor de la forma 'ID type;'
                    else:
                        # executeExpressionC3D, retorna codigo de 3 direcciones de una expresion declaration.expression
                        self.plcode+=declaration.expression.translate(self,1)
                        if(vartype==""):self.plcode+="\t"+declaration.name+"="+self.getLastTemp()+"\n" #asigna el valor del ultimo temporal que contiene el valor de la expresion
                        else: self.plcode+="\t"+declaration.name+":"+vartype+"="+self.getLastTemp()+"\n" #asigna el valor del ultimo temporal que contiene el valor de la expresion
        # statements
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
    
