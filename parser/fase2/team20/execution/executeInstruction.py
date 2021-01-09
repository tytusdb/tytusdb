from .AST.instruction import *
from .AST.expression import *
from .AST.error import * 
from .AST.sentence import *
from .storageManager.TypeChecker import * 
from console import print_success, print_table, print_error, print_text

def executeInstruction(self, instruction,indent, main):
    if isinstance(instruction, CreateFunction):
        functioncode = ""
        functionname = instruction.name
        replace = instruction.replace
        # def alterDatabase(databaseOld: str, databaseNew) -> int:
        if(instruction.params==None):functioncode+="\n@with_goto\ndef "+instruction.name+"():\n" #funcion sin parametros
        else: #funcion con parametros
            functioncode+="\n@with_goto\ndef "+instruction.name+"("
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
            functioncode+= textparams[:-2]
            if(instruction.returnValue==None):functioncode+="):\n"# sin valor de retorno
            elif(instruction.returnValue.type != None):
                returntype = ""
                if(instruction.returnValue.type!="ANYELEMENT" or instruction.returnValue.type!="ANYCOMPATIBL"):
                    returntype = getType(instruction.returnValue.type[0])# se mapea el tipo
                if(returntype==""):functioncode+="):\n"
                else: functioncode+=") ->"+returntype+":\n"# se asigna el tipo a la funcion de python
        # Body function
        if(instruction.block.declarations != None):
            # declarations
            for declaration in instruction.block.declarations:
                if(isinstance(declaration,VariableDeclaration)):
                    vartype = ""
                    if(instruction.returnValue.type!="ANYELEMENT" or instruction.returnValue.type!="ANYCOMPATIBL"):
                        vartype = getType(declaration.type[0])
                    if(declaration.expression == None):
                        if(vartype==""):functioncode+="\t"+declaration.name+"\n"
                        else: functioncode+="\t"+declaration.name+":"+vartype+"\n" # declaracion sin valor de la forma 'ID type;'
                    else:
                        # executeExpressionC3D, retorna codigo de 3 direcciones de una expresion declaration.expression
                        expcode = declaration.expression.translate(self,indent)
                        if not isinstance(expcode,Value): 
                            functioncode+=expcode
                            if(vartype==""):functioncode+="\t"+declaration.name+"="+self.getLastTemp()+"\n" #asigna el valor del ultimo temporal que contiene el valor de la expresion
                            else: functioncode+="\t"+declaration.name+":"+vartype+"="+self.getLastTemp()+"\n" #asigna el valor del ultimo temporal que contiene el valor de la expresion
                        else:
                            if(vartype==""):functioncode+="\t"+declaration.name+"="+str(expcode.value)+"\n" #asigna el valor de la expresion
                            else: functioncode+="\t"+declaration.name+":"+vartype+"="+str(expcode.value)+"\n" #asigna el valor de la expresion
        # statements
        for statement in instruction.block.statements:
            if isinstance(statement,Sentence):
                old_stdout = sys.stdout
                new_stdout = StringIO()
                sys.stdout = new_stdout
                print(statement)
                val1 = new_stdout.getvalue()[:-1]
                sys.stdout = old_stdout
                functioncode+=(indent*"\t")+str(val1)+"\n"
            if(isinstance(statement,StatementReturn)):
                expcode=statement.expression.translate(self,indent)
                if not isinstance(expcode,Value):
                    functioncode+=expcode
                    functioncode+=(indent*"\t")+"return "+self.getLastTemp()+"\n"
                else:
                    functioncode+=(indent*"\t")+"return "+str(expcode.value)+"\n"
            elif isinstance(statement,If):
                expcode=statement.expression.translate(self,indent)
                if not isinstance(expcode,Value):
                    functioncode+=expcode
                    ifcode=(indent*"\t")+"if "+self.getLastTemp()+":\n"
                else:
                    ifcode=(indent*"\t")+"if "+str(expcode.value)+":\n"
                iflabel=(indent*"\t")+"label ."+self.generateLabel()+"\n"
                ifcode+=(indent*"\t")+"\tgoto ."+self.getLastLabel()+"\n"
                for ifstatement in statement.statements:
                    iflabel+=executeInstruction(self,ifstatement,indent,1)
                #else if list
                elselabel=""
                elsecode=""
                if(statement.statementsElse != None):
                    elselabel=(indent*"\t")+"label ."+self.generateLabel()+"\n"
                    elsecode=(indent*"\t")+"else:\n"+(indent*"\t")+"\tgoto. "+self.getLastLabel()+"\n"
                    for elsestatement in statement.statementsElse:
                        elselabel+=executeInstruction(self,elsestatement,indent,1)
                    elselabel+=(indent*"\t")+"label ."+self.generateLabel()+"\n"
                    iflabel+=(indent*"\t")+"goto ."+self.getLastLabel()+"\n"
                else:
                    elselabel+=(indent*"\t")+"label ."+self.generateLabel()+"\n"
                    elsecode=(indent*"\t")+"else:\n"+(indent*"\t")+"\tgoto. "+self.getLastLabel()+"\n"
                functioncode+=ifcode+elsecode+iflabel+elselabel
            elif isinstance(statement,Asignment):
                if statement.expression !=None:
                    expcode=statement.expression.translate(self,indent)
                    if not isinstance(expcode,Value):
                        functioncode+=expcode
                        functioncode+=(indent*"\t")+statement.name+"="+self.getLastTemp()+"\n"
                    else:
                        functioncode+=(indent*"\t")+statement.name+"="+str(expcode.value)+"\n"
                else:
                    functioncode += "#SelectF1" #asignment of select
            elif(isinstance(statement,Call) or isinstance(statement,Excute)):
                params="("
                for expression in statement.params:
                    expcode=expression.translate(self,indent)
                    if not isinstance(expcode,Value):
                        functioncode+=expcode
                        params+=self.getLastTemp()+", "
                    else:
                        params+=str(expcode.value)+", "
                functioncode+=(indent*"\t")+statement.name+params[:-2]+")\n"
        if(len(instruction.block.statements)==0): functioncode+="\tprint(1)\n"
        # save functioncode in TypeChecker
        archivo = open("C3D.py", 'a')
        archivo.write("\n"+(indent*"\t")+"createFunction('"+functionname+"','''"+functioncode+"''',"+str(replace)+")\n") 
        archivo.close()
        self.plcode += functioncode
    elif(isinstance(instruction,StatementReturn)):
        code = ""
        expcode=instruction.expression.translate(self,indent)
        if not isinstance(expcode,Value):
            code+=expcode
            code+=(indent*"\t")+"return "+self.getLastTemp()+"\n"
        else:
            code+=(indent*"\t")+"return "+str(expcode.value)+"\n"
        return code
    elif(isinstance(instruction,Asignment)):
        code = ""
        if instruction.expression !=None:
            expcode=instruction.expression.translate(self,indent)
            if not isinstance(expcode,Value):
                code+=expcode
                code+=(indent*"\t")+instruction.name+"="+self.getLastTemp()+"\n"
            else:
                code+=(indent*"\t")+instruction.name+"="+str(expcode.value)+"\n"
        else:
            code += "#SelectF1"
        return code
    elif(isinstance(instruction,Call) or isinstance(instruction,Excute)):
        code = "\n"
        params="("
        if instruction.params != None:
            for expression in instruction.params:
                expcode=expression.translate(self,indent)
                if not isinstance(expcode,Value):
                    code+=expcode
                    params+=self.getLastTemp()+", "
                else:
                    params+=str(expcode.value)+", "
            if(main==0): 
                code+="\n"+(indent*"\t")+"print_text('"+instruction.name+"',"+instruction.name+params[:-2]+"),2)\n"
                code+="\n"+(indent*"\t")+"print("+instruction.name+params[:-2]+"))\n"
                archivo = open("C3D.py", 'a')
                archivo.write(code) 
                archivo.close()
            else:
                code+=(indent*"\t")+instruction.name+params[:-2]+")\n"
        else:
            if(main==0): 
                code+="\n"+(indent*"\t")+"print_text('"+instruction.name+"',"+instruction.name+"(),2)\n"
                code+="\n"+(indent*"\t")+"print("+instruction.name+"())\n"
                archivo = open("C3D.py", 'a')
                archivo.write(code) 
                archivo.close()
            else:
                code+=(indent*"\t")+instruction.name+"()\n"
        return code
    elif isinstance(instruction,If):
        code = ""
        expcode=instruction.expression.translate(self,indent)
        if not isinstance(expcode,Value):
            code+=expcode
            ifcode=(indent*"\t")+"if "+self.getLastTemp()+":\n"
        else:
            ifcode=(indent*"\t")+"if "+str(expcode.value)+":\n"
        iflabel=(indent*"\t")+"label ."+self.generateLabel()+"\n"
        ifcode+=(indent*"\t")+"\tgoto ."+self.getLastLabel()+"\n"
        for ifstatement in instruction.statements:
            iflabel+=executeInstruction(self,ifstatement,indent,1)
        #else if list
        elselabel=""
        elsecode=""
        if(instruction.statementsElse != None):
            elselabel=(indent*"\t")+"label ."+self.generateLabel()+"\n"
            elsecode=(indent*"\t")+"else:\n"+(indent*"\t")+"\tgoto. "+self.getLastLabel()+"\n"
            for elsestatement in instruction.statementsElse:
                elselabel+=executeInstruction(self,elsestatement,indent,1)
            elselabel+=(indent*"\t")+"label ."+self.generateLabel()+"\n"
            iflabel+=(indent*"\t")+"goto ."+self.getLastLabel()+"\n"
        code+=ifcode+elsecode+iflabel+elselabel
        return code
    elif isinstance(instruction,DropFunction):
        archivo = open("C3D.py", 'a')
        archivo.write("\n"+(indent*"\t")+"deleteFunction('"+instruction.name+"')\n") 
        archivo.close()

def createFunction(functionname:str,functioncode:str,replace:bool):
    res = TCcreateFunction(functionname,functioncode,replace)
    if res==1:
        print("Function "+functionname+" stored")
        print_success("MESSAGE","Function "+functionname+" stored",2)
    elif res==2:
        print("Function "+functionname+" replaced")
        print_success("MESSAGE","Function "+functionname+" replaced",2)
    else:
        print("Function "+functionname+" already exists")
        print_error("SEMANTIC","Function "+functionname+" already exists",2)

def deleteFunction(function:str):
    ans = TCdeleteFunction(function)
    if(ans == 1):
        print("Function "+str(function)+" droped")
        print_success("MESSAGE","Function "+str(function)+" droped",2)
    else: 
        print("Function "+str(function)+" does not exist")
        print_error("SEMANTIC","Function "+str(function)+" does not exist",2)

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