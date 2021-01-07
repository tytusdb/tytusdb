from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from Fase1.analizer.statement.instructions.select.select import Select
from Fase1.analizer.abstract.instruction import envVariables
from Fase1.analizer import grammar
from Fase1.analizer.reports import BnfGrammar


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
                #print(r)
            else:
                r = v.execute(None)
                #print(r)
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
    global envVariables
    environments = envVariables
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
    envVariables = []
    return report
