#Clase principal de la Estructura de Datos

from graphviz import Digraph, nohtml
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

#Clase Nodo de Arbol AVL
class NodoAVL:
    #Constructor de Nodo de Arbol Binario de Busqueda
    def __init__(self,clave,valor=None,datos=None,hizq=None,hder=None,padre=None):
        self.clave = clave
        self.valor = valor
        self.datos = datos
        self.Izq = hizq
        self.Der = hder
        self.padre = padre
        self.factorEquilibrio = 0

    #Devuelve el hijo a la izquierda
    def tieneIzq(self):
        return self.Izq

    #Devuelve el hijo a la derecha
    def tieneDer(self):
        return self.Der

    #Verifica si un nodo es hijo a la izquierda
    def esIzq(self):
        return self.padre and self.padre.Izq == self

    #Verifica si un nodo es hijo a la derecha
    def esDer(self):
        return self.padre and self.padre.Der == self

    #Verifica si un nodo es la raiz de un arbol
    def esRaiz(self):
        return not self.padre

    #Verifica si un nodo es una hoja
    def esHoja(self):
        return not (self.Der or self.Izq)

    #Verifica si un nodo tiene hijo(s)
    def tieneAlgunHijo(self):
        return self.Der or self.Izq

    #Verifica si un nodo tiene ambos hijos
    def tieneAmbosHijos(self):
        return self.Der and self.Izq

    #Reemplaza datos de un nodo
    def reemplazar(self,clave,datos,hizq,hder):
        self.clave = clave
        self.datos = datos
        self.Izq = hizq
        self.Der = hder
        self.factorEquilibrio = 0
        if self.tieneIzq():
            self.Izq.padre = self
        if self.tieneDer():
            self.Der.padre = self

    #Auxiliar en la eliminacion, despues de eliminar al sucesor
    def unir(self):
       if self.esHoja():
           if self.esIzq():
                self.padre.Izq = None
           else:
                self.padre.Der = None
       elif self.tieneAlgunHijo():
           if self.tieneIzq():
                if self.esIzq():
                    self.padre.Izq = self.Izq
                else:
                    self.padre.Der = self.Izq
                self.Izq.padre = self.padre
           else:
                if self.esIzq():
                    self.padre.Izq = self.Der
                else:
                    self.padre.Der = self.Der
                self.Der.padre = self.padre

    #Auxiliar en la eliminación, busca al nodo sucesor
    def sucesor(self):
      suc = None
      if self.tieneDer():
          suc = self.Der.encontrarMin()
      else:
          if self.padre:
                 if self.esIzq():
                     suc = self.padre
                 else:
                     self.padre.Der = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.Der = self
      return suc

    #Encuentra la clave mínima de un subárbol
    def encontrarMin(self):
      actual = self
      while actual.tieneIzq():
          actual = actual.Izq
      return actual

    #Sobrecarga del método iter para recorrido inorden
    def __iter__(self):
        if self:
            if self.tieneIzq():
                for elem in self.Izq:
                    yield elem
            yield self.clave
            if self.tieneDer():
                for elem in self.Der:
                    yield elem

    #Extrae los datos de un arbol en recorrido inorden
    def extraer(self, arbol, lista):
        if arbol:
            self.extraer(arbol.Izq, lista)
            lista.append(arbol.valor)
            self.extraer(arbol.Der, lista)
    
    #Agrega una Columna en cada registro con un valor default
    def agregaColumna(self, arbol, default):
        if arbol:
            self.agregaColumna(arbol.Izq, default)
            arbol.valor.append(default)
            self.agregaColumna(arbol.Der, default)

    #Quita una Columna en cada registro
    def quitaColumna(self, arbol, pos):
        if arbol:
            self.quitaColumna(arbol.Izq, pos)
            arbol.valor.pop(pos)
            self.quitaColumna(arbol.Der, pos)

#Clase Arbol AVL
class AVL:
    #Constructor de Arbol Binario de Busqueda
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    #Tamano del Arbol Binario de Busqueda
    def obtTamano(self):
        return self.tamano

    #Sobrecarga del operador método len
    def __len__(self):
        return self.tamano
    
    #Comprobacion de factores de equilibrio despues de la insercion
    def comprobarInsercion(self,n):
        y = n
        x = n.padre
        fin = False
        while fin == False and x != None:
            if x.Izq == y: #y es hijo izquierdo
                x.factorEquilibrio += 1
                if x.factorEquilibrio == 2: #Reestructuracion y final
                    if y.factorEquilibrio == -1:
                        #Doble rotacion a la derecha
                        self.rotacion_doble_neg(x)
                    else:
                        #Rotacion simple a la derecha
                        self.rotacion_simple_neg(x)
                    fin = True
                elif x.factorEquilibrio == 1: #Continuar
                    y = x
                    x = x.padre
                else: #Final x.factorEquilibrio = 0
                    fin = True
            else: #x.Der = y, o sea, y es hijo Derecho
                x.factorEquilibrio -= 1
                if x.factorEquilibrio == -2: #Reestructuracion y final
                    if y.factorEquilibrio == 1:
                        #doble rotacion a la izquierda
                        self.rotacion_doble_pos(x)
                    else:
                        #rotacion simple a la izquierda
                        self.rotacion_simple_pos(x)
                    fin = True
                elif x.factorEquilibrio == -1: #Continuar
                    y = x
                    x = x.padre
                else: #Final x.factorEquilibrio = 0
                    fin = True

    def aaaagregar(self,clave,valor=None,datos=None) -> int:
        tamanoinicial = self.tamano
        if self.raiz:
            nodo = self._obtener(clave,self.raiz)
            if nodo:
                datos = AVL()
                nuevoNodo = NodoAVL(clave,valor,datos,padre=nodoActual)
                nuevoNodo.padre = nodo
                if clave < nodo.clave:
                    nodo.Izq = nuevoNodo
                else:
                    nodo.Der = nuevoNodo
                self.tamano = self.tamano + 1
                self.comprobarInsercion(nuevoNodo)
        else:
            datos = AVL()
            self.raiz = NodoAVL(clave,valor,datos)
            self.tamano = self.tamano + 1
        if tamanoinicial == self.tamano:
            return 2
        else:
            return 0

    #Agrega nodo al arbol (Asigna nodo a raiz si está vacía, o llama a _agregar si no está vacóa)
    def agregar(self,clave,valor=None,datos=None) -> int:
        tamanoinicial = self.tamano
        if self.raiz:
            self._agregar(clave,valor,datos,self.raiz)
        else:
            datos = AVL()
            self.raiz = NodoAVL(clave,valor,datos)
            self.tamano = self.tamano + 1
        if tamanoinicial == self.tamano:
            return 2
        else:
            return 0

    #Rotacion simple a la izquierda
    def rotacion_simple_pos(self, x):
        y = x.Der
        b = y.Izq
        #Modificar enlaces del padre de x
        if x.padre:
            if x.padre.Izq == x:
                x.padre.Izq = y
            else:
                x.padre.Der = y
        else:
            self.raiz = y
        y.padre = x.padre
        y.Izq = x
        x.padre = y
        x.Der = b
        if b:
            b.padre = x
        #Factores de equilibrio
        if y.factorEquilibrio == -1:
            y.factorEquilibrio = 0
            x.factorEquilibrio = 0
        else:
            y.factorEquilibrio = 1
            x.factorEquilibrio = -1
    
    #Rotacion simple a la derecha
    def rotacion_simple_neg(self, x):
        y = x.Izq
        b = y.Der
        #Modificar enlaces del padre de x
        if x.padre:
            if x.padre.Izq == x:
                x.padre.Izq = y
            else:
                x.padre.Der = y
        else:
            self.raiz = y
        y.padre = x.padre
        y.Der = x
        x.padre = y
        x.Izq = b
        if b:
            b.padre = x
        #Factores de equilibrio
        if y.factorEquilibrio == 1:
            y.factorEquilibrio = 0
            x.factorEquilibrio = 0
        else:
            y.factorEquilibrio = -1
            x.factorEquilibrio = 1

    #Rotacion doble a la izquierda
    def rotacion_doble_pos(self, x):
        y = x.Der
        z = y.Izq
        b = z.Izq
        c = z.Der
        #Modificar enlaces del padre de x
        if x.padre:
            if x.padre.Izq == x:
                x.padre.Izq = z
            else:
                x.padre.Der = z
        else:
            self.raiz = z
        z.padre = x.padre
        z.Izq = x
        z.Der = y
        x.padre = z
        x.Der = b
        y.padre = z
        y.Izq = c
        if b:
            b.padre = x
        if c:
            c.padre = y
        #Factores de equilibrio
        if z.factorEquilibrio == 1:
            x.factorEquilibrio = 0
            y.factorEquilibrio = -1
        elif z.factorEquilibrio == 0:
            x.factorEquilibrio = 0
            y.factorEquilibrio = 0
        else: #z.factorEquilibrio = -1
            x.factorEquilibrio = 1
            y.factorEquilibrio = 0
        z.factorEquilibrio = 0

    #Rotacion doble a la derecha
    def rotacion_doble_neg(self, x):
        y = x.Izq
        z = y.Der
        b = z.Izq
        c = z.Der
        #Modificar enlaces del padre de x
        if x.padre:
            if x.padre.Izq == x:
                x.padre.Izq = z
            else:
                x.padre.Der = z
        else:
            self.raiz = z
        z.padre = x.padre
        z.Izq = y
        z.Der = x
        x.padre = z
        x.Izq = c
        y.padre = z
        y.Der = b
        if b:
            b.padre = y
        if c:
            c.padre = x
        #Factores de equilibrio
        if z.factorEquilibrio == 1:
            x.factorEquilibrio = -1
            y.factorEquilibrio = 0
        elif z.factorEquilibrio == 0:
            x.factorEquilibrio = 0
            y.factorEquilibrio = 0
        else: #z.factorEquilibrio = -1
            x.factorEquilibrio = 0
            y.factorEquilibrio = 1
        z.factorEquilibrio = 0

    #Realiza una rotación a la izquierda
    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.Der
        rotRaiz.Der = nuevaRaiz.Izq
        if nuevaRaiz.Izq != None:
            nuevaRaiz.Izq.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esIzq():
                rotRaiz.padre.Izq = nuevaRaiz
            else:
                rotRaiz.padre.Der = nuevaRaiz
        nuevaRaiz.Izq = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)

    #Realiza una rotación a la derecha
    def rotarDerecha(self,rotRaiz):
        nuevaRaiz = rotRaiz.Izq
        rotRaiz.Izq = nuevaRaiz.Der
        if nuevaRaiz.Der != None:
            nuevaRaiz.Der.padre = rotRaiz
        nuevaRaiz.padre = rotRaiz.padre
        if rotRaiz.esRaiz():
            self.raiz = nuevaRaiz
        else:
            if rotRaiz.esDer():
                rotRaiz.padre.Der = nuevaRaiz
            else:
                rotRaiz.padre.Izq = nuevaRaiz
        nuevaRaiz.Der = rotRaiz
        rotRaiz.padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio - 1 - max(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio - 1 - min(rotRaiz.factorEquilibrio, 0)

    #Actualiza el equilibrio en el arbol
    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
            if nodo.Der.factorEquilibrio > 0:
                self.rotarDerecha(nodo.Der)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.Izq.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.Izq)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)

    #Verifica si el arbol necesita reequilibrio al agregar
    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            #if nodo.padre.padre:
            #    if nodo.padre.padre.factorEquilibrio == 2 or nodo.padre.padre.factorEquilibrio == -2:
            #        self.reequilibrar(nodo.padre.padre)
            return
        if nodo.padre != None:
            if nodo.esIzq():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esDer():
                nodo.padre.factorEquilibrio -= 1

            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)

    #Verifica si el arbol necesita reequilibrio al eliminar
    def actualizarEquilibrioEliminar(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre != None:
            if nodo.esIzq():
                nodo.padre.factorEquilibrio -= 1
            elif nodo.esDer():
                nodo.padre.factorEquilibrio += 1

            if nodo.padre.factorEquilibrio != 0:
                self.actualizarEquilibrio(nodo.padre)

    #Agrega nodo al arbol
    def _agregar(self,clave,valor,datos,nodoActual):
        if clave == nodoActual.clave:
            return 0
        elif clave < nodoActual.clave:
            if nodoActual.tieneIzq():
                self._agregar(clave,valor,datos,nodoActual.Izq)
            else:
                datos = AVL()
                nodoActual.Izq = NodoAVL(clave,valor,datos,padre=nodoActual)
                #self.actualizarEquilibrio(nodoActual.Izq) #xyz
                self.comprobarInsercion(nodoActual.Izq)
                self.tamano = self.tamano + 1
        else:
            if nodoActual.tieneDer():
                self._agregar(clave,valor,datos,nodoActual.Der)
            else:
                datos = AVL()
                nodoActual.Der = NodoAVL(clave,valor,datos,padre=nodoActual)
                #self.actualizarEquilibrio(nodoActual.Der)
                self.comprobarInsercion(nodoActual.Der)
                self.tamano = self.tamano + 1
    
    #Sobrecarga del operador [] para asignación --> arbolbb[c] = d
    def __setitem__(self,c,v):
       return self.agregar(c,v)

    #Devuelve los datos de un nodo por medio de su clave (envia la raiz al método _obtener)
    def obtener(self,clave):
       if self.raiz:
           resultado = self._obtener(clave,self.raiz)
           if resultado:
                  return resultado
           else:
                  return None
       else:
           return None

    #Busca un nodo en el arbol por medio de la clave
    def _obtener(self,clave,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.clave == clave:
           return nodoActual
       elif clave < nodoActual.clave:
           return self._obtener(clave,nodoActual.Izq)
       else:
           return self._obtener(clave,nodoActual.Der)

    #Sobrecarga del operador [] para busqueda --> d = arbolbb[c]
    def __getitem__(self,clave):
       return self.obtener(clave)

    #Sobrecarga del operador in --> if c in arbolbbb:
    def __contains__(self,clave):
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False
    
    #Comprobación del árbol tras la eliminación de un nodo
    def comprobarBorrado(self,n,hijoIzq):
        x = n
        es_Izq = not hijoIzq
        Fin = False
        while Fin == False and x != None:
            if es_Izq: #Arbol derecho ha decrecido
                x.factorEquilibrio += 1
                if x.factorEquilibrio == 2:
                    if x.Izq.factorEquilibrio == -1:
                        #self.rotarIzquierda(x.Izq)
                        #self.rotarDerecha(x)
                        #Doble rotacion a la derecha
                        self.rotacion_doble_neg(x)
                    else:
                        #self.rotarDerecha(x)
                        #Rotacion simple a la derecha
                        self.rotacion_simple_neg(x)
                    if x.Der.factorEquilibrio == 0:
                        Fin = True
                    else:
                        if x.padre:
                            es_Izq = x.padre.Izq != x
                        x = x.padre
                    #if x.padre != None:
                    #    if x.padre.padre != None:
                    #        es_Izq = x.padre.padre.Izq != x.padre
                    #        x = x.padre.padre
                    #    else:
                    #        Fin = True
                    #else:
                    #    Fin = True
                elif x.factorEquilibrio == 1:
                    Fin = True
                else: #x.factorEquilibrio = 0
                    if x.padre != None:
                        es_Izq = x.padre.Izq != x
                    x = x.padre
            else: #Arbol izquierdo ha decrecido
                x.factorEquilibrio -= 1
                if x.factorEquilibrio == -2:
                    if x.Der.factorEquilibrio == 1:
                        #self.rotarDerecha(x.Der)
                        #self.rotarIzquierda(x)
                        #doble rotacion a la izquierda
                        self.rotacion_doble_pos(x)
                    else:
                        #self.rotarIzquierda(x)
                        #Rotacion simple a la izquierda
                        self.rotacion_simple_pos(x)
                    if x.Der.factorEquilibrio == 0:
                        Fin = True
                    else:
                        if x.padre:
                            es_Izq = x.padre.Izq != x
                        x= x.padre
                    #if x.padre != None:
                    #    if x.padre.padre != None:
                    #        es_Izq = x.padre.padre.Izq != x.padre
                    #        x = x.padre.padre
                    #    else:
                    #        Fin = True
                    #else:
                    #    Fin = True
                elif x.factorEquilibrio == -1:
                    Fin = True
                else: #x.factorEquilibrio = 0, continuar
                    if x.padre != None:
                        es_Izq = x.padre.Izq != x
                    x = x.padre

    #Eliminación de un nodo por medio de su clave
    def quitar(self,clave) -> int:
        tamanoinicial = self.tamano
        if self.tamano >= 1:
         nodo = self._obtener(clave,self.raiz)
        if nodo:
            Fin = False
            while not Fin:
                if nodo.Izq == None or nodo.Der == None:
                    if nodo.Izq == None:
                        hijo = nodo.Der
                    else:
                        hijo = nodo.Izq
                    if nodo == self.raiz:
                        self.tamano = self.tamano-1
                        self.raiz = hijo
                        if self.tamano > 0:
                            self.raiz.padre = None
                    else:
                        if hijo != None:
                            hijo.padre = nodo.padre
                        if nodo.padre.Izq == nodo:
                            nodo.padre.Izq = hijo
                            es_hijo_izq = True
                        else:
                            nodo.padre.Der = hijo
                            es_hijo_izq = False
                        self.comprobarBorrado(nodo.padre, es_hijo_izq)
                        self.tamano = self.tamano-1
                    Fin = True
                else: #Caso dos hijos
                    hijo = nodo.Der.encontrarMin()
                    nodo.clave = hijo.clave
                    nodo = hijo
        if tamanoinicial == self.tamano:
            return 2
        else:
            return 0

    #Sobrecarga del operador del
    def __delitem__(self,clave):
       self.quitar(clave)

    #Crea nodos en la graficación de un árbol
    def crearnodos(self, arbol, f, dir):
        if arbol != None:
            strclave = str(arbol.clave)
            f.node(strclave, nohtml('<f0> |<f1> ' + strclave + '|<f2>'))
            if arbol.padre != None:
                if dir == 0:
                    f.edge(str(arbol.padre.clave)+':<f0>', str(arbol.clave)+':<f1>')
                else:
                    f.edge(str(arbol.padre.clave)+':<f2>', str(arbol.clave)+':<f1>')
            self.crearnodos(arbol.Izq, f, 0)
            self.crearnodos(arbol.Der, f, 1)

    #Crea un gráfico del árbol
    def armararbol(self, arbol, titulo, nombreArchivo):
        f = Digraph('arbol', filename=nombreArchivo,
                format="png", node_attr={'shape': 'record', 'height': '.1'})
        self.crearnodos(arbol, f, 0)
        f.attr(label=r'\n\n'+titulo)
        f.attr(fontsize='20')
        f.render()

    def fe(self, arbol):
        if arbol:
            self.fe(arbol.Izq)
            print("Clave = ", arbol.clave, "FE = ", arbol.factorEquilibrio)
            self.fe(arbol.Der)