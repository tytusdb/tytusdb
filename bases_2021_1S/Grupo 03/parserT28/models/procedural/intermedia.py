from parserT28.utils.analyzers.syntactic import parse as analize
from parserT28.models.instructions.DML.select import Select
from parserT28.models.instructions.DML.special_functions import format_df, format_table_list
from parserT28.controllers.symbol_table import SymbolTable
from parserT28.utils.reports.tchecker_report import TypeCheckerReport
from parserT28.utils.reports.symbol_report import SymbolTableReport
from pandas import DataFrame
import os


def parse(entrada):
    entrada = entrada.replace(";;", ";")
    output = analize(entrada)
    print("ENTRADA: ", entrada)
    print("SALIDA CONSOLA ------------------------------------------------------------------------------")
    # print(output)
    console_output = None
    valor_return = None
    for inst in output:

        if isinstance(inst, Select):
            console_output = inst.process(0)

            if isinstance(console_output, DataFrame):
                valor_return = console_output.values.tolist()
                # print("dataframe to list", valor_return)
                console_output = format_df(console_output)
            elif isinstance(console_output, list):
                valor_return = console_output
                console_output = format_table_list(console_output)
            print(
                "SALIDA DE EJECUCION  ------------------------------------------------------------------------")
            if console_output is not None:
                print(console_output)
            if len(valor_return) > 1:
                return valor_return[1][0]
            else:
                return valor_return[0][0]
        else:
            console_output = inst.process(0)
            print(
                "SALIDA DE EJECUCION  ------------------------------------------------------------------------")
            if console_output is not None:
                print(console_output)
    return console_output


def report_symbols_windows():
    try:
        report = open('symbolTableIndexes.dot', 'w')
        report.write(SymbolTableReport().generateReport())
        report.close()
        os.system('dot -Tpdf symbolTableIndexes.dot -o symbolTableIndexes.pdf')
        os.startfile('symbolTableIndexes.pdf')
    except:
        print("INSTALA GRAPHVIZ!!!!")


def report_typeChecker_windows():
    try:
        report = open('typeChecker.dot', 'w')
        report.write(TypeCheckerReport().generateReport())
        report.close()
        os.system('dot -Tpdf typeChecker.dot -o typeChecker.pdf')
        os.startfile('typeChecker.pdf')
    except:
        print("INSTALA GRAPHVIZ!!!!")
