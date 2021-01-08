from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class clase_if(Instruccion): #block y _else_block son listas
    def __init__(self, expresion, block, _else_block,strGram, linea, columna):
        self.expresion = expresion
        self.block = block
        self._else_block = _else_block
        self.linea = linea
        self.columna = columna
                      
    def ejecutar(self, tabla, arbol):
       pass


    def getCodigo(self, tabla, arbol):
        label_true = arbol.getLabel()
        label_false = arbol.getLabel()
        label_salida = arbol.getLabel()
        
        result = self.expresion.getCodigo(tabla, arbol)
        
        codigo = result['codigo']
        codigo += f"\tif({result['dir']}): goto .{label_true}\n"
        codigo += f"\tgoto .{label_false}\n"
        codigo += f"\tlabel .{label_true}\n"
        codigo += self.block.getCodigo(tabla, arbol)
        codigo += f"\tgoto .{label_salida}\n"
        codigo += f"\tlabel .{label_false}\n"
        codigo += self._else_block.getCodigo(tabla, arbol) if self._else_block else ""
        codigo += f"\tlabel .{label_salida}\n"
        
        return codigo