# File:     B Tree Structure
# License:  Released under MIT License
# Notice:   Copyright (c) 2020 TytusDB Team

import os

# ------------- CREACION DE LOS NODOS -------------#

class NodoB:
    def __init__(self, grado): #INICIALIZAR NODO
        self.llaves = []
        self.padre = None
        self.hijos = []
 
    def insertar(self, valor): 
        if valor not in self.llaves:
            self.llaves.append(valor)
            self.ordenar_llaves()
        return len(self.llaves)
    
    def comparar(self, valor):
        i = 0
        tamano = len(self.llaves) 
        if self.hijos == [] or self.buscar_llave(valor, self.llaves): #Si la lista de hijos esta vacia o el valor ya se encuentra en la lista de llaves
            return -1
        while(i < tamano):
            if str(valor).isdigit():
                if str(self.llaves[i][0]).isdigit():
                    if int(valor) < int(self.llaves[i][0]):
                        return i
                    i += 1
                else:
                    if int(valor) < self.toASCII(self.llaves[i][0]):
                        return i
                    i += 1
            else:
                if str(self.llaves[i][0]).isdigit():
                    if self.toASCII(valor) < int(self.llaves[i][0]):
                        return i
                    i += 1
                else:
                    if valor < self.llaves[i][0]:
                        return i
                    i += 1
        return i #Regresa la posicion
    
    def posicionNodo(self):
        try:
            return self.padre.hijos.index(self)
        except:
            pass
    
    def buscar_llave(self, llave, llaves):
        for i in llaves:
            if i[0] == llave:
                return True

    def ordenar_llaves(self):
        for i in range(len(self.llaves)-1):
            for j in range(i+1,len(self.llaves)):
                if str(self.llaves[i][0]).isdigit():
                    if str(self.llaves[j][0]).isdigit():
                        
                        if int(self.llaves[i][0]) > int(self.llaves[j][0]):
                            tmp = self.llaves[i]
                            self.llaves[i] = self.llaves[j]
                            self.llaves[j] = tmp
                    else:
                        if int(self.llaves[i][0]) > self.toASCII(self.llaves[j][0]):
                            tmp = self.llaves[i]
                            self.llaves[i] = self.llaves[j]
                            self.llaves[j] = tmp
                else:
                    if str(self.llaves[j][0]).isdigit():
                        if self.toASCII(self.llaves[i][0]) > int(self.llaves[j][0]):
                            tmp = self.llaves[i]
                            self.llaves[i] = self.llaves[j]
                            self.llaves[j] = tmp
                    else:
                        if self.llaves[i][0] > self.llaves[j][0]:
                            tmp = self.llaves[i]
                            self.llaves[i] = self.llaves[j]
                            self.llaves[j] = tmp
    
    def toASCII(self, cadena):
        result = 0
        for char in cadena:
            result += ord(char)
        return result

 # ----------------ARMAR EL ARBOL -----------------#

class arbolB:
    def __init__(self, grado):
        self.root = NodoB(grado)
        self.grado = grado
        self.enmedio = int((self.grado-1)/2)
 
    
    def buscar(self, valor):
        return self._buscar(valor)

    def _buscar(self, valor, tmp = None):
        if not tmp: 
            tmp2 = self.root
        else:
            tmp2 = tmp
        result = tmp2.comparar(valor)
        if result == -1:
            return tmp2
        else:
            return self._buscar(valor, tmp2.hijos[result])

    def separar_nodo(self, tmp):
        n1 = NodoB(self.grado)
        n2 = NodoB(self.grado)
        n3 = NodoB(self.grado)
        return self._separar_nodo(tmp,n1,n2,n3)
    
    def _separar_nodo(self, tmp,nodo_p,nodo_i,nodo_d): #Se crean 3 nodos nuevos para realizar la separacion de nodos
        if len(tmp.llaves)+ 1 <= self.grado:
            return 0
        padre = tmp.padre
        enmedio = self.enmedio
        center = tmp.llaves[enmedio]
        
        for i in range(0,enmedio):
            nodo_i.llaves.append(tmp.llaves[i]) #Llenado del nodo izquierdo

        for i in range(enmedio+1, len(tmp.llaves)):
            nodo_d.llaves.append(tmp.llaves[i]) #Llenado del nodo derecho

        if tmp.hijos != []:
            for i in range(enmedio+1):
                nodo_i.hijos.append(tmp.hijos[i]) #Asigna los hijos izquierdos
            for i in range(enmedio+1, len(tmp.hijos)):
                nodo_d.hijos.append(tmp.hijos[i]) #Asigna los hijos derechos
            i = 0
            while(i < enmedio+1):
                tmp.hijos[i].padre = nodo_i #Asigna el padre al nodo izquierdo 
                i += 1
            while(i < self.grado +1):
                tmp.hijos[i].padre = nodo_d #Asigna el padre al nodo derecho
                i += 1
 
        if not padre:
            padre = nodo_p
            padre.llaves.append(center)
            padre.hijos.insert(0, nodo_i)
            padre.hijos.insert(1, nodo_d)
            nodo_i.padre = padre
            nodo_d.padre = padre
            self.root = padre
            return 0
        nodo_i.padre = padre
        nodo_d.padre = padre
        padre.insertar(center)
        index = padre.hijos.index(tmp)
        padre.hijos.pop(index)
        padre.hijos.insert(index, nodo_i)
        padre.hijos.insert(index + 1, nodo_d)
        return self.separar_nodo(padre)
 
    def insertar(self, *valores):
        for valor in valores:
            tmp = self.buscar(valor[0])
            self._insertar(valor, tmp)
    
    def _insertar(self, valor, tmp):
        length = tmp.insertar(valor)
        if length == self.grado:
            self.separar_nodo(tmp)
 
    # UTILIDADES
    # ME DEVUELVE UNA LISTA CON LA INFORMACION DE TODOS LOS NODOS INGRESADOS

    def registros(self):
        global l
        l = list()
        return self._registros(self.root)

    def _registros(self, tmp):
        if tmp:
            for i in tmp.llaves:
                l.append(i[1])
            for j in tmp.hijos:
                self._registros(j)
        return l

    # ME DEVUELVE UNA LISTA CON LA PK DE TODOS LOS NODOS INGRESADOS

    def Keys(self):
        global l
        l = list()
        return self._Keys(self.root)

    def _Keys(self, tmp):
        if tmp:
            for i in tmp.llaves:
                l.append(str(i[0]))
            for j in tmp.hijos:
                self._Keys(j)
        return l
    
    # AGREGA UNA COLUMNA MAS A TODOS LOS NODOS

    def agregarValor(self, valor):
        self.root = self._agregarValor(self.root, valor)
    
    def _agregarValor(self, tmp, valor):
        if tmp:
            for i in tmp.llaves:
                i[1].append(valor)
            for j in tmp.hijos:
                self._agregarValor(j,valor)
        return tmp

    def update(self, valor, llave):
        self._update(self.root, valor, llave)

    def _update(self, tmp, valor, llave):
        if tmp:
            for i in tmp.llaves:
                if str(i[0]) == str(llave):
                    i[1] = valor
                    i[0] = llave
            for j in tmp.hijos:
                self._update(j, valor, llave)
        return tmp

    # ELIMINA UNA COLUMNA A TODOS LOS NODOS

    def eliminarValor(self, valor):
        self.root = self._eliminarValor(self.root, valor)
    
    def _eliminarValor(self, tmp, valor):
        if tmp:
            for i in tmp.llaves:
                i[1].pop(valor)
            for j in tmp.hijos:
                self._eliminarValor(j,valor)
        return tmp

    # ELIMINA UN NODO DEL ARBOL

    def _del(self, llave):
        tmp = self.buscar(llave)
        posicion = self.posicion(tmp, llave)
        tmp.llaves.pop(posicion)
        self.estructurar(tmp, posicion)

    # ME RETORNA LA POSICION DE UNA TUPLA EN UN NODO

    def posicion(self, nodo, llave):
        for i in range(len(nodo.llaves)):
            if str(nodo.llaves[i][0]) == str(llave):
                return i
    
    # ME RETORNA EL VALOR EN UNA POSICION

    def valor_buscar(self, nodo, llave):
        for i in range(len(nodo.llaves)):
            if str(nodo.llaves[i][0]) == str(llave):
                return nodo.llaves[i]

    # ORDENA EL ARBOL DE NUEVO

    def estructurar(self, tmp, posicion):
        if tmp.hijos == []:
            return self.unir(tmp, tmp.posicionNodo())
        siguiente = tmp.hijos[posicion + 1]
        tmp.insertar(siguiente.llaves.pop(0))
        return self.estructurar(siguiente, 0)
    
    # UNE LOS HIJOS AL PADRE PARA REGRESAR A LA FORMA IDEAL

    def unir(self, tmp, pos):
        if not tmp.padre:
            return 0
        
        if len(tmp.llaves) >= self.enmedio:
            return 0
 
        padre = tmp.padre
        if pos:
            pre = padre.llaves[pos-1]
            tmp2 = padre.hijos[pos-1]
        else:
            pre = None
            tmp2 = padre.hijos[1]
 
        if len(tmp2.llaves) > self.enmedio:
            return self.rotar(tmp, tmp2, padre, pre)
 
        if not pre:
            tmp.insertar(padre.llaves.pop(0))
            tmp2.hijos = tmp.hijos + tmp2.hijos
        else:
            tmp.insertar(padre.llaves.pop(pos-1))
            tmp2.hijos = tmp.hijos + tmp2.hijos
        tmp2.llaves += tmp.llaves
        tmp2.ordenar_llaves()       
        padre.hijos.remove(tmp)
        if len(padre.llaves) == 0 and not padre.padre:
            self.root = tmp2
            return 0
        
        if len(padre.llaves) < self.enmedio:
            return self.unir(padre, padre.posicionNodo())

    def rotar(self, nodo, tmp, padre, pre):
        if not pre:
            nodo.insertar(padre.llaves.pop(0)) #Izquierda
            padre.insertar(tmp.llaves.pop(0))
            return 0
        pos = nodo.posicionNodo() #Derecha
        nodo.insertar(padre.llaves.pop(pos-1))
        padre.insertar(tmp.llaves.pop(-1))
        return 0    

    def graficar(self):
        f = open('archivo.dot', 'w',encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out"];')
        f.write('rankdir=TB;\n')
        global t
        t = 0
        f = self._graficar(f,self.root)
        f.write('}')
        f.close()
        os.system('dot -Tpng archivo.dot -o salida.png')
    
    def _graficar(self, f, temp):
        global t
        if temp:
            nombre = "Nodo"+str(t)
            t+=1
            f.write(nombre+' [ label = "'+", ".join(str(x[0]) for x in temp.llaves)+'",shape = box];\n')
            for c in temp.hijos:
                nombre2 = "Nodo"+str(t)
                f = self._graficar(f, c)
                f.write(nombre+'->'+ nombre2+';\n')
                t+=1
        return f
