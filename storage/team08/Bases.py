#D:\Usuarios\ayapa\Escritorio\U\2020\VD\EDD\PR
from graphviz import Digraph
import pickle
import sys
import os
import GeneralesAVL as gA
import Tablas as ta
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

class nodoBase:
    index = 0
    grafica = 'digraph G {\n'
    def __init__(self, nomDTB, index, value):
        self.nomDTB = nomDTB
        self.derecha = None
        self.izquierda = None
        self.index = index
        self.value = value
        self.nivel = 0

class AVLBases:
    
    def __init__(self):
        self.root = None
        self.graf = None
    
    def guardar(self):
        gA.g.commitBase(self, nodoBase.index)

    #index nodo
    def indexNodo(self):
        hey = nodoBase.index
        hey += 1
        nodoBase.index = hey
        return hey

    #agregar Base
    def createBase(self, nomDTB):
        try:
            value = gA.g.jalarValN(nomDTB)
            if self.buscarBase(value):
                return 2
            else:
                self.root = self._createBase(nomDTB,self.root)
                return 0
        except:
            return 1
    
    def _createBase(self, nomDTB, tmp):
        if tmp is None:
            index = self.indexNodo()
            nodoBase.grafica += str(index) + ' [label="' + nomDTB + '"]\n'
            return nodoBase(nomDTB, index, gA.g.jalarValN(nomDTB))
        elif gA.g.jalarValN(nomDTB) > (gA.g.jalarValN(tmp.nomDTB)):
            tmp.derecha = self._createBase(nomDTB, tmp.derecha)
            if(gA.g.nivel(tmp.derecha) - gA.g.nivel(tmp.izquierda)) == 2:
                if gA.g.jalarValN(nomDTB) > gA.g.jalarValN(tmp.derecha.nomDTB):
                    tmp = gA.g.srr(tmp)
                else:
                    tmp = gA.g.drr(tmp)
        else:
            tmp.izquierda = self._createBase(nomDTB, tmp.izquierda)
            if (gA.g.nivel(tmp.izquierda) - gA.g.nivel(tmp.derecha)) == 2:
                if gA.g.jalarValN(nomDTB) < gA.g.jalarValN(tmp.izquierda.nomDTB):
                    tmp = gA.g.srl(tmp)
                else:
                    tmp = gA.g.drl(tmp)
        d = gA.g.nivel(tmp.derecha)
        i = gA.g.nivel(tmp.izquierda)
        m = gA.g.maxi(d, i)
        tmp.nivel = m + 1
        return tmp

    #para mostrar en consola
    def mostrarBasesConsola(self):
        if self.root != None:
            self._mostrarBasesConsola(self.root)

    def _mostrarBasesConsola(self, tmp):
        if tmp != None:
            print('Base = %s, Index: %d, Valor: %d'%(tmp.nomDTB, tmp.index, tmp.value))
            self._mostrarBasesConsola(tmp.izquierda)
            self._mostrarBasesConsola(tmp.derecha)

    #mostrar devolviendo listas
    def showDataBases(self):
        lstBDT = []
        if self.root == None:
            return None
        else:
            return self._showDataBases(lstBDT, self.root)
        
    def _showDataBases(self, lstBDT, tmp):
        if tmp is not None:
            lstBDT += [tmp.nomDTB]
            self._showDataBases(lstBDT, tmp.izquierda)
            self._showDataBases(lstBDT, tmp.derecha)
        return lstBDT

    def buscarBase(self, value):
        if self.root == None:
            return None
        else:
            return self._buscarBase(value, self.root)
        
    def _buscarBase(self, value, tmp):
        if value == tmp.value:
            return True
        elif value > tmp.value and tmp.derecha != None:
            return self._buscarBase(value, tmp.derecha)
        elif value < tmp.value and tmp.izquierda != None:
            return self._buscarBase(value, tmp.izquierda)

    #cambiar nombre de Base
    def alterDatabase(self, dtbVieja, dtbNueva):
        try:
            valueViejo = gA.g.jalarValN(dtbVieja)
            valueNuevo = gA.g.jalarValN(dtbNueva)
            if self.buscarBase(valueViejo) != True:
                return 2
            elif self.buscarBase(valueNuevo):
                return 3
            else:
                self.dropDatabase(dtbVieja)
                self.createBase(dtbNueva)
                return 0
        except:
            return 1
    
    #eliminar tabla
    def dropDatabase(self, nomDTB):
        try:
            value = gA.g.jalarValN(nomDTB)
            if self.buscarBase(value):
                tablas = ta.t.showTables(nomDTB)
                if tablas is None:
                    self._dropDatabase(value ,self.root)
                    return 0
                else:
                    for n in range(0,len(tablas)):
                        ta.t.dropTable(nomDTB, tablas[n])
                    self._dropDatabase(value, self.root)
                    return 0    
            else:
                return 2
        except:
            return 1
    
    def _dropDatabase(self, value, tmp):
        if not tmp:
            return tmp
        elif value < tmp.value:
            tmp.izquierda = self._dropDatabase(value, tmp.izquierda)
        elif value > tmp.value:
            tmp.derecha = self._dropDatabase(value, tmp.derecha)
        else:
            if tmp.derecha is None:
                temp = tmp.derecha
                tmp = None
                return temp
            elif tmp.derecha is None:
                temp = tmp.izquierda
                tmp = None
                return temp
            temp = gA.g.leMenor(tmp.derecha)
            tmp.value = temp.value
            tmp.derecha = self._dropDatabase(temp.value, tmp.derecha)
        
        if tmp is None:
            return tmp
        
        tmp.nivel = 1 + gA.g.maxi(gA.g.nivel(tmp.izquierda), gA.g.nivel(tmp.derecha))
        balan = gA.g.Balance(tmp)

        if balan > 1 + gA.g.Balance(tmp.izquierda) >= 0:
            return gA.g.srr(tmp)

        if balan < -1 and gA.g.Balance(tmp.derecha) <= 0:
            return gA.g.srl(tmp)

        if balan > 1 and gA.g.Balance(tmp.izquierda) < 0:
            tmp.derecha = gA.g.srl(tmp.izquierda)
            return gA.g.srr(tmp)

        if balan < -1 and gA.g.Balance(tmp.derecha) < 0:
            tmp.derecha = gA.g.srr(tmp.derecha)
            return gA.g.drl(tmp)
            
        return tmp

    def generarGraphvizBases(self):
        self.graf = Digraph(
            format='svg', filename = 'Bases Árbol', 
            node_attr={'shape': 'circle', 'height': '1', 'size': '8'})
        #agregar raíz 
        self.graf.node(self.root.nomDTB)
        #generar el resto
        self._generarGraphvizBases(self.root)
        self.graf.attr(rank='same')
        #mostrar
        self.graf.view()
    
    def _generarGraphvizBases(self, tmp):
        if tmp != None:
            if tmp.izquierda != None:
                self.graf.node(tmp.izquierda.nomDTB)
                self.graf.edge(tmp.nomDTB, tmp.izquierda.nomDTB)
            if tmp.derecha != None:
                self.graf.node(tmp.derecha.nomDTB)
                self.graf.edge(tmp.nomDTB, tmp.derecha.nomDTB)
            self._generarGraphvizBases(tmp.izquierda)
            self._generarGraphvizBases(tmp.derecha)

b = AVLBases()