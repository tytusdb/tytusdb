import Bases as ba
import Tablas as ta
from graphviz import Digraph
import GeneralesAVL as gA

class nodoTupla(object):
    key = 0
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []
        self.leaf = True

    def agregar(self, key, nomDTB, nomTBL, registro):
        if not self.keys:
            self.keys.append(key)
            self.values.append([nomDTB,nomTBL,registro])
            return None

        for i, item in enumerate(self.keys):
            if key == item:
                self.values[i].append([nomDTB,nomTBL,registro])
                break

            elif key < item:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[nomDTB,nomTBL,registro]] + self.values[i:]
                break
            elif i + 1 == len(self.keys):
                self.keys.append(key)
                self.values.append([nomDTB,nomTBL,registro])

    def split(self):
        izquierda = nodoTupla(self.order)
        right = nodoTupla(self.order)
        mid = self.order // 2

        izquierda.keys = self.keys[:mid]
        izquierda.values = self.values[:mid]

        right.keys = self.keys[mid:]
        right.values = self.values[mid:]

        self.keys = [right.keys[0]]
        self.values = [izquierda, right]
        self.leaf = False

    def is_full(self):
        return len(self.keys) == self.order

    def show(self, nivel=0):
        if len(self.keys) == 3:
            ga = self.keys[0]
            gaa = self.keys[1]
            lega = u.retrieve(ga)
            legaa = u.retrieve(gaa)
            gaaa = self.keys[2]
            legaaa = u.retrieve(gaaa)
            print('Nivel: ' + str(nivel), '[ Llave: ' + str(ga) + ' Datos: ' + str(lega[2]) + ' , Llave: ' + str(gaa) + ' Datos: ' + str(legaa[2]) + ' , Llave: ' + str(gaaa) + ' Datos: ' + str(legaaa[2]) + ' ]' )
        else:
            ga = self.keys[0]
            gaa = self.keys[1]
            lega = u.retrieve(ga)
            legaa = u.retrieve(gaa)
            print('Nivel: ' + str(nivel), '[ Llave: ' + str(ga) + ' Datos: ' + str(lega[2]) + ' , Llave: ' + str(gaa) + ' Datos: ' + str(legaa[2]) + ' ]')

        if not self.leaf:
            for item in self.values:
                item.show(nivel + 1)
    
    def graficar(self, nivel, nodos):
        if len(self.keys) == 3:
            ga = self.keys[0]
            gaa = self.keys[1]
            lega = u.retrieve(ga)
            legaa = u.retrieve(gaa)
            gaaa = self.keys[2]
            legaaa = u.retrieve(gaaa)
            zi =  str(lega[0]) + ', ' + str(lega[1])+ ', ' + str(lega[2]) + '  |  ' + str(legaa[0]) + ', ' + str(legaa[1])+ ', ' + str(legaa[2]) + '  |  ' + str(legaaa[0]) + ', ' + str(legaaa[1])+ ', ' + str(legaaa[2])
            nodos += [nivel]
            nodos += [zi]
            u.agregarNodo(zi)
        else:
            ga = self.keys[0]
            gaa = self.keys[1]
            lega = u.retrieve(ga)
            legaa = u.retrieve(gaa)
            zo = str(lega[0]) + ', ' + str(lega[1])+ ', ' + str(lega[2]) + '  |  ' + str(legaa[0]) + ', ' + str(legaa[1])+ ', ' + str(legaa[2])
            nodos += [nivel]
            nodos += [zo]
            u.agregarNodo(zo)

        if not self.leaf:
            for item in self.values:
                item.graficar(nivel + 1, nodos)
        
        return nodos

class BPlusTree(object):
    
    def guardar(self):
        gA.g.commitTupla(self, nodoTupla.key)

    def __init__(self, order=8):
        self.root = nodoTupla(order)
        self.graf = None

    def buscar(self, node, key):
        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i

        return node.values[i + 1], i + 1

    def unir(self, parent, hijo, index):
        parent.values.pop(index)
        pivot = hijo.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + hijo.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += hijo.values
                break
            
    def cantiKey(self):
        return nodoTupla.key

    def autoKey(self):
        hey = nodoTupla.key
        hey += 1
        nodoTupla.key = hey
        return hey


    def insert(self, nomDTB, nomTBL, registro):
        try:
            h = int(ta.t.buscarCol(gA.g.jalarValN(nomTBL),nomDTB))
            if ba.b.buscarBase(gA.g.jalarValN(nomDTB)):
                if ta.t.buscar(gA.g.jalarValN(nomTBL),nomDTB):
                    if h == len(registro):
                        parent = None
                        hijo = self.root
                        key = self.autoKey()

                        while not hijo.leaf:
                            parent = hijo
                            hijo, index = self.buscar(hijo, key)
                        
                        hijo.agregar(key, nomDTB, nomTBL, registro)

                        if hijo.is_full():
                            hijo.split()
                            if parent and not parent.is_full():
                                self.unir(parent, hijo, index)
                        return 0
                    else:
                        return 5
                else:
                    return 3
            else:
                return 2
        except:
            return 1

    def retrieve(self, key):
        hijo = self.root

        while not hijo.leaf:
            hijo, index = self.buscar(hijo, key)

        for i, item in enumerate(hijo.keys):
            if key == item:
                return hijo.values[i]

        return None

    def mandarDatosTBL(self, key, nomDTB, nomTBL):
        hijo = self.root
        while not hijo.leaf:
            hijo, index = self.buscar(hijo, key)

        for i, item in enumerate(hijo.keys):
            ga = hijo.values[i]
            if key == item and ga[0] == nomDTB and ga[1] == nomTBL:
                return ga[2]
        return None

    def mostrarTuplasConsola(self):
        self.root.show()
    
    def extractRow(self, nomDTB, nomTBL, column):
        paDevolver = []
        for n in range(0,len(column)):
            ga = column[n]
            lega = self.retrieve(ga)
            paDevolver += [lega[2]]
        return paDevolver

    #para el extractRangeTable de tablas
    def extractRowRange(self, nomDTB, nomTBL, col, ini, fin):
        l = [col]
        tmp = self.extractRow(nomDTB, nomTBL, l)
        temp = tmp[0]
        lst = []
        for n in range(ini-1,fin):
            lst += [temp[n]]
        return lst

    #para cargar las tuplas con csv
    def loadCSV(self, ruta, nomDTB, nomTBL):
        f = open(ruta,'r')
        for linea in f:
            h = linea.replace('\n','')
            self.insert(nomDTB,nomTBL,h.split(','))
            if not linea:
                break
        f.close()

    #crear gráfica
    def agregarNodo(self, conte):
        self.graf.node(conte)

    def generarGraphvizTuplas(self):
        nodos = []
        nivs = []
        self.graf = Digraph(
        format='svg', filename = 'Tuplas Árbol', 
        node_attr={'shape': 'record', 'height': '.1'})
        self.graf.attr(rank='same')
        nodos = self.root.graficar(0, nodos)
        nivs = []
        for n in range(0,len(nodos),2):
            nivs += [nodos[n]]
        maxN = max(nivs)
        minN = min(nivs)
        tatascan = ''
        
        #comenzar a enlazar desde la raíz
        for n in range(0,len(nodos),2):
            if nodos[n] == minN:
                tatascan = nodos[n+1]

                for y in range(0,len(nodos),2):
                    if nodos[y] == minN+1:
                        hijo = str(nodos[y+1])
                        self.graf.edge(tatascan,hijo)
                minN += 1
                
        with self.graf.subgraph(name='hojas') as h:
            #enlazar hojas finales
            for x in range(0,len(nodos),2):
                if nodos[x] == maxN and ((x+3) <= len(nodos)):
                    zi = str(nodos[x+1])
                    zo = str(nodos[x+3])
                    h.edge(zi,zo)

        self.graf.view()

u = BPlusTree(order=4)