from .Tables import Tables
#import ISAM.BinWriter as b
from .ISAM import BinWriter as b
import os
import pickle
from PIL import Image

class DataBase:
    def __init__(self, value):
        self.value  = value
        self.tables= Tables(value)
        self.left   = None
        self.right  = None
        self.height = 0   #altura 

     

class AVLTree:
    def __init__(self):
        self.root = None
        self.arr=[]
        self.eliminados=[]
        self.load()

    def load(self):
        if os.path.exists("data/databases/Bases.b"):
            var=b.read("data/databases/Bases.b")
            for i in var:
                self.add(i)
        
    def writer(self):
        b.write(self.arr,"data/databases/Bases.b")


    def add(self, value):
        self.root = self._add(value, self.root)
        self.arr.append(value)
        self.writer()
        
    
    def _add(self, value, tmp):
        if tmp is None: # SI esta vacio la raiz solola devuelve
            tmp=DataBase(value)
            return tmp      
        elif value>str(tmp.value):  # es mayor que la raiz
            #ingresa al nodo derecho del padre
            tmp.right=self._add((value), tmp.right)
            #calcula la altura para nivelar
            if (self.height(tmp.right)-self.height(tmp.left))==2: # si es igual a 2 no esta equilibrado
                if value>tmp.right.value:
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.left=self._add(value, tmp.left)
            if (self.height(tmp.left)-self.height(tmp.right))==2:
                if value<str(tmp.left.value):
                    tmp = self.srl(tmp)
                else:
                    tmp = self.drl(tmp)
        r = self.height(tmp.right)
        l = self.height(tmp.left)
        m = self.maxi(r, l)
        tmp.height = m+1
        return tmp

    def height(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.height
        
    def maxi(self, r, l):
        return (l,r)[r>l]   

    #rotations

    def srl(self, t1):
        t2 = t1.left
        t1.left = t2.right
        t2.right = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2

    def srr(self, t1):
        t2 = t1.right
        t1.right = t2.left
        t2.left = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2
    
    def drl(self, tmp):
        tmp.left = self.srr(tmp.left)
        return self.srl(tmp)
    
    def drr(self, tmp):
        tmp.right = self.srl(tmp.right)
        return self.srr(tmp)

           
    def Eliminar(self,value):
        self.root=self._eliminar(value,self.root)
        self.arr.remove(value)
        self.writer()
        

    def _eliminar(self, valor,nodo):

        if nodo is None:  # Si el nodo a eliminar no existe, terminar
            return nodo
        elif valor < str(nodo.value):  # El valor a eliminar es menor 
            nodo.left= self._eliminar(valor,nodo.left)
        elif valor > str(nodo.value):  # El valor a eliminar es mayor 
            nodo.right = self._eliminar(valor,nodo.right)
        else:  # Ya encontré el nodo
            if nodo.left is None:  # El hijo izquierdo no existe, no es posible buscar por la izquierda
                nodo_mas_derecho = nodo.right
                raiz = None
                return nodo_mas_derecho
            elif nodo.right is None:  # El hijo derecho no existe, se toma el hijo izquierdo
                nodo_mas_derecho = nodo.left
                raiz = None
                return nodo_mas_derecho

            # Buscando el nodo con el dato
            nodo_mas_derecho = self.nodo_mas_derecho(nodo.left)
            nodo.value = nodo_mas_derecho.value

            nodo.left = self._eliminar(nodo_mas_derecho.value,nodo.left)


        return self.balanceo(nodo)

    def balanceo(self,x):
        #envia el factor para obtener los niveles
        if self.factor(x)>1:
            if self.factor(x.right)<0:
                x.right= self.srr(x.right)
            x=self.srl(x)
        elif self.factor(x)<-1:
            if self.factor(x.left)>0:
                x.left= self.srl(x.left)
            x=self.srr(x)

        return x


    # NODO MÁS LA DERECHA
    def nodo_mas_derecho(self, n):
        while True:
            if n is None or n.right is None:
                break
            else:
                n = n.right
        return n

    # FACTOR DE EQUILIBRIO
    def factor(self, nodo):
        if not nodo:
            return 0
        return self.height(nodo.left) - self.height(nodo.right)

  

    def grafo(self):
        if self.root !=None:
            g=open("grafo.dot","w")
            g.write("digraph G { ")
            g.write('graph [ordering="out"];\n randkdir=TB;\nnode [shape=circule];')
            
            g=self._grafo(g,self.root)
            g.write("\n}")
            g.close()
            os.system('dot -Tpng grafo.dot -o AvlData.png')
            os.system('AvlData.png')
            img=Image.open("AvlData.png")
            img.show()
    

    def _grafo(self,f,actual):
        if actual:
            f.write(str(actual.value)+'[ label ="'+str(actual.value)+'"];\n')
            self._grafo(f,actual.left)
            self._grafo( f,actual.right )
            if actual.left:
                f.write(str(actual.value)+"->"+str(actual.left.value)+";\n")
            if actual.right:
                f.write(str(actual.value)+"->"+str(actual.right.value)+";\n")
        
        return f


    def modicar(self,name,NewName):
        nodo=DataBase(NewName)
        nodo.tables=self.bus(name)
  #      self.modwrite(name)
        self.Eliminar(name)
        
        nodo=self.add(nodo.value)
        
        
            

    def bus(self,valor):
        temp=self.root
        while temp is not None:
            if valor == temp.value:
                return temp.tables
            elif valor > str(temp.value):
                temp = temp.right
            elif valor < str(temp.value):
                temp = temp.left
        return None

    
    def imprimir(self):
        
        if len(self.eliminados)!=0:
            for i in self.eliminados:
                for j in self.arr:
                    if i==j:
                        self.arr.remove(i)
        
        return self.arr

    def verificar(self,valor):
        band=False
        temp=self.root
        while temp is not None:
            if valor == temp:
                return 
            elif valor > str(temp.value):
                temp = temp.right
            elif valor < str(temp.value):
                temp = temp.left

        return band
    
d=AVLTree()

print(d.imprimir())
