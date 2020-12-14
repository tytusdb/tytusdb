
# ------------- CREACION DE LOS NODOS -------------#
class NodoB:
    def __init__(self, grado): #INICIALIZAR NODO
        self.llaves = []
        self.padre = None
        self.hijos = []
 
    def insertar(self, valor): 
        if valor not in self.llaves:
            self.llaves.append(valor)
            self.llaves.sort()
        return len(self.llaves)
    
    def comparar(self, valor):
        i = 0
        length = len(self.llaves) 
        if self.hijos == [] or valor in self.llaves: #Si la lista de hijos esta vacia o el valor ya se encuentra en la lista de llaves
            return -1
        while(i < length):
            if valor < self.llaves[i]:
                return i
            i += 1
        return i #Regresa la posicion

 # ----------------ARMAR EL ARBOL -----------------#
class ArbolB:
    def __init__(self, grado):
        self.root = NodoB(grado)
        self.grado = grado
        self.enmedio = int((self.grado-1)/2)
 
    def buscar(self, valor):
        return self._buscar(valor, None)

    def _buscar(self, valor, tmp):
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
        # Se le asigna el nodo padre a los nuevos nodos #
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
            tmp = self.buscar(valor)
            self._insertar(valor, tmp)
    
    def _insertar(self, valor, tmp):
        length = tmp.insertar(valor)
        if length == self.grado:
            self.separar_nodo(tmp)

