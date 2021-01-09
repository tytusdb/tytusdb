from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Call(Instruccion):
    def __init__(self, _id, expressions, strGram, linea, columna):
        self.id = _id
        self.expressions = expressions
        self.linea = linea
        self.columna = columna

    def ejecutar(self, tabla, arbol):   
        pass
        
    def getCodigo(self, tabla, arbol):
        codigo = f""
        if self.expressions:
            temp_tam_func = arbol.getTemporal()
            
            codigo = f"\t{temp_tam_func} = pointer + {len(self.expressions)}\n"
            cont = 1
            for exp in self.expressions:
                temp_param_value = arbol.getTemporal()
                temp_param_index = arbol.getTemporal()
                dic = exp.getCodigo(tabla, arbol)
                
                codigo += dic['codigo']
                codigo += f"\t{temp_param_value} = {dic['dir']}\n"
                codigo += f"\t{temp_param_index} = {temp_tam_func}  + {cont}\n"
                codigo += f"\tstack[{temp_param_index}] = {temp_param_value}\n"
                cont += 1
        
            codigo += f"\tpointer = pointer + {len(self.expressions)}\n"
            
        codigo += f"\t{self.id}()\n"
        
        temp_return_index = arbol.getTemporal()
        temp_return = arbol.getTemporal()
            
        codigo += f"\t{temp_return_index} = pointer + 0\n"
        codigo += f"\t{temp_return} = stack[{temp_return_index}]\n"
        codigo += f"\tpointer = pointer - {len(self.expressions)}\n"
        codigo += f"\tprint({temp_return})\n"
        
        arbol.consola.append(codigo)
            
        return {'codigo' : codigo, 'dir': temp_return}