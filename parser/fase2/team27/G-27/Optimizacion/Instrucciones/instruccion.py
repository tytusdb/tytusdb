class Instruccion(object):
    def __init__(self, ins, params):
        self.ins = ins
        self.params = params

    def execute(self):
        raise NotImplementedError 
    
print('Instruccion')