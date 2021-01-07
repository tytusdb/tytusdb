# clase Graficar AST genera el string para graficar en graphviz 

class GraficarAST:
    def __init__(self):
        self.counter = 0
        self.cadena = []
    
    def generate_string(self, raiz):
        self.cadena.append('digraph D{\n\tnode[style=filled color="#324960" fillcolor="#324960", fontcolor="#F8F8F2"];\n\t')
        self.cadena.append('graph[label="AST SQL"];\n\t')
        self.get_nodos(raiz, self.cadena)
        self.set_rotation(raiz, self.cadena)
        self.cadena.append('\r}')
        return ''.join(self.cadena)
    
    def get_nodos(self, raiz, cadena):
        aux_cadena = "node" + str(self.counter) + " [label =\"" + str(raiz.get_value()) + "\"];\n\t"
        cadena.append(aux_cadena) 
        raiz.set_id(self.counter)
        self.counter += 1
        aux_value = raiz.get_childrens().head_value
        while aux_value is not None:
            self.get_nodos(aux_value.data, cadena)
            aux_value = aux_value.next
    
    def set_rotation(self, raiz, cadena):
        aux_value = raiz.get_childrens().head_value
        while aux_value is not None:
            aux_cadena = '"node' + str(raiz.get_id()) + '"->'
            cadena.append(aux_cadena)
            aux_cadena = '"node' + str(aux_value.data.get_id()) + '";\n\t'
            cadena.append(aux_cadena)
            self.set_rotation(aux_value.data, cadena)
            aux_value = aux_value.next
            
