from Interpreter.Instruction.instruction import Instruction

from Scripts import jsonMode as j

from Statics.console import Console
from Scripts.jsonMode import alterTable
from Scripts.jsonMode import alterAddColumn
from Scripts.jsonMode import alterDropColumn

class Alter_tb(Instruction):
    def __init__(self, exp1, exp2, accion):
        self.exp1 = exp1 #TablaOld
        self.exp2 = exp2 #TablaNew
        self.accion = accion #Rename simple
    
    def execute(self, env):
        print("Se ejecutó la instrucción 'ALTER TABLE'")
        #aqui se debe evaluar la acción relacionada al alter
        #Acciones: RENAME SIMPLE O RENAME COLUMN
        if self.accion == 'COLUMN':
            print("Se ejecutó la función RENAME COLUMN")
        elif self.accion == 'TO':
            print("Se ejecutó la función RENAME TO")
            resultado = alterTable(
                env.currentDB, self.exp1.getValue(env), self.exp2.getValue(env))
            Console.add(resultado)

#correspondiente a instrucción ALTER TABLE ADD COLUMN
class Alter_tb_AC(Instruction):
    def __init__(self, tabla, accion, default:None):
        self.tabla = tabla
        self.accion = accion
        self.default = default

    def execute(self, env):
        print("Se ejecutó la instrucción 'ALTER TABLE ADD'")
        #Aqui se deben validar las acciones
        #Las acciones pueden ser
        #aqui se debe evaluar la acción relacionada al alter
        #Acciones: ADD CHECK, ADD CONSTRAINT, ADD FOREIGN KEY
        print("Se ejecutó una función ADD COLUMN.")
        resultado = alterAddColumn(
            env.currentDB, self.tabla.getValue(env), self.default.getValue(env))
        Console.add(resultado)  

class Alter_tb_DC(Instruction):
    def __init__(self, tabla, accion, columnNumber):
        self.tabla = tabla
        self.columnNumber = columnNumber
        self.accion = accion
    
    def execute(self, env):
        #Se debe evaluar que tipo de DROP viene: DROP COLUMN, DROP CONSTRAINT
        if self.accion == 'COLUMN':
            print("Se ejecutó la instrucción 'ALTER TABLE DROP COLUMN'")
            resultado = alterDropColumn(env.currentDB, self.tabla.getValue(env), self.columnNumber.getValue(env))
            Console.add(resultado)
        elif self.accion == 'CONSTRAINT':
            print("Se ejecutó un DROP CONSTRAINT")

class Alter_tb_AddFK(Instruction):
    def __init__(self, tabla, parametro, referencia):
        self.tabla = tabla
        self.parametro = parametro
        self.referencia = referencia
    
    def execute(self, env):
        print("Se ejecutó la instrucción ADD FOREIGN KEY")

class Alter_tb_AddCheck(Instruction):
    def __init__(self, tabla, parametro, valor):
        self.tabla = tabla
        self.parametro = parametro
        self.valor = valor
    
    def execute(self, env):
        print("Se ejecutó la instrucción ADD CHECK")

class Alter_tb_AddConstraint(Instruction):
    def __init__(self, tabla, parametro, valor):
        self.tabla = tabla
        self.parametro = parametro
        self.valor = valor
    
    def execute(self, env):
        print("Se ejecutó la instrucción ADD FOREIGN KEY")

class Alter_tb_AlterColumn(Instruction):
    def __init__(self, tabla, parametro, valor):
        self.tabla = tabla
        self.parametro = parametro
        self.valor = valor
    
    def execute(self, env):
        print("Se ejecutó la instrucción ALTER COLUMN")
