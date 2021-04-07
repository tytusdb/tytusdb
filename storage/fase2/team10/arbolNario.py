from graphviz import Digraph
class Nodo:
    def __init__(self, valor, dist ):
        self.info = valor
        self.distancia_padre = 0
        self.hijos = []

class ArbolN:

    def __init__(self):
        self.__raiz = None

    def __buscar(self, valor, hermanos = None, pos = 0):
        if pos >= len(hermanos):
            return None
        if hermanos[pos].info == valor:
            return hermanos[pos]
        
        nodo = self.__buscar(valor, hermanos[pos].hijos)
        if nodo != None:
            return nodo
        nodo = self.__buscar(valor, hermanos, pos +1)

        if nodo != None :
            return nodo
        
        return None 

    def insertar(self, valor, dist , padre = None, pos_hijo = 0 ):
        if self.__raiz == None:
            self.__raiz = Nodo(valor, 0)
            return True

        if padre == self.__raiz.info:
            padre = self.__raiz
        else:
            padre = self.__buscar(padre, self.__raiz.hijos, 0)
        if (padre != None):
            padre.hijos.insert(pos_hijo, Nodo(valor, dist))
            return True
        return False
    
   
    
    def retornarArbol(self, valor , raiz=None):
        if raiz == None:
            raiz = self.__raiz 
        if raiz.info == valor:
            print("padre: " + raiz.info)
            for i in range(len(raiz.hijos)):
                print("Hijos: " + str(raiz.hijos[i].info))
    def buscarRetornaNodo(self, valor):
        if self.__raiz.info == valor:
            return self.__raiz
        node = self.__buscar(valor , self.__raiz.hijos)
        if node:
            return node 


    def GenTree(self):
        controlPaso = True

        if self.__raiz:
            listaCondecendencia = self.__raiz.hijos[:]
            print("Raiz: " , str(self.__raiz.info))
            hijos = [nodo.info for nodo in self.__raiz.hijos]
            print("hijos: " , str(hijos))
            for i in listaCondecendencia:
                print("nodo: " , str(i.info))
                descendientes = [nodo.info for nodo in i.hijos]
                print("desencientes: " , str(descendientes))
                nodosHijos = [nodo for nodo in i.hijos]
                for j in nodosHijos:
                    if len(j.hijos)>0:
                        listaCondecendencia.append(j) 

    def GenGraph(self):
        f = Digraph("Tree",  filename = 'tree.gv' , format= 'svg' )
        f.attr('node' , shape= 'circle' )
        f.node(self.__raiz.info)
        conDesendencia = self.__raiz.hijos[:]
        hijos = [nodo.info for nodo in self.__raiz.hijos]
        for i in hijos:
            f.node(i)
            f.edge(self.__raiz.info, i)

        for j in conDesendencia:
            if len(j.hijos) >0 :
                descendiente = [nodo.info for nodo in j.hijos]
                nodosDescendientes = [nodo for nodo in j.hijos]
                contador = 0
                for k in descendiente: 
                    f.node(k)
                    f.edge(j.info,k)
                    if len(nodosDescendientes[contador].hijos) >0:
                        conDesendencia.append(nodosDescendientes[contador])
                    contador +=1

        f.view()



"""
a = ArbolN()

a.insertar("A",0 )
a.insertar("b",1,"A", 0)
a.insertar("c",1,"A", 1)
a.insertar("d",1,"A", 2)
a.insertar("e",1,"A", 3)
a.insertar("q",1,"b", 3)
a.insertar("nene",1,"q", 3)
a.retornarArbol("A")
a.GenTree()
a.GenGraph()
"""
