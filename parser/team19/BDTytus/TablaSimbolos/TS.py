
from TablaSimbolos.Simbolo import Simbolo


class TabladeSimbolos:
    def __init__(self):
        self.simbolos = []


    def insertar(self, column_name, data_type, size_type, table_name, pos_line, pos_colum, sql_instruction):
        simboloNuevo = Simbolo(column_name, data_type, size_type, table_name, pos_line, pos_colum, sql_instruction)
        if self.obtenerSimbolo(simboloNuevo) is None:
            self.simbolos.append(simboloNuevo)
            return True
        return False


    def obtenerSimbolo(self, simbolo):
        for simbolo_ in self.simbolos:
            if simbolo_.column_name == simbolo.column_name and simbolo_.data_type == simbolo.data_type and simbolo_.pos_colum == simbolo.pos_colum and simbolo_.pos_line == simbolo.pos_line and simbolo_.type.size_type == simbolo.size_type and simbolo_.sql_instruction == simbolo.sql_instruction:
                return simbolo
        return None

