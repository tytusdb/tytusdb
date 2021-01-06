
import os
from BTree import *

class nodo :
    def __init__(self,nombreDeLaTabla,numeroDeColumnasDeLaTabla) :
        self.nombre = nombreDeLaTabla
        self.columnas = numeroDeColumnasDeLaTabla
        self.elementosAB = BTree()
        self.siguiente = None
        self.anterior = None
        
class ListaDobledeArboles :
    def __init__ (self) :
        self.inicio = None
        self.fin = None
    
    #Metodo para saber si la lista esta vacia
    def estaVacia(self) :
        return self.inicio is None

    #Metodo para buscar una tabla
    def buscar(self,nombreTabla) :
        aux = self.inicio
        while aux != None :
            if aux.nombre == nombreTabla :
                #print("La tabla existe")
                return aux
            aux = aux.siguiente
        #print("La tabla no existe")
        return None

    #Metodo para listar los nodos
    def verNodos(self) :
        tablas = []
        aux = self.inicio
        while aux != None :
            tablas.append(aux.nombre)
            aux = aux.siguiente
        return tablas 

    def insertar(self,nombreTabla,numCol) :
        nuevo = nodo(nombreTabla,numCol)
        # lista vacia
        if self.inicio == None :
            self.inicio=self.fin=nuevo
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin
            self.fin = nuevo
        return self.inicio

    def eliminar(self,nombreTabla) :
        if self.estaVacia() != None :
            aux = self.inicio
            while aux != None :
                if aux.nombre == nombreTabla :
                    if aux.anterior == None and aux.siguiente == None :
                        self.inicio=self.fin=None
                        return 0
                    #en el original no tenias los elif
                    elif aux.anterior == None :
                        self.inicio = self.inicio.siguiente
                        self.inicio.anterior = None
                        aux.siguiente = None
                        return 0
                    elif aux.siguiente == None :
                        self.fin = self.fin.anterior
                        self.fin.siguiente = None
                        aux.anterior = None
                        return 0
                    else:
                        aux.anterior.siguiente = aux.siguiente
                        aux.siguiente.anterior = aux.anterior
                        aux.anterior = None
                        aux.siguiente = None
                        return 0
                else:
                    aux = aux.siguiente
        else:
            #return("BD vacia")
            return(4)

    def modificar(self,nombreViejo,nombreNuevo):
        aux = self.inicio
        while aux != None :
            if aux.nombre == nombreViejo :
                aux.nombre = nombreNuevo
                return 0
            aux = aux.siguiente

    def graficar(self):
        f = open("listadoble.dot", "w")            
        f.write("digraph G {\n")
        f.write("node [shape = rect, width=1, height=0.4];\n")     
        f.write("rankdir=LR;\n")  
        
        n=self.inicio
        while (n.siguiente!=None):
            #la linea siguiente es para mostrar el nombre de la tabla por separadao, por el momento no es necesario
            #f.write(str(n.nombre)+"[label="+"\""+str.(n.nombre)+"\""+"];")
            f.write("\""+str(n.nombre)+"\"->"+"\""+str(n.siguiente.nombre)+"\";\n")
            f.write("\n")
            n=n.siguiente

        n=self.fin
        while n.anterior!=None :
            f.write("\""+str(n.nombre)+"\"->"+"\""+str(n.anterior.nombre)+"\";\n")
            f.write("\n")
            n=n.anterior

        f.write("}")
        f.close()
        os.system("dot -Tjpg listadoble.dot -o listadoble.png")