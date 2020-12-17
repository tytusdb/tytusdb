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
        t1.nivel = self.maxi(self.nivel(t1.izquierda), self.nivel(t1.derecha))+1
        t2.nivel = self.maxi(self.nivel(t2.izquierda), t1.nivel)+1
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
    
    def createTable(self, nomDTB, nomTBL, numCOL):
        self.root = self._createTable(nomDTB, nomTBL, numCOL,self.root)
    
    def _createTable(self, nomDTB, nomTBL, numCOL, tmp):
        if tmp is None:
            index = self.indexNodo()
            nodoTabla.grafica += str(index) + ' [label="' + nomDTB + ' | ' + nomTBL  + ' | ' + str(numCOL) + '"]\n'
            return nodoTabla(nomDTB, nomTBL, numCOL, index, self.jalarValN(nomTBL))
        elif self.jalarValN(nomTBL) > (self.jalarValN(tmp.nomTBL)):
            tmp.derecha = self._createTable(nomDTB, nomTBL, numCOL, tmp.derecha)
            if(self.nivel(tmp.derecha) - self.nivel(tmp.izquierda)) == 2:
                if self.jalarValN(nomTBL) > self.jalarValN(tmp.derecha.nomTBL):
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.izquierda = self._createTable(nomDTB, nomTBL, numCOL, tmp.izquierda)
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
    def mostrarTablasConsola(self):
        if self.root != None:
            self._mostrarTablasConsola(self.root)

    def _mostrarTablasConsola(self, tmp):
        if tmp != None:
            self._mostrarTablasConsola(tmp.izquierda)
            print('Base = %s, Tabla = %s, Columnas = %d, Nivel = %d, Index: %d, Valor: %d'%(tmp.nomDTB, tmp.nomTBL, tmp.numCOL, tmp.nivel, tmp.index, tmp.value))
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
    def leMenor(self, tmp):
        while tmp.izquierda != None:
            tmp = tmp.izquierda
        return tmp  

    def buscar(self, value):
        if self.root == None:
            return None
        else:
            return self._buscar(value, self.root)
        
    def _buscar(self, value, tmp):
        if value == tmp.value:
            return tmp
        elif value > tmp.value and tmp.derecha != None:
            return self._buscar(value, tmp.derecha)
        elif value < tmp.value and tmp.izquierda != None:
            return self._buscar(value, tmp.izquierda)

    def nHojas(self, tmp):
        nHojas = 0
        if tmp.izquierda != None:
            nHojas += 1
        if tmp.derecha != None:
            nHojas += 1
        return nHojas

    def dropTable(self, nomDTB, nomTBL):
        try:
            value = self.jalarValN(nomTBL)
            return self.dropTableN(self.buscar(value))
            #falta comprobar que exista la base para devolver 2 sino existe
        except:
            return 1

    def dropTableN(self, tmp):
        if tmp == None:
            return 3  #tabla no existe
        else:
            nHoja = self.nHojas(tmp)
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
                    leSigue = self.leMenor(tmp)
                    self.dropTableN(leSigue)
                    tmp.value = leSigue.value
                    tmp.nivel = leSigue.nivel + 1
                    return 0
                else:
                    leSigue = self.leMenor(tmp)
                    self.dropTableN(leSigue)
                    tmp.value = leSigue.value
                    tmp.nivel = self.root.nivel + 1
                    return 0
    #fin eliminar tabla -----------------
        

    
#iniciar
os.system('cls')
t = AVLTablas()

#agregando tablas
t.createTable('Base 1', 'Nombre 1', 25) #692   1
t.createTable('Base 2', 'Tabla 2', 15) #566  2
t.createTable('Base 1', 'Tabla 1', 50) #565   3
t.createTable('Base 2', 'Nombre', 8) #611   4
t.createTable('Base 2', 'ya no', 15) #471    5
t.createTable('Base 3', 'ya', 5) #218    6
t.createTable('Base 1', 'Empleados', 45) #922    7
t.createTable('Base 2', 'Sucursal', 5) #850    8
t.createTable('Base 1', 'Yucas', 5) #517    9

#mostrar
t.mostrarTablasConsola()
'''#t.crearGraphviz()

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
print(t.extractRangeTable(extraerB,extraerT,lo,up))'''
eliB = 'Base 1'
eliT = 'Tabla 555'
print(t.dropTable(eliB,eliT))
t.mostrarTablasConsola()