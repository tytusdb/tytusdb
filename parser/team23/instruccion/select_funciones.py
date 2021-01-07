from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *
from tools.tabla_simbolos import *
from abstract.retorno import *
from prettytable import PrettyTable

class select_funciones(instruccion):
    def __init__(self,expresiones, line, column, num_nodo):
        super().__init__(line,column)
        self.nodo = nodo_AST('SELECT',num_nodo)
        self.nodo.hijos.append(nodo_AST('SELECT',num_nodo+1))
        self.expresiones=expresiones

        self.grammar_=''

        if expresiones != None:
            for element2 in expresiones:
                if element2 != None:
                    self.nodo.hijos.append(element2.nodo)

    def ejecutar(self, imprimir=None):
        id_db = get_actual_use() 
        salidaTabla = PrettyTable()
        encabezados=[]
        registro = []
        list_campo = []
        for dato in self.expresiones:
            if dato != None:
                auxDato=dato.ejecutar(id_db)
                list_campo.append(auxDato.valor)
            salidaTabla.add_column(auxDato.query,list_campo)
            list_campo.clear()
        
        add_text('\n')
        add_text(salidaTabla)
        add_text('\n')


        return retorno(registro,encabezados)