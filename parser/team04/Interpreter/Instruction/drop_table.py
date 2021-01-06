
from Interpreter.Instruction.instruction import Instruction

from Statics.console import Console
from Scripts.jsonMode import dropTable



class DropTable(Instruction):
    def __init__(self, expression):
        self.expression = expression
 
    def execute(self, env):
        print("Se ejecutó la instrucción 'DROP TABLE'") 
        resultado = dropTable(env.currentDB, self.expression.getValue(env) ) 
        Console.add(resultado)
        Console.add(self.expression.getValue(env))
