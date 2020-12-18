from graphviz import Digraph
from AST.Nodo import Nodo
from AST.Nodo import reset_id_arbol
import AST.Nodo as Node
from AST.Expresiones import *


class Raiz(Node.Nodo):
    def __init__(self, Errores, sentencias = [], fila = 0, columna = 0):
        super().__init__(fila=fila, columna=columna)
        self.sentencias = sentencias
        self.errores = Errores

    def ejecutar(self, TS, Errores):
        respuesta = ''
        for hijo in self.sentencias:
            if isinstance(hijo, Expression):
                respuesta += ''
            respuesta += hijo.ejecutar(TS, Errores) + '\n'
        return respuesta

    def getC3D(self, TS):
        pass 

    def graficarasc(self, padre = None, grafica=None):
        grafica = Digraph(name="AST", comment='AST generado')
        grafica.edge_attr.update(arrowhead='none')
        grafica.node(self.mi_id, "SentenciasSQL")
        for hijo in self.sentencias:
            hijo.graficarasc(self.mi_id, grafica)
        grafica.render(directory='Reportes/graficaAST', view=True)
        reset_id_arbol()


class Sentencia(Raiz):
    def __init__(self, nombre_sentencia, sentencias, fila = 0, columna = 0):
        super().__init__(None, sentencias=sentencias, fila=fila, columna=columna)
        self.nombre_sentencia = nombre_sentencia

    #No necesito definir ejecutar porque ya lo hereda de Raiz y realiza lo mismo aqui que alli

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        grafica.node(self.mi_id, self.nombre_sentencia)
        grafica.edge(padre, self.mi_id)
        for hijo in self.sentencias:
            hijo.graficarasc(self.mi_id, grafica)