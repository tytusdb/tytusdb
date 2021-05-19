from sys import path
from os.path import dirname as dir
from numpy.lib.arraysetops import isin
from prettytable import PrettyTable

path.append(dir(path[0]))

from Parser.analizer.statement.instructions.select.select import Select
from Parser.analizer.statement.functions.call import FunctionCall, TYPE
from Parser.analizer.statement.functions.extract import ExtractDate
from Parser.analizer.statement.functions.part import DatePart
from Parser.analizer.statement.expressions.primitive import Primitive
from Parser.analizer.abstract import instruction
from Parser.analizer import grammar
from Parser.analizer.reports import BnfGrammar
import pandas as pd
from Parser.analizer.typechecker.Metadata import File


def execution(input):
    """
    docstring
    """
    querys = []
    messages = []
    result = grammar.parse(input)
    lexerErrors = grammar.returnLexicalErrors()
    syntaxErrors = grammar.returnSyntacticErrors()
    if len(lexerErrors) + len(syntaxErrors) == 0 and result:
        for v in result:
            if isinstance(v, Select):
                r = v.execute(None)
                if r:
                    list_ = r[0].values.tolist()
                    labels = r[0].columns.tolist()
                    querys.append([labels, list_])
                    messages.append("Select ejecutado con exito.")
                else:
                    querys.append(None)
                    messages.append("Error: Select.")
            else:
                r = v.execute(None)
                print(r)
                messages.append(r)
    semanticErrors = grammar.returnSemanticErrors()
    PostgresErrors = grammar.returnPostgreSQLErrors()
    symbols = symbolReport()
    indexes = indexReport()
    obj = {
        "messages": messages,
        "querys": querys,
        "lexical": lexerErrors,
        "syntax": syntaxErrors,
        "semantic": semanticErrors,
        "postgres": PostgresErrors,
        "symbols": symbols,
        "indexes": indexes,
        "functions": [],
    }
    printTable_PT(querys)
    astReport()
    return obj


def parser(input):
    """
    docstring
    """
    grammar.parse(input)
    lexerErrors = grammar.returnLexicalErrors()
    syntaxErrors = grammar.returnSyntacticErrors()
    obj = {
        "lexical": lexerErrors,
        "syntax": syntaxErrors,
    }
    astReport()
    BnfGrammar.grammarReport()
    return obj


def astReport():
    grammar.InitTree()


def symbolReport():
    environments = instruction.envVariables
    report = []
    for env in environments:
        vars = env.variables
        types = env.types
        enc = [["Alias", "Nombre", "Tipo", "Fila", "Columna"]]
        filas = []
        for (key, symbol) in vars.items():
            r = [
                key,
                symbol.value,
                symbol.type if symbol.type else "Tabla",
                symbol.row,
                symbol.column,
            ]
            filas.append(r)
        for (key, type_) in types.items():
            r = [key, key, str(type_.name) if type_ else "Columna", "-", "-"]
            filas.append(r)
        enc.append(filas)
        report.append(enc)
    instruction.envVariables = list()
    return report


def selectFirstValue(input):
    """
    Funcion para obtener el primer valor de un select
    """
    result = grammar.parse(input)
    if len(result) > 1:
        result[0].execute(None)
        type_ = result[1].params[0].temp
        result = result[1].execute(None)
        df = result[0]
        types = result[1]
        if df.empty:
            if types[type_] == TYPE.STRING:
                return ""
            elif types[type_] == TYPE.NUMBER:
                return 0
            if types[type_] == TYPE.BOOLEAN:
                return "False"
            return ""
        if isinstance(df, pd.core.series.Series):
            df = df.iloc[0]
        else:
            df = df.iloc[0].iloc[0]
    else:
        df = result[0].execute(None)[0].iloc[0].iloc[0]
    return df


def indexReport():
    index = File.importFile("Index")
    enc = [["Nombre", "Tabla", "Unico", "Metodo", "Columnas"]]
    filas = []
    for (name, Index) in index.items():
        columns = ""
        for column in Index["Columns"]:
            columns += (
                ", " + column["Name"] + " " + column["Order"] + " " + column["Nulls"]
            )
        filas.append(
            [name, Index["Table"], Index["Unique"], Index["Method"], columns[1:]]
        )
    enc.append(filas)
    return enc


def invokeFunction(id, *params):
    temp = None
    list_ = params
    params = []
    for p in list_:
        if isinstance(p, str):
            p = p.strip('"')
            p = p.strip("'")
        params.append(p)
    if id == "extract":
        temp = ExtractDate(params[0], params[1], params[2], 0, 0)
        temp = temp.execute(None)
    elif id == "date_part":
        temp = DatePart(params[0], params[1], params[2], 0, 0)
        temp = temp.execute(None)
    else:
        parameters = []
        for p in params:
            parameters.append(Primitive(TYPE.NULL, p, p, 0, 0))
        temp = FunctionCall(id, parameters, 0, 0)
        temp = temp.execute(None)
    if temp:
        return temp.value
    return temp


def printTable_PT(tables):
    if tables != None:
        i = 0
        for table in tables:
            i += 1
            if table != None:
                table_pt = PrettyTable()
                fill_table(table[0], table[1], table_pt)
                print(table_pt)
            else:
                print("Error: Consulta sin resultado")


def fill_table(columns, rows, table):
    table.field_names = columns
    table.add_rows(rows)
