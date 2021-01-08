from Optimizacion.instruccion import Instruccion
from Optimizacion.llamada import Llamada

class Def(Instruccion):
    def __init__(self, with_goto, id, instrucciones, linea):
        self.with_goto = with_goto
        self.id = id
        self.instrucciones = instrucciones
        self.linea = linea
        
    def toString(self):
        with_goto = f"{self.with_goto}\n" if self.with_goto else f""
        codigo = f"{with_goto}def {self.id}():\n"
        
        for inst in self.instrucciones:
            if isinstance(inst, Llamada) and inst.expresion.toString() == 'main':
                codigo += f"\n{inst.toString()}"
            else:
                codigo += f"\t{inst.toString()}"
        codigo += f"\n"
        return codigo