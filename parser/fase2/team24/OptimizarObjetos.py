
class Asignacion():
    def __init__(self, indice, operador1, operador2 = "", signo = "", cadena = False):
        self.indice = indice
        self.operador1 = operador1
        self.operador2 = operador2
        self.signo = signo
        self.cadena = cadena
    """
    indice: Es el nombre del asignado
    operador1: Es el operador de la izquierda
    operador2: Es el operador de la derecha
    signo: signo que existe entre operadores
    Ejemplo: 
    t2 = a - g
    t2 -> indice
    a -> operador1
    b -> operador2
    - -> signo
    """

class Optimizado():
    def __init__(self, regla, original, resultado):
        self.regla = regla
        self.original = original
        self.resultado = resultado
    """
    regla: Referencia al numerro de regla que se utilizo
    original: Muestra el codigo original
    resultado: Muestra el resultado de la optimizacion
    """

class Temporal():
    def __init__(self, indice, valor, cadena = False):
        self.indice = indice
        self.valor = valor
        self.cadena = cadena