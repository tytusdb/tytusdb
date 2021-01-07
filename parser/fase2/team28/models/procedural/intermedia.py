from utils.analyzers.syntactic import parse as analize
from models.instructions.DML.select import Select
from models.instructions.DML.special_functions import format_df, format_table_list
from pandas import DataFrame
def parse(entrada):
    entrada = entrada.replace(";;", ";")
    output = analize(entrada)
    print("SALIDA CONSOLA ------------------------------------------------------------------------------")
    # print(output)
    console_output = None
    valor_return = None
    for inst in output:

        if isinstance(inst, Select):
            console_output = inst.process(0)

            if isinstance(console_output, DataFrame):
                valor_return = console_output
                console_output = format_df(console_output)
            elif isinstance(console_output, list):
                valor_return = console_output
                console_output = format_table_list(console_output)
            print("SALIDA DE EJECUCION  ------------------------------------------------------------------------")
            if console_output is not None:
                print(console_output)
            if len(valor_return) > 1:
                return valor_return[1][0]
            else:
                return valor_return
        else:
            console_output = inst.process(0)
            print("SALIDA DE EJECUCION  ------------------------------------------------------------------------")
            if console_output is not None:
                print(console_output)
            return console_output