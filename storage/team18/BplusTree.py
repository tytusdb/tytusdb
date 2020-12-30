# B+ Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import os

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.keys = []
        self.values = {}
        self.child = []
        self.next = None
        self.leaf = True

    def insert(self, key, value):
        self.keys.append(key)
        if value:
            self.values[key] = value
            self.values = dict(sorted(self.values.items()))
        if len(self.keys) > 1:
            self.keys.sort()

class BPlusTree:

    def __init__(self, degree = 5, columns = 0, direction=''):
        self.root = Node(None)
        self.degree = degree
        self.valuar = False
        self.PKey = []
        self.Fkey = []
        self.Incremet = 1
        self.dropPK = False
        self.columns = columns
        self.direction = direction

    def insert(self, key, value):
        self.root = self._insert(self.root, str(key), value)
        self.valuar = False
    
    def _insert(self, temp, key, value):
        if temp.leaf:
            if key not in temp.keys:
                temp.insert(key, value)
            else:
                return temp
        else:
            found = False
            for i in range(0, len(temp.keys)):
                if key < temp.keys[i]:
                    found = True
                    self._insert(temp.child[i], key, value)
                    break
            if not found:
                self._insert(temp.child[len(temp.keys)], key, value)

        if len(temp.keys) == self.degree:
            if temp.parent == None:
                c = temp
                temp = Node(None)
                temp.insert(c.keys[int((self.degree)/2)], None)
                temp.child.append(Node(temp))
                temp.child.append(Node(temp))
                if self.valuar:
                    temp.child[0].keys = c.keys[0:int((self.degree)/2)]
                    temp.child[1].keys = c.keys[int((self.degree)/2)+1:]
                    # k = 0
                    if self.degree%2 == 0:
                        ii = int((len(c.child))/2)+1
                    else:
                        ii = int((len(c.child))/2)
                    for i in range(0,ii):
                        c.child[i].parent = temp.child[0]
                        temp.child[0].child.append(c.child[i])
                    for i in range(ii, len(c.child)):
                        c.child[i].parent = temp.child[1]
                        temp.child[1].child.append(c.child[i])
                    temp.child[0].leaf = False
                    temp.child[1].leaf = False
                    self.valuar=False
                else:
                    temp.child[0].keys = c.keys[0:int((self.degree)/2)]
                    temp.child[1].keys = c.keys[int((self.degree)/2):]
                    if temp.leaf:
                        temp.child[0].next = temp.child[1]
                        temp.child[1].next = c.next
                if len(c.values):
                    for x in temp.child[1].keys:
                        temp.child[1].values[x] = c.values.get(x)
                    for x in temp.child[0].keys:
                        temp.child[0].values[x] = c.values.get(x)
                    temp.child[1].values = dict(sorted(temp.child[1].values.items()))
                    temp.child[0].values = dict(sorted(temp.child[0].values.items()))
                temp.leaf = False
            else:
                n = 0
                ev = False
                v = temp.values
                if self.valuar:
                        n = 1
                        ev = True
                        self.valuar = False
                mkey = temp.keys[int((self.degree)/2)]
                temp.parent.insert(str(mkey), None)
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
                temp.parent.child[index+1].keys = temp.keys[int((self.degree)/2)+n:]
                keys = temp.keys
                child = temp.child
                if not ev:
                    temp.parent.child[index] = temp
                    temp.parent.child[index].keys = []
                else:
                    temp.parent.child[index] = Node(temp.parent)
                temp.parent.child[index].keys = keys[0:int((self.degree)/2)]
                
                if ev:
                    if len(child)>0:
                        if self.degree%2 == 0:
                            ii = int((len(child))/2)+1
                        else:
                            ii = int((len(child))/2)
                        temp.parent.child[index].leaf = False
                        temp.parent.child[index+1].leaf = False
                        for i in range(0, ii):
                            child[i].parent = temp.parent.child[index]
                            temp.parent.child[index].child.append(child[i])
                        for i in range(ii, len(child)):
                            child[i].parent = temp.parent.child[index+1]
                            temp.parent.child[index+1].child.append(child[i])
                else:
                    if len(temp.values):
                        temp.parent.child[index+1].values = {}
                        temp.parent.child[index].values = {}
                        for x in temp.parent.child[index+1].keys:
                            temp.parent.child[index+1].values[x] = v.get(x)
                        temp.parent.child[index+1].values = dict(sorted(temp.parent.child[index+1].values.items()))
                        for x in temp.parent.child[index].keys:
                            temp.parent.child[index].values[x] = v.get(x)
                        temp.parent.child[index].values = dict(sorted(temp.parent.child[index].values.items()))
                if  self.valuar and not ev:
                    temp.parent.child[index+1].next =temp.parent.child[index].next 
                    for i in range(0,len(temp.parent.child)-1):
                        temp.parent.child[i].next = temp.parent.child[i+1]
        return temp

    def delete(self, keys):
        val = "_".join(str(x) for x in keys)
        self.root = self._delete(self.root, val, None)
    
    def _delete(self, temp, key, copy):
        found = False
        if temp == self.root and not temp.child:
            if len(temp.keys)==1:
                temp = Node(None)
            else:
                temp.keys.remove(key)
                del temp.values[key]
            return temp
        if temp.child:
            for i in range(0, len(temp.keys)):
                if key in temp.keys:
                    copy = temp
                if key < temp.keys[i]:
                    found = True
                    self._delete(temp.child[i], key, copy)
                    temp = self.rotation(temp)
                    break
        if not found:
            if temp.child:
                self._delete(temp.child[len(temp.keys)], key, copy)
                temp = self.rotation(temp)
            else:
                if key not in temp.keys:
                    return False
                temp.keys.remove(key)
                del temp.values[key]
                if copy:
                    copy.keys.remove(key)
                    if len(temp.keys)!=0:
                        copy.insert(temp.keys[0], None)
                    elif temp.next:
                        if self.degree>4:
                            copy.insert(temp.next.keys[0], None)
                        else:
                            if copy!=temp.parent:
                                copy.insert(temp.next.keys[0], None)
                temp = self.rotation(temp)
        return temp

    #---------Rotaciones---------------#
    def rotation(self, temp):   
        if not len(temp.keys) and temp.parent:
            index = temp.parent.child.index(temp)
            if index== len(temp.parent.child)-1:
                if len(temp.keys)==0 and len(temp.parent.keys)==0:
                    if len(temp.parent.child[index-1].keys)>1:
                        temp = self.MoverIzquierda(temp,index)
                    else:
                        temp = self.UnirIzquierda(temp,index)
                else:
                    if len(temp.parent.child[index-1].keys) >1 and len(temp.parent.keys) >= 1 and len(temp.parent.child) == self.degree:
                        temp = self.MoverIzquierda(temp,index)
                    else:
                        if len(temp.parent.child[index-1].child) == self.degree:
                            temp = self.CambioRaizI(temp, index)
                        else:
                            temp = self.UnirIzquierdaRaiz(temp,index)
            elif not index:
                if len(temp.keys)==0 and len(temp.parent.keys)==0:
                    temp = self.UnirDerecha(temp,index)
                else:
                    if len(temp.parent.child[index+1].keys) >1 and len(temp.parent.keys) >= 1 and len(temp.parent.child) == len(temp.parent.keys)+1:
                        temp = self.MoverDerecha(temp,index)
                    else:
                        if len(temp.parent.child[index-1].child) == self.degree:
                            temp = self.CambioRaizI(temp, index)
                        else:
                            temp = self.UnirDerechaRaiz(temp, index)
                
            else:
                izquierda = len(temp.parent.child[index-1].keys)
                derecha = len(temp.parent.child[index+1].keys)
                if izquierda ==1 and len(temp.parent.keys)>0 and izquierda>=derecha:
                    temp = self.UnirIzquierda(temp,index)
                elif derecha ==1 and len(temp.parent.keys)>0 and derecha>izquierda:
                    temp = self.UnirDerecha(temp, index)
                elif izquierda>=derecha:
                    if len(temp.parent.child[index-1].child) == self.degree:
                        temp = self.CambioRaizI(temp, index)
                    else:
                        temp = self.MoverIzquierda(temp, index)
                elif derecha> izquierda:
                    if len(temp.parent.child[index+1].child) == self.degree:
                        print("Caso especial")
                    else:
                        temp = self.MoverDerecha(temp,index)
        elif temp.parent:
            index = temp.parent.child.index(temp)
            derecha = 0
            actual = len(temp.keys)
            izquierda = 0
            if index == len(temp.parent.child)-1:
                izquierda = len(temp.parent.child[index-1].keys)
                if izquierda+actual >= self.degree-1 and actual+1 != izquierda and actual<izquierda:
                    temp = self.MoverIzquierda(temp,index)
                elif izquierda+actual < self.degree-1 and actual<izquierda:
                    temp = self.UnirIzquierda(temp,index)
            elif not index:
                derecha = len(temp.parent.child[index+1].keys)
                if derecha+actual >= self.degree-1 and actual+1 != derecha and derecha>actual:
                    temp = self.MoverDerecha(temp,index)
                elif derecha+actual < self.degree-1 and actual<derecha:
                    temp = self.UnirDerecha(temp,index)
            else:
                izquierda = len(temp.parent.child[index-1].keys)
                derecha = len(temp.parent.child[index+1].keys)
                if izquierda+actual >= self.degree-1 and actual+1 != izquierda and izquierda>actual:
                    temp = self.MoverIzquierda(temp,index)
                elif derecha+actual >= self.degree-1 and actual+1 != derecha and actual<derecha and derecha>izquierda:
                    temp = self.MoverDerecha(temp,index)
                elif izquierda+actual < self.degree-1 and actual< izquierda:
                    if len(temp.parent.child[index-1].child) == self.degree:
                        temp = self.CambioRaizI(temp, index)
                    else:
                        temp = self.UnirIzquierda(temp,index)
                elif derecha+actual < self.degree-1 and actual<derecha and derecha>izquierda:
                    if len(temp.parent.child[index+1].child) == self.degree:
                        print("Caso especial")
                    else:
                        temp = self.UnirDerecha(temp,index)
        else:
            if len(temp.child)==1:
                if len(temp.keys)==1:
                    temp.child[0].insert(temp.keys[0])
                temp = temp.child[0]
                temp.parent = None
    
        return temp

    def CambioRaizI(self, temp, index):
        temp.parent.keys.remove(temp.parent.keys[index-1])
        temp.insert(temp.child[0].keys[0], None)
        val = temp.parent.child[index-1].keys[len(temp.parent.child[index-1].keys)-1]
        temp.parent.insert(val, None)
        temp.parent.child[index-1].keys.remove(val)
        hijo = temp.parent.child[index-1].child[len(temp.parent.child[index-1].child)-1]
        temp.parent.child[index-1].child.remove(hijo)
        hijo.parent = temp
        temp.child.insert(0,hijo)
        return temp

    def UnirDerechaRaiz(self, temp, index):
        temp.keys = temp.parent.child[index+1].keys
        val = temp.parent.keys[0]
        if val not in temp.keys:
            temp.insert(val, temp.parent.values.get(val))
            if temp.parent.values.get(val):
                del temp.parent.values[val]
        temp.parent.keys.remove(val)
        for x in temp.parent.child[index+1].child:
            x.parent = temp
            temp.child.append(x)
        temp.next = temp.parent.child[index+1].next
        temp.values.update(temp.parent.child[index+1].values)
        temp.values = dict(sorted(temp.values.items()))
        temp.parent.child.remove(temp.parent.child[index+1])
        return temp

    def UnirIzquierdaRaiz(self, temp, index):
        val = temp.parent.keys[len(temp.parent.keys)-1]
        if val not in temp.parent.child[index-1].keys:
            temp.parent.child[index-1].insert(val, temp.parent.values.get(val))
            if temp.parent.values.get(val):
                del temp.parent.values[val]
            temp.parent.keys.remove(val)
        elif len(temp.parent.keys)>1:
            temp.parent.keys.remove(val)
        for x in temp.child:
            x.parent = temp.parent.child[index-1]
            temp.parent.child[index-1].child.append(x)
        temp.parent.child[index-1].next = temp.next
        temp.parent.child[index-1].values.update(temp.values)
        temp.parent.child[index-1].values = dict(sorted(temp.parent.child[index-1].values.items()))
        temp.parent.child.remove(temp)
        return temp

    def UnirIzquierda(self, temp, index):
        for x in temp.keys:
            temp.parent.child[index-1].insert(x, temp.values.get(x))
            if temp.values.get(x):
               del temp.values[x]
        for x in temp.child:
            x.parent = temp.parent.child[index-1]
            temp.parent.child[index-1].child.append(x)
        temp.parent.child[index-1].next = temp.next
        temp.parent.child.remove(temp)
        if len(temp.child):
            temp.parent.child[index-1].insert(temp.parent.keys.pop(index-1), None)
        else:
            temp.parent.keys.pop(index-1)
        if len(temp.child)==1:
            if temp.child[0].keys[0] in temp.parent.keys:
                temp.parent.keys.remove(temp.child[0].keys[0])
                temp.parent.child[index-1].insert(temp.child[0].keys[0], None)
        if not len(temp.child):
            temp = self.ReorganizarKeys(temp)
        return temp
    
    def UnirDerecha(self, temp, index):
        for x in temp.parent.child[index+1].keys:
            temp.insert(x, temp.parent.child[index+1].values.get(x))
            if temp.parent.child[index+1].values.get(x):
                del temp.parent.child[index+1].values[x]
        for x in temp.parent.child[index+1].child:
            x.parent = temp
            temp.child.append(x)
        if len(temp.child):
            temp.insert(temp.parent.keys.pop(index), None)
        else:
            temp.parent.keys.pop(index)
        temp.next = temp.parent.child[index+1].next
        temp.parent.child.remove(temp.parent.child[index+1])
        if not len(temp.child):
            temp = self.ReorganizarKeys(temp)
        return temp
    
    def MoverDerecha(self, temp, index):
        if not len(temp.child):
            val = temp.parent.child[index+1].keys[0]
            temp.insert(val, temp.parent.child[index+1].values.get(val))
            if temp.parent.child[index+1].values.get(val):
                del temp.parent.child[index+1].values[val]
            temp.parent.child[index+1].keys.remove(val)
        else:
            val = temp.parent.keys.pop(index)
            temp.insert(val, None)
            temp.parent.insert(temp.parent.child[index+1].keys.pop(0), None)
        if temp.child and self.degree<5  or len(temp.child)==len(temp.keys):
            hijo = temp.parent.child[index+1].child[0]
            temp.child.append(hijo)
            temp.parent.child[index+1].child.remove(hijo)
            hijo.parent = temp
        if not len(temp.child):
            temp = self.ReorganizarKeys(temp)
        return temp

    def MoverIzquierda(self, temp, index):
        if not len(temp.child):
            val = temp.parent.child[index-1].keys[len(temp.parent.child[index-1].keys)-1]
            temp.insert(val, temp.parent.child[index-1].values.get(val))
            if temp.parent.child[index-1].values.get(val):
                del temp.parent.child[index-1].values[val]
            temp.parent.child[index-1].keys.remove(val)
        else:
            val = temp.parent.keys.pop(index-1)
            temp.insert(val, None)
            temp.parent.insert(temp.parent.child[index-1].keys.pop(-1), None)
        if temp.child and self.degree<5  or len(temp.child)==len(temp.keys):
            hijo = temp.parent.child[index-1].child[len(temp.parent.child[index-1].child)-1]
            temp.child.insert(0,hijo)
            temp.parent.child[index-1].child.remove(hijo)
            hijo.parent = temp
        if not len(temp.child):
            temp = self.ReorganizarKeys(temp)
        return temp

    def ReorganizarKeys(self, temp):
        temp.parent.keys = []
        for g in range(1,len(temp.parent.child)):
            temp.parent.insert(temp.parent.child[g].keys[0], None)
        return temp
    
    def ReorganizarKeysHijo(self, temp):
        temp.keys = []
        for g in range(1,len(temp.child)):
            temp.insert(temp.child[g].keys[0], None)
        return temp
    #---------Graficar-----------------#
    def graficar(self, database, table):
        f= open(f'Data/BPlusMode/{database}/{table}/{table}.dot', 'w',encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out"];')
        f.write('rankdir=TB;\n')
        f.write('node [shape = box];\n')
        f = self._graficar(f,self.root,'')
        lista = self._next('', self.root)
        lista1 = self._rank('{rank=same;', self.root)
        if lista!='':
            f.write(lista)
        if lista1!= '{rank=same;':
            f.write(lista1)
        f.write('}')
        f.close()
        os.system(f'dot -Tpng Data/BPlusMode/{database}/{table}/{table}.dot -o ./Data/BPlusMode/{database}/{table}/{table}.png')
    
    def _graficar(self, f, temp, nombre):
        if temp:
            if nombre == '':
                nombre = "Nodo"+"D".join(str(x).replace(" ","") for x in temp.keys)
            valor = "   |   ".join("".join(str(x)) for x in temp.keys)
            f.write(nombre+' [ label = "'+valor+'"];\n')
            for c in temp.child:
                if c:
                    if len(c.child)==0:
                        nombre2 = "NodoH"+"D".join(str(x).replace(" ","")  for x in c.keys)
                    else:
                        nombre2 = "Nodo"+"D".join(str(x).replace(" ","")  for x in c.keys)
                    f = self._graficar(f, c, nombre2)
                    f.write(nombre+'->'+ nombre2+';\n')
        return f

    def _next(self, f, temp):
        if temp:
            if len(temp.child)==0 and temp!= self.root:
                nombre2 = "NodoH"+"D".join(str(x).replace(" ","")  for x in temp.keys)
                if temp.next:
                    f+=nombre2+'->'
                    f = self._next(f, temp.next)
                else:
                    f+=nombre2+';\n'
            else:
                if len(temp.child)!=0:
                    f = self._next(f, temp.child[0])
        return f
    
    def _rank(self, f, temp):
        if temp:
            if len(temp.child)==0 and temp!= self.root:
                nombre2 = "NodoH"+"D".join(str(x).replace(" ","")  for x in temp.keys)
                if temp.next:
                    f+=nombre2+';'
                    f = self._rank(f, temp.next)
                else:
                    f+=nombre2+'}\n'
            else:
                if len(temp.child)!=0:
                    f = self._rank(f,temp.child[0])
        return f

    def reorganizar(self):
        lista = list(self.lista().values())
        temp = self.root
        self.root = Node(None)
        self.Incremet = 1
        for l in lista:
            if self.buscar(l):
                self.root = temp
                return 1
            else:
                self.register(l)
        return 0

    def register(self, register):
        if len(register)!=self.columns:
            return 5
        if self.buscar(register):
            return 4
        try:
            key = self.GenKey(register)
            if not len(self.PKey):
                if len(self.search([key])):
                    self.reorganizar()
                    key = self.GenKey(register)
            self.insert(key, register)
            return 0
        except:
            if not len(self.PKey):
                self.PKey-=1
            return 1
    
    def GenKey(self, register):
        key = ''
        if len(self.PKey):
            if len(self.PKey)==1:
                key = str(register[self.PKey[0]])
            else:
                for x in self.PKey:
                    if self.PKey.index(x)==len(self.PKey)-1:
                        key+=str(register[x])
                    else:
                        key+= str(register[x])+'_'   
        else:
            key = str(self.Incremet)
            self.Incremet+=1
        return key
    
    def search(self, keys):
        try:
            key = "_".join(str(x) for x in keys)
            res = self._buscar(self.root, key)
            if res:
                return list(res.values[key])
            else:
                return [] 
        except:
            return []

    def buscar(self, register):
        try:
            if len(self.PKey):
                key = self.GenKey(register)
                return self._buscar(self.root ,key)
            else:
                return None
        except:
            return 1

    def _buscar(self, temp, key):
        found = False
        if temp.child:
            for i in range(0, len(temp.keys)):
                if key < temp.keys[i]:
                    found = True
                    return self._buscar(temp.child[i], key)
        if not found:
            if temp.child:
                return self._buscar(temp.child[len(temp.keys)], key)
            else:
                if key in temp.keys:
                    return temp
                else:
                    return False
        return False
    
    def CreatePK(self, Pk):
        try:
            if len(self.PKey):
                return 4
            else:
                maximun = max(Pk)
                minimun = min(Pk)
                if not (minimun >= 0 and maximun < self.columns):
                    return 5
                for x in Pk:
                    if type(x) != int:
                        return 1
                self.PKey = Pk
                if not len(self.root.keys):
                    self.Incremet = 1
                    return 0
                else:
                    res = self.reorganizar()
                    return res
        except:
            return 1
        
    def DeletePk(self):
        try:
            if not len(self.PKey):
                return 4
            else:
                self.PKey = []
                self.dropPK = True
                return 0
        except:
            return 1
    
    def addColumn(self, default):
        try:
            self.columns+=1
            lista = list(self.lista().values())
            for l in lista:
                l.append(default)
            return 0
        except:
            return 1
    
    def dropColumn(self, column):
        try:
            if column in self.PKey or self.columns==1:
                return 4
            else:
                if column < 0 or column >= self.columns:
                    return 5
                self.columns-=1
                lista = list(self.lista().values())
                for l in lista:
                    l.pop(column)
                if len(self.PKey):
                    for x in self.PKey:
                        if x>column:
                            index = self.PKey.index(x)
                            x-=1
                            self.PKey[index]=x
                return 0
        except:
            return 1
    
    def lista(self):
        try:
            if len(self.root.keys):
                return self._lista(self.root,{})
            else:
                return {}
        except:
            return {}
    
    def _lista(self, temp,lista):
        if len(temp.child):
            lista = self._lista(temp.child[0], {})
        else:
            lista.update(temp.values)
            if temp.next:
                lista.update(self._lista(temp.next,lista))
        return lista

    def GrafiarTupla(self, tupla):
        f= open('tupla.dot', 'w',encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out"];')
        f.write('rankdir=TB;\n')
        f.write('node [shape = box];\n')
        data =""
        for x in tupla:
            data+="""<td>"""+str(x)+"""</td>"""
        tabla ="""<<table cellspacing='0' cellpadding='20' border='0' cellborder='1'>
            <tr>"""+data+"""</tr>        
        </table> >"""
        f.write('table [label = '+tabla+',  fontsize="30", shape = plaintext ];\n')
        f.write('}')
        f.close()
        os.system('dot -Tpng tupla.dot -o tupla.png')
        os.system('tupla.png')

    def update(self, data, columns):
        try:
            key = "_".join(str(x) for x in columns)
            delete = False
            mini = min(data.keys())
            maxi = max(data.keys())
            if mini<0 or maxi>= self.columns:
                return 1
            for x in data.keys():
                if x in self.PKey:
                    delete = True
            return self._update(self.root, data, delete, key, columns)  
        except:
            return 1       
    
    def _update(self, temp, data, delete, key, keys):
        if temp.child:
            for i in range(0, len(temp.keys)):
                if key < temp.keys[i]:
                    return self._update(temp.child[i], data,delete,key,keys)

        if temp.child:
            return self._update(temp.child[len(temp.keys)], data,delete,key,keys)
        else:
            if key in temp.keys:
                try:
                    list = temp.values.get(key)[:]
                    for x in data.keys():
                        list[x] = data.get(x)
                    if delete:
                        if self.buscar(list):
                            return 1
                        self.delete(keys)
                        self.register(list)
                    else:
                        temp.values[key] = list
                    return 0
                except:
                    return 1
            else:
                return 4
        return 1
    
    def truncate(self):
        self.root = Node(None)
        self.Incremet = 1
