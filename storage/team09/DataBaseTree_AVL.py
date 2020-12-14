
class DataBase:
    def __init__(self, value):
        self.value  = value
        self.tables={}
        self.left   = None
        self.right  = None
        self.height = 0   #altura 

     

class AVLTree:
    def __init__(self):
        self.root = None

    #add
        
    def add(self, value,lista):
        self.root = self._add(value, self.root,lista)
    
    def _add(self, value, tmp,lista):
        if tmp is None: # SI esta vacio la raiz solola devuelve
            tmp=DataBase(value)
            tmp.tables=lista
            return tmp      
        elif value>str(tmp.value):  # es mayor que la raiz
            #ingresa al nodo derecho del padre
            tmp.right=self._add((value), tmp.right,lista)
            #calcula la altura para nivelar
            if (self.height(tmp.right)-self.height(tmp.left))==2: # si es igual a 2 no esta equilibrado
                if value>tmp.right.value:
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.left=self._add(value, tmp.left,lista)
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

    #traversals

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, tmp):
        if tmp:
            print(tmp.value,end = ' ')
            self._preorder(tmp.left)            
            self._preorder(tmp.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tmp):
        if tmp:
            self._inorder(tmp.left)
            print(tmp.value,end = ' ')
            self._inorder(tmp.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tmp):
        if tmp:
            self._postorder(tmp.left)            
            self._postorder(tmp.right)
            print(tmp.value,end = ' ')
           
    def Eliminar(self,value):
        self.root=self._eliminar(value,self.root)
    

    def _eliminar(self, valor,nodo):

        if nodo is None:  # Si el nodo a eliminar no existe, terminar
            print('El nodo NO existe')
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
            print("digraph G { ")
            print('graph [ordering="out"];\n randkdir=TB;\nnode [shape=circule];')
            
            self._grafo(self.root)
            print("\n}")
            
    

    def _grafo(self,actual):
        if actual:
            print(str(actual.value)+'[ label ="'+str(actual.value)+'"];\n')
            self._grafo(actual.left)
            self._grafo( actual.right )
            if actual.left:
                print(str(actual.value)+"->"+str(actual.left.value)+";\n")
            if actual.right:
                print(str(actual.value)+"->"+str(actual.right.value)+";\n")
        
    def modicar(self,name,NewName):
        nodo=DataBase(NewName)
        nodo.tables=self.bus(name)
        
        self.Eliminar(name)
        
        nodo=self.add(nodo.value,nodo.tables)
        
        
            

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

    def _imprimir(self,actual):
        if actual:
            
            self._imprimir(actual.left)
            self._imprimir( actual.right )
            if actual.left:
                print(str(actual.value)+"->"+ str(actual.tables)+";\n")
            if actual.right:
                print(str(actual.value)+"->"+str(actual.tables)+";\n")
    def imprimir(self):
        self._imprimir(self.root)
#init
t = AVLTree()

#add
diccionario1={1:"hola ",2:"como ",3:"estas?"}
diccionario2={1:"bien ",2:" y ",3:" tu ?"}
diccionario3={1:" Me ",2:" llamo ",3:" mynor"}

t.add("base1",diccionario1)
t.add("base2",diccionario2)
t.add("base3",diccionario3)
t.add("base4",diccionario1)
t.add("base5",diccionario2)
t.add("base6",diccionario3)
t.add("base7",diccionario1)
t.add("base8",diccionario1)
t.add("base9",diccionario1)
t.add("base10",diccionario2)
t.add("base11",diccionario3)
t.add("base12",diccionario3)
t.add("base13",diccionario2)
t.add("base14",diccionario2)
t.grafo()
#print traversals
#t.preorder()

#t.Eliminar("base4")
#t.add("1005")
t.modicar("base4","hola32")
t.add("hola5000",diccionario1)
t.Eliminar("base1")
t.imprimir()

t.grafo()
