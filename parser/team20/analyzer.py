from grammar import *
from analyzer_result import *

class analyzer:

    def __init__(self):
        i=0

    def analyze(self, input_text):
        parse_result_ = parse(input_text)
        printed_error_table = self.get_error_table_printing(parse_result_.Error_Table)
        analyzer_result_ = analyzer_result(parse_result_.AST_Tree, "", parse_result_.Error_Table, printed_error_table)
        return analyzer_result_

    def get_error_table_printing(self, error_table):
        error_table_string = ""
        error_table_string += "ERROR TABLE\n"
        error_table_string += "NUMBER, TYPE, LEXEME, LINE, COLUMN\n"
        if len(error_table)==0:
            error_table_string += "empty"
        i = 0
        while i < len(error_table):
            error_table_string += str(int(i)+1) + ", "
            error_table_string += error_table[i].type + ", "
            error_table_string += error_table[i].data + ", "
            error_table_string += str(error_table[i].row) + ", "
            error_table_string += str(error_table[i].column)
            if (int(i)+1) != len(error_table):
                error_table_string += "\n"
            i += 1
        return error_table_string