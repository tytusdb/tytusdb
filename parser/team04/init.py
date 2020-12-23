from Interpreter import lex
from Interpreter import ascparse
from Interpreter.ast import Ast

expresiones = "./Scripts/Consultas.sql"

data = open(expresiones).read()
print(data)
root = ascparse.parse(data)
AST = Ast(root)
AST.execute()
