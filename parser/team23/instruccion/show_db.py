from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *

class show_db(instruccion):
    def __init__(self, line, column, num_nodo):
        super().__init__(line, column)

        #Nodo AST Show DB
        self.nodo = nodo_AST('SHOW DATABASES', num_nodo)
        self.nodo.hijos.append(nodo_AST('SHOW DATABASES', num_nodo+1))

        # Gramatica        
        self.grammar_ = "<TR><TD>INSTRUCCION ::= SHOW DATABASES;</TD><TD>INSTRUCCION = new show_db();</TD></TR>"

    def ejecutar(self):
        try:
            bases_datos = funciones.showDatabases()
            # Valor de retorno: lista de strings, si no hay bases de datos devuelve una lista vacía [].

            conteo = 0
            if len(bases_datos) > 0:
                print_db = "\nM-00000 successful completion:\n Database list:\n"

                for base in bases_datos:
                    print_db += " " + str(conteo) + " | " + base + "\n"
                    conteo += 1
                print_db += "-------------------------------\n"
                
                add_text(print_db)
            else:
                add_text("E-22005 error in assignment: No database exists.\n")
        except:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: No database exists', 'Semántico'))