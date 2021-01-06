from sys import path
from os.path import dirname as dir
from prettytable import PrettyTable

path.append(dir(path[0]))

from analizer.statement.instructions.select.select import Select
from analizer.abstract import instruction
from analizer import grammar
from analizer.reports import BnfGrammar
import pandas as pd
from analizer.typechecker.Metadata import File


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
                # print(r[0].iloc[0].iloc[0])
                # print(r)
            else:
                r = v.execute(None)
                print(r)
                messages.append(r)
    semanticErrors = grammar.returnSemanticErrors()
    PostgresErrors = grammar.returnPostgreSQLErrors()
    symbols = symbolReport()
    obj = {
        "messages": messages,
        "querys": querys,
        "lexical": lexerErrors,
        "syntax": syntaxErrors,
        "semantic": semanticErrors,
        "postgres": PostgresErrors,
        "symbols": symbols,
    }
    printTable_PT(querys)
    astReport()
    BnfGrammar.grammarReport()
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
        result = result[0].execute(None)
        result = result[1].execute(None)[0].iloc[0].iloc[0]
    else:
        result = result[0].execute(None)[0].iloc[0].iloc[0]
    return result


print(selectFirstValue("SELECT EXTRACT(HOUR FROM TIMESTAMP '2001-02-16 20:38:40');"))


def indexReport():
    index = File.importFile("Index")
    enc = [["Nombre", "Tabla", "Unico", "Metodo", "Columnas"]]
    filas = []
    for (name, Index) in index.items():
        columns = ""
        for column in Index["Columns"]:
            columns += ", " + column["Name"]
        filas.append(
            [name, Index["Table"], Index["Unique"], Index["Method"], columns[1:]]
        )
    enc.append(filas)
    return [enc]


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
