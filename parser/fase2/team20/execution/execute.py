#Importacion de metodos de ejecucion
#Se utilizan archivos separados para minimizar los conflictos
from .AST.sentence import *
from .executeSentence import executeSentence
from .executeSentence2 import executeSentence2
from .executeInstruction import executeInstruction
from .generateASTReport import graphAST
from .generateSymbolTableReport import printSymbolTable
from .execute_result import *
from .storageManager.TypeChecker import *
from io import StringIO  # Python3
import sys
path_c3d = "C3D.py"
class Execute():
    nodes = []
    errors = []
    messages = []
    querys = []
    ts = []
    pila =[] # cada item es un diccionario {resultado,argumento1,argumento2,operacion}
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
        self.labelcount = -1
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
            global path_c3d
            archivo = open(path_c3d, 'w+')
            archivo.write("from execution.executeSentence import executeSentence ") 
            archivo.write("\nfrom execution.AST.sentence import *")
            archivo.write("\nfrom execution.AST.expression import *")
            archivo.write("\nfrom execution.executeInstruction import createFunction, deleteFunction")
            archivo.write("\nfrom console import print_error, print_success, print_warning, print_text")
            archivo.write("\nfrom goto import with_goto")
            archivo.write("\nimport math")
            archivo.write("\n\n@with_goto")
            archivo.write("\ndef up():")
            archivo.write("\n\tprint(1)\n")
            archivo.close()
            if(len(self.nodes)==0):
                archivo = open(path_c3d, 'a')
                archivo.write("\n\tprint(1)\n")
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
                    archivo = open(path_c3d, 'a')
                    archivo.write("\n\t")
                    archivo.write(val1) 
                    archivo.close()
                else:
                    executeInstruction(self,node, 1, 0)
                
                #executeSentence2(self,node)
        try:
            for storedproc in TCgetFunctions():
                if storedproc not in self.plcode: 
                    self.plcode+=storedproc
        except:
            pass
        archivo = open(path_c3d, 'a')
        archivo.write("\n")
        archivo.write(self.plcode)
        archivo.write("\n#up()")
        archivo.close()
        dotAST = graphAST(self)
        printSymbolTable_ = printSymbolTable(self)
        contentC3D = ""
        try:
            f = open(path_c3d, "r")
            contentC3D = f.read()
            f.close()
        except Exception as e:
            i=0#print(e)
        result = execute_result(dotAST, printSymbolTable_, self.errors, self.messages, self.querys, contentC3D)
        return result
    def generateTemp(self):
        self.tempcount+=1
        temp = 't'+str(self.tempcount)
        return temp
    def getLastTemp(self):
        temp = 't'+str(self.tempcount)
        return temp
    def generateLabel(self):
        self.labelcount+=1
        label = 'lbl'+str(self.labelcount)
        return label
    def getLastLabel(self):
        label = 'lbl'+str(self.labelcount)
        return label



#Como guardar un error
# self.errors.append(
#                         Error('Semántico', 'Ya existe una tabla con el nombre ' + nodo.id, nodo.fila, nodo.columna))
    
    
    