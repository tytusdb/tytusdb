from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer.statement.instructions.select.select import Select
from analizer.abstract import instruction
from analizer import grammar  # GRAMATICA DE LA FASE 2
from analizer.gramaticaFase2 import getCodigo, parserTo3D
from analizer import gramaticaFase2
from analizer.reports import BnfGrammar


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
                print(r)
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
        enc = [["Nombre", "Valor", "Tipo", "Fila", "Columna"]]
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
        for (key, func) in env.functions.items():
            r = [key, "-", "Function " + str(func.type[0]), "-", "-"]
            filas.append(r)
        for key in env.procedures:
            r = [key, "-", "Procedure", "-", "-"]
            filas.append(r)
        enc.append(filas)
        report.append(enc)
    instruction.envVariables = list()
    return report

def generar_codigo_3d(entrada):
    parserTo3D(entrada)
    lErrors = gramaticaFase2.returnLexicalErrors()
    sErrors = gramaticaFase2.returnSyntacticErrors()
    semanticErrors = gramaticaFase2.returnSemanticErrors()
    symbols = symbolReport()
    obj = {
        "err_lexicos": lErrors,
        "err_sintacticos": sErrors,
        "semantic": semanticErrors,
        "symbols": symbols,
    }
    astReport()
    #BnfGrammar.grammarReport2()
    return obj
