from graphviz import Digraph
import sys
import os
#os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

class nodoTabla:
    index = 0
    grafica = 'digraph G {\n'
    def __init__(self, nomDTB, nomTBL, numCOL, index, value):
        self.nomDTB = nomDTB
        self.nomTBL = nomTBL
        self.numCOL = numCOL
        self.derecha = None
        self.izquierda = None
        self.index = index
        self.value = value
        self.nivel = 0

class AVLTablas:
    def __init__(self):
        self.root = None
    
    #index nodo
    def indexNodo(self):
        hey = nodoTabla.index
        hey += 1
        nodoTabla.index = hey
        return hey

    
    
    #rotaciones
    def srl(self, t1):
        t2 = t1.izquierda
        t1.izquierda = t2.derecha
        t2.derecha = t1
        t1.nivel = self.maxi(self.nivel(t1.izquirda), self.nivel(t1.derecha))+1
        t2.nivel = self.maxi(self.nivel(t2.izquirda), t1.nivel)+1
        return t2

    def srr(self, t1):
        t2 = t1.derecha
        t1.derecha = t2.izquierda
        t2.izquierda = t1
        t1.nivel = self.maxi(self.nivel(t1.izquierda), self.nivel(t1.derecha))+1
        t2.nivel = self.maxi(self.nivel(t2.izquierda), t1.nivel)+1
        return t2
    
    def drl(self, tmp):
        tmp.izquierda = self.srr(tmp.izquierda)
        return self.srl(tmp)
    
    def drr(self, tmp):
        tmp.derecha = self.srl(tmp.derecha)
        return self.srr(tmp)

    #agregar tabla
    def jalarValN(self, vali):
        return sum(ord(x) for x in vali)
    
    def agregarTabla(self, nomDTB, nomTBL, numCOL):
        self.root = self._agregarTabla(nomDTB, nomTBL, numCOL,self.root)
    
    def _agregarTabla(self, nomDTB, nomTBL, numCOL, tmp):
        if tmp is None:
            index = self.indexNodo()
            nodoTabla.grafica += str(index) + ' [label="' + nomDTB + ' | ' + nomTBL  + ' | ' + str(numCOL) + '"]\n'
            return nodoTabla(nomDTB, nomTBL, numCOL, index, (self.jalarValN(nomDTB) + self.jalarValN(nomTBL)))
        elif (self.jalarValN(nomDTB) + self.jalarValN(nomTBL)) > (self.jalarValN(tmp.nomDTB) + self.jalarValN(tmp.nomTBL)):
            tmp.derecha = self._agregarTabla(nomDTB, nomTBL, numCOL, tmp.derecha)
            if(self.nivel(tmp.derecha) - self.nivel(tmp.izquierda)) == 2:
                if self.jalarValN(nomTBL) > self.jalarValN(tmp.derecha.nomTBL):
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.izquierda = self._agregarTabla(nomDTB, nomTBL, numCOL, tmp.izquierda)
            if (self.nivel(tmp.izquierda) - self.nivel(tmp.derecha)) == 2:
                if self.jalarValN(nomTBL) < self.jalarValN(tmp.izquierda.nomTBL):
                    tmp = self.srl(tmp)
                else:
                    tmp = self.drl(tmp)
        d = self.nivel(tmp.derecha)
        i = self.nivel(tmp.izquierda)
        m = self.maxi(d, i)
        tmp.nivel = m + 1
        return tmp

    def nivel(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.nivel
        
    def maxi(self, r, l):
        return (l,r)[r>l]

    #saber quien es el padre:
    def tatascan(self, niv, value):
        return self._tatascan(niv, value, self.root)

    def _tatascan(self, niv, value, tmp):
        if (niv - 1) == self.root.nivel:
            return None
        elif tmp.nivel == niv and (tmp.izquierda.value == value or tmp.derecha.value == value):
            return tmp
        elif value > tmp.value and tmp.derecha != None:
            return self._tatascan(niv, value, tmp.derecha)
        elif value < tmp.value and tmp.izquierda != None:
            return self._tatascan(niv, value, tmp.izquierda)

    #para mostrar en consola
    def mostrarTablas(self):
        if self.root != None:
            self._mostrarTablas(self.root)

    def _mostrarTablas(self, tmp):
        if tmp != None:
            self._mostrarTablas(tmp.izquierda)
            print('Base = %s, Tabla = %s, Columnas = %d, Nivel = %d, Index: %d, Valor: %d'%(tmp.nomDTB, tmp.nomTBL, tmp.numCOL, tmp.nivel, tmp.index, tmp.value))
            self._mostrarTablas(tmp.derecha)

    #mostrar usando graphviz
    def crearGraphviz(self):
        self._crearGraphviz(self.root)
        nodoTabla.grafica += '}'
        archivo = open('Tablas.dot','w')
        archivo.write(nodoTabla.grafica)
        archivo.close()
        os.system('dot -Tsvg Tablas.dot -o Tablas.svg')

    def _crearGraphviz(self, tmp):
        if tmp:
            if tmp != self.root:
                tata = self.tatascan((tmp.nivel + 1), tmp.value)
                nodoTabla.grafica += str(tata.index) + ' -> ' + str(tmp.index) + '\n'
            self._crearGraphviz(tmp.izquierda)
            self._crearGraphviz(tmp.derecha)
    
#iniciar
os.system('cls')
t = AVLTablas()

#agregando tablas

t.agregarTabla('Base 1', 'Nombre', 25) #1071   1
t.agregarTabla('Base 2', 'Tabla 2', 15) #1027  2
t.agregarTabla('La Mera', 'Tabla 1', 50) #1608   3
t.agregarTabla('Base 2', 'Nombre', 8) #1072   4
t.agregarTabla('Hola', 'ya no', 15) #859    5
t.agregarTabla('Empresa', 'Empleados', 45) #1639    6

#mostrar
t.crearGraphviz()
t.mostrarTablas()