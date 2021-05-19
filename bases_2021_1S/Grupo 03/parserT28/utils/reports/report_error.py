from parserT28.controllers.error_controller import ErrorController


class ReportError:
    def __init__(self):
        pass

    def get_report(self):
        file_content = ''
        file_content += "digraph D{\n\t"
        file_content += 'graph [pad="0.8", nodesep="0.8", ranksep="1", bgcolor = grey77, label=\"Report Of Errors\"];\n'
        file_content += 'node [shape=note]\n'
        file_content += 'rankdir=LR;\n'
        file_content += 'arset [label=<\n'
        file_content += '<table border="0" cellborder="1" color="green1" cellspacing="0">\n'
        file_content += "<tr> <td colspan=\"6\" bgcolor=\"green1\"> Reporte De Errores </td> </tr>\n"
        file_content += "<tr>\n\t <td bgcolor=\"paleturquoise1\"> ID </td>\n <td  bgcolor=\"paleturquoise1\"> Type of Error </td>\n <td bgcolor=\"paleturquoise1\"> ID Error </td>\n"
        file_content += '<td bgcolor=\"paleturquoise1\"> Description </td>\n  <td bgcolor=\"paleturquoise1\"> Row </td>\n <td bgcolor=\"paleturquoise1\"> Column </td> </tr>\n\r'

        for data in ErrorController().getList():
            file_content += '<tr>\n\t'
            if data.get_id() % 2 == 0:
                file_content += "<td bgcolor=\"LightSalmon1\">" + \
                    str(data.get_id()) + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + data.get_type() + \
                    "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + data.get_id_error() + \
                    "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + \
                    data.get_description() + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + \
                    str(data.get_row()) + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + \
                    str(data.get_column()) + "</td>\n"
            else:
                file_content += "<td bgcolor=\"yellow\">" + \
                    str(data.get_id()) + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + data.get_type() + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + \
                    data.get_id_error() + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + \
                    data.get_description() + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + \
                    str(data.get_row()) + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + \
                    str(data.get_column()) + "</td>\n"
            file_content += '</tr>\n\r'
        file_content += "</table>\n"
        file_content += ">]\n\r}"
        return file_content
