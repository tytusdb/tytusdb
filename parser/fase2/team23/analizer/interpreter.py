from sys import path
from os.path import dirname as dir
from shutil import rmtree
import pickle

path.append(dir(path[0]))

from analizer.abstract import instruction as inst
from analizer import grammar
from analizer.reports import BnfGrammar
from analizer.symbol.environment import Environment
from prettytable import PrettyTable


global_env = Environment()

def getc3d(input):
    """
    docstring
    """
    querys = []
    messages = []
    result = grammar.parse(input)
    lexerErrors = grammar.returnLexicalErrors()
    syntaxErrors = grammar.returnSyntacticErrors()
    tabla = Environment()
    if len(lexerErrors) + len(syntaxErrors) == 0 and result:

        for v in result:
            if isinstance(v, inst.FunctionPL) or isinstance(v, inst.ProcedureStmt):
                v.c3d(tabla)

        tabla.codigo += "def main():\n"
        tabla.conta_exec = 0

        for v in result:
            if isinstance(v, inst.Select) or isinstance(v, inst.SelectOnlyParams):
                r = v.c3d(tabla)
                if r:
                    list_ = r[0].values.tolist()
                    labels = r[0].columns.tolist()
                    querys.append([labels, list_])
                else:
                    querys.append(None)

            elif isinstance(v, inst.FunctionPL) or isinstance(v, inst.ProcedureStmt):
                cont = tabla.conta_exec
                tabla.codigo += "".join(tabla.count_tabs) + "C3D.pila = "+str(cont)+"\n"
                tabla.codigo += "".join(tabla.count_tabs) + "C3D.ejecutar() #Llamada\n\n"
                tabla.conta_exec+=1

            else:
                r = v.c3d(tabla)
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
        "codigo": tabla.codigo,
    }
    astReport()
    BnfGrammar.grammarReport()
    return obj

def execution(input):
    """
    docstring
    """
    querys = []
    messages = []
    result = grammar.parse(input)
    with open("obj.pickle", "wb") as f:
        pickle.dump(result, f)
    lexerErrors = grammar.returnLexicalErrors()
    syntaxErrors = grammar.returnSyntacticErrors()
    tabla = global_env
    cont = 0
    if len(lexerErrors) + len(syntaxErrors) == 0 and result:
        for v in result:
            if isinstance(v, inst.Select) or isinstance(v, inst.SelectOnlyParams):
                r = v.execute(tabla)
                if r:
                    list_ = r[0].values.tolist()
                    labels = r[0].columns.tolist()
                    querys.append([labels, list_])
                    salidaTabla = PrettyTable()
                    encabezados = labels
                    salidaTabla.field_names = encabezados
                    cuerpo = list_
                    salidaTabla.add_rows(cuerpo)
                    print(salidaTabla)
                    print("\n")
                    print("\n")
                else:
                    querys.append(None)
            elif isinstance(v, inst.FunctionPL) or isinstance(v, inst.ProcedureStmt):
                v.pos = cont
                r = v.execute(tabla)
                messages.append(r)
            else:
                r = v.execute(tabla)
                messages.append(r)
            cont+=1
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
    environments = inst.envVariables
    report = []
    for env in environments:
        vars = env.variables
        types = env.types
        enc = [["Alias", "Nombre", "Tipo", "Columnas Formadas", "Consideraciones", "Fila", "Columna"]]
        filas = []
        for (key, symbol) in vars.items():
            #print(symbol.type)
            r = [
                key,
                symbol.value,
                symbol.type,
                symbol.col_creada,
                symbol.cons,
                symbol.row,
                symbol.column
            ]
            filas.append(r)

        for (key, symbol) in types.items():
            r = [key, key, str(symbol) if not symbol else "Columna", "-", "-"]
            filas.append(r)
        enc.append(filas)
        report.append(enc)
    inst.envVariables = []
    return report


# BnfGrammar.grammarReport()