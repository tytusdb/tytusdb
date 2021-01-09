import os


class BplusGraph:
    def __init__(self, tree):
        self.tree = tree
        self.root = tree.root

    def export(self):
        fname = '_tmp_/grafo-bplus'
        f = open(fname + '.dot', 'w', encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out", bgcolor="#0f1319"];')
        f.write('rankdir=TB;\n')
        f.write('node [shape = box, style= filled, color="#006400", fillcolor="#90EE90"];\n')
        f.write('edge[color="#145A32"]')
        f = self._graficar(f, self.root, '')
        lista = self._next('', self.root)
        lista1 = self._rank('{rank=same;', self.root)
        if lista != '':
            f.write(lista)
        if lista1 != '{rank=same;':
            f.write(lista1)
        f.write('}')
        f.close()
        os.system('dot ' + fname + '.dot' + ' -Tpng -o ' + fname + '.png')
        os.remove(fname + '.dot')

    def _graficar(self, f, temp, nombre):
        if temp:
            if nombre == '':
                nombre = "Nodo" + "D".join(str(x).replace(" ", "") for x in temp.keys)
            valor = "   |   ".join("".join(str(x)) for x in temp.keys)
            f.write(nombre + ' [ label = "' + valor + '"];\n')
            for c in temp.child:
                if c:
                    if len(c.child) == 0:
                        nombre2 = "NodoH" + "D".join(str(x).replace(" ", "") for x in c.keys)
                    else:
                        nombre2 = "Nodo" + "D".join(str(x).replace(" ", "") for x in c.keys)
                    f = self._graficar(f, c, nombre2)
                    f.write(nombre + '->' + nombre2 + ';\n')
        return f

    def _next(self, f, temp):
        if temp:
            if len(temp.child) == 0 and temp != self.root:
                nombre2 = "NodoH" + "D".join(str(x).replace(" ", "") for x in temp.keys)
                if temp.next:
                    f += nombre2 + '->'
                    f = self._next(f, temp.next)
                else:
                    f += nombre2 + ';\n'
            else:
                if len(temp.child) != 0:
                    f = self._next(f, temp.child[0])
        return f

    def _rank(self, f, temp):
        if temp:
            if len(temp.child) == 0 and temp != self.root:
                nombre2 = "NodoH" + "D".join(str(x).replace(" ", "") for x in temp.keys)
                if temp.next:
                    f += nombre2 + ';'
                    f = self._rank(f, temp.next)
                else:
                    f += nombre2 + '}\n'
            else:
                if len(temp.child) != 0:
                    f = self._rank(f, temp.child[0])
        return f
