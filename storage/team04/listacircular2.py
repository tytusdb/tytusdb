class Node(object):
    def __init__(self, data):
        self.dato=data
        self.siguiente=None

class CrearListaCircular(object):
    def __init__(self):
        self.head=None

    #Metodo para averiguar si la lista está vacía o no
    def esta_vacia(self):
        return (self.head is None)
    
    #Método para saber el largo de la lista
    def largo(self):
        aux=self.head
        contador=0
        while aux is not None:
            contador+=1
            if aux.next==self.head:
                break
            else:
                aux=aux.next
        return contador
    
    #Método para agregar al inicio (parecido a una pila)
    def agregar(self,dato):
        node=Node(dato)
        if self.esta_vacia():
            self.head=node
            node.next=self.head
        else:
            aux=self.head
            while aux.next is not self.head:
                aux=aux.next
            aux.next=node
            node.next=self.head
            self.head=node

    #Metodo para editar un nodo especifico
    def editar_nodo(self,dato):
        aux=self.head
        while aux is not None:
            if aux.dato==dato:
                print("Ingrese el nuevo valor del dato:")
                nuevodato=input()
                self.eliminar_nodo(dato)
                self.agregar(nuevodato)
                aux=aux.next
            elif aux.next==self.head:
                return print("Nodo no existe")
            else:
                aux=aux.next

    #Metodo para mostrar todo lo que esta en la lista por medio de la consola
    def recorrer_nodo(self):
        if self.esta_vacia():
            return
        aux=self.head
        print(aux.dato)
        while aux.next!=self.head:
            aux=aux.next
            print(aux.dato)

    #Metodo que elimina un nodo de la lista
    def eliminar_nodo(self,dato):
        if self.esta_vacia():
            return
        elif dato==self.head.dato:
            aux=self.head
            while aux.next!=self.head:
                aux=aux.next
            aux.next=self.head.next
            self.head=self.head.next
        else:
            aux=self.head
            pre=None
            while aux.dato!=dato:
                pre=aux
                aux=aux.next
            pre.next=aux.next
    
    
    