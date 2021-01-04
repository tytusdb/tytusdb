
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