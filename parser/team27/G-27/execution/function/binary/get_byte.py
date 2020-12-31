from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.bstring_functions import get_byte

class Get_Byte:
    def __init__(self, input1, input2, row, column):
        Function.__init__(self,row,column)
        self.input1 = input1
        self.input2 = input2

    def execute(self, environment):
    #Input es una lista        
        if isinstance(self.input1,list):
            respuesta = []
            for val in self.input1:
                value = val.execute(environment)
                value2 = self.input2.execute(environment)
                if value['typ'] != Type.STRING:
                    return {'Error':"El valor " + value['value'] + " no es String", 'linea':self.row,'columna':self.column }
                if value2['typ'] != Type.INT:
                    return {'Error':"El valor " + value2['value'] + " no es Entero", 'linea':self.row,'columna':self.column }
                result = get_byte(value['value'], value2['value'])
                respuesta.append({'value':result, 'typ': Type.INT})
            return respuesta
        #Input valor puntual
        else:
            input1 = self.input1.execute(environment)
            input2 = self.input2.execute(environment)
            
            if input1['typ'] != Type.STRING or input2['typ'] != Type.INT :
                incorrect =  [input1['value'] + " no es String" , str(input2['value']) + " no es Entero"]
                error = incorrect[0] if (input1['typ'] != Type.STRING) else  ""
                error += incorrect[1] if (input2['typ'] != Type.INT) else  ""
                return {'Error':"El valor " + error, 'linea':self.row,'columna':self.column }
            return {'value': get_byte(input1['value'],input2['value']), 'typ': Type.STRING}


