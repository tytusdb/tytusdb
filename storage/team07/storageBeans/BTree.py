def toASCII(cadena):
    cadena = str(cadena)
    resultado = 0
    for i in cadena:
        i = str(i)
        resultado += ord(i)
    return resultado


class Table(object):  # sera mi llave
    def __init__(self, name):
        self.name = name
        self.numero = toASCII(name)  # codigo ascci del name
        # self.AVLtree = AVLtree()


class Nodo(object):
    def __init__(self, padre):
        self.hoja = True
        self.n = 0  # cantidad de elementos almacenados , cantidad de tablas almacenadas
        self.elementos = []  # va a ser del tamaño del grado del arbol  , los elementos del nodo, son tables
        self.hijos = []  # va a ser del tamaño del grado del arbol, los hijos seran nodos
        if padre == 0:  # significa que es la cabeza por lo tanto el padre es None
            self.padre = None  # sera un nudo o null
        else:
            self.padre = padre

    def insert(self, elemento):
        self.n += 1
        self.elementos.append(Table(elemento))  # Table(elemento)
        if (self.n > 1):
            self.sort()

    def sort(self):
        i = 0
        while i < self.n - 1:
            j = i + 1
            while j < self.n:
                if (self.elementos[i].numero > self.elementos[j].numero):
                    temporal = self.elementos[i]
                    self.elementos[i] = self.elementos[j]
                    self.elementos[j] = temporal
                j += 1
            i += 1

    def show(self):
        cadena = "[ "
        i = 0
        while i < self.n:
            cadena += f"{self.elementos[i].numero} "
            i += 1
        cadena += " ]"
        print(cadena)


class Btree(object):
    def __init__(self):
        self.cabeza = Nodo(0)  # es como null , no tiene padre
        # self.avl = AVLtree()
        self.grado = 5  # hare un split , cuando tenga 5 elementos en mi nodo

    def insert(self, elemento):
        self.cabeza = self._insert(elemento, self.cabeza)  # cabeza es un nodo que contiene un table

    def _insert(self, elemento, temporal):  # elemento es un int, temporal es un nodo
        if temporal.hoja:
            temporal.insert(elemento)
        else:
            encontrar = False
            i = 0
            while i < temporal.n - 1:
                if (toASCII(elemento) < temporal.elementos[i].numero):
                    encontrar = True
                    self._insert(elemento, temporal.hijos[i])
                    break
                i += 1
            if encontrar is False:
                self._insert(elemento, temporal.hijos[temporal.n])
        if (temporal.n == self.grado):  # se hace un split
            if (temporal.padre is None):
                c = temporal
                temporal = Nodo(0)
                temporal.insert(c.elementos[2].name)  # se le debe enviar un string - un elemento
                temporal.hijos.append(Nodo(temporal))
                temporal.hijos.append(Nodo(temporal))
                i = 0
                while i < 2:
                    temporal.hijos[0].insert(c.elementos[i].name)
                    i += 1
                i = 3
                while i < self.grado:
                    temporal.hijos[1].insert(c.elementos[int(i)].name)
                    i += 1
                temporal.hoja = False
            else:
                tempElemento = temporal.elementos[2].name  # es mas para sacar mi nameque va en medio
                temporal.padre.insert(tempElemento)
                index = 0
                while index < temporal.padre.n:
                    if (temporal.padre.elementos[index].name == tempElemento):
                        break
                    index += 1
                i = temporal.padre.n
                while (i > index + 1):
                    try:
                        temporal.padre.hijos[i] = temporal.padre.hijos[i - 1]
                    except:
                        temporal.padre.hijos.append(temporal.padre.hijos[i - 1])
                    i -= 1

                temporal.padre.hijos.append(Nodo(temporal.padre))
                i = 3
                while i < self.grado:
                    temporal.padre.hijos[index + 1].insert(temporal.elementos[int(i)].name)
                    i += 1
                aux = temporal
                try:
                    temporal.padre.hijos[index] = Nodo(temporal.padre)
                except:
                    temporal.padre.hijos.append(Nodo(temporal.padre))
                i = 0
                while i < 2:
                    temporal.padre.hijos[index].insert(aux.elementos[i].name)
                    i += 1
        return temporal

    def show(self):
        self._show(self.cabeza, 0)

    def _show(self, temporal, h):  # nodo y altura
        print(f"Nivel {h}: ")
        temporal.show()
        i = 0
        while i < self.grado:
            try:
                if (temporal.hijos[i] is not None):
                    self._show(temporal.hijos[i], h + 1)
                i += 1
            except:
                i += 1


b = Btree()
b.insert("byron")
b.insert("april")
b.insert("Kelly")
b.insert("NOse")
b.insert("asda")
b.insert("sds")
b.insert("ASga")
b.insert("puto")
b.insert("algo")
b.insert("xD")


# b.insert("a")
# b.insert("b")
# b.insert("c")
# b.insert("d")
# b.insert("e")
# b.insert("f")
# b.insert("g")
# b.insert("h")
# b.insert("i")
# b.insert("j")
# b.insert("k")
# b.insert("l")
# b.insert("m")
# b.insert("n")
# b.insert("o")
# b.insert("p")
# b.insert("q")

b.show()
