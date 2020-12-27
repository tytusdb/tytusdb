from Interpreter.Instruction.instruction import Instruction
from Statics.console import Console
from Scripts.jsonMode import *



class truncatef(Instruction):
    def __init__(self, tabla):
        self.tabla = tabla
            
 
    def execute(self, env):
        print("Se ejecutó la instrucción 'TRUNCATE ó DELETE * FROM'")
        resultado = truncate(env.currentDB, self.tabla.getValue(env) ) 
        Console.add(resultado)
      

