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
