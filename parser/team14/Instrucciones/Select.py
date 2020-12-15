from Instrucciones.Instruccion import Instruccion

class Select(Instruccion):
    'This is an abstract class'

    def __init__(self,distinct=None,exps=None,froms=None,where=None,group=None,having=None,order=None,limit=None,combinging=None):
        self.distinct=distinct
        self.exps=exps
        self.froms=froms
        self.where=where
        self.group=group
        self.having=having
        self.order=order
        self.limit=limit
        self.combinig=combinging


    def ejecutar(self):
            'Metodo Abstracto para ejecutar la instruccion'
            if self.distinct is None and self.froms is None and self.where is None and self.group is None and self.having is None and self.order is None and self.combinig is None:
                for exp in self.exps:
                    print(exp.getval())
                    return exp.getval()
