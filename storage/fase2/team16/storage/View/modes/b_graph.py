import os


class BGraph:
    def __init__(self, tree):
        self.tree = tree
        self.root = tree.root

    def export(self):
        fname = '_tmp_/grafo-b'
        f = open(fname + '.dot', 'w', encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out", bgcolor="#0f1319"];')
        f.write('node [style= filled, color="#006400", fillcolor="#90EE90"]; \n')
        f.write('edge[color="#145A32"];')
        f.write('rankdir=TB;\n')
        global t
        t = 0
        f = self._graficar(f, self.root)
        f.write('}')
        f.close()
        os.system('dot ' + fname + '.dot' + ' -Tpng -o ' + fname + '.png')
        os.remove(fname + '.dot')

    def _graficar(self, f, temp):
        global t
        if temp:
            nombre = "Nodo" + str(t)
            t += 1
            f.write(nombre + ' [ label = "' + ", ".join(str(x[0]) for x in temp.llaves) + '",shape = box];\n')
            for c in temp.hijos:
                nombre2 = "Nodo" + str(t)
                f = self._graficar(f, c)
                f.write(nombre + '->' + nombre2 + ';\n')
                t += 1
        return f
