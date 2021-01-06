# Package:      BPlusMode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team

import os


class Nodo:
    def __init__(self, bPlus, name, numberColumns):
        self.bPlus = bPlus
        self.name = name
        self.numberColumns = numberColumns
        self.listPk = []
        self.listFK = []

        self.izq = None
        self.der = None
        self.factor = 1

    def set_numberColumns(self, numberColumns):
        self.numberColumns = numberColumns

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
        for i in columns:
            if self.verifyOutOfRange(int(i)):
                return 5
        bandera = True
        listaObjetos = []
        dataList = self.bPlus.alterColumnsData(columns, listaObjetos)
        if len(dataList) != 0:
            for j in dataList:
                if dataList.count(j) > 1:
                    bandera = False
                    return 1

        if bandera:
            self.updateListPk(columns)
            self.bPlus.set_PK(columns)

            if self.bPlus.get_root() is not None:
                self.bPlus.set_root(None) 
                for i in listaObjetos:
                    self.bPlus.insert(i.register)
            return 0

    def alterDropPk(self):
        self.listPk = []
        self.bPlus.set_PK([])
        self.bPlus.set_hide(True)
        self.bPlus.set_contador(1)
        return 0

class AVL_TABLE:

    def __init__(self):
        self.raiz = None

    def insertar(self, bPlus, name, numberColumns):
        self.raiz = self.__insertar(self.raiz, bPlus, name, numberColumns)

    def __insertar(self, nodo, bPlus, name, numberColumns):
        if nodo == None:
            return Nodo(bPlus, name, numberColumns)
        elif name < nodo.name:
            nodo.izq = self.__insertar(nodo.izq, bPlus, name, numberColumns)
        elif name > nodo.name:
            nodo.der = self.__insertar(nodo.der, bPlus, name, numberColumns)

        nodo.factor = 1 + max(self.__obtenerFactor(nodo.der), self.__obtenerFactor(nodo.izq))

        factorBalance = self.__obtenerBalance(nodo)

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

    def __obtenerFactor(self, nodo):
        if nodo == None:
            return 0

        return nodo.factor

    def __obtenerBalance(self, nodo):
        if nodo == None:
            return 0

        return self.__obtenerFactor(nodo.izq) - self.__obtenerFactor(nodo.der)

    def __rotacionDerecha(self, nodo):
        nodo2 = nodo.izq
        nodo2_1 = nodo2.der
        nodo2.der = nodo
        nodo.izq = nodo2_1
        nodo.factor = 1 + max(self.__obtenerFactor(nodo.izq), self.__obtenerFactor(nodo.der))
        nodo2.factor = 1 + max(self.__obtenerFactor(nodo2.izq), self.__obtenerFactor(nodo.der))

        return nodo2

    def __rotacionIzquierda(self, nodo):
        nodo2 = nodo.der
        nodo2_1 = nodo2.izq
        nodo.der = nodo2_1
        nodo2.izq = nodo
        nodo.factor = 1 + max(self.__obtenerFactor(nodo.izq), self.__obtenerFactor(nodo.der))
        nodo2.factor = 1 + max(self.__obtenerFactor(nodo2.izq), self.__obtenerFactor(nodo.der))

        return nodo2

    def eliminar(self, name):
        self.raiz = self.__eliminar(self.raiz, name)

    def __eliminar(self, raiz, name):

        if raiz == None:
            return raiz
        elif name < raiz.name:
            raiz.izq = self.__eliminar(raiz.izq, name)
        elif name > raiz.name:
            raiz.der = self.__eliminar(raiz.der, name)
        else:
            if raiz.factor == 1:
                raiz = self.__caso1(raiz)
                return raiz
            elif raiz.der != None and raiz.izq != None:
                valores = self.__caso2(raiz.izq)
                raiz.izq = valores.nodo
                raiz.name = valores.bPlus
                raiz = self.__balance(raiz)
                return raiz
            elif raiz.der != None or raiz.izq != None:
                raiz = self.__caso3(raiz)
                return raiz

        raiz = self.__balance(raiz)
        return raiz


    def __balance(self,raiz):
        raiz.factor = 1 + max(self.__obtenerFactor(raiz.der), self.__obtenerFactor(raiz.izq))

        factorBalance = self.__obtenerBalance(raiz)

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

    def __caso1(self, nodo):
        nodo = None
        return nodo

    def __caso2(self, nodo):
        class NodoyValor:
            def __init__(self):
                self.nodo = None
                self.bPlus = 0

        if nodo.der == None:
            if nodo.factor == 1:
                valores = NodoyValor()
                valores.bPlus = nodo.name
                nodo = None
                valores.nodo = nodo
                return valores
            elif nodo.izq != None:
                valores = NodoyValor()
                valores.bPlus = nodo.name
                valores.nodo = nodo.izq
                nodo = None
                return valores


        rotorno = self.__caso2(nodo.der)
        nodo.der = rotorno.nodo
        rotorno.nodo = nodo
        return rotorno

    def __caso3(self, nodo):
        if nodo.der != None:
            nodo = nodo.der
            return nodo
        else:
            nodo = nodo.izq
            return nodo

    def graficar(self):
        if self.raiz != None:
            graph = 'digraph G{\n'
            graph += "node[shape = \"record\"]\n"
            graph += self.__graficar(self.raiz)
            graph += '}'
            file = open("AVL_T.dot", "w")
            file.write(graph)
            file.close()
            os.system('dot -Tpng AVL_T.dot -o AVL_T.png')
        else:
            print('No ha Bases de datos')

    def __graficar(self, raiz):
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
        lista_T = self.__recorrido(self.raiz)
        return lista_T

    def __recorrido(self, nodo):
        tablas = ''

        if nodo == None:
            return ''

        tablas += str(self.__recorrido(nodo.izq))
        tablas += nodo.name + ' '
        tablas += str(self.__recorrido(nodo.der))

        return tablas



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
