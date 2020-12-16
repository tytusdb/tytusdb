from graphviz import Digraph
import sys
import os
import GeneralesAVL as gA
import AVLtablas as ta
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

    def buscarBaseNodo(self, value):
        if self.root == None:
            return None
        else:
            return self._buscarBaseNodo(value, self.root)
        
    def _buscarBaseNodo(self, value, tmp):
        if value == tmp.value:
            return tmp
        elif value > tmp.value and tmp.derecha != None:
            return self._buscarBaseNodo(value, tmp.derecha)
        elif value < tmp.value and tmp.izquierda != None:
            return self._buscarBaseNodo(value, tmp.izquierda)

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
                return self._alterDatabase(dtbNueva, valueViejo, self.root)
        except:
            return 1
    
    def _alterDatabase(self, dtbNueva, valueViejo, tmp):
        if valueViejo == tmp.value:
            tmp.nomDTB = dtbNueva
            tmp.value = gA.g.jalarValN(dtbNueva)
            return 0
        elif valueViejo > tmp.value and tmp.derecha != None:
            return self._alterDatabase(dtbNueva, valueViejo, tmp.derecha)
        elif valueViejo < tmp.value and tmp.izquierda != None:
            return self._alterDatabase(dtbNueva, valueViejo, tmp.izquierda)

    #eliminar base de datos
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

    def dropDatabase(self, nomDTB):
        try:
            value = gA.g.jalarValN(nomDTB)
            if self.buscarBase(value):
                tablas = ta.t.showTables(nomDTB)
                print(tablas)
                for n in range(0,len(tablas)):
                    ta.t.dropTable(nomDTB, tablas[n])
                
                self.dropDatabaseN(self.buscarBaseNodo(value))
                return 0
        except:
            return 1
    
    def dropDatabaseN(self, tmp):
        if tmp == None:
            return 2  #base no existe
        else:
            nHoja = gA.g.nHojas(tmp)
            if nHoja == 0: #nodo sin hojas
                tata = self.tatascan((tmp.nivel+1), tmp.value)
                if tata != None:
                    if tata.izquierda == tmp:
                        tata.izquierda = None
                        return 0
                    else:
                        tata.derecha = None
                        return 0
                else:
                    self.root = None
                    return 0

            elif nHoja == 1: #nodo con 1 hoja
                if tmp.izquierda != None:
                    hijo = tmp.izquierda
                else:
                    hijo = tmp.derecha
                
                tata = self.tatascan((tmp.nivel+1), tmp.value)
                
                if tata != None:
                    if tata.izquierda == tmp:
                        tata.izquierda = hijo
                        tata.izquierda.nivel = hijo.nivel + 1
                        hijo = None
                        return 0
                    else:
                        tata.derecha = hijo
                        tata.derecha.nivel = hijo.nivel + 1
                        hijo = None
                        r = 0
                        return r
                else:
                    self.root = hijo
                    return 0

            elif nHoja == 2: #nodo con dos hojas
                if tmp.nivel != self.root.nivel: #esta condicion es para que tome bien el nivel si en dado caso quiere eliminar la raíz
                    leSigue = gA.g.leMenor(tmp)
                    self.dropDatabaseN(leSigue)
                    tmp.value = leSigue.value
                    tmp.nivel = leSigue.nivel + 1
                    return 0
                else:
                    leSigue = gA.g.leMenor(tmp)
                    self.dropDatabaseN(leSigue)
                    tmp.value = leSigue.value
                    tmp.nivel = self.root.nivel + 1
                    return 0
    #fin eliminar base -----------------


b = AVLBases()