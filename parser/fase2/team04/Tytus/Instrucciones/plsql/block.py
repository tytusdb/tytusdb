from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.plsql.call import Call
from Instrucciones.Excepcion import Excepcion

class Block(Instruccion):
    #inst es una lista de instrucciones
    def __init__(self, instructions):
        self.instructions = instructions

    def ejecutar(self, tabla, arbol):   
        pass
    
        
    def getCodigo(self, tabla, arbol):
        codigo = f""
        for inst in self.instructions:
            if isinstance(inst, Call):
                result = inst.getCodigo(tabla, arbol)
                codigo += result['codigo']
            else:
                codigo += inst.getCodigo(tabla, arbol)
            
        return codigo