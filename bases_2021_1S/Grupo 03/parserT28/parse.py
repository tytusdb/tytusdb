from pandas.core.frame import DataFrame

from parserT28.views.data_window import DataWindow
from parserT28.models.instructions.DML.select import Select
from parserT28.controllers.error_controller import ErrorController
from parserT28.utils.analyzers.syntactic import parse


def execution(input):
    querys = []
    messages = []
    DataWindow().clearProperties()
    result = parse(input)
    errors = ErrorController().getList()

    if len(ErrorController().getList()) == 0:
        for inst in result:
            if isinstance(inst, Select):
                result = inst.process(0)
                if isinstance(result, DataFrame):
                    DataWindow().format_df(result)
                    querys.append([DataWindow().headers, DataWindow().rows])
                elif isinstance(result, list):
                    DataWindow().format_table_list(result)
                    querys.append([DataWindow().headers, [DataWindow().rows]])
            else:
                inst.process(0)
                querys.append([DataWindow().headers, DataWindow().rows])
            messages.append(DataWindow().data)

    obj = {
        "messages": messages,
        "querys": querys,
        "lexical": errors
    }
    return obj
