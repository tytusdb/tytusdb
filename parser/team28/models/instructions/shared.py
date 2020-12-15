#TODO: DISTINCT
from abc import abstractmethod
from models.nodo import Node
class Instruction:
    '''Clase abstracta'''
    @abstractmethod
    def execute(self):
        ''' recibe hijos paras el ast grafico '''
        pass

class BinaryOperation(Instruction):
    '''
        Una operacion binaria recibe, sus dos operandos y el operador
    '''
    def __init__(self, value1, value2, operador) :
        self.value1 = value1
        self.value2 = value2
        self.operador = operador
    
    def __repr__(self):
        return str(vars(self))


class Alias(Instruction):
    '''
        Alias recibe el ID original y su ALIAS
    '''
    def __init__(self, id, alias) :
        self.id = id
        self.alias = alias
    
    def __repr__(self):
        return str(vars(self))

class From(Instruction):
    '''
        FROM recibe una tabla en la cual buscar los datos
    '''
    def __init__(self,  tables) :
        self.tables = tables
    
    def __repr__(self):
        return str(vars(self))
    
class Where(Instruction):
    '''
        WHERE recibe una condicion logica 
    '''
    def __init__(self,  condition) :
        self.condition = condition
    
    def __repr__(self):
        return str(vars(self))

class GroupBy(Instruction):
    '''
        * The GROUP BY statement groups rows 
            that have the same values into summary rows
        * Recibe una lista de nombres de columnas
    '''
    def __init__(self,  column_names) :
        self.column_names = column_names
    
    def __repr__(self):
        return str(vars(self))
    
class Having(Instruction):
    '''
        HAVING recibe una condicion logica
    '''
    def __init__(self,  condition) :
        self.condition = condition
    
    def __repr__(self):
        return str(vars(self))

class Using(Instruction):
    '''
        USING recibe un array con ids
    '''
    def __repr__(self):
        return str(vars(self))
class Returning(Instruction):
    '''
        RETURNING recibe un array con ids o un asterisco
    '''
    def __init__(self,  value):
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Between(Instruction):
    '''
        BETWEEN recibe 2 parametros
        Sintax: BETWEEN value1 AND value2
    '''
    def __init__(self, opt_not, opt_simmetric,  value1, value2) :
        self.opt_not = opt_not
        self.opt_simmetric = opt_simmetric
        self.value1 = value1
        self.value2 = value2
    
    def __repr__(self):
        return str(vars(self))

'''
    FUNCIONES MATEMATICAS =======================================================================================================================
'''
class Abs(Instruction):
    '''
        Valor absoluto de una columna tipo entero o de un valor.
    '''
    def __init__(self,  value) :
        self.value = value

    def __repr__(self):
        return str(vars(self))

class Cbrt(Instruction):
    '''
        Raiz Cubica de un numero o una columna tipo entero.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Ceil(Instruction):
    '''
        Redondear cualquier valor decimal positivo o negativo como
        mayor que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Ceiling(Instruction):
    '''
        Redondear cualquier valor decimal positivo o
        negativo como mayor que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Degrees(Instruction):
    '''
        Se usa para devolver los valores en grados de radianes 
        como se especifica en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Div(Instruction):
    '''
        Se utiliza para devolver el cociente entero de
        una división como se especifica en el argumento.
    '''
    def __init__(self,  dividendo, divisor) :
        self.dividendo = dividendo
        self.divisor = divisor
    
    def __repr__(self):
        return str(vars(self))

class Exp(Instruction):
    '''
        La función se usa para devolver la exponenciación de
        un número como se especifica en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Factorial(Instruction):
    '''
        Se puede utilizar la libreria Math de Python **
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Floor(Instruction):
    '''
        Se usa para devolver el valor después de redondear 
        cualquier valor decimal positivo o negativo 
        como más pequeño que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Gcd(Instruction):
    '''
        Se puede utilizar la libreria Math de Python. 
        Maximo Comun Divisor *
    '''
    def __init__(self,  value) :
        self.value = value

    def __repr__(self):
        return str(vars(self))

class Ln(Instruction):
    '''
        Logaritmo natural de un numero ***
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Log(Instruction):
    '''
        Logaritmo base 2 (no seria base 10?) de un número.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Mod(Instruction):
    '''
        La función se usa para devolver el resto de una
        división de dos números, como se especifica 
        en el argumento
    '''
    def __init__(self,  value1, value2) :
        self.value1 = value1
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))

class Pi(Instruction):
    '''
        Retorna el valor de la constant PI
        ***** TODO: SIN ARGUMENTOS *****
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Power(Instruction):
    '''
        La función se usa para devolver el valor de un 
        número elevado a la potencia de otro número, 
        proporcionado en el argumento.
    '''
    def __init__(self, base, exp) :
        self.base = base
        self.exp = exp
    
    def __repr__(self):
        return str(vars(self))

class Radians(Instruction):
    '''
        La función se usa para devolver el valor en radianes 
        a partir de grados, proporcionado en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class Round(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

class ObjectReference(Instruction):
    '''
        ObjectReference
    '''
    def __init__(self, reference_base, reference_table, reference_column, opt_asterisk):
        self.reference_base = reference_base
        self.reference_table = reference_table
        self.reference_colunm = reference_column
        self.opt_asterisk = opt_asterisk

    def __repr__(self):
        return str(vars(self))

class ExpressionsTime(Instruction):
    '''
        ExpressionsTime
    '''
    def __init__(self, name_date, type_date, name_opt):
        self.name_date = name_date
        self.type_date = type_date
        self.name_opt = name_opt

    def __repr__(self):
        return str(vars(self))

class ExpressionsTrigonometric(Instruction):
    '''
        ExpressionsTrigonometric
    '''
    def __init__(self, type_trigonometric, expression1, optional_expression2):
        self.type_trigonometric = type_trigonometric
        self.expression1 = expression1
        self.optional_expression2 = optional_expression2

    def __repr__(self):
        return str(vars(self))

class ExpressionsGreastLeast(Instruction):
    '''
        ExpressionsGreastLeast
    '''
    def __init__(self, type_expression, lista_arr):
        self.type_expression = type_expression
        self.lista_arr = lista_arr
    def __repr__(self):
        return str(vars(self))

class MathematicalExpressions(Instruction):
    '''
        MathematicalExpressions
    '''
    def __init__(self, type_expression, lista_arr, optional_alias):
        self.type_expression = type_expression
        self.lista_arr = lista_arr
        self.optiona_alias = optional_alias
    
    def __repr__(self):
        return str(vars(self))

class UnaryOrSquareExpressions(Instruction):
    '''
    UnaryOrSquareExpressions
    '''
    def __init__(self, sign, expression_list):
        self.sign = sign
        self.expression_list = expression_list
    
    def __repr__(self):
        return str(vars(self))


class LogicalOperators(Instruction):
    '''
    LogicalOperators
    '''
    def __init__(self, value1, logical_operator, value2):
        self.value1 = value1
        self.logical_operator = logical_operator
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))





