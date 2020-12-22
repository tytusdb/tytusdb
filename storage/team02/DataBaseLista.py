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


