import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/libraries')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
from function import *
from typ import *
from trigonometric_functions import atan2
from literal import *
# pendiente
class Atan2(Function):
    def __init__(self, input,input2, row, column):
        Function.__init__(self,row,column)
        self.input = input #dividendo
        self.input2 = input2 #divisor
    
    def execute(self, environment):
        #input es una lista
        # los valores del imput deben estar en el rango de [infinito,infinito]   
        if isinstance(self.input,list):
            respuesta = []
            for val in self.input:
                value = val.execute(environment)
                if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                    return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }

                result = atan2(value['value'])
                respuesta.append({'value':result, 'typ': value['typ']})
            return respuesta
        #input valor puntual
        else:
            value = self.input.execute(environment)
            if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }

            return [{'value':atan2(value['value']), 'typ': Type.DECIMAL}]

# prueba

val1 = Literal(,Type.DECIMAL,1,2)
valorabs = Atan(val1,2,3).execute("")
#valorabs = acosd(1)
print(valorabs)