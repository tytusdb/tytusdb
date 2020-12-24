import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Start\\')
sys.path.append(nodo_dir)

from prettytable import PrettyTable
from Libraries import Nodo
from Libraries import Database
from Libraries import Table
from Libraries import Use
from Libraries import Type
from Libraries import Select
from Libraries import InsertTable



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

    def tabular_data(self, encabezados : list, data : list) -> str: 
        index = 0
        for i in encabezados:
            if i == "?column?":
                encabezados[index] = "?column?"+str(index)
                index += 1
        x = PrettyTable()
        x.field_names = encabezados
        for item in data:
            if len(item) == len(encabezados):
                x.add_row(item)
        return x.get_string()
        
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
                res = nuevaTabla.execute(hijo, enviroment)
                if res.code != "00000":
                    print(res.responseObj.descripcion)
            elif hijo.nombreNodo == 'CREATE_TYPE_ENUM':
                nuevoEnum = Type()
                nuevoEnum.execute(hijo)
            elif hijo.nombreNodo == 'SENTENCIA_SELECT' or hijo.nombreNodo == 'SENTENCIA_SELECT_DISTINCT':
                respuesta = hijo.execute(enviroment)
                print(respuesta.data)
                self.listaSemanticos.append({"Code":"0000","Message":  " rows returned", "Data" : self.tabular_data(respuesta.encabezados, respuesta.data)})
            elif hijo.nombreNodo == 'E':
                hijo.execute(enviroment)
                print("Tipo Expresion: "+str(hijo.tipo.data_type))
                print("Expresion valor: "+str(hijo.valorExpresion))
            elif hijo.nombreNodo == 'SENTENCIA_INSERT':
                nuevoInsert = InsertTable()
                nuevoInsert.execute(hijo,enviroment)
            elif hijo.nombreNodo == "SENTENCIA_SHOW":
                self.listaSemanticos.append(hijo.execute(None))
            elif hijo.nombreNodo == "SENTENCIA_DROP":
                self.listaSemanticos.append(hijo.execute(None))
            elif hijo.nombreNodo == "SENTENCIA_DELETE":
                hijo.execute(enviroment)
                
