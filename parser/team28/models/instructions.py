class Instruction:
    '''Clase abstracta'''

class Select(Instruction):
    '''
        Select recibe un array con todas los parametros
    '''
    def __init__(self,  instrs) :
        self.instrs = instrs
            
class From(Instruction):
    '''
        FROM recibe una tabla en la cual buscar los datos
    '''
    def __init__(self,  table) :
        self.table = table
    
class Where(Instruction):
    '''
        WHERE recibe una condicion logica 
    '''
    def __init__(self,  condition) :
        self.condition = condition
    
class GroupBy(Instruction):
    '''
        * The GROUP BY statement groups rows 
            that have the same values into summary rows
        * Recibe una lista de nombres de columnas
    '''
    def __init__(self,  column_names) :
        self.column_names = column_names
    
class Having(Instruction):
    '''
        HAVING recibe una condicion logica
    '''
    def __init__(self,  condition) :
        self.condition = condition
    
class Between(Instruction):
    '''
        BETWEEN recibe 2 parametros
        Sintax: BETWEEN value1 AND value2
    '''
    def __init__(self,  value1, value2) :
        self.value1 = value1
        self.value2 = value2
'''
    FUNCIONES MATEMATICAS 
'''
class Abs(Instruction):
    '''
        Valor absoluto de una columna tipo entero o de un valor.
    '''
    def __init__(self,  value) :
        self.value = value

class Cbrt(Instruction):
    '''
        Raiz Cubica de un numero o una columna tipo entero.
    '''
    def __init__(self,  value) :
        self.value = value

class Ceil(Instruction):
    '''
        Redondear cualquier valor decimal positivo o negativo como
        mayor que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value

class Ceiling(Instruction):
    '''
        Redondear cualquier valor decimal positivo o
        negativo como mayor que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value

class Degrees(Instruction):
    '''
        Se usa para devolver los valores en grados de radianes 
        como se especifica en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value

class Div(Instruction):
    '''
        Se utiliza para devolver el cociente entero de
        una división como se especifica en el argumento.
    '''
    def __init__(self,  dividendo, divisor) :
        self.dividendo = dividendo
        self.divisor = divisor

class Exp(Instruction):
    '''
        La función se usa para devolver la exponenciación de
        un número como se especifica en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value

class Factorial(Instruction):
    '''
        Se puede utilizar la libreria Math de Python **
    '''
    def __init__(self,  value) :
        self.value = value

class Floor(Instruction):
    '''
        Se usa para devolver el valor después de redondear 
        cualquier valor decimal positivo o negativo 
        como más pequeño que el argumento.
    '''
    def __init__(self,  value) :
        self.value = value

class Gcd(Instruction):
    '''
        Se puede utilizar la libreria Math de Python. 
        Maximo Comun Divisor *
    '''
    def __init__(self,  value) :
        self.value = value

class Ln(Instruction):
    '''
        Logaritmo natural de un numero ***
    '''
    def __init__(self,  value) :
        self.value = value

class Log(Instruction):
    '''
        Logaritmo base 2 (no seria base 10?) de un número.
    '''
    def __init__(self,  value) :
        self.value = value

class Mod(Instruction):
    '''
        La función se usa para devolver el resto de una
        división de dos números, como se especifica 
        en el argumento
    '''
    def __init__(self,  value1, value2) :
        self.value1 = value1
        self.value2 = value2

class Pi(Instruction):
    '''
        Retorna el valor de la constant PI
        ***** TODO: SIN ARGUMENTOS *****
    '''
    def __init__(self,  value) :
        self.value = value

class Power(Instruction):
    '''
        La función se usa para devolver el valor de un 
        número elevado a la potencia de otro número, 
        proporcionado en el argumento.
    '''
    def __init__(self, base, exp) :
        self.base = base
        self.exp = exp

class Radians(Instruction):
    '''
        La función se usa para devolver el valor en radianes 
        a partir de grados, proporcionado en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value

class Round(Instruction):
    '''
        La función se usa para devolver el valor después de 
        redondear un número hasta un decimal específico, 
        proporcionado en el argumento.
    '''
    def __init__(self,  value) :
        self.value = value






