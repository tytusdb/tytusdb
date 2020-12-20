import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Start\\')
sys.path.append(nodo_dir)


from Libraries import Nodo
from Libraries import Database
from Libraries import Table
from Libraries import Use
from Libraries import Type
from Libraries import Select



# Importación de Clases para Execute


class Start(Nodo):
    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
        self.listaSemanticos = []
            
    def addChild(self, node):
        self.hijos.append(node)

    def createChild(self, nombreNodo, fila = -1, columna =-1, valor = None):
        nuevo = Start(nombreNodo,fila,columna,valor)
        self.hijos.append(nuevo)
    
    def createTerminal(self, lexToken):
        nuevo = Start(lexToken.type, lexToken.lineno, lexToken.lexpos, lexToken.value)
        self.hijos.append(nuevo)


    # recursiva por la izquierda
    def execute(self, enviroment):
        
        for hijo in self.hijos:
            if hijo.nombreNodo == 'CREATE_DATABASE':
                nuevaBase=Database()                
                # Recibe un json
                message = nuevaBase.execute(hijo)
                self.listaSemanticos.append(message)
            elif hijo.nombreNodo == 'SENTENCIA_USE':
                useDB = Use()
                message = useDB.execute(hijo)
                self.listaSemanticos.append(message)
            elif hijo.nombreNodo == 'CREATE_TABLE':
                nuevaTabla = Table()
                nuevaTabla.execute(hijo, enviroment)
            elif hijo.nombreNodo == 'CREATE_TYPE_ENUM':
                nuevoEnum = Type()
                nuevoEnum.execute(hijo)
            elif hijo.nombreNodo == 'SENTENCIA_SELECT':
                nuevoSelect = Select()
                nuevoSelect.execute(hijo,enviroment)
            elif hijo.nombreNodo == 'E':
                hijo.execute(enviroment)
                print("Tipo Expresion: "+str(hijo.tipo.data_type))
                print("Expresion valor: "+str(hijo.valorExpresion))
                