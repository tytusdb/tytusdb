
class Instruction:
    ''' '''

class CreateFunction(Instruction):
    def __init__(self, name, replace, params, returnValue, block):
        self.name = name
        self.replace = replace
        self.params = params
        self.returnValue = returnValue
        self.block = block
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"CreateFunction\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CREATE") + hash(self)) + '\n'
        dot += str(hash("CREATE") + hash(self)) + \
            '[label=\"' + "CREATE" + '\"]\n'
        if(self.replace):
            dot += str(hash(self)) + '->' + \
            str(hash("OR") + hash(self)) + '\n'
            dot += str(hash("OR") + hash(self)) + \
                '[label=\"' + "OR" + '\"]\n'
            dot += str(hash(self)) + '->' + \
            str(hash("REPLACE") + hash(self)) + '\n'
            dot += str(hash("REPLACE") + hash(self)) + \
                '[label=\"' + "REPLACE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("FUNCTION") + hash(self)) + '\n'
        dot += str(hash("FUNCTION") + hash(self)) + \
            '[label=\"' + "FUNCTION" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        if(self.params != None):
            dot += str(hash(self)) + '->' + \
            str(hash("Params") + hash(self)) + '\n'
            dot += str(hash("Params") + hash(self)) + \
                '[label=\"' + "Params" + '\"]\n'
            for param in self.params:
                dot += param.graphAST('',str(hash("Params") + hash(self)))
        if(self.returnValue != None):
            dot+= self.returnValue.graphAST('',str(hash(self)))
        dot += self.block.graphAST('',str(hash(self)))
        return dot

class CreateParam(Instruction):
    def __init__(self, name, type, out):
        self.name = name
        self.type = type
        self.out = out
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"CreateParam\"]\n'
        if(self.name != None):
            dot += str(hash(self)) + '->' + \
            str(hash(self.name) + hash(self)) + '\n'
            dot += str(hash(self.name) + hash(self)) + \
                '[label=\"' + self.name + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.type[0]) + hash(self)) + '\n'
        dot += str(hash(self.type[0]) + hash(self)) + \
            '[label=\"' + self.type[0] + '\"]\n'
        return dot

class CreateReturn(Instruction):
    def __init__(self, type, paramsTable):
        self.type = type #Si es un tipo paramasTable esta vacio
        self.paramsTable = paramsTable #Si es una tabla typo esta vacio
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"CreateReturn\"]\n'
        if(self.type != None):
            dot += str(hash(self)) + '->' + \
            str(hash(self.type[0]) + hash(self)) + '\n'
            dot += str(hash(self.type[0]) + hash(self)) + \
                '[label=\"' + self.type[0] + '\"]\n'
        return dot

class BlockFunction(Instruction):
    def __init__(self, declarations, statements):
        self.declarations = declarations #Bloque DECLARE
        self.statements = statements #Bloque de statements
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"BlockFunction\"]\n'
        if(self.declarations != None):
            dot += str(hash(self)) + '->' + \
            str(hash("declarationBlock") + hash(self)) + '\n'
            dot += str(hash("declarationBlock") + hash(self)) + \
                '[label=\"' + "declarationBlock" + '\"]\n'
            for declaration in self.declarations:
                dot+=declaration.graphAST('',str(hash("declarationBlock") + hash(self)))
        dot += str(hash(self)) + '->' + \
        str(hash("statementsBlock") + hash(self)) + '\n'
        dot += str(hash("statementsBlock") + hash(self)) + \
            '[label=\"' + "statementsBlock" + '\"]\n'
        for statement in self.statements:
            dot+=statement.graphAST('',str(hash("statementsBlock") + hash(self)))
        return dot

class VariableDeclaration(Instruction):
    def __init__(self, name, constant, type, collate, notNull, expression):
        self.name = name
        self.constant = constant
        self.type = type
        self.collate = collate
        self.notNull = notNull
        self.expression = expression
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"VariableDeclaration\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        if self.constant:
            dot += str(hash(self)) + '->' + \
            str(hash("CONSTANT") + hash(self)) + '\n'
            dot += str(hash("CONSTANT") + hash(self)) + \
                '[label=\"' + "CONSTANT" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.type[0]) + hash(self)) + '\n'
        dot += str(hash(self.type[0]) + hash(self)) + \
            '[label=\"' + self.type[0] + '\"]\n'
        if self.collate != None:
            dot += str(hash(self)) + '->' + \
            str(hash("'"+self.collate+"'") + hash(self)) + '\n'
            dot += str(hash("'"+self.collate+"'") + hash(self)) + \
                '[label=\"' + "'"+self.collate+"'" + '\"]\n'
        if self.notNull:
            dot += str(hash(self)) + '->' + \
            str(hash("NOT") + hash(self)) + '\n'
            dot += str(hash("NOT") + hash(self)) + \
                '[label=\"' + "NOT" + '\"]\n'
        dot += str(hash(self)) + '->' + \
            str(hash("NULL") + hash(self)) + '\n'
        dot += str(hash("NULL") + hash(self)) + \
                '[label=\"' + "NULL" + '\"]\n'
        if self.expression != None:
            dot+=self.expression.graphAST('',str(hash(self)))
        return dot

class AliasDeclaration(Instruction):
    def __init__(self, newName, oldName):
        self.newName = newName
        self.oldName = oldName
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"AliasDeclaration\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.newName) + hash(self)) + '\n'
        dot += str(hash(self.newName) + hash(self)) + \
            '[label=\"' + self.newName + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.oldName) + hash(self)) + '\n'
        dot += str(hash(self.oldName) + hash(self)) + \
            '[label=\"' + self.oldName + '\"]\n'
        return dot

class TypeDeclaration(Instruction):
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"TypeDeclaration\"]\n'
        return dot

class StatementReturn(Instruction):
    def __init__(self, expression, next, collate, select):
        self.expression = expression
        self.next = next
        self.collate = collate
        self.select = select
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"StatementReturn\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("RETURN") + hash(self)) + '\n'
        dot += str(hash("RETURN") + hash(self)) + \
            '[label=\"' + "RETURN" + '\"]\n'
        if self.expression != None: dot += self.expression.graphAST('',str(hash(self)))
        else: dot+=self.select.graphAST('',str(hash(self)))
        return dot 
class Asignment(Instruction):
    def __init__(self, name, expression, select):
        self.name = name
        self.expression = expression
        self.select = select
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Asignment\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        if self.expression != None: 
            dot += self.expression.graphAST('',str(hash(self)))
        else: 
            dot+=self.select.graphAST('',str(hash(self)))
        return dot

class DropFunction(Instruction):
    def __init__(self, name, ifexists):
        self.name = name
        self.ifexists = ifexists
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"DropFunction\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        return dot 

class Call(Instruction):
    def __init__(self, name, params):
        self.name = name 
        self.params = params
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Call\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CALL") + hash(self)) + '\n'
        dot += str(hash("CALL") + hash(self)) + \
            '[label=\"' + "CALL" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        if(self.params != None):
            dot += str(hash(self)) + '->' + \
            str(hash("Params") + hash(self)) + '\n'
            dot += str(hash("Params") + hash(self)) + \
                '[label=\"' + "Params" + '\"]\n'
            for param in self.params:
                dot += param.graphAST('',str(hash("Params") + hash(self)))
        return dot 

class Excute(Instruction):
    def __init__(self, name, params):
        self.name = name 
        self.params = params
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Execute\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("EXECUTE") + hash(self)) + '\n'
        dot += str(hash("EXECUTE") + hash(self)) + \
            '[label=\"' + "EXECUTE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash(self.name) + hash(self)) + '\n'
        dot += str(hash(self.name) + hash(self)) + \
            '[label=\"' + self.name + '\"]\n'
        if(self.params != None):
            dot += str(hash(self)) + '->' + \
            str(hash("Params") + hash(self)) + '\n'
            dot += str(hash("Params") + hash(self)) + \
                '[label=\"' + "Params" + '\"]\n'
            for param in self.params:
                dot += param.graphAST('',str(hash("Params") + hash(self)))
        return dot 

class If(Instruction):
    def __init__(self, expression, statements, elseifList, statementsElse):
        self.expression = expression 
        self.statements = statements 
        self.elsifList = elseifList 
        self.statementsElse = statementsElse
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"If\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("IF") + hash(self)) + '\n'
        dot += str(hash("IF") + hash(self)) + \
            '[label=\"' + "IF" + '\"]\n'
        dot+= self.expression.graphAST('',str(hash(self)))
        dot += str(hash(self)) + '->' + \
        str(hash("THEN") + hash(self)) + '\n'
        dot += str(hash("THEN") + hash(self)) + \
            '[label=\"' + "THEN" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("Statements") + hash(self)) + '\n'
        dot += str(hash("Statements") + hash(self)) + \
            '[label=\"' + "Statements" + '\"]\n'
        for statement in self.statements:
            dot+= statement.graphAST('',str(hash("Statements") + hash(self)))
        if self.elsifList != None:
            dot += str(hash(self)) + '->' + \
            str(hash("elsifList") + hash(self)) + '\n'
            dot += str(hash("elsifList") + hash(self)) + \
                '[label=\"' + "elsifList" + '\"]\n'
            for elseif in self.elsifList:
                dot+= elseif.graphAST('',str(hash("elsifList") + hash(self)))
        if self.statementsElse != None:
            dot += str(hash(self)) + '->' + \
            str(hash("Else") + hash(self)) + '\n'
            dot += str(hash("Else") + hash(self)) + \
                '[label=\"' + "Else" + '\"]\n'
            for statement in self.statementsElse:
                dot+= statement.graphAST('',str(hash("Else") + hash(self)))
        dot += str(hash(self)) + '->' + \
        str(hash("END") + hash(self)) + '\n'
        dot += str(hash("END") + hash(self)) + \
            '[label=\"' + "END" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("EIF") + hash(self)) + '\n'
        dot += str(hash("EIF") + hash(self)) + \
            '[label=\"' + "IF" + '\"]\n'
        return dot 

class ElsIf(Instruction):
    def __init__(self, expression, statements):
        self.expression = expression 
        self.statements = statements
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"ElsIf\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ELSE") + hash(self)) + '\n'
        dot += str(hash("ELSE") + hash(self)) + \
            '[label=\"' + "ELSE" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("IF") + hash(self)) + '\n'
        dot += str(hash("IF") + hash(self)) + \
            '[label=\"' + "IF" + '\"]\n'
        dot += self.expression.graphAST('',str(hash(self)))
        dot += str(hash(self)) + '->' + \
        str(hash("Statements") + hash(self)) + '\n'
        dot += str(hash("Statements") + hash(self)) + \
            '[label=\"' + "Statements" + '\"]\n'
        for statement in self.statements:
            dot+= statement.graphAST('',str(hash("Statements") + hash(self)))
        return dot 

class Case(Instruction):
    def __init__(self, expression, whenList, statementsElse):
        self.expression = expression 
        self.whenList = whenList 
        self.statementsElse = statementsElse
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"Case\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("CASE") + hash(self)) + '\n'
        dot += str(hash("CASE") + hash(self)) + \
            '[label=\"' + "CASE" + '\"]\n'
        if self.expression != None: dot += self.expression.graphAST('',str(hash(self)))
        dot += str(hash(self)) + '->' + \
        str(hash("whenList") + hash(self)) + '\n'
        dot += str(hash("whenList") + hash(self)) + \
            '[label=\"' + "whenList" + '\"]\n'
        for when in self.whenList:
            dot += when.graphAST('',str(hash("whenList") + hash(self)))
        if self.statementsElse != None:
            dot += str(hash(self)) + '->' + \
            str(hash("ElseStatements") + hash(self)) + '\n'
            dot += str(hash("ElseStatements") + hash(self)) + \
                '[label=\"' + "ElseStatements" + '\"]\n'
            for statement in self.statementsElse:
                dot+= statement.graphAST('',str(hash("ElseStatements") + hash(self)))
        dot += str(hash(self)) + '->' + \
        str(hash("END") + hash(self)) + '\n'
        dot += str(hash("END") + hash(self)) + \
            '[label=\"' + "END" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("ECASE") + hash(self)) + '\n'
        dot += str(hash("ECASE") + hash(self)) + \
            '[label=\"' + "CASE" + '\"]\n'
        return dot 

class When(Instruction):
    def __init__(self, expressions, statements):
        self.expressions = expressions
        self.statements = statements
    def graphAST(self, dot, parent):
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"When\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("WHEN") + hash(self)) + '\n'
        dot += str(hash("WHEN") + hash(self)) + \
            '[label=\"' + "WHEN" + '\"]\n'
        dot += str(hash(self)) + '->' + \
        str(hash("expressionList") + hash(self)) + '\n'
        dot += str(hash("expressionList") + hash(self)) + \
            '[label=\"' + "expressionList" + '\"]\n'
        for expression in self.expressions:
            dot+= expression.graphAST('',str(hash("expressionList") + hash(self)))
        dot += str(hash(self)) + '->' + \
        str(hash("statementList") + hash(self)) + '\n'
        dot += str(hash("statementList") + hash(self)) + \
            '[label=\"' + "statementList" + '\"]\n'
        for statement in self.statements:
            dot+= statement.graphAST('',str(hash("statementList") + hash(self)))
        return dot 