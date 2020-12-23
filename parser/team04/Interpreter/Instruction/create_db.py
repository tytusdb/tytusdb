
from Interpreter.Instruction.instruction import Instruction

from Statics.console import Console
from Scripts.jsonMode import createDatabase


class Create_db(Instruction):
    def __init__(self, expression):
        self.expression = expression

    def execute(self, env):
        print("Se ejecutó la instrucción 'CREATE DATABASE'")
        resultado = createDatabase(self.expression.getValue(env))
        # print(self.expression.getValue(env))
        Console.add(resultado)
