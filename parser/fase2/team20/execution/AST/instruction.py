
class Instruction:
    ''' '''

class CreateFunction(Instruction):
    def __init__(self, name, replace, params, returnValue, block):
        self.name = name
        self.replace = replace
        self.params = params
        self.returnValue = returnValue
        self.block = block

class CreateParam(Instruction):
    def __init__(self, name, type, out):
        self.name = name
        self.type = type
        self.out = out

class CreateReturn(Instruction):
    def __init__(self, type, paramsTable):
        self.type = type #Si es un tipo paramasTable esta vacio
        self.paramsTable = paramsTable #Si es una tabla typo esta vacio

class BlockFunction(Instruction):
    def __init__(self, declarations, statements):
        self.declarations = declarations #Bloque DECLARE
        self.statements = statements #Bloque de statements

class VariableDeclaration(Instruction):
    def __init__(self, name, constant, type, collate, notNull, expression):
        self.name = name
        self.constant = constant
        self.type = type
        self.collate = collate
        self.notNull = notNull
        self.expression = expression

class AliasDeclaration(Instruction):
    def __init__(self, newName, oldName):
        self.newName = newName
        self.oldName = oldName

class TypeDeclaration(Instruction):
    def __init__(self, name, type):
        self.name = name
        self.type = type

class StatementReturn(Instruction):
    def __init__(self, expression, next, collate, select):
        self.expression = expression
        self.next = next
        self.collate = collate
        self.select = select 

class Call(Instruction):
    def __init__(self, name, params):
        self.name = name 
        self.params = params 

class Excute(Instruction):
    def __init__(self, name, params):
        self.name = name 
        self.params = params 

class If(Instruction):
    def __init__(self, expression, statements, elseifList, statementsElse):
        self.expression = expression 
        self.statements = statements 
        self.elsifList = elseifList 
        self.statementsElse = statementsElse 

class ElsIf(Instruction):
    def __init__(self, expression, statements):
        self.expression = expression 
        self.statements = statements 

class Case(Instruction):
    def __init__(self, expression, whenList, statementsElse):
        self.expression = expression 
        self.whenList = whenList 
        self.statementsElse = statementsElse 

class When(Instruction):
    def __init__(self, expressions, statements):
        self.expressions = expressions
        self.statements = statements 