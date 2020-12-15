import os
import pickle

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

    def agregar(self, valor, dic):
        if self.raiz == None:
            self.raiz = Nodo(valor, dic)
        else:
            self._agregar(valor, self.raiz, dic)

    def _agregar(self, valor, tmp, dic):
        if valor < tmp.valor:
            if tmp.izq == None:
                tmp.izq = Nodo(valor, dic)
                tmp.izq.padre = tmp
                self.confirmaAgre(tmp.izq)
                return 1
            else:
                self._agregar(valor, tmp.izq, dic)
        else:
            if tmp.der == None:
                tmp.der = Nodo(valor, dic)
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
        if valor == tmp.valor:
            return tmp
        elif valor < tmp.valor and tmp.izq != None:
            return self._buscar(valor, tmp.izq)
        elif valor > tmp.valor and tmp.der != None:
            return self._buscar(valor, tmp.der)

    def eliminar(self, valor):
        return self._eliminar(self.buscar(valor))

    def _eliminar(self, tmp):

        if tmp == None or self.buscar(tmp.valor) == None:
            print("No se encuentra el valor")
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
                    print("Base de datos: ", raiz.valor)
                    raiz.lista.preorden()
                    return 1
            else:
                print("no existe la base de datos: ", db)
                return 2
        else:
            return 3

    def eliminartabla(self, db, tabla):
        raiz = self.buscar(db)
        if raiz != None:
            if raiz.lista is None:
                print("la lista no tiene raiz")
            else:
                raiz.lista.eliminar(tabla)
                print("Base de datos",raiz.valor)
                raiz.lista.preorden()

        else:
            print("no existe la base de datos: ", db)


    def buscartabla(self, db,tabla):
        raiz = self.buscar(db)
        if raiz != None:
            if raiz.lista != None:
                return raiz.lista.buscar(tabla)
            else:
                return None
        else:
            return None

    def agregarregistroatabla(self, db, tabla, valor):
        raiz = self.buscartabla(db, tabla)
        if raiz != None:
            if raiz.lista is None:
                raiz.lista = ArbolAVL()
                raiz.lista.agregar(valor[0], valor)
                print("base: ",db,"Tabla:" , raiz.valor)
                raiz.lista.preorden()
                return False
            else:
                raiz.lista.agregar(valor[0], valor)
                print("base: ",db,"Tabla:" , raiz.valor)
                raiz.lista.preorden()
                return False
        else:
            return True

    def generarlista(self, tmp, lista):
        if tmp:
            lista.append(tmp.valor)
            self.generarlista(tmp.izq, lista)
            self.generarlista(tmp.der, lista)
            return lista

    def generarregistros(self, tmp, lista, max, min):
        if max ==0 and min == 0:
            if tmp:
                cadena = ""
                for i in tmp.campos:
                    cadena = cadena + str(i)
                lista.append(cadena)
                self.generarregistros(tmp.izq, lista,0,0)
                self.generarregistros(tmp.der, lista,0,0)
                return lista
        else:
            if tmp:
                if tmp.valor > min and tmp.valor < max:
                    cadena = ""
                    for i in tmp.campos:
                        cadena = cadena + str(i)
                    lista.append(cadena)
                    self.generarregistros(tmp.izq, lista, min, max)
                    self.generarregistros(tmp.der, lista, min, max)
                    return lista
                else:
                    self.generarregistros(tmp.izq, lista, min, max)
                    self.generarregistros(tmp.der, lista, min, max)

    def agregarcolumna(self, tmp, valor):
        if tmp:
            tmp.campos[1].append(valor)
            self.generarregistros(tmp.izq, valor)
            self.generarregistros(tmp.der, valor)

    def eliminarcolumna(self, raiz, Nocol):
        if raiz.campos != None:
            raiz.campos.__delitem__(Nocol)
            self.eliminarcolumna(raiz.izquierdo, Nocol)
            self.eliminarcolumna(raiz.derecho, Nocol)

    def extraercolumna(self, raiz, lista, columnas):
        if raiz.campos:
            for i in lista:
                if raiz.campos[i] == columnas[i]:
                    print(raiz.campos)
                    return raiz
                else:
                    self.extraercolumna(raiz.izquierdo, lista, columnas)
                    self.extraercolumna(raiz.derecho, lista, columnas)

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
            subprocess.call("dot -Tpng tab.dot -o tab.png")
            os.system('tab.png')

    def _graficar(self, tmp):
        contenido = ""
        if tmp.izq == None and tmp.der == None:
            contenido = "nodo" + str(tmp.valor) + " [ label =\"" + str(tmp.valor) + "\"];\n    ";
        else:
            contenido = "nodo" + str(tmp.valor) + " [ label =\"<AI>|" + str(tmp.valor) + "|<AD>\"];\n    ";
        if tmp.izq != None:
            contenido += self._graficar(tmp.izq) + "nodo" + str(tmp.valor) + ":AI->nodo" + str(
                tmp.izq.valor) + "\n    ";

        if tmp.der != None:
            contenido += self._graficar(tmp.der) + "nodo" + str(tmp.valor) + ":AD->nodo" + str(tmp.der.valor) + "\n    "

        return contenido

    def createdatabase(self, valor):
        nodo = self.buscar(valor)
        if nodo is None:
            try:
                self.agregar(valor, None)
                return 0
            except:
                return 1

        else:
            return 2

    def showdatabases(self):
        lista = []
        list = self.generarlista(self.raiz, lista)
        print()
        print("Lista de elementos en arbol")
        print(list)
        return list

    def alterdatabase(self, old, nuevo):
        vieja = self.buscar(old)
        nueva = self.buscar(nuevo)
        if vieja != None:
            if nueva is None:
                vieja.valor = nuevo
                return 1
            else:
                return 3
        else:
            return 2

    def dropdatabase(self, db):
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

    def createtable(self, db, tabla, dic):
        raiz = self.buscar(db)
        i = self.buscartabla(db, tabla)
        if i is None:
            if raiz != None:
                if raiz.lista is None:
                    try:
                        raiz.lista = ArbolAVL()
                        lista = [None, dic]
                        raiz.lista.agregar(tabla, lista)
                        return 1
                    except:
                        return 0
                else:
                    try:
                        lista=[None, dic]
                        raiz.lista.agregar(tabla, lista)
                        print("Base de datos: ", raiz.valor)
                        raiz.lista.preorden()
                        return 1
                    except:
                        return 0
            else:
                print("no existe la base de datos: ", db)
                return 2
        else:
            return 3

    def showtables(self, db):
        raiz = self.buscar(db)
        if raiz != None:
            lista = []
            if raiz.lista != None:
                list = raiz.lista.generarlista(raiz.lista.raiz, lista)
                print(list)
                return list
        else:
            return None

    def extracttable(self, db, tabla):
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = []
                li = self.generarregistros(i.lista.raiz ,lista,0,0)
                print(li)
                return li
        else:
            return None


    def extractrangetable(self, db, tabla, max, min):
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = []
                li = self.generarregistros(i.lista.raiz, lista, max, min)
                print(li)
                return li
        else:
            return None

    def alteraddpk(self, db, tabla, columnas):
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                if i.campos[0] != None:
                    return 4
                else:
                    try:
                        i.campos[0] = columnas
                        print(i.campos)
                        return 0
                    except:
                        return 1
            else:
                return 3
        else:
            return 2

    def alterdroppk(self, db, tabla):
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

    def altertable(self, db, tabla, tablanueva):
        print("altertable")

    def alteraddcolumn(self, db, tabla, valor):
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    self.agregarcolumna(i.lista.raiz, valor)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def alterdropcolumn(self, db, tabla, Nocol):
        raiz = self.buscar(db)
        if raiz !=None:
            i = self.buscartabla(db, tabla)
            if i != None:
                if i.campos[1] < Nocol:
                    return 5
                else:
                    for f in i.campos[0]:
                        if f == Nocol:
                            return 4
                try:
                    self.eliminarcolumna(i.lista.raiz, Nocol)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def droptable(self, db, tabla):
        print("eliminar tabla")

    def insert(self, db, tabla, lista):
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                try:
                    self.agregarregistroatabla(db, tabla, lista)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def extractrow(self, db, tabla, columnas):
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = i.campos[0]
                try:
                    self.extraercolumna(i.lista.raiz, lista, columnas)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def deletet(self, db, tabla, columnas):
        raiz = self.buscar(db)
        if raiz != None:
            i = self.buscartabla(db, tabla)
            if i != None:
                lista = i.campos[0]
                try:
                    tmp = self.extraercolumna(i.lista.raiz, lista, columnas)
                    i.lista.eliminar(tmp.valor)
                    return 0
                except:
                    return 1
            else:
                return 3
        else:
            return 2

    def truncate(self, db, tabla):
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

def commit(objeto, nombre):
    file = open(nombre + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()

def rollback(nombre):
    file = open(nombre + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)


t = ArbolAVL()
t.createdatabase(1)
t.createdatabase(23)
t.createdatabase(45)
t.createdatabase(86)
t.createdatabase(89)
t.createdatabase(5)

t.showdatabases()
t.enorden()
t.dropdatabase(20)

t.preorden()
t.enorden()

t.createtable(1, 3, 1)
t.createtable(1, 10, 1)
t.createtable(1, 13, 1)
t.createtable(1, 5, 1)
t.createtable(5, 6, 1)
t.createtable(5, 15, 1)
t.createtable(5, 20, 1)
t.eliminartabla(1,5)
lita = [1,2,3]
lita1 = [2,2,4]
lita2 = [3,2,5]

t.agregarregistroatabla(1,3,lita)
t.agregarregistroatabla(1,3,lita1)
t.agregarregistroatabla(1,3,lita2)
print("extraer tabla")
t.extracttable(1,3)
print("extraer rango de tablas")
t.extractrangetable(1,3,3,1)
t.agregarregistroatabla(5,6,lita)
t.preorden()
t.showtables(1)
t.showtables(1)
t.alteraddpk(1,3,[0,1])
t.alterdroppk(1,3)
t.alteraddpk(1,3,[0,2])
