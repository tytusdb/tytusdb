from abstract.instruccion import *
from tools.tabla_tipos import *

class alter_tb(instruccion):
    def __init__(self, ID, opciones, line, column, num_nodo):

        super().__init__(line, column)
        self.ID = ID
        self.opciones = opciones

        #Nodo de op_add
        self.nodo = nodo_AST('alter_statement', num_nodo)
        self.nodo.hijos.append(nodo_AST('ALTER', num_nodo + 1))
        self.nodo.hijos.append(nodo_AST('TABLE', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 3))
        for alter_item in opciones:
            self.nodo.hijos.append(alter_item.nodo)

        #Gramatica
        self.grammar_ = '<TR><TD> INSTRUCCION ::= ALTER TABLE ' + ID + ' list_alter </TD><TD> new alter_tb(' + ID + ', list_alter); </TD></TR>\n'
        self.grammar_ += '<TR><TD> LIST_ALTER ::= LIST_ALTER1 COMA OP_ALTER </TD><TD> LIST_ALTER = LIST_ALTER1.append(OP_ALTER); </TD></TR>\n'
        self.grammar_ += '<TR><TD> LIST_ALTER ::= OP_ALTER </TD><TD> LIST_ALTER = [OP_ALTER]; </TD></TR>\n'
        for alter_item in opciones:
            self.grammar_ += alter_item.grammar_

    def ejecutar(self):
        for alter_item in self.opciones:
            #Ejecutar cada alter con el id de la tabla
            alter_item.ejecutar(self.ID)