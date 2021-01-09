from graphviz import Digraph
from arbolNario import ArbolN
class Nodo:
    def __init__(self, valor ):
        self.valor  = valor
        self.conexiones = {}


class Grafo:

    def __init__(self):
        self.nodosAgregados = []
        
    def returnValores(self):
        return [nodo.valor for nodo in self.nodosAgregados]
    def insertIndependiente(self, ind):
        self.nodosAgregados.append(ind)

    def insertar(self, nodoPadre, distancia, nodoHijo):
        if len(self.nodosAgregados) == 0:
            nodoP = Nodo(nodoPadre)
            nodoH = Nodo(nodoHijo)
            nodoP.conexiones[nodoH.valor] = distancia
            nodoH.conexiones[nodoP.valor] = distancia
            self.nodosAgregados.append(nodoP)
            self.nodosAgregados.append(nodoH)
        else:
            valores = self.returnValores()
            if nodoPadre in valores :
                indice = valores.index(nodoPadre)
                nodoP = self.nodosAgregados[indice]
                if nodoHijo in valores:
                    index2 =valores.index(nodoHijo)
                    nodoH = self.nodosAgregados[index2]
                    nodoP.conexiones[nodoH.valor] = distancia
                    nodoH.conexiones[nodoP.valor] = distancia
                else:
                    nodoH = Nodo(nodoHijo)
                    nodoP.conexiones[nodoH.valor] = distancia
                    nodoH.conexiones[nodoP.valor] = distancia
                    self.nodosAgregados.append(nodoH)
            else:
                nodoP = Nodo(nodoPadre)
                if nodoHijo in valores:
                    index2 =valores.index(nodoHijo)
                    nodoH = self.nodosAgregados[index2]
                    nodoP.conexiones[nodoH.valor] = distancia
                    nodoH.conexiones[nodoP.valor] = distancia
                    self.nodosAgregados.append(nodoP)
                else:
                    nodoH = Nodo(nodoHijo)
                    nodoP.conexiones[nodoH.valor] = distancia
                    nodoH.conexiones[nodoP.valor] = distancia
                    self.nodosAgregados.append(nodoH)
                    self.nodosAgregados.append(nodoP)
    
    def retornaGrafo(self):
        for i in self.nodosAgregados:
            print("Nodo: " + str(i.valor) )
            for j in i.conexiones.keys():
                print(str(i.valor) +"<----"+ str(i.conexiones[j])+ "----> "+ str(j) )

    def graficar(self):
        f = Digraph(name='grafo' , filename= 'grafo.gv', format = "svg")
        f.attr(rankdir='LR')
        f.attr('node', shape='box')
        for i in self.nodosAgregados:
            f.node(i.valor)

        nodosvisitados =[]

        for i in self.nodosAgregados:
            nodosvisitados.append(i.valor)
            if list(i.conexiones.keys()) !=[]:
                for j in i.conexiones.keys():
                    if j not in nodosvisitados:
                        f.edge_attr["arrowhead"] ='vee'
                        f.edge(i.valor, j, label= str(i.conexiones[j]) )
                
        f.view()

    def ArbolGenerador(self, Raiz):
        tree = ArbolN()
        nodos_visitados = []
        nodos = [nodo.valor for nodo in self.nodosAgregados]
        NodoRaiz = self.nodosAgregados[nodos.index(Raiz)]
        nodos_visitados.append(NodoRaiz.valor)
        tree.insertar(NodoRaiz.valor, 0)
        nodosXvisitar = []
        posicion = 0
        for i in NodoRaiz.conexiones.keys():
            tree.insertar(i ,NodoRaiz.conexiones[i], NodoRaiz.valor,posicion )
            nodos_visitados.append(i)
            nodosXvisitar.append(self.nodosAgregados[nodos.index(i)])
            posicion +=1
        
        for j in nodosXvisitar:
            position = 0 
            for k in j.conexiones.keys():
                if k not in nodos_visitados:
                    tree.insertar(k, j.conexiones[k],j.valor,position )
                    nodos_visitados.append(j.valor)
                    nodos_visitados.append(k)
                    nodosXvisitar.append(self.nodosAgregados[nodos.index(k)])
                    position +=1
        tree.GenGraph()
