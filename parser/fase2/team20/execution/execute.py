#Importacion de metodos de ejecucion
#Se utilizan archivos separados para minimizar los conflictos
from .executeSentence import executeSentence
from .generateASTReport import graphAST
from .generateSymbolTableReport import printSymbolTable
from .execute_result import *
from .intermediateFunctions import *
class Execute():
    nodes = []
    errors = []
    messages = []
    querys = []
    intermediate = IntermediateFunctions()
    code = "from goto import with_goto\n@with_goto\ndef c3d():\n"
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
           for node in self.nodes:
               executeSentence(self,node)
        else:
            self.code += "\tt0=0\n"
            self.code += "\tlabel .begin\n"
            self.code += "\tif t0 == 10: goto .end\n"
            self.code += "\tprint(t0)\n"
            self.code += "\tt0=t0+1\n"
            self.code += "\tgoto .begin\n"
            self.code += "\tlabel .end\n"
        dotAST = graphAST(self)
        printSymbolTable_ = printSymbolTable(self)
        self.code += "c3d()"
        inter_exec_file = open("C3D.py", "w")
        inter_exec_file.write(self.code)
        inter_exec_file.close()
        result = execute_result(dotAST, printSymbolTable_, self.errors, self.messages, self.querys)
        return result



#Como guardar un error
# self.errors.append(
#                         Error('Semántico', 'Ya existe una tabla con el nombre ' + nodo.id, nodo.fila, nodo.columna))
    
    
    