from PLSQL.instruccionesPLSQL import *
from PLSQL.expresionesPLSQL import *
from graphviz import Digraph

dot = Digraph('AST', node_attr={'shape': 'note','color': 'lightblue2', 'style': 'filled'})
contadorNodos = 0
instrucciones_Global = []

class AST: 

    def __init__(self):
        '''print('AST')'''


    def generarAST(self,instrucciones):
        global contadorNodos, dot, instrucciones_Global
        instrucciones_Global = instrucciones
        dot = Digraph('AST')
        contadorNodos = 2
        dot.node('node1','INIT')
        dot.node('node2','INSTRUCCIONES 3D')
        dot.edge('node1','node2')
        indice = 0
        while indice < len(instrucciones_Global) :
            instruccion = instrucciones_Global[indice]
            if isinstance(instruccion, Funcion):
                self.crearNodoFuncion("node2", instruccion)
            elif isinstance(instruccion, CreateDatabase):
                self.crearNodoCreateDatabase("node2", instruccion)
            indice = indice +1
        dot.view('reportes/ASTPLSQL', cleanup=True)



    def crearNodoExpresion(self, padre, expresion):
        global contadorNodos, dot
        if isinstance(expresion, ExpresionIdentificador):
            if expresion.val != "":
                contadorNodos = contadorNodos + 1
                dot.node("node" + str(contadorNodos), str(expresion.val))
                dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionBinaria):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.exp1))
            dot.node("node" + str(contadorNodos), str(expresion.exp2))
            dot.node("node" + str(contadorNodos), str(expresion.operador))
            dot.edge(padre, "node" + str(contadorNodos))
        else:
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion))
            dot.edge(padre, "node" + str(contadorNodos))

    def crearNodoCreateDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
    
    def crearNodoFuncion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'FUNCION')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoFuncionTipo(temp1,instruccion)

    def crearNodoFuncionTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(instruccion.tipo))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        
    
    