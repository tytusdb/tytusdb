from storageManager.Nodo_AVL import Nodo_AVL
import os

class Arbol_AVL:
    def __init__(self):
        self.root = None

    def __getAltura(self, nodo):
        #'if not nodo' quiere decir que se ejecutara si nodo es nulo o vacio
        if not nodo:
            return 0

        return nodo.altura

    def __rotarDerecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        #Funcionamiento de la rotacion
        x.derecha = y
        y.izquierda = T2

        #Actualizacion de alturas
        y.altura = max(self.__getAltura(y.izquierda), self.__getAltura(y.derecha)) + 1
        x.altura = max(self.__getAltura(x.izquierda), self.__getAltura(x.derecha)) + 1

        #Se retorna la nueva raiz
        return x

    def __rotarIzquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        #Funcionamiento de la rotacion
        y.izquierda = x
        x.derecha = T2

        #Actualizacion de alturas
        x.altura = max(self.__getAltura(x.izquierda), self.__getAltura(x.derecha)) + 1
        y.altura = max(self.__getAltura(y.izquierda), self.__getAltura(y.derecha)) + 1

        #Se retorna la nueva raiz
        return y

    def __getBalance(self, nodo):
        #'if not nodo' quiere decir que se ejecutara si nodo es nulo o vacio
        if not nodo:
            return 0

        return self.__getAltura(nodo.izquierda) - self.__getAltura(nodo.derecha)

    def insertar(self, objeto):
        self.root = self.__insertarObjeto(self.root, objeto)

    def __insertarObjeto(self, nodo, obj):

        #Insercion normal
        if not nodo:
            return Nodo_AVL(obj)
        
        if obj.getNombreASCII() < nodo.objeto.getNombreASCII():
            nodo.izquierda = self.__insertarObjeto(nodo.izquierda, obj)
        elif obj.getNombreASCII() > nodo.objeto.getNombreASCII():
            nodo.derecha = self.__insertarObjeto(nodo.derecha, obj)
        else:
            #Nodos iguales no son permitidos
            #Nodos con el mismo ascii(nombre) pero diferente nombre
            if obj.nombre != nodo.objeto.nombre:
                nodo.derecha = self.__insertarObjeto(nodo.derecha, obj)
            else:#Si tienen el mismo ascii(nombre) solo retorna el nodo
                return nodo
        
        #Actualizar altura del nodo antecesor al nodo insertado
        nodo.altura = 1 + max(self.__getAltura(nodo.izquierda), self.__getAltura(nodo.derecha))

        #Obtener el factor balance del nodo antecesor al nodo insertado
        #Notar que no quede desbalanceado
        balance = self.__getBalance(nodo)

        #Caso rotacion simple -> izquierda izquierda
        #El nodo ingresado se encuentra a la izquierda de su antecesor
        #    /n
        #   /n
        #  /nodonuevo
        if balance > 1 and obj.getNombreASCII() < nodo.izquierda.objeto.getNombreASCII():
            return self.__rotarDerecha(nodo)

        #Caso rotacion simple -> derecha derecha
        #El nodo ingresado se encuentra a la derecha de su antecesor
        #  \n
        #   \n
        #    \nodonuevo
        if balance < -1 and obj.getNombreASCII() > nodo.derecha.objeto.getNombreASCII():
            return self.__rotarIzquierda(nodo)

        #Caso rotacion doble -> izquierda derecha
        #El nodo ingresado se encuentra a la derecha de su antecesor
        #   /n
        #  /n
        #   \\nodonuevo
        if balance > 1 and obj.getNombreASCII() > nodo.izquierda.objeto.getNombreASCII():
            nodo.izquierda = self.__rotarIzquierda(nodo.izquierda)
            return self.__rotarDerecha(nodo)

        #Caso rotacion doble -> derecha izquierda
        #El nodo ingresado se encuentra a la izquierda de su antecesor
        #  \n
        #   \n
        #  /nodonuevo
        if balance < -1 and obj.getNombreASCII() < nodo.derecha.objeto.getNombreASCII():
            nodo.derecha = self.__rotarDerecha(nodo.derecha)
            return self.__rotarIzquierda(nodo)

        #Se retorna el nodo sin cambios
        return nodo

    def __nodoMenorValor(self, nodo):
        actual = nodo

        while actual.izquierda != None:
            actual = actual.izquierda
        
        return actual

    def eliminar(self, objeto):
        self.root = self.__eliminarObjeto(self.root, objeto)

    def __eliminarObjeto(self, nodo, obj):
        #Retornar None si no hay nodos
        if not nodo:
            return nodo

        #Si el identificador que será eliminado es menor que el
        #identificador de la raiz, entonces se busca hacia la izquierda
        if obj.getNombreASCII() < nodo.objeto.getNombreASCII():
            nodo.izquierda = self.__eliminarObjeto(nodo.izquierda, obj)
        elif obj.getNombreASCII() > nodo.objeto.getNombreASCII():#Identificador a eliminar es mayor al del nodo, se busca hacia la derecha
            nodo.derecha = self.__eliminarObjeto(nodo.derecha, obj)
        else:#Encontro el identificador. Validacion si es el mismo identificador pero no el mismo nombre
            if obj.nombre == nodo.objeto.nombre:
                #Nodo con solo un hijo o sin hijos
                if nodo.izquierda is None:
                    temp = nodo.derecha
                    nodo = None
                    return temp
                elif nodo.derecha is None:
                    temp = nodo.izquierda
                    nodo = None
                    return temp

                #Nodo con dos hijos. Se obtiene el sucesor mas pequeno de la derecha
                temp = self.__nodoMenorValor(nodo.derecha)

                #Copiar los datos del sucesor a nodo
                nodo.objeto.nombre = temp.objeto.nombre
                nodo.objeto.estructura = temp.objeto.estructura

                #Eliminar el sucesor
                nodo.derecha = self.__eliminarObjeto(nodo.derecha, temp.objeto)
            else:#Si el nombre no es el mismo sigue buscando hacia la derecha
                nodo.derecha = self.__eliminarObjeto(nodo.derecha, obj)

        #Si el arbol se quedo vacio
        if nodo is None:
            return nodo
        
        nodo = self.__factorEquilibrio(nodo)
        return nodo

    def __factorEquilibrio(self, nodo):
        #Actualizar altura del nodo actual
        nodo.altura = 1 + max(self.__getAltura(nodo.izquierda), self.__getAltura(nodo.derecha))

        #Obtener el balance del nodo
        balance = self.__getBalance(nodo)

        #Si el nodo queda desbalanceado hay 4 casos:

        #Caso rotacion simple -> izquierda izquierda
        #El nodo ingresado se encuentra a la izquierda de su antecesor
        #    /n
        #   /n
        #  /nodonuevo
        if balance > 1 and self.__getBalance(nodo.izquierda) >= 0:
            return self.__rotarDerecha(nodo)

        #Caso rotacion simple -> derecha derecha
        #El nodo ingresado se encuentra a la derecha de su antecesor
        #  \n
        #   \n
        #    \nodonuevo
        if balance < -1 and self.__getBalance(nodo.derecha) <= 0:
            return self.__rotarIzquierda(nodo)

        #Caso rotacion doble -> izquierda derecha
        #El nodo ingresado se encuentra a la derecha de su antecesor
        #   /n
        #  /n
        #   \\nodonuevo
        if balance > 1 and self.__getBalance(nodo.izquierda) < 0:
            nodo.izquierda = self.__rotarIzquierda(nodo.izquierda)
            return self.__rotarDerecha(nodo)

        #Caso rotacion doble -> derecha izquierda
        #El nodo ingresado se encuentra a la izquierda de su antecesor
        #  \n
        #   \n
        #  /nodonuevo
        if balance < -1 and self.__getBalance(nodo.derecha) > 0:
            nodo.derecha = self.__rotarDerecha(nodo.derecha)
            return self.__rotarIzquierda(nodo)

        #Se retorna el nodo sin cambios
        return nodo

    # Retorna el nodo donde se encuentra el objeto buscado
    def buscarObjeto(self, id, nombre):
        buscado = self.__buscarObjeto(self.root, id, nombre)
        return buscado
    
    def __buscarObjeto(self, raiz, id, nombre):
        if not raiz:
            return raiz
        elif id < raiz.objeto.getNombreASCII():
            raiz = self.__buscarObjeto(raiz.izquierda, id, nombre)
        elif id > raiz.objeto.getNombreASCII():
            raiz = self.__buscarObjeto(raiz.derecha, id, nombre)
        else:
            #Comprobar por nombre la base de datos
            if nombre == raiz.objeto.nombre:
                '''Solo retorna la raiz'''
            else:
                raiz = self.__buscarObjeto(raiz.derecha, id, nombre)
        return raiz

    def __dot(self, raiz):
        dot = ""
        if raiz is None:
            return dot
        
        if raiz.izquierda != None:
            dot += self.__dot(raiz.izquierda)
            dot += "\"" + raiz.objeto.nombre + "\" -> \"" + raiz.izquierda.objeto.nombre + "\"\n"

        if raiz.derecha != None:
            dot += self.__dot(raiz.derecha)
            dot += "\"" + raiz.objeto.nombre + "\" -> \"" + raiz.derecha.objeto.nombre + "\"\n"

        return dot + "\"" + raiz.objeto.nombre + "\" [label = \"" + str(raiz.objeto.getNombreASCII()) + "\n" + raiz.objeto.nombre + "\", fillcolor = orange]\n"
    
    def __getDot(self):
        if self.root is None:
            return "\n\n"
        else:
            return "\n\n" + self.__dot(self.root) + "\n"

    def reporteDB(self):
        dot = open("DB.dot", "w")
        dot.write("digraph G{\n")
        dot.write("nodesep = 0.8\n")
        dot.write("ranksep = 0.5\n")
        dot.write("node [style = filled, fillcolor = white]\n")
        dot.write(self.__getDot())
        dot.write("}")
        dot.close()

        os.system('dot -Tpng DB.dot -o DB.png')

    def reporteTablas(self):
        dot = open("Tablas.dot", "w")
        dot.write("digraph G{\n")
        dot.write("nodesep = 0.8\n")
        dot.write("ranksep = 0.5\n")
        dot.write("node [style = filled, fillcolor = white]\n")
        dot.write(self.__getDot())
        dot.write("}")
        dot.close()

        os.system('dot -Tpng Tablas.dot -o Tablas.png')

    def getListaNombres(self):
        lista = []
        self.imprimirInOrden(self.root, lista)
        
        return lista

    def imprimirInOrden(self, raiz, lista):
        if raiz != None:
            self.imprimirInOrden(raiz.izquierda, lista)
            lista.append(raiz.objeto.nombre)
            self.imprimirInOrden(raiz.derecha, lista)

    def getObjetosList(self):
        listaOb = []
        self.imprimirPreOrden(self.root, listaOb)

        return listaOb

    def imprimirPreOrden(self, raiz, listaOb):
        if raiz != None:
            listaOb.append(raiz.objeto)
            self.imprimirPreOrden(raiz.izquierda, listaOb)
            self.imprimirPreOrden(raiz.derecha, listaOb)

    def imprimirPosOrden(self, raiz):
        if raiz != None:
            self.imprimirPosOrden(raiz.izquierda)
            self.imprimirPosOrden(raiz.derecha)
            print(raiz.objeto.nombre, " ", str(raiz.objeto.getNombreASCII()))

    def getRoot(self):
        return self.root
