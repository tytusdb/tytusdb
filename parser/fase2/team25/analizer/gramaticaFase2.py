from analizer.statement.pl.execute import Execute
from sys import path
from os.path import dirname as dir
import re
path.append(dir(path[0]))
import ply.yacc as yacc
from analizer.tokens import *
from analizer.reports import Nodo
from analizer.c3d.codigo3d import Codigo3d, instancia_codigo3d

# Construccion del analizador léxico
import ply.lex as lex

lexer = lex.lex()
# Asociación de operadores y precedencia
listInst = [] # esta es para el arbol , ya estaba en el proyecto
repGrammar = []
count_ins = 0
entrada = ''

syntax_errors = list()
PostgreSQL = list()

precedence = (
    ("left", "R_UNION", "R_INTERSECT", "R_EXCEPT"),
    ("right", "R_NOT"),
    ("left", "R_AND", "R_OR"),
    (
        "left",
        "R_BETWEEN",
        "R_IS",
    ),
    (
        "left",
        "S_IGUAL",
        "OL_DISTINTODE",
        "OL_MAYORQUE",
        "OL_MENORQUE",
        "OL_MAYORIGUALQUE",
        "OL_MENORIGUALQUE",
    ),
    ("left", "OC_CONCATENAR"),
    ("left", "O_SUMA", "O_RESTA"),
    ("left", "O_PRODUCTO", "O_DIVISION", "O_MODULAR"),
    ("right", "UO_SUMA", "UO_RESTA"),
    ("left", "O_EXPONENTE"),
)

# Definición de la gramática

from analizer.abstract.expression import TYPE
from analizer.abstract.expression import returnExpErrors
import analizer.modules.expressions as expression
import analizer.abstract.instruction as instruction
import analizer.modules.instructions as instruction2
from analizer.statement.pl.sentenciaIf import IfSimple, If_Elseif
from analizer.statement.pl.sentenciaReturn import  Return_
from analizer.statement.pl.codeblock import CodeBlock
from analizer.statement.pl.instruccionesF1 import F1
from analizer.statement.pl.case import Case, CaseWhen
from analizer.statement.pl.asignacion import Asignacion
from analizer.statement.pl.declaration import Declaration
from analizer.statement.pl.procedure import Procedure, dropProc
from analizer.statement.pl.function import Function, dropFunc
from analizer.statement.pl.index import Index, dropIndex, alterIndex, alterIndexChange
from analizer.statement.pl.raise_print import Raise
from analizer.statement.pl.f2Statement import f2Statement
from analizer.statement.pl.f1Statement import f1Statement
from analizer.statement.pl.arbolGeneral import ArbolGeneral

import analizer.symbol.c3dSymbols as SymbolTable
from analizer.statement.instructions.select.select import Select
def p_init(t):
    """init : stmtList"""
    t[0] = t[1]
    repGrammar.append(t.slice)
    return t[0]




def p_stmt_list(t):
    """stmtList : stmtList stmt"""
    t[1].append(t[2])
    t[0] = t[1]
    repGrammar.append(t.slice)






def p_stmt_u(t):
    """stmtList : stmt"""
    t[0] = [t[1]]
    repGrammar.append(t.slice)



def p_stmt(t):#INSTRUCCIONES
    """
    stmt : fase1_stmt
        | fase2_stmt
    """
    #listInst.append(t[1].dot())
    try:
        t[0] = t[1]
    except:
        return
    repGrammar.append(t.slice)


def p_fase1_stmt(t):
    """
    fase1_stmt : showStmt S_PUNTOCOMA
        | alterStmt S_PUNTOCOMA
        | dropStmt S_PUNTOCOMA
        | insertStmt S_PUNTOCOMA
        | updateStmt S_PUNTOCOMA
        | deleteStmt S_PUNTOCOMA
        | truncateStmt S_PUNTOCOMA
        | useStmt S_PUNTOCOMA
        | selectStmt S_PUNTOCOMA
        | dml_index S_PUNTOCOMA
    """
    #listInst.append(t[1].dot()) # * :v solo si queremos tener un nodo ins llamando a los demas nodos
    t[0] = t[1]
    if isinstance(t[0],Index):
        C3D_INSTRUCCIONES_SIN_EJECUCION(t)
    else:
        C3D_INSTRUCCIONES_FASE1(t)
    try:
        t[0] = f1Statement(row = t.slice[2].lineno, column = t.slice[2].lexpos, statement = t[1])
    except:
        return
    # SOLO CUENTA LOS PUNTO Y COMA
    repGrammar.append(t.slice)

    global count_ins
    count_ins += 1



def p_create_index(t):
    """
    dml_index : R_CREATE R_INDEX ID R_ON ID S_PARIZQ ID orderOpts orderNull S_PARDER whereCl
        | R_CREATE R_INDEX ID R_ON ID R_USING R_HASH S_PARIZQ ID S_PARDER
        | R_CREATE R_INDEX ID R_ON ID S_PARIZQ ID S_COMA ID S_PARDER
        | R_CREATE R_INDEX ID R_ON ID S_PARIZQ funcCall S_PARDER
        | R_CREATE R_UNIQUE R_INDEX ID R_ON ID S_PARIZQ idList S_PARDER
    """
    repGrammar.append(t.slice)
    if t[2] == 'UNIQUE':
            t[0] = Index(t[4], t[6], t[8], t[2], t.slice[1].lineno, t.slice[1].lexpos)
    else:
        if len(t) == 11:
            if t[8].upper() == 'HASH':
                t[0] = Index(t[3], t[5], t[9], None, t.slice[1].lineno, t.slice[1].lexpos)
            else:
                t[0] = Index(t[3], t[5], [t[7],t[9]], None, t.slice[1].lineno, t.slice[1].lexpos)
        else:
            if t[8] == '(':
                t[0] = Index(t[3], t[5], t[9], None, t.slice[1].lineno, t.slice[1].lexpos)
            else:
                t[0] = Index(t[3], t[5], t[7], None, t.slice[1].lineno, t.slice[1].lexpos)
    t[0].execute(None)

def p_drop_index(t):
    """
    dml_index : R_DROP R_INDEX ID
    """
    dropIndex(t[3])
    repGrammar.append(t.slice)
    C3D_INSTRUCCIONES_SIN_EJECUCION(t)

def p_alter_index(t):
    """
    dml_index : R_ALTER R_INDEX R_IF R_EXISTS ID R_ALTER R_COLUMN INTEGER
        | R_ALTER R_INDEX R_IF R_EXISTS ID R_ALTER INTEGER 
        | R_ALTER R_INDEX ID R_ALTER R_COLUMN INTEGER
        | R_ALTER R_INDEX ID R_ALTER INTEGER
    """
    if len(t) == 9:
        alterIndex(t[5],t[8], True)
    elif len(t) == 8:
        alterIndex(t[5],t[7], True)
    elif len(t) == 7:
        alterIndex(t[3],t[6])
    else:
        alterIndex(t[3],t[5])
    repGrammar.append(t.slice)
    C3D_INSTRUCCIONES_SIN_EJECUCION(t)

def p_alter_index_name(t):
    """
    dml_index : R_ALTER R_INDEX R_IF R_EXISTS ID R_ALTER R_COLUMN ID ID
        | R_ALTER R_INDEX R_IF R_EXISTS ID R_ALTER ID ID
        | R_ALTER R_INDEX ID R_ALTER R_COLUMN ID ID
        | R_ALTER R_INDEX ID R_ALTER ID ID
    """
    repGrammar.append(t.slice)
    if len(t) == 10:
        alterIndexChange(t[5],t[8], t[9], True)
    elif len(t) == 9:
        alterIndexChange(t[5],t[7], t[8], True)
    elif len(t) == 8:
        alterIndexChange(t[3],t[6], t[7])
    else:
        alterIndexChange(t[3],t[5], t[6])

def p_fase2_stmt(t):
    '''
    fase2_stmt : createStmt  S_PUNTOCOMA
                | llamadaProcedimiento_o_funcion S_PUNTOCOMA
                | pl_drop S_PUNTOCOMA

    '''
    #  Execute dropProc,dropFunc
    t[0] = f2Statement(row = t.slice[2].lineno, column = t.slice[2].lexpos, statement = t[1])
    repGrammar.append(t.slice)
    global count_ins
    count_ins += 1


# region FASE 2
# Indices
def p_llamadaProcedimiento_o_funcion(t):# esta aparte porque va directo al MAIN
    '''llamadaProcedimiento_o_funcion : R_EXECUTE ID S_PARIZQ paramsList S_PARDER
        | R_EXECUTE ID S_PARIZQ S_PARDER
        | R_EXECUTE ID
        | R_EXECUTE STRING'''
    repGrammar.append(t.slice)
    if len(t) == 6:
        t[0] = Execute(t[2], t[4], t.slice[2].lineno, t.slice[2].lexpos)
    else:
        t[0] = Execute(t[2], [], t.slice[2].lineno, t.slice[2].lexpos) # NO USAR EL GENERATE3D ACA porque ese se usara para manejar los excute internos en funciones y procedimientos
    t[0].generate3d(None, instancia_codigo3d,True)


#_----------------------------------------------- FUNCION
def p_drop_procedure_and_functions2(t):
    '''
    pl_drop : R_DROP R_FUNCTION R_IF R_EXISTS detalle_drop
            | R_DROP R_FUNCTION detalle_drop
    '''
    repGrammar.append(t.slice)
    if len(t) == 7:
        dropFunc(t[5], True)
    else:
        dropFunc(t[3])

def p_drop_procedure_and_functions(t):
    '''
    pl_drop : R_DROP R_PROCEDURE R_IF R_EXISTS detalle_drop
            | R_DROP R_PROCEDURE detalle_drop
    '''
    repGrammar.append(t.slice)
    if len(t) == 7:
        dropProc(t[5], True)
    else:
        dropProc(t[3])

def p_detalle_drop(t):
    '''
    detalle_drop : detalle_drop S_COMA drop_argumentos
                | drop_argumentos
    '''
    repGrammar.append(t.slice)
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_drop_argumentos(t):
    '''
    drop_argumentos : ID S_PARIZQ  typeParamsList S_PARDER
                    | ID S_PARIZQ  S_PARDER
                    | ID
    '''
    repGrammar.append(t.slice)
    if len(t) == 5:
        t[0] = (t[1],t[3])
    elif len(t) == 4:
        t[0] = (t[1],[])
    else:
        t[0] = t[1]


#* def p_raise_main(t): NO PUEDE VENIR EN EL MAIN 
#     '''
#     raise_main : R_RAISE R_NOTICE STRING S_COMA datatype
#             | R_RAISE  STRING S_COMA datatype
#     '''
#     repGrammar.append(t.slice)
#     if len(t) == 6:
#         t[0] = Raise(t[3],t[5] , t.slice[1].lineno, t.slice[1].lexpos , True)
#         t[0].generate3dToMain(0,instancia_codigo3d)
#     elif len(t) == 5:
#         t[0] = Raise(string1 = t[2], string2 = t[4] , row = t.slice[1].lineno, column = t.slice[1].lexpos)
#         t[0].generate3dToMain(0,instancia_codigo3d)
#     else:
#         print('no entro en len(t)')
#     #ambos son un print

def p_raise_procedural(t):
    '''
    raise_procedural : R_RAISE R_NOTICE STRING S_COMA datatype
            | R_RAISE  STRING S_COMA datatype
    '''
    repGrammar.append(t.slice)
    if len(t) == 6:
        t[0] = Raise(t[3],t[5] , t.slice[1].lineno, t.slice[1].lexpos , True)
    elif len(t) == 5:
        t[0] = Raise(string1 = t[2], string2 = t[4] , row = t.slice[1].lineno, column = t.slice[1].lexpos)
    else:
        print('no entro en len(t)')
    #ambos son un print



# Procedimientos
def p_createopts_procedure(t):
    """
    createOpts : R_PROCEDURE ID S_PARIZQ S_PARDER R_AS S_DOBLEDOLAR codeBlock S_PUNTOCOMA S_DOBLEDOLAR R_LANGUAGE R_PLPGSQL
    """
    t[0] = Procedure(t[2],[],t[7], t.slice[2].lineno, t.slice[2].lexpos)
    t[0].execute(None)
    global count_ins # por el token S_PUNTOCOMA necesitaba agregar esto :v
    count_ins += 1
    repGrammar.append(t.slice)

def p_createopts_procedure_params(t):
    """
    createOpts : R_PROCEDURE ID S_PARIZQ typeParamsList S_PARDER R_AS S_DOBLEDOLAR codeBlock S_PUNTOCOMA S_DOBLEDOLAR R_LANGUAGE R_PLPGSQL
    """
    t[0] = Procedure(t[2],t[4],t[8], t.slice[2].lineno, t.slice[2].lexpos)
    t[0].execute(None)
    global count_ins
    count_ins += 1
    repGrammar.append(t.slice)

def p_createopts_function(t):
    """
    createOpts : R_FUNCTION ID S_PARIZQ S_PARDER R_RETURNS types R_AS S_DOBLEDOLAR codeBlock S_PUNTOCOMA S_DOBLEDOLAR R_LANGUAGE R_PLPGSQL
    """
    t[0] = Function(t[2],t[6],[],t[9], t.slice[2].lineno, t.slice[2].lexpos)
    t[0].execute(None)
    global count_ins
    count_ins += 1
    repGrammar.append(t.slice)

def p_createopts_function_params(t):
    """
    createOpts : R_FUNCTION ID S_PARIZQ typeParamsList S_PARDER R_RETURNS types R_AS S_DOBLEDOLAR codeBlock S_PUNTOCOMA S_DOBLEDOLAR R_LANGUAGE R_PLPGSQL
    """
    t[0] = Function(t[2],t[7],t[4],t[10], t.slice[2].lineno, t.slice[2].lexpos)
    t[0].execute(None)
    global count_ins
    count_ins += 1
    repGrammar.append(t.slice)

def p_typeParamsList(t):
    """
    typeParamsList : typeParamsList S_COMA typeParam
        | typeParam
    """
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]
    repGrammar.append(t.slice)

def p_typeParam(t):
    """
    typeParam : ID types
    """
    t[0] = (t[1],t[2])
    repGrammar.append(t.slice)

# Instrucciones de los procedimentos
def p_codeBlock(t):
    """
    codeBlock : R_DECLARE declarationList R_BEGIN plInstructions R_END
    | R_DECLARE declarationList list_declaraciones_declere R_BEGIN plInstructions R_END
    | R_BEGIN plInstructions R_END
    """
    if len(t) == 6:
        t[0] = CodeBlock(lista_instrucciones=t[4] , lista_declaraciones=t[2] , row=t.slice[1].lineno , column=t.slice[1].lexpos)
    elif len(t) == 7:
        for item in t[3]:
            t[2].append(item)
        # t[2].append(t[3])
        t[0] = CodeBlock(lista_instrucciones=t[5],lista_declaraciones=t[2], row=t.slice[1].lineno , column=t.slice[1].lexpos)
    else:
        t[0] = CodeBlock(lista_instrucciones=t[2] , row=t.slice[1].lineno , column=t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_declarationList(t):
    """
    declarationList : declarationList declaration
        | declaration
    """
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
    repGrammar.append(t.slice)

def p_declarationList_2(t):
    """
    list_declaraciones_declere : list_declaraciones_declere  R_DECLARE declarationList
        | R_DECLARE declarationList
    """
    if len(t) == 4:
        for item in t[3]:
            t[1].append(item)
        t[0] = t[1]
    else:
        t[0] = t[2]
    repGrammar.append(t.slice)

def p_declaration(t):
    """
    declaration : ID types S_PUNTOCOMA
        | ID types S_ASIGNACION expresion S_PUNTOCOMA
        | ID types S_IGUAL expresion S_PUNTOCOMA
    """
    if len(t)==6:
        #print('\t'+str(t[1])+' = '+str(t[4]))
        if isinstance( t[4] , Select): # PARA VALIDACION DEL SELECT
            t[4] = F1(t[4],C3D_INSTRUCCIONES_FASE1_CADENA(t,True), t.slice[1].lineno , t.slice[1].lexpos )
        t[0] = Declaration(t[1],t[2],t[4],t.slice[1].lineno,t.slice[1].lexpos)
    else:
        t[0] = Declaration(t[1],t[2],None,t.slice[1].lineno,t.slice[1].lexpos)

    global count_ins
    count_ins += 1
    repGrammar.append(t.slice)

def p_plInstructions(t):
    """
    plInstructions : plInstructions plInstruction
    | plInstruction
    """
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_plInstruction(t):
    """
    plInstruction : assignment S_PUNTOCOMA
    | executeStmt S_PUNTOCOMA
    | ifStmt S_PUNTOCOMA
    | caseStmt S_PUNTOCOMA
    | codeBlock S_PUNTOCOMA
    | returnStmt S_PUNTOCOMA
    | raise_procedural S_PUNTOCOMA
    """
    t[0]=t[1]

    global count_ins
    count_ins += 1
    repGrammar.append(t.slice)

def p_plInstruction2(t):# los separe solo para generar su codigo 3d diferente
    """
    plInstruction : insertStmt S_PUNTOCOMA
    | updateStmt S_PUNTOCOMA
    | deleteStmt S_PUNTOCOMA
    | selectStmt S_PUNTOCOMA
    """
    t[0] = F1(t[1],C3D_INSTRUCCIONES_FASE1_CADENA(t), t.slice[2].lineno , t.slice[2].lexpos)
    global count_ins
    count_ins += 1
    repGrammar.append(t.slice)


def p_assignment(t):
    """
    assignment : ID S_ASIGNACION expresion
    | ID S_IGUAL expresion
    """
    if isinstance( t[3] , Select): # PARA VALIDACION DEL SELECT
        t[3] = F1(t[3],C3D_INSTRUCCIONES_FASE1_CADENA(t,True), t.slice[2].lineno , t.slice[2].lexpos )
    t[0] = Asignacion(t[1],t[3], row=t.slice[1].lineno , column=t.slice[1].lexpos)
    repGrammar.append(t.slice)

    #puede subir un function call :v
    
def p_executeStmt(t):
    """
    executeStmt : R_EXECUTE ID S_PARIZQ paramsList S_PARDER
        | R_EXECUTE ID S_PARIZQ S_PARDER
        | R_EXECUTE ID
        | R_EXECUTE STRING
    """
    repGrammar.append(t.slice)
    if len(t) == 6:
        t[0] = Execute(t[2], t[4],t.slice[2].lineno, t.slice[2].lexpos)
    else:
        t[0] = Execute(t[2], [],t.slice[2].lineno, t.slice[2].lexpos)

    #t[0].generate3d(None, instancia_codigo3d)

def p_ifStmt(t):
    """
    ifStmt : R_IF expresion R_THEN plInstructions elsifList R_ELSE plInstructions R_END R_IF
    | R_IF expresion R_THEN plInstructions elsifList R_END R_IF
    """
    if len(t) == 10:
        t[0] = If_Elseif(if_exp=t[2] , if_inst=t[4], lista_elifs = t[5],  row=t.slice[1].lineno , column=t.slice[1].lexpos , else_inst=t[7])
    else:
        t[0] = If_Elseif(if_exp=t[2] , if_inst=t[4],lista_elifs = t[5] , row=t.slice[1].lineno , column=t.slice[1].lexpos)
    repGrammar.append(t.slice)

def p_ifStmt2(t): # ! NO SE PUEDE HACER UN AND CON UN PRIMITIVO
    """
    ifStmt : R_IF expresion R_THEN plInstructions R_ELSE plInstructions R_END R_IF
    | R_IF expresion R_THEN plInstructions R_END R_IF
    """
    if len(t) == 9:
        t[0] = IfSimple(if_exp=t[2] , if_inst=t[4], row=t.slice[1].lineno , column=t.slice[1].lexpos , else_inst=t[6])
    else:
        t[0] = IfSimple(if_exp=t[2] , if_inst=t[4], row=t.slice[1].lineno , column=t.slice[1].lexpos)
    repGrammar.append(t.slice)

def p_elsifList(t):
    """
    elsifList : elsifList elsifStmt
    | elsifStmt
    """
    repGrammar.append(t.slice)
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_elsifStmt(t):
    """
    elsifStmt : reservada_elseif expresion R_THEN plInstructions
    """
    t[0] = IfSimple(if_exp=t[2] , if_inst=t[4], row=t.slice[3].lineno , column=t.slice[3].lexpos)
    repGrammar.append(t.slice)
def p_reservada_elseif(t):
    '''
    reservada_elseif : R_ELSEIF
                    | R_ELSIF
    '''
    t[0] = t[1]

def p_caseStmt(t):
    """
    caseStmt : R_CASE expresion caseListStmt R_ELSE plInstructions R_END R_CASE
            | R_CASE expresion caseListStmt R_END R_CASE
    """
    if len(t) == 8:
        t[0] = Case(t[2],t[3],t[5],t.slice[1].lineno,t.slice[1].lexpos)
    else:
        t[0] = Case(t[2],t[3],None,t.slice[1].lineno,t.slice[1].lexpos)
    repGrammar.append(t.slice)
        
def p_caseListStmt(t):
    """
    caseListStmt : caseListStmt caseWhenStmt
            | caseWhenStmt
    """
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
    repGrammar.append(t.slice)

def p_caseWhenStmt(t):
    """caseWhenStmt : R_WHEN expresion R_THEN plInstructions"""
    t[0] = CaseWhen(t[2], t[4],t.slice[1].lineno,t.slice[1].lexpos)
    repGrammar.append(t.slice)

def p_returnStmt(t):
    """
    returnStmt : R_RETURN expresion
    """
    t[0] = Return_(exp = t[2] ,  row=t.slice[1].lineno , column=t.slice[1].lexpos)
    repGrammar.append(t.slice)
#endregion

















# Statement para el CREATE
# region CREATE
def p_id_string(t):
    """
    idOrString : ID
    | STRING
    | CHARACTER
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_createstmt(t):
    """createStmt : R_CREATE createBody"""
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_createbody(t):
    """
    createBody : createOpts
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_createopts_table(t):
    """createOpts : R_TABLE ifNotExists idOrString S_PARIZQ createTableList S_PARDER inheritsOpt """
    t[0] = instruction2.CreateTable(
        t[2], t[3], t[7], t.slice[1].lineno, t.slice[1].lexpos, t[5]
    )
    repGrammar.append(t.slice)
    C3D_INSTRUCCIONES_FASE1(t)


def p_createopts_db(t):
    """
    createOpts : orReplace R_DATABASE ifNotExists idOrString createOwner createMode
    """
    t[0] = instruction2.CreateDataBase(
        t[1], t[3], t[4], t[5], t[6], t.slice[2].lineno, t.slice[2].lexpos
    )
    repGrammar.append(t.slice)
    C3D_INSTRUCCIONES_FASE1(t)


def p_replace_true(t):
    """
    orReplace : R_OR R_REPLACE
    """
    t[0] = True
    repGrammar.append(t.slice)


def p_replace_false(t):
    """
    orReplace :
    """
    t[0] = False
    repGrammar.append(t.slice)


def p_createopts_type(t):
    """
    createOpts : R_TYPE ifNotExists ID R_AS R_ENUM S_PARIZQ paramsList S_PARDER
    """
    t[0] = instruction2.CreateType(
        t[2], t[3], t.slice[1].lineno, t.slice[1].lexpos, t[7]
    )
    repGrammar.append(t.slice)
    C3D_INSTRUCCIONES_FASE1(t)


def p_ifnotexists_true(t):
    """
    ifNotExists : R_IF R_NOT R_EXISTS
    """
    t[0] = True
    repGrammar.append(t.slice)


def p_ifnotexists_false(t):
    """
    ifNotExists :
    """
    t[0] = False
    repGrammar.append(t.slice)


def p_inheritsOpt(t):
    """
    inheritsOpt : R_INHERITS S_PARIZQ ID S_PARDER
    """
    t[0] = t[3]
    repGrammar.append(t.slice)


def p_inheritsOpt_none(t):
    """
    inheritsOpt :
    """
    t[0] = None
    repGrammar.append(t.slice)


def p_createowner(t):
    """
    createOwner : R_OWNER ID
    | R_OWNER STRING
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_createowner_asg(t):
    """
    createOwner :  R_OWNER S_IGUAL ID
    | R_OWNER S_IGUAL STRING
    """
    t[0] = t[3]
    repGrammar.append(t.slice)


def p_createowner_none(t):
    """
    createOwner :
    """
    t[0] = None
    repGrammar.append(t.slice)


def p_createmode(t):
    """
    createMode : R_MODE INTEGER
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_createMode_asg(t):
    """
    createMode : R_MODE S_IGUAL INTEGER
    """
    t[0] = t[3]
    repGrammar.append(t.slice)


def p_createmode_none(t):
    """
    createMode :
    """
    t[0] = None
    repGrammar.append(t.slice)


def p_createtable_list(t):
    """createTableList : createTableList S_COMA createTable"""
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_createtable_u(t):
    """createTableList :  createTable"""
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_createTable_id(t):
    """
    createTable :  ID types createColumns
    """
    t[0] = [False, t[1], t[2], t[3]]
    repGrammar.append(t.slice)


def p_createTable(t):
    """
    createTable : createConstraint
    | createUnique
    | createPrimary
    | createForeign
    """
    t[0] = [True, t[1]]
    repGrammar.append(t.slice)


def p_createColumNs(t):
    """
    createColumns : colOptionsList
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_createColumNs_none(t):
    """
    createColumns :
    """
    t[0] = None
    repGrammar.append(t.slice)


def p_createConstraint(t):
    """createConstraint : constrName R_CHECK S_PARIZQ booleanCheck S_PARDER"""
    t[0] = [t[2], t[1], t[4]]
    repGrammar.append(t.slice)


def p_createUnique(t):
    """createUnique : R_UNIQUE S_PARIZQ idList S_PARDER"""
    t[0] = [t[1], t[3], None]
    repGrammar.append(t.slice)


def p_createPrimary(t):
    """createPrimary : R_PRIMARY R_KEY S_PARIZQ idList S_PARDER"""
    t[0] = [t[1], t[4]]
    repGrammar.append(t.slice)


def p_createForeign(t):
    """
    createForeign : constrName R_FOREIGN R_KEY S_PARIZQ idList S_PARDER R_REFERENCES ID S_PARIZQ idList S_PARDER
    """
    t[0] = [t[2], t[5], t[8], t[10], t[1]]
    repGrammar.append(t.slice)


def p_constrName(t):
    """
    constrName : R_CONSTRAINT ID
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_constrName_none(t):
    """
    constrName :
    """
    t[0] = None
    repGrammar.append(t.slice)


def p_id_list(t):
    """idList : idList S_COMA ID"""
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_id_u(t):
    """idList : ID"""
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_types(t):
    """
    types :  ID
    """
    t[0] = [t[1], [None]]
    repGrammar.append(t.slice)


def p_types_simple(t):
    """
    types : T_SMALLINT
    | T_INTEGER
    | T_BIGINT
    | T_REAL
    | T_DOUBLE T_PRECISION
    | T_MONEY
    | T_TEXT
    | T_BOOLEAN
    | R_TIMESTAMP
    | T_DATE
    | T_TIME
    """
    t[0] = [t[1], [None]]
    repGrammar.append(t.slice)


# TODO: Cambiar el optParams
def p_types_params(t):
    """
    types : T_DECIMAL optParams
    | T_NUMERIC optParams
    | T_VARCHAR optParams
    | T_CHARACTER optParams
    | T_CHAR optParams
    """
    t[0] = [t[1], t[2]]
    repGrammar.append(t.slice)


def p_types_var(t):
    """
    types : T_CHARACTER T_VARYING optParams
    """
    t[0] = [t[2], t[3]]
    repGrammar.append(t.slice)


def p_timeType_interval(t):
    """
    types : R_INTERVAL intervalFields
    """
    t[0] = [t[1], [t[2]]]
    repGrammar.append(t.slice)


def p_intervalFields(t):
    """
    intervalFields :  R_YEAR
    | R_MONTH
    | R_DAY
    | R_HOUR
    | R_MINUTE
    | R_SECOND
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_intervalFields_none(t):
    """
    intervalFields :
    """
    t[0] = False
    repGrammar.append(t.slice)


def p_optParams(t):
    """optParams : S_PARIZQ literalList S_PARDER"""
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_optParams_none(t):
    """optParams : """
    t[0] = None
    repGrammar.append(t.slice)


def p_colOptions_list(t):
    """colOptionsList : colOptionsList colOptions"""
    t[1].append(t[2])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_colOptions_u(t):
    """colOptionsList : colOptions"""
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_colOptions(t):
    """
    colOptions : defaultVal
    | nullOpt
    | constraintOpt
    | primaryOpt
    | referencesOpt
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


# cambiar literal
def p_defaultVal(t):
    """defaultVal : R_DEFAULT literal"""
    t[0] = [t[1], t[2].execute(0)]
    repGrammar.append(t.slice)


def p_nullOpt_true(t):
    """
    nullOpt : R_NOT R_NULL
    """
    t[0] = [t[2], True]
    repGrammar.append(t.slice)


def p_nullOpt_false(t):
    """
    nullOpt : R_NULL
    """
    t[0] = [t[1], False]
    repGrammar.append(t.slice)


# cambiar literal


def p_constraintOpt_unique(t):
    """
    constraintOpt : constrName R_UNIQUE
    """
    t[0] = [t[2], t[1]]
    repGrammar.append(t.slice)


def p_constraintOpt_check(t):
    """
    constraintOpt : constrName R_CHECK S_PARIZQ booleanCheck S_PARDER
    """
    t[0] = [t[2], t[1], t[4]]
    repGrammar.append(t.slice)


def p_primaryOpt(t):
    """primaryOpt : R_PRIMARY R_KEY"""
    t[0] = [t[1], True]
    repGrammar.append(t.slice)


def p_referencesOpt(t):
    """referencesOpt : R_REFERENCES ID"""
    t[0] = [t[1], t[2]]
    repGrammar.append(t.slice)


# endregion CREATE

# Gramatica para expresiones

# region Expresiones
def p_expresion(t):
    """
    expresion : datatype
            | expBool
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_expresion_(t):
    """
    expresion : S_PARIZQ selectStmt S_PARDER
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_funcCall_1(t):
    """
    funcCall : ID S_PARIZQ paramsList S_PARDER
    """
    t[0] = expression.FunctionCall(t[1], t[3], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_funcCall_2(t):
    """
    funcCall : ID S_PARIZQ S_PARDER
            | R_NOW S_PARIZQ S_PARDER
    """
    t[0] = expression.FunctionCall(t[1], [], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_funcCall_3(t):
    """
    funcCall : R_COUNT S_PARIZQ datatype S_PARDER
            | R_COUNT S_PARIZQ O_PRODUCTO S_PARDER
            | R_SUM S_PARIZQ datatype S_PARDER
            | R_PROM S_PARIZQ datatype S_PARDER
    """
    repGrammar.append(t.slice)
    t[0] = expression.AggregateFunction(
        t[1], t[3], t.slice[1].lineno, t.slice[1].lexpos
    )


def p_extract_1(t):
    """
    extract : R_EXTRACT S_PARIZQ optsExtract R_FROM timeStamp S_PARDER
    """
    t[0] = expression.ExtractDate(
        t[3], t[5][0], t[5][1], t.slice[1].lineno, t.slice[1].lexpos
    )

    repGrammar.append(t.slice)


def p_extract_2(t):
    """
    extract : R_EXTRACT S_PARIZQ optsExtract R_FROM columnName S_PARDER
    """
    t[0] = expression.ExtractColumnDate(
        t[3], t[5], t.slice[1].lineno, t.slice[1].lexpos
    )
    repGrammar.append(t.slice)


def p_timeStamp(t):
    """
    timeStamp : R_TIMESTAMP STRING
          | R_INTERVAL STRING
    """
    t[0] = [t[1], t[2], t.slice[1].lineno, t.slice[1].lexpos]
    repGrammar.append(t.slice)


def p_optsExtract(t):
    """
    optsExtract : R_YEAR
                  | R_MONTH
                  | R_DAY
                  | R_HOUR
                  | R_MINUTE
                  | R_SECOND
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_datePart(t):
    """
    datePart : R_DATE_PART S_PARIZQ STRING S_COMA dateSource S_PARDER
    """
    t[0] = expression.DatePart(
        t[3], t[5][0], t[5][1], t.slice[1].lineno, t.slice[1].lexpos
    )
    repGrammar.append(t.slice)


def p_dateSource(t):
    """
    dateSource : R_TIMESTAMP STRING
          | T_DATE STRING
          | T_TIME STRING
          | R_INTERVAL STRING
          | R_NOW S_PARIZQ S_PARDER
    """
    t[0] = [t[1], t[2]]
    repGrammar.append(t.slice)


def p_current(t):
    """
    current : R_CURRENT_DATE
          | R_CURRENT_TIME
    """
    t[0] = expression.Current(t[1], None, t.slice[1].lineno, t.slice[1].lexpos)

    repGrammar.append(t.slice)


def p_current_1(t):
    """
    current : timeStamp
    """
    t[0] = expression.Current(t[1][0], t[1][1], t[1][2], t[1][3])
    repGrammar.append(t.slice)


def p_literal_list(t):
    """literalList : literalList S_COMA literal"""
    t[1].append(t[3].execute(0).value)
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_literal_u(t):
    """literalList : literal"""
    t[0] = [t[1].execute(0).value]
    repGrammar.append(t.slice)


def p_literal(t):
    """
    literal :  INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE
    | R_NULL
    """
    if t.slice[1].type == "CHARACTER" or t.slice[1].type == "STRING":
        tipo = TYPE.STRING
    elif t.slice[1].type == "R_TRUE" or t.slice[1].type == "R_FALSE":
        t.slice[1].value = t.slice[1].value == "TRUE"
        tipo = TYPE.BOOLEAN
    elif t.slice[1].type == "R_NULL":
        tipo = TYPE.NULL
    else:
        tipo = TYPE.NUMBER
    t[0] = expression.Primitive(
        tipo, t.slice[1].value, t.slice[1].value, t.slice[1].lineno, t.slice[1].lexpos
    )
    repGrammar.append(t.slice)


def p_params_list(t):
    """paramsList : paramsList S_COMA datatype"""
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_params_u(t):
    """paramsList : datatype"""
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_datatype_operadores_binarios1(t):
    """
    datatype : datatype O_SUMA datatype
    | datatype O_RESTA datatype
    | datatype O_PRODUCTO datatype
    | datatype O_DIVISION datatype
    | datatype O_EXPONENTE datatype
    | datatype O_MODULAR datatype
    """
    t[0] = expression.BinaryArithmeticOperation(t[1], t[3], t[2], t[1].row, t[1].column)

    repGrammar.append(t.slice)


def p_datatype_operadores_binarios2(t):
    """
    datatype : datatype OC_CONCATENAR datatype
    """
    t[0] = expression.BinaryStringOperation(t[1], t[3], t[2], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_datatype_case_when(t):
    """
    datatype : R_CASE caseList optElse R_END
    """


def p_case_list(t):
    """
    caseList : caseList caseWhen
            | caseWhen
    """


def p_caseWhen(t):
    """caseWhen : R_WHEN expBool R_THEN literal"""


def p_caseWhen_2(t):
    """optElse : R_ELSE literal
    |
    """


def p_datatype_operadores_unarios(t):
    """
    datatype : O_RESTA datatype %prec UO_RESTA
    | O_SUMA datatype %prec UO_SUMA
    """
    t[0] = expression.UnaryArithmeticOperation(t[2], t[1], t[2].row, t[2].column)
    repGrammar.append(t.slice)


def p_datatype_operandos(t):
    """
    datatype : columnName
    | literal
    | funcCall
    | extract
    | datePart
    | current
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_datatype_agrupacion(t):
    """
    datatype : S_PARIZQ datatype S_PARDER
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_expCompBinario_1(t):
    """
    expComp : datatype OL_MENORQUE datatype
    | datatype OL_MAYORQUE datatype
    | datatype OL_MAYORIGUALQUE datatype
    | datatype OL_MENORIGUALQUE datatype
    | datatype S_IGUAL datatype
    | datatype OL_DISTINTODE datatype
    """
    t[0] = expression.BinaryRelationalOperation(t[1], t[3], t[2], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_expCompBinario_2(t):
    """
    expComp : datatype R_IS R_DISTINCT R_FROM datatype
    """
    t[0] = expression.BinaryRelationalOperation(
        t[1], t[5], t[2] + t[3] + t[4], t[1].row, t[1].column
    )
    repGrammar.append(t.slice)


def p_expCompBinario_3(t):
    """
    expComp : datatype R_IS R_NOT R_DISTINCT R_FROM datatype
    """
    t[0] = expression.BinaryRelationalOperation(
        t[1], t[6], t[2] + t[3] + t[4] + t[5], t[1].row, t[1].column
    )
    repGrammar.append(t.slice)


def p_expComp_ternario_1(t):
    """
    expComp :  datatype R_BETWEEN datatype R_AND datatype
    """
    t[0] = expression.TernaryRelationalOperation(
        t[1], t[3], t[5], t[2], t[1].row, t[1].column
    )
    repGrammar.append(t.slice)


def p_expComp_ternario_2(t):
    """
    expComp : datatype R_NOT R_BETWEEN datatype R_AND datatype
    | datatype R_BETWEEN R_SYMMETRIC datatype R_AND datatype
    """
    t[0] = expression.TernaryRelationalOperation(
        t[1], t[4], t[6], t[2] + t[3], t[1].row, t[1].column
    )

    repGrammar.append(t.slice)


def p_expComp_unario_1(t):
    """
    expComp : datatype R_ISNULL
    | datatype R_NOTNULL
    """
    t[0] = expression.UnaryRelationalOperation(t[1], t[2], t[1].row, t[1].column)

    repGrammar.append(t.slice)


def p_expComp_unario_2(t):
    """
    expComp : datatype R_IS R_NULL
    | datatype R_IS R_TRUE
    | datatype R_IS R_FALSE
    | datatype R_IS R_UNKNOWN
    """
    t[0] = expression.UnaryRelationalOperation(t[1], t[2] + t[3], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_expComp_unario_3(t):
    """
    expComp : datatype R_IS R_NOT R_NULL
    | datatype R_IS R_NOT R_TRUE
    | datatype R_IS R_NOT R_FALSE
    | datatype R_IS R_NOT R_UNKNOWN
    """
    t[0] = expression.UnaryRelationalOperation(
        t[1], t[2] + t[3] + t[4], t[1].row, t[1].column
    )
    repGrammar.append(t.slice)








def p_boolean_1(t):
    """
    boolean : R_EXISTS S_PARIZQ selectStmt S_PARDER
    """
    t[0] = expression.ExistsRelationalOperation(
        t[3], t.slice[1].lineno, t.slice[1].lexpos
    )
    repGrammar.append(t.slice)


def p_boolean_2(t):
    """
    boolean : datatype R_IN S_PARIZQ selectStmt S_PARDER
    """
    t[0] = expression.InRelationalOperation(t[1], "", t[4], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_boolean_3(t):
    """
    boolean : datatype R_NOT R_IN S_PARIZQ selectStmt S_PARDER
    """
    t[0] = expression.InRelationalOperation(t[1], t[2], t[5], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_boolean_4(t):
    """
    boolean : expComp
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_expBool_1(t):
    """
    expBool : expBool R_AND expBool
            | expBool R_OR expBool
    """
    t[0] = expression.BinaryLogicalOperation(t[1], t[3], t[2], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_expBool_2(t):
    """
    expBool : R_NOT expBool
    """
    t[0] = expression.UnaryLogicalOperation(t[2], t[1], t[2].row, t[2].column)
    repGrammar.append(t.slice)


def p_expBool_3(t):
    """
    expBool : S_PARIZQ expBool S_PARDER
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_expBool_5(t):
    """
    expBool : expBool optBoolPredicate
    """
    t[0] = expression.UnaryLogicalOperation(t[1], t[2], t[1].row, t[1].column)
    repGrammar.append(t.slice)


def p_expBool_4(t):
    """
    expBool : boolean
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_optBoolPredicate_1(t):
    """
    optBoolPredicate : R_IS R_TRUE
    | R_IS R_FALSE
    | R_IS R_UNKNOWN
    """
    t[0] = t[1] + t[2]
    repGrammar.append(t.slice)


def p_optBoolPredicate_2(t):
    """
    optBoolPredicate : R_IS R_NOT R_TRUE
    | R_IS R_NOT R_FALSE
    | R_IS R_NOT R_UNKNOWN
    """
    t[0] = t[1] + t[2] + t[3]
    repGrammar.append(t.slice)


def p_columnName_id(t):
    """
    columnName : ID
    """
    t[0] = expression.Identifiers(None, t[1], t.slice[1].lineno, t.slice[1].lexpos)

    repGrammar.append(t.slice)


def p_columnName_table_id(t):
    """
    columnName : ID S_PUNTO ID
    """
    t[0] = expression.Identifiers(t[1], t[3], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


# En caso de errores descomentar este metodo
'''
def p_columnName_table_idAll(t):
    """
    columnName : ID S_PUNTO O_PRODUCTO
    """
    t[0] = expression.TableAll(t[1], t.slice[1].lineno, t.slice[1].lexpos)
'''


def p_booleanCheck_1(t):
    """
    booleanCheck : idOrLiteral OL_MENORQUE idOrLiteral
    | idOrLiteral OL_MAYORQUE idOrLiteral
    | idOrLiteral OL_MAYORIGUALQUE idOrLiteral
    | idOrLiteral OL_MENORIGUALQUE idOrLiteral
    | idOrLiteral S_IGUAL idOrLiteral
    | idOrLiteral OL_DISTINTODE idOrLiteral
    """
    t[0] = [t[1].value, t[3].value, t[2], t[1].type, t[3].type]
    repGrammar.append(t.slice)


def p_booleanCheck_2(t):
    """
    booleanCheck : idOrLiteral R_IS R_DISTINCT R_FROM idOrLiteral
    """
    t[0] = [t[1].value, t[5].value, "!=", t[1].type, t[5].type]
    repGrammar.append(t.slice)


def p_booleanCheck_3(t):
    """
    booleanCheck : idOrLiteral R_IS R_NOT R_DISTINCT R_FROM idOrLiteral
    """
    t[0] = [t[1].value, t[5].value, "==", t[1].type, t[6].type]
    repGrammar.append(t.slice)


def p_idOrLiteral(t):
    """
    idOrLiteral : ID
    | INTEGER
    | STRING
    | DECIMAL
    | CHARACTER
    | R_TRUE
    | R_FALSE
    """

    if t.slice[1].type == "CHARACTER" or t.slice[1].type == "STRING":
        tipo = "STRING"
    elif t.slice[1].type == "R_TRUE" or t.slice[1].type == "R_FALSE":
        t.slice[1].value = t.slice[1].value == "TRUE"
        tipo = "BOOLEAN"
    elif t.slice[1].type == "INTEGER" or t.slice[1].type == "DECIMAL":
        tipo = "NUMBER"
    else:
        tipo = "ID"
    t[0] = expression.CheckValue(
        t.slice[1].value, tipo, t.slice[1].lineno, t.slice[1].lexpos
    )
    t[0].execute(0)

    repGrammar.append(t.slice)


# endregion

# Statement para el ALTER
# region ALTER


def p_alterStmt(t):
    """alterStmt : R_ALTER R_DATABASE idOrString alterDb
    | R_ALTER R_TABLE idOrString alterTableList
    """
    if t[2] == "DATABASE":
        t[0] = instruction2.AlterDataBase(
            t[4][0], t[3], t[4][1], t.slice[1].lineno, t.slice[1].lexpos
        )
    else:
        t[0] = instruction2.AlterTable(t[3], t.slice[1].lineno, t.slice[1].lexpos, t[4])
    repGrammar.append(t.slice)


def p_alterDb(t):
    """alterDb : R_RENAME R_TO idOrString
    | R_OWNER R_TO ownerOPts
    """
    t[0] = [t[1], t[3]]

    repGrammar.append(t.slice)


def p_ownerOpts(t):
    """
    ownerOPts : idOrString
    | R_CURRENT_USER
    | R_SESSION_USER
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_alterTableList(t):
    """
    alterTableList : alterTableList S_COMA alterTable
    """
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_alterTableList_u(t):
    """
    alterTableList : alterTable
    """
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_alterTable(t):
    """
    alterTable : R_ADD alterAdd
    | R_ALTER alterAlter
    | R_DROP alterDrop
    | R_RENAME alterRename
    """
    t[0] = [t[1], t[2]]
    repGrammar.append(t.slice)


def p_alterAdd_column(t):
    """
    alterAdd : R_COLUMN ID types
    """
    t[0] = [False, t[2], t[3], None]
    repGrammar.append(t.slice)


def p_alterAdd_constraint(t):
    """
    alterAdd : createConstraint
    | createPrimary
    | createForeign
    """
    t[0] = [True, t[1]]
    repGrammar.append(t.slice)


def p_alterAdd_unique(t):
    """
    alterAdd : constrName R_UNIQUE S_PARIZQ ID S_PARDER
    """
    t[0] = [True, [t[2], [t[4]], t[1]]]
    repGrammar.append(t.slice)


def p_alterAlter(t):
    """
    alterAlter : R_COLUMN ID R_SET nullOpt
    | R_COLUMN ID R_SET defaultVal
    | R_COLUMN ID R_TYPE types
    """
    t[0] = [t[3], t[2], t[4]]
    repGrammar.append(t.slice)


def p_alterDrop(t):
    """
    alterDrop : R_CONSTRAINT ID
    | R_COLUMN ID
    """
    t[0] = [t[1], t[2]]
    repGrammar.append(t.slice)


def p_alterRename(t):
    """
    alterRename : R_COLUMN ID R_TO ID
    """
    t[0] = [t[2], t[4]]
    repGrammar.append(t.slice)


# endregion


"""
Statement para el DROP
"""

# region DROP


def p_dropStmt(t):
    """
    dropStmt : R_DROP R_TABLE ifExists idOrString
    | R_DROP R_DATABASE ifExists idOrString
    """
    exists = True
    if t[3] == None:
        exists = False
    t[0] = instruction2.Drop(t[2], t[4], exists, t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_ifExists(t):
    """ifExists : R_IF R_EXISTS
    |
    """

    repGrammar.append(t.slice)


# endregion

# Statement para el SELECT
# region SELECT


def p_selectStmt_1(t):
    """selectStmt : R_SELECT R_DISTINCT selectParams fromCl whereCl groupByCl limitCl orderByCl"""
    t[0] = instruction2.Select(
        t[3].params,
        t[4],
        t[5],
        t[6][0],
        t[6][1],
        t[7],
        t[8],
        True,
        t.slice[1].lineno,
        t.slice[1].lexpos,
    )
    repGrammar.append(t.slice)


# TODO: Cambiar gramatica | R_SELECT selectParams R_FROM tableExp joinList whereCl groupByCl orderByCl limitCl
def p_selectStmt_2(t):
    """selectStmt : R_SELECT selectParams fromCl whereCl groupByCl limitCl orderByCl"""
    t[0] = instruction2.Select(
        t[2],
        t[3],
        t[4],
        t[5][0],
        t[5][1],
        t[6],
        t[7],
        False,
        t.slice[1].lineno,
        t.slice[1].lexpos,
    )
    repGrammar.append(t.slice)


def p_selectStmt_union(t):
    """selectStmt : selectStmt R_UNION allOpt selectStmt"""
    t[0] = instruction2.Union(t[1], t[4], t.slice[2].lineno, t.slice[2].lexpos)
    repGrammar.append(t.slice)


def p_selectStmt_intersect(t):
    """selectStmt : selectStmt R_INTERSECT allOpt selectStmt"""
    t[0] = instruction2.Intersect(t[1], t[4], t.slice[2].lineno, t.slice[2].lexpos)
    repGrammar.append(t.slice)


def p_selectStmt_except(t):
    """selectStmt : selectStmt R_EXCEPT allOpt selectStmt"""
    t[0] = instruction2.Except_(t[1], t[4], t.slice[2].lineno, t.slice[2].lexpos)
    repGrammar.append(t.slice)


def p_selectStmt_agrupacion(t):
    """selectStmt : S_PARIZQ selectStmt S_PARDER"""
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_fromClause(t):
    """
    fromCl : R_FROM tableExp
    """
    tables = []
    aliases = []
    for i in range(len(t[2])):
        tables.append(t[2][i][0])
        aliases.append(t[2][i][1])
    t[0] = instruction2.FromClause(
        tables, aliases, t.slice[1].lineno, t.slice[1].lexpos
    )
    repGrammar.append(t.slice)


def p_selectstmt_only_params(t):
    """selectStmt : R_SELECT selectParams"""
    t[0] = instruction2.SelectOnlyParams(t[2], t.slice[1].lineno, t.slice[1].lineno)
    repGrammar.append(t.slice)


def p_allOpt(t):
    """allOpt : R_ALL
    |
    """

    repGrammar.append(t.slice)


def p_selectparams_all(t):
    """selectParams : O_PRODUCTO"""
    t[0] = []
    repGrammar.append(t.slice)


def p_selectparams_params(t):
    """selectParams : selectList"""
    t[0] = t[1]
    repGrammar.append(t.slice)


# En caso de errores cambiar selectListParams -> expresion
def p_selectList_list(t):
    """selectList : selectList S_COMA selectListParams optAlias"""
    if t[4] != None:
        t[3].temp = t[4]
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


# En caso de errores cambiar selectListParams -> expresion
def p_selectList_u(t):
    """selectList : selectListParams optAlias"""
    if t[2] != None:
        t[1].temp = t[2]
    t[0] = [t[1]]

    repGrammar.append(t.slice)


def p_selectListParams_1(t):
    """selectListParams : expresion"""
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_selectListParams_2(t):
    """selectListParams : ID S_PUNTO O_PRODUCTO"""
    t[0] = expression.TableAll(t[1], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_optalias_as(t):
    """
    optAlias : R_AS idOrString
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_optalias_id(t):
    """
    optAlias : idOrString
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_optalias_none(t):
    """optAlias : """
    t[0] = None
    repGrammar.append(t.slice)


def p_tableexp_list(t):
    """tableExp : tableExp S_COMA fromBody """
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_tableexp_u(t):
    """tableExp : fromBody """
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_fromBody(t):
    """fromBody : ID optAlias"""
    if t[2] != None:
        t[0] = [instruction2.TableID(t[1], t.slice[1].lineno, t.slice[1].lexpos), t[2]]
    else:
        t[0] = [instruction2.TableID(t[1], t.slice[1].lineno, t.slice[1].lexpos), ""]
    repGrammar.append(t.slice)


def p_tableexp_subq(t):
    """fromBody : S_PARIZQ selectStmt S_PARDER R_AS idOrString"""
    t[0] = [t[2], t[5]]

    repGrammar.append(t.slice)















def p_whereCl(t):
    """whereCl : R_WHERE expBool"""
    if t[2] != None:
        t[0] = instruction2.WhereClause(t[2], t.slice[1].lineno, t.slice[1].lexpos)
    else:
        t[0] = None
    repGrammar.append(t.slice)


def p_whereCl_none(t):
    """whereCl : """
    t[0] = None
    repGrammar.append(t.slice)


def p_groupByCl_1(t):
    """
    groupByCl : R_GROUP R_BY groupList havingCl
    """
    t[0] = [t[3], t[4]]
    repGrammar.append(t.slice)


def p_groupByCl_2(t):
    """
    groupByCl :
    """
    t[0] = [None, None]
    repGrammar.append(t.slice)


def p_groupList_1(t):
    """
    groupList :  groupList S_COMA columnName
            | groupList S_COMA INTEGER
    """
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_groupList_2(t):
    """
    groupList :  columnName
            | INTEGER
    """
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_havingCl_1(t):
    """havingCl : R_HAVING expBool"""
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_havingCl_2(t):
    """havingCl :"""
    t[0] = None
    repGrammar.append(t.slice)


def p_orderByCl(t):
    """orderByCl : R_ORDER R_BY orderList"""
    t[0] = instruction2.OrderByClause(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_orderByCl_n(t):
    """orderByCl : """
    t[0] = None
    repGrammar.append(t.slice)


def p_orderList(t):
    """orderList : orderList S_COMA orderByElem"""
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_orderList_1(t):
    """orderList : orderByElem"""
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_orderByElem(t):
    """
    orderByElem : columnName orderOpts orderNull
                | INTEGER orderOpts orderNull
    """
    t[0] = instruction2.OrderByElement(t[1], t[2], t[3])
    repGrammar.append(t.slice)


def p_orderOpts(t):
    """orderOpts : R_ASC
    | R_DESC
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_orderOpts_n(t):
    """orderOpts :"""
    t[0] = "ASC"
    repGrammar.append(t.slice)


def p_orderNull(t):
    """orderNull : R_NULLS R_FIRST
    | R_NULLS R_LAST
    """
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_orderNull_n(t):
    """orderNull :"""
    t[0] = "FIRST"
    repGrammar.append(t.slice)


def p_limitCl(t):
    """limitCl : R_LIMIT INTEGER offsetLimit
    | R_LIMIT R_ALL offsetLimit
    """
    t[0] = instruction2.LimitClause(t[2], t[3], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_limitCl_n(t):
    """limitCl :"""
    t[0] = None
    repGrammar.append(t.slice)


def p_offsetLimit(t):
    """offsetLimit : R_OFFSET INTEGER"""
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_offsetLimit_n(t):
    """offsetLimit :"""
    t[0] = None
    repGrammar.append(t.slice)


# endregion

# Statement para el INSERT

# region INSERT


def p_insertStmt(t):
    """insertStmt : R_INSERT R_INTO ID paramsColumn R_VALUES S_PARIZQ paramsList S_PARDER"""

    t[0] = instruction2.InsertInto(
        t[3], t[4], t[7], t.slice[1].lineno, t.slice[1].lexpos
    )
    repGrammar.append(t.slice)


def p_paramsColumn(t):
    """paramsColumn : S_PARIZQ idList S_PARDER"""
    t[0] = t[2]
    repGrammar.append(t.slice)


def p_paramsColumn_none(t):
    """paramsColumn :"""
    t[0] = None

    repGrammar.append(t.slice)


# endregion

# Statement para el UPDATE

# region UPDATE


def p_updateStmt(t):
    """updateStmt : R_UPDATE fromBody R_SET updateCols whereCl"""
    fc = instruction2.FromClause(
        [t[2][0]], [t[2][1]], t.slice[1].lineno, t.slice[1].lexpos
    )
    t[0] = instruction2.Update(fc, t[4], t[5], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_updateCols_list(t):
    """updateCols : updateCols S_COMA updateVals"""
    t[1].append(t[3])
    t[0] = t[1]
    repGrammar.append(t.slice)


def p_updateCols_u(t):
    """updateCols : updateVals """
    t[0] = [t[1]]
    repGrammar.append(t.slice)


def p_updateVals(t):
    """updateVals : ID S_IGUAL updateExp"""
    t[0] = instruction2.Assignment(t[1], t[3], t.slice[1].lineno, t.slice[1].lexpos)

    repGrammar.append(t.slice)


def p_updateExp(t):
    """updateExp : datatype
    | R_DEFAULT
    """
    t[0] = t[1]
    repGrammar.append(t.slice)


# endregion

# Statement para el DELETE y OTROS

# region DELETE, ETC


def p_deleteStmt(t):
    """deleteStmt : R_DELETE fromCl whereCl"""
    t[0] = instruction2.Delete(t[2], t[3], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_truncateStmt(t):
    """truncateStmt : R_TRUNCATE tableOpt ID"""
    t[0] = instruction2.Truncate(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_tableOpt(t):
    """tableOpt : R_TABLE
    |
    """
    repGrammar.append(t.slice)


def p_showStmt(t):
    """showStmt : R_SHOW R_DATABASES likeOpt"""

    t[0] = instruction2.showDataBases(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    repGrammar.append(t.slice)


def p_likeOpt(t):
    """likeOpt : R_LIKE STRING
    |
    """
    if len(t) == 3:
        t[0] = t[2]
    else:
        t[0] = None
    repGrammar.append(t.slice)


def p_useStmt(t):
    """useStmt : R_USE ID"""
    t[0] = instruction.useDataBase(t[2], t.slice[1].lineno, t.slice[1].lexpos)

    repGrammar.append(t.slice)


# endregion





def p_error(t):
    try:
        print(t)
        print("Error sintáctico en '%s'" % t.value)
        syntax_errors.insert(
            len(syntax_errors), ["Error sintáctico en '%s'" % t.value, t.lineno]
        )
        PostgreSQL.insert(
            len(PostgreSQL), "ERROR: 42601: error de sintaxis en '%s'" % t.value
        )
    except AttributeError:
        print("end of file")


parser = yacc.yacc()


def returnSyntacticErrors():
    return syntax_errors


def returnPostgreSQLErrors():
    errors = returnExpErrors()
    errors += PostgreSQL
    errors += instruction.returnErrors()
    return errors


def returnSemanticErrors():
    return instruction.returnSemanticErrors()


def InitTree():
    init = Nodo.Nodo("INSTRUCTION_LIST")
    Tree(init)
    makeAst(init)



def Tree(n):
    if len(listInst) > 0:
        l = listInst.pop()
        n.addNode(l)
        inst = Nodo.Nodo("INST")
        n.addNode(inst)
        Tree(inst)


def makeAst(root):
    instruction.makeAst(root)


def getRepGrammar():
    return repGrammar


def parserTo3D(input)-> None:
    global syntax_errors, PostgreSQL, repGrammar,entrada,count_ins
    entrada = input
    entrada = re.sub('\-\-(.*)\n|/\*(.|\n)*?\*/' ,"",entrada)
    count_ins = 0
    repGrammar = []
    syntax_errors = list()
    PostgreSQL = list()
    expression.list_errors = list()
    instruction.syntaxPostgreSQL = list()
    instruction.semanticErrors = list()
    lexer.lineno = 1
    instancia_codigo3d.restart()
    SymbolTable.symbolTable.clear()
    return ArbolGeneral(parser.parse(input))




#------------------------------------ METODOS PROPIOS DE LA FASE 2

def getCodigo():
    instancia_codigo3d.generarArchivoEjecucion()
    return instancia_codigo3d.getCodigo()

def C3D_INSTRUCCIONES_FASE1(t):
    """
    este metodo es para guardar las cadenas correspondientes a la fase 1
    en una variable temporal en el codigo de 3 direcciones

    Parametro: t es una produccion de cualquiera de las instrucciones principales
    salida: tn = "instruccion"
    """


    global count_ins
    arreglo_split = entrada.split(sep=";", maxsplit=count_ins + 1)
    # POSEE UN MAX SPLIT poque no es necesario dividir las instrucciones que aun no se han analizado
    instruccionAnlizada = str(arreglo_split[count_ins]).strip() + ";"

    # antes verificar que inicie con una de las palabras reservadas
    instruccionAnlizada = instancia_codigo3d.asegurarIntruccion(instruccionAnlizada,True)#TRUE VA EN EL MAIN
    if len(instruccionAnlizada) != 0:
        tn = instancia_codigo3d.getNewTemporal()
        instruccionC3D = f'\t{tn} = "{instruccionAnlizada}"'
        instancia_codigo3d.addToMain(instruccionC3D)
        instancia_codigo3d.addToMain(f"\tstack.push({tn})")
        instancia_codigo3d.addToMain(f"\tfuncionIntermedia()")

def C3D_INSTRUCCIONES_SIN_EJECUCION(t):
    """
        solo lo pasa como 
        tn = "  cadena pura  "
    """
    global count_ins
    arreglo_split = entrada.split(sep=";", maxsplit=count_ins + 1)
    # POSEE UN MAX SPLIT poque no es necesario dividir las instrucciones que aun no se han analizado
    instruccionAnlizada = str(arreglo_split[count_ins]).strip() + ";"
    # antes verificar que inicie con una de las palabras reservadas
    instruccionAnlizada = instancia_codigo3d.asegurarIntruccion(instruccionAnlizada,True)#TRUE VA EN EL MAIN
    if len(instruccionAnlizada) != 0:
        tn = instancia_codigo3d.getNewTemporal()
        instruccionC3D = f'\t{tn} = "{instruccionAnlizada}"'
        instancia_codigo3d.addToMain(instruccionC3D)



def C3D_INSTRUCCIONES_FASE1_CADENA(t , quitarParentesis = False)->str:
    """
    retorna la cadena de la fase 1 correspondiente
    """
    global count_ins
    arreglo_split = entrada.split(sep=";", maxsplit=count_ins + 1)
    instruccionAnlizada = str(arreglo_split[count_ins]).strip() + ";"
    instruccionAnlizada = instancia_codigo3d.asegurarIntruccion(instruccionAnlizada,False,quitarParentesis)#FALSE VA EN UN PROCEDURE O FUNCION
    if len(instruccionAnlizada) != 0:
        return instruccionAnlizada # RETORNA UNA CADENA , Tn
    return None












#PARA PROBAR LA GENERACION DE CODIGO 3D
# ast = parserTo3D("""
# CREATE FUNCTION CALCULOS(xd TEXT, valor decimal(10,2)) RETURNS integer AS $$
# DECLARE
#     ejemplo integer := valor;
#     example integer := ejemplo / valor;
#     test text;
# BEGIN
#     valor := 100;
#     IF valor < 1 THEN 
#         CASE valor 
#             WHEN -1 THEN
#                 return False;
#             ELSE 
#                 return True;
#         END CASE;
#     ELSIF valor > 100 THEN
#         return false;
#     ELSE
#         return True;
#     END IF;
# RETURN VALOR;
# END;
# $$ LANGUAGE plpgsql;

# CREATE FUNCTION Nacimiento(xd DATE) RETURNS integer AS $$
# BEGIN
#     IF xd = '4' THEN
#         return False;
#     ELSE
#         return True;
#     END IF;
# RETURN VALOR;
# END;
# $$ LANGUAGE plpgsql;

# CREATE PROCEDURE Prueba() AS $$
# BEGIN
#     RAISE 'Checha Fuma', 'Marihuano';
# RETURN hola;
# END;
# $$ LANGUAGE plpgsql;

# CREATE DATABASE DBFase2;

# USE DBFase2;

# CREATE FUNCTION myFuncion(texto text) RETURNS text AS $$
# BEGIN
#     RETURN texto;
# END;
# $$ LANGUAGE plpgsql;

# select myFuncion('INICIO CALIFICACION FASE 2');

# CREATE TABLE tbProducto (idproducto integer not null primary key,
#                            producto varchar(150) not null,
#                            fechacreacion date not null,
#                          estado integer);

# CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);

# CREATE TABLE tbCalificacion (idcalifica integer not null primary key,
#                              item varchar(100) not null,
#                              punteo integer not null);

# CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);

# INSERT INTO tbProducto values(1,'Laptop Lenovo',now(),1);
# INSERT INTO tbProducto values(2,'Bateria para Laptop Lenovo T420',now(),1);
# INSERT INTO tbProducto values(3,'Teclado Inalambrico',now(),1);
# INSERT INTO tbProducto values(4,'Mouse Inalambrico',now(),1);
# INSERT INTO tbProducto values(5,'WIFI USB',now(),1);

# CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS int AS $$
# DECLARE resultado INTEGER; 
#         retorna   INTEGER;
# BEGIN
#     if tabla = 'tbProducto' then
#         resultado := (SELECT COUNT(*) FROM tbProducto);
#         if cantidad = resultado then
#             retorna = 1;
#         else 
#             retorna = 0;
#         end if;
#     end if;
# RETURN retorna;
# END;
# $$ LANGUAGE plpgsql;
# """)
# print("\n---------------- SALIDA: -----------------")
# instancia_codigo3d.showCode()
