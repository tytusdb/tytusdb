from enum import Enum
class OptimizedInstruction:
    """
    Optimización de las instrucciones en 3D
    """
    def __init__(self, row) -> None:
        self.row = row
        self.optimizable = None

    def optimize(self,generador) -> None:
        pass

    def addToCode(self, generador) -> None:
        if not self.optimizable in (None,RULES.OMISION):
            generador.addToCode(f'\t#{self.optimizable.value} aplicada')

    def toReport(self,generador) -> str:
        if not self.optimizable in (None,RULES.OMISION):
            generador.toReport(f'\t\t\t\t<tr><td scope="row">{str(self)}</td><td>{self.optimizable.value}</td><td>{self.row}</td></tr>')


# Reglas que se usan para optimizar 
class RULES(Enum):
    O1 = 'Regla 1'
    O2 = 'Regla 2'
    O3 = 'Regla 3'
    O4 = 'Regla 4'
    O5 = 'Regla 5'
    O6 = 'Regla 6'
    O7 = 'Regla 7'
    O8 = 'Regla 8'
    O9 = 'Regla 9'
    O10 = 'Regla 10'
    O11 = 'Regla 11'
    O12 = 'Regla 12'
    O13 = 'Regla 13'
    O14 = 'Regla 14'
    O15 = 'Regla 15'
    O16 = 'Regla 16'
    O17 = 'Regla 17'
    O18 = 'Regla 18'
    OMISION = 'Regla que quita partes innecesarias' 



#Ayuda de declaraciones
class TEVAL(Enum):
    SINGLE = 'SINGLE'
    OPERATION = 'OPERATION'
    FUNCTION = 'FUNCTION'

#Ayuda de tipos
class TYPE(Enum):
    TEMP = 'TEMP'
    ID = 'ID'
    NUMBER = 'NUMBER'
    CADENA = 'CADENA'
    BOOL = 'BOOL'
    RETURN = 'RETURN'