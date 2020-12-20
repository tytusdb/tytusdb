import os

class Nodo:

    def __init__(self,valor,name):
        self.bPlus = bPlus
        self.name = name
        self.numberColumns = numberColumns
        self.listPk = []
        self.listFK = []
        
        self.izq = None
        self.der = None
        self.factor = 1
        
        
    def verifyListPk(self):
        if len(self.listPk) == 0:
            return True
        return False
    
    
    def verifyColumns(self, columnsList):
        columnas = len(columnsList)
        if (columnas > 0) and (columnas <= self.numberColumns):
            return True
        return False
    
    
    def verifyColumnPk(self, columnNumber):
        if (columnNumber in self.listPk) or (self.numberColumns == 1):
            return True
        return False
    
    
    def verifyOutOfRange(self, column):
        if 0 <= column <= (self.numberColumns - 1):
            return False
        return True
    
    
    def updateListPk(self, newListPk):
        self.listPk = []
        self.listPk = newListPk
        
        
    def alterAddPk(self, columns):
        bandera = True
        dataList = self.bPlus.verify_Nodes()
        if len(dataList) != 0:
            for i in columns:
                listaColumna = []
                for j in dataList:
                    listaColumna.append(j.register[i])
                for j in dataList:
                    if listaColumna.count(j.register[i]) > 1:
                        bandera = False
                        return 1


        if bandera:
            self.updateListPk(columns)
            self.bPlus.set_PK(columns)

            # Reestructuracion del arbol
            if self.bPlus.get_root() is not None:
                self.bPlus.set_root(None)  # "Eliminando" arbol
                for i in dataList:
                    self.bPlus.insert(i.register)
            # self.bPlus.graphTree()
            return 0

        
    def alterDropPk(self):
        self.listPk = []
        self.bPlus.set_PK([])
        self.bPlus.set_hide(True)
        self.bPlus.set_contador(1)
        return 0
    

class AVLL_TABLE:

    def __init__(self):
        self.raiz = None

    def insertar(self,tabla,valor):
        self.raiz = self.__insertar(self.raiz,tabla,name)

    def __insertar(self,nodo,tabla,name):
        #Insertar nodos
        if nodo == None:
            return Nodo(tabla,name)
        elif name < nodo.name:
            nodo.izq = self.__insertar(nodo.izq,tabla,name)
        elif name > nodo.name:
            nodo.der = self.__insertar(nodo.der,tabla,name)
        
        #Determinar el Factor
        nodo.factor = 1 + max(self.__obtenerFactor(nodo.der),self.__obtenerFactor(nodo.izq))

        factorBalance = self.__obtenerBalance(nodo)

        #Rotaciones
        if factorBalance > 1 and name < nodo.izq.name:
            return self.__rotacionDerecha(nodo)
        if factorBalance < -1 and name > nodo.der.name:
            return self.__rotacionIzquierda(nodo)
        if factorBalance > 1 and name > nodo.izq.name:
            nodo.izq = self.__rotacionIzquierda(nodo.izq)
            return self.__rotacionDerecha(nodo)
        if factorBalance < -1 and name < nodo.der.name:
            nodo.der = self.__rotacionDerecha(nodo.der)
            return self.__rotacionIzquierda(nodo)

        return nodo
    
    def __obtenerFactor(self,nodo):
        if nodo == None:
            return 0
        
        return nodo.factor

    def __obtenerBalance(self,nodo):
        if nodo == None:
            return 0
        
        return self.__obtenerFactor(nodo.izq) - self.__obtenerFactor(nodo.der)

    def __rotacionDerecha(self,nodo):
        #declarar nodos a mover
        nodo2 = nodo.izq
        nodo2_1 = nodo2.der
        #mover nodos
        nodo2.der = nodo
        nodo.izq = nodo2_1
        #recalcular factor
        nodo.factor = 1 + max(self.__obtenerFactor(nodo.izq),self.__obtenerFactor(nodo.der))
        nodo2.factor = 1 + max(self.__obtenerFactor(nodo2.izq),self.__obtenerFactor(nodo.der))

        return nodo2

    def __rotacionIzquierda(self,nodo):
        #declarar nodos a mover
        nodo2 = nodo.der
        nodo2_1 = nodo2.izq
        #mover nodos
        nodo.der = nodo2_1
        nodo2.izq = nodo
        #recalcular factor
        nodo.factor = 1 + max(self.__obtenerFactor(nodo.izq),self.__obtenerFactor(nodo.der))
        nodo2.factor = 1 + max(self.__obtenerFactor(nodo2.izq),self.__obtenerFactor(nodo.der))

        return nodo2

    def eliminar(self,valor):
        nodo = self.__eliminar(self.raiz,valor)



    def __eliminar(self,raiz,name):

        #Buscar el nodo
        if raiz == None:
            return raiz
        elif name < raiz.name:
            raiz.izq = self.__eliminar(raiz.izq,name)
        elif name > raiz.name:
            raiz.der = self.__eliminar(raiz.der,name)
        else:
            #Nodo Hoja
            if raiz.factor == 1:
                raiz = self.__caso1(raiz)
                return raiz
            #Nodo con dos hijos
            elif raiz.der != None and raiz.izq != None:
                valores = self.__caso2(raiz.izq)
                raiz.izq = valores.nodo
                raiz.valor = valores.valor
                return raiz
            #Nodo con un hijo
            elif raiz.der != None or raiz.izq != None:
                raiz = self.__caso3(raiz)
                return raiz

        #Determinar el Factor
        raiz.factor = 1 + max(self.__obtenerFactor(raiz.der),self.__obtenerFactor(raiz.izq))

        factorBalance = self.__obtenerBalance(raiz)

        #Rotaciones
        if factorBalance > 1 and self.__obtenerBalance(raiz.izq) >= 0: 
            return self.__rotacionDerecha(raiz) 
        if factorBalance < -1 and self.__obtenerBalance(raiz.der) <= 0: 
            return self.__rotacionIzquierda(raiz) 
        if factorBalance > 1 and self.__obtenerBalance(raiz.izq) < 0: 
            raiz.izq = self.__rotacionIzquierda(raiz.izq) 
            return self.__rotacionDerecha(raiz) 
        if factorBalance < -1 and self.__obtenerBalance(raiz.der) > 0: 
            raiz.der = self.__rotacionDerecha(raiz.der) 
            return self.__rotacionIzquierda(raiz)  

        return raiz

    #Funcion caso 1
    def __caso1(self,nodo):
        nodo = None
        return nodo
    
    #Funcion caso 2
    def __caso2(self,nodo):
        class NodoyValor:
            def __init__(self):
                self.nodo = None
                self.valor = 0

        if nodo.der == None:
            valores = NodoyValor()
            valores.valor = nodo.name
            nodo = None
            valores.nodo = nodo
            return valores
        
        rotorno = self.__caso2(nodo.der)
        nodo.der = rotorno.nodo
        rotorno.nodo = nodo
        return rotorno
    
    #Funcion caso 3
    def __caso3(self,nodo):
        if nodo.der != None:
            nodo = nodo.der
            return nodo
        else:
            nodo = nodo.izq
            return nodo

    #Metodo para Graficar
    def graficar(self):
        if self.raiz != None:
            graph = 'digraph G{\n'
            graph += "node[shape = \"record\"]\n"
            graph += self.__graficar(self.raiz)
            graph += '}'
            file = open("AVL_T.dot","w")
            file.write(graph)
            file.close()
            os.system('dot -Tpng AVL_T.dot -o AVL_T.png')
        else:
            print('No ha Bases de datos')

    def __graficar(self,raiz):
        if raiz == None:
            return ''

        graph = ''
        
        graph += self.__graficar(raiz.der)
        graph += self.__graficar(raiz.izq)

        nodo = 'node' + str(raiz.name)

        if raiz.factor == 1:
            graph += nodo + '[label=' + str(raiz.name) + ']\n'
        else:
            graph += nodo + '[label=\"<f0>|{' + str(raiz.name) + '}|<f2>\"]\n'
            if raiz.izq != None:
                graph += nodo + ':f0 -> ' + 'node' + str(raiz.izq.name) + '\n'
            if raiz.der != None:
                graph += nodo + ':f2 -> ' + 'node' + str(raiz.der.name) + '\n'
        
        return graph

    def recorrido(self):
        lista_BD = self.__recorrido(self.raiz)
        return lista_BD

    def __recorrido(self,nodo):
        bases = ''

        if nodo == None:
            return ''

        bases += str(self.__recorrido(nodo.izq))
        bases += nodo.name + ' '
        bases += str(self.__recorrido(nodo.der))

        return bases
    
    def buscar(self, name):
        resultado = self.__buscar(name, self.raiz)
        return resultado

    def __buscar(self, name, nodo):
        if nodo is not None:
            if name < nodo.name:
                nodo = self.__buscar(name, nodo.izq)
            elif name > nodo.name:
                nodo = self.__buscar(name, nodo.der)
        return nodo

    # Metodo para actualizar
    def actualizar(self, valor_actual, nuevo_valor):
        nodo = self.buscar(valor_actual)

        if nodo is not None:
            self.insertar(nodo.bPlus, nuevo_valor, nodo.numberColumns)
            self.eliminar(nodo.name)
            return 'exito'
        else:
            return 'error'

    def lista_tablas(self):
        lista = []
        lista_db = self._lista_tablas(self.raiz, lista)
        return lista_db

    def _lista_tablas(self, nodo, lista):
        if nodo is not None:
            lista.append(nodo.name)
            self._lista_tablas(nodo.izq, lista)
            self._lista_tablas(nodo.der, lista)
            return lista
