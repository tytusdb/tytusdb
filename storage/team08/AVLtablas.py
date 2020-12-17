from graphviz import Digraph
import sys
import os
import AVLbase as ba
import GeneralesAVL as gA
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

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
    def mostrarTablasConsola(self):
        if self.root != None:
            self._mostrarTablasConsola(self.root)

    def _mostrarTablasConsola(self, tmp):
        if tmp != None:
            print('Base = %s, Tabla = %s, Columnas = %d, Nivel = %d, Index: %d, Valor: %d'%(tmp.nomDTB, tmp.nomTBL, tmp.numCOL, tmp.nivel, tmp.index, tmp.value))
            self._mostrarTablasConsola(tmp.izquierda)
            self._mostrarTablasConsola(tmp.derecha)

    #mostrar usando graphviz, pendiente de correcciones
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
                if tata is not None:
                    nodoTabla.grafica += str(tata.index) + ' -> ' + str(tmp.index) + '\n'
            self._crearGraphviz(tmp.izquierda)
            self._crearGraphviz(tmp.derecha)

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
                lstTBL += [tmp.nomTBL]
                h = True
            self._extractTable(base, tabla, lstTBL,  h, tmp.izquierda)
            self._extractTable(base, tabla, lstTBL,  h, tmp.derecha)
        
        if lstTBL == [] and h == False:
            return None
        else:
            return lstTBL

    #devolver lista con un rango de la tabla
    def extractRangeTable(self, base, tabla, lower, upper):
        lstTBL = []
        h = False
        if self.root == None:
            return None
        else:
            return self._extractRangeTable(base, tabla, lstTBL, h, self.root)
        
    def _extractRangeTable(self, base, tabla, lstTBL,  h, tmp):
        if tmp:
            if tmp.nomDTB == base and tmp.nomTBL == tabla:
                lstTBL += [tmp.nomTBL] #aquí se llama la función que devuelve el rango de datos
                h = True
            self._extractRangeTable(base, tabla, lstTBL,  h, tmp.izquierda)
            self._extractRangeTable(base, tabla, lstTBL,  h, tmp.derecha)
        
        if lstTBL == [] and h == False:
            return None
        else:
            return lstTBL
    
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
                return self.dropTableN(self.buscarNodo(value))
            else:
                return 2
        except:
            return 1

    def dropTableN(self, tmp):
        if tmp == None:
            return 3  #tabla no existe
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
                    self.dropTableN(leSigue)
                    tmp.value = leSigue.value
                    tmp.nivel = leSigue.nivel + 1
                    return 0
                else:
                    leSigue = gA.g.leMenor(tmp)
                    self.dropTableN(leSigue)
                    tmp.value = leSigue.value
                    tmp.nivel = self.root.nivel + 1
                    return 0
    #fin eliminar tabla -----------------
        

    
'''#iniciar
#mostrar
t.mostrarTablasConsola()
#t.crearGraphviz()

#buscar tablas en base de datos
busc = 'Base 2'
print('Se va a buscar: ' + busc)
print(t.showTables(busc))

#extraer una tabla de una base
extraerB = 'Base 1'
extraerT = 'Tabla 1'
print('Se va a extraer: ' + extraerT + ' de ' + extraerB)
print(t.extractTable(extraerB,extraerT))

#extraer rango
xtraerB = 'Base 2'
xtraerT = 'Tabla 2'
up = 5
lo = 6
print('Se va a extraer: ' + xtraerT + ' de ' + xtraerB + ' desde ' + str(lo) + ' hasta ' + str(up))
print(t.extractRangeTable(extraerB,extraerT,lo,up))
eliB = 'Base 1'
eliT = 'Tabla 555'
print(t.dropTable(eliB,eliT))
t.mostrarTablasConsola()'''

t = AVLTablas()