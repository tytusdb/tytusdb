#Importacion de metodos de ejecucion
#Se utilizan archivos separados para minimizar los conflictos
from .executeSentence import executeSentence
from .executeSentence2 import executeSentence2
from .generateASTReport import graphAST
from .generateSymbolTableReport import printSymbolTable
from .execute_result import *
import pickle
from pprint import pprint
from io import StringIO  # Python3
import sys
class Execute():
    nodes = []
    errors = []
    messages = []
    querys = []
    types = {
        1: 'Entero',
        2: 'Decimal',
        3: 'Cadena',
        4: 'Variable',
        5: 'Regex'
    }
    def __init__(self, nodes):
        self.nodes = nodes
        self.errors = []
        self.messages = []
        self.querys = []
    # def __init__(self, nodes, errors):
    #     self.nodes = nodes
    #     self.errors = errors
    #Aqui va metodo principal ejecutar, al que se le enviara la raiz del AST 
    #y se encargaran de llamar el resto de metodos
    def execute(self):
        if(self.nodes is not None):
            archivo = open("C3D.py", 'w+')
            archivo.write("from execution.executeSentence import executeSentence ") 
            archivo.write("\nfrom execution.AST.sentence import *")
            archivo.write("\nfrom execution.AST.expression import *")
            archivo.write("\ndef up():")
            archivo.close()
            
            for node in self.nodes:
                #pprint(vars(node))
                old_stdout = sys.stdout
                new_stdout = StringIO()
                sys.stdout = new_stdout
                print(node)
                val1 = new_stdout.getvalue()[:-1]
                sys.stdout = old_stdout
                archivo = open("C3D.py", 'a')
                archivo.write("\n\t")
                archivo.write(val1) 
                archivo.close()
                
                executeSentence2(self,node)
        dotAST = graphAST(self)
        printSymbolTable_ = printSymbolTable(self)

        result = execute_result(dotAST, printSymbolTable_, self.errors, self.messages, self.querys)
        return result



#Como guardar un error
# self.errors.append(
#                         Error('Semántico', 'Ya existe una tabla con el nombre ' + nodo.id, nodo.fila, nodo.columna))
    
    
    