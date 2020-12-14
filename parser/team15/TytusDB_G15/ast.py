import ts as TS
from expresiones import *
from instrucciones import *
from graphviz import Digraph

dot = Digraph('AST', node_attr={'shape': 'note','color': 'lightblue2', 'style': 'filled'})
contadorNodos = 0
instrucciones_Global = []

class AST: 

    def __init__(self):
        print('AST')


    def generarAST(self,instrucciones):
        global contadorNodos, dot, instrucciones_Global
        instrucciones_Global = instrucciones
        dot = Digraph('AST')
        contadorNodos = 2
        dot.node('node1','INIT')
        dot.node('node2','INSTRUCCIONES')
        dot.edge('node1','node2')
        indice = 0
        while indice < len(instrucciones_Global) :
            instruccion = instrucciones_Global[indice]
            if isinstance(instruccion, CreateDatabase):
                self.crearNodoCreateDatabase("node2", instruccion)
            indice = indice +1
        dot.view('reportes/AST', cleanup=True)

    def crearNodoCreateDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreDatabase(temp1,instruccion)
        if instruccion.usuario.id != "":
            self.crearNodoUsuarioDatabase(temp1,instruccion)
        self.crearNodoModoDatabase(temp1,instruccion)

    def crearNodoNombreDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'NOMBRE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.nombre)

    def crearNodoUsuarioDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'USUARIO DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.usuario)

    def crearNodoModoDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'MODO DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.modo)

    def crearNodoExpresion(self, padre, expresion):
        global contadorNodos, dot
        if isinstance(expresion, ExpresionIdentificador):
            if expresion.id != "":
                contadorNodos = contadorNodos + 1
                dot.node("node" + str(contadorNodos), str(expresion.id))
                dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionNumeroSimple):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
            dot.edge(padre, "node" + str(contadorNodos))
