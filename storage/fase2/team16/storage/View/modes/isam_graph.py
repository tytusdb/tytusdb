import os


class ISAMGraph:
    def __init__(self, table):
        self.tree = table
        self.root = table.tuples.root

    def export(self):
        fname = '_tmp_/grafo-isam'
        file = open(fname + '.dot', 'w')
        file.write('digraph isam {\ngraph[bgcolor="#0f1319"];\n')
        file.write('rankdir=TD;\n')
        file.write('node[shape=box, style= filled, color="#006400", fillcolor="#90EE90"];\n')
        file.write('edge[color="#145A32"];')
        file.close()
        self._chart(self.root, 0)
        file = open(fname + '.dot', "a")
        file.write('}')
        file.close()
        os.system('dot ' + fname + '.dot' + ' -Tpng -o ' + fname + '.png')
        os.remove(fname + '.dot')

    def _chart(self, tmp, level):
        if tmp:
            fname = '_tmp_/grafo-isam'
            file = open(fname + '.dot', 'a')
            tail = ''
            for i in tmp.values:
                tail += str(i.PK) + ', '
            if level < 2:
                if tmp.left is not None:
                    leftHead = ''
                    for i in tmp.left.values:
                        leftHead += str(i.PK) + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(leftHead)[:-2] + '" \n')
                if tmp.center is not None:
                    centerHead = ''
                    for i in tmp.center.values:
                        centerHead += str(i.PK) + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(centerHead)[:-2] + '" \n')
                if tmp.right is not None:
                    rightHead = ''
                    for i in tmp.right.values:
                        rightHead += str(i.PK) + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(rightHead)[:-2] + '" \n')
                if tmp.left is None and tmp.right is None and tmp.center is None and level == 0:
                    head = ''
                    for i in tmp.values:
                        head += i.PK + ', '
                    head = head[:-2]
                    file.write(' " ' + head + '"' + '[shape=box] \n')
                file.close()
                self._chart(tmp.left, level + 1)
                self._chart(tmp.center, level + 1)
                self._chart(tmp.right, level + 1)
            else:
                if tmp.next is not None:
                    nextHead = ''
                    for i in tmp.next.values:
                        nextHead += str(i.PK) + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(nextHead)[:-2] + '" \n')
                file.close()
                self._chart(tmp.next, level + 1)
