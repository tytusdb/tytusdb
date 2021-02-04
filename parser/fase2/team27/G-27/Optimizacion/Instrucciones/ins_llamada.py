from Optimizacion.Instrucciones.instruccion import Instruccion
class Ins_Llamada(Instruccion):
    def __init__(self, ins, params):
        Instruccion.__init__(self, ins, params)

    def execute(self):
        return {'ins': self.ins, 'params': self.params}
    
    def toString(self,tab):
        funcion = '\n' +'\t'*tab + self.ins + '('
        
        for i in range(len(self.params)):
            funcion += str(self.params[i])
            if ( i< len(self.params)-1):
                funcion += ', '
        
        funcion += ')'
        return funcion