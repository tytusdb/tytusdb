import os

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.keys = []
        self.child = []
        self.next = None
        self.leaf = True
    
    def insert(self, key):
        self.keys.append(key)
        if len(self.keys) > 1:
            self.keys.sort()

class BPlusTree:

    def __init__(self, degree):
        self.root = Node(None)
        self.degree = degree
        self.valuar = False
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.valuar = False
    
    def _insert(self, temp, key):
        if temp.leaf:
            temp.insert(key)
        else:
            found = False
            for i in range(0, len(temp.keys)):
                if key < temp.keys[i]:
                    found = True
                    self._insert(temp.child[i], key)
                    break
            if not found:
                self._insert(temp.child[len(temp.keys)], key)

        if len(temp.keys) == self.degree:
            if temp.parent == None:
                c = temp
                temp = Node(None)
                temp.insert(c.keys[int((self.degree-1)/2)])
                temp.child.append(Node(temp))
                temp.child.append(Node(temp))
                if self.valuar:
                    temp.child[0].keys = c.keys[0:int((self.degree-1)/2)]
                    temp.child[1].keys = c.keys[int((self.degree-1)/2)+1:]
                    # k = 0
                    for i in range(0,int((len(c.child))/2)):
                        c.child[i].parent = temp.child[0]
                        temp.child[0].child.append(c.child[i])
                    for i in range(int((len(c.child))/2), len(c.child)):
                        c.child[i].parent = temp.child[1]
                        temp.child[1].child.append(c.child[i])
                    temp.child[0].leaf = False
                    temp.child[1].leaf = False
                    self.valuar=False
                else:
                    temp.child[0].keys = c.keys[0:int((self.degree-1)/2)]
                    temp.child[1].keys = c.keys[int((self.degree-1)/2):]
                    if temp.leaf:
                        temp.child[0].next = temp.child[1]
                        temp.child[1].next = c.next
                temp.leaf = False
            else:
                n = 0
                ev = False
                if self.valuar:
                        n = 1
                        ev = True
                        self.valuar = False
                mkey = temp.keys[int((self.degree-1)/2)]
                temp.parent.insert(mkey)
                index = 0
                for index in range(0, len(temp.parent.keys)):
                    if temp.parent.keys[index] == mkey:
                        break
                temp.parent.child.append(Node(temp))
                if index+1 < len(temp.parent.child):
                    k = len(temp.parent.child)-1
                    while k > index:
                        temp.parent.child[k] = temp.parent.child[k-1]
                        k-=1
                self.valuar = True
                temp.parent.child[index+1] = Node(temp.parent)
                temp.parent.child[index+1].keys = temp.keys[int((self.degree-1)/2)+n:]
                keys = temp.keys
                child = temp.child
                if not ev:
                    temp.parent.child[index] = temp
                    temp.parent.child[index].keys = []
                else:
                    temp.parent.child[index] = Node(temp.parent)
                temp.parent.child[index].keys = keys[0:int((self.degree-1)/2)]
                if ev:
                    if len(child)>0:
                        temp.parent.child[index].leaf = False
                        temp.parent.child[index+1].leaf = False
                        for i in range(0, int((len(child))/2)):
                            child[i].parent = temp.parent.child[index]
                            temp.parent.child[index].child.append(child[i])
                        for i in range(int((len(child))/2), len(child)):
                            child[i].parent = temp.parent.child[index+1]
                            temp.parent.child[index+1].child.append(child[i])
                if  self.valuar and not ev:
                    temp.parent.child[index+1].next =temp.parent.child[index].next 
                    for i in range(0,len(temp.parent.child)-1):
                        temp.parent.child[i].next = temp.parent.child[i+1]
        return temp

    def graficar(self):
        f= open('archivo.dot', 'w',encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out"];')
        f.write('rankdir=TB;\n')
        f.write('node [shape = box];\n')
        f = self._graficar(f,self.root,'')
        lista = self._next('', self.root)
        print(lista)
        lista1 = self._rank('{rank=same;', self.root)
        f.write(lista)
        f.write(lista1)
        f.write('}')
        f.close()
        os.system('dot -Tpng archivo.dot -o salida.png')
        os.system('salida.png')
   
    def _graficar(self, f, temp, nombre):
        if temp:
            if nombre == '':
                nombre = "Nodo"+"".join(str(x) for x in temp.keys)
            f.write(nombre+' [ label = "'+",".join(str(x) for x in temp.keys if x)+'"];\n')
            for c in temp.child:
                if c:
                    if len(c.child)==0:
                        nombre2 = "NodoH"+"".join(str(x) for x in c.keys)
                    else:
                        nombre2 = "Nodo"+"".join(str(x) for x in c.keys)
                    f = self._graficar(f, c, nombre2)
                    f.write(nombre+'->'+ nombre2+';\n')
        return f

    def _next(self, f, temp):
        if temp:
            if len(temp.child)==0:
                nombre2 = "NodoH"+"".join(str(x) for x in temp.keys)
                if temp.next:
                    f+=nombre2+'->'
                    f = self._next(f, temp.next)
                else:
                    f+=nombre2+';\n'
            else:
                f = self._next(f, temp.child[0])
        return f
    
    def _rank(self, f, temp):
        if temp:
            if len(temp.child)==0:
                nombre2 = "NodoH"+"".join(str(x) for x in temp.keys)
                if temp.next:
                    f+=nombre2+';'
                    f = self._rank(f, temp.next)
                else:
                    f+=nombre2+'}\n'
            else:
                f = self._rank(f,temp.child[0])
        return f