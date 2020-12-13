class ReportError:
    def __init__(self, list_errors):
        self.list_errors = list_errors

    def get_report(self):
        file_content = ''
        values = self.list_errors.head_value
        file_content += "digraph D{\n\t"
        file_content += 'graph [pad="0.8", nodesep="0.8", ranksep="1", bgcolor = grey77, label=\"Report Of Errors\"];\n'
        file_content += 'node [shape=note]\n'
        file_content += 'rankdir=LR;\n'
        file_content += 'arset [label=<\n'
        file_content += '<table border="0" cellborder="1" color="green1" cellspacing="0">\n'
        file_content += "<tr> <td colspan=\"6\" bgcolor=\"green1\"> Reporte De Errores </td> </tr>\n"
        file_content += "<tr>\n\t <td bgcolor=\"paleturquoise1\"> ID </td>\n <td  bgcolor=\"paleturquoise1\"> Type of Error </td>\n <td bgcolor=\"paleturquoise1\"> ID Error </td>\n"
        file_content += '<td bgcolor=\"paleturquoise1\"> Description </td>\n  <td bgcolor=\"paleturquoise1\"> Row </td>\n <td bgcolor=\"paleturquoise1\"> Column </td> </tr>\n\r'
        while values is not None:
            file_content += '<tr>\n\t'
            if values.data.get_id() % 2 == 0:
                file_content += "<td bgcolor=\"LightSalmon1\">" + str(values.data.get_id()) + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + values.data.get_type() + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + values.data.get_id_error() + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + values.data.get_description() + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + str(values.data.get_row()) + "</td>\n"
                file_content += "<td bgcolor=\"LightSalmon1\">" + str(values.data.get_column()) + "</td>\n"
            else:
                file_content += "<td bgcolor=\"yellow\">" + str(values.data.get_id()) + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + values.data.get_type() + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + values.data.get_id_error() + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + values.data.get_description() + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + str(values.data.get_row()) + "</td>\n"
                file_content += "<td bgcolor=\"yellow\">" + str(values.data.get_column()) + "</td>\n"
            file_content += '</tr>\n\r'
            values = values.next
        file_content += "</table>\n"
        file_content += ">]\n\r}"
        return file_content
    

    # def get_content_report(self):
    #     file_content = ""
    #     values = self.list_errors.head_value
    #     while values is not None:
    #         file_content += "<TR>"
    #         file_content += "<TH>" + str(values.data.get_id()) + "</TH>"
    #         file_content += "<TH>" + values.data.get_type() + "</TH>"
    #         file_content += "<TH>" + values.data.get_id_error() + "</TH>"
    #         file_content += "<TH>" + values.data.get_description() + "</TH>"
    #         file_content += "<TH>" + str(values.data.get_row()) + "</TH>"
    #         file_content += "<TH>" + str(values.data.get_column()) + "</TH>"
    #         file_content += "</TR>"
    #         values = values.next
    #     return file_content
