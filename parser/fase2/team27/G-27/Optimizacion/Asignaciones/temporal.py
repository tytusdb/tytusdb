class Temporal(object):
    def __init__(self,tem,izq,op,der):
        self.tem = tem
        self.izq = izq
        self.op = op
        self.der = der

    def execute(self):
        if self.op != None:
            return {'temp': self.tem, 'izq': self.izq, 'op': self.op, 'der': self.der }
        else:
            return {'temp': self.tem, 'val': self.izq}
    