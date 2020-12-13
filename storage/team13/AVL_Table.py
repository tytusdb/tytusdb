import os

class Nodo:

    def __init__(self,valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.factor = 1


class Avl:

    def __init__(self):
        self.raiz = None

    def insertar(self,valor):
        self.raiz = self.__insertar(self.raiz,valor)

    def __insertar(self,nodo,valor):
        #Insertar nodos
        if nodo == None:
            return Nodo(valor)
        elif valor < nodo.valor:
            nodo.izq = self.__insertar(nodo.izq,valor)
        elif valor > nodo.valor:
            nodo.der = self.__insertar(nodo.der,valor)
        
        #Determinar el Factor
        nodo.factor = 1 + max(self.__obtenerFactor(nodo.der),self.__obtenerFactor(nodo.izq))

        factorBalance = self.__obtenerBalance(nodo)

        #Rotaciones
        if factorBalance > 1 and valor < nodo.izq.valor:
            return self.__rotacionDerecha(nodo)
        if factorBalance < -1 and valor > nodo.der.valor:
            return self.__rotacionIzquierda(nodo)
        if factorBalance > 1 and valor > nodo.izq.valor:
            nodo.izq = self.__rotacionIzquierda(nodo.izq)
            return self.__rotacionDerecha(nodo)
        if factorBalance < -1 and valor < nodo.der.valor:
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



    def __eliminar(self,raiz,valor):

        #Buscar el nodo
        if raiz == None:
            return raiz
        elif valor < raiz.valor:
            raiz.izq = self.__eliminar(raiz.izq,valor)
        elif valor > raiz.valor:
            raiz.der = self.__eliminar(raiz.der,valor)
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
            valores.valor = nodo.valor
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
            file = open("AVL_DB.dot","w")
            file.write(graph)
            file.close()
            os.system('dot -Tpng AVL_DB.dot -o AVL_DB.png')
        else:
            print('No ha Bases de datos')

    def __graficar(self,raiz):
        if raiz == None:
            return ''

        graph = ''
        
        graph += self.__graficar(raiz.der)
        graph += self.__graficar(raiz.izq)

        nodo = 'node' + str(raiz.valor)

        if raiz.factor == 1:
            graph += nodo + '[label=' + str(raiz.valor) + ']\n'
        else:
            graph += nodo + '[label=\"<f0>|{' + str(raiz.valor) + '}|<f2>\"]\n'
            if raiz.izq != None:
                graph += nodo + ':f0 -> ' + 'node' + str(raiz.izq.valor) + '\n'
            if raiz.der != None:
                graph += nodo + ':f2 -> ' + 'node' + str(raiz.der.valor) + '\n'
        
        return graph