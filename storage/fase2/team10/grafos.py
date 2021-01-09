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
                        f.edge_attr["arrowtail"] ='vee'
                        f.edge_attr["dir"] ='both'
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

"""
gr = Grafo()

gr.insertar("A", "referencia" , "B" )
gr.insertar("A", 5 , "C" )
gr.insertar("C", 6 , "B" )
gr.insertar("B", 3 , "D" )
gr.insertar("D", 1 , "A" )
gr.insertar("C", 5 , "F" )   
gr.insertar("C", 5 , "G" )  
gr.insertar("G", 5 , "A" )  
gr.insertar("G", 5 , "B" )  
gr.insertar("F", 5 , "X" )  
gr.insertar("X", 5 , "A" )  
gr.insertar("V", 5 , "F" )  
gr.insertar("V", 5 , "K" )  
gr.insertar("D", 5 , "K" )  

gr.retornaGrafo()
gr.ArbolGenerador("B")
gr.graficar()
"""

"""
def graphDF(database, table):
    try: 
        grafo = Grafo()
        tam_tabla = 0
        lista_columna = []
        pk = []
        for db in databases: 
            if database == db["name"]:
                for t in db["tables"]: 
                    if t["name"] == table: 
                        pk = t["pk"].copy()
                        tam_tabla = int(t["nCols"])
                        lista_columna = [x for x in range(tam_tabla)]
        
        try:
            tablas = fkIndex[database]
            indice_foraneo = ""
            indices_foraneos =[]
            for i in list(tablas.keys()):
                if table == i[0]:
                    indices =table[i]
                    indice_foraneo = indices[0]   
                    indices_foraneos = indices[1]
            tabla_unicos = uIndex[database]
            indices_unicos = tabla_unicos[database]
            indice_unico = table+indices_unicos[0]
            listaIndices = indices_unicos[1]
            for i in lista_columna:
                grafo.insertar(str(pk)," " ,i )
            grafo.insertar(str(pk) , " " , indice_foraneo)
            grafo.insertar(str(pk) , " " , indice_foraneo)

            for i in indices_foraneos: 
                grafo.insertar(indice_foraneo," ",i )
            for i in lista_columna:
                grafo.insertar(indice_unico, " ",i )

            grafo.ArbolGenerador(pk)
            grafo.ArbolGenerador(indice_foraneo)
            grafo.ArbolGenerador(indice_unico)

        except: 
            for i in list(tablas.keys()):
                if table == i[0]:
                    indices =table[i]
                    indice_foraneo = indices[0]   
                    indices_foraneos = indices[1]

    except:
        None

"""
