
from parserT28.controllers.optimization_controller import OptimizationController


class ReportOfOptimization:
    def __init__(self):
        pass

    def get_report(self):
        file_content = ''
        file_content += "digraph D{\n\t"
        file_content += 'graph [pad="0.8", nodesep="0.8", ranksep="1", bgcolor = grey77, label=\"Report Of Optimization\"];\n'
        file_content += 'node [shape=note]\n'
        file_content += 'rankdir=LR;\n'
        file_content += 'arset [label=<\n'
        file_content += '<table border="0" cellborder="1" color="green1" cellspacing="0">\n'
        file_content += "<tr> <td colspan=\"4\" bgcolor=\"green1\"> Reporte De Optimizacion </td></tr> \n\n"
        file_content += "\n\t <tr> <td bgcolor=\"paleturquoise1\"> ID </td>\n <td  bgcolor=\"paleturquoise1\"> No Optimizado </td>\n <td bgcolor=\"paleturquoise1\"> Optimizado </td>\n"
        file_content += '<td bgcolor=\"paleturquoise1\">  Regla Aplicada  </td></tr>\n\r'
        for data in OptimizationController().getList():
            file_content += '<tr>\n\t'
            valor = self.relIntoWord(data.get_no_optimizado())
            if data.get_id() % 2 == 0:
                file_content += "<td bgcolor=\"LightSalmon1\">" + \
                    str(data.get_id()) + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + valor + \
                    "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + data.get_optimizado() + \
                    "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + \
                    data.get_regla() + "</td>\n"
            else:
                file_content += "<td bgcolor=\"yellow\">" + \
                    str(data.get_id()) + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + valor + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + \
                    data.get_optimizado() + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + \
                    data.get_regla() + "</td>\n"
            file_content += '</tr>\n\r'
        file_content += "</table>\n"
        file_content += ">]\n\r}"
        return file_content
    # END---------------------- Report -------------------------

    def relIntoWord(self, cadena):
        cadena = cadena.replace('==', 'EQUALS')
        cadena = cadena.replace('!=', 'NON_EQUALS')
        cadena = cadena.replace('>', 'MAYOR_QUE')
        cadena = cadena.replace('<', 'MENOR_QUE')
        cadena = cadena.replace('>=', 'MAYOR_IGUAL')
        cadena = cadena.replace('<=', 'MENOR_IGUAL')
        return cadena

# ----- Codigo no Optimizado ---           ---------- Optimizado ----
# ----- t1 = x*2 ---------------           ----------- t1 = x + x ---
# ----- t1 = x*2 ---------------           ----------- t1 = x + x ---
# ----- t1 = x*2 ---------------           ----------- t1 = x + x ---
# ----- t1 = x*2 ---------------           ----------- t1 = x + x ---
# ----- t1 = x*2 ---------------           ----------- t1 = x + x ---
# ----- t1 = x*2 ---------------           ----------- t1 = x + x ---
