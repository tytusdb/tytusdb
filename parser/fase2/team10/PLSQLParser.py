from ply import *

from lexico_pl import *
from InstruccionesPL.TablaSimbolosPL.TipoPL import TipoPL, Tipo_DatoPL
from InstruccionesPL.Expresiones import PrimitivoPL, Parametro, AritmeticaPL, RelacionalPL, LogicaPL
from InstruccionesPL import IdentificadorPL, OutIdentificador, InstruccionPL, InOutIdentificador
from InstruccionesPL.Diccionarios.Directions import  Directions, Direction_Enum
from InstruccionesPL.Funcion.CallFun import   CallFun
from InstruccionesPL.Funcion.InstruSet import   InstruSet
from InstruccionesPL.IndicesPL import IndicePL1, IndicePLUnique, IndicePLUsingNull, IndicePLUsing, IndicePL7,IndicePL8 , IndicePL9, DropIndice, DropIndiceIf, AlterIndice
from InstruccionesPL.ObtenerSql import ObtenerSql
from InstruccionesPL.OpenPL import OpenPL
from InstruccionesPL.Fetch import FetchInto, FetchFromInto, FetchIn
from InstruccionesPL.Move import Move, MoveFrom, MoveIn
from InstruccionesPL.Update import Update, UpdateOper
from InstruccionesPL.Deletes import Deletes
from InstruccionesPL.Closes import Closes
from InstruccionesPL.Gets import Gets, GetsCurrent
from InstruccionesPL.Alias import Alias
from InstruccionesPL.Returns import Returns, ReturnsNext, ReturnsQuery, ReturnQueryExecute
from InstruccionesPL.Ifs import Ifs, IfsElse, IfsElseIf, Elses
from InstruccionesPL.Cases import Cases, WhenPL, CaseElse
from InstruccionesPL.LoopPL import LoopPL
from InstruccionesPL.Exits import Exits
from InstruccionesPL.CreatePL import CreatePL, CreateOrReplacePL
from InstruccionesPL.PLExecute import Execute, ExecuteM
from InstruccionesPL.ProcedurePL import CreateOrReplace, Procedure
from InstruccionesPL.DropPL import DropPL, DropExistsPL
from InstruccionesPL.VariablePL import VariablePL
from InstruccionesPL.CursoresPL import CursorScroll, RecursorPL
from InstruccionesPL.DeclaracionesPL import DeclaracionesPL, DeclaracionesCollatePL
from InstruccionesPL.Asignaciones import AsignacionConstant,Asignaciones, AsignacionDefault, AsignacionVariable
from InstruccionesPL.Collates import Collates, CollatesConstant
from InstruccionesPL.Performs import Performs
from InstruccionesPL.Ends import Ends
from InstruccionesPL.Exceptions import ResultExcept, Exceptions, WhenExcept, GetStacked
from InstruccionesPL.ExceptionPL import ExceptionPL

lista_lexicos=lista_errores_lexico

#imPORt NOdo AS grammer
#FROM InstrucPL.EXECUTEPL imPORt EXECUTEpl
# Definición de la gramática

#tokens = lexico_pl.tokens
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVISION'),
    ('NOnASsoc','BETWEEN', 'LIKE'),
    ('left', 'MENOR', 'MAYOR', 'IGUAL', 'MENORIGUAL', 'MAYORIGUAL', 'DIFERENTE'),
    ('right', 'NOT'),
    ('left', 'AND'),
    ('left', 'OR')
)

def p_init(t):
    'init : instruccionesPL'
    t[0] = t[1]

def p_instruccionesPL_lista1(t):
    'instruccionesPL    :  instruccionesPL instruccion '
    t[1].append(t[2])
    t[0] = t[1]
    
def p_instruccionesPL_lista2(t):
    'instruccionesPL : instruccion '
    t[0] = [t[1]]


def p_instruccionesSQL(t):
    '''instruccion : CADENA'''
    strGram = "<instruccion> ::= CADENA"
    t[0]= ObtenerSql.ObtenerSql(t[1],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_funciones(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR BEGIN contenidosbegin END PYC
    '''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR BEGIN <contenidosbegin> END PYC"
    t[0]= CreatePL.CreatePL(t[3], None, None, t[5],None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)
    

def p_funciones2(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 BEGIN contenidosbegin END PYC
    '''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR PAR1 <listid> PAR2 BEGIN <contenidosbegin> END PYC"
    t[0]= CreatePL.CreatePL(t[3],t[5], None, t[8],None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)
    

def p_funciones22(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR PAR1  PAR2 BEGIN contenidosbegin END PYC
    '''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR PAR1 PAR2 BEGIN <contenidosbegin> END PYC"
    t[0]= CreatePL.CreatePL(t[3],None, None, t[8],None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)    

def p_funciones3(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS operacion_logica BEGIN contenidosbegin END PYC
    '''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR PAR1 <listid> PAR2 AS <operacion_logica> BEGIN <contenidosbegin> END PYC"
    t[0]= CreatePL.CreatePL(t[3], t[5], t[8], t[10],None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)
    

def p_funciones4(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR PAR1 <listid> PAR2 AS <operacion_logica> BEGIN <instruccionesPL> END PYC"
    t[0]= CreatePL.CreatePL(t[3], t[5], t[8], t[13],t[15], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_funciones45(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR PAR1  PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR PAR1 <listid> PAR2 AS <operacion_logica> BEGIN <instruccionesPL> END PYC"
    t[0]= CreatePL.CreatePL(t[3], None, t[8], t[13],t[15], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_funciones5(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0]= CreateOrReplacePL.CreateOrReplacePL(t[5], t[7], t[10], t[15],t[17], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_funciones6(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR PAR1 <listid> PAR2 AS <operacion_logica> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0]= CreatePL.CreatePL(t[3], t[5], t[8], None,t[13], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_funciones7(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid  AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR"
    t[0]= CreateOrReplacePL.CreateOrReplacePL(t[5], t[7], t[10], None,t[15], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_funciones8(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR PAR1 <listid> PAR2 AS <operacion_logica> BEGIN <contenidosbegin> END PYC  DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0]= CreatePL.CreatePL(t[3], t[5], None, t[11],t[13], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_funciones9(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0]= CreateOrReplacePL.CreateOrReplacePL(t[5], t[7], None, t[13],t[15], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_funciones10(t):
    '''
     instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE FUNCTION IDENTIFICADOR PAR1 <listid> PAR2 AS <operacion_logica> BEGIN <contenidosbegin> END PYC"
    t[0]= CreatePL.CreatePL(t[3], t[5], None, None,t[11], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_funciones11(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0]= CreateOrReplacePL.CreateOrReplacePL(t[5], t[7], None, None,t[13], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_eliminarfuncion(t):
    '''instruccion : DROP FUNCTION listid opciondropprocedure '''
    strGram ="instruccion : DROP FUNCTION listid opciondropprocedure PYC"
    t[0]= DropPL.DropPL(None, t[3], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_eliminarfuncion2(t):
    '''instruccion : DROP FUNCTION IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure '''
    strGram ="instruccion : DROP FUNCTION IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure PYC"
    t[0]= DropPL.DropPL(t[1], t[5], t[7], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_eliminarfuncion3(t):
    '''instruccion : DROP FUNCTION IF EXISTS listid opciondropprocedure'''
    strGram ="instruccion : DROP FUNCTION IF EXISTS listid opciondropprocedure PYC"
    t[0]= DropExistsPL.DropExistsPL(None,t[5], t[6], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_eliminarfuncion4(t):
    'instruccion : DROP FUNCTION IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure '
    strGram ="instruccion : DROP FUNCTION IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure PYC"

    t[0]= DropExistsPL.DropExistsPL(t[5], t[7],t[9], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_ejecutarFunVoid(t):
    '''instruccion : PERFORM IDENTIFICADOR PAR1 listid PAR2 PYC'''
    strGram = "<instruccion> ::= PERFORM ID PARIZQ <lcol> PARDER PUNTO_COMA"
    t[0] = Performs.Performs(t[2], t[4], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_ejecutarDinamico(t):
    '''instruccion : EXECUTE CADENA PYC'''
    strGram = "<instruccion> ::= EXECUTE CADENA PYC"
    t[0] = Execute.Execute(t[2], None, None,None,None,'', t.lexer.lineno, t.lexer.lexpos,  strGram)
   
def p_ejecutarDinamico2(t):
    '''instruccion : EXECUTE CADENA INTO IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= EXECUTE CADENA INTO IDENTIFICADOR PYC"
    t[0] = Execute.Execute(t[2], True, None,t[4],None,'', t.lexer.lineno, t.lexer.lexpos,  strGram)
   

def p_ejecutarDinamico3(t):
    '''instruccion : EXECUTE CADENA INTO STRICT IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= EXECUTE COMILLA <instruccion> COMILLA INTO STRICT <listid> PYC"
    t[0] = Execute.Execute(t[2], True, True,t[5],None,'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_ejecutarDinamico4(t):
    '''instruccion : EXECUTE CADENA INTO IDENTIFICADOR USING listid PYC'''
    strGram = "<instruccion> ::= EXECUTE COMILLA <instruccion> COMILLA INTO <listid> USING <expre> PYC"
    t[0] = Execute.Execute(t[2], True, None,t[4],t[6],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_ejecutarDinamico5(t):
    '''instruccion : EXECUTE CADENA INTO STRICT IDENTIFICADOR USING listid PYC'''
    strGram = "<instruccion> ::= EXECUTE COMILLA <instruccion> COMILLA INTO STRICT <listid> USING <expre> PYC"
    t[0] = Execute.Execute(t[2], True, True,t[5],t[7],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_ejecutarDinamico6(t):
    '''instruccion : EXECUTE IDENTIFICADOR PAR1 listid PAR2 PYC'''
    strGram = "<instruccion> ::= EXECUTE CADENA PYC"
    t[0] = ExecuteM.ExecuteM(t[2], t[4], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_ejecutarDinamico7(t):
    '''instruccion : EXECUTE IDENTIFICADOR PAR1 PAR2 PYC'''
    strGram = "<instruccion> ::= EXECUTE CADENA PYC"
    t[0] = ExecuteM.ExecuteM(t[2], None,'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_procedimiento(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE PROCEDURE IDENTIFICADOR PAR1 <listid> PAR2 AS DOLLAR DOLLAR DECLARE <declaraciones> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0] = Procedure.Procedure(t[3], t[5], None, t[11],t[13], '', t.lexer.lineno, t.lexer.lexpos,  strGram )

def p_procedimiento2(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 <listid> PAR2 AS DOLLAR DOLLAR DECLARE <declaraciones> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0] = CreateOrReplace.CreateOrReplace(t[5], t[7],None, t[13], t[15],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_procedimiento3(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE PROCEDURE IDENTIFICADOR PAR1 <listid> PAR2  AS DOLLAR DOLLAR DECLARE <declaraciones> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0] = Procedure.Procedure(t[3], t[5],None, None,t[11], '', t.lexer.lineno, t.lexer.lexpos,  strGram )

def p_procedimiento4(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 <listid> PAR2 AS DOLLAR DOLLAR DECLARE <declaraciones> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0] = CreateOrReplace.CreateOrReplace(t[5], t[7], None, None, t[13],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_procedimiento5(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE PROCEDURE IDENTIFICADOR PAR1 <listid> PAR2 AS DOLLAR DOLLAR DECLARE <declaraciones> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0] = Procedure.Procedure(t[3], None, None, t[11],t[13], '', t.lexer.lineno, t.lexer.lexpos,  strGram )

def p_procedimiento6(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 <listid> PAR2 AS DOLLAR DOLLAR DECLARE <declaraciones> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0] = CreateOrReplace.CreateOrReplace(t[5], None,None, t[13], t[15],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_procedimiento7(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE PROCEDURE IDENTIFICADOR PAR1 <listid> PAR2  AS DOLLAR DOLLAR DECLARE <declaraciones> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0] = Procedure.Procedure(t[3], None,None, None,t[11], '', t.lexer.lineno, t.lexer.lexpos,  strGram )

def p_procedimiento8(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 <listid> PAR2 AS DOLLAR DOLLAR DECLARE <declaraciones> BEGIN <contenidosbegin> END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC"
    t[0] = CreateOrReplace.CreateOrReplace(t[5], None, None, None, t[12],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_llamadaprocedimiento(t):
    '''instruccion : instru_call'''
    t[0]= t[1]

def p_eliminarprocedimiento(t):
    '''instruccion : DROP PROCEDURE listid opciondropprocedure '''
    strGram ="instruccion : DROP PROCEDURE listid opciondropprocedure PYC"
    t[0]= DropPL.DropPL(None, t[3], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_eliminarprocedimiento2(t):
    '''instruccion : DROP PROCEDURE IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure '''
    strGram ="instruccion : DROP PROCEDURE IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure PYC"
    t[0]= DropPL.DropPL(t[1], t[5], t[7], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_eliminarprocedimiento3(t):
    '''instruccion : DROP PROCEDURE IF EXISTS listid opciondropprocedure'''
    strGram ="instruccion : DROP PROCEDURE IF EXISTS listid opciondropprocedure PYC"
    t[0]= DropExistsPL.DropExistsPL(None,t[5], t[6], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_eliminarprocedimiento4(t):
    'instruccion : DROP PROCEDURE IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure '
    strGram ="instruccion : DROP PROCEDURE IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure PYC"

    t[0]= DropExistsPL.DropExistsPL(t[5], t[7],t[9], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_instruccionIndices(t):
    '''instruccion : indice'''
    t[0]= t[1]


def p_opciondropprocedure(t):
    '''opciondropprocedure : CASCADE PYC
                            | RESTRICT PYC
    '''
    t[0]=t[1]
    
def p_opciondropprocedure2(t):
    '''opciondropprocedure : PYC 
    '''
    strGram ="opciondropprocedure : PYC"
    t[0]= Ends.Ends('', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaraciones(t):
    'declaraciones : declaraciones declaracion'
    #strGram = "<declaraciones> ::= <declaraciones><declaracion>"
    t[1].append(t[2])
    t[0] = t[1]

def p_declaraciones2(t):
    'declaraciones : declaracion'
    t[0] = [t[1]]


def p_declaracion(t):
    '''declaracion : IDENTIFICADOR tipo PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> PYC"
    t[0]= VariablePL.VariablePL(t[1], t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_declaracion2(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR CONSTANT <tipo> PYC"
    t[0] = AsignacionConstant.AsignacionesConstant(t[1],t[3],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion3(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR CONSTANT <tipo> COLLATE IDENTIFICADOR PYC"
    t[0]= CollatesConstant.CollatesConstant(t[1], t[3], t[5], None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion4(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR NOT NULL PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR CONSTANT <tipo> COLLATE IDENTIFICADOR NOT null PYC"
    t[0]= CollatesConstant.CollatesConstant(t[1], t[3], t[5], None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion5(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR DEFAULT operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR CONSTANT <tipo> COLLATE IDENTIFICADOR DEFAULT <expre> PYC"
    t[0]= CollatesConstant.CollatesConstant(t[1], t[3], t[5], t[7], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_declaracion6(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= "
    t[0]= CollatesConstant.CollatesConstant(t[1], t[3], t[5], t[8], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_declaracion7(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR CONSTANT <tipo> COLLATE IDENTIFICADOR IGUAL <expre> PYC"
    t[0]= CollatesConstant.CollatesConstant(t[1], t[3], t[5], t[7], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion8(t):
    '''declaracion : IDENTIFICADOR tipo COLLATE IDENTIFICADOR IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> COLLATE IDENTIFICADOR IGUAL <expre> PYC"
    t[0]=Collates.Collates(t[1], t[2], t[4], t[6],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion9(t):
    '''declaracion : IDENTIFICADOR tipo IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> IGUAL <expre> PYC"
    t[0]= AsignacionVariable.AsignacionVariable(t[1], t[2], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion10(t):
    '''declaracion : IDENTIFICADOR tipo COLLATE IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> COLLATE IDENTIFICADOR DOSP IGUAL <expre> PYC"
    t[0]=Collates.Collates(t[1], t[2], t[4], t[7],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion11(t):
    '''declaracion : IDENTIFICADOR tipo DOSP IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> DOSP IGUAL <expre> PYC"
    #verficar si es asignaciones
    t[0]= AsignacionDefault.AsignacionDefault(t[1],t[2], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_declaracion12(t):
    '''declaracion : IDENTIFICADOR tipo DEFAULT operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> DEFAULT <expre> PYC"
    t[0]= AsignacionDefault.AsignacionDefault(t[1],t[2], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion13(t):
    '''declaracion : IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> DOSP IGUAL <expre> PYC"
    t[0]=Asignaciones.Asignaciones(t[1],t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declaracion14(t):
    '''declaracion : IDENTIFICADOR IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> DOSP IGUAL <expre> PYC"
    t[0]=Asignaciones.Asignaciones(t[1],t[3],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declararcursor(t):
    '''declaracion : IDENTIFICADOR REFCURSOR PYC'''
    strGram = "<instruccion> : IDENTIFICADOR REFCURSOR PYC"
    t[0]= RecursorPL.RecursorPL(t[1], None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_declararcursor2(t):
    '''declaracion : IDENTIFICADOR CURSOR FOR CADENA PYC'''
    strGram = "declaracion : IDENTIFICADOR CURSOR FOR CADENA PYC"

    t[0]= CursorScroll.CursorScroll(t[1], None, t[4], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_declararcursor3(t):
    '''declaracion : IDENTIFICADOR SCROLL CURSOR FOR CADENA PYC'''
    strGram = "declaracion : IDENTIFICADOR SCROLL CURSOR FOR CADENA PYC"
    t[0]= CursorScroll.CursorScroll(t[1], None, t[5], '', t.lexer.lineno, t.lexer.lexpos,  strGram)
    #Pendiente de procesar 3D

def p_declararcursor4(t):
    '''declaracion : IDENTIFICADOR NO SCROLL CURSOR FOR CADENA PYC'''
    strGram = "declaracion : IDENTIFICADOR NO SCROLL CURSOR FOR CADENA PYC"

    t[0]= CursorScroll.CursorScroll(t[1], None, t[6], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_declararcursor5(t):
    '''declaracion : IDENTIFICADOR CURSOR PAR1 listid PAR2 FOR CADENA PYC'''
    strGram = "declaracion : IDENTIFICADOR CURSOR PAR1 listid PAR2 FOR CADENA PYC"
    t[0]= CursorScroll.CursorScroll(t[1], t[4], t[7], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_contenidosbegin(t):
    '''contenidosbegin : contenidosbegin contenidobegin'''
    t[1].append(t[2])
    t[0]=t[1]


def p_contenidosbeing(t): 
    '''contenidosbegin : contenidobegin'''
    t[0]= [t[1]]


def p_contenidobegin(t):
    '''contenidobegin : instruccionesPL_gen'''
    strGram = "<instruccion> ::= instruccionesPL_gen"
    t[0] = t[1]

 
def p_contenidobegin2(t):
    '''contenidobegin : CADENA'''
    strGram = "<contenidobegin> ::= CADENA"
    t[0]= ObtenerSql.ObtenerSql(t[1],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_abrircursor(t):
    '''contenidobegin : OPEN IDENTIFICADOR FOR contenidobegin PYC'''
    strGram = "contenidobegin : OPEN IDENTIFICADOR FOR contenidobegin PYC"

    t[0] = OpenPL.OpenPL(t[2], None, t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_abrircursor2(t):
    '''contenidobegin : OPEN IDENTIFICADOR SCROLL FOR contenidobegin PYC'''
    strGram = "contenidobegin : OPEN IDENTIFICADOR SCROLL FOR contenidobegin PYC"

    t[0] = OpenPL.OpenPL(t[2], True, t[5],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_abrircursor3(t):
    '''contenidobegin : OPEN IDENTIFICADOR NO SCROLL FOR contenidobegin PYC'''
    strGram = "contenidobegin : OPEN IDENTIFICADOR NO SCROLL FOR contenidobegin PYC"
    t[0] = OpenPL.OpenPL(t[2], False, t[5],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_abrircursor4(t):
    '''contenidobegin : OPEN IDENTIFICADOR PYC'''
    strGram = "contenidobegin : OPEN IDENTIFICADOR PYC"

    t[0] = OpenPL.OpenPL(t[2], None, None,'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_abrircursor5(t):
    '''contenidobegin : OPEN IDENTIFICADOR listid PYC'''
    strGram = "contenidobegin : OPEN IDENTIFICADOR listid PYC"

    t[0] = OpenPL.OpenPL(t[2], None, t[3],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_usandocursor6(t):
    '''contenidobegin : FETCH IDENTIFICADOR INTO listid PYC'''
    strGram = "contenidobegin : FETCH IDENTIFICADOR INTO listid PYC"

    t[0]= FetchInto.FetchInto(t[2], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_usandocursor7(t):
    '''contenidobegin : FETCH direction FROM IDENTIFICADOR INTO listid PYC'''
    strGram = "contenidobegin : FETCH direction FROM IDENTIFICADOR INTO listid PYC"

    t[0] = FetchFromInto.FetchFromInto(t[2], t[4], t[6],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_usandocursor8(t):
    '''contenidobegin : FETCH direction IN IDENTIFICADOR INTO listid PYC'''
    strGram = "contenidobegin : FETCH direction IN IDENTIFICADOR INTO listid PYC"

    t[0] = FetchIn.FetchIn(t[2], t[4], t[6], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_usandocursor9(t):
    '''contenidobegin : MOVE IDENTIFICADOR PYC'''
    strGram = "contenidobegin : MOVE IDENTIFICADOR PYC"

    t[0]= Move.Move(t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_usandocursor10(t):
    '''contenidobegin : MOVE direction FROM IDENTIFICADOR PYC'''
    strGram = "contenidobegin : MOVE direction FROM IDENTIFICADOR PYC"

    t[0]= MoveFrom.MoveFrom(t[2], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_usandocursor11(t):
    '''contenidobegin : MOVE direction IN IDENTIFICADOR PYC'''
    strGram = "contenidobegin : MOVE direction IN IDENTIFICADOR PYC"

    t[0]= MoveIn.MoveIn(t[2], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_usandocursor12(t):
    '''contenidobegin : UPDATE IDENTIFICADOR SET instru_set WHERE CURRENT OF IDENTIFICADOR PYC'''
    strGram = "contenidobegin : UPDATE IDENTIFICADOR SET instru_set WHERE CURRENT OF IDENTIFICADOR PYC"
    t[0]= Update.Upadte(t[2], t[4], t[8],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_usandocursor13(t):
    '''contenidobegin : UPDATE IDENTIFICADOR SET instru_set WHERE operacion_logica PYC'''
    strGram = "contenidobegin : UPDATE IDENTIFICADOR SET instru_set WHERE operacion_logica PYC"
    t[0]= UpdateOper.UpadteOper(t[2], t[4], t[6],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_usandocursor14(t):
    '''contenidobegin : DELETE FROM IDENTIFICADOR WHERE CURRENT OF IDENTIFICADOR PYC'''
    strGram = "contenidobegin : DELETE FROM IDENTIFICADOR WHERE CURRENT OF IDENTIFICADOR PYC"
    t[0] = Deletes.Deletes(t[3], t[7],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_cerrandocursor(t):
    '''contenidobegin : CLOSE IDENTIFICADOR PYC'''
    strGram = "contenidobegin : CLOSE IDENTIFICADOR PYC"
    t[0]= Closes.Closes(t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

#get RESULT STATUS

def p_getstatus(t):
    '''contenidobegin : GET DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC'''
    strGram = "<instruccion> ::= GET DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC"
    t[0] = Gets.Gets(t[3], t[5], '', t.lexer.lineno, t.lexer.lexpos,  strGram)
def p_getstatus2(t):
    '''contenidobegin : GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC'''
    strGram = "<instruccion> ::= GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC"
    t[0] = GetsCurrent.GetsCurrent(t[4], t[6], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_getstatus3(t):
    '''contenidobegin : GET DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC'''
    strGram = "<instruccion> ::= GET DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC"
    t[0] = Gets.Gets(t[3], t[5], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_getstatus4(t):
    '''contenidobegin : GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC'''
    strGram = "<instruccion> ::= GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC"
    t[0] = GetsCurrent.GetsCurrent(t[4], t[6], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

#NOTHING AT ALL- VACIO

def p_nada(t):
    '''contenidobegin : NULL PYC'''
    strGram = "<instruccion> ::= NULL PYC" 
    t[0]= Ends.Ends('', t.lexer.lineno, t.lexer.lexpos,  strGram)

#alias
def p_alias(t):
    '''instruccion : IDENTIFICADOR ALIAS FOR IDENTIFICADOR PYC'''
    strGram = "<instruccion> ::= IDENTIFICADOR ALIAS FOR IDENTIFICADOR PYC"
    t[0] = Alias.Alias(t[1], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram) 


def p_return(t):
    '''contenidobegin : RETURN operacion_logica PYC'''
    strGram = "<instruccion> ::= RETURN <operacion_logica> PYC"
    t[0] = Returns.Returns(t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)
    

#instruccionesPL DE CICLOS
def p_instruccionesPL_gen(t): 
    'instruccionesPL_gen : instruccionesPL_gen instruccionesPL_pl '
	#strGram = "<instruccionesPL_gen> ::= instruccionesPL_pl instruccionesPL_gen"
    t[1].append(t[2])
    t[0]= t[1]


def p_instruccionesPL_gen1(t): 
    '''instruccionesPL_gen : instruccionesPL_pl'''
    strGram = "<instruccionesPL_gen> ::= instruccionesPL_pl"
    t[0]= [t[1]]


def p_instruccionesPL_pl(t):
    '''instruccionesPL_pl : sentencia_if
							  | sentencia_case
							  | sentencia_loop
							  | instru_exit
							  | instru_except
							  | instru_get_error
							  | instru_return
							  | operacion_logica
                              | asignacion
    '''
    t[0]= t[1]

def p_asignar(t):
    '''asignacion : IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    strGram = "<instruccion> ::= IDENTIFICADOR <tipo> DOSP IGUAL <expre> PYC"
    t[0]=Asignaciones.Asignaciones(t[1],t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_asignar2(t):
    '''asignacion : IDENTIFICADOR IGUAL operacion_logica PYC''' 
    strGram = "<asignacion> ::= IDENTIFICADOR <tipo> DOSP IGUAL <expre> PYC"
    t[0]=Asignaciones.Asignaciones(t[1],t[3],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_sentencia_if(t):
    '''sentencia_if : if_simple
							 | if_con_else	
							 | if_con_elsif'''

    t[0]= t[1]


def p_if_simple(t):
    '''if_simple : IF operacion_logica THEN instruccionesPL_gen END IF PYC'''
    strGram = "<if_simple> ::= IF operacion_logica THEN instruccionesPL_gen END IF PYC"
    t[0]= Ifs.Ifs(t[2], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_if_con_else(t):
    '''if_con_else : IF operacion_logica THEN instruccionesPL_gen ELSE instruccionesPL_gen END IF PYC'''
    strGram = "<if_con_else> ::= IF operacion_logica THEN instruccionesPL_gen else instruccionesPL_gen END IF PYC"
    t[0]= IfsElse.IfsElse(t[2], t[4],t[6],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_if_con_elsif(t):
    '''if_con_elsif : IF operacion_logica THEN instruccionesPL_gen cont_if'''
    strGram = "<if_con_elsif> ::= IF operacion_logica THEN instruccionesPL_gen cont_if"
    t[0]= IfsElseIf.IfsElseIf(t[2], t[4],t[5],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_cont_if1(t):
    '''cont_if : ELSIF operacion_logica THEN instruccionesPL_gen cont_if'''
    strGram = "<cont_if> ::= ELSIF operacion_logica THEN instruccionesPL_gen cont_if"
    t[0] = IfsElseIf.IfsElseIf(t[2], t[4], t[5],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_cont_if2(t):
    '''cont_if : ELSE instruccionesPL_gen cont_if'''
    strGram = "<cont_if> ::= else instruccionesPL_gen cont_if"
    t[0] = Elses.Elses(t[2], t[3],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_cont_if3(t):
    '''cont_if : END IF PYC'''
    strGram = "<cont_if> ::= END IF PYC"
    ##este if debe verficarse
    t[0]= Ends.Ends('', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_sentencia_case(t):
    '''sentencia_case : CASE operacion_logica list_contentcase end_case'''
    strGram = "<sentencia_case> ::= CASE operacion_logica cont_case"
    t[0] = Cases.Cases(t[2], t[3], t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_listContentCase(t):
    '''list_contentcase : list_contentcase cont_case'''
    t[1].append(t[2])
    t[0]= t[1]

def p_listContentCase2(t):
    '''list_contentcase : cont_case'''
    t[0]= [t[1]]

def p_cont_case1(t):
    '''cont_case : WHEN lista_op THEN instruccionesPL_gen PYC'''
    strGram = "<cont_case> ::= WHEN lista_op THEN instruccionesPL_gen"
    t[0] = WhenPL.WhenPL(t[2], t[4], None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_cont_case2(t):
    '''cont_case : ELSE instruccionesPL_gen PYC'''
    strGram = "<cont_case> ::= ELSE instruccionesPL_gen"
    t[0] = CaseElse.CaseElse(t[2], None, '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_cont_case3(t):
    '''end_case : END CASE PYC'''
    strGram = "<end_case> ::= END CASE PYC"
    t[0]= Ends.Ends('', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_lista_op1(t):
    '''lista_op : lista_op COMA operacion_logica'''
    strGram = "<lista_op> ::= lista_op COMA operacion_logica"
    t[1].append(t[3])
    t[0] = t[1] 

def p_lista_op2(t):
    '''lista_op : operacion_logica'''
    strGram = "<lista_op> ::= operacion_logica"
    t[0]= [t[1]]

def p_sentencia_loop(t):
    '''sentencia_loop : LOOP instruccionesPL_gen END LOOP PYC'''
    strGram = "<sentencia_loop> ::= LOOP instruccionesPL_gen END LOOP PYC"
    t[0]= LoopPL.LoopPL(t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_instru_exit(t):
    '''instru_exit : EXIT  PYC'''
    strGram = "<instru_exit> ::= EXIT PYC"
    t[0] = Exits.Exits(t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_instru_exit2(t):
    '''instru_exit : EXIT IDENTIFICADOR PYC'''
    strGram = "<instru_exit> ::= EXIT cont_instru"
    t[0] = Exits.Exits(t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_sentencia_case2(t):
    '''sentencia_case : CASE list_contentcase end_case'''
    strGram = "<instru_exit> ::= EXIT cont_instru"
    t[0] = Cases.Cases(None, t[2], t[3],'', t.lexer.lineno, t.lexer.lexpos,  strGram)
def p_instru_except(t):
    '''instru_except : EXCEPTION cont_except'''
    strGram = "<instru_except> ::= EXCEPTION cont_except"
    t[0] = Exceptions.Exceptions(t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_cont_except1(t):
    '''cont_except : WHEN operacion_logica THEN RAISE EXCEPTION resultadoexception'''
    strGram = "<ont_except> ::= WHEN  operacion_logica THEN RAISE EXCEPTION resultadoexception"
    t[0] = WhenExcept.WhenExcept(t[2], t[6], '', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_resultadoexception(t):
    '''resultadoexception : CADENACARACTER COMA IDENTIFICADOR PYC'''
    strGram='<resultadoexception> ::= CADENACARACTER COMA IDENTIFICADOR PYC'
    t[0]= ResultExcept.ResultExcept(t[1], t[3])
def p_resultadoexception2(t):
    '''resultadoexception : CADENACARACTER PYC'''
    strGram='<resultadoexception> ::= CADENACARACTER PYC'
    t[0] = PrimitivoPL.PrimitivoPL( t[1],Tipo_DatoPL.CHAR , strGram, t.lexer.lineno, t.lexer.lexpos)


def p_resultadoexception3(t):
    '''resultadoexception : CADENA PYC'''
    strGram='<resultadoexception>::= CADENA PYC'
    t[0] = PrimitivoPL.PrimitivoPL( t[1],Tipo_DatoPL.VARCHAR , strGram, t.lexer.lineno, t.lexer.lexpos)
    

def p_instru_get_error(t):
    '''instru_get_error : GET STACKED DIAGNOSTICS IDENTIFICADOR cont_get'''
    strGram = "<instru_get_error> ::= GET STACKED DIAGNOSTICS IDENTIFICADOR cont_get"
    t[0] = GetStacked.GetStacked(t[4],t[5], '', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_cont_get1(t):
    '''cont_get : IGUAL operacion_logica'''
    strGram = "<cont_get> ::= IGUAL operacion_logica"
    t[0] = t[2]

def p_cont_get2(t):
    '''cont_get : DOSP IGUAL operacion_logica'''
    strGram = "<cont_get> ::= DOSP IGUAL operacion_logica"
    t[0] = t[3]

def p_instru_return1(t):
    '''instru_return : RETURN operacion_logica PYC'''
    strGram = "<instru_return> ::= RETURN operacion_logica PYC"
    t[0]= Returns.Returns(t[2],'', t.lexer.lineno, t.lexer.lexpos,  strGram)
def p_instru_return2(t):
    '''instru_return : RETURN QUERY CADENA PYC'''
    strGram = "<instru_return> ::= RETURN query SELECT"

    t[0]= ReturnsQuery.ReturnsQuery(t[3],'', t.lexer.lineno, t.lexer.lexpos,  strGram)
def p_instru_return3(t):
    '''instru_return : RETURN QUERY EXECUTE CADENA PYC'''
    strGram = "<instru_return> ::= RETURN query EXECUTE SELECT"
    t[0]= ReturnsQuery.ReturnsQueryExecute(t[4],'', t.lexer.lineno, t.lexer.lexpos,  strGram)

def p_instru_return4(t):
    '''instru_return : RETURN NEXT operacion_logica PYC'''
    strGram = '<instru_return> :: = RETURN NEXT operacion_logica PYC'
    t[0]=ReturnsNext.ReturnsNext(t[3],'', t.lexer.lineno, t.lexer.lexpos,  strGram)


def p_instru_call(t):
    '''instru_call : CALL IDENTIFICADOR PAR1 operacion_logica PAR2 PYC'''
    strGram = "<instru_call> ::= CALL IDENTIFICADOR PAR1 operacion_logica PAR2 PYC"
    t[0]= CallFun(t[2],t[4],None,strGram,t.lexer.lineno, t.lexer.lexpos)


#EXPRESIONES LOGICAS, ARITMETICAS Y RELACIONALES AQUI-->


def p_instru_set(t):
    '''instru_set : instru_set COMA operacion_logica'''
    strGram = "<instru_set> ::= <instru_set> COMA <operacion_logica>"
    t[0] = InstruSet(t[1],None,strGram,t.lexer.lineo, t.lexer.lexpos)


def p_instru_set2(t):
    '''instru_set : operacion_logica'''
    t[0]=t[1]

	
def p_op_logica(t):
    '''operacion_logica : operacion_logica AND operacion_logica
						 | operacion_logica OR operacion_logica
    '''    
    strGram = ""
    if t[2] == "OR":
        strGram = "<expre> ::= <expre> OR <expre>"
    elif t[2] == "AND":
        strGram = "<expre> ::= <expre> AND <expre>"

    t[0] = LogicaPL.LogicaPL(t[1], t[3], t[2].upper(), strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_logica2(t):
    '''operacion_logica :  NOT operacion_logica'''
    strGram = "<operacion_logica> ::= operacion_logica signo operacion_logica"
    t[0] = LogicaPL.LogicaPL(t[2], None, 'NOT', strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_logica1(t):
    '''operacion_logica : operacion_relacional'''
    strGram = "<operacion_logica> ::= operacion_relacional"
    t[0]=t[1]

def p_op_relacional(t):
    '''operacion_relacional : operacion_relacional MAYOR operacion_relacional
							 | operacion_relacional MENOR operacion_relacional
							 | operacion_relacional MAYORIGUAL operacion_relacional
		 					 | operacion_relacional MENORIGUAL operacion_relacional
							 | operacion_relacional DIFERENTE operacion_relacional
							 | operacion_relacional IGUAL operacion_relacional'''
    strGram = ""
    if t[2] == "IGUAL":
        strGram = "<operacion_relacional> ::= <operacion_relacional> IGUAL <operacion_relacional>"
    elif t[2] == "MAYORIGUAL":
        strGram = "<operacion_relacional> ::= <operacion_relacional> MAYORIGUAL <operacion_relacional>"
    elif t[2] == "MENORIGUAL":
        strGram = "<operacion_relacional> ::= <operacion_relacional> MENORIGUAL <operacion_relacional>"
    elif t[2] == "MENOR":
        strGram = "<operacion_relacional> ::= <operacion_relacional> MENOR <operacion_relacional>"
    elif t[2] == "MAYOR":
        strGram = "<operacion_relacional> ::= <operacion_relacional> MAYOR <operacion_relacional>"
    elif t[2] == "DIFERENTE":
        strGram = "<operacion_relacional> ::= <operacion_relacional> DIFERENTE <operacion_relacional>"
    t[0] = RelacionalPL.RelacionalPL(t[1], t[3], t[2],strGram ,t.lexer.lineno, t.lexer.lexpos)


def p_op_relacional1(t):
    '''operacion_relacional : operacion_aritmetica'''
    strGram = "<operacion_relacional> ::= operacion_aritmetica"
    t[0]=t[1]

def p_op_aritmetica1(t):
    '''operacion_aritmetica : operacion_aritmetica MAS operacion_aritmetica
							 | operacion_aritmetica MENOS operacion_aritmetica
							 | operacion_aritmetica POR operacion_aritmetica
							 | operacion_aritmetica DIVISION operacion_aritmetica
                             | operacion_aritmetica EXPONENCIACION operacion_aritmetica
                             | operacion_aritmetica PORCENTAJE operacion_aritmetica'''
    strGram = ""
    if t[2] == "MAS":
        strGram = "<operacion_aritmetica> ::= <operacion_aritmetica> MAS <operacion_aritmetica>"
    elif t[2] == "MENOS":
        strGram = "<operacion_aritmetica> ::= <operacion_aritmetica> MENOS <operacion_aritmetica>"
    elif t[2] == "POR":
        strGram = "<operacion_aritmetica> ::= <expre> POR <operacion_aritmetica>"
    elif t[2] == "DIVISION":
        strGram = "<operacion_aritmetica> ::= <operacion_aritmetica> DIVISION <operacion_aritmetica>"
    elif t[2] == "EXPONENCIACION":
        strGram = "<operacion_aritmetica> ::= <operacion_aritmetica> EXPONENCIACION <operacion_aritmetica>"
    elif t[2] == "PORCENTAJE":
        strGram = "<operacion_aritmetica> ::= <operacion_aritmetica> MODULO <operacion_aritmetica>"

    t[0]= AritmeticaPL.AritmeticaPL(t[1],t[3],t[2],strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_aritmetica2(t):
    '''operacion_aritmetica : PAR1 operacion_logica PAR2'''
    strGram = "<operacion_aritmetica> ::= par1 operacion_aritmetica par2"
    t[0]=t[2]

def p_op_aritmetica3(t):
    '''operacion_aritmetica : valor'''
    strGram = "<operacion_aritmetica> ::= valor"
    t[0]=t[1]

def p_direccion(t):
    '''direction : NEXT 
    '''
    strGram = "<direction> ::= NEXT"
    t[0] = t[1]

def p_direccion8(t):
    '''direction : LAST 
    '''
    strGram = "<direction> ::= LAST"
    t[0] = t[1]

def p_direccion9(t):
    '''direction : PRIOR 
    '''
    strGram = "<direction> ::= PRIOR"
    t[0] = t[1]

def p_direccion10(t):
    '''direction : FIRST 
    '''
    strGram = "<direction> ::= FIRST"
    t[0] = t[1]

def p_direccion2(t):
    '''direction : ABSOLUTE valor'''
    strGram = "<direction> ::= ABSOLUTE  valor "
    t[0] = Directions(t[2],Direction_Enum.ABSOLUTE,'', strGram, t.lexer.lineno, t.lexer.lexpos)
    
def p_direccion3(t):
    '''direction : RELATIVE valor'''
    strGram = "<direction> ::= RELATIVE  valor "
    t[0] = Directions(t[2],Direction_Enum.RELATIVE,'', strGram, t.lexer.lineno, t.lexer.lexpos)


def p_direccion4(t):
    '''direction : FORWARD valor'''
    strGram = "<direction> ::= FORWARD  valor "
    t[0] = Directions(t[2],Direction_Enum.FORWARD, '',strGram, t.lexer.lineno, t.lexer.lexpos)
    

def p_direccion5(t):
    '''direction : BACKWARD valor'''
    strGram = "<direction> ::= ABSOLUTE  valor "
    t[0] = Directions(t[2],Direction_Enum.BACKWARD,'', strGram, t.lexer.lineno, t.lexer.lexpos)
    

def p_crearindices(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 PYC'''
    strGram = "<indice> ::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC"
    t[0]=IndicePL1.IndicePL1(t[3], t[5], t[7], '',strGram, t.lexer.lineno, t.lexer.lexpos)


def p_crearindices0(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC'''
    strGram = "<indice> ::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC"
    t[0]=IndicePL1.IndicePL1(t[3], t[5], t[7], '',strGram, t.lexer.lineno, t.lexer.lexpos)

#Aqui en using especifica el nombre del metodo que se esta usando, como HASH, btree, etc
#por eso lo puse como identificador tambien-->


def p_crearindices2(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR USING IDENTIFICADOR PAR1 listid PAR2 PYC'''
    strGram = "<indice> ::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR USING HASH PAR1 IDENTIFICADOR PAR2 PYC"
    t[0]=IndicePLUsing.IndicePLUsing(t[3], t[5], t[7], t[9],'',strGram, t.lexer.lineno, t.lexer.lexpos)

def p_crearindices3(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR NULLS ordenposicion PAR2 PYC'''
    strGram = "<indice> ::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR NULLS ordenposicion PAR2 PYC"
    t[0] = IndicePLUsingNull.IndicePLUsingNull(t[3], t[5], t[7], None,  t[9],'',strGram, t.lexer.lineno, t.lexer.lexpos)

def p_crearindices4(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR ASC NULLS ordenposicion PAR2 PYC'''
    strGram = "<indice> ::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR ASC NULLS ordenposicion PAR2 PYC"
    t[0]= IndicePLUsingNull.IndicePLUsingNull(t[3], t[5], t[7],t[8], t[10], '',strGram, t.lexer.lineno, t.lexer.lexpos)

def p_crearindices5(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR DESC NULLS ordenposicion PAR2 PYC'''
    strGram = "<indice> ::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR DESC NULLS ordenposicion PAR2 PYC"
    #t[0] = IndicePL(t[3],t[5],None,None,None,None,t[7],None, strGram, t.lexer.lineno, t.lexer.lexpos)
    t[0]= IndicePLUsingNull.IndicePLUsingNull(t[3], t[5], t[7],t[8], t[10],'',strGram, t.lexer.lineno, t.lexer.lexpos)

def p_crearindices6(t):
    '''indice : CREATE UNIQUE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC'''
    strGram = "<indice> ::= CREATE UNIQUE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC"
   # t[0] = IndicePL(t[3],t[5],None,None,None,None,t[7],None, strGram, t.lexer.lineno, t.lexer.lexpos)
    t[0]=IndicePLUnique.IndicePLUnique(t[4], t[6], t[8],'',strGram, t.lexer.lineno, t.lexer.lexpos )
    

def p_crearindices7(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 LOWER PAR1 IDENTIFICADOR PAR2 PAR2 PYC'''
    strGram = "<indice> ::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 LOWER PAR1 IDENTIFICADOR PAR2 PAR2 PYC"
    t[0]= IndicePL7.IndicePL7(t[3],t[5],t[9],'',strGram, t.lexer.lineno, t.lexer.lexpos)
   
def p_crearindices8(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE NOT PAR1 operacion_logica PAR2 PYC'''
    strGram = "<indice> ::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE NOT PAR1 operacion_logica PAR2 PYC"
    t[0]= IndicePL8.IndicePL8(t[3],t[5],t[7],t[12],'',strGram, t.lexer.lineno, t.lexer.lexpos)
   

def p_crearindices9(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE operacion_logica PYC'''
    
    strGram = "<indice> ::=CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE operacion_logica PYC"
    t[0]= IndicePL9.IndicePL9(t[3],t[5],t[7],t[10],'',strGram, t.lexer.lineno, t.lexer.lexpos)
   

def p_dropindices1(t):
    'indice : DROP INDEX IF EXISTS listid opciondropprocedure'
    strGram ="<indice> : DROP INDEX IF EXISTS listid opciondropprocedure"
    t[0] = DropIndiceIf.DropIndiceIf(t[5],t[6],'',strGram, t.lexer.lineno, t.lexer.lexpos)


def p_dropindices2(t):
    'indice : DROP INDEX listid opciondropprocedure'
    strGram ="<indice> : DROP INDEX <listid> opciondropprocedure"
    t[0] = DropIndice.DropIndice(t[3],t[4],'',strGram, t.lexer.lineno, t.lexer.lexpos)


def p_alterindices2(t):
    'indice : ALTER INDEX IDENTIFICADOR ALTER COLUMN IDENTIFICADOR IDENTIFICADOR PYC'
    strGram ="<indice>: ALTER INDEX IDENTIFICADOR ALTER COLUMN IDENTIFICADOR IDENTIFICADOR PYC"
    t[0] = AlterIndice.AlterIndice(t[3],t[6],t[7],'',strGram, t.lexer.lineno, t.lexer.lexpos)


def p_alterindices3(t):
    'indice : ALTER INDEX IDENTIFICADOR ALTER IDENTIFICADOR IDENTIFICADOR PYC'
    strGram="<indice>: ALTER INDEX IDENTIFICADOR ALTER IDENTIFICADOR IDENTIFICADOR PYC"
    t[0] = AlterIndice.AlterIndice(t[3],t[5],t[6],'',strGram, t.lexer.lineno, t.lexer.lexpos)


def p_ordenposicion(t):
    'ordenposicion : FIRST'

    t[0] = t[1]


def p_ordenposicion2(t):
    'ordenposicion : LAST'''
    t[0]= t[1]


def p_listaIDENTIFICADOR(t):
    'listid : listid COMA parametro'
    strGram = "<listid> ::= <listid>   COMA paramametro "
    t[1].append(t[3])
    t[0]=t[1]

def p_listaIDENTIFICADOR2(t):
    'listid : parametro'
    t[0]= [t[1]]

def p_parametro3(t):
    'parametro : IDENTIFICADOR tipo'
    strGram = "<parametro> ::=  IDENTIFICADOR tipo  \n"
    t[0] = Parametro.Parametro(t[1],t[2], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_parametro(t):
    'parametro : IDENTIFICADOR'
    strGram = "<parametro> ::= IDENTIFICADOR"
    t[0] = IdentificadorPL.IdentificadorPL(t[1], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_parametro4(t):
    'parametro : INOUT IDENTIFICADOR tipo'
    strGram = "<parametro> ::= INOUT IDENTIFICADOR tipo  \n"
    t[0] = InOutIdentificador.InOutIdentificador(t[2],t[3], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_parametro5(t):
    'parametro : OUT IDENTIFICADOR tipo'
    strGram = "<parametro> ::= OUT IDENTIFICADOR tipo"
    t[0] = OutIdentificador.OutIdentificador(t[2],t[3], strGram, t.lexer.lineno, t.lexer.lexpos)


def p_parametro2(t):
    'parametro : tipo'
    t[0]= t[1] 


def p_parametro6(t):
    'parametro : valor'
    t[0]= t[1] 


def p_valor(t):
    '''valor : NUM
    '''
    strGram = "<valor> ::= NUM \n"
    t[0] = PrimitivoPL.PrimitivoPL( t[1],Tipo_DatoPL.NUMERIC , strGram, t.lexer.lineno, t.lexer.lexpos)
	
def p_valor2(t):
    '''valor : CADENA
    '''
    strGram = "<valor> ::= CADENA\n"
    t[0] = PrimitivoPL.PrimitivoPL( t[1],Tipo_DatoPL.VARCHAR , strGram, t.lexer.lineno, t.lexer.lexpos)


def p_valor3(t):
    '''valor : PDECIMAL
    '''
    strGram = "<valor> ::= PDECIMAL\n"
    t[0] = PrimitivoPL.PrimitivoPL( t[1],Tipo_DatoPL.DECIMAL , strGram, t.lexer.lineno, t.lexer.lexpos)


def p_valor4(t):
    '''valor : IDENTIFICADOR
    '''
    strGram = "<valor> ::= IDENTIFICADOR\n"
    t[0] = IdentificadorPL.IdentificadorPL(t[1], strGram, t.lexer.lineno, t.lexer.lexpos)


def p_valor5(t):
    '''valor : CADENACARACTER
    '''
    strGram = "<valor> ::= CADENACARACTER\n"
    t[0] = PrimitivoPL.PrimitivoPL( t[1],Tipo_DatoPL.CHAR , strGram, t.lexer.lineno, t.lexer.lexpos)


#TIPO DE DATOS 


def p_tipo_datos_int6(t):
    '''tipo : DOUBLE PRECISION
    '''
    t[0]=TipoPL(Tipo_DatoPL.DOUBLE_PRECISION)



def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP
    '''
    t[0]=TipoPL(Tipo_DatoPL.TIMESTAMP)


def p_tipo(t):
    '''tipo : SMALLINT 
    '''
    t[0] = TipoPL(Tipo_DatoPL.SMALLINT)
    
def p_tipo_1(t):
    '''tipo : INTEGER 
    '''
    t[0] = TipoPL(Tipo_DatoPL.INTEGER)

def p_tipo_2(t):
    '''tipo : BIGINT 
    '''
    t[0] = TipoPL(Tipo_DatoPL.BIGINT)


def p_tipo15(t):
    '''tipo : DECIMAL PAR1 valdecimal PAR2
    '''
    strGram = "<valor> ::= PDECIMAL\n"
    t[0] = PrimitivoPL.PrimitivoPL( t[1],Tipo_DatoPL.DECIMAL , strGram, t.lexer.lineno, t.lexer.lexpos)


def p_tipo_3(t):
    '''tipo : DECIMAL 
    '''
    t[0] = TipoPL(Tipo_DatoPL.DECIMAL)
def p_tipo_4(t):
    '''tipo : NUMERIC 
    '''
    t[0] = TipoPL(Tipo_DatoPL.NUMERIC)
def p_tipo_5(t):
    '''tipo : REAL 
    '''
    t[0] = TipoPL(Tipo_DatoPL.REAL)

def p_tipo_6(t):
    '''tipo : DOUBLE 
    '''
    t[0] = TipoPL(Tipo_DatoPL.DOUBLE_PRECISION)

def p_tipo_7(t):
    '''tipo : MONEY 
    '''
    t[0] = TipoPL(Tipo_DatoPL.MONEY)

def p_tipo_8(t):
    '''tipo : CHARACTER 
    '''
    t[0] = TipoPL(Tipo_DatoPL.CHARACTER)

def p_tipo_10(t):
    '''tipo : TEXT 
    '''
    t[0] = TipoPL(Tipo_DatoPL.TEXT)

def p_tipo_11(t):
    '''tipo : DATE 
    '''
    t[0] = TipoPL(Tipo_DatoPL.DATE)

def p_tipo_12(t):
    '''tipo : BOOLEAN 
    '''
    t[0] = TipoPL(Tipo_DatoPL.BOOLEAN)

def p_tipo_13(t):
    '''tipo : INT 
    '''
    t[0] = TipoPL(Tipo_DatoPL.NUMERIC)

def p_tipo_14(t):

    '''tipo : IDENTIFICADOR 
    '''
    t[0] = TipoPL(Tipo_DatoPL.TIPOENUM)


def p_valdecimal(t):
    '''valdecimal : valdecimal COMA NUM'''
    t[1].append(t[3])
    t[0] = t[1] 


def p_valdecimal2(t):
    '''valdecimal : NUM'''
    t[0]=t[1]


def p_tipo_datos_varchar(t):
    '''tipo : VARCHAR PAR1 NUM PAR2
    '''
    t[0] = TipoPL(Tipo_DatoPL.VARCHAR,t[3])

def p_tipo_datos_vaying(t):
    '''tipo : VARYING PAR1 NUM PAR2
    '''
    t[0] = TipoPL(Tipo_DatoPL.VARYING,t[3])

def p_tipo_datos_character(t):
    '''tipo : CHARACTER PAR1 NUM PAR2
    '''
    t[0] = TipoPL(Tipo_DatoPL.CHARACTER,t[3])
def p_tipo_datos_char(t):
    '''tipo : CHAR PAR1 NUM PAR2
    '''
    t[0] = TipoPL(Tipo_DatoPL.CHAR,t[3])
def p_tipo_datos_char2(t):
    '''tipo : VARCHAR
    '''
    t[0] = TipoPL(Tipo_DatoPL.VARCHAR,t[1])


# def p_error(t):
#     print("EntrANDo a errOR **********")
#     print(t.value)
#     print(t.lineno)
#     if t:
#         parser.errok()
#     else:
#         print("SQL statement NOT yet complete")

def p_error(t):
    if not t:
        print("Fin del archivo")
        return
    dato = ExceptionPL(1, "Error Sintactico", f"se esperaba una  instruccion y viene {t.value}",t.lexer.lineno, find_column(lexer.lexdata,t))
    lista_lexicos.append(dato)
    while True:   
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PYC':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con ;")
                break
        dato = ExceptionPL(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {tok.value}", t.lexer.lineno, find_column(lexer.lexdata,tok))
        lista_lexicos.append(dato)
        
    parser.restart()

def find_column(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    ast_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

parser = yacc.yacc()

#f = open("entrada.txt", "r")
#input = f.read()
#print(input)

def getParser(input):
    global columna
    lista_lexicos.clear()
    columna=0
    resultado = parser.parse(input.upper())
    return resultado
