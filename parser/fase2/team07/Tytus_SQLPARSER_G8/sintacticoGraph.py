#IMPORTS
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Identificador import Identificador
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from tkinter.constants import HORIZONTAL
from ply import *
from lexico import *
#tokens= lexico.tokens
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.FunctionAgregate import Avg, Count, Greatest, Least, Max, Min, Sum, Top
from Instrucciones.FunctionMathematical import Abs, Cbrt, Ceil, Ceiling, Degrees, Div, Exp, Factorial, Floor, Gcd, Lcm, Ln, Log, Log10, MinScale, Mod, PI, Power, Radians, Random, Round, Scale, SetSeed, Sign, Sqrt, TrimScale, Trunc, WidthBucket
from Instrucciones.FunctionTrigonometric import Acos, Acosd, Acosh, Asin, Asind, Asinh, Atan, Atan2, Atan2d, Atand, Atanh, Cos, Cosd, Cosh, Cot, Cotd, Sin, Sind, Sinh, Tan, Tand, Tanh
from Instrucciones.FunctionBinaryString import Convert, Decode, Encode, GetByte, Length, Md5, SetByte, Sha256, Substr, Substring, Trim
from Instrucciones.Expresiones import Aritmetica, Logica, Primitivo, Relacional, Between
from Instrucciones.DateTimeTypes import Case , CurrentDate, CurrentTime, DatePart, Extract, Now, Por, TimeStamp

from Instrucciones.Sql_alter import AlterDatabase, AlterTable, AlterDBOwner, AlterTableAddColumn, AlterTableAddConstraintFK, Columna, AlterTableDropColumn, AlterTableAddConstraint, AlterTableAddFK, AlterTableAlterColumn, AlterTableDropConstraint, AlterTableAlterColumnType, AlterTableAddCheck, AlterIndex
from Instrucciones.Sql_create import CreateDatabase, CreateFunction, CreateOrReplace, CreateTable, CreateType, Use, ShowDatabases,Set, CreateIndex
from Instrucciones.Sql_declare import Declare
from Instrucciones.Sql_delete import DeleteTable
from Instrucciones.Sql_drop import DropDatabase, DropTable, DropIndex
from Instrucciones.Sql_insert import insertTable
from Instrucciones.Sql_Joins import Join, JoinFull, JoinInner, JoinLeft, JoinRight
from Instrucciones.Sql_select import GroupBy, Having, Limit, OrderBy, Select, Where, SelectLista
from Instrucciones.Sql_truncate import Truncate
from Instrucciones.Sql_update import UpdateTable
from Instrucciones.Sql_create import Columna as CColumna
from Instrucciones import Relaciones, LlamadoFuncion
import nodoGeneral

from Instrucciones.plpgsql import condicional_if, Funcion, DeclaracionVariable, DeclaracionAlias, condicional_case, Procedimiento, DeclaracionRetorno, AsignacionVariable

# IMPORTAMOS EL STORAGE
from storageManager import jsonMode as storage
from Instrucciones.Sql_create.Tipo_Constraint import *

lista_lexicos=lista_errores_lexico

# INICIA EN ANALISIS SINTACTICO

global numNodo 
numNodo = 0

def incNodo(valor):
    global numNodo
    numNodo = numNodo + 1
    return numNodo

def crear_nodo_general(nombre, valor, fila, column):
    nNodo = incNodo(numNodo)
    hijos = []
    nodoEnviar = nodoGeneral.NodoGeneral(fila, column, nombre, nNodo, valor, hijos)
    return nodoEnviar

# Asociación de operadores y precedencia
precedence = (
    ('left', 'CHECK'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IS', 'FROM','DISTINCT'),
    ('left', 'LIKE', 'BETWEEN', 'IN'),
    ('left', 'NOT'),
    ('left', 'IGUAL', 'MAYORQ', 'MENORQ', 'MAYOR_IGUALQ', 'MENOR_IGUALQ', 'DISTINTO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'EXPONENCIACION'),
    ('left', 'POR', 'DIVIDIDO'),
    ('left', 'MODULO'),
    ('left', 'AS', 'ASC', 'DESC'),
    ('left', 'COUNT'),
    ('left', 'UNION', 'INTERSECT', 'EXCEPT'),
    ('left', 'PARIZQ', 'PARDER'),
    ('right', 'UMENOS')
)

# Definición de la gramática

def p_init(t):
    'init : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista1(t):
    'instrucciones    :  instrucciones instruccion '
    nodo = t[1]
    nodo.hijos.append(t[2])
    t[0] = nodo
    
def p_instrucciones_lista2(t):
    'instrucciones : instruccion '
    nodo = crear_nodo_general("init", "", t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo


    
# CREATE DATABASE
def p_instruccion_create_database1(t):
    '''instruccion : CREATE DATABASE if_not_exists ID PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    nodoId = crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[3]
    nodo = crear_nodo_general("CREATE DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoId)
    t[0] = nodo

def p_instruccion_create_database2(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    nodoId = crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[3]
    nodoO = t[7]
    nodo = crear_nodo_general("CREATE DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoO)
    t[0] = nodo

def p_instruccion_create_database3(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    nodoId = crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[3]
    nodoO = t[7]
    nodoM = crear_nodo_general("Mode",t[10],t.lexer.lineno, t.lexer.lexpos)
    nodo = crear_nodo_general("CREATE DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoO)
    nodo.hijos.append(nodoM)
    t[0] = nodo

def p_instruccion_create_database4(t):
    '''instruccion : CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    #                     ID    tipo  opcion ID2  ENTERO
    nodoId = crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[3]
    nodoM = crear_nodo_general("Mode",t[7],t.lexer.lineno, t.lexer.lexpos)
    nodo = crear_nodo_general("CREATE DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoM)
    t[0] = nodo

# CREATE OR REPLACE DATABASE
def p_instruccion_create_or_database1(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
    '''
    nodoR = crear_nodo_general("OR REPLACE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[5]
    nodo = crear_nodo_general("CREATE DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoR)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoId)
    t[0] = nodo

def p_instruccion_create_or_database2(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    nodoR = crear_nodo_general("OR REPLACE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[5]
    nodoO = t[9]
    nodo = crear_nodo_general("CREATE DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoR)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoO)
    t[0] = nodo

def p_instruccion_create_or_database3(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    nodoR = crear_nodo_general("OR REPLACE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[5]
    nodoO = t[9]
    nodoM = crear_nodo_general("Mode",t[12],t.lexer.lineno, t.lexer.lexpos)
    nodo = crear_nodo_general("CREATE DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoR)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoO)
    nodo.hijos.append(nodoM)
    t[0] = nodo

def p_instruccion_create_or_database4(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    nodoR = crear_nodo_general("OR REPLACE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[5]
    nodoM = crear_nodo_general("Mode",t[9],t.lexer.lineno, t.lexer.lexpos)
    nodo = crear_nodo_general("CREATE DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoR)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoM)
    t[0] = nodo

def p_owner(t):
    '''cowner : ID
                | CARACTER
                | CADENA
    '''
    t[0] = crear_nodo_general("Owner",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_if_not_exists(t):
    '''if_not_exists : IF NOT EXISTS
    '''
    t[0] = crear_nodo_general("IF NOT EXISTS","",t.lexer.lineno, t.lexer.lexpos)

def p_if_not_exists1(t):
    '''if_not_exists : 
    '''
    t[0] = None

def p_instruccion_create1(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER PUNTO_COMA
    '''
    nodo = crear_nodo_general("CREATE TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoCampos = t[5]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoCampos)
    t[0] = nodo

def p_instruccion_create2(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA
    '''
    nodo = crear_nodo_general("CREATE TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoCampos = t[5]
    nodoI = crear_nodo_general("INHERITS",t[9],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoCampos)
    nodo.hijos.append(nodoI)
    t[0] = nodo

def p_instruccion_use(t):
    '''instruccion : USE ID PUNTO_COMA
    '''
    t[0] = crear_nodo_general("USE",t[2],t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_show_database1(t):
    '''instruccion : SHOW DATABASES PUNTO_COMA
    '''
    t[0] = crear_nodo_general("SHOW DATABASES","",t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_show_database2(t):
    '''instruccion : SHOW DATABASES LIKE cadena_o_caracter PUNTO_COMA
    '''
    nodo = crear_nodo_general("SHOW DATABASES","",t.lexer.lineno, t.lexer.lexpos)
    nodoL = crear_nodo_general("LIKE","",t.lexer.lineno, t.lexer.lexpos)
    nodoC = t[4]
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoC)
    t[0] = nodo

def p_instruccion_create_enumerated_type(t):
    '''instruccion : CREATE TYPE ID AS ENUM PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    nodo = crear_nodo_general("CREATE TYPE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[7]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoE)
    t[0] = nodo

def p_instruccion_truncate(t):
    '''instruccion : TRUNCATE TABLE ID PUNTO_COMA
    '''
    nodo = crear_nodo_general("TRUNCATE TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    t[0] = nodo

# DROP DATABASE
def p_instruccion_drop_database1(t):
    '''instruccion : DROP DATABASE ID PUNTO_COMA

    '''
    nodo = crear_nodo_general("DROP DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    t[0] = nodo

def p_instruccion_drop_database2(t):
    '''instruccion : DROP DATABASE IF EXISTS ID PUNTO_COMA

    '''
    nodo = crear_nodo_general("DROP DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodoI = crear_nodo_general("IF EXISTS","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[5],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoI)
    nodo.hijos.append(nodoId)
    t[0] = nodo

# DROP TABLE
def p_instruccion_drop(t):
    '''instruccion : DROP TABLE ID PUNTO_COMA

    '''
    nodo = crear_nodo_general("DROP TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    t[0] = nodo

def p_instruccion_drop2(t):
    '''instruccion : DROP ID

    '''
    nodo = crear_nodo_general("DROP ID",t[2],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo


def p_instruccion_where(t):
    '''
        instructionWhere :  WHERE expre
    '''
    nodo = crear_nodo_general("WHERE","",t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[2]
    nodo.hijos.append(nodoE)
    t[0] = nodo


# update tabla set campo = valor , campo 2= valor where condicion

def p_instruccion_update(t):
    '''instruccion : UPDATE ID SET lcol instructionWhere PUNTO_COMA

    '''
    nodo = crear_nodo_general("UPDATE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[2],t.lexer.lineno, t.lexer.lexpos)
    nodoL = t[4]
    nodoInstr = t[5]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoInstr)
    t[0] = nodo

# update tabla set campo = valor , campo 2= valor;

def p_instruccion_update2(t):
    '''instruccion : UPDATE ID SET lcol PUNTO_COMA

    '''
    nodo = crear_nodo_general("UPDATE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[2],t.lexer.lineno, t.lexer.lexpos)
    nodoL = t[4]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoL)
    t[0] = nodo

# DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
def p_columunas_delete(t):
    '''
     instruccion : DELETE FROM ID instructionWhere PUNTO_COMA
    '''
    nodo = crear_nodo_general("DELETE FROM","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoInstr = t[4]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoInstr)
    t[0] = nodo

#FUNCIONES
#def p_funciones(t):
    #'''
    # instruccion : CREATE FUNCTION ID BEGIN instrucciones END PUNTO_COMA
    #'''
#    strGram = "<instruccion> ::= CREATE FUNCTION ID BEGIN <instrucciones> END PUNTO_COMA"
#    t[0] = CreateFunction.CreateFunction(t[3],None, None, None, t[5], strGram, t.lexer.lineno, t.lexer.lexpos)

#def p_funciones2(t):
    #'''
    # instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER BEGIN instrucciones END PUNTO_COMA
    #'''
#    strGram = "<instruccion> ::= CREATE FUNCTION ID PARIZQ <lcol> PARDER BEGIN <instrucciones> END PUNTO_COMA"
#    t[0] = CreateFunction.CreateFunction(t[3],None, t[5], None, t[8], strGram, t.lexer.lineno, t.lexer.lexpos)

#def p_funciones3(t):
    #'''
    # instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER AS expresion BEGIN instrucciones END PUNTO_COMA
    #'''
#    strGram = "<instruccion> ::= CREATE FUNCTION ID PARIZQ <lcol> PARDER AS <expresion> BEGIN <instrucciones> END PUNTO_COMA"
#    t[0] = CreateFunction.CreateFunction(t[3],None, t[5], t[8], t[10], strGram, t.lexer.lineno, t.lexer.lexpos)


def p_declaracion(t):
    '''
     instruccion : DECLARE expresion AS expresion PUNTO_COMA
    '''
    nodo = crear_nodo_general("DECLARE","",t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[2]
    nodoA = crear_nodo_general("AS","",t.lexer.lineno, t.lexer.lexpos)
    nodoE2 = t[4]
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoA)
    nodo.hijos.append(nodoE2)
    t[0] = nodo

def p_declaracion1(t):
    '''
     instruccion : DECLARE expresion tipo PUNTO_COMA
    '''
    nodo = crear_nodo_general("DECLARE","",t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[2]
    nodoT = t[3]
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoT)
    t[0] = nodo
    
def p_set(t):
    '''
     instruccion : SET expresion IGUAL expre PUNTO_COMA
    '''
    nodo = crear_nodo_general("SET","",t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[2]
    nodoI = crear_nodo_general("=","",t.lexer.lineno, t.lexer.lexpos)
    nodoE2 = t[4]
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoI)
    nodo.hijos.append(nodoE2)
    t[0] = nodo

# ALTER DATABASE name RENAME TO new_name
def p_instruccion_alter_database1(t):
    '''instruccion : ALTER DATABASE ID RENAME TO ID PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer)
    nodoR = crear_nodo_general("RENAME TO","",t.lexer.lineno, t.lexer.lexpos)
    nodoId2 = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoR)
    nodo.hijos.append(nodoId2)
    t[0] = nodo

# ALTER DATABASE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
def p_instruccion_alter_database2(t):
    '''instruccion : ALTER DATABASE ID OWNER TO list_owner PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER DATABASE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoOwner = crear_nodo_general("OWNER TO","",t.lexer.lineno, t.lexer.lexpos)
    nodoL = t[6]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoOwner)
    nodo.hijos.append(nodoL)
    t[0] = nodo

# { new_owner | CURRENT_USER | SESSION_USER }
def p_list_owner(t):
    '''list_owner : ID
                | CURRENT_USER
                | SESSION_USER
    '''
    
    t[0] = crear_nodo_general("OWNER",t[1],t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD COLUMN NOMBRE_COLUMNA TIPO;
def p_instruccion_alter1(t):
    '''instruccion : ALTER TABLE ID l_add_column PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoL = t[4]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoL)
    t[0] = nodo

def p_l_add_column1(t):
    '''l_add_column : l_add_column COMA add_column
    '''
    nodo = t[1]
    nodo.hijos.append(t[3])
    t[0] = nodo


def p_l_add_column2(t):
    '''l_add_column : add_column
    '''
    nodo = crear_nodo_general("l_add_column","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_add_column(t):
    '''add_column : ADD COLUMN ID tipo'''
    nodo = crear_nodo_general("ADD COLUMN","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoT = t[4]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoT)
    t[0] = nodo

# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;
def p_instruccion_alter2(t):
    '''instruccion : ALTER TABLE ID l_drop_column PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoL = t[4]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoL)
    t[0] = nodo

def p_l_drop_column1(t):
    '''l_drop_column : l_drop_column COMA drop_column'''
    nodo = t[1]
    nodo.hijos.append(t[3])
    t[0] = nodo

def p_l_drop_column2(t):
    '''l_drop_column : drop_column'''
    nodo = crear_nodo_general("l_drop_column","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_drop_column(t):
    'drop_column : DROP COLUMN ID'
    nodo = crear_nodo_general("DROP COLUMN","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    t[0] = nodo

# ALTER TABLE 'NOMBRE_TABLA' ADD CHECK EXP;
def p_instruccion_alter3(t):
    '''instruccion : ALTER TABLE ID ADD CHECK expre PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoC = crear_nodo_general("ADD CHECK","",t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[6]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoC)
    nodo.hijos.append(nodoE)
    t[0] = nodo

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter4(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ lista_id PARDER PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoConst = crear_nodo_general("ADD CONSTRAINT","",t.lexer.lineno, t.lexer.lexpos)
    nodoId2 = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodoU = crear_nodo_general("UNIQUE","",t.lexer.lineno, t.lexer.lexpos)
    nodoL = t[9]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoConst)
    nodo.hijos.append(nodoId2)
    nodo.hijos.append(nodoU)
    nodo.hijos.append(nodoL)
    t[0] = nodo

def p_instruccion_altercfk(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoConst = crear_nodo_general("ADD CONSTRAINT","",t.lexer.lineno, t.lexer.lexpos)
    nodoId2 = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodoU = crear_nodo_general("FOREIGN KEY","",t.lexer.lineno, t.lexer.lexpos)
    nodoLI = t[10]
    nodoR = crear_nodo_general("REFERENCES","",t.lexer.lineno, t.lexer.lexpos)
    nodoId3 = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodoLI2 = t[15]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoConst)
    nodo.hijos.append(nodoId2)
    nodo.hijos.append(nodoU)
    nodo.hijos.append(nodoLI)
    nodo.hijos.append(nodoR)
    nodo.hijos.append(nodoId3)
    nodo.hijos.append(nodoLI2)
    t[0] = nodo

# ALTER TABLE child_table ADD FOREIGN KEY (fk_columns) REFERENCES parent_table (parent_key_columns);
def p_instruccion_alter5(t):
    '''instruccion : ALTER TABLE ID ADD FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoF = crear_nodo_general("ADD FOREIGN KEY","",t.lexer.lineno, t.lexer.lexpos)
    nodoLI = t[8]
    nodoR = crear_nodo_general("REFERENCES","",t.lexer.lineno, t.lexer.lexpos)
    nodoId2 = crear_nodo_general("ID",t[11],t.lexer.lineno, t.lexer.lexpos)
    nodoLI = t[13]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoF)
    nodo.hijos.append(nodoLI)
    nodo.hijos.append(nodoR)
    nodo.hijos.append(nodoId2)
    nodo.hijos.append(nodoLI)
    t[0] = nodo

# ALTER TABLE 'NOMBRE_TABLA' ALTER COLUMN 'NOMBRE' SET NOT NULL;
def p_instruccion_alter6(t):
    '''instruccion : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoA = crear_nodo_general("ALTER COLUMN","",t.lexer.lineno, t.lexer.lexpos)
    nodoId2 = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodoS = crear_nodo_general("SET NOT NULL","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoA)
    nodo.hijos.append(nodoId2)
    nodo.hijos.append(nodoS)
    t[0] = nodo

# ALTER TABLE 'NOMBRE_TABLA' DROP CONSTRAINT 'NOMBRE';
def p_instruccion_alter7(t):
    '''instruccion : ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoC = crear_nodo_general("DROP CONSTRAINT","",t.lexer.lineno, t.lexer.lexpos)
    nodoId2 = crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoC)
    nodo.hijos.append(nodoId2)
    t[0] = nodo

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter8(t):
    '''instruccion : ALTER TABLE ID l_alter PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoL = t[4]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoL)
    t[0] = nodo

def p_l_alter1(t):
    'l_alter : l_alter COMA alter_column'
    nodo = t[1]
    nodo.hijos.append(t[3])
    t[0] = nodo

def p_l_alter2(t):
    'l_alter : alter_column'
    nodo = crear_nodo_general("l_alter","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_alter_column(t):
    'alter_column : ALTER COLUMN ID TYPE tipo'
    nodo = crear_nodo_general("ALTER TABLE","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoT = crear_nodo_general("TYPE",t[5],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoT)
    t[0] = nodo

# insert into tabla (campo1,campo2,campo3,campo4) values (valor1, valor2, valor3, valor4)
# unicamente validar que tengan los mismos campos y la mismas cantidad de valores

def p_instruccion_insert(t):
    '''instruccion : INSERT INTO ID PARIZQ lista_id PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    nodo = crear_nodo_general("INSERT INTO","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoL = t[5]
    nodoV = crear_nodo_general("VALUES","",t.lexer.lineno, t.lexer.lexpos)
    nodoLE = t[9]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoV)
    nodo.hijos.append(nodoLE)
    t[0] = nodo

#insert into tabla values (valor1,valor2,valor3)
# debe validar que la cantidad de valores coincida con la cantidad de columnas de la tabla y el tipo de dato
def p_instruccion_insert2(t):
    '''
    instruccion : INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    nodo = crear_nodo_general("INSERT INTO","",t.lexer.lineno, t.lexer.lexpos)
    nodoId = crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos)
    nodoV = crear_nodo_general("VALUES","",t.lexer.lineno, t.lexer.lexpos)
    nodoLE = t[6]
    nodo.hijos.append(nodoId)
    nodo.hijos.append(nodoV)
    nodo.hijos.append(nodoLE)
    t[0] = nodo
    
# SELECT col, col FROM id;
# SELECT * from id;
def p_instruccion_query(t):
    '''
    instruccion : lquery PUNTO_COMA
    '''
    t[0] = t[1]

def p_lista_querys(t):
    '''lquery : lquery relaciones query
    '''
    nodo = crear_nodo_general("lquery","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    nodo.hijos.append(t[2])
    nodo.hijos.append(t[3])
    t[0] = nodo

def p_lista_querys2(t):
    '''
    lquery : query
    '''
    t[0] = t[1]


def p_tipo_relaciones(t):
    '''relaciones : UNION
                | INTERSECT
                | EXCEPT
    '''
    if(t[1]=="UNION"):
        t[0] = crear_nodo_general("relaciones",t[1],t.lexer.lineno, t.lexer.lexpos)
    elif(t[1]=="INTERSECT"):
        t[0] = crear_nodo_general("relaciones",t[1],t.lexer.lineno, t.lexer.lexpos)
    elif(t[1]=="EXCEPT"):
        t[0] = crear_nodo_general("relaciones",t[1],t.lexer.lineno, t.lexer.lexpos)
    else:
        t[0] = None

def p_tipo_relaciones2(t):
    '''relaciones : UNION ALL 
                | INTERSECT ALL 
                | EXCEPT ALL 
    '''
    if(t[1]=="UNION"):
        t[0] = crear_nodo_general("relaciones","UNION ALL",t.lexer.lineno, t.lexer.lexpos)
    elif(t[1]=="INTERSECT"):
        t[0] = crear_nodo_general("relaciones","INTERSECT ALL" ,t.lexer.lineno, t.lexer.lexpos)
    elif(t[1]=="EXCEPT"):
        t[0] = crear_nodo_general("relaciones","EXCEPT ALL",t.lexer.lineno, t.lexer.lexpos)
    else:
        t[0] = None

def p_instruccion_select(t):
    '''
    query : SELECT dist lcol FROM lcol
    '''
    nodo = crear_nodo_general("SELECT","",t.lexer.lineno, t.lexer.lexpos)
    nodoD = t[2]
    nodoL = t[3]
    nodoF = crear_nodo_general("FROM","",t.lexer.lineno, t.lexer.lexpos)
    nodoLC = t[5]
    nodo.hijos.append(nodoD)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoF)
    nodo.hijos.append(nodoLC)
    t[0] = nodo

def p_instruccion_select1(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    nodo = crear_nodo_general("SELECT","",t.lexer.lineno, t.lexer.lexpos)
    nodoD = t[2]
    nodoL = t[3]
    nodoF = crear_nodo_general("FROM","",t.lexer.lineno, t.lexer.lexpos)
    nodoLC = t[5]
    nodoW = t[6]
    nodoLR = t[7]
    nodo.hijos.append(nodoD)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoF)
    nodo.hijos.append(nodoLC)
    nodo.hijos.append(nodoW)
    nodo.hijos.append(nodoLR)
    t[0] = nodo

def p_instruccion_select2(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    nodo = crear_nodo_general("SELECT","",t.lexer.lineno, t.lexer.lexpos)
    nodoD = t[2]
    nodoL = t[3]
    nodoF = crear_nodo_general("FROM","",t.lexer.lineno, t.lexer.lexpos)
    nodoLC = t[5]
    nodoW = t[6]
    nodo.hijos.append(nodoD)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoF)
    nodo.hijos.append(nodoLC)
    nodo.hijos.append(nodoW)
    t[0] = nodo

def p_instruccion_select3(t):
    '''
    query : SELECT dist lcol FROM lcol linners 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    nodo = crear_nodo_general("SELECT","",t.lexer.lineno, t.lexer.lexpos)
    nodoD = t[2]
    nodoL = t[3]
    nodoF = crear_nodo_general("FROM","",t.lexer.lineno, t.lexer.lexpos)
    nodoLC = t[5]
    nodoLi = t[6]
    nodo.hijos.append(nodoD)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoF)
    nodo.hijos.append(nodoLC)
    nodo.hijos.append(nodoLi)
    t[0] = nodo

def p_instruccion_select4(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    nodo = crear_nodo_general("SELECT","",t.lexer.lineno, t.lexer.lexpos)
    nodoD = t[2]
    nodoL = t[3]
    nodoF = crear_nodo_general("FROM","",t.lexer.lineno, t.lexer.lexpos)
    nodoLC = t[5]
    nodoLi = t[6]
    nodoW = t[7]
    nodoLR = t[8]
    nodo.hijos.append(nodoD)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoF)
    nodo.hijos.append(nodoLC)
    nodo.hijos.append(nodoLi)
    nodo.hijos.append(nodoW)
    nodo.hijos.append(nodoLR)
    t[0] = nodo

def p_instruccion_select5(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    nodo = crear_nodo_general("SELECT","",t.lexer.lineno, t.lexer.lexpos)
    nodoD = t[2]
    nodoL = t[3]
    nodoF = crear_nodo_general("FROM","",t.lexer.lineno, t.lexer.lexpos)
    nodoLC = t[5]
    nodoLi = t[6]
    nodoW = t[7]
    nodo.hijos.append(nodoD)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoF)
    nodo.hijos.append(nodoLC)
    nodo.hijos.append(nodoLi)
    nodo.hijos.append(nodoW)
    t[0] = nodo

def p_instruccion_select6(t):
    '''
    query : SELECT dist lcol 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    nodo = crear_nodo_general("SELECT","",t.lexer.lineno, t.lexer.lexpos)
    nodoD = t[2]
    nodoL = t[3]
    nodo.hijos.append(nodoD)
    nodo.hijos.append(nodoL)
    t[0] = nodo

def p_instruccion_select7(t):
    '''
    query   : SELECT dist lcol FROM lcol lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    nodo = crear_nodo_general("SELECT","",t.lexer.lineno, t.lexer.lexpos)
    nodoD = t[2]
    nodoL = t[3]
    nodoF = crear_nodo_general("FROM","",t.lexer.lineno, t.lexer.lexpos)
    nodoLC = t[5]
    nodoLr = t[6]
    nodo.hijos.append(nodoD)
    nodo.hijos.append(nodoL)
    nodo.hijos.append(nodoF)
    nodo.hijos.append(nodoLC)
    nodo.hijos.append(nodoLr)
    t[0] = nodo

def p_lista_case(t):
    '''lcase : lcase case
    '''
    nodo = t[1]
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_lista_case_case(t):
    '''lcase : case
    '''
    nodo = crear_nodo_general("lcase","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo


def p_instruccion_case(t):
    '''
    case    : WHEN expre THEN expre
            | ELSE expre
    '''
    t[0] = crear_nodo_general("CASE","",t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_lrows(t):
    '''lrows : lrows rows
    '''
    nodo = t[1]
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_instruccion_lrows2(t):
    '''lrows : rows
    '''
    nodo = crear_nodo_general("lrows","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_dist(t):
    '''dist : DISTINCT
    '''
    t[0] = crear_nodo_general("DISTINCT",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_dist1(t):
    '''dist : 
    '''
    t[0] = None

def p_instruccion_rows(t):
    '''
    rows    : ORDER BY l_expresiones
            | ORDER BY l_expresiones DESC
            | ORDER BY l_expresiones ASC
            | ORDER BY l_expresiones NULLS FIRST
            | ORDER BY l_expresiones NULLS LAST 
            | GROUP BY l_expresiones
            | HAVING lcol
            | LIMIT ENTERO
    '''
    if t[1] == "ORDER":
        nodo = crear_nodo_general("ORDER BY","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[3])
        if len(t) == 5:
            nodo.hijos.append(crear_nodo_general("ORDER",t[4],t.lexer.lineno, t.lexer.lexpos))
        if len(t) == 6:
            nodo.hijos.append(crear_nodo_general("NULLS",t[5],t.lexer.lineno, t.lexer.lexpos))
    if t[1] == "GROUP":
        nodo = crear_nodo_general("GROUP BY","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[3])
    if t[1] == "HAVING":
        nodo = crear_nodo_general("HAVING","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[2])
    if t[1] == "LIMIT":
        nodo = crear_nodo_general("LIMIT","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(crear_nodo_general("ENTERO",t[2],t.lexer.lineno, t.lexer.lexpos))

def p_instruccion_row2(t):
    '''rows : LIMIT ENTERO OFFSET ENTERO'''
    #LIMIT(LIMITE,FILAS_A_EXCLUIR,fila,columna)
    nodo = crear_nodo_general("LIMIT","",t.lexer.lineno, t.lexer.lexpos)
    nodoE = crear_nodo_general("ENTERO",t[2],t.lexer.lineno, t.lexer.lexpos)
    nodoO = crear_nodo_general("OFFSET","",t.lexer.lineno, t.lexer.lexpos)
    nodoEn = crear_nodo_general("ENTERO",t[4],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoO)
    nodo.hijos.append(nodoEn)
    t[0] = nodo

def p_linner_join(t):
    '''linners : linners inners
    '''
    nodo = t[1]
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_linner_join2(t):
    '''linners : inners
    '''
    nodo = crear_nodo_general("linners","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_inner_join(t):
    '''
    inners : INNER JOIN expre nombre ON expre
            | LEFT JOIN expre nombre ON expre
            | FULL OUTER JOIN expre nombre ON expre
            | JOIN expre nombre ON expre
            | RIGHT JOIN expre nombre ON expre
    '''

def p_operadores_logicos(t):
    ''' expre : expre OR expre
            | expre AND expre
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[2] == "OR":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("OR","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "AND":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("AND","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    t[0] = nodo

def p_operadores_unarios(t):
    ''' expre : NOT expre
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("NOT","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    t[0] = nodo 

def p_operadores_relacionales(t):
    ''' expre : expre IGUAL expre
            | expre MAYORQ expre
            | expre MENORQ expre
            | expre MAYOR_IGUALQ expre
            | expre MENOR_IGUALQ expre
            | expre DISTINTO expre
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[2] == "IGUAL":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("IGUAL","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "MAYORQ":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("MAYORQ","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "MENORQ":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("MENORQ","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "MAYOR_IGUALQ":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("MAYOR_IGUALQ","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "MENOR_IGUALQ":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("MENOR_IGUALQ","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "DISTINTO":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("DISTINTO","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    t[0] = nodo

def p_operadores_aritmeticos(t):
    '''expre : expre MAS expre
            | expre MENOS expre
            | expre POR expre
            | expre DIVIDIDO expre
            | expre EXPONENCIACION expre
            | expre MODULO expre
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[2] == "MAS":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("MAS","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "MENOS":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("MENOS","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "POR":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("POR","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "DIVIDIDO":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("DIVIDIDO","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "EXPONENCIACION":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("EXPONENCIACION","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    if t[2] == "MODULO":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("MODULO","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    t[0] = nodo

def p_operador_unario(t):
    'expre : MENOS expre %prec UMENOS'
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    nodoM = crear_nodo_general("MENOS",t[1],t.lexer.lineno, t.lexer.lexpos)
    nodoE = t[2]
    nodoU = crear_nodo_general("UMENOS",t[4],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(nodoM)
    nodo.hijos.append(nodoE)
    nodo.hijos.append(nodoU)
    t[0] = nodo

def p_operadores_like(t):
    '''expre : expre LIKE expre
            | expre NOT LIKE expre
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[2] == "LIKE":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("LIKE","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
    else:
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("NOT LIKE","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[4])
    t[0] = nodo
        
    #t[0] = PatternMatching(t[1], t[3], 'LIKE', t.lexer.lineno, t.lexer.lexpos) if t[2] == 'LIKE' else PatternMatching(t[1], t[3], 'NOT_LIKE', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_between(t):
    '''expre : expre BETWEEN expresion AND expresion
            | expre NOT BETWEEN expresion AND expresion
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[2] == "NOT":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("NOT BETWEEN","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[4])
        nodo.hijos.append(crear_nodo_general("AND","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[6])
        t[0] = nodo

    else:
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("BETWEEN","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(crear_nodo_general("AND","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[5])
        t[0] = nodo

    #t[0] = Between(t[1], t[3], t[5], 'BETWEEN', t.lexer.lineno, t.lexer.lexpos) if t[2] == 'LIKE' else Between(t[1], t[4], t[5], 'NOT_BETWEEN', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_in(t):
    '''expre : expre IN expre
            | expre NOT IN expre
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[2] == "NOT":
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("NOT IN","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[4])
        t[0] = nodo

    else: 
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("IN","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo

def p_operadores_is(t):
    '''expre : expre IS NULL
            | expre IS NOT NULL
            | expre IS DISTINCT FROM expre
            | expre IS NOT DISTINCT FROM expre
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    if t[3] == 'NULL':
        nodo.hijos.append(crear_nodo_general("IS NULL","",t.lexer.lineno, t.lexer.lexpos))
    if t[3] == 'DISTINCT':
        nodo.hijos.append(crear_nodo_general("IS DISTINCT FROM","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[5])
    elif t[3] == 'NOT' and t[4] == 'NULL':
        nodo.hijos.append(crear_nodo_general("IS NOT NULL","",t.lexer.lineno, t.lexer.lexpos))
    elif t[3] == 'NOT' and t[4] == 'DISTINCT':
        nodo.hijos.append(crear_nodo_general("IS NOT DISTINCT FROM","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[6])
    t[0] = nodo

def p_operadores_agregacion(t):
    '''expre : AVG PARIZQ expre PARDER
            | COUNT PARIZQ expre PARDER
            | GREATEST PARIZQ lcol PARDER
            | LEAST PARIZQ lcol PARDER
            | MAX PARIZQ expre PARDER
            | MIN PARIZQ expre PARDER
            | SUM PARIZQ expre PARDER
            | TOP PARIZQ expre PARDER
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[1] == 'AVG':
        nodo.hijos.append(crear_nodo_general("AVG",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
        pass
    elif t[1] == 'COUNT':
        nodo.hijos.append(crear_nodo_general("COUNT",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
        pass
    elif t[1] == 'GREATEST':
        nodo.hijos.append(crear_nodo_general("GREATEST",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
        pass
    elif t[1] == 'LEAST':
        nodo.hijos.append(crear_nodo_general("LEAST",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
        pass
    elif t[1] == 'MAX':
        nodo.hijos.append(crear_nodo_general("MAX",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
        pass
    elif t[1] == 'MIN':
        nodo.hijos.append(crear_nodo_general("MIN",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
        pass
    elif t[1] == 'SUM':
        nodo.hijos.append(crear_nodo_general("SUM",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
        pass
    elif t[1] == 'TOP':
        nodo.hijos.append(crear_nodo_general("TOP",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
        pass

def p_operadores_matematica(t):
    '''expre : ABS PARIZQ expre PARDER 
            | CBRT PARIZQ expre PARDER 
            | CEIL PARIZQ expre PARDER 
            | CEILING PARIZQ expre PARDER 
            | DEGREES PARIZQ expre PARDER 
            | DIV PARIZQ expre COMA expre  PARDER
            | EXP PARIZQ expre PARDER 
            | FACTORIAL PARIZQ expre PARDER 
            | FLOOR PARIZQ expre PARDER 
            | GCD PARIZQ expre COMA expre PARDER
            | LCM PARIZQ expre PARDER 
            | LN PARIZQ expre PARDER 
            | LOG PARIZQ expre PARDER 
            | LOG10 PARIZQ expre PARDER 
            | MIN_SCALE PARIZQ expre PARDER
            | MOD PARIZQ expre COMA expre PARDER 
            | PI PARIZQ PARDER 
            | POWER PARIZQ expre COMA expre PARDER 
            | RADIANS PARIZQ expre PARDER 
            | RANDOM PARIZQ PARDER 
            | ROUND PARIZQ expre PARDER 
            | SCALE PARIZQ expre PARDER 
            | SETSEED PARIZQ expre PARDER
            | SIGN PARIZQ expre PARDER
            | SQRT PARIZQ expre PARDER 
            | TRIM_SCALE PARIZQ expre PARDER 
            | TRUNC PARIZQ expre PARDER 
            | WIDTH_BUCKET PARIZQ expresion COMA expresion COMA expresion COMA expresion PARDER 
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[1] == 'ABS':
        nodo.hijos.append(crear_nodo_general("ABS",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'CBRT':
        nodo.hijos.append(crear_nodo_general("CBRT",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'CEIL':
        nodo.hijos.append(crear_nodo_general("CEIL",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'CEILING':
        nodo.hijos.append(crear_nodo_general("CEILING",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'DEGREES':
        nodo.hijos.append(crear_nodo_general("DEGREES",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'DIV':
        nodo.hijos.append(crear_nodo_general("DIV",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(t[5])
        t[0] = nodo
    elif t[1] == 'EXP':
        nodo.hijos.append(crear_nodo_general("EXP",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'FACTORIAL':
        nodo.hijos.append(crear_nodo_general("FACTORIAL",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'FLOOR':
        nodo.hijos.append(crear_nodo_general("FLOOR",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'GCD':
        nodo.hijos.append(crear_nodo_general("GCD",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(t[5])
        t[0] = nodo
    elif t[1] == 'LCM':
        nodo.hijos.append(crear_nodo_general("LCM",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'LN':
        nodo.hijos.append(crear_nodo_general("LN",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'LOG':
        nodo.hijos.append(crear_nodo_general("LOG",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'LOG10':
        nodo.hijos.append(crear_nodo_general("LOG10",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'MIN_SCALE':
        nodo.hijos.append(crear_nodo_general("MIN_SCALE",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'MOD':
        nodo.hijos.append(crear_nodo_general("MOD",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(t[5])
        t[0] = nodo
    elif t[1] == 'PI':
        nodo.hijos.append(crear_nodo_general("PI",t[1],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'POWER':
        nodo.hijos.append(crear_nodo_general("POWER",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(t[5])
        t[0] = nodo
    elif t[1] == 'RADIANS':
        nodo.hijos.append(crear_nodo_general("RADIANS",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'RANDOM':
        nodo.hijos.append(crear_nodo_general("RANDOM",t[1],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'ROUND':
        nodo.hijos.append(crear_nodo_general("ROUND",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'SCALE':
        nodo.hijos.append(crear_nodo_general("SCALE",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'SETSEED':
        nodo.hijos.append(crear_nodo_general("SETSEED",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'SIGN':
        nodo.hijos.append(crear_nodo_general("SIGN",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'SQRT':
        nodo.hijos.append(crear_nodo_general("SQRT",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'TRIM_SCALE':
        nodo.hijos.append(crear_nodo_general("TRIM_SCALE",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'TRUNC':
        nodo.hijos.append(crear_nodo_general("TRUNC",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'WIDTH_BUCKET':
        nodo.hijos.append(crear_nodo_general("WIDTH_BUCKET",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(t[5])
        nodo.hijos.append(t[7])
        nodo.hijos.append(t[9])
        t[0] = nodo

def p_operadores_binarias(t):  
    ''' expre : CONVERT PARIZQ expre AS tipo PARDER
            | DECODE PARIZQ expre COMA expre PARDER
            | ENCODE PARIZQ expre COMA expre PARDER
            | GET_BYTE PARIZQ expre COMA ENTERO PARDER
            | LENGTH PARIZQ expre PARDER
            | MD5 PARIZQ expre PARDER
            | SET_BYTE PARIZQ expre COMA ENTERO COMA ENTERO PARDER
            | SHA256 PARIZQ expre PARDER
            | SUBSTR PARIZQ expre COMA ENTERO COMA ENTERO PARDER
            | SUBSTRING PARIZQ expre COMA ENTERO COMA ENTERO PARDER
            | TRIM PARIZQ expre PARDER
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[1] == 'CONVERT':
        nodo.hijos.append(crear_nodo_general("CONVERT",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(t[5])
        t[0] = nodo
    elif t[1] == 'DECODE':
        nodo.hijos.append(crear_nodo_general("DECODE",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'ENCODE':
        nodo.hijos.append(crear_nodo_general("ENCODE",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'GET_BYTE':
        nodo.hijos.append(crear_nodo_general("GET_BYTE",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(crear_nodo_general("ENTERO",t[5],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'LENGTH':
        nodo.hijos.append(crear_nodo_general("LENGTH",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'MD5':
        nodo.hijos.append(crear_nodo_general("MD5",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'SET_BYTE':
        nodo.hijos.append(crear_nodo_general("GET_BYTE",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(crear_nodo_general("ENTERO",t[5],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(crear_nodo_general("ENTERO",t[7],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'SHA256':
        nodo.hijos.append(crear_nodo_general("SHA256",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    elif t[1] == 'SUBSTR':
        nodo.hijos.append(crear_nodo_general("SUBSTR",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(crear_nodo_general("ENTERO",t[5],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(crear_nodo_general("ENTERO",t[7],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'SUBSTRING':
        nodo.hijos.append(crear_nodo_general("SUBSTRING",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(crear_nodo_general("ENTERO",t[5],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(crear_nodo_general("ENTERO",t[7],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'TRIM':
        nodo.hijos.append(crear_nodo_general("TRIM",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo

def p_operadores_trigonometricas(t):  
    ''' expre : ACOS PARIZQ expre PARDER
            | ACOSD PARIZQ expre PARDER
            | ACOSH PARIZQ expre PARDER
            | ASIN PARIZQ expre PARDER
            | ASIND PARIZQ expre PARDER
            | ASINH PARIZQ expre PARDER
            | ATAN PARIZQ expre PARDER
            | ATAN2 PARIZQ expre COMA expre PARDER
            | ATAN2D PARIZQ expre COMA expre PARDER
            | ATAND PARIZQ expre PARDER 
            | ATANH PARIZQ expre PARDER          
            | COS PARIZQ expre PARDER
            | COSD PARIZQ expre PARDER
            | COSH PARIZQ expre PARDER
            | COT PARIZQ expre PARDER
            | COTD PARIZQ expre PARDER
            | SIN PARIZQ expre PARDER
            | SIND PARIZQ expre PARDER
            | SINH PARIZQ expre PARDER
            | TAN PARIZQ expre PARDER
            | TAND PARIZQ expre PARDER
            | TANH PARIZQ expre PARDER
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if len(t) == 5:
        nodo.hijos.append(crear_nodo_general(t[1],t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        t[0] = nodo
    else:
        nodo.hijos.append(crear_nodo_general(t[1],t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(t[5])
        t[0] = nodo
            
def p_cadena_o_caracter(t):
    '''
    cadena_o_caracter : CADENA
                      | CARACTER
    '''


def p_operadores_otros(t):
    ''' expre : EXTRACT PARIZQ tiempo FROM TIMESTAMP cadena_o_caracter PARDER
            | NOW PARIZQ PARDER
            | DATE_PART PARIZQ cadena_o_caracter COMA INTERVAL cadena_o_caracter PARDER
            | CURRENT_DATE
            | CURRENT_TIME
            | TIMESTAMP cadena_o_caracter
            | CASE lcase END 
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    if t[1] == 'EXTRACT':
        nodo.hijos.append(crear_nodo_general("EXTRACT",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(crear_nodo_general("FROM TIMESTAMP","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(T[6])
        t[0] = nodo
    elif t[1] == 'NOW':
        nodo.hijos.append(crear_nodo_general("NOW",t[1],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'DATE_PART':
        nodo.hijos.append(crear_nodo_general("DATE_PART",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(t[6])
        t[0] = nodo
    elif t[1] == 'CURRENT_DATE':
        nodo.hijos.append(crear_nodo_general("CURRENT_DATE",t[1],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'CURRENT_TIME':
        nodo.hijos.append(crear_nodo_general("CURRENT_TIME",t[1],t.lexer.lineno, t.lexer.lexpos))
        t[0] = nodo
    elif t[1] == 'TIMESTAMP':
        nodo.hijos.append(crear_nodo_general("TIMESTAMP",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[2])
        t[0] = nodo
    elif t[1] == 'CASE':
        nodo.hijos.append(crear_nodo_general("CASE","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[2])
        t[0] = nodo

def p_operadores_parentesis(t):
    ''' expre : PARIZQ expre PARDER
            | PARIZQ query PARDER
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[2])
    t[0] = nodo

 
def p_operadores_logicos5(t):
    ''' expre :  expresion
    '''
    nodo = crear_nodo_general("expre","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_tiempo1(t):
    ''' tiempo :  YEAR
    '''
    t[0] = crear_nodo_general("tiempo",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_tiempo2(t):
    ''' tiempo :  MONTH
    '''
    t[0] = crear_nodo_general("tiempo",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_tiempo3(t):
    ''' tiempo :  DAY
    '''
    t[0] = crear_nodo_general("tiempo",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_tiempo4(t):
    ''' tiempo :  HOUR
    '''
    t[0] = crear_nodo_general("tiempo",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_tiempo5(t):
    ''' tiempo :  MINUTE
    '''
    t[0] = crear_nodo_general("tiempo",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_tiempo6(t):
    ''' tiempo :  SECOND
    '''
    t[0] = crear_nodo_general("tiempo",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_campos_tablas(t):
    '''campos : campos COMA ID tipo lista_op
    '''
    #ESTOY HACIENDO ESTA
    nodo = t[1]
    nodo.hijos.append(crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[4])
    nodo.hijos.append(t[5])
    t[0] = nodo

def p_campos_tablas1(t):
    '''campos : campos COMA ID tipo
    '''
    nodo = t[1]
    nodo.hijos.append(crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[4])
    t[0] = nodo

#def p_campos_tablas2(t):
#    '''campos : campos COMA CHECK expre
#    '''
    #AQUI ESTOY TRABAJANDO
#    t[1].append(Tipo_Constraint(None,Tipo_Dato_Constraint.CHECK,t[4]))
#    t[0] = t[1]

#def p_campos_tablas3(t):
#    '''campos : campos COMA CONSTRAINT ID CHECK expre
#    '''
#    t[1].append(Tipo_Constraint(t[4],Tipo_Dato_Constraint.CHECK,t[4]))
#    t[0] = t[1]

def p_campos_tablas4(t):
    '''campos : campos COMA UNIQUE PARIZQ lista_id PARDER
    '''
    nodo = t[1]
    nodo.hijos.append(crear_nodo_general("UNIQUE","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[5])
    t[0] = nodo

def p_campos_tablas5(t):
    '''campos : campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
    '''
    nodo = t[1]
    nodo.hijos.append(crear_nodo_general("FOREIGN KEY","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[6])
    nodo.hijos.append(crear_nodo_general("REFERENCES","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("ID",t[9],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[11])
    t[0] = nodo

def p_campos_tablas6(t):
    '''campos : campos COMA PRIMARY KEY PARIZQ lista_id PARDER
    '''
    nodo = t[1]
    nodo.hijos.append(crear_nodo_general("PRIMARY KEY","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[6])
    t[0] = nodo

def p_campos_tablas7(t):
    '''campos : ID tipo lista_op
    '''
    nodo = crear_nodo_general("campos","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    nodo.hijos.append(t[3])
    t[0] = nodo

def p_campos_tablas8(t):
    '''campos : ID tipo
    '''
    nodo = crear_nodo_general("campos","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_lista_id1(t):
    '''lista_id : lista_id COMA ID
    '''
    nodo = t[1]
    nodo.hijos.append(t[3])
    t[0] = nodo

def p_lista_id2(t):
    '''lista_id : ID
    '''
    nodo = crear_nodo_general("lista_id","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo


def p_lista_op1(t):
    '''lista_op : lista_op opcion
    '''
    nodo = t[1]
    nodo.hijos.append(t[2])
    t[0] = nodo


def p_lista_op2(t):
    '''lista_op : opcion
    '''
    nodo = crear_nodo_general("lista_op","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_opcion(t):
    '''opcion : PRIMARY KEY
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("PRIMARY KEY","",t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_opcion1(t):
    '''opcion : REFERENCES ID PARIZQ lista_id PARDER
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("REFERENCES","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("ID",t[2],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_opcion2(t):
    '''opcion : DEFAULT expresion
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("DEFAULT","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_opcion3(t):
    '''opcion : NOT NULL
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("NOT NULL","",t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_opcion4(t):
    '''opcion : NULL
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("NULL","",t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_opcion5(t):
    '''opcion : UNIQUE
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("UNIQUE","",t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_opcion6(t):
    '''opcion : CONSTRAINT ID UNIQUE
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("CONSTRAINT","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("ID",t[2],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("UNIQUE","",t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_opcion7(t):
    '''opcion : CONSTRAINT ID CHECK expre
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("CONSTRAINT","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("ID",t[2],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("CHECK","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_opcion8(t):
    '''opcion : CHECK expre
    '''
    nodo = crear_nodo_general("opcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("CHECK","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_lista_expresiones(t):
    '''
    l_expresiones : l_expresiones COMA expre
    '''
    nodo = t[1]
    nodo.hijos.append(t[3])
    t[0] = nodo

def p_lista_expresiones1(t):
    '''
    l_expresiones : expre
    '''
    nodo = crear_nodo_general("l_expresiones","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_expresion(t):
    '''
    expresion : CADENA
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("CADENA",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_expresion1(t):
    '''expresion : CARACTER
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("CARACTER",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_expresion2(t):
    '''expresion : ENTERO
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ENTERO",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo
    
def p_expresion3(t):
    '''expresion : FDECIMAL
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("FDECIMAL",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_expresion4(t):
    '''expresion : DOUBLE
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("DOUBLE",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_expresion5(t):
    '''expresion : ID
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_expresion61(t):
    '''expresion : ID PUNTO ID
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID.ID",t[1] + "." + t[3],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_expresion62(t):
    '''expresion : ID PUNTO POR
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID.*",t[1] + ".*",t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo


def p_expresion7(t):
    '''expresion : ARROBA ID
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("@ID","@" + t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_expresion8(t):
    '''expresion : ID PARIZQ lcol PARDER
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[3])
    t[0] = nodo

def p_expresion9(t):
    '''expresion : TRUE
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("TRUE",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_expresion10(t):
    '''expresion : FALSE
    '''
    nodo = crear_nodo_general("expresion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("FALSE",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_lista_columas(t):
    '''lcol : lcol COMA expre
    '''
    nodo = t[1]
    nodo.hijos.append(t[3])
    t[0] = nodo

def p_lista_columas1(t):
    '''lcol : lcol COMA expre nombre
    '''
    nodo = t[1]
    nodo.hijos.append(t[3])
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_lista_columas2(t):
    '''lcol : lcol COMA expre AS nombre
    '''
    nodo = t[1]
    nodo.hijos.append(t[3])
    nodo.hijos.append(t[5])
    t[0] = nodo


def p_lista_columas01(t):
    '''lcol : POR
    '''
    nodo = crear_nodo_general("lcol",t[1],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("POR",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_lista_columas3(t):
    '''lcol : expre
    '''
    nodo = crear_nodo_general("lcol",t[1],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo
    
def p_lista_columas4(t):
    '''lcol : expre nombre
    '''
    nodo = crear_nodo_general("lcol",t[1],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_lista_columas5(t):
    '''lcol : expre AS nombre
    '''
    nodo = crear_nodo_general("lcol",t[1],t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_nombre(t):
    '''nombre : ID
        | CADENA
        | CARACTER
    '''
    t[0] = crear_nodo_general("nombre",t[1],t.lexer.lineno, t.lexer.lexpos)

#----------------------TIPO DE DATOS---------------------------------
def p_tipo_datos(t):
    '''tipo : INT
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos1(t):
    '''tipo : DATE
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

# NO RECUERDO PARA QUE IMPLEMENTAMOS ESTA PARTE ENTONCES LA COMENTE
#def p_tipo_datos2(t):
#    '''tipo : ID PARIZQ ID PARDER
#    '''
#    t[0]=t[1]

def p_tipo_datos_varchar(t):
    '''tipo : VARCHAR PARIZQ ENTERO PARDER
    '''
    nodo = crear_nodo_general("tipo",str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]),t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_varchar1(t):
    '''tipo : CHAR PARIZQ ENTERO PARDER
    '''
    nodo = crear_nodo_general("tipo",str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]),t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_varchar2(t):
    '''tipo : CHARACTER VARYING PARIZQ ENTERO PARDER
    '''
    nodo = crear_nodo_general("tipo","CHARACTER VARYING" + str(t[3]) + str(t[4]) + str(t[5]),t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_varchar3(t):
    '''tipo : CHARACTER PARIZQ ENTERO PARDER
    '''
    nodo = crear_nodo_general("tipo",str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]),t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_varchar4(t):
    '''tipo : TEXT
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

#ESTE NO SE CONTEMPLO EN LA GRAMATICA DE MAEDA
def p_tipo_datos_decimal(t):
    '''tipo : DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
    '''
    nodo = crear_nodo_general("tipo",str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]),t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

#def p_tipo_datos_decimal1(t):
#    '''tipo : DOUBLE
#    '''
#    t[0] = Tipo("",Tipo_Dato.DOUBLE_PRECISION)
    
def p_tipo_datos_decimal2(t):
    '''tipo : DECIMAL
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

#ESTE NO SE CONTEMPLO EN LA GRAMATICA
#def p_tipo_datos_decimal3(t):
#    '''tipo : FLOAT PARIZQ ENTERO COMA ENTERO PARDER
#    '''
#    t[0]= 

#HAY QUE VALIDAR ESTE, CREO QUE ESTA DEMAS ACA
#def p_tipo_datos_int(t):
#    '''tipo : ENTERO
#    '''
#    t[0]=Tipo("",Tipo_Dato.INTEGER)

def p_tipo_datos_int1(t):
    '''tipo : SMALLINT
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_int2(t):
    '''tipo : INTEGER
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_int3(t):
    '''tipo : BIGINT
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_int4(t):
    '''tipo : NUMERIC
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_int5(t):
    '''tipo : REAL
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_int6(t):
    '''tipo : DOUBLE PRECISION
    '''
    nodo = crear_nodo_general("tipo","DOUBLE PRECISION",t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_int7(t):
    '''tipo : MONEY
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_int8(t):
    '''tipo : BOOLEAN
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_date1(t):
    '''tipo : TIME
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos_date2(t):
    '''tipo : INTERVAL
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo

def p_tipo_datos2(t):
    '''tipo : ID 
    '''
    nodo = crear_nodo_general("tipo",t[1],t.lexer.lineno, t.lexer.lexpos)
    t[0] = nodo






########################################### GRAMATICA FASE 2 ########################################

def p_exect_func_pro(t):
    '''
    instruccion     :   EXECUTE ID PARDER l_expresiones PARIZQ PUNTO_COMA
    '''
    nodo = crear_nodo_general("EXECUTE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[2],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_procedimiento(t):
    '''
    instruccion     :   CREATE PROCEDURE ID PARIZQ parametros_funcion PARDER LANGUAGE PLPGSQL AS DOLLAR DOLLAR declaraciones_funcion BEGIN contenido_funcion END PUNTO_COMA DOLLAR DOLLAR
    '''
    nodo = crear_nodo_general("CREATE PROCEDURE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[5])
    nodo.hijos.append(t[12])
    nodo.hijos.append(t[14])
    t[0] = nodo


#DECLARACION DE UNA FUNCION
def p_funciones(t):
    '''
    instruccion    :   CREATE FUNCTION ID PARIZQ parametros_funcion PARDER returns_n retorno_funcion declaraciones_funcion BEGIN contenido_funcion END PUNTO_COMA DOLLAR DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    nodo = crear_nodo_general("CREATE FUNCTION","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[5])
    nodo.hijos.append(t[7])
    nodo.hijos.append(t[8])
    nodo.hijos.append(t[9])
    nodo.hijos.append(t[11])
    t[0] = nodo

def p_funciones_drop(t):
    '''
    instruccion : DROP FUNCTION if_op ID PUNTO_COMA
    '''
    nodo = crear_nodo_general("DROP FUNCTION","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[3])
    nodo.hijos.append(crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_procedimientos_drop(t):
    '''
    instruccion : DROP PROCEDURE if_op ID PUNTO_COMA
    '''
    nodo = crear_nodo_general("DROP PROCEDURE","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[3])
    nodo.hijos.append(crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_parametros_funcion(t):
    '''
    parametros_funcion  : lista_parametros_funcion 
    '''
    t[0] = t[1]

def p_parametros_funcion_e(t):
    '''
    parametros_funcion  :
    '''
    t[0] = None

def p_lista_parametros_funcion(t):
    '''
    lista_parametros_funcion    :   lista_parametros_funcion COMA parametro_fucion
    '''
    nodo = t[1]
    nodo.hijos.append(t[3])
    t[0] = nodo


def p_lista_parametros_funcion2(t):
    '''
    lista_parametros_funcion    :   parametro_fucion
    '''
    nodo = crear_nodo_general("lista_parametros_funcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_parametro_fucion(t):
    '''
    parametro_fucion 	: 	ID tipo
					    |	tipo
    '''
    nodo = crear_nodo_general("parametro_fucion","",t.lexer.lineno, t.lexer.lexpos)
    if len(t) == 3:
        nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[2])
    else:
        nodo.hijos.append(t[2])
    t[0] = nodo


def p_returns(t):
    '''
    returns_n 	:	RETURNS 
    '''
    t[0] = crear_nodo_general("RETURNS","",t.lexer.lineno, t.lexer.lexpos)

def p_returns_e(t):
    '''
    returns_n   :
    '''
    t[0] = None

def p_retorno_funcion(t):
    '''
    retorno_funcion :   tipo AS DOLLAR DOLLAR
				    |   TABLE PARIZQ lista_campos_tabla PARDER AS DOLLAR DOLLAR
				    |   AS DOLLAR DOLLAR
    '''
    nodo = crear_nodo_general("retorno_funcion","",t.lexer.lineno, t.lexer.lexpos)
    if len(t) == 4:
        nodo.hijos.append(crear_nodo_general("AS $$","",t.lexer.lineno, t.lexer.lexpos))
    elif len(t) == 5:
        nodo.hijos.append(t[1])
        nodo.hijos.append(crear_nodo_general("AS $$","",t.lexer.lineno, t.lexer.lexpos))
    else:
        nodo.hijos.append(crear_nodo_general("TABLA","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(crear_nodo_general("AS $$","",t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_lista_campos_tabla(t):
    '''
    lista_campos_tabla  :	lista_campos_tabla COMA ID tipo
    '''
    nodo = t[1]
    nodo.hijos.append(crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_lista_campos_tabla2(t):
    '''
    lista_campos_tabla  :	ID tipo
    '''
    nodo = crear_nodo_general("lista_campos_tabla","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_declaraciones_funcion(t):
    '''
    declaraciones_funcion 	: 	DECLARE list_dec_var_funcion
    ''' 
    nodo = crear_nodo_general("DECLARE","",t.lexer.lineno, t.lexer.lexpos) 
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_declaraciones_funcion_e(t):
    '''
    declaraciones_funcion   :
    '''    
    t[0] = None

def p_list_dec_var_funcion(t):
    '''
    list_dec_var_funcion 	:	list_dec_var_funcion dec_var_funcion PUNTO_COMA
    '''
    nodo = t[1]
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_list_dec_var_funcion2(t):
    '''
    list_dec_var_funcion 	:	dec_var_funcion PUNTO_COMA
    '''
    nodo = crear_nodo_general("list_dec_var_funcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo

def p_dec_var_funcion(t):
    '''
    dec_var_funcion : 	ID constant_n tipo nnull aisgnacion_valor 
    '''
    nodo = crear_nodo_general("dec_var_funcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    nodo.hijos.append(t[3])
    nodo.hijos.append(t[4])
    nodo.hijos.append(t[5])
    t[0] = nodo
    
def p_dec_var_funcion2(t):
    '''
    dec_var_funcion : 	ID ALIAS FOR DOLLAR ENTERO
				    |	ID ALIAS FOR ID
    '''
    nodo = crear_nodo_general("dec_var_funcion","",t.lexer.lineno, t.lexer.lexpos)
    if len(t) == 5:
        nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(crear_nodo_general("ALIAS FOR","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos))
    else:
        nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(crear_nodo_general("ALIAS FOR $","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(crear_nodo_general("ENTERO",t[5],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_dec_var_funcion3(t):
    '''
    dec_var_funcion : 	ID tabla_typerow MODULO type_row
    '''
    nodo = crear_nodo_general("dec_var_funcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    nodo.hijos.append(crear_nodo_general("MODULO","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_tabla_typerow(t):
    '''
    tabla_typerow   :   ID PUNTO ID
                    |   ID
    '''
    nodo = crear_nodo_general("tabla_typerow","",t.lexer.lineno, t.lexer.lexpos)
    if len(t) == 4:
        nodo.hijos.append(crear_nodo_general("ID.ID",str(t[1]) + str(t[2]) + str(t[3]),t.lexer.lineno, t.lexer.lexpos))
    else:
        nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo


def p_type_row(t):
    '''
    type_row 	:	TYPE
			    |	ROWTYPE
    '''
    t[0] = crear_nodo_general("type_row",t[1],t.lexer.lineno, t.lexer.lexpos)


def p_constant(t):
    '''
    constant_n  :   CONSTANT
    '''
    t[0] = crear_nodo_general("CONSTANT",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_constant_e(t):
    '''
    constant_n  :   
    '''
    t[0] = None

def p_nnull(t):
    '''
    nnull : NOT NULL
    '''
    t[0] = crear_nodo_general("NOT NULL",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_nnull_e(t):
    '''
    nnull :
    '''
    t[0] = None

def p_aisgnacion_valor(t):
    '''
    aisgnacion_valor 	: 	DEFAULT expre 
					    |	DOSP_IGUAL expre 
					    |	IGUAL expre 
    '''
    nodo = crear_nodo_general("aisgnacion_valor","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general(t[1],"",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    t[0] = t[2]


def p_aisgnacion_valor_e(t):
    '''
    aisgnacion_valor    :
    '''
    t[0] = None

def p_contenido_funcion(t):
    '''
    contenido_funcion   : contenido_funcion cont_funcion''' 
    nodo = t[1]
    nodo.hijos.append(t[2])
    t[0] = nodo

def p_contenido_funcion2(t):
    '''
    contenido_funcion   : cont_funcion '''
    nodo = crear_nodo_general("contenido_funcion","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[1])
    t[0] = nodo
    
def p_cont_funcion(t):
    '''
    cont_funcion    :   sentencia_if
                    |   instruccion
                    |   sentencia_retorno
                    |   asignacion_var
    '''
    t[0] = t[1]

def p_sentencia_retorno(t):
    '''
    sentencia_retorno   :  RETURN PUNTO_COMA
                        | RETURN expre PUNTO_COMA
    '''
    nodo = crear_nodo_general("sentencia_retorno","",t.lexer.lineno, t.lexer.lexpos)
    if len(t) == 3:
        nodo.hijos.append(crear_nodo_general("RETURN","",t.lexer.lineno, t.lexer.lexpos))
    else:
        nodo.hijos.append(crear_nodo_general("RETURN","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[2])
    t[0] = nodo

def p_asignacion_var(t):
    '''
    asignacion_var  :   ID IGUAL expre PUNTO_COMA
                    |   ID DOSP_IGUAL expre PUNTO_COMA
    '''
    nodo = crear_nodo_general("asignacion_var","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("IGUAL",t[2],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[3])
    t[0] = nodo


def p_sentencia_if(t):    
    '''
     sentencia_if : IF expre THEN instrucciones_if condicionesif ELSE  instrucciones_if END IF PUNTO_COMA
				  | IF expre THEN instrucciones_if condicionesif END IF PUNTO_COMA
				  | IF expre THEN instrucciones_if ELSE  instrucciones_if END IF PUNTO_COMA
				  | IF expre THEN instrucciones_if END IF PUNTO_COMA
				  | CASE ID condiciones_cuando ELSE instrucciones_if END CASE PUNTO_COMA
				  | CASE ID condiciones_cuando END CASE PUNTO_COMA
				  | CASE condiciones_cuandoB ELSE instrucciones_if END CASE PUNTO_COMA
				  | CASE condiciones_cuandoB END CASE PUNTO_COMA
				  | BEGIN instrucciones_if EXCEPTION WHEN l_identificadores THEN instrucciones_if END PUNTO_COMA
				  | BEGIN instrucciones_if EXCEPTION WHEN sql_states THEN instrucciones_if END PUNTO_COMA
    '''
    nodo = crear_nodo_general("sentencia_if","",t.lexer.lineno, t.lexer.lexpos)
    if t[1] == "IF" and len(t) == 11:
        nodo.hijos.append(t[2])
        nodo.hijos.append(t[4])
        nodo.hijos.append(t[5])
        nodo.hijos.append(crear_nodo_general("ELSE","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[7])

    elif t[1] == "IF" and  len(t) == 8:
        nodo.hijos.append(t[2])
        nodo.hijos.append(t[4])

    elif t[1] == "IF" and len(t) == 10:
        nodo.hijos.append(t[2])
        nodo.hijos.append(t[4])
        nodo.hijos.append(crear_nodo_general("ELSE","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[6])

    elif t[1] == "IF" and len(t) == 9:
        nodo.hijos.append(t[2])
        nodo.hijos.append(t[4])
        nodo.hijos.append(t[5])

    elif t[1] == "CASE" and len(t) == 6:
        nodo.hijos.append(t[2])
        
    elif t[1] == "CASE" and len(t) == 8:
        nodo.hijos.append(t[2])
        nodo.hijos.append(crear_nodo_general("ELSE","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[4])
        
    elif t[1] == "CASE" and len(t) == 7:
        nodo.hijos.append(crear_nodo_general("ID",t[2],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        
    elif t[1] == "CASE" and len(t) == 9:
        nodo.hijos.append(crear_nodo_general("ID",t[2],t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[3])
        nodo.hijos.append(crear_nodo_general("ELSE","",t.lexer.lineno, t.lexer.lexpos))
        nodo.hijos.append(t[5])
    else:
        nodo.hijos.append(crear_nodo_general("EXCEPTION","",t.lexer.lineno, t.lexer.lexpos))
        
    t[0] = nodo
    
def p_instrucciones_if(t):
    ''' 
    instrucciones_if : instrucciones_if instruccion_if 
                     | instruccion_if
    '''
    if len(t) == 3:
        nodo = t[1]
        nodo.hijos.append(t[2])
        t[0] = nodo
    else:
        nodo = crear_nodo_general("instrucciones_if","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[1])
        t[0] = nodo
    
def p_instruccion_if(t):
    '''
    instruccion_if : cont_funcion
                   | expre PUNTO_COMA
                   | RAISE NOTICE CADENA PUNTO_COMA
                   | RAISE NOTICE CADENA COMA ID PUNTO_COMA
                   | RAISE NOTICE CARACTER PUNTO_COMA
                   | RAISE NOTICE CARACTER COMA ID PUNTO_COMA
    '''
    t[0] = t[1]

def p_condiciones_if(t):
    '''
    condicionesif : condicionesif condicionif
			      | condicionif
    '''
    if len(t) == 3:
        nodo = t[1]
        nodo.hijos.append(t[2])
        t[0] = nodo
    else:
        nodo = crear_nodo_general("condicionesif","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[1])
        t[0] = nodo

def p_condicion_if(t):
    '''
    condicionif : ELSIF expre THEN instrucciones_if 
			    | ELSEIF expre THEN instrucciones_if  
    '''
    nodo = crear_nodo_general(t[1],"",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[2])
    nodo.hijos.append(t[4])
    t[0] = nodo
    
def p_condiciones_cuando(t):
    '''
    condiciones_cuando : condiciones_cuando condicion_cuando
				       | condicion_cuando
    '''
    if len(t) == 3:
        nodo = t[1]
        nodo.hijos.append(t[2])
        t[0] = nodo
    else:
        nodo = crear_nodo_general("condiciones_cuando","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[1])
        t[0] = nodo

def p_condicion_cuando(t):
    '''
    condicion_cuando : WHEN l_expresiones THEN instrucciones_if

    '''
    nodo = crear_nodo_general("condicion_cuando","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[2])
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_condiciones_cuando_B(t):
    '''
    condiciones_cuandoB : condiciones_cuandoB condicion_cuandoB
					    | condicion_cuandoB
    '''
    if len(t) == 3:
        nodo = t[1]
        nodo.hijos.append(t[2])
        t[0] = nodo
    else:
        nodo = crear_nodo_general("condiciones_cuandoB","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[1])
        t[0] = nodo

def p_condicion_cuando_B(t):
    '''
    condicion_cuandoB : WHEN expre THEN instrucciones_if
    '''
    nodo = crear_nodo_general("condicion_cuandoB","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[2])
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_sql_states(t):
    '''
    sql_states : sql_states OR sql_state
			   | sql_state
    '''
    if len(t) == 4:
        nodo = t[1]
        nodo.hijos.append(t[3])
        t[0] = nodo
    else:
        nodo = crear_nodo_general("sql_states","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[1])
        t[0] = nodo

def p_sql_state(t):
    '''
    sql_state : SQLSTATE CADENA
    '''
    t[0] = crear_nodo_general("SQLSTATE",t[2],t.lexer.lineno, t.lexer.lexpos)

def p_identificadores(t):
    '''
    l_identificadores : l_identificadores OR ID
                      | ID
    '''
    if len(t) == 4:
        nodo = t[1]
        nodo.hijos.append(t[3])
        t[0] = nodo
    else:
        nodo = crear_nodo_general("l_identificadores","",t.lexer.lineno, t.lexer.lexpos)
        nodo.hijos.append(t[1])
        t[0] = nodo

def p_instruccion_index(t):
    '''
    instruccion : CREATE unique_op INDEX nombre_op ON ID hash_op PARIZQ l_indexes PARDER where_op PUNTO_COMA
    '''
    nodo = crear_nodo_general("CREATE INDEX","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[2])
    nodo.hijos.append(t[4])
    nodo.hijos.append(crear_nodo_general("ID",t[6],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[7])
    nodo.hijos.append(t[9])
    nodo.hijos.append(t[11])
    t[0] = nodo

def p_instruccion_del_index(t):
    '''
    instruccion : DROP INDEX if_op ID PUNTO_COMA
    '''
    nodo = crear_nodo_general("DROP INDEX","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[3])
    nodo.hijos.append(crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_instruccion_alter_index(t):
    '''
    instruccion : ALTER INDEX if_op ID ALTER column_op ID ID PUNTO_COMA
    '''
    nodo = crear_nodo_general("ALTER INDEX","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(t[3])
    nodo.hijos.append(crear_nodo_general("ID",t[4],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("ALTER","",t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[6])
    nodo.hijos.append(crear_nodo_general("ID",t[7],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("ID",t[8],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo


def p_index_column(t):
    '''
    column_op : COLUMN
    '''
    t[0] = crear_nodo_general("COLUMN","",t.lexer.lineno, t.lexer.lexpos)

def p_index_column_e(t):
    '''
    column_op : 
    '''
    t[0] = None

def p_index_if_exists(t):
    '''
    if_op : IF EXISTS
    '''
    t[0] = crear_nodo_general("IF EXISTS","",t.lexer.lineno, t.lexer.lexpos)

def p_index_if_e(t):
    '''
    if_op : 
    '''
    t[0] = None

def p_index_nombre(t):
    '''
    nombre_op : ID
    '''
    t[0] = crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos)

def p_index_nombre_e(t):
    '''
    nombre_op : 
    '''
    t[0] = None

def p_index_unique(t):
    '''
    unique_op : UNIQUE
    '''
    t[0] = crear_nodo_general("UNIQUE","",t.lexer.lineno, t.lexer.lexpos)

def p_index_unique_e(t):
    '''
    unique_op : 
    '''
    t[0] = None

def p_index_hash(t):
    '''
    hash_op : USING HASH
    '''
    t[0] = crear_nodo_general("USING HASH","",t.lexer.lineno, t.lexer.lexpos)

def p_index_hash_e(t):
    '''
    hash_op : 
    '''
    t[0] = None

def p_index_indexes(t):
    '''
    l_indexes : l_indexes COMA ID order_op null_op first_last_op
    '''
    nodo = t[1]
    nodo.hijos.append(crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[4])
    nodo.hijos.append(t[5])
    nodo.hijos.append(t[6])
    t[0] = nodo

def p_index_index(t):
    '''
    l_indexes : ID order_op null_op first_last_op
    '''
    nodo = crear_nodo_general("l_indexes","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(t[2])
    nodo.hijos.append(t[3])
    nodo.hijos.append(t[4])
    t[0] = nodo

def p_index_func(t):
    '''
    l_indexes : ID PARIZQ ID PARDER
    '''
    nodo = crear_nodo_general("l_indexes","",t.lexer.lineno, t.lexer.lexpos)
    nodo.hijos.append(crear_nodo_general("ID",t[1],t.lexer.lineno, t.lexer.lexpos))
    nodo.hijos.append(crear_nodo_general("ID",t[3],t.lexer.lineno, t.lexer.lexpos))
    t[0] = nodo

def p_index_order(t):
    '''
    order_op : ASC
            | DESC
    '''
    t[0] = crear_nodo_general(t[1],"",t.lexer.lineno, t.lexer.lexpos)

def p_index_order_e(t):
    '''
    order_op : 
    '''
    t[0] = None

def p_index_null(t):
    '''
    null_op : NULLS
    '''
    t[0] = crear_nodo_general("NULLS","",t.lexer.lineno, t.lexer.lexpos)

def p_index_null_e(t):
    '''
    null_op : 
    '''
    t[0] = None

def p_index_first_last(t):
    '''
    first_last_op : FIRST
                | LAST
    '''
    t[0] = crear_nodo_general(t[1],"",t.lexer.lineno, t.lexer.lexpos)

def p_index_first_last_e(t):
    '''
    first_last_op : 
    '''
    t[0] = None

def p_index_where(t):
    '''
    where_op : instructionWhere
    '''
    t[0] = t[1]

def p_index_where_e(t):
    '''
    where_op : 
    '''
    t[0] = None

#FIN DE LA GRAMATICA
# MODO PANICO ***************************************

def p_error(p):

    if not p:
        print("Fin del Archivo!")
        return
    dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {p.value}", p.lexer.lineno, find_column(lexer.lexdata,p))
    lista_lexicos.append(dato)
    while True:
        
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PUNTO_COMA':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con ;")
                break
        dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {tok.value}", p.lexer.lineno, find_column(lexer.lexdata,tok))
        lista_lexicos.append(dato)
        
    parser.restart()
    
def find_column(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    ast_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

parser = yacc.yacc()
def ejecutar_analisis(texto):
    
    #LIMPIAR VARIABLES
    columna=0
    lista_lexicos.clear()
    #se limpia analisis lexico
    lexer.input("")
    lexer.lineno = 0
    #se obtiene la acción de analisis sintactico
    print("inicio")
    return parser.parse(texto)