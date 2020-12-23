from Interpreter.Instruction.instruction import Instruction

from Statics.console import Console
from Statics.symbolTable import SymbolTable
from Scripts.jsonMode import createTable
from Scripts.jsonMode import alterAddPK


class Create_tb(Instruction):   # Crear tabla
    def __init__(self, exp1, attributesList):
        self.exp1 = exp1
        self.attributesList = attributesList

    def execute(self, env):
        print("Se ejecutó la instrucción 'CREATE TABLE'")
        tableName = self.exp1.getValue(env)

        table = {}
        pkList = []

        for attr in self.attributesList:
            for key in attr:
                if key == 'len':
                    attr[key] = attr[key].getValue(env)
                elif key == 'pk':
                    index = self.attributesList.index(attr)
                    pkList.append(index)
            table[attr['id']] = attr

            symbol = (attr['id'], attr['type'], tableName)
            SymbolTable.add(symbol)

        result = createTable(env.currentDB, tableName,
                             len(self.attributesList))
        Console.add('CREATE TABLE: %s' % result)

        if (len(pkList) != 0):
            result = alterAddPK(env.currentDB, tableName, pkList)
            Console.add('ALTER ADD PK: %s' % result)

        env.addTable(env.currentDB, {tableName: table})
