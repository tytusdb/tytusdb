from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Proc(Instruccion):
    def __init__(self, name, params, block, ret, strGram, linea, columna):
        self.name = name
        self.params = params
        self.block = block
        self.ret = ret
        self.linea = linea
        self.columna = columna

    def ejecutar(self, tabla, arbol):
        pass
        
    def getCodigo(self, tabla, arbol):
        arbol.setScope(self.name)
        
        func = f"@with_goto\n"
        func += f"def {self.name}():\n"
        func += f"\tglobal pointer\n"
        func += f"\tglobal stack\n"
        
        func += self.block.getCodigo(tabla, arbol)
        func += f"\n"

        return func