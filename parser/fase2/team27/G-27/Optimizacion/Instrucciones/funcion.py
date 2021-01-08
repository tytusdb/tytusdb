from Optimizacion.Instrucciones.instruccion import Instruccion
class Funcion(Instruccion):
    def __init__(self, ins, params, func):
        Instruccion.__init__(self, ins, params)
        self.func = func

    def execute(self):
        return {'ins': self.ins, 'params': self.params, 'func': self.func}

    def toString(self,tab):
        if self.func != None:
            funcion =  '\n@with_goto \ndef ''' + self.ins + '('

            for i in range(len(self.params)):
                funcion += str(self.params[i])
                if ( i< len(self.params)-1):
                    funcion += ', '
            
            funcion += '): '

            for instruccion in self.func:
                funcion += '\n' + instruccion.toString(tab+1)
                    
            return funcion
        else:
            funcion = self.ins + '('
            
            for i in range(len(self.params)):
                funcion += str(self.params[i])
                if ( i< len(self.params)-1):
                    funcion += ', '
            
            funcion += ')'
            return funcion
            


print('funcion')
