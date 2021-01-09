import os


class HashGraph:
    def __init__(self, table):
        self.table = table
        self.size = 13
        self.vector = table.vector

    def export(self):
        fname = '_tmp_/grafo-hash'
        file = open(fname + '.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write('graph [pad="0.5", bgcolor="#0f1319"];' + os.linesep)
        file.write("nodesep=.05;" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)
        file.write(
            'node [shape=record,width=.1,height=.1, style= filled, color="#006400", fillcolor="#90EE90"];' + os.linesep)
        file.write('edge[color="#145A32"];' + os.linesep)

        for i in range(self.size):
            if i == 0:
                file.write('vector [label = "<f0> 0|' + os.linesep)
            elif i == self.size - 1:
                file.write(
                    '<f' + str(i) + '> ' + str(i) + '",height=' + str(self.size / 2) + ', width=.8];' + os.linesep)
            else:
                file.write('<f' + str(i) + '> ' + str(i) + '|' + os.linesep)

        contador = 0
        for listaNodos in self.vector:
            if not listaNodos is None:
                for nodo in listaNodos:
                    file.write('node' + str(nodo.primaria).replace(' ', '').replace('-', 'y') + '[label = "{<n> ' + str(
                        nodo.primaria).replace(' ', '').replace('-', 'y') + '| <p> }"];' + os.linesep)
                file.write(
                    'vector:f' + str(contador) + ' -> node' + str(listaNodos[0].primaria).replace(' ', '').replace('-',
                                                                                                                   'y') + ':n;' + os.linesep)
                if len(listaNodos) > 1:
                    for i in range(len(listaNodos)):
                        if not i == len(listaNodos) - 1:
                            file.write('node' + str(listaNodos[i].primaria).replace(' ', '').replace('-',
                                                                                                     'y') + ':p -> node' + str(
                                listaNodos[i + 1].primaria).replace(' ', '').replace('-', 'y') + ':n;' + os.linesep)

            else:
                file.write('nodeNone' + str(contador) + ' [shape=plaintext, label="None", width=0.5]' + os.linesep)
                file.write('vector:f' + str(contador) + ' -> nodeNone' + str(contador) + os.linesep)
            contador += 1

        file.write(' }' + os.linesep)
        file.close()
        os.system('dot ' + fname + '.dot' + ' -Tpng -o ' + fname + '.png')
        os.remove(fname + '.dot')
