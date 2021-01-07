from Interpreter.Instruction.instruction import Instruction


from Scripts import jsonMode as j

from Statics.console import Console
from Scripts.jsonMode import alterDatabase


class Alter_db(Instruction):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def execute(self, env):
        print("Se ejecutó la instrucción 'ALTER DATABASE'")
        resultado = alterDatabase(
            self.exp1.getValue(env), self.exp2.getValue(env))
        # print(self.expression.getValue(env))
        Console.add(resultado)
