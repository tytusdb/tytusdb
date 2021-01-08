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

from Instrucciones.plpgsql import condicional_if, Funcion, DeclaracionVariable, DeclaracionAlias, condicional_case, Procedimiento, DeclaracionRetorno, AsignacionVariable, DropFuncion, DropProcedimiento, Execute

# IMPORTAMOS EL STORAGE
from storageManager import jsonMode as storage
from Instrucciones.Sql_create.Tipo_Constraint import *

lista_lexicos=lista_errores_lexico

# INICIA EN ANALISIS SINTACTICO


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
    t[1].append(t[2])
    t[0] = t[1]
    
def p_instrucciones_lista2(t):
    'instrucciones : instruccion '
    t[0] = [t[1]]


    
# CREATE DATABASE
def p_instruccion_create_database1(t):
    '''instruccion : CREATE DATABASE if_not_exists ID PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID PUNTO_COMA"
    strSent = "CREATE DATABASE " + t[3].strSent + " " + t[4] + ";"
    t[0] =CreateDatabase.CreateDatabase(t[4], None, t[3].valor, None, 1, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create_database2(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> ID PUNTO_COMA"
    strSent = "CREATE DATABASE " + t[3].strSent + " " + t[4] + " OWNER = " + t[7] + ";"
    t[0] =CreateDatabase.CreateDatabase(t[4],None,t[3].valor, t[7], 1, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create_database3(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> MODE IGUAL ENTERO PUNTO_COMA"
    strSent = "CREATE DATABASE " + t[3].strSent + " " + t[4] + " OWNER = " + t[7] + " MODE = " + str(t[10]) + ";"
    t[0] =CreateDatabase.CreateDatabase(t[4],None,t[3].valor, t[7], t[10], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create_database4(t):
    '''instruccion : CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    #                     ID    tipo  opcion ID2  ENTERO
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID MODE IGUAL ENTERO PUNTO_COMA"
    strSent = "CREATE DATABASE " + t[3].strSent + " " + t[4] + " MODE = " + str(t[7]) + ";"
    t[0] =CreateDatabase.CreateDatabase(t[4], None, t[3].valor, None, t[7], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# CREATE OR REPLACE DATABASE
def p_instruccion_create_or_database1(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID PUNTO_COMA"
    strSent = "CREATE OR REPLACE DATABASE " + t[5].strSent + " " + t[6] + ";"
    t[0] =CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, None, 1, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create_or_database2(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> PUNTO_COMA"
    strSent = "CREATE OR REPLACE DATABASE " + t[5].strSent + " " + t[6] + " OWNER = " + t[9] + ";"
    t[0] =CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], 1, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create_or_database3(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> MODE IGUAL ENTERO PUNTO_COMA"
    strSent = "CREATE OR REPLACE DATABASE " + t[5].strSent + " " + t[6] + " OWNER = " + t[9] + " MODE = " + str(t[12]) + ";"
    t[0] =CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], t[12], strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create_or_database4(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> : CREATE OR REPLACE DATABASE <if_not_exists> ID MODE IGUAL ENTERO PUNTO_COMA"
    strSent = "CREATE OR REPLACE DATABASE " + t[5].strSent + " " + t[6] + " MODE = " + str(t[9]) + ";"
    t[0] =CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], 1, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_owner(t):
    '''cowner : ID
                | CARACTER
                | CADENA
    '''
    t[0] = t[1]

def p_if_not_exists(t):
    '''if_not_exists : IF NOT EXISTS
    '''
    strGram = "<if_not_exists> ::= IF NOT EXISTS"
    strSent = "IF NOT EXISTS"
    t[0] = Primitivo.Primitivo("IF NOT EXISTS",Tipo_Dato.VARCHAR, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_if_not_exists1(t):
    '''if_not_exists : 
    '''
    strGram = "<if_not_exists> ::= "
    strSent = ""
    t[0] = Primitivo.Primitivo("NULL",Tipo_Dato.VARCHAR, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create1(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE TABLE ID PARIZQ <campos> PARDER PUNTO_COMA"

    strSent = "CREATE TABLE " + t[3] + "("
    for col in t[5]:
        strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ");"

    t[0] =CreateTable.CreateTable(t[3], None, t[5], None, strGram,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create2(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE TABLE ID PARIZQ <campos> PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA"
    strSent = "CREATE TABLE " + t[3] + "(" 
    for col in t[5]:
        strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ") INHERITS (" + t[9] + ");"

    t[0] =CreateTable.CreateTable(t[3],None, t[5], t[9], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_use(t):
    '''instruccion : USE ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= USE ID PUNTO_COMA"
    strSent = "USE " + t[2] + ";"
    t[0] =Use.Use(t[2], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_show_database1(t):
    '''instruccion : SHOW DATABASES PUNTO_COMA
    '''
    strGram = "<instruccion> ::= SHOW DATABASES PUNTO_COMA"
    strSent = "SHOW DATABASES;"
    t[0] =ShowDatabases.ShowDatabases(None, None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_show_database2(t):
    '''instruccion : SHOW DATABASES LIKE cadena_o_caracter PUNTO_COMA
    '''
    strGram = "<instruccion> ::= SHOW DATABASES LIKE cadena_o_caracter PUNTO_COMA"
    strSent = "SHOW DATABASES LIKE " + t[4] + ";"
    t[0] =ShowDatabases.ShowDatabases(t[4],None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_create_enumerated_type(t):
    '''instruccion : CREATE TYPE ID AS ENUM PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE TYPE ID AS ENUM PARIZQ <l_expresiones> PARDER PUNTO_COMA"
    strSent = "CREATE TYPE " + t[3] + " AS ENUM ("
    for col in t[7]:
        strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ");"

    t[0] =CreateType.CreateType(t[3],None,t[7], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)


def p_instruccion_truncate(t):
    '''instruccion : TRUNCATE TABLE ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= TRUNCATE TABLE ID PUNTO_COMA"
    strSent = "TRUNCATE TABLE " + t[3] + ";"
    t[0] =Truncate.Truncate(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# DROP DATABASE
def p_instruccion_drop_database1(t):
    '''instruccion : DROP DATABASE ID PUNTO_COMA

    '''
    strGram = "<instruccion> ::= DROP DATABASE ID PUNTO_COMA"
    strSent = "DROP DATABASE " + t[3] + ";"
    t[0] =DropDatabase.DropDatabase(t[3],None,False,0, strGram,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_drop_database2(t):
    '''instruccion : DROP DATABASE IF EXISTS ID PUNTO_COMA

    '''
    strGram = "<instruccion> ::= DROP DATABASE IF EXISTS ID PUNTO_COMA"
    strSent = "DROP DATABASE IF EXISTS " + t[5] + ";"
    t[0] =DropDatabase.DropDatabase(t[5],None,True,1, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# DROP TABLE
def p_instruccion_drop(t):
    '''instruccion : DROP TABLE ID PUNTO_COMA

    '''
    strGram = "<instruccion> ::= DROP TABLE ID PUNTO_COMA"
    strSent = "DROP TABLE " + t[3] + ";"
    t[0] =DropTable.DropTable(t[3],None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_drop2(t):
    '''instruccion : DROP ID

    '''
    strGram = "<instruccion> ::= DROP ID"
    strSent = "DROP " + t[2]
    t[0] =DropTable.DropTable(t[2],None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)


def p_instruccion_where(t):
    '''
        instructionWhere :  WHERE expre
    '''
    strGram = "<instructionWhere> ::=  WHERE <expre>"
    strSent = "WHERE " + t[2].strSent
    t[0] = Where.Where(t[2],None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)


# update tabla set campo = valor , campo 2= valor where condicion

def p_instruccion_update(t):
    '''instruccion : UPDATE ID SET lcol instructionWhere PUNTO_COMA

    '''
    strGram = "<instruccion> ::= UPDATE ID SET <lcol> <instructionWhere> PUNTO_COMA"
    strGram2 = ""
    strSent = "UPDATE " + t[2] + " SET "
    for col in t[4]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + " " + t[5].strSent + ";"

    id1 = Identificador(t[2], strGram2 ,t.lexer.lineno, t.lexer.lexpos, strSent)
    
    

    t[0] = UpdateTable.UpdateTable(id1, None, t[4], t[5], strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)

# update tabla set campo = valor , campo 2= valor;

def p_instruccion_update2(t):
    '''instruccion : UPDATE ID SET lcol PUNTO_COMA

    '''
    strGram = "<instruccion> ::= UPDATE ID SET <lcol> PUNTO_COMA"
    strGram2 = ""
    strSent = "UPDATE " + t[2] + " SET "
    for col in t[4]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ";"
    id1 = Identificador(t[2], strGram2 ,t.lexer.lineno, t.lexer.lexpos, strSent)
    
    

    t[0] = UpdateTable.UpdateTable(id1, None, t[4], None, strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)

# DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
def p_columunas_delete(t):
    '''
     instruccion : DELETE FROM ID instructionWhere PUNTO_COMA
    '''
    strGram = "<instruccion> ::= DELETE FROM ID <instructionWhere> PUNTO_COMA"
    strSent = "DELETE FROM " + t[3] + " " + t[4].strSent + ";"
    t[0] = DeleteTable.DeleteTable(t[3],None, t[4], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)

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
    strGram = "<instruccion> ::= DECLARE <expresion> AS <expresion> PUNTO_COMA"
    strSent = "DECLARE " + t[2].strSent + " AS " + t[4].strSent + ";"
    t[0] = Declare.Declare(t[2], None, t[4], strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_declaracion1(t):
    '''
     instruccion : DECLARE expresion tipo PUNTO_COMA
    '''
    strGram = "<instruccion> ::= DECLARE <expresion> tipo PUNTO_COMA"
    strSent = "DECLARE " + t[2].strSent + " " + t[3].strSent + ";"
    t[0] = Declare.Declare(t[2], t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    
def p_set(t):
    '''
     instruccion : SET expresion IGUAL expre PUNTO_COMA
    '''
    strGram = "<instruccion> ::= SET <expresion> IGUAL <expre> PUNTO_COMA"
    strSent = "SET " + t[2].strSent + " = " + t[4].strSent + ";"
    t[0] =Set.Set(t[2], None, t[4], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)


# ALTER DATABASE name RENAME TO new_name
def p_instruccion_alter_database1(t):
    '''instruccion : ALTER DATABASE ID RENAME TO ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER DATABASE ID RENAME TO ID PUNTO_COMA"
    strSent = "ALTER DATABASE " + t[3] + " RENAME TO " + t[6] + ";"
    t[0] = AlterDatabase.AlterDatabase(t[3], None, t[4], t[6], strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)


# ALTER DATABASE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
def p_instruccion_alter_database2(t):
    '''instruccion : ALTER DATABASE ID OWNER TO list_owner PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER DATABASE ID OWNER TO <list_owner> PUNTO_COMA\n"
    strGram = strGram + "<list_owner> ::= ID| CURRENT_USER| SESSION_USER" 
    strSent = "ALTER DATABASE " + t[3] + " OWNER TO " + t[6] + ";"
    t[0] = AlterDBOwner.AlterDBOwner(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)


# { new_owner | CURRENT_USER | SESSION_USER }
def p_list_owner(t):
    '''list_owner : ID
                | CURRENT_USER
                | SESSION_USER
    '''
    
    t[0] = t[1]

# ALTER TABLE 'NOMBRE_TABLA' ADD COLUMN NOMBRE_COLUMNA TIPO;
def p_instruccion_alter1(t):
    '''instruccion : ALTER TABLE ID l_add_column PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID <l_add_column> PUNTO_COMA\n"
    strGram = strGram + "<l_add_column> ::= <l_add_column> COMA <add_column>\n"
    strGram = strGram + "<l_add_column> ::= <add_column>"
    
    strSent = "ALTER TABLE " + t[3] + " "
    for col in t[4]:
        strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ";"
    print(strSent)
    t[0] = AlterTableAddColumn.AlterTableAddColumn(t[3], t[4], strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_l_add_column1(t):
    '''l_add_column : l_add_column COMA add_column
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_l_add_column2(t):
    '''l_add_column : add_column
    '''
    t[0] = [t[1]]

def p_add_column(t):
    '''add_column : ADD COLUMN ID tipo'''
    strGram = "<add_column> ::= ADD COLUMN ID <tipo>"
    strSent = "ADD COLUMN " + t[3] + " " + t[4].strSent
    t[0] = Columna.Columna(t[3], t[4], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;
def p_instruccion_alter2(t):
    '''instruccion : ALTER TABLE ID l_drop_column PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID <l_drop_column> PUNTO_COMA\n"
    strGram = strGram + "<l_drop_column> ::= <l_drop_column> COMA <drop_column>\n"
    strGram = strGram + "<l_drop_column> ::= <drop_column>"
    
    strSent = "ALTER TABLE " + t[3] + " "
    for col in t[4]:
        strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ";"

    t[0] = AlterTableDropColumn.AlterTableDropColumn(t[3], t[4], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_l_drop_column1(t):
    '''l_drop_column : l_drop_column COMA drop_column'''
    t[1].append(t[3])
    t[0] = t[1]

def p_l_drop_column2(t):
    '''l_drop_column : drop_column'''
    t[0] = [t[1]]

def p_drop_column(t):
    'drop_column : DROP COLUMN ID'
    strGram = "<drop_column> ::= DROP COLUMN ID"
    strSent = "DROP COLUMN " + t[3]
    t[0] = Columna.Columna(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# ALTER TABLE 'NOMBRE_TABLA' ADD CHECK EXP;
def p_instruccion_alter3(t):
    '''instruccion : ALTER TABLE ID ADD CHECK expre PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ADD CHECK <expre> PUNTO_COMA"
    strSent = "ALTER TABLE " + t[3] + " ADD CHECK " + t[6].strSent + ";"
    t[0] = AlterTableAddCheck.AlterTableAddCheck(t[3],t[6], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter4(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ lista_id PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ <lista_id> PARDER PUNTO_COMA"
    
    strSent = "ALTER TABLE " + t[3] + " ADD CONSTRAINT " + t[6] + " UNIQUE ("
    for col in t[9]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ");"
    
    t[0] = AlterTableAddConstraint.AlterTableAddConstraint(t[3], t[6], t[9], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)


def p_instruccion_altercfk(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER PUNTO_COMA"
    
    strSent = "ALTER TABLE " + t[3] + " ADD CONSTRAINT " + t[6] + " FOREIGN KEY ( "
    for col in t[10]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ") REFERENCES " + t[13] + "( "
    for col in t[15]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ");"
    
    t[0] = AlterTableAddConstraintFK.AlterTableAddConstraintFK(t[3], t[6], t[10], t[13], t[15], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# ALTER TABLE child_table ADD FOREIGN KEY (fk_columns) REFERENCES parent_table (parent_key_columns);
def p_instruccion_alter5(t):
    '''instruccion : ALTER TABLE ID ADD FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ADD FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER PUNTO_COMA"
    
    strSent = "ALTER TABLE " + t[3] + " ADD FOREIGN KEY ( "
    for col in t[8]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ") REFERENCES " + t[11] + "( "
    for col in t[13]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ");"

    t[0] = AlterTableAddFK.AlterTableAddFK(t[3], t[8], t[11], t[13], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# ALTER TABLE 'NOMBRE_TABLA' ALTER COLUMN 'NOMBRE' SET NOT NULL;
def p_instruccion_alter6(t):
    '''instruccion : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA"
    strSent = "ALTER TABLE " + t[3] + " ALTER COLUMN " + t[6] + " SET NOT NULL;"
    t[0] = AlterTableAlterColumn.AlterTableAlterColumn(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# ALTER TABLE 'NOMBRE_TABLA' DROP CONSTRAINT 'NOMBRE';
def p_instruccion_alter7(t):
    '''instruccion : ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA"
    strSent = "ALTER TABLE " + t[3] + " DROP CONSTRAINT " + t[6] + ";"
    t[0] = AlterTableDropConstraint.AlterTableDropConstraint(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter8(t):
    '''instruccion : ALTER TABLE ID l_alter PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID <l_alter> PUNTO_COMA"
    
    strSent = "ALTER TABLE " + t[3] + " "
    for col in t[4]:
        strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ";"

    t[0] = AlterTableAlterColumnType.AlterTableAlterColumnType(t[3], t[4], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_l_alter1(t):
    'l_alter : l_alter COMA alter_column'
    t[1].append(t[3])
    t[0] = t[1]

def p_l_alter2(t):
    'l_alter : alter_column'
    t[0] = [t[1]]

def p_alter_column(t):
    'alter_column : ALTER COLUMN ID TYPE tipo'
    strGram = "<alter_column> ::= ALTER COLUMN ID TYPE tipo"
    strSent = "ALTER COLUMN " + t[3] + " TYPE " + t[4].strSent
    t[0] = Columna.Columna(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

# insert into tabla (campo1,campo2,campo3,campo4) values (valor1, valor2, valor3, valor4)
# unicamente validar que tengan los mismos campos y la mismas cantidad de valores

def p_instruccion_insert(t):
    '''instruccion : INSERT INTO ID PARIZQ lista_id PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= INSERT INTO ID PARIZQ <lista_id> PARDER VALUES PARIZQ <l_expresiones> PARDER PUNTO_COMA"
    
    strSent = "INSERT INTO " + t[3] + "("
    for col in t[5]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ") VALUES ("
    for col in t[9]:
        strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ");"

    t[0] = insertTable.insertTable(t[3], None, t[5], t[9], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

#insert into tabla values (valor1,valor2,valor3)
# debe validar que la cantidad de valores coincida con la cantidad de columnas de la tabla y el tipo de dato
def p_instruccion_insert2(t):
    '''
    instruccion : INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= INSERT INTO ID VALUES PARIZQ <l_expresiones> PARDER PUNTO_COMA"
    
    strSent = "INSERT INTO " + t[3] + " VALUES ("
    for col in t[6]:
        strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ");"

    t[0] = insertTable.insertTable(t[3], None, None, t[6], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    
# SELECT col, col FROM id;
# SELECT * from id;
def p_instruccion_query(t):
    '''
    instruccion : lquery PUNTO_COMA
    '''
    t[1].strSent = t[1].strSent + ";"
    t[0]=t[1]

def p_lista_querys(t):
    '''lquery : lquery relaciones query
    '''
    strGram = "<lquery> ::= <lquery> <relaciones> <query>"   
    strSent = t[1].strSent + " " +  t[2] + " " + t[3].strSent
    t[0] = Relaciones.Relaciones(t[1],t[2],t[3],strGram,t.lexer.lineno, t.lexer.lexpos, strSent)

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
        t[0] = "UNION"
    elif(t[1]=="INTERSECT"):
        t[0] = "INTERSECT"
    elif(t[1]=="EXCEPT"):
        t[0] = "EXCEPT"
    else:
        t[0] = None

def p_tipo_relaciones2(t):
    '''relaciones : UNION ALL 
                | INTERSECT ALL 
                | EXCEPT ALL 
    '''
    if(t[1]=="UNION"):
        t[0] = "UNIONALL"
    elif(t[1]=="INTERSECT"):
        t[0] = "INTERSECTALL"
    elif(t[1]=="EXCEPT"):
        t[0] = "EXCEPTALL"
    else:
        t[0] = None

def p_instruccion_select(t):
    '''
    query : SELECT dist lcol FROM lcol
    '''
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol>"
    strGram2 = ""

    strSent = "SELECT " + t[2] + " "
    for col in t[3]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + " FROM "
    for col in t[5]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]

    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, None, None, strGram ,t.lexer.lineno, t.lexer.lexpos, strSent))
    
    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos,strSent)

def p_instruccion_select1(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <instructionWhere> <lrows>"
    strGram2 = ""
    val = []
    
    strSent = "SELECT " + t[2] 
    for col in t[3]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + " FROM "
    for col in t[5]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + " " + t[6].strSent
    for col in t[7]:
        strSent = strSent + " " + col.strSent

    val.append(Select.Select(t[2], t[3], t[5], None, t[6], t[7], strGram ,t.lexer.lineno, t.lexer.lexpos, strSent))
    
    t[0] = SelectLista.SelectLista(val, strGram2 ,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_select2(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <instructionWhere>"
    strGram2 = ""
    val = []
    strSent = "SELECT " + t[2]
    for col in t[3]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + " FROM "
    for col in t[5]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + " " + t[6].strSent

    val.append(Select.Select(t[2], t[3], t[5], None, t[6], None, strGram,t.lexer.lineno, t.lexer.lexpos, strSent))

    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_select3(t):
    '''
    query : SELECT dist lcol FROM lcol linners 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <linners>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], None, None, strGram,t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2 , t.lexer.lineno, t.lexer.lexpos,"")


def p_instruccion_select4(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <linners> <instructionWhere> <lrows>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], t[7], t[8], strGram, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos,"")

def p_instruccion_select5(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <linners> <instructionWhere>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], t[7], None, strGram, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos,"")

def p_instruccion_select6(t):
    '''
    query : SELECT dist lcol 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol>"
    
    strSent = "SELECT " + t[2]
    for col in t[3]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]

    t[0] = SelectLista.SelectLista(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)


def p_instruccion_select7(t):
    '''
    query   : SELECT dist lcol FROM lcol lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <lrows>"
    strGram2 = ""
    val = []
    strSent = "SELECT " + t[2]
    for col in t[3]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + " FROM "
    for col in t[5]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    for col in t[7]:
        strSent = strSent + " " + col.strSent

    val.append(Select.Select(t[2], t[3], t[5], None, None, t[6], strGram, t.lexer.lineno, t.lexer.lexpos, strSent))


    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_lista_case(t):
    '''lcase : lcase case
    '''
    t[0] = t[1].append(t[2])

def p_lista_case_case(t):
    '''lcase : case
    '''
    t[0] = t[1]


def p_instruccion_case(t):
    '''
    case    : WHEN expre THEN expre
            | ELSE expre
    '''

def p_instruccion_lrows(t):
    '''lrows : lrows rows
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_instruccion_lrows2(t):
    '''lrows : rows
    '''
    t[0] = [t[1]]

def p_dist(t):
    '''dist : DISTINCT
    '''
    t[0] = t[1]

def p_dist1(t):
    '''dist : 
    '''
    t[0] = ""

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
    if(t[1] == "ORDER"):
        strGram = "<rows> ::= ORDER BY <l_expresiones>"
        
        strSent = "ORDER BY "
        for col in t[3]:
            strSent = strSent + col.strSent + ","
        strSent = strSent[:-1]
        
        if t[4]:
            if t[4] == "DESC":
                strGram = strGram + " DESC"
                strSent = strSent + " DESC"
            elif t[4] == "ASC":
                strGram = strGram + " ASC"
                strSent = strSent + " ASC"
            else:
                if t[5]:
                    if t[5] == "FIRST":
                        strGram = strGram + " FIRST"
                        strSent = strSent + " NULLS FIRST"
                    else:
                        strGram = strGram + " LAST"
                        strSent = strSent + " NULLS LAST"


        t[0] = OrderBy.OrderBy(t[3], t[4], strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
    elif(t[1] == "GROUP"):
        strGram = "<rows> ::= GROUP BY <l_expresiones>"
        strSent = "GROUP BY "
        for col in t[3]:
            strSent = strSent + col.strSent + ","
        strSent = strSent[:-1]

        t[0] = GroupBy.GroupBy(t[3], None, strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
    elif(t[1] == "HAVING"):
        strGram = "<rows> ::= HAVING <lcol>"
        
        strSent = "HAVING "
        for col in t[2]:
            if isinstance(col, str):
                strSent = strSent + col + ","
            else:
                strSent = strSent + col.strSent + ","
        strSent = strSent[:-1]
        
        t[0] = Having.Having(t[2], None, t.lexer.lineno, t.lexer.lexpos, strSent)   
    elif(t[1] == "LIMIT"):
        #LIMIT(LIMITE,None,fila,columna)
        strGram = "<rows> ::= LIMIT ENTERO"
        strSent = "LIMIT " + str(t[2])
        t[0] = Limit.Limit(t[2], None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_row2(t):
    '''rows : LIMIT ENTERO OFFSET ENTERO'''
    #LIMIT(LIMITE,FILAS_A_EXCLUIR,fila,columna)
    strGram = "<rows> ::= LIMIT ENTERO OFFSET ENTERO"
    strSent = "LIMIT " + str(t[2]) + " OFFSET " + str(t[4])
    t[0] = Limit.Limit(t[2], t[4], strGram, t.lexer.lineno, t.lexer.lexpos, strSent) 


def p_linner_join(t):
    '''linners : linners inners
    '''
    t[0] = t[1].append(t[2])

def p_linner_join2(t):
    '''linners : inners
    '''
    t[0] = [t[1]]

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
    strGram = ""
    strSent = ""
    if t[2] == "OR":
        strGram = "<expre> ::= <expre> OR <expre>"
        strSent = t[1].strSent + " OR " + t[3].strSent
    elif t[2] == "AND":
        strGram = "<expre> ::= <expre> AND <expre>"
        strSent = t[1].strSent + " AND " + t[3].strSent

    t[0] = Logica.Logica(t[1], t[3], t[2].upper(), strGram, t.lexer.lineno, t.lexer.lexpos, strSent)


def p_operadores_unarios(t):
    ''' expre : NOT expre
    '''
    strGram = "<expre> ::= NOT <expre>"
    strSent = "NOT " + t[2].strSent
    t[0] = Logica.Logica(t[2], None, 'NOT', strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_operadores_relacionales(t):
    ''' expre : expre IGUAL expre
            | expre MAYORQ expre
            | expre MENORQ expre
            | expre MAYOR_IGUALQ expre
            | expre MENOR_IGUALQ expre
            | expre DISTINTO expre
    '''
    strGram = ""
    strSent = ""
    if t[2] == "=":
        strGram = "<expre> ::= <expre> IGUAL <expre>"
        strSent = t[1].strSent + " = " + t[3].strSent
    elif t[2] == ">":
        strGram = "<expre> ::= <expre> MAYORQ <expre>"
        strSent = t[1].strSent + " > " + t[3].strSent
    elif t[2] == "<":
        strGram = "<expre> ::= <expre> MENORQ <expre>"
        strSent = t[1].strSent + " < " + t[3].strSent
    elif t[2] == ">=":
        strGram = "<expre> ::= <expre> MAYOR_IGUALQ <expre>"
        strSent = t[1].strSent + " >= " + t[3].strSent
    elif t[2] == "<=":
        strGram = "<expre> ::= <expre> MENOR_IGUALQ <expre>"
        strSent = t[1].strSent + " <= " + t[3].strSent
    elif t[2] == "<>":
        strGram = "<expre> ::= <expre> DISTINTO <expre>"
        strSent = t[1].strSent + " <> " + t[3].strSent

    t[0] = Relacional.Relacional(t[1], t[3], t[2],strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_operadores_aritmeticos(t):
    '''expre : expre MAS expre
            | expre MENOS expre
            | expre POR expre
            | expre DIVIDIDO expre
            | expre EXPONENCIACION expre
            | expre MODULO expre
    '''
    
    strGram = ""
    strSent = ""
    if t[2] == "+":
        strGram = "<expre> ::= <expre> MAS <expre>"
        strSent = t[1].strSent + " + " + t[3].strSent
    elif t[2] == "-":
        strGram = "<expre> ::= <expre> MENOS <expre>"
        strSent = t[1].strSent + " - " + t[3].strSent
    elif t[2] == "*":
        strGram = "<expre> ::= <expre> POR <expre>"
        strSent = t[1].strSent + " * " + t[3].strSent
    elif t[2] == "/":
        strGram = "<expre> ::= <expre> DIVIDIDO <expre>"
        strSent = t[1].strSent + " / " + t[3].strSent
    elif t[2] == "^":
        strGram = "<expre> ::= <expre> EXPONENCIACION <expre>"
        strSent = t[1].strSent + " ^ " + t[3].strSent
    elif t[2] == "%":
        strGram = "<expre> ::= <expre> MODULO <expre>"
        strSent = t[1].strSent + " % " + t[3].strSent

    t[0] = Aritmetica.Aritmetica(t[1], t[3], t[2], strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_operador_unario(t):
    'expre : MENOS expre %prec UMENOS'
    strGram = "<expre> ::= MENOS <expre> %prec UMENOS"
    strSent = "-" + t[2].strSent
    t[0] = Aritmetica.Aritmetica(t[2], None, '-', strGram,t.lexer.lineno, t.lexer.lexpos, strSent)

def p_operadores_like(t):
    '''expre : expre LIKE expre
            | expre NOT LIKE expre
    '''
    strGram = ""
    if t[2] == "NOT":
        strGram = "<expre> ::= <expre> NOT LIKE <expre>"
        strSent = t[1].strSent + " LIKE " + t[3].strSent
        t[0] = Relacional.Relacional(t[1], t[4], "NOT LIKE", strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

    else: 
        strGram = "<expre> ::= <expre> LIKE <expre>"
        strSent = t[1].strSent + " NOT LIKE " + t[3].strSent
        t[0] = Relacional.Relacional(t[1], t[3], "LIKE", strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        
    #t[0] = PatternMatching(t[1], t[3], 'LIKE', t.lexer.lineno, t.lexer.lexpos) if t[2] == 'LIKE' else PatternMatching(t[1], t[3], 'NOT_LIKE', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_between(t):
    '''expre : expre BETWEEN expresion AND expresion
            | expre NOT BETWEEN expresion AND expresion
    '''

    if t[2] == "NOT":
        strGram = "<expre> ::= <expre> NOT BETWEEN <expresion> AND <expresion>"
        strSent = t[0].strSent + " BETWEEN " + t[3].strSent + " AND " + t[5].strSent
        t[0] = Between.Between(t[1], t[4], t[6], "NOT", strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

    else:
        strGram = "<expre> ::= <expre> BETWEEN <expresion> AND <expresion>"
        strSent = t[0].strSent + " NOT BETWEEN " + t[3].strSent + " AND " + t[5].strSent
        t[0] = Between.Between(t[1], t[3], t[5], "", strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

    #t[0] = Between(t[1], t[3], t[5], 'BETWEEN', t.lexer.lineno, t.lexer.lexpos) if t[2] == 'LIKE' else Between(t[1], t[4], t[5], 'NOT_BETWEEN', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_in(t):
    '''expre : expre IN expre
            | expre NOT IN expre
    '''
    strGram = ""
    if t[2] == "NOT":
        strGram = "<expre> ::= <expre> NOT INT <expre>"
        strSent = t[1].strSent + " IN " + t[3].strSent
        t[0] = Relacional.Relacional(t[1], t[4], "NOT IN", strGram, t.lexer.lineno, t.lexer.lexpos,strSent)

    else: 
        strGram = "<expre> ::= <expre> IN <expre>"
        strSent = t[1].strSent + " NOT IN " + t[3].strSent
        t[0] = Relacional.Relacional(t[1], t[3], "IN", strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_operadores_is(t):
    '''expre : expre IS NULL
            | expre IS NOT NULL
            | expre IS DISTINCT FROM expre
            | expre IS NOT DISTINCT FROM expre
    '''
    if t[3] == 'NULL':
        #t[0] = Is(t[1],None,'NULL', t.lexer.lineno, t.lexer.lexpos)
        pass
    if t[3] == 'DISTINCT':
        #t[0] = Is(t[1],t[5],'DISTINCT_FROM', t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[3] == 'NOT' and t[4] == 'NULL':
        #t[0] = Is(t[1],None,'NOT_NULL', t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[3] == 'NOT' and t[4] == 'DISTINCT':
        #t[0] = Is(t[1],t[6],'NOT_DISTINCT', t.lexer.lineno, t.lexer.lexpos)
        pass

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
    if t[1] == 'AVG':
        strGram = "<expre> ::= AVG PARIZQ <expre> PARDER"
        strSent = "AVG (" + t[3].strSent + ")"
        t[0] = Avg.Avg(t[3], Tipo("",Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'COUNT':
        strGram = "<expre> ::= COUNT PARIZQ <expre> PARDER"
        strSent = "COUNT (" + t[3].strSent + ")"
        t[0] = Count.Count(t[3], Tipo("",Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'GREATEST':
        strGram = "<expre> ::= GREATEST PARIZQ <lcol> PARDER"
        strSent = "GREATEST ("
        for col in t[3]:
            if isinstance(col, str):
                strSent = strSent + col + ","
            else:
                strSent = strSent + col.strSent + ","
        strSent = strSent[:-1]
        strSent = strSent + ")"
        t[0] = Greatest.Greatest(t[3], Tipo("",Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'LEAST':
        strGram = "<expre> ::= LEAST PARIZQ <lcol> PARDER"
        strSent = "LEAST ("
        for col in t[3]:
            if isinstance(col, str):
                strSent = strSent + col + ","
            else:
                strSent = strSent + col.strSent + ","
        strSent = strSent[:-1]
        strSent = strSent + ")"
        t[0] = Least.Least(t[3], Tipo("",Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'MAX':
        strGram = "<expre> ::= MAX PARIZQ <expre> PARDER"
        strSent = "MAX (" + t[3].strSent + ")"
        t[0] = Max.Max(t[3], Tipo("",Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'MIN':
        strGram = "<expre> ::= MIN PARIZQ <expre> PARDER"
        strSent = "MIN (" + t[3].strSent + ")"
        t[0] = Min.Min(t[3], Tipo("",Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'SUM':
        strGram = "<expre> ::= MAX PARIZQ <expre> PARDER"
        strSent = "SUM (" + t[3].strSent + ")"
        t[0] = Sum.Sum(t[3], Tipo("",Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'TOP':
        strGram = "<expre> ::= TOP PARIZQ <lcol> PARDER"
        strSent = "TOP ("
        for col in t[3]:
            if isinstance(col, str):
                strSent = strSent + col + ","
            else:
                strSent = strSent + col.strSent + ","
        strSent = strSent[:-1]
        strSent = strSent + ")"
        t[0] = Top.Top(t[3], Tipo("",Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
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
    
    if t[1] == 'ABS':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        strSent = "ABS(" + t[3].strSent + ")"
        t[0] = Abs.Abs(t[3], strGram,t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'CBRT':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        strSent = "CBRT(" + t[3].strSent + ")"
        t[0] = Cbrt.Cbrt(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'CEIL':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        strSent = "CEIL(" + t[3].strSent + ")" 
        t[0] = Ceil.Ceil(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'CEILING':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        strSent = "CEILING(" + t[3].strSent + ")"
        t[0] = Ceiling.Ceiling(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'DEGREES':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        strSent = "DEGREES(" + t[3].strSent + ")"
        t[0] = Degrees.Degrees(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'DIV':
        strGram = "<expre> ::= DIV PARIZQ <expre> COMA <expre>  PARDER"
        strSent = "DIV(" + t[3].strSent + "," + t[5].strSent + ")"
        t[0] = Div.Div(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'EXP':
        strGram = "<expre> ::= EXP PARIZQ <expre> PARDER"
        strSent = "EXP(" + t[3].strSent + ")"
        t[0] = Exp.Exp(t[3], Tipo("",Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'FACTORIAL':
        strGram = "<expre> ::= FACTORIAL PARIZQ <expre> PARDER"
        strSent = "FACTORIAL(" + t[3].strSent + ")"
        t[0] = Factorial.Factorial(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'FLOOR':
        strGram = "<expre> ::= FLOOR PARIZQ <expre> PARDER"
        strSent = "FLOOR(" + t[3].strSent + ")"
        t[0] = Floor.Floor(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'GCD':
        strGram = "<expre> ::= GCD PARIZQ <expre> COMA <expre> PARDER"
        strSent = "GDC(" + t[3].strSent + "," + t[5].strSent + ")"
        t[0] = Gcd.Gcd(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'LCM':
        strGram = "<expre> ::= LCM PARIZQ <expre> PARDER"
        strSent = "LCM(" + t[3].strSent + ")"
        t[0] = Lcm.Lcm(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'LN':
        strGram = "<expre> ::= LN PARIZQ <expre> PARDER"
        strSent = "LN(" + t[3].strSent + ")"
        t[0] = Ln.Ln(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'LOG':
        strGram = "<expre> ::= LOG PARIZQ <expre> PARDER"
        strSent = "LOG(" + t[3].strSent + ")"
        t[0] = Log.Log(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'LOG10':
        strGram = "<expre> ::= LOG10 PARIZQ <expre> PARDER"
        strSent = "LOG10(" + t[3].strSent + ")"
        t[0] = Log10.Log10(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'MIN_SCALE':
        strGram = "<expre> ::= MIN_SCALE PARIZQ <expre> PARDER"
        strSent = "MIN_SCALE(" + t[3].strSent + ")"
        t[0] = MinScale.MinScale(t[3], t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'MOD':
        strGram = "<expre> ::= MOD PARIZQ <expre> COMA <expre> PARDER"
        strSent = "MOD(" + t[3].strSent + "," + t[5].strSent + ")"
        t[0] = Mod.Mod(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'PI':
        strGram = "PI PARIZQ PARDER "
        strSent = "PI()"
        t[0] = PI.PI(strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'POWER':
        strGram = "<expre> ::= POWER PARIZQ <expre> COMA <expre> PARDER"
        strSent = "POWER(" + t[3].strSent + "," + t[5].strSent + ")"
        t[0] = Power.Power(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'RADIANS':
        strGram = "<expre> ::= RADIANS PARIZQ <expre> PARDER "
        strSent = "RADIANS(" + t[3].strSent + ")"
        t[0] = Radians.Radians(t[3], strGram ,t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'RANDOM':
        strGram = "RANDOM PARIZQ PARDER"
        strSent = "RANDOM()"
        t[0] = Random.Random(strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'ROUND':
        strGram = "<expre> ::= ROUND PARIZQ <expre> PARDER "
        strSent = "ROUND(" + t[3].strSent + ")"
        t[0] = Round.Round(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'SCALE':
        strGram = "<expre> ::= SCALE PARIZQ <expre> PARDER "
        strSent = "SCALE(" + t[3].strSent + ")"
        t[0] = Scale.Scale(t[3], strGram ,t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'SETSEED':
        strGram = "<expre> ::= SETSEED PARIZQ <expre> PARDER"
        strSent = "SETSEED(" + t[3].strSent + ")"
        t[0] = SetSeed.SetSeed(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'SIGN':
        strGram = "<expre> ::= SIGN PARIZQ <expre> PARDER"
        strSent = "SIGN(" + t[3].strSent + ")"
        t[0] = Sign.Sign(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'SQRT':
        strGram = "<expre> ::= SQRT PARIZQ <expre> PARDER"
        strSent = "SQRT(" + t[3].strSent + ")"
        t[0] = Sqrt.Sqrt(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'TRIM_SCALE':
        strGram = "<expre> ::= TRIM_SCALE PARIZQ <expre> PARDER"
        strSent = "TRIM_SCALE(" + t[3].strSent + ")"
        t[0] = TrimScale.TrimScale(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'TRUNC':
        strGram = "<expre> ::= TRUNC PARIZQ <expre> PARDER"
        strSent = "TRUNC(" + t[3].strSent + ")"
        t[0] = Trunc.Trunc(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'WIDTH_BUCKET':
        strGram = "<expre> ::= WIDTH_BUCKET PARIZQ <expresion> COMA <expresion> COMA <expresion> COMA <expresion> PARDER "
        strSent = "WIDTH_BUCKET(" + t[3].strSent + "," + t[5].strSent + "," + t[7].strSent + "," + t[9].strSent + ")"
        t[0] = WidthBucket.WidthBucket(t[3], t[5], t[7], t[9], Tipo("",Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

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

    if t[1] == 'CONVERT':
        strGram = "<expre> ::= CONVERT PARIZQ <expre> AS <tipo> PARDER"
        strSent = "CONVERT(" + t[3].strSent + " AS " + t[5].strSent + ")"
        t[0] = Convert.Convert(t[3], None, t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'DECODE':
        strGram = "<expre> ::= DECODE PARIZQ <expre> PARDER"
        strSent = "DECODE(" + t[3].strSent + ")"
        t[0] = Decode.Decode(t[3],  None, t[5],strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'ENCODE':
        strGram = "<expre> ::= ENCODE PARIZQ <expre> PARDER"
        strSent = "ENCODE(" + t[3].strSent + ")"
        t[0] = Encode.Encode(t[3],  None, t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'GET_BYTE':
        strGram = "<expre> ::= GET_BYTE PARIZQ <expre> COMA ENTERO PARDER"
        strSent = "GET_BYTE(" + t[3].strSent + "," + str(t[5]) + ")"
        t[0] = GetByte.GetByte(t[3], None,t[5], strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'LENGTH':
        strGram = "<expre> ::= LENGTH PARIZQ <expre> PARDER"
        strSent = "LENGTH(" + t[3].strSent + ")"
        t[0] = Length.Length(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'MD5':
        strGram = "<expre> ::= MD5 PARIZQ <expre> PARDER"
        strSent = "MD5(" + t[3].strSent + ")"
        t[0] = Md5.Md5(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'SET_BYTE':
        strGram = "<expre> ::= SET_BYTE PARIZQ <expre> COMA ENTERO COMA ENTERO PARDER"
        strSent = "SET_BYTE(" + t[3].strSent + "," + str(t[5]) + "," + str(t[7]) +")"
        t[0] = SetByte.SetByte(t[3], None, t[5], t[7], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'SHA256':
        strGram = "<expre> ::= SHA256 PARIZQ <expre> PARDER"
        strSent = "SHA256(" + t[3].strSent + ")"
        t[0] = Sha256.Sha256(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass
    elif t[1] == 'SUBSTR':
        strGram = "<expre> ::= SUBSTR PARIZQ <expre> COMA ENTERO COMA ENTERO PARDER"
        strSent = "SUBSTR(" + t[3].strSent + "," + str(t[5]) + "," + str(t[7]) +")"
        t[0] = Substring.Substring(t[3], t[5], t[7], None, strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
        pass
    elif t[1] == 'SUBSTRING':
        strGram = "<expre> ::= SUBSTRING PARIZQ <expre> COMA ENTERO COMA ENTERO PARDER"
        strSent = "SUBSTRING(" + t[3].strSent + "," + str(t[5]) + "," + str(t[7]) +")"
        t[0] = Substring.Substring(t[3], t[5], t[7], None, strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
        pass
    elif t[1] == 'TRIM':
        strGram = "<expre> ::= TRIM PARIZQ <expre> PARDER"
        strSent = "TRIM(" + t[3].strSent + ")"
        t[0] = Trim.Trim(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
        pass

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
    strGram = "<expre> ::= "+ t[1] +" PARIZQ <expre> PARDER"
    strSent = t[1] + "(" + t[3].strSent + ")"
    if t[1] == 'ACOS':
        t[0] = Acos.Acos(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'ACOSD':
        t[0] = Acosd.Acosd(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'ACOSH':
        t[0] = Acosh.Acosh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    elif t[1] == 'ASIN':
        t[0] = Asin.Asinh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'ASIND':
        t[0] = Asind.Asind(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'ASINH':
        t[0] = Asinh.Asinh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'ATAN':
        
        t[0] = Atan.Atan(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'ATAN2':
        strGram = "<expre> ::= ATAN2 PARIZQ <expre> COMA <expre> PARDER"
        strSent = t[1] + "(" + t[3].strSent + "," + t[5].strSent + ")"
        t[0] = Atan2.Atan2(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'ATAN2D':
        strGram = "<expre> ::= ATAN2D PARIZQ <expre> COMA <expre> PARDER"
        strSent = t[1] + "(" + t[3].strSent + "," + t[5].strSent + ")"
        t[0] = Atan2d.Atan2d(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'ATAND':
        t[0] = Atand.Atand(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'ATANH':
        t[0] = Atanh.Atanh(t[3], strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'COS':
        t[0] = Cos.Cos(t[3], strGram,t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'COSD':
        t[0] = Cosd.Cosd(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'COSH':
        t[0] = Cosh.Cosh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'COT':
        t[0] = Cot.Cot(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'COTD':
        t[0] = Cotd.Cotd(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'SIN':
        t[0] = Sin.Sin(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'SIND':
        t[0] = Sind.Sind(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'SINH':
        t[0] = Sinh.Sinh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'TAN':
        t[0] = Tan.Tan(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'TAND':
        t[0] = Tand.Tand(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'TANH':
        t[0] = Tanh.Tanh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
            
def p_cadena_o_caracter(t):
    '''
    cadena_o_caracter   : CADENA
                        | CARACTER
    '''
    t[0] = t[1]

def p_operadores_otros(t):
    ''' expre : EXTRACT PARIZQ tiempo FROM TIMESTAMP cadena_o_caracter PARDER
            | NOW PARIZQ PARDER
            | DATE_PART PARIZQ cadena_o_caracter COMA INTERVAL cadena_o_caracter PARDER
            | CURRENT_DATE
            | CURRENT_TIME
            | TIMESTAMP cadena_o_caracter
            | CASE lcase END 
    '''
    if t[1] == 'EXTRACT':
        strGram = "<expre> ::= EXTRACT PARIZQ <tiempo> FROM TIMESTAMP CARACTER PARDER"
        strSent = "EXTRACT(" + t[3] + " FROM TIMESTAMP " + t[6] + ")"
        t[0] = Extract.Extract(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'NOW':
        strGram = "<expre> ::= NOW PARIZQ PARDER"
        strSent = "NOW()"
        t[0] = Now.Now( strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'DATE_PART':
        strGram = "<expre> ::= DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER"
        strSent = "DATE_PART(" + t[3] + "," + t[5] + " " + t[6] + ")"
        t[0] = DatePart.DatePart(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'CURRENT_DATE':
        strGram = "<expre> ::= CURRENT_DATE"
        strSent = "CURRENT_DATE"
        t[0] = CurrentDate.CurrentDate(strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'CURRENT_TIME':
        strGram = "<expre> ::= CURRENT_TIME"
        strSent = "CURRENT_TIME"
        t[0] = CurrentTime.CurrentTime(strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'TIMESTAMP':
        strGram = "<expre> ::= TIMESTAMP CARACTER"
        strSent = "TIMESTAMP " + t[2]
        t[0] = TimeStamp.TimeStamp(t[2], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)
    elif t[1] == 'POR':
        t[0] = 'Pendiente'
    elif t[1] == 'CASE':
        strGram = "<expre> ::= CASE <lcase> END "
        t[0] = Case.Case(t[2], strGram, t.lexer.lineno, t.lexer.lexpos, strSent, "")

def p_operadores_parentesis(t):
    ''' expre : PARIZQ expre PARDER
    '''
    t[2].strSent = "(" + t[2].strSent + ")"
    t[0] = t[2]

def p_operadores_parentesis1(t):
    ''' expre : PARIZQ query PARDER
    '''
    t[0] = t[2]

 
def p_operadores_logicos5(t):
    ''' expre :  expresion
    '''
    #print("entro a expre - expresion")
    t[0] = t[1]

def p_tiempo1(t):
    ''' tiempo :  YEAR
    '''
    t[0] = "YEAR"

def p_tiempo2(t):
    ''' tiempo :  MONTH
    '''
    t[0] = "MONTH"

def p_tiempo3(t):
    ''' tiempo :  DAY
    '''
    t[0] = "DAY"

def p_tiempo4(t):
    ''' tiempo :  HOUR
    '''
    t[0] = "HOUR"

def p_tiempo5(t):
    ''' tiempo :  MINUTE
    '''
    t[0] = "MINUTE"

def p_tiempo6(t):
    ''' tiempo :  SECOND
    '''
    t[0] = "SECOND"

def p_campos_tablas(t):
    '''campos : campos COMA ID tipo lista_op
    '''
    #ESTOY HACIENDO ESTA
    strGram = "<campos> ::= <campos> COMA ID <tipo> <lista_op>"
    
    strSent = t[3] + " " + t[4].strSent
    for col in t[5]:
        strSent = strSent + " " + col.strSent
    
    t[1].append(CColumna.Columna(t[3],t[4],t[5], strGram, t.lineno,t.lexpos,strSent))
    t[0] =t[1]

def p_campos_tablas1(t):
    '''campos : campos COMA ID tipo
    '''
    strGram = "<campos> ::= <campos> COMA ID tipo"
    strSent = t[3] + " " + t[4].strSent
    t[1].append(CColumna.Columna(t[3],t[4],None,strGram,t.lineno,t.lexpos, strSent))
    t[0] =t[1]

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
    strGram = "<campos> ::= <campos> COMA UNIQUE PARIZQ <lista_id> PARDER"
    
    strSent = "UNIQUE("
    for col in t[5]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ")"

    t[1].append(Tipo_Constraint(None,Tipo_Dato_Constraint.UNIQUE,t[5],strSent))
    t[0] = t[1]

def p_campos_tablas5(t):
    '''campos : campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
    '''
    strGram = "<campos> ::= <campos> COMA FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER"
    
    strSent = "FOREIGN KEY("
    for col in t[6]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ") REFERENCES " + t[9] + "("
    for col in t[11]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ")"

    t[1].append(Tipo_Constraint(t[6],Tipo_Dato_Constraint.FOREIGN_KEY,Tipo_Constraint([9],Tipo_Dato_Constraint.REFERENCES,t[11]),strSent))
    t[0] = t[1]

def p_campos_tablas6(t):
    '''campos : campos COMA PRIMARY KEY PARIZQ lista_id PARDER
    '''
    strSent = "PRIMARY KEY("
    for col in t[6]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ")"

    t[1].append(Tipo_Constraint(None,Tipo_Dato_Constraint.PRIMARY_KEY,t[6],strSent))
    t[0] = t[1]

def p_campos_tablas7(t):
    '''campos : ID tipo lista_op
    '''
    strGram = "<campos> ::= ID <tipo> <lista_op>"
    strSent = t[1] + " " + t[2].strSent
    for col in t[3]:
        strSent = strSent + " " + col.strSent
    
    t[0] = [CColumna.Columna(t[1],t[2],t[3], strGram, t.lineno,t.lexpos, strSent)]

def p_campos_tablas8(t):
    '''campos : ID tipo
    '''
    strGram = "<campos> ::= ID <tipo>"
    strSent = t[1] + " " + t[2].strSent
    t[0] = [CColumna.Columna(t[1],t[2],None,strGram,t.lineno,t.lexpos,strSent)]

def p_lista_id1(t):
    '''lista_id : lista_id COMA ID
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_id2(t):
    '''lista_id : ID
    '''
    t[0] = [t[1]]


def p_lista_op1(t):
    '''lista_op : lista_op opcion
    '''
    t[1].append(t[2])
    t[0] = t[1]


def p_lista_op2(t):
    '''lista_op : opcion
    '''
    t[0] = [t[1]]

def p_opcion(t):
    '''opcion : PRIMARY KEY
    '''
    strSent = "PRIMARY KEY"
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.PRIMARY_KEY, None, strSent)

def p_opcion1(t):
    '''opcion : REFERENCES ID PARIZQ lista_id PARDER
    '''
    strSent = "REFERENCES " + t[2] + "("
    for col in t[4]:
        strSent = strSent + col + ","
    strSent = strSent[:-1]
    strSent = strSent + ")"

    t[0] = Tipo_Constraint(t[2], Tipo_Dato_Constraint.REFERENCES, t[4],strSent)

def p_opcion2(t):
    '''opcion : DEFAULT expresion
    '''
    strSent = "DEFAULT " + t[2].strSent
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.DEFAULT, t[2],strSent)

def p_opcion3(t):
    '''opcion : NOT NULL
    '''
    strSent = "NOT NULL"
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.NOT_NULL, None, strSent)

def p_opcion4(t):
    '''opcion : NULL
    '''
    strSent = "NULL"
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.NULL, None, strSent)

def p_opcion5(t):
    '''opcion : UNIQUE
    '''
    strSent = "UNIQUE"
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.UNIQUE, None, strSent)

def p_opcion6(t):
    '''opcion : CONSTRAINT ID UNIQUE
    '''
    strSent = "CONSTRAINT " + t[2] + " UNIQUE"
    t[0] = Tipo_Constraint(t[2], Tipo_Dato_Constraint.UNIQUE, None, strSent)

def p_opcion7(t):
    '''opcion : CONSTRAINT ID CHECK expre
    '''
    strSent = "CONSTRAINT " + t[2] + " CHECK " + t[4].strSent
    t[0] = Tipo_Constraint(t[2], Tipo_Dato_Constraint.CHECK, t[4], strSent)

def p_opcion8(t):
    '''opcion : CHECK expre
    '''
    strSent = "CHECK " + t[2].strSent
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.CHECK, t[2], strSent)

def p_lista_expresiones(t):
    '''
    l_expresiones : l_expresiones COMA expre
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_expresiones1(t):
    '''
    l_expresiones : expre
    '''
    t[0] = [t[1]]

def p_expresion(t):
    '''
    expresion : CADENA
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= CADENA"
    strSent = t[1]
    t[0] = Primitivo.Primitivo(t[1],Tipo("",Tipo_Dato.TEXT), strGram, t.lexer.lineno, t.lexer.lexpos,strSent)

def p_expresion1(t):
    '''expresion : CARACTER
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= CARACTER"
    strSent = t[1]
    t[0] = Primitivo.Primitivo(t[1],Tipo("",Tipo_Dato.CHAR), strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    

def p_expresion2(t):
    '''expresion : ENTERO
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ENTERO"
    strSent = str(t[1])
    t[0] = Primitivo.Primitivo(t[1], Tipo("",Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos,strSent)
    
def p_expresion3(t):
    '''expresion : FDECIMAL
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= FDECIMAL"
    strSent = str(t[1])
    t[0] = Primitivo.Primitivo(t[1],Tipo("",Tipo_Dato.NUMERIC), strGram, t.lexer.lineno, t.lexer.lexpos,strSent)

def p_expresion4(t):
    '''expresion : DOUBLE
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram +"<expresion> ::= DOUBLE"
    strSent = str(t[1])
    t[0] = Primitivo.Primitivo(t[1],Tipo("",Tipo_Dato.DOUBLE_PRECISION), strGram, t.lexer.lineno, t.lexer.lexpos,strSent)

def p_expresion5(t):
    '''expresion : ID
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ID"
    #t[0] = Primitivo.Primitivo(t[1],Tipo_Dato.ID, t.lexer.lineno, t.lexer.lexpos)
    strSent = t[1]
    t[0] = Identificador(t[1], strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_expresion61(t):
    '''expresion : ID PUNTO ID
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ID PUNTO ID"
    strSent = t[1] + "." + t[3]
    t[0] = SelectLista.Alias(t[1],t[3],strSent)
    #t[0] = Primitivo.Primitivo(f"{t[1]}.{t[3]}",Tipo_Dato.ID, strGram,t.lexer.lineno, t.lexer.lexpos)

def p_expresion62(t):
    '''expresion : ID PUNTO POR
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ID PUNTO POR"
    strSent = t[1] + ".*"
    t[0] = SelectLista.Alias(t[1],t[3],strSent)
    #t[0] = Primitivo.Primitivo(f"{t[1]}.{t[3]}",Tipo_Dato.ID, strGram, t.lexer.lineno, t.lexer.lexpos)


def p_expresion7(t):
    '''expresion : ARROBA ID
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ARROBA ID"
    strSent = "@" + t[2]
    t[0] = Primitivo.Primitivo(t[1],Tipo_Dato.ARROBA, strGram, t.lexer.lineno, t.lexer.lexpos,strSent)

def p_expresion8(t):
    '''expresion : ID PARIZQ lcol PARDER
    '''
    strGram = "<expresion> ::= ID PARIZQ <lcol> PARDER\n"
    strSent = t[1] + "("
    for col in t[3]:
        if isinstance(col, str):
            strSent = strSent + col + ","
        else:
            strSent = strSent + col.strSent + ","
    strSent = strSent[:-1]
    strSent = strSent + ")"
    t[0] = LlamadoFuncion.LlamadoFuncion(strGram, t.lexer.lineno, t.lexer.lexpos, strSent)

def p_expresion9(t):
    '''expresion : TRUE
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= TRUE"
    strSent = "TRUE"
    t[0] = Primitivo.Primitivo(True,Tipo("",Tipo_Dato.BOOLEAN), strGram, t.lexer.lineno, t.lexer.lexpos,strSent)

def p_expresion10(t):
    '''expresion : FALSE
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= FALSE"
    strSent = "FALSE"
    t[0] = Primitivo.Primitivo(False,Tipo("",Tipo_Dato.BOOLEAN), strGram, t.lexer.lineno, t.lexer.lexpos,strSent)

def p_lista_columas(t):
    '''lcol : lcol COMA expre
    '''
    #print("entro aqui 1")
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_columas1(t):
    '''lcol : lcol COMA expre nombre
    '''
    t[1].append(SelectLista.Alias(t[4],t[3], t[3].strSent + " " + t[4]))
    t[0] = t[1]

def p_lista_columas2(t):
    '''lcol : lcol COMA expre AS nombre
    '''
    t[1].append(SelectLista.Alias(t[5],t[3], t[3].strSent + " AS " + t[5]))
    t[0] = t[1]


def p_lista_columas01(t):
    '''lcol : POR
    '''
    t[0] = t[1]

def p_lista_columas3(t):
    '''lcol : expre
    '''
    t[0] = [t[1]]
    
def p_lista_columas4(t):
    '''lcol : expre nombre
    '''
    t[0] = [SelectLista.Alias(t[2],t[1], t[1].strSent + " " + t[2])]

def p_lista_columas5(t):
    '''lcol : expre AS nombre
    '''
    t[0] = [SelectLista.Alias(t[3],t[1], t[1].strSent + " AS " + t[3])]

def p_nombre(t):
    '''nombre : ID
        | CADENA
        | CARACTER
    '''
    t[0] = t[1]

#----------------------TIPO DE DATOS---------------------------------
def p_tipo_datos(t):
    '''tipo : INT
    '''
    strSent = t[1]
    t[0] = Tipo(strSent, Tipo_Dato.INTEGER)

def p_tipo_datos1(t):
    '''tipo : DATE
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.DATE)

# NO RECUERDO PARA QUE IMPLEMENTAMOS ESTA PARTE ENTONCES LA COMENTE
#def p_tipo_datos2(t):
#    '''tipo : ID PARIZQ ID PARDER
#    '''
#    t[0]=t[1]

def p_tipo_datos_varchar(t):
    '''tipo : VARCHAR PARIZQ ENTERO PARDER
    '''
    strSent = "VARCHAR(" + str(t[3]) + ")"
    t[0] = Tipo(strSent, Tipo_Dato.VARCHAR,t[3])

def p_tipo_datos_varchar1(t):
    '''tipo : CHAR PARIZQ ENTERO PARDER
    '''
    strSent = "CHAR(" + str(t[3]) + ")"
    t[0] = Tipo(strSent, Tipo_Dato.CHAR,t[3])

def p_tipo_datos_varchar2(t):
    '''tipo : CHARACTER VARYING PARIZQ ENTERO PARDER
    '''
    strSent = "CHARACTER VARYING(" + str(t[4]) + ")"
    t[0]= Tipo(strSent, Tipo_Dato.VARYING,t[4])

def p_tipo_datos_varchar3(t):
    '''tipo : CHARACTER PARIZQ ENTERO PARDER
    '''
    strSent = "CHARACTER(" + str(t[3]) + ")"
    t[0]= Tipo(strSent, Tipo_Dato.CHARACTER,t[3])

def p_tipo_datos_varchar4(t):
    '''tipo : TEXT
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.TEXT)

#ESTE NO SE CONTEMPLO EN LA GRAMATICA DE MAEDA
def p_tipo_datos_decimal(t):
    '''tipo : DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
    '''
    strSent = "DECIMAL(" + str(t[3]) + "," + str(t[5]) + ")"
    t[0]= Tipo(strSent, Tipo_Dato.DECIMAL,[t[3],t[5]])

#def p_tipo_datos_decimal1(t):
#    '''tipo : DOUBLE
#    '''
#    t[0] = Tipo("",Tipo_Dato.DOUBLE_PRECISION)
    
def p_tipo_datos_decimal2(t):
    '''tipo : DECIMAL
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.DECIMAL)

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
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.SMALLINT)

def p_tipo_datos_int2(t):
    '''tipo : INTEGER
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.INTEGER)

def p_tipo_datos_int3(t):
    '''tipo : BIGINT
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.BIGINT)

def p_tipo_datos_int4(t):
    '''tipo : NUMERIC
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.NUMERIC)

def p_tipo_datos_int5(t):
    '''tipo : REAL
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.REAL)

def p_tipo_datos_int6(t):
    '''tipo : DOUBLE PRECISION
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.DOUBLE_PRECISION)

def p_tipo_datos_int7(t):
    '''tipo : MONEY
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.MONEY)

def p_tipo_datos_int8(t):
    '''tipo : BOOLEAN
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.BOOLEAN)

def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.TIMESTAMP)

def p_tipo_datos_date1(t):
    '''tipo : TIME
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.TIME)

def p_tipo_datos_date2(t):
    '''tipo : INTERVAL
    '''
    strSent = t[1]
    t[0]=Tipo(strSent, Tipo_Dato.INTERVAL)

def p_tipo_datos2(t):
    '''tipo : ID 
    '''
    strSent = t[1]
    t[0] = Tipo(strSent, Tipo_Dato.TIPOENUM)
    t[0].nombre = t[1]






########################################### GRAMATICA FASE 2 ########################################

def p_exect_func_pro(t):
    '''
    instruccion     :   EXECUTE ID PARIZQ l_expresiones PARDER PUNTO_COMA 
    '''
    t[0] = Execute.Execute(t[2], t[4],"", t.lexer.lineno, t.lexer.lexpos, "")


def p_procedimiento(t):
    '''
    instruccion     :   CREATE PROCEDURE ID PARIZQ parametros_funcion PARDER LANGUAGE PLPGSQL AS DOLLAR DOLLAR declaraciones_funcion BEGIN contenido_funcion END PUNTO_COMA DOLLAR DOLLAR
    '''
    t[0] = Procedimiento.Procedimiento(t[3], t[5], t[12], t[14], "", t.lexer.lineno, t.lexer.lexpos,"")


#DECLARACION DE UNA FUNCION
def p_funciones(t):
    '''
    instruccion    :   CREATE FUNCTION ID PARIZQ parametros_funcion PARDER returns_n retorno_funcion declaraciones_funcion BEGIN contenido_funcion END PUNTO_COMA DOLLAR DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = Funcion.Funcion(t[3], t[5], t[8], t[9], t[11], "", t.lexer.lineno, t.lexer.lexpos, "")

def p_funciones_drop(t):
    '''
    instruccion : DROP FUNCTION if_op ID PUNTO_COMA
    '''
    t[0] = DropFuncion.DropFuncion(t[4], "", t.lexer.lineno, t.lexer.lexpos, "")

def p_procedimientos_drop(t):
    '''
    instruccion : DROP PROCEDURE if_op ID PUNTO_COMA
    '''
    t[0] = DropProcedimiento.DropProcedimiento(t[4], "", t.lexer.lineno, t.lexer.lexpos, "")

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
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_parametros_funcion2(t):
    '''
    lista_parametros_funcion    :   parametro_fucion
    '''
    t[0] = [t[1]]

def p_parametro_fucion(t):
    '''
    parametro_fucion 	: 	ID tipo
					    |	tipo
    '''
    if len(t) == 3:
        t[0] = t[1]
    else:
        t[0] = "$"


def p_returns(t):
    '''
    returns_n 	:	RETURNS 
    '''


def p_returns_e(t):
    '''
    returns_n   :
    '''

def p_retorno_funcion(t):
    '''
    retorno_funcion :   tipo AS DOLLAR DOLLAR
				    |   TABLE PARIZQ lista_campos_tabla PARDER AS DOLLAR DOLLAR
				    |   AS DOLLAR DOLLAR
    '''
    if len(t) == 4:
        t[0] = "NO ESPECIFICADO"
    elif len(t) == 5:
        t[0] = t[1].strSent
    else:
        t[0] = "TABLA"

def p_lista_campos_tabla(t):
    '''
    lista_campos_tabla  :	lista_campos_tabla COMA ID tipo
    '''
    t[1].append(t[3] + " " + t[4].strSent)
    t[0] = t[1]

def p_lista_campos_tabla2(t):
    '''
    lista_campos_tabla  :	ID tipo
    '''
    t[0] = [t[1] + " " + t[2].strSent]

def p_declaraciones_funcion(t):
    '''
    declaraciones_funcion 	: 	DECLARE list_dec_var_funcion
    '''
    t[0] = t[2]

def p_declaraciones_funcion_e(t):
    '''
    declaraciones_funcion   :
    '''    
    t[0] = None

def p_list_dec_var_funcion(t):
    '''
    list_dec_var_funcion 	:	list_dec_var_funcion dec_var_funcion PUNTO_COMA
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_list_dec_var_funcion2(t):
    '''
    list_dec_var_funcion 	:	dec_var_funcion PUNTO_COMA
    '''
    t[0] = [t[1]]

def p_dec_var_funcion(t):
    '''
    dec_var_funcion : 	ID constant_n tipo nnull aisgnacion_valor 
    '''
    t[0] = DeclaracionVariable.DeclaracionVariable(t[1], t[2], t[3], t[4], t[5], "", t.lexer.lineno, t.lexer.lexpos, "")
    
def p_dec_var_funcion2(t):
    '''
    dec_var_funcion : 	ID ALIAS FOR DOLLAR ENTERO
				    |	ID ALIAS FOR ID
    '''

    if len(t) == 5:
        t[0] = DeclaracionAlias.DeclaracionAlias(t[1], t[4], None, "", t.lexer.lineno, t.lexer.lexpos, "")
    else:
        t[0] = DeclaracionAlias.DeclaracionAlias(t[1], None, t[5], "", t.lexer.lineno, t.lexer.lexpos, "")


def p_dec_var_funcion3(t):
    '''
    dec_var_funcion : 	ID tabla_typerow MODULO type_row
    '''



def p_tabla_typerow(t):
    '''
    tabla_typerow   :   ID PUNTO ID
                    |   ID
    '''


def p_type_row(t):
    '''
    type_row 	:	TYPE
			    |	ROWTYPE
    '''


def p_constant(t):
    '''
    constant_n  :   CONSTANT
    '''
    t[0] = t[1]

def p_constant_e(t):
    '''
    constant_n  :   
    '''
    t[0] = None

def p_nnull(t):
    '''
    nnull : NOT NULL
    '''
    t[0] = "NOT NULL"

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
    t[0] = t[2]



def p_aisgnacion_valor_e(t):
    '''
    aisgnacion_valor    :
    '''
    t[0] = None

def p_contenido_funcion(t):
    '''
    contenido_funcion   : contenido_funcion cont_funcion''' 
    t[1].append(t[2])
    t[0] = t[1]

def p_contenido_funcion2(t):
    '''
    contenido_funcion   : cont_funcion '''
    t[0] = [t[1]]
    
    
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
    if len(t) == 3:
        t[0] = DeclaracionRetorno.DeclaracionRetorno(None, "", t.lexer.lineno, t.lexer.lexpos, "")
    else:
        t[0] = DeclaracionRetorno.DeclaracionRetorno(t[2], "", t.lexer.lineno, t.lexer.lexpos, "")

def p_asignacion_var(t):
    '''
    asignacion_var  :   ID IGUAL expre PUNTO_COMA
                    |   ID DOSP_IGUAL expre PUNTO_COMA
    '''
    t[0] = AsignacionVariable.AsignacionVariable(t[1], t[3], "", t.lexer.lineno, t.lexer.lexpos, "")

def p_asignacion_var1(t):
    '''
    asignacion_var  :   ID IGUAL PARIZQ instruccion PARDER PUNTO_COMA
                    |   ID DOSP_IGUAL PARIZQ instruccion PARDER PUNTO_COMA
    '''
    t[0] = AsignacionVariable.AsignacionVariable(t[1], t[4], "", t.lexer.lineno, t.lexer.lexpos, "")

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
    if t[1] == "IF" and len(t) == 11:
        print("Llega")
        t[0] = condicional_if.IfElseIfElse(t[2],t[4],t[5],t[7],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent") 
    elif t[1] == "IF" and  len(t) == 8:
        print("Llega")
        t[0] = condicional_if.If(t[2],t[4],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")
    elif t[1] == "IF" and len(t) == 10:
        print("Llega")
        t[0] = condicional_if.Ifelse(t[2],t[4],t[6],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")
    elif t[1] == "IF" and len(t) == 9:
        t[0] = condicional_if.IfElseIf(t[2],t[4],t[5],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")
    elif t[1] == "CASE" and len(t) == 6:
        t[0] = condicional_case.Case(t[2],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")
    elif t[1] == "CASE" and len(t) == 8:
        t[0] = condicional_case.CaseElse(t[2],t[4],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")
    elif t[1] == "CASE" and len(t) == 7:
        t[0] = condicional_case.CaseID(t[2],t[3],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")
    elif t[1] == "CASE" and len(t) == 9:
        t[0] = condicional_case.CaseIDElse(t[2],t[3],t[5],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")

def p_instrucciones_if(t):
    ''' 
    instrucciones_if : instrucciones_if instruccion_if 
                     | instruccion_if
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
    
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
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_condicion_if(t):
    '''
    condicionif : ELSIF expre THEN instrucciones_if 
			    | ELSEIF expre THEN instrucciones_if  
    '''
    t[0] = condicional_if.If(t[2],t[4],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")
    
def p_condiciones_cuando(t):
    '''
    condiciones_cuando : condiciones_cuando condicion_cuando
				       | condicion_cuando
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_condicion_cuando(t):
    '''
    condicion_cuando : WHEN l_expresiones THEN instrucciones_if

    '''
    t[0] = condicional_case.condicion_caseID(t[2],t[4],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")

def p_condiciones_cuando_B(t):
    '''
    condiciones_cuandoB : condiciones_cuandoB condicion_cuandoB
					    | condicion_cuandoB
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_condicion_cuando_B(t):
    '''
    condicion_cuandoB : WHEN expre THEN instrucciones_if
    '''
    print("regresando")
    t[0] = condicional_case.condicion_case(t[2],t[4],"strGram",t.lexer.lineno, t.lexer.lexpos,"strSent")

def p_sql_states(t):
    '''
    sql_states : sql_states OR sql_state
			   | sql_state
    '''

def p_sql_state(t):
    '''
    sql_state : SQLSTATE CADENA
    '''

def p_identificadores(t):
    '''
    l_identificadores : l_identificadores OR ID
                      | ID
    '''

def p_instruccion_index(t):
    '''
    instruccion : CREATE unique_op INDEX nombre_op ON ID hash_op PARIZQ l_indexes PARDER where_op PUNTO_COMA
    '''
    strId = ""
    if isinstance(t[9] , list):
        for i in t[9][:-1]:
            strId += i + ","
        strId += t[9][-1]
    else:
        strId = t[9]
    strTipo = t[2] + " INDEX " + t[7]
    strSent = "CREATE " + t[2] + " INDEX " + t[4] + " ON " + t[6] + " " + t[7] + " (" + strId +") " + t[11] + ";"
    t[0] = CreateIndex.CreateIndex(t[4], strTipo, t[6], strId, "", t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_del_index(t):
    '''
    instruccion : DROP INDEX if_op ID PUNTO_COMA
    '''
    strSent = "DROP " + "INDEX " + t[3] + t[4] + ";"
    t[0] = DropIndex.DropIndex(t[4],None, "", t.lexer.lineno, t.lexer.lexpos, strSent)

def p_instruccion_alter_index(t):
    '''
    instruccion : ALTER INDEX if_op ID ALTER column_op ID ID PUNTO_COMA
    '''
    strSent = "ALTER INDEX " + t[3] + t[4] + " ALTER " + t[6] + t[7] + " " + t[8] + ";"
    t[0] = AlterIndex.AlterIndex(t[4], None, t[7], t[8], "", t.lexer.lineno, t.lexer.lexpos, strSent)


def p_index_column(t):
    '''
    column_op : COLUMN
    '''
    t[0] = "COLUMN "

def p_index_column_e(t):
    '''
    column_op : 
    '''
    t[0] = ""

def p_index_if_exists(t):
    '''
    if_op : IF EXISTS
    '''
    t[0] = "IF EXISTS "

def p_index_if_e(t):
    '''
    if_op : 
    '''
    t[0] = ""

def p_index_nombre(t):
    '''
    nombre_op : ID
    '''
    t[0] = t[1]

def p_index_nombre_e(t):
    '''
    nombre_op : 
    '''
    t[0] = ""

def p_index_unique(t):
    '''
    unique_op : UNIQUE
    '''
    t[0] = "UNIQUE"

def p_index_unique_e(t):
    '''
    unique_op : 
    '''
    t[0] = ""

def p_index_hash(t):
    '''
    hash_op : USING HASH
    '''
    t[0] = "USING HASH"

def p_index_hash_e(t):
    '''
    hash_op : 
    '''
    t[0] = ""

def p_index_indexes(t):
    '''
    l_indexes : l_indexes COMA ID order_op null_op first_last_op
    '''
    cadena = t[3]
    if t[4] != "":
        cadena += " " + t[4]
    if t[5] != "":
        cadena += " " + t[5]
    if t[6] != "":
        cadena += " " + t[6]
    t[1].append(cadena)
    t[0] = t[1]

def p_index_index(t):
    '''
    l_indexes : ID order_op null_op first_last_op
    '''
    cadena = t[1]
    if t[2] != "":
        cadena += " " + t[2]
    if t[3] != "":
        cadena += " " + t[3]
    if t[4] != "":
        cadena += " " + t[4]
    t[0] = [cadena]

def p_index_func(t):
    '''
    l_indexes : ID PARIZQ ID PARDER
    '''
    cadena = t[1] + " (" + t[3] + ")"
    t[0] = cadena

def p_index_order(t):
    '''
    order_op : ASC
            | DESC
    '''
    t[0] = t[1]

def p_index_order_e(t):
    '''
    order_op : 
    '''
    t[0] = ""

def p_index_null(t):
    '''
    null_op : NULLS
    '''
    t[0] = "NULLS"

def p_index_null_e(t):
    '''
    null_op : 
    '''
    t[0] = ""

def p_index_first_last(t):
    '''
    first_last_op : FIRST
                | LAST
    '''
    t[0] = t[1]

def p_index_first_last_e(t):
    '''
    first_last_op : 
    '''
    t[0] = ""

def p_index_where(t):
    '''
    where_op : instructionWhere
    '''
    t[0] = t[1].strSent

def p_index_where_e(t):
    '''
    where_op : 
    '''
    t[0] = ""

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
    