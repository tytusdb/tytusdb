from execution.abstract.function import *
from execution.symbol.typ import *

class Width_Bucket(Function):
    def __init__(self, expr, min_value, max_value, num_buckets, row, column):
        Function.__init__(self,row,column)
        self.expr = expr
        self.min_value = min_value
        self.max_value = max_value
        self.num_buckets = num_buckets
    
    def execute(self, environment):
        #Input es una lista        
        min = self.min_value.execute(environment)['value']
        max = self.max_value.execute(environment)['value']
        valor = self.expr.execute(environment)['value']
        cubos = self.num_buckets.execute(environment)['value']
        
        espectro = max - min
        tamañoSegmento = espectro / cubos

        init = min
        vals = []
        while init <= max + tamañoSegmento:
            vals.append(init)
            init += tamañoSegmento
        
        i = 1
        for val in vals:
            if valor > val and valor <= val + tamañoSegmento:
                return {'value': i , 'typ': Type.INT}
            i+=1
        return cubos+1