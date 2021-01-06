#Importacion de metodos de ejecucion
#Se utilizan archivos separados para minimizar los conflictos
from .AST.sentence import *
from .executeSentence import executeSentence
from .executeSentence2 import executeSentence2
from .executeInstruction import executeInstruction
from .generateASTReport import graphAST
from .generateSymbolTableReport import printSymbolTable
from .execute_result import *
from io import StringIO  # Python3
import sys
class Execute():
    nodes = []
    errors = []
    messages = []
    querys = []
    ts = []
    plcode = ""
    #intermediate = IntermediateFunctions()
    types = {
        1: 'Entero',
        2: 'Decimal',
        3: 'Cadena',
        4: 'Variable',
        5: 'Regex'
    }
    def __init__(self, nodes):
        self.tempcount = -1
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
            archivo.write("\n\tprint(1)")
            archivo.close()
            if(len(self.nodes)==0):
                archivo = open("C3D.py", 'a')
                archivo.write("\n\tprint(1)")
                archivo.close() 
            for node in self.nodes:
                #pprint(vars(node))
                if isinstance(node,Sentence):
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
                else:
                    executeInstruction(self,node)
                
                #executeSentence2(self,node)
        archivo = open("C3D.py", 'a')
        archivo.write("\n")
        archivo.write(self.plcode) 
        archivo.close()
        dotAST = graphAST(self)
        printSymbolTable_ = printSymbolTable(self)
        result = execute_result(dotAST, printSymbolTable_, self.errors, self.messages, self.querys)
        return result
    def generateTemp(self):
        self.tempcount+=1
        temp = 't'+str(self.tempcount)
        return temp
    def getLastTemp(self):
        temp = 't'+str(self.tempcount)
        return temp



#Como guardar un error
# self.errors.append(
#                         Error('Semántico', 'Ya existe una tabla con el nombre ' + nodo.id, nodo.fila, nodo.columna))
    
    
    