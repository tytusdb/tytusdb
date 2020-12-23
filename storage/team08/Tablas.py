from graphviz import Digraph
import sys
import os
import GeneralesAVL as gA
import Bases as ba
import Tuplas as tu
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

class nodoTabla:
    index = 0
    grafica = ''
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
        self.graf = None
    
    def guardar(self):
        gA.g.commitTabla(self, nodoTabla.index)
    
    #index nodo
    def indexNodo(self):
        hey = nodoTabla.index
        hey += 1
        nodoTabla.index = hey
        return hey
    
    #agregar tabla
    def createTable(self, nomDTB, nomTBL, numCOL):
        try:
            valueBase = gA.g.jalarValN(nomDTB)
            valueTabla = gA.g.jalarValN(nomTBL)
            if ba.b.buscarBase(valueBase):
                if self.buscar(valueTabla, nomDTB):
                    return 3
                else:
                    self.root = self._createTable(nomDTB, nomTBL, numCOL,self.root)
                    return 0
            else:
                return 2
        except:
            return 1
    
    def _createTable(self, nomDTB, nomTBL, numCOL, tmp):
        if tmp is None:
            index = self.indexNodo()
            nodoTabla.grafica += str(index) + ' [label="' + nomDTB + ' | ' + nomTBL  + ' | ' + str(numCOL) + '"]\n'
            return nodoTabla(nomDTB, nomTBL, numCOL, index, gA.g.jalarValN(nomTBL))
        elif gA.g.jalarValN(nomTBL) > (gA.g.jalarValN(tmp.nomTBL)):
            tmp.derecha = self._createTable(nomDTB, nomTBL, numCOL, tmp.derecha)
            if(gA.g.nivel(tmp.derecha) - gA.g.nivel(tmp.izquierda)) == 2:
                if gA.g.jalarValN(nomTBL) > gA.g.jalarValN(tmp.derecha.nomTBL):
                    tmp = gA.g.srr(tmp)
                else:
                    tmp = gA.g.drr(tmp)
        else:
            tmp.izquierda = self._createTable(nomDTB, nomTBL, numCOL, tmp.izquierda)
            if (gA.g.nivel(tmp.izquierda) - gA.g.nivel(tmp.derecha)) == 2:
                if gA.g.jalarValN(nomTBL) < gA.g.jalarValN(tmp.izquierda.nomTBL):
                    tmp = gA.g.srl(tmp)
                else:
                    tmp = gA.g.drl(tmp)
        d = gA.g.nivel(tmp.derecha)
        i = gA.g.nivel(tmp.izquierda)
        m = gA.g.maxi(d, i)
        tmp.nivel = m + 1
        return tmp

    #para mostrar en consola
    def mostrarTablasConsola(self):
        if self.root != None:
            self._mostrarTablasConsola(self.root)

    def _mostrarTablasConsola(self, tmp):
        if tmp != None:
            print('Base = %s, Tabla = %s, Columnas = %s, Nivel = %d, Index: %d, Valor: %d'%(tmp.nomDTB, tmp.nomTBL, tmp.numCOL, tmp.nivel, tmp.index, tmp.value))
            self._mostrarTablasConsola(tmp.izquierda)
            self._mostrarTablasConsola(tmp.derecha)

    #buscar por nombre de Base de datos y devolver lista
    def showTables(self, base):
        lstTBL = []
        if self.root == None:
            return None
        else:
            return self._showTables(base, lstTBL, self.root)
        
    def _showTables(self, base, lstTBL, tmp):
        if tmp:
            if tmp.nomDTB == base:
                lstTBL += [tmp.nomTBL]
            self._showTables(base, lstTBL, tmp.izquierda)
            self._showTables(base, lstTBL, tmp.derecha)
        return lstTBL

    #devolver lista de registros de una tabla
    def extractTable(self, base, tabla):
        lstTBL = []
        h = False
        if self.root == None:
            return None
        else:
            return self._extractTable(base, tabla, lstTBL, h, self.root)
        
    def _extractTable(self, base, tabla, lstTBL,  h, tmp):
        if tmp:
            if tmp.nomDTB == base and tmp.nomTBL == tabla:
                for n in range(0,tu.u.cantiKey()+1):
                    val = tu.u.mandarDatosTBL(n, base, tabla)
                    if val is not None:
                        lstTBL += [val]
                        h = True

            self._extractTable(base, tabla, lstTBL,  h, tmp.izquierda)
            self._extractTable(base, tabla, lstTBL,  h, tmp.derecha)
        
        if lstTBL == [] and h == False:
            return None
        else:
            return lstTBL

    #devolver lista con un rango de la tabla
    def extractRangeTable(self, base, tabla,col,lower, upper):
        if self.root == None:
            return None
        else:
            lst = tu.u.extractRowRange(base,tabla,col,lower,upper)
            if lst == []:
                return lst
            elif lst is None:
                return None
            else:
                return lst
            #return self._extractRangeTable(base, tabla, lstTBL, col, lower, upper, h, self.root)
        
    #buscar columna
    def buscarCol(self, value, nomDTB):
        if self.root == None:
            return None
        else:
            return self._buscarCol(value, nomDTB, self.root)
        
    def _buscarCol(self, value, nomDTB, tmp):
        if value == tmp.value and nomDTB == tmp.nomDTB:
            return tmp.numCOL
        elif value > tmp.value and tmp.derecha != None:
            return self._buscarCol(value, nomDTB, tmp.derecha)
        elif value < tmp.value and tmp.izquierda != None:
            return self._buscarCol(value, nomDTB, tmp.izquierda)

    #eliminar tabla ---------------------
    def buscar(self, value, nomDTB):
        if self.root == None:
            return None
        else:
            return self._buscar(value, nomDTB, self.root)
        
    def _buscar(self, value, nomDTB, tmp):
        if value == tmp.value and nomDTB == tmp.nomDTB:
            return True
        elif value > tmp.value and tmp.derecha != None:
            return self._buscar(value, nomDTB, tmp.derecha)
        elif value < tmp.value and tmp.izquierda != None:
            return self._buscar(value, nomDTB, tmp.izquierda)
    
    def buscarNodo(self, value):
        if self.root == None:
            return None
        else:
            return self._buscarNodo(value, self.root)
        
    def _buscarNodo(self, value, tmp):
        if value == tmp.value:
            return tmp
        elif value > tmp.value and tmp.derecha != None:
            return self._buscarNodo(value, tmp.derecha)
        elif value < tmp.value and tmp.izquierda != None:
            return self._buscarNodo(value, tmp.izquierda)

    def dropTable(self, nomDTB, nomTBL):
        try:
            valueB = gA.g.jalarValN(nomDTB)
            value = gA.g.jalarValN(nomTBL)
            if ba.b.buscarBase(valueB):
                if self.buscar(value, nomDTB):
                    self._dropTable(value, self.root)
                    return 0
                else:
                    return 3
            else:
                return 2
        except:
            return 1

    def _dropTable(self, value, tmp):
        if not tmp:
            return tmp
        elif value < tmp.value:
            tmp.izquierda = self._dropTable(value, tmp.izquierda)
        elif value > tmp.value:
            tmp.derecha = self._dropTable(value, tmp.derecha)
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
            tmp.derecha = self._dropTable(temp.value, tmp.derecha)
        
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

    #renombrar tabla de una base de datos
    def alterTable(self, nomDTB, nomTBLV, nomTBLN):
        try:
            valueDTB = gA.g.jalarValN(nomDTB)
            valueTBLV = gA.g.jalarValN(nomTBLV)
            valueTBLN = gA.g.jalarValN(nomTBLN)
            if ba.b.buscarBase(valueDTB):
                if self.buscar(valueTBLV, nomDTB):
                    if self.buscar(valueTBLN, nomDTB):
                        return 4
                    else:
                        tmp = self.buscarNodo(valueTBLV)
                        c = tmp.numCOL
                        self.dropTable(nomDTB, nomTBLV)
                        self.createTable(nomDTB, nomTBLN,c)
                        return 0
                else:
                    return 3
            else:
                return 2
        except:
            return 1
    
    def generarGraphvizTablas(self):
        self.graf = Digraph(
            format='svg', filename = 'Tablas Árbol', 
            node_attr={'shape': 'circle', 'height': '1', 'size': '8'})
        #agregar raíz 
        self.graf.node(self.root.nomDTB + ' | ' + self.root.nomTBL + ' | ' + self.root.numCOL)
        #generar el resto
        self._generarGraphvizTablas(self.root)
        self.graf.attr(rank='same')
        #mostrar
        self.graf.view()
    
    def _generarGraphvizTablas(self, tmp):
        if tmp != None:
            if tmp.izquierda != None:
                self.graf.node(tmp.izquierda.nomDTB + ' | '  + tmp.izquierda.nomTBL)
                self.graf.edge(tmp.nomDTB + ' | '  + tmp.nomTBL, tmp.izquierda.nomDTB + ' | '  +  tmp.izquierda.nomTBL)
            if tmp.derecha != None:
                self.graf.node(tmp.derecha.nomDTB + ' | ' + tmp.derecha.nomTBL)
                self.graf.edge(tmp.nomDTB  + ' | ' + tmp.nomTBL, tmp.derecha.nomDTB + ' | ' + tmp.derecha.nomTBL)
            self._generarGraphvizTablas(tmp.izquierda)
            self._generarGraphvizTablas(tmp.derecha)
    

t = AVLTablas()