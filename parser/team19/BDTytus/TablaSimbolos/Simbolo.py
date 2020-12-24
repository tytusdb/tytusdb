class Simbolo:
    def __init__(self, column_name, data_type, size_type, table_name, pos_line, pos_colum, sql_instruction):
        self.column_name = column_name
        self.data_type = data_type
        self.size_type = size_type
        self.table_name = table_name
        self.pos_line = pos_line
        self.pos_colum = pos_colum
        self.sql_instruction = sql_instruction

    def get_html_table(self):
        size_type = self.size_type
        if size_type == 1998:
            if self.data_type == 'text':
                size_type = 'ilimitado'
            else:
                size_type = 'Enum Type'
        return '''             <tr>
                  <td>%s</td>
                  <td>%s</td>
                  <td>%s</td>
                  <td>%s</td>
                  <td>%s</td>
                  <td>%s</td>
                  <td>%s</td>
                </tr>''' % (self.column_name, self.data_type, str(size_type), self.table_name, str(self.pos_line), str(self.pos_colum), self.sql_instruction)