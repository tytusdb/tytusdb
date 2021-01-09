from ply import *
from lexico_pl import *
import nodo as grammer
import graficas as generar

listGrammer = []

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
    '''init : instruccionesPL'''
    instru = grammer.nodoGramatical('init')
    instru.agregarDetalle('::= instruccionesPL')
    listGrammer.insert(0,instru)


def p_instruccionesPL_lista1(t):
    '''instruccionesPL : instruccionesPL instruccion'''
    instru = grammer.nodoGramatical('instruccionesPL')
    instru.agregarDetalle('::= instruccionesPL instruccion')
    listGrammer.insert(0,instru)


def p_instruccionesPL_lista2(t):
    '''instruccionesPL : instruccion'''
    instru = grammer.nodoGramatical('instruccionesPL')
    instru.agregarDetalle('::= instruccion')
    listGrammer.insert(0,instru)


def p_instruccionesSQL(t):
    '''instruccion : CADENA'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CADENA')
    listGrammer.insert(0,instru)


def p_funciones(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR BEGIN contenidosbegin END PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR BEGIN contenidosbegin END PYC')
    listGrammer.insert(0,instru)


def p_funciones2(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 BEGIN contenidosbegin END PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 BEGIN contenidosbegin END PYC')
    listGrammer.insert(0,instru)


def p_funciones22(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1  PAR2 BEGIN contenidosbegin END PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR PAR1  PAR2 BEGIN contenidosbegin END PYC')
    listGrammer.insert(0,instru)
    


def p_funciones3(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS operacion_logica BEGIN contenidosbegin END PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS operacion_logica BEGIN contenidosbegin END PYC')
    listGrammer.insert(0,instru)


def p_funciones4(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_funciones45(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1  PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR PAR1  PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_funciones5(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_funciones6(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_funciones7(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_funciones8(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_funciones9(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_funciones10(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_funciones11(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_eliminarfuncion(t):
    '''instruccion : DROP FUNCTION listid opciondropprocedure '''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= DROP FUNCTION listid opciondropprocedure')
    listGrammer.insert(0,instru)


def p_eliminarfuncion2(t):
    '''instruccion : DROP FUNCTION IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure '''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= DROP FUNCTION IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure')
    listGrammer.insert(0,instru)


def p_eliminarfuncion3(t):
    '''instruccion : DROP FUNCTION IF EXISTS listid opciondropprocedure'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= DROP FUNCTION IF EXISTS listid opciondropprocedure')
    listGrammer.insert(0,instru)

def p_eliminarfuncion4(t):
    'instruccion : DROP FUNCTION IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure '
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= DROP FUNCTION IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure')
    listGrammer.insert(0,instru)


def p_ejecutarFunVoid(t):
    '''instruccion : PERFORM IDENTIFICADOR PAR1 listid PAR2 PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= PERFORM IDENTIFICADOR PAR1 listid PAR2 PYC')
    listGrammer.insert(0,instru)


def p_ejecutarDinamico(t):
    '''instruccion : EXECUTE CADENA PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= EXECUTE CADENA PYC')
    listGrammer.insert(0,instru)


def p_ejecutarDinamico2(t):
    '''instruccion : EXECUTE CADENA INTO IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= EXECUTE CADENA INTO IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_ejecutarDinamico3(t):
    '''instruccion : EXECUTE CADENA INTO STRICT IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= EXECUTE CADENA INTO STRICT IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_ejecutarDinamico4(t):
    '''instruccion : EXECUTE CADENA INTO IDENTIFICADOR USING listid PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= EXECUTE CADENA INTO IDENTIFICADOR USING listid PYC')
    listGrammer.insert(0,instru)


def p_ejecutarDinamico5(t):
    '''instruccion : EXECUTE CADENA INTO STRICT IDENTIFICADOR USING listid PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= EXECUTE CADENA INTO STRICT IDENTIFICADOR USING listid PYC')
    listGrammer.insert(0,instru)


def p_ejecutarDinamico6(t):
    '''instruccion : EXECUTE IDENTIFICADOR PAR1 listid PAR2 PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= EXECUTE IDENTIFICADOR PAR1 listid PAR2 PYC')
    listGrammer.insert(0,instru)


def p_ejecutarDinamico7(t):
    '''instruccion : EXECUTE IDENTIFICADOR PAR1 PAR2 PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= EXECUTE IDENTIFICADOR PAR1 PAR2 PYC')
    listGrammer.insert(0,instru)


def p_procedimiento(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_procedimiento2(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_procedimiento3(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_procedimiento4(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_procedimiento5(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_procedimiento6(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_procedimiento7(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_procedimiento8(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_llamadaprocedimiento(t):
    '''instruccion : instru_call'''
    instru = grammer.nodoGramatical('instruccionesPL')
    instru.agregarDetalle('::= instruccion')
    listGrammer.insert(0,instru)


def p_eliminarprocedimiento(t):
    '''instruccion : DROP PROCEDURE listid opciondropprocedure'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= instru_call')
    listGrammer.insert(0,instru)


def p_eliminarprocedimiento2(t):
    '''instruccion : DROP PROCEDURE IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= DROP PROCEDURE IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure')
    listGrammer.insert(0,instru)


def p_eliminarprocedimiento3(t):
    '''instruccion : DROP PROCEDURE IF EXISTS listid opciondropprocedure'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= DROP PROCEDURE IF EXISTS listid opciondropprocedure')
    listGrammer.insert(0,instru)


def p_eliminarprocedimiento4(t):
    '''instruccion : DROP PROCEDURE IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= DROP PROCEDURE IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure')
    listGrammer.insert(0,instru)


def p_instruccionIndices(t):
    '''instruccion : indice'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= indice')
    listGrammer.insert(0,instru)


def p_opciondropprocedure(t):
    '''opciondropprocedure : CASCADE PYC
    | RESTRICT PYC'''
    instru = grammer.nodoGramatical('opciondropprocedure')

    if t[1] == 'CASCADE':
        instru.agregarDetalle('::= CASCADE PYC')
    elif  t[1] == 'RESTRICT':
        instru.agregarDetalle(' RESTRICT PYC')
    listGrammer.insert(0,instru)


def p_opciondropprocedure2(t):
    '''opciondropprocedure : PYC'''
    instru = grammer.nodoGramatical('opciondropprocedure')
    instru.agregarDetalle('::= PYC')
    listGrammer.insert(0,instru)


def p_declaraciones(t):
    '''declaraciones : declaraciones declaracion'''
    instru = grammer.nodoGramatical('declaraciones')
    instru.agregarDetalle('::= declaraciones declaracion')
    listGrammer.insert(0,instru)


def p_declaraciones2(t):
    '''declaraciones : declaracion'''
    instru = grammer.nodoGramatical('declaraciones')
    instru.agregarDetalle('::= declaracion')
    listGrammer.insert(0,instru)


def p_declaracion(t):
    '''declaracion : IDENTIFICADOR tipo PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR tipo PYC')
    listGrammer.insert(0,instru)


def p_declaracion2(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR CONSTANT tipo PYC')
    listGrammer.insert(0,instru)


def p_declaracion3(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_declaracion4(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR NOT NULL PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR NOT NULL PYC')
    listGrammer.insert(0,instru)


def p_declaracion5(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR DEFAULT operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR DEFAULT operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion6(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR DOSP IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion7(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion8(t):
    '''declaracion : IDENTIFICADOR tipo COLLATE IDENTIFICADOR IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR tipo COLLATE IDENTIFICADOR IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion9(t):
    '''declaracion : IDENTIFICADOR tipo IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR tipo IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion10(t):
    '''declaracion : IDENTIFICADOR tipo COLLATE IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR tipo COLLATE IDENTIFICADOR DOSP IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion11(t):
    '''declaracion : IDENTIFICADOR tipo DOSP IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR tipo DOSP IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion12(t):
    '''declaracion : IDENTIFICADOR tipo DEFAULT operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR tipo DEFAULT operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion13(t):
    '''declaracion : IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR DOSP IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declaracion14(t):
    '''declaracion : IDENTIFICADOR IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_declararcursor(t):
    '''declaracion : IDENTIFICADOR REFCURSOR PYC'''
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR REFCURSOR PYC')
    listGrammer.insert(0,instru)


def p_declararcursor2(t):
    '''declaracion : IDENTIFICADOR CURSOR FOR CADENA PYC'''
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR CURSOR FOR CADENA PYC')
    listGrammer.insert(0,instru)


def p_declararcursor3(t):
    '''declaracion : IDENTIFICADOR SCROLL CURSOR FOR CADENA PYC'''
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR SCROLL CURSOR FOR CADENA PYC')
    listGrammer.insert(0,instru)


def p_declararcursor4(t):
    '''declaracion : IDENTIFICADOR NO SCROLL CURSOR FOR CADENA PYC'''
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR NO SCROLL CURSOR FOR CADENA PYC')
    listGrammer.insert(0,instru)


def p_declararcursor5(t):
    '''declaracion : IDENTIFICADOR CURSOR PAR1 listid PAR2 FOR CADENA PYC'''
    instru = grammer.nodoGramatical('declaracion')
    instru.agregarDetalle('::= IDENTIFICADOR CURSOR PAR1 listid PAR2 FOR CADENA PYC')
    listGrammer.insert(0,instru)


def p_contenidosbegin(t):
    '''contenidosbegin : contenidosbegin contenidobegin'''
    instru = grammer.nodoGramatical('contenidosbegin')
    instru.agregarDetalle('::= contenidosbegin contenidobegin')
    listGrammer.insert(0,instru)


def p_contenidosbeing(t): 
    '''contenidosbegin : contenidobegin'''
    instru = grammer.nodoGramatical('contenidosbegin')
    instru.agregarDetalle('::= contenidobegin')
    listGrammer.insert(0,instru)


def p_contenidobegin(t):
    '''contenidobegin : instruccionesPL_gen'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= instruccionesPL_gen')
    listGrammer.insert(0,instru)

 
def p_contenidobegin2(t):
    '''contenidobegin : CADENA'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= CADENA')
    listGrammer.insert(0,instru)


def p_abrircursor(t):
    '''contenidobegin : OPEN IDENTIFICADOR FOR contenidobegin PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= OPEN IDENTIFICADOR FOR contenidobegin PYC')
    listGrammer.insert(0,instru)


def p_abrircursor2(t):
    '''contenidobegin : OPEN IDENTIFICADOR SCROLL FOR contenidobegin PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= OPEN IDENTIFICADOR SCROLL FOR contenidobegin PYC')
    listGrammer.insert(0,instru)


def p_abrircursor3(t):
    '''contenidobegin : OPEN IDENTIFICADOR NO SCROLL FOR contenidobegin PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= OPEN IDENTIFICADOR NO SCROLL FOR contenidobegin PYC')
    listGrammer.insert(0,instru)


def p_abrircursor4(t):
    '''contenidobegin : OPEN IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= OPEN IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_abrircursor5(t):
    '''contenidobegin : OPEN IDENTIFICADOR listid PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= OPEN IDENTIFICADOR listid PYC')
    listGrammer.insert(0,instru)


def p_usandocursor6(t):
    '''contenidobegin : FETCH IDENTIFICADOR INTO listid PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= FETCH IDENTIFICADOR INTO listid PYC')
    listGrammer.insert(0,instru)


def p_usandocursor7(t):
    '''contenidobegin : FETCH direction FROM IDENTIFICADOR INTO listid PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= FETCH direction FROM IDENTIFICADOR INTO listid PYC')
    listGrammer.insert(0,instru)


def p_usandocursor8(t):
    '''contenidobegin : FETCH direction IN IDENTIFICADOR INTO listid PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= FETCH direction IN IDENTIFICADOR INTO listid PYC')
    listGrammer.insert(0,instru)


def p_usandocursor9(t):
    '''contenidobegin : MOVE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= MOVE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_usandocursor10(t):
    '''contenidobegin : MOVE direction FROM IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= MOVE direction FROM IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_usandocursor11(t):
    '''contenidobegin : MOVE direction IN IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= MOVE direction IN IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_usandocursor12(t):
    '''contenidobegin : UPDATE IDENTIFICADOR SET instru_set WHERE CURRENT OF IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= UPDATE IDENTIFICADOR SET instru_set WHERE CURRENT OF IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_usandocursor13(t):
    '''contenidobegin : UPDATE IDENTIFICADOR SET instru_set WHERE operacion_logica PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= UPDATE IDENTIFICADOR SET instru_set WHERE operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_usandocursor14(t):
    '''contenidobegin : DELETE FROM IDENTIFICADOR WHERE CURRENT OF IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= DELETE FROM IDENTIFICADOR WHERE CURRENT OF IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_cerrandocursor(t):
    '''contenidobegin : CLOSE IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= CLOSE IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


#get RESULT STATUS


def p_getstatus(t):
    '''contenidobegin : GET DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= GET DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC')
    listGrammer.insert(0,instru)


def p_getstatus2(t):
    '''contenidobegin : GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC')
    listGrammer.insert(0,instru)


def p_getstatus3(t):
    '''contenidobegin : GET DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= GET DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC')
    listGrammer.insert(0,instru)


def p_getstatus4(t):
    '''contenidobegin : GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC')
    listGrammer.insert(0,instru)


#NOTHING AT ALL- VACIO


def p_nada(t):
    '''contenidobegin : NULL PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= NULL PYC')
    listGrammer.insert(0,instru)


#alias


def p_alias(t):
    '''instruccion : IDENTIFICADOR ALIAS FOR IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instruccion')
    instru.agregarDetalle('::= IDENTIFICADOR ALIAS FOR IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_return(t):
    '''contenidobegin : RETURN operacion_logica PYC'''
    instru = grammer.nodoGramatical('contenidobegin')
    instru.agregarDetalle('::= RETURN operacion_logica PYC')
    listGrammer.insert(0,instru)

#instruccionesPL DE CICLOS


def p_instruccionesPL_gen(t): 
    '''instruccionesPL_gen : instruccionesPL_gen instruccionesPL_pl'''
    instru = grammer.nodoGramatical('instruccionesPL_gen')
    instru.agregarDetalle('::= instruccionesPL_gen instruccionesPL_pl')
    listGrammer.insert(0,instru)


def p_instruccionesPL_gen1(t): 
    '''instruccionesPL_gen : instruccionesPL_pl'''
    instru = grammer.nodoGramatical('instruccionesPL_gen')
    instru.agregarDetalle('::= instruccionesPL_pl')
    listGrammer.insert(0,instru)


def p_instruccionesPL_pl(t):
    '''instruccionesPL_pl : sentencia_if
    | sentencia_case
    | sentencia_loop
    | instru_exit
    | instru_get_error
    | instru_return
    | operacion_logica
    | asignacion'''
    instru = grammer.nodoGramatical('instruccionesPL_pl')
    if t[1] == 'sentencia_if':
        instru.agregarDetalle('sentencia_if')
    elif  t[1] == 'sentencia_case':
        instru.agregarDetalle('sentencia_case')
    elif  t[1] == 'sentencia_loop':
        instru.agregarDetalle('sentencia_loop')
    elif  t[1] == 'instru_exit':
        instru.agregarDetalle('instru_exit')
    elif  t[1] == 'instru_get_error':
        instru.agregarDetalle('instru_get_error')
    elif  t[1] == 'instru_return':
        instru.agregarDetalle('instru_return')
    elif  t[1] == 'operacion_logica':
        instru.agregarDetalle('operacion_logica')
    elif  t[1] == 'asignacion':
        instru.agregarDetalle('asignacion')

    listGrammer.insert(0,instru)

def p_asignar(t):
    '''asignacion : IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('asignacion')
    instru.agregarDetalle('::= IDENTIFICADOR DOSP IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_asignar2(t):
    '''asignacion : IDENTIFICADOR IGUAL operacion_logica PYC''' 
    instru = grammer.nodoGramatical('asignacion')
    instru.agregarDetalle('::= IDENTIFICADOR IGUAL operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_sentencia_if(t):
    '''sentencia_if : if_simple
    | if_con_else	
    | if_con_elsif'''
    instru = grammer.nodoGramatical('sentencia_if')
    if t[1] == 'if_simple':
        instru.agregarDetalle('if_simple')
    elif t[1] == 'if_con_else':
        instru.agregarDetalle('if_con_else')
    elif t[1] == 'if_con_elsif':
        instru.agregarDetalle('if_con_elsif')
    listGrammer.insert(0,instru)


def p_if_simple(t):
    '''if_simple : IF operacion_logica THEN instruccionesPL_gen END IF PYC'''
    instru = grammer.nodoGramatical('if_simple')
    instru.agregarDetalle('::= IF operacion_logica THEN instruccionesPL_gen END IF PYC')
    listGrammer.insert(0,instru)


def p_if_con_else(t):
    '''if_con_else : IF operacion_logica THEN instruccionesPL_gen ELSE instruccionesPL_gen END IF PYC'''
    instru = grammer.nodoGramatical('if_con_else')
    instru.agregarDetalle('::= IF operacion_logica THEN instruccionesPL_gen ELSE instruccionesPL_gen END IF PYC')
    listGrammer.insert(0,instru)


def p_if_con_elsif(t):
    '''if_con_elsif : IF operacion_logica THEN instruccionesPL_gen cont_if'''
    instru = grammer.nodoGramatical('if_con_elsif')
    instru.agregarDetalle('::= IF operacion_logica THEN instruccionesPL_gen cont_if')
    listGrammer.insert(0,instru)


def p_cont_if1(t):
    '''cont_if : ELSIF operacion_logica THEN instruccionesPL_gen cont_if'''
    instru = grammer.nodoGramatical('cont_if')
    instru.agregarDetalle('::= ELSIF operacion_logica THEN instruccionesPL_gen cont_if')
    listGrammer.insert(0,instru)


def p_cont_if2(t):
    '''cont_if : ELSE instruccionesPL_gen cont_if'''
    instru = grammer.nodoGramatical('cont_if')
    instru.agregarDetalle('::= ELSE instruccionesPL_gen cont_if')
    listGrammer.insert(0,instru)


def p_cont_if3(t):
    '''cont_if : END IF PYC'''
    instru = grammer.nodoGramatical('cont_if')
    instru.agregarDetalle('::= END IF PYC')
    listGrammer.insert(0,instru)


def p_sentencia_case(t):
    '''sentencia_case : CASE operacion_logica list_contentcase end_case'''
    instru = grammer.nodoGramatical('sentencia_case')
    instru.agregarDetalle('::= CASE operacion_logica list_contentcase end_case')
    listGrammer.insert(0,instru)

def p_listContentCase(t):
    '''list_contentcase : list_contentcase cont_case'''
    instru = grammer.nodoGramatical('list_contentcase')
    instru.agregarDetalle('::= list_contentcase cont_case')
    listGrammer.insert(0,instru)

def p_listContentCase2(t):
    '''list_contentcase : cont_case'''
    instru = grammer.nodoGramatical('list_contentcase')
    instru.agregarDetalle('::= cont_case')
    listGrammer.insert(0,instru)


def p_cont_case1(t):
    '''cont_case : WHEN lista_op THEN instruccionesPL_gen PYC'''
    instru = grammer.nodoGramatical('cont_case')
    instru.agregarDetalle('::= WHEN lista_op THEN instruccionesPL_gen PYC')
    listGrammer.insert(0,instru)


def p_cont_case2(t):
    '''cont_case : ELSE instruccionesPL_gen PYC'''
    instru = grammer.nodoGramatical('cont_case')
    instru.agregarDetalle('::= ELSE instruccionesPL_gen PYC')
    listGrammer.insert(0,instru)


def p_cont_case3(t):
    '''end_case : END CASE PYC'''
    instru = grammer.nodoGramatical('end_case')
    instru.agregarDetalle('::= END CASE PYC')
    listGrammer.insert(0,instru)


def p_lista_op1(t):
    '''lista_op : lista_op COMA operacion_logica'''
    instru = grammer.nodoGramatical('lista_op')
    instru.agregarDetalle('::= lista_op : lista_op COMA operacion_logica')
    listGrammer.insert(0,instru)


def p_lista_op2(t):
    '''lista_op : operacion_logica'''
    instru = grammer.nodoGramatical('lista_op')
    instru.agregarDetalle('::= operacion_logica')
    listGrammer.insert(0,instru)


def p_sentencia_loop(t):
    '''sentencia_loop : LOOP instruccionesPL_gen END LOOP PYC'''
    instru = grammer.nodoGramatical('instru_exit')
    instru.agregarDetalle('::= EXIT PYC')
    listGrammer.insert(0,instru)


def p_instru_exit(t):
    '''instru_exit : EXIT  PYC'''
    instru = grammer.nodoGramatical('instru_exit')
    instru.agregarDetalle('::= EXIT PYC')
    listGrammer.insert(0,instru)


def p_instru_exit2(t):
    '''instru_exit : EXIT IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('instru_exit')
    instru.agregarDetalle('::= EXIT IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)

def p_sentencia_case2(t):
    '''sentencia_case : CASE list_contentcase end_case'''
    instru = grammer.nodoGramatical('sentencia_case')
    instru.agregarDetalle('::= CASE list_contentcase end_case')
    listGrammer.insert(0,instru)


def p_instru_except(t):
    '''instru_except : EXCEPTION cont_except'''
    instru = grammer.nodoGramatical('instru_except')
    instru.agregarDetalle('::= EXCEPTION cont_except')
    listGrammer.insert(0,instru)


def p_cont_except1(t):
    '''cont_except : WHEN operacion_logica THEN RAISE EXCEPTION resultadoexception'''
    instru = grammer.nodoGramatical('resultadoexception')
    instru.agregarDetalle('::= WHEN operacion_logica THEN RAISE EXCEPTION resultadoexception')
    listGrammer.insert(0,instru)


def p_resultadoexception(t):
    '''resultadoexception : CADENACARACTER COMA IDENTIFICADOR PYC'''
    instru = grammer.nodoGramatical('resultadoexception')
    instru.agregarDetalle('::= CADENACARACTER COMA IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_resultadoexception2(t):
    '''resultadoexception : CADENACARACTER PYC'''
    instru = grammer.nodoGramatical('resultadoexception')
    instru.agregarDetalle('::= CADENACARACTER PYC')
    listGrammer.insert(0,instru)


def p_resultadoexception3(t):
    '''resultadoexception : CADENA PYC'''
    instru = grammer.nodoGramatical('resultadoexception')
    instru.agregarDetalle('::= CADENA PYC')
    listGrammer.insert(0,instru)


def p_instru_get_error(t):
    '''instru_get_error : GET STACKED DIAGNOSTICS IDENTIFICADOR cont_get'''
    instru = grammer.nodoGramatical('instru_get_error')
    instru.agregarDetalle('::= GET STACKED DIAGNOSTICS IDENTIFICADOR cont_get')
    listGrammer.insert(0,instru)


def p_cont_get1(t):
    '''cont_get : IGUAL operacion_logica'''
    instru = grammer.nodoGramatical('cont_get')
    instru.agregarDetalle('::= IGUAL operacion_logica')
    listGrammer.insert(0,instru)


def p_cont_get2(t):
    '''cont_get : DOSP IGUAL operacion_logica'''
    instru = grammer.nodoGramatical('cont_get')
    instru.agregarDetalle('::= DOSP IGUAL operacion_logica')
    listGrammer.insert(0,instru)


def p_instru_return1(t):
    '''instru_return : RETURN operacion_logica PYC'''
    instru = grammer.nodoGramatical('instru_return')
    instru.agregarDetalle('::= RETURN operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_instru_return2(t):
    '''instru_return : RETURN QUERY CADENA PYC'''
    instru = grammer.nodoGramatical('instru_return')
    instru.agregarDetalle('::= RETURN QUERY CADENA PYC')
    listGrammer.insert(0,instru)


def p_instru_return3(t):
    '''instru_return : RETURN QUERY EXECUTE CADENA PYC'''
    instru = grammer.nodoGramatical('instru_return')
    instru.agregarDetalle('::= RETURN QUERY EXECUTE CADENA PYC')
    listGrammer.insert(0,instru)

def p_instru_return4(t):
    '''instru_return : RETURN NEXT operacion_logica PYC'''
    instru = grammer.nodoGramatical('instru_return')
    instru.agregarDetalle('::= RETURN NEXT operacion_logica PYC')
    listGrammer.insert(0,instru)


def p_instru_return3(t):
    '''instru_return : RETURN QUERY EXECUTE CADENA'''
    instru = grammer.nodoGramatical('instru_return')
    instru.agregarDetalle('::= RETURN QUERY EXECUTE CADENA')
    listGrammer.insert(0,instru)


def p_instru_call(t):
    '''instru_call : CALL IDENTIFICADOR PAR1 operacion_logica PAR2 PYC'''
    instru = grammer.nodoGramatical('instru_call')
    instru.agregarDetalle('::= CALL IDENTIFICADOR PAR1 operacion_logica PAR2 PYC')
    listGrammer.insert(0,instru)


#EXPRESIONES LOGICAS, ARITMETICAS Y RELACIONALES AQUI-->


def p_instru_set(t):
    '''instru_set : instru_set COMA operacion_logica'''
    instru = grammer.nodoGramatical('instru_set')
    instru.agregarDetalle('::= instru_set COMA operacion_logica')
    listGrammer.insert(0,instru)


def p_instru_set2(t):
    '''instru_set : operacion_logica'''
    instru = grammer.nodoGramatical('instru_set')
    instru.agregarDetalle('::= operacion_logica')
    listGrammer.insert(0,instru)


def p_op_logica(p):
    '''operacion_logica : operacion_logica AND operacion_logica'''
    instru = grammer.nodoGramatical('operacion_logica')
    instru.agregarDetalle('::= operacion_logica AND operacion_logica')
    listGrammer.insert(0,instru)

def p_op_logica2(p):
    '''operacion_logica : operacion_logica OR operacion_logica'''
    instru = grammer.nodoGramatical('operacion_logica')
    instru.agregarDetalle('::= operacion_logica OR operacion_logica')
    listGrammer.insert(0,instru)

def p_op_logica3(p):
    '''operacion_logica : operacion_logica NOT operacion_logica'''
    instru = grammer.nodoGramatical('operacion_logica')
    instru.agregarDetalle('::= operacion_logica NOT operacion_logica')
    listGrammer.insert(0,instru)


def p_op_logica1(p):
    '''operacion_logica : operacion_relacional'''
    instru = grammer.nodoGramatical('operacion_logica')
    instru.agregarDetalle('::= operacion_relacional')
    listGrammer.insert(0,instru)


def p_op_relacional(p):
    '''operacion_relacional : operacion_relacional MAYOR operacion_relacional'''
    instru = grammer.nodoGramatical('operacion_relacional')
    instru.agregarDetalle('::= operacion_relacional MAYOR operacion_relacional')
    listGrammer.insert(0,instru)


def p_op_relacional2(p):
    '''operacion_relacional : operacion_relacional MENOR operacion_relacional'''
    instru = grammer.nodoGramatical('operacion_relacional')
    instru.agregarDetalle('::= operacion_relacional MENOR operacion_relacional')
    listGrammer.insert(0,instru)


def p_op_relacional3(p):
    '''operacion_relacional : operacion_relacional MAYORIGUAL operacion_relacional'''
    instru = grammer.nodoGramatical('operacion_relacional')
    instru.agregarDetalle('::= operacion_relacional MAYORIGUAL operacion_relacional')
    listGrammer.insert(0,instru)

def p_op_relacional4(p):
    '''operacion_relacional : operacion_relacional MENORIGUAL operacion_relacional'''
    instru = grammer.nodoGramatical('operacion_relacional')
    instru.agregarDetalle('::= operacion_relacional MENORIGUAL operacion_relacional')
    listGrammer.insert(0,instru)
    
def p_op_relacional5(p):
    '''operacion_relacional : operacion_relacional DIFERENTE operacion_relacional'''
    instru = grammer.nodoGramatical('operacion_relacional')
    instru.agregarDetalle('::= operacion_relacional DIFERENTE operacion_relacional')
    listGrammer.insert(0,instru)

def p_op_relacional6(p):
    '''operacion_relacional : operacion_relacional IGUAL operacion_relacional'''
    instru = grammer.nodoGramatical('operacion_relacional')
    instru.agregarDetalle('::= operacion_relacional IGUAL operacion_relacional')
    listGrammer.insert(0,instru)


def p_op_relacional1(p):
    '''operacion_relacional : operacion_aritmetica'''
    instru = grammer.nodoGramatical('operacion_relacional')
    instru.agregarDetalle('::= operacion_aritmetica')
    listGrammer.insert(0,instru)


def p_op_aritmetica1(p):
    '''operacion_aritmetica : operacion_aritmetica MAS operacion_aritmetica'''
    instru = grammer.nodoGramatical('operacion_aritmetica')
    instru.agregarDetalle('::= operacion_aritmetica MAS operacion_aritmetica')
    listGrammer.insert(0,instru)


def p_op_aritmetica2(p):
    '''operacion_aritmetica : operacion_aritmetica MENOS operacion_aritmetica'''
    instru = grammer.nodoGramatical('operacion_aritmetica')
    instru.agregarDetalle('::= operacion_aritmetica MENOS operacion_aritmetica')
    listGrammer.insert(0,instru)


def p_op_aritmetica3(p):
    '''operacion_aritmetica : operacion_aritmetica POR operacion_aritmetica'''
    instru = grammer.nodoGramatical('operacion_aritmetica')
    instru.agregarDetalle('::= operacion_aritmetica POR operacion_aritmetica')
    listGrammer.insert(0,instru)

def p_op_aritmetica4(p):
    '''operacion_aritmetica : operacion_aritmetica DIVISION operacion_aritmetica'''
    instru = grammer.nodoGramatical('operacion_aritmetica')
    instru.agregarDetalle('::= operacion_aritmetica DIVISION operacion_aritmetica')
    listGrammer.insert(0,instru)

def p_op_aritmetica5(p):
    '''operacion_aritmetica : operacion_aritmetica EXPONENCIACION operacion_aritmetica'''
    instru = grammer.nodoGramatical('operacion_aritmetica')
    instru.agregarDetalle('::= operacion_aritmetica EXPONENCIACION operacion_aritmetica')
    listGrammer.insert(0,instru)

def p_op_aritmetica6(p):
    '''operacion_aritmetica : operacion_aritmetica PORCENTAJE operacion_aritmetica'''
    instru = grammer.nodoGramatical('operacion_aritmetica')
    instru.agregarDetalle('::= operacion_aritmetica PORCENTAJE operacion_aritmetica')
    listGrammer.insert(0,instru)


def p_op_aritmetica7(p):
    '''operacion_aritmetica : PAR1 operacion_logica PAR2'''
    instru = grammer.nodoGramatical('operacion_aritmetica')
    instru.agregarDetalle('::= PAR1 operacion_logica PAR2')
    listGrammer.insert(0,instru)


def p_op_aritmetica8(p):
    '''operacion_aritmetica : valor'''
    instru = grammer.nodoGramatical('operacion_aritmetica')
    instru.agregarDetalle('::= valor')
    listGrammer.insert(0,instru)


def p_direccion(t):
    '''direction : NEXT'''
    instru = grammer.nodoGramatical('direction')
    instru.agregarDetalle('::= NEXT')
    listGrammer.insert(0,instru)
    
def p_direccion2(t):
    '''direction : LAST'''
    instru = grammer.nodoGramatical('direction')
    instru.agregarDetalle('::= LAST')
    listGrammer.insert(0,instru)

def p_direccion3(t):
    '''direction : PRIOR'''
    instru = grammer.nodoGramatical('direction')
    instru.agregarDetalle('::= PRIOR')
    listGrammer.insert(0,instru)

def p_direccion4(t):
    '''direction : FIRST'''
    instru = grammer.nodoGramatical('direction')
    instru.agregarDetalle('::= FIRST')
    listGrammer.insert(0,instru)


def p_direccion5(t):
    '''direction : ABSOLUTE valor'''
    instru = grammer.nodoGramatical('direction')
    instru.agregarDetalle('::= ABSOLUTE valor')
    listGrammer.insert(0,instru)


def p_direccion6(t):
    '''direction : RELATIVE valor'''
    instru = grammer.nodoGramatical('direction')
    instru.agregarDetalle('::= RELATIVE valor')
    listGrammer.insert(0,instru)


def p_direccion7(t):
    '''direction : FORWARD valor'''
    instru = grammer.nodoGramatical('direction')
    instru.agregarDetalle('::= FORWARD valor')
    listGrammer.insert(0,instru)


def p_direccion8(t):
    '''direction : BACKWARD valor'''
    instru = grammer.nodoGramatical('direction')
    instru.agregarDetalle('::= BACKWARD valor')
    listGrammer.insert(0,instru)


def p_crearindices(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 PYC')
    listGrammer.insert(0,instru)

def p_crearindices0(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC')
    listGrammer.insert(0,instru)

#Aqui en using especifica el nombre del metodo que se esta usando, como HASH, btree, etc
#por eso lo puse como identificador tambien-->


def p_crearindices2(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR USING IDENTIFICADOR PAR1 listid PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR USING IDENTIFICADOR PAR1 listid PAR2 PYC')
    listGrammer.insert(0,instru)

def p_crearindices3(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR NULLS ordenposicion PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR NULLS ordenposicion PAR2 PYC')
    listGrammer.insert(0,instru)


def p_crearindices4(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR ASC NULLS ordenposicion PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR ASC NULLS ordenposicion PAR2 PYC')
    listGrammer.insert(0,instru)

def p_crearindices5(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR DESC NULLS ordenposicion PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR DESC NULLS ordenposicion PAR2 PYC')
    listGrammer.insert(0,instru)


def p_crearindices6(t):
    '''indice : CREATE UNIQUE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE UNIQUE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC')
    listGrammer.insert(0,instru)

def p_crearindices7(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 LOWER PAR1 IDENTIFICADOR PAR2 PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 LOWER PAR1 IDENTIFICADOR PAR2 PAR2 PYC')
    listGrammer.insert(0,instru)


def p_crearindices8(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE NOT PAR1 operacion_logica PAR2 PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE NOT PAR1 operacion_logica PAR2 PYC')
    listGrammer.insert(0,instru)


def p_crearindices9(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE operacion_logica PYC'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE operacion_logica PYC')
    listGrammer.insert(0,instru)

def p_dropindices(t):
    '''indice : DROP INDEX IF EXISTS listid opciondropprocedure'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= DROP INDEX IF EXISTS listid opciondropprocedure')
    listGrammer.insert(0,instru)

def p_dropindices2(t):
    '''indice : DROP INDEX listid opciondropprocedure'''
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= DROP INDEX listid opciondropprocedure')
    listGrammer.insert(0,instru)


def p_alterindices(t):
    'indice : ALTER INDEX IDENTIFICADOR ALTER COLUMN IDENTIFICADOR IDENTIFICADOR PYC'
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= ALTER INDEX IDENTIFICADOR ALTER COLUMN IDENTIFICADOR IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_alterindices2(t):
    'indice : ALTER INDEX IDENTIFICADOR ALTER IDENTIFICADOR IDENTIFICADOR PYC'
    instru = grammer.nodoGramatical('indice')
    instru.agregarDetalle('::= ALTER INDEX IDENTIFICADOR ALTER IDENTIFICADOR IDENTIFICADOR PYC')
    listGrammer.insert(0,instru)


def p_ordenposicion(t):
    'ordenposicion : FIRST'
    instru = grammer.nodoGramatical('ordenposicion')
    instru.agregarDetalle('::= FIRST')
    listGrammer.insert(0,instru)


def p_ordenposicion2(t):
    'ordenposicion : LAST'''
    instru = grammer.nodoGramatical('ordenposicion')
    instru.agregarDetalle('::= LAST')
    listGrammer.insert(0,instru)


def p_listaIDENTIFICADOR(t):
    '''listid : listid COMA parametro '''
    instru = grammer.nodoGramatical('listid')
    instru.agregarDetalle('::= listid COMA parametro')
    listGrammer.insert(0,instru)


def p_listaIDENTIFICADOR2(t):
    '''listid : parametro'''
    instru = grammer.nodoGramatical('listid')
    instru.agregarDetalle('::= parametro')
    listGrammer.insert(0,instru)


def p_parametro2(t):
    '''parametro :  tipo'''
    instru = grammer.nodoGramatical('parametro')
    instru.agregarDetalle('::= tipo')
    listGrammer.insert(0,instru)


def p_parametro(t):
    '''parametro : IDENTIFICADOR'''
    instru = grammer.nodoGramatical('parametro')
    instru.agregarDetalle('::= IDENTIFICADOR')
    listGrammer.insert(0,instru)


def p_parametro3(t):
    '''parametro : IDENTIFICADOR tipo'''
    instru = grammer.nodoGramatical('parametro')
    instru.agregarDetalle('::= IDENTIFICADOR tipo')
    listGrammer.insert(0,instru)


def p_parametro4(t):
    '''parametro : INOUT IDENTIFICADOR tipo'''
    instru = grammer.nodoGramatical('parametro')
    instru.agregarDetalle('::= INOUT IDENTIFICADOR tipo')
    listGrammer.insert(0,instru)


def p_parametro5(t):
    ''' parametro : OUT IDENTIFICADOR tipo'''
    instru = grammer.nodoGramatical('parametro')
    instru.agregarDetalle('::= OUT IDENTIFICADOR tipo')
    listGrammer.insert(0,instru)


def p_parametro6(t):
    'parametro : valor'
    instru = grammer.nodoGramatical('parametro')
    instru.agregarDetalle('::= valor')
    listGrammer.insert(0,instru)


def p_valor(t):
    '''valor : NUM'''
    instru = grammer.nodoGramatical('valor')
    instru.agregarDetalle('::= NUM')
    listGrammer.insert(0,instru)


def p_valor2(t):
    '''valor : CADENA'''
    instru = grammer.nodoGramatical('valor')
    instru.agregarDetalle('::= CADENA')
    listGrammer.insert(0,instru)


def p_valor3(t):
    '''valor : PDECIMAL'''
    instru = grammer.nodoGramatical('valor')
    instru.agregarDetalle('::= PDECIMAL')
    listGrammer.insert(0,instru)


def p_valor4(t):
    '''valor : IDENTIFICADOR'''
    instru = grammer.nodoGramatical('valor')
    instru.agregarDetalle('::= IDENTIFICADOR')
    listGrammer.insert(0,instru)


def p_valor5(t):
    '''valor : CADENACARACTER'''
    instru = grammer.nodoGramatical('valor')
    instru.agregarDetalle('::= CADENACARACTER')
    listGrammer.insert(0,instru)

#TIPO DE DATOS 


def p_tipo_datos_int6(t):
    '''tipo : DOUBLE PRECISION'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= DOUBLE PRECISION')
    listGrammer.insert(0,instru)


def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= TIMESTAMP')
    listGrammer.insert(0,instru)


def p_tipo(t):
    '''tipo : SMALLINT'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= SMALLINT')
    listGrammer.insert(0,instru)


def p_tipo_1(t):
    '''tipo : INTEGER'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= INTEGER')
    listGrammer.insert(0,instru)


def p_tipo_2(t):
    '''tipo : BIGINT'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= BIGINT')
    listGrammer.insert(0,instru)


def p_tipo_3(t):
    '''tipo : DECIMAL'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= DECIMAL')
    listGrammer.insert(0,instru)


def p_tipo_4(t):
    '''tipo : NUMERIC'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= NUMERIC')
    listGrammer.insert(0,instru)


def p_tipo_5(t):
    '''tipo : REAL'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= REAL')
    listGrammer.insert(0,instru)


def p_tipo_6(t):
    '''tipo : DOUBLE'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= DOUBLE')
    listGrammer.insert(0,instru)


def p_tipo_7(t):
    '''tipo : MONEY'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= MONEY')
    listGrammer.insert(0,instru)


def p_tipo_8(t):
    '''tipo : CHARACTER'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= CHARACTER')
    listGrammer.insert(0,instru)


def p_tipo_10(t):
    '''tipo : TEXT'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= TEXT')
    listGrammer.insert(0,instru)


def p_tipo_11(t):
    '''tipo : DATE'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= DATE')
    listGrammer.insert(0,instru)


def p_tipo_12(t):
    '''tipo : BOOLEAN'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= BOOLEAN')
    listGrammer.insert(0,instru)


def p_tipo_13(t):
    '''tipo : INT'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= INT')
    listGrammer.insert(0,instru)


def p_tipo_14(t):
    '''tipo : IDENTIFICADOR'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= IDENTIFICADOR')
    listGrammer.insert(0,instru)


def p_tipo15(t):
    '''tipo : DECIMAL PAR1 valdecimal PAR2'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= DECIMAL PAR1 valdecimal PAR2')
    listGrammer.insert(0,instru)

def p_valdecimal(t):
    '''valdecimal : valdecimal COMA NUM'''
    instru = grammer.nodoGramatical('valdecimal')
    instru.agregarDetalle('::= aldecimal COMA NUM')
    listGrammer.insert(0,instru)


def p_valdecimal2(t):
    '''valdecimal : NUM'''
    instru = grammer.nodoGramatical('valdecimal')
    instru.agregarDetalle('::= NUM')
    listGrammer.insert(0,instru)


def p_tipo_datos_varchar(t):
    '''tipo : VARCHAR PAR1 NUM PAR2'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= VARCHAR PAR1 NUM PAR2')
    listGrammer.insert(0,instru)


def p_tipo_datos_vaying(t):
    '''tipo : VARYING PAR1 NUM PAR2'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= VARYING PAR1 NUM PAR2')
    listGrammer.insert(0,instru)


def p_tipo_datos_character(t):
    '''tipo : CHARACTER PAR1 NUM PAR2'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= CHARACTER PAR1 NUM PAR2')
    listGrammer.insert(0,instru)


def p_tipo_datos_char(t):
    '''tipo : CHAR PAR1 NUM PAR2'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= CHAR PAR1 NUM PAR2')
    listGrammer.insert(0,instru)


def p_tipo_datos_char2(t):
    '''tipo : VARCHAR'''
    instru = grammer.nodoGramatical('tipo')
    instru.agregarDetalle('::= VARCHAR')
    listGrammer.insert(0,instru)

#def p_error(t):
    #print("EntrANDo a errOR **********")
    #if t:
        #parser.errok()
    #else:
        #print("SQL statement NOT yet complete")

parser = yacc.yacc()
def parse(input):
    parser.parse(input.upper())
    gramati = generar.graficaGramaticalbnf(listGrammer)
    gramati.ejecutarGrafica()

def ejecutar():
    f = open("entrada.txt", "r")
    input = f.read()
    print(input)
    parser.parse(input.upper())
    gramati = generar.graficaGramaticalbnf(listGrammer)
    gramati.ejecutarGrafica()