#Package:       AVL Mode
#License:       Released under MIT License
#Notice:        Copyright  (c) 2020 Tytus DB Team

import os
import pickle
import csv

class Nodo:
    def __init__(self, valor, dic):
        self.valor = valor
        self.campos = dic
        self.izq = self.der = None
        self.padre = None
        self.altura = 1
        self.lista = None


class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.contador = 1

    def agregar(self, valor, dic):
        valor = str(valor)
        if self.raiz == None:
            self.raiz = Nodo(valor, dic)
            self.contador += 1
        else:
            self._agregar(valor, self.raiz, dic)

    def _agregar(self, valor, tmp, dic):
        valor = str(valor)
        if valor < tmp.valor:
            if tmp.izq == None:
                tmp.izq = Nodo(valor, dic)
                self.contador += 1
                tmp.izq.padre = tmp
                self.confirmaAgre(tmp.izq)
                return 1
            else:
                self._agregar(valor, tmp.izq, dic)
        else:
            if tmp.der == None:
                tmp.der = Nodo(valor, dic)
                self.contador += 1
                tmp.der.padre = tmp
                self.confirmaAgre(tmp.der)
                return 1
            else:
                self._agregar(valor, tmp.der, dic)

    def preorden(self):
        self._preorden(self.raiz)
        print()

    def _preorden(self, tmp):
        if tmp:
            print(tmp.valor, end=' ')
            self._preorden(tmp.izq)
            self._preorden(tmp.der)

    def enorden(self):
        self._enorden(self.raiz)
        print()

    def _enorden(self, tmp):
        if tmp:
            self._preorden(tmp.izq)
            print(tmp.valor, end=' ')
            self._preorden(tmp.der)

    def postorden(self):
        self._preorden(self.raiz)
        print()

    def _postorden(self, tmp):
        if tmp:
            self._preorden(tmp.izq)
            self._preorden(tmp.der)
            print(tmp.valor, end=' ')

    def altura(self):
        if self.raiz != None:
            return self._altura(self.raiz, 0)
        else:
            return 0

    def _altura(self, tmp, altPrevia):
        if tmp == None: return altPrevia
        alturaIzq = self._altura(tmp.izq, altPrevia + 1)
        alturaDer = self._altura(tmp.der, altPrevia + 1)
        return max(alturaIzq, alturaDer)

    def buscar(self, valor):
        if self.raiz != None:
            return self._buscar(valor, self.raiz)
        else:
            return None

    def _buscar(self, valor, tmp):
        valor = str(valor)
        if valor == tmp.valor:
            return tmp
        elif valor < tmp.valor and tmp.izq != None:
            return self._buscar(valor, tmp.izq)
        elif valor > tmp.valor and tmp.der != None:
            return self._buscar(valor, tmp.der)

    def eliminar(self, valor):
        valor = str(valor)
        return self._eliminar(self.buscar(valor))

    def _eliminar(self, tmp):

        if tmp == None or self.buscar(tmp.valor) == None:
            return None

        def minimValor(tmp):
            actual = tmp
            while actual.izq != None:
                actual = actual.izq
            return actual

        def numHijos(tmp):
            numHijos = 0
            if tmp.izq != None:
                numHijos += 1
            if tmp.der != None:
                numHijos += 1
            return numHijos

        nodoPadre = tmp.padre

        nodoHijo = numHijos(tmp)

        if nodoHijo == 0:

            if nodoPadre != None:
                if nodoPadre.izq == tmp:
                    nodoPadre.izq = None
                else:
                    nodoPadre.der = None
            else:
                self.raiz = None

        if nodoHijo == 1:

            if tmp.izq != None:
                hijo = tmp.izq
            else:
                hijo = tmp.der

            if nodoPadre != None:
                if nodoPadre.izq == tmp:
                    nodoPadre.izq = hijo
                else:
                    nodoPadre.der = hijo
            else:
                self.raiz = hijo

            # correct the padre pointer in node
            hijo.padre = nodoPadre

        if nodoHijo == 2:
            siguiente = minimValor(tmp.der)

            tmp.valor = siguiente.valor

            self._eliminar(siguiente)

            return

        if nodoPadre != None:
            nodoPadre.altura = 1 + max(self.altura(nodoPadre.izq), self.altura(nodoPadre.der))
            self.validaEliminacion(nodoPadre)

    def confirmaAgre(self, tmp, ajuste=[]):
        if tmp.padre == None: return
        ajuste = [tmp] + ajuste

        alturaIzq = self.altura(tmp.padre.izq)
        alturaDer = self.altura(tmp.padre.der)

        if abs(alturaIzq - alturaDer) > 1:
            ajuste = [tmp.padre] + ajuste
            self.balanceo(ajuste[0], ajuste[1], ajuste[2])
            return

        nuevaAltura = 1 + tmp.altura
        if nuevaAltura > tmp.padre.altura:
            tmp.padre.altura = nuevaAltura

        self.confirmaAgre(tmp.padre, ajuste)

    def validaEliminacion(self, tmp):
        if tmp == None: return

        if abs(self.altura(tmp.izq) - self.altura(tmp.der)) > 1:
            y = self.hijoMayor(tmp)
            x = self.hijoMayor(y)
            self.balanceo(tmp, y, x)

        self.validaEliminacion(tmp.padre)

    def balanceo(self, z, y, x):
        if y == z.izq and x == y.izq:
            self.rotDer(z)
        elif y == z.izq and x == y.der:
            self.rotIzq(y)
            self.rotDer(z)
        elif y == z.der and x == y.der:
            self.rotIzq(z)
        elif y == z.der and x == y.izq:
            self.rotDer(y)
            self.rotIzq(z)

    def rotDer(self, z):
        sub_raiz = z.padre
        y = z.izq
        t3 = y.der
        y.der = z
        z.padre = y
        z.izq = t3
        if t3 != None: t3.padre = z
        y.padre = sub_raiz
        if y.padre == None:
            self.raiz = y
        else:
            if y.padre.izq == z:
                y.padre.izq = y
            else:
                y.padre.der = y
        z.altura = 1 + max(self.altura(z.izq),
                           self.altura(z.der))
        y.altura = 1 + max(self.altura(y.izq),
                           self.altura(y.der))

    def rotIzq(self, z):
        sub_raiz = z.padre
        y = z.der
        t2 = y.izq
        y.izq = z
        z.padre = y
        z.der = t2
        if t2 != None: t2.padre = z
        y.padre = sub_raiz
        if y.padre == None:
            self.raiz = y
        else:
            if y.padre.izq == z:
                y.padre.izq = y
            else:
                y.padre.der = y
        z.altura = 1 + max(self.altura(z.izq),
                           self.altura(z.der))
        y.altura = 1 + max(self.altura(y.izq),
                           self.altura(y.der))

    def altura(self, tmp):
        if tmp == None:
            return 0
        return tmp.altura

    def hijoMayor(self, tmp):
        izq = self.altura(tmp.izq)
        der = self.altura(tmp.der)
        return tmp.izq if izq >= der else tmp.der


    def agregaralista(self, db, tabla, dic):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        i = self.buscartabla(db, tabla)
        if i is None:
            if raiz != None:
                if raiz.lista is None:
                    raiz.lista = ArbolAVL()
                    cam = [None, dic]
                    raiz.lista.agregar(tabla, cam)
                    return 1
                else:
                    cam = [None, dic]
                    raiz.lista.agregar(tabla, cam)
                    return 1
            else:
                return 2
        else:
            return 3

    def buscartabla(self, db,tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)

        if raiz != None:
            if raiz.lista != None:
                return raiz.lista.buscar(tabla)
            else:
                return None
        else:
            return None

    def buscarreistro(self, db,tabla , valor):
        valor = str(valor)
        tabla = str(tabla)
        db = str(db)
        raiz = self.buscartabla(db, tabla)
        if raiz != None:
            if raiz.lista != None:
                l = raiz.lista.buscar(valor)
                return l
            else:
                return None
        else:
            return None

    def agregarregistroatabla(self, db, tabla, valor, lista):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscartabla(db, tabla)
        if raiz != None:
            if raiz.lista is None:
                raiz.lista = ArbolAVL()
                cadena = ""
                if lista != None:
                    for i in lista:
                        cadena += str(valor[int(i)])+"_"
                    cadena = cadena[0:len(cadena) - 1]
                else:
                    cadena = raiz.lista.contador
                raiz.lista.agregar(cadena, valor)
            else:
                cadena = ""

                if lista != None:
                    for i in lista:
                        cadena += str(valor[int(i)])+"_"
                    cadena = cadena[0:len(cadena) - 1]
                else:
                    cadena = raiz.lista.contador

                tmp = self.buscarreistro(db, tabla, cadena)
                if tmp is None:
                    raiz.lista.agregar(cadena, valor)
                else:
                    return 4
        else:
            return True

    def generarlista(self, tmp, lista):
        if tmp:
            lista.append(tmp.valor)
            self.generarlista(tmp.izq, lista)
            self.generarlista(tmp.der, lista)
            return lista

    def generarregistros(self, tmp, lista, max, min, col):
        if tmp != None:
            max = str(max)
            min = str(min)
            l = str(0)
            if max == l and min == l:
                if tmp:
                    cadena = ""
                    for i in tmp.campos:
                        cadena = cadena + str(i)
                    lista.append(tmp.campos)
                    self.generarregistros(tmp.izq, lista,0,0,0)
                    self.generarregistros(tmp.der, lista,0,0,0)
                    return lista
            else:
                if tmp:
                    if int(col) <= len(tmp.campos):
                        if str(tmp.campos[int(col)]) >= str(min) and str(tmp.campos[int(col)]) <= str(max):
                            lista.append(tmp.campos)
                            self.generarregistros(tmp.izq, lista, max, min,col)
                            self.generarregistros(tmp.der, lista, max, min,col)
                            return lista
                        else:
                            self.generarregistros(tmp.izq, lista, max, min,col)
                            self.generarregistros(tmp.der, lista, max, min,col)

    def agregarcolumna(self, tmp, valor):
        valor = str(valor)
        if tmp:
            tmp.campos.append(valor)
            self.agregarcolumna(tmp.izq, valor)
            self.agregarcolumna(tmp.der, valor)

    def eliminarcolumna(self, raiz, Nocol):
        if raiz != None:
            Nocol=int(Nocol)
            raiz.campos.pop(Nocol)
            self.eliminarcolumna(raiz.izq, Nocol)
            self.eliminarcolumna(raiz.der, Nocol)

    def extraercolumna(self, raiz, lista, columnas):
        if raiz:
            compro = raiz.valor.split("_")
            if compro == columnas:
                return raiz.campos

            else:
                if raiz.izq != None:
                    po = self.extraercolumna(raiz.izq, lista, columnas)
                    if po != None:
                        return po
                if raiz.der != None:
                    po = self.extraercolumna(raiz.der, lista, columnas)
                    if po != None:
                        return po
        else:
           return None

    def cambiardatos(self, tmp, columnas,db,tabla,arbol):
        cadena = ""
        if tmp != None:
            if tmp.izq == None and tmp.der == None:
                for i in columnas:
                    cadena += str(tmp.campos[int(i)]) + "_"
                cadena = cadena[0:len(cadena) - 1]
                arbol.agregar(cadena, tmp.campos)
            if tmp.izq != None and tmp.der !=None:
                for i in columnas:
                    cadena += str(tmp.campos[int(i)]) + "_"
                cadena = cadena[0:len(cadena) - 1]
                arbol.agregar(cadena, tmp.campos)
                self.cambiardatos(tmp.izq, columnas, db, tabla, arbol)
                self.cambiardatos(tmp.der, columnas, db, tabla, arbol)
            if tmp.izq != None and tmp.der ==None:
                for i in columnas:
                    cadena += str(tmp.campos[int(i)]) + "_"
                cadena = cadena[0:len(cadena) - 1]
                arbol.agregar(cadena, tmp.campos)
                self.cambiardatos(tmp.izq, columnas, db, tabla, arbol)
            if tmp.izq == None and tmp.der !=None:
                for i in columnas:
                    cadena += str(tmp.campos[int(i)]) + "_"
                cadena = cadena[0:len(cadena) - 1]
                arbol.agregar(cadena, tmp.campos)
                self.cambiardatos(tmp.der, columnas, db, tabla, arbol)
        return arbol

    def graficar(self):
        contenido = "digraph grafica{\n    rankdir=TB;\n    node [shape = record, style=filled, fillcolor=lightcyan2];\n    "
        contenido += self._graficar(self.raiz)
        contenido += "}"

        if contenido != "":
            tabGen = open("tab.dot","w")
            tabGen.write(contenido)
            tabGen.close()
            tab = open("tab.cmd","w")
            tab.write("dot -Tpng tab.dot -o tab.png")
            tab.close()
            try:
                os.system('tab.cmd')
            except:
                print("")

    def _graficar(self, tmp):
        contenido = ""
        if tmp.izq == None and tmp.der == None:
            contenido = "nodo" + str(tmp.valor) + " [ label =\"" + str(tmp.valor) + "\"];\n    "
        else:
            contenido = "nodo" + str(tmp.valor) + " [ label =\"<AI>|" + str(tmp.valor) + "|<AD>\"];\n    "
        if tmp.izq != None:
            contenido += self._graficar(tmp.izq) + "nodo" + str(tmp.valor) + ":AD->nodo" + str(tmp.izq.valor) + "\n    "

        if tmp.der != None:
            contenido += self._graficar(tmp.der) + "nodo" + str(tmp.valor) + ":AI->nodo" + str(tmp.der.valor) + "\n    "

        return contenido

    def contadorRep(self, columnas):
        return self._contadorRp(self.raiz, columnas)

    def _contadorRp(self, tmp, columnas):
        cadena = ""
        for i in columnas:
            cadena +=str(tmp.campos[int(i)])+","
        cadena = cadena[0:len(cadena)-1]
        bandera = False
        if tmp.izq == None and tmp.der == None:
            bandera = self.buscRep(cadena, columnas)
            if bandera == False:
                return False
        if tmp.izq != None:
            self._contadorRp(tmp.izq, columnas)
            bandera = self.buscRep(cadena, columnas)
            if bandera == False:
                return False
        if tmp.der != None:
            self._contadorRp(tmp.der, columnas)
            bandera = self.buscRep(cadena, columnas)
            if bandera == False:
                return False
        return bandera

    def buscRep(self, valor, columnas):
        contador = self._buscarRep(valor, self.raiz, columnas)
        if contador > 1:
            return False
        else:
            return True

    def _buscarRep(self, valor, tmp, columnas):
        contador = 0
        if tmp.izq == None and tmp.der == None:
            cadena = ""
            for i in columnas:
                cadena += str(tmp.campos[int(i)]) + ","
            cadena = cadena[0:len(cadena) - 1]

            if cadena == valor:
                contador += 1
        if tmp.izq != None and tmp.der != None:
            contador += self._buscarRep(valor, tmp.izq, columnas)
            contador += self._buscarRep(valor, tmp.der, columnas)
            cadena = ""
            for i in columnas:
                cadena += str(tmp.campos[int(i)]) + ","
            cadena = cadena[0:len(cadena) - 1]
            if cadena == valor:
                contador += 1

        if tmp.izq != None and tmp.der == None:
            contador += self._buscarRep(valor, tmp.izq, columnas)
            cadena = ""
            for i in columnas:
                cadena += str(tmp.campos[int(i)]) + ","
            cadena = cadena[0:len(cadena) - 1]
            if cadena == valor:
                contador += 1

        if tmp.izq == None and tmp.der != None:
            contador += self._buscarRep(valor, tmp.der, columnas)
            cadena = ""
            for i in columnas:
                cadena += str(tmp.campos[int(i)]) + ","
            cadena = cadena[0:len(cadena) - 1]
            if cadena == valor:
                contador += 1
        return contador

    def createDatabase(self, valor):
        valor = str(valor)
        nodo = self.buscar(valor)
        if nodo is None:
            try:
                self.agregar(str(valor), None)
                return 0
            except:
                return 1

        else:
            return 2

    def showDatabases(self):
        lista = []
        list = self.generarlista(self.raiz, lista)
        return list

    def alterDatabase(self, old, nuevo):
        old = str(old)
        nuevo = str(nuevo)
        vieja = self.buscar(old)
        nueva = self.buscar(nuevo)
        if vieja != None:
            if nueva is None:
                vieja.valor = nuevo
                self.validaEliminacion(vieja)
                #__________________________________________
                return 1
            else:
                return 3
        else:
            return 2

    def dropDatabase(self, db):
        db = str(db)
        base = self.buscar(db)
        if base is None:
            return 2
        else:
            self.eliminar(db)
            i = self.buscar(db)
            if i is None:
                return 0
            else:
                return 1

    def createTable(self, db, tabla, dic):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        i = self.buscartabla(db, tabla)

        if i is None:
            if raiz != None:
                if raiz.lista is None:
                    try:
                        raiz.lista = ArbolAVL()
                        lista = [None, dic, raiz.lista.contador]
                        raiz.lista.agregar(tabla, lista)
                        return 0
                    except:
                        return 1
                else:
                    try:
                        lista=[None, dic, raiz.lista.contador]
                        raiz.lista.agregar(tabla, lista)
                        return 0
                    except:
                        return 1
            else:
                return 2
        else:
            return 3

    def showTables(self, db):
        db = str(db)
        raiz = self.buscar(db)
        if raiz != None:
            lista = []
            if raiz.lista != None:
                list = raiz.lista.generarlista(raiz.lista.raiz, lista)
                return list
        else:
            return None

    def extractTable(self, db, tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i.lista != None:
                lista = []
                li = self.generarregistros(i.lista.raiz ,lista,0,0,0)
                return li
        else:
            return None

    def extractRangeTable(self, db, tabla, col,max, min):
        db = str(db)
        tabla = str(tabla)
        min = str(min)
        max = str(max)
        raiz = self.buscar(db)
        if raiz.lista != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = []
                li = self.generarregistros(i.lista.raiz, lista, max, min,col)
                return lista
        else:
            return None

    def alterAddPK(self, db, tabla, columnas):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                if i.campos[0] != None:
                    return 4
                else:
                    try:
                        if i.lista is None:
                            i.campos[0] = columnas
                        else:
                            listanueva = []
                            if i.campos[0] is None:
                                listanueva.append(i.campos[2])
                            else:
                                listanueva = i.campos[0]

                            t2 = i.lista
                            if t2.contadorRep(columnas):
                                i.campos[0]=columnas
                                arbol = ArbolAVL()
                                a = i.lista.cambiardatos(i.lista.raiz,columnas,db,tabla,arbol)
                                i.lista = a
                            else:
                                return 1
                        return 0
                    except:
                        return 1
            else:
                return 3
        else:
            return 2

    def alterDropPK(self, db, tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                if i.campos[0] != None:
                    try:
                        i.campos[0]=None
                        return 0
                    except:
                        return 1
                else:
                    return 4
            else:
                return 3
        else:
            return 2

    def alterTable(self, db, tabla, tablanueva):
        tabla = str(tabla)
        db = str(db)
        tablanueva=str(tablanueva)
        raiz = self.buscar(db)
        if raiz != None:
            f = self.buscartabla(db, tablanueva)
            if f is None:
                i = self.buscartabla(db, tabla)
                if i !=None:
                    try:
                        i.valor = tablanueva
                        self.validaEliminacion(i)
                        return 0
                    except:
                        return 1
                else:
                    return 3
            else:
                return 4
        else:
            return 2

    def alterAddColumn(self, db, tabla, valor):
        db = str(db)
        tabla = str(tabla)
        valor = str(valor)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    i.campos[1]=int(i.campos[1])
                    i.campos[1]=i.campos[1]+1
                    self.agregarcolumna(i.lista.raiz, valor)
                    return 0
                except:
                    return 1 
            else:
                return 3
        else:
            return 2

    def alterDropColumn(self, db, tabla, Nocol):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz !=None:
            i = self.buscartabla(db, tabla)
            if i != None:
                if int(i.campos[1]) < int(Nocol):
                    return 5
                else:
                    for f in i.campos[0]:
                        if f == Nocol:
                            return 4
                try:
                    i.campos[1]=int(i.campos[1])-1
                    self.eliminarcolumna(i.lista.raiz, Nocol)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def dropTable(self, db, tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            if raiz.lista is None:
                return 3
            else:
                try:
                    raiz.lista.eliminar(tabla)
                    return 0
                except:
                    return 1

        else:
            return 2

    def insert(self, db, tabla, lista):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    c = 0
                    c = int(i.campos[1])
                    if c != len(lista):
                        return 5
                    else:
                        lista2 = []
                        if i.campos[0] is None:
                            lista2 = None
                        else:
                            lista2 = i.campos[0]
                        r = self.agregarregistroatabla(db, tabla, lista, lista2)
                        if r == 4:
                            return 4
                        else:
                            return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def extractRow(self, db, tabla, columnas):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = i.campos[0]
                try:
                    ja = self.extraercolumna(i.lista.raiz, lista, columnas)
                    return ja
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def update(self, db, tabla, dict, columnas):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    cadena = ""
                    for j in columnas:
                        cadena += str(j) + "_"
                    cadena = cadena[0:len(cadena) - 1]
                    l = self.buscarreistro(db, tabla, cadena)
                    bandera = False
                    for key in dict:
                        for clave in i.campos[0]:
                            if int(key) == int(clave) or int(key)>int(i.campos[1]):
                                bandera = True

                    if bandera == False:
                        for key in dict:
                            l.campos[int(key)]=dict[key]
                    else:
                        return 1
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def deletet(self, db, tabla, columnas):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = i.campos[0]
                try:
                    if lista is None:
                        i.lista.eliminar(columnas[0])
                    else:
                        cadena = ""
                        for j in columnas:
                            cadena += str(j) +"_"
                        cadena = cadena[0:len(cadena)-1]
                        eliminado=self.buscarreistro(db, tabla, cadena)
                        if eliminado != None:
                            i.lista.eliminar(eliminado.valor)
                        else:
                            return 4
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def truncate(self, db, tabla):
        db = str(db)
        tabla = str(tabla)
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    i.lista = None
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def loadCSV(self, dirfile, database, table):
        l = []
        raiz = self.buscar(database)
        i = self.buscartabla(database, table)
        if raiz is not None:
            if i is not None:
                with open(dirfile) as f:
                    reader = csv.reader(f)
                    for row in reader:
                        #row = [int(i) for i in row]   Convierte la lista de string a int
                        if int(i.campos[1]) == len(row):
                            con = self.insert(database, table, row)
                            if con != 4:
                                l.append(row)

        return l


def commit(objeto, nombre):
    file = open(nombre + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()

def rollback(nombre):
    file = open(nombre + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)
