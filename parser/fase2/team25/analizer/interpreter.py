from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from analizer.statement.instructions.select.select import Select
from analizer.abstract import instruction
from analizer import grammar  # GRAMATICA DE LA FASE 2
from analizer.gramaticaFase2 import getCodigo, parserTo3D , InitTree
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
    #BnfGrammar.grammarReport()
    try:
        if len(querys) == 1:
            if len(querys[0][1]) == 1:
                if len(querys[0][1][0]) == 1:
                    return querys[0][1][0][0]
    except:
        return obj
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
            #Parametros
            for (llave,param) in func.params:
                s = [llave, "-", "Param " + str(param[0]) , "-", "-"]
                filas.append(s)
        for (key, proc) in env.procedures.items():
            r = [key, "-", "Procedure", "-", "-"]
            filas.append(r)
            #Parametros
            for (llave,param) in proc.params:
                s = [llave, "-", "Param " + str(param[0]) , "-", "-"]
                filas.append(s)
        enc.append(filas)
        report.append(enc)
    instruction.envVariables = list()
    return report

from analizer.statement.pl.index import indexEnv
from analizer.statement.pl.procedure import envProcedure
from analizer.statement.pl.function import envFunction
from analizer.c3d.codigo3d import instancia_codigo3d
from analizer.reports.AST import AST
def generar_codigo_3d(entrada):
    ast=parserTo3D(entrada)
    graficador = AST()
    try:
        graficador.makeAst(ast.dot())
    except:
        pass
    #Ejectamos el c3d de cada funcion, procedimiento
    for func in envFunction.functions.values():
        func.generate3d(None,instancia_codigo3d)
    for proc in envProcedure.procedures.values():
        proc.generate3d(None,instancia_codigo3d)

    lErrors = gramaticaFase2.returnLexicalErrors()
    sErrors = gramaticaFase2.returnSyntacticErrors()
    semanticErrors = gramaticaFase2.returnSemanticErrors()
    #Agrega los especiales
    instruction.envVariables.append(indexEnv)
    instruction.envVariables.append(envFunction)
    instruction.envVariables.append(envProcedure)
    symbols = symbolReport()
    obj = {
        "err_lexicos": lErrors,
        "err_sintacticos": sErrors,
        "semantic": semanticErrors,
        "symbols": symbols,
    }
    BnfGrammar.grammarReport2() # ! DESCOMENTAR EN EL COMMIT FINAL :v
    return obj
