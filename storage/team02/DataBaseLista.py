import os

class Nodo:
    def __init__(self, nombreBase):
        self.nombreBase = nombreBase
        self.tabla = None
        self.siguiente = None
        self.anterior = None
        
class ListaDOBLE:
    def __init__(self):
        self.primero = None
        self.ultimo = None
         
    #Método que verifica si la lista esta vacía
    def listaVacia(self):
        if self.primero is None:
            return True
        else:
            return False

    #Método agregar MÉTODO FUNCIONAL PARA ENVIAR
    def agregarLista(self, nombreBase):
        nuevoNodo = Nodo(nombreBase)
        try:
            if type(nombreBase) != int:
                if self.listaVacia() is True:
                    self.primero = nuevoNodo
                    self.ultimo = nuevoNodo
                    return 0
                else:
                    if self.buscarNodo(nombreBase) == 0:
                        if self.primero != None:
                            self.ultimo.siguiente = nuevoNodo
                            nuevoNodo.anterior = self.ultimo
                            self.ultimo = nuevoNodo
                        else:
                            self.primero = nuevoNodo
                            self.ultimo = nuevoNodo
                        return 0
                    elif self.buscarModificar(nombreBase) == 2:
                        return 2
                    else:
                        return 1
            else:
                return 1
        except:
            return 1


	#Método Buscar para lista de tablas
    def buscarNodo(self, dato):
        actual = self.primero
        encontrado = False
        if self.primero != None:
            while actual != None and encontrado != True:
                if actual.nombreBase == dato:
                    encontrado = True
                    return actual
                actual = actual.siguiente
            if not encontrado:
                return 0
        else:    
            return 1  

    #buscar para agregar y modificar
    def buscarModificar(self, dato):
        actual = self.primero
        encontrado = False
        if self.primero != None:
            while actual != None and encontrado != True:
                if actual.nombreBase == dato:
                    encontrado = True
                    return 2
                actual = actual.siguiente
            if not encontrado:
                return 0
        else:    
            return 1   

    #Método Eliminar MÉTODO FUNCIONAL PARA ENVIAR
    def eliminarNodo(self, dato):
        aux = self.primero
        tmp = None
        encontrado = False
        try:
            if self.listaVacia() is True:
                return 1
            else:
                if self.primero != None:
                    while aux != None and encontrado != True:
                        if aux.nombreBase == dato:
                            if aux == self.primero:
                                self.primero = self.primero.siguiente
                                self.primero.anterior = None
                            elif aux == self.ultimo:
                                tmp.siguiente = None
                                self.ultimo = tmp
                            else:
                                tmp.siguiente = aux.siguiente
                                aux.siguiente.anterior = tmp
                            encontrado = True
                            return 0
                        tmp = aux
                        aux = aux.siguiente
                    if not encontrado:
                        return 2
        except:
            return 1

    #Método Modificar MÉTODO FUNCIONAL PARA ENVIAR
    def modificarNodo(self, nombreActual, nuevoNombre):
        try:
            if self.buscarModificar(nuevoNombre) == 2:
                return 3
            else:
                actual = self.primero
                encontrado = False
                if self.primero != None:
                    while actual != None and encontrado != True:
                        if actual.nombreBase == nombreActual:
                            encontrado = True
                            actual.nombreBase = nuevoNombre
                            return 0
                        actual = actual.siguiente
                    if not encontrado:
                        return 2
                else:
                    return 1
        except:
            return 1
        
    #Método imprimir MÉTODO FUNCIONAL PARA ENVIAR
    def imprimir(self):
        lista = []
        tmp = self.primero
        while tmp != None:
            lista.append(tmp.nombreBase)
            tmp = tmp.siguiente
        return lista

    #MÉTODO GRAFICAR SIN LIBRERIAS DE GRAPHVIZ
    def GraficarConArchivo(self):
        f = open("listaDoble.dot", "w")
        f.write("digraph g {\n")
        f.write("node [shape = rect, width=1, height=0.4];\n")     
        f.write("rankdir=LR;\n")

        tmp = self.primero
        while tmp.siguiente != None:
            f.write("\""+str(tmp.nombreBase)+"\"->"+"\""+str(tmp.siguiente.nombreBase)+"\";\n")
            tmp = tmp.siguiente
        aux = self.ultimo
        while aux.anterior != None:
            f.write("\""+str(aux.nombreBase)+"\"->"+"\""+str(aux.anterior.nombreBase)+"\";\n")
            aux = aux.anterior
        f.write("}")
        f.close()
        os.system("dot -Tjpg listaDoble.dot -o listaDoble.png")
        os.system("listaDoble.png")