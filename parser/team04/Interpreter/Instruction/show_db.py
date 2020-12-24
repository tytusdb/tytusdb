
from Interpreter.Instruction.instruction import Instruction


from Statics.console import Console
from Scripts.jsonMode import showDatabases

class Show_db(Instruction):
    def __init__(self, expression):
        self.expression = expression

    def execute(self, env):
        print("Se ejecutó la instrucción 'SHOW DATABASE'")
        resultado = showDatabases()
        #print(self.expression.getValue(env))
        Console.add(resultado)