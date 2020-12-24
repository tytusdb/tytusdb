from sys import path
from os.path import dirname as dir
from shutil import rmtree

path.append(dir(path[0]))

from analizer.abstract import instruction as inst
from analizer import grammar
from analizer.reports import BnfGrammar
from analizer.abstract.instruction import envVariables as environments


def execution(input):
    """
    docstring
    """
    querys = []
    messages = []
    result = grammar.parse(input)
    lexerErrors = grammar.returnLexicalErrors()
    syntaxErrors = grammar.returnSyntacticErrors()
    if len(lexerErrors) + len(syntaxErrors) == 0:
        for v in result:
            if isinstance(v, inst.Select) or isinstance(v, inst.SelectOnlyParams):
                r = v.execute(None)
                if r:
                    list_ = r[0].values.tolist()
                    labels = r[0].columns.tolist()
                    querys.append([labels, list_])
                else:
                    querys.append(None)
            else:
                r = v.execute(None)
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
        "symbols": symbols
    }
    symbols = symbolReport()
    print(symbols)
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
    print(obj)
    return obj


def astReport():
    grammar.InitTree()


def symbolReport():
    global environments
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
                symbol.type if not symbol.type else "Tabla",
                symbol.row,
                symbol.column,
            ]
            filas.append(r)

        for (key, symbol) in types.items():
            r = [key, key, str(symbol) if not symbol else "Columna", "-", "-"]
            filas.append(r)

        enc.append(filas)
        report.append(enc)
    return report


s = """ 
USE test*;
select *
from tbrol WHERE idrol > 0;
"""
r = """ 
USE test[];
select *
from tbrol WHERE idrol > 0;
"""
# parser(s)
# execution(r)
# BnfGrammar.grammarReport()