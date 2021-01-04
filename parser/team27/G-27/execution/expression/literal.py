from execution.abstract.expression import *

class Literal(Expression):
    """
    value: valor puro (es decir un número, un string, true | false, null)
    typ: recibe un enum ubicado en el archivo typ.py en la carpeta  symbol
    """
    def __init__(self, value, typ, row, column):
        Expression.__init__(self, row, column)
        self.value = value
        self.typ = typ
    
    def execute(self, environment):
        valor = self.value
        tipo = self.typ
        return {'value':valor, 'typ':tipo}
