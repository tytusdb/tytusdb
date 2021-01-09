#IMPORTS
from Instrucciones import Relaciones
from Instrucciones.DateTimeTypes import Case , CurrentDate, CurrentTime, DatePart, Extract, Now, Por, TimeStamp
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones import Aritmetica, Logica, Primitivo, Relacional, Between
from Instrucciones.FunctionAgregate import Avg, Count, Greatest, Least, Max, Min, Sum, Top
from Instrucciones.FunctionBinaryString import Convert, Decode, Encode, GetByte, Length, Md5, SetByte, Sha256, Substr, Substring, Trim
from Instrucciones.FunctionMathematical import Abs, Cbrt, Ceil, Ceiling, Degrees, Div, Exp, Factorial, Floor, Gcd, Lcm, Ln, Log, Log10, MinScale, Mod, PI, Power, Radians, Random, Round, Scale, SetSeed, Sign, Sqrt, TrimScale, Trunc, WidthBucket
from Instrucciones.FunctionTrigonometric import Acos, Acosd, Acosh, Asin, Asind, Asinh, Atan, Atan2, Atan2d, Atand, Atanh, Cos, Cosd, Cosh, Cot, Cotd, Sin, Sind, Sinh, Tan, Tand, Tanh
from Instrucciones.Identificador import Identificador
from Instrucciones.PLpgSQL import Body, CaseWhen, Continue, CreateFunction, Execute, Exit, For, IfElse, Llamada, Loop, Parametro, Variable, While
from Instrucciones.Sql_alter import AlterDatabase, AlterDBOwner, AlterIndex, AlterTable, AlterTableAddColumn, AlterTableAddConstraintFK, Columna, AlterTableDropColumn, AlterTableAddConstraint, AlterTableAddFK, AlterTableAlterColumn, AlterTableDropConstraint, AlterTableAlterColumnType, AlterTableAddCheck
from Instrucciones.Sql_create import CreateDatabase, CreateIndex, Campo, CreateOrReplace, CreateTable, CreateType, Use, ShowDatabases,Set
from Instrucciones.Sql_create import Columna as CColumna
from Instrucciones.Sql_create.Tipo_Constraint import *
from Instrucciones.Sql_declare import Declare
from Instrucciones.Sql_delete import DeleteTable
from Instrucciones.Sql_drop import DropDatabase, DropIndex, DropTable
from Instrucciones.Sql_insert import insertTable
from Instrucciones.Sql_Joins import Join, JoinFull, JoinInner, JoinLeft, JoinRight
from Instrucciones.Sql_select import GroupBy, Having, Limit, OrderBy, Select, Where, SelectLista
from Instrucciones.Sql_truncate import Truncate
from Instrucciones.Sql_update import UpdateTable
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.Undefined import Undefined
from lexico import *
from ply import *
from tkinter.constants import HORIZONTAL
from storageManager import jsonMode as storage
# para C3D
import op_aritmeticas as op
import instrucciones as inst
import encabezado as encabezado
import ast_op as op_ast
import reglas as r

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

# Definición de la gramática sql

def p_init(t):
    'init : instrucciones' # gramática SQL
    t[0] = t[1]

def p_instrucciones_lista1(t):
    'instrucciones    :  instrucciones instruccion '
    t[1].append(t[2])
    t[0] = t[1]
    
def p_instrucciones_lista2(t):
    'instrucciones : instruccion '
    t[0] = [t[1]]

# CREATE INDEX
def p_instruccion_create_index(t):
    '''instruccion : CREATE op_unique INDEX ID ON ID op_using PARIZQ ls_index_col PARDER op_where PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE <op_unique> INDEX ID ON ID <op_using> PARIZQ <ls_index_col> PARDER <op_where> PUNTO_COMA"
    t[0] = CreateIndex.CreateIndex(t[2], t[4], t[6], t[7], t[9], t[11], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_unique1(t):
    '''op_unique : UNIQUE
    '''
    strGram = "<op_unique> ::= UNIQUE"
    t[0] = Undefined.Undefined("UNIQUE", "", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_unique2(t):
    '''op_unique : 
    '''
    strGram = "<op_unique> ::= "
    t[0] = Undefined.Undefined("UNIQUE", None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_using1(t):
    '''op_using : USING HASH
    '''
    strGram = "<op_using> ::= USING HASH"
    t[0] = Undefined.Undefined("USING", " HASH", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_using2(t):
    '''op_using : 
    '''
    strGram = "<op_using> ::= "
    t[0] = Undefined.Undefined("USING", None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_ls_index_col1(t):
    '''ls_index_col : ls_index_col COMA val_index_col
    '''
    strGram = "<ls_index_col> ::= <ls_index_col> COMA <val_index_col>"
    t[1].append(t[3])
    t[0] = t[1]

def p_ls_index_col2(t):
    '''ls_index_col : val_index_col
    '''
    strGram = "<ls_index_col> ::= <val_index_col>"
    t[0] = []
    t[0].append(t[1])

def p_ls_index_col3(t):
    '''ls_index_col : PARIZQ ls_index_col PARDER
    '''
    strGram = "<ls_index_col> ::= PARIZQ <ls_index_col> PARDER"
    t[0] = t[2]

def p_val_index_col1(t):
    '''val_index_col : ID op_order op_null
    '''
    strGram = "<val_index_col> ::= ID <op_order> <op_null>"
    t[0] = Campo.Campo(t[1], False, t[2], t[3], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_val_index_col2(t):
    '''val_index_col : LOWER PARIZQ ID op_order op_null PARDER
    '''
    strGram = "<val_index_col> ::= LOWER PARIZQ ID <op_order> <op_null> PARDER "
    t[0] = Campo.Campo(t[3], True, t[4], t[5], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_order1(t):
    '''op_order : ASC
    '''
    strGram = "<op_order> ::= ASC"
    t[0] = Undefined.Undefined("", "ASC", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_order2(t):
    '''op_order : DESC
    '''
    strGram = "<op_order> ::= DESC"
    t[0] = Undefined.Undefined("", "DESC", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_order3(t):
    '''op_order : 
    '''
    strGram = "<op_order> ::= "
    t[0] = Undefined.Undefined("ORDER", None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_null1(t):
    '''op_null : NULLS FIRST
    '''
    strGram = "<op_null> ::= NULLS FIRST"
    t[0] = Undefined.Undefined("NULLS", " FIRST", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_null2(t):
    '''op_null : NULLS LAST
    '''
    strGram = "<op_null> ::= NULLS LAST"
    t[0] = Undefined.Undefined("NULLS", " LAST", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_null3(t):
    '''op_null : 
    '''
    strGram = "<op_null> ::= "
    t[0] = Undefined.Undefined("NULLS", None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_where1(t):
    '''op_where : WHERE expre
    '''
    strGram = "<instructionWhere> ::=  WHERE <expre>"
    t[0] = Where.Where(t[2], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_where2(t):
    '''op_where : 
    '''
    strGram = "<op_where> ::= "
    t[0] = Undefined.Undefined("WHERE", None, strGram, t.lexer.lineno, t.lexer.lexpos)
    
# DROP INDEX
def p_instruccion_drop_index1(t):
    '''instruccion : DROP INDEX op_exists ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= DROP INDEX <op_exists> ID PUNTO_COMA"
    if t[4]:
        strGram += "\n<op_exists> ::= "
    else:
        strGram += "\n<op_exists> ::= IF EXISTS"
    t[0] = DropIndex.DropIndex(t[3], t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_exists1(t):
    '''op_exists : IF EXISTS
    '''
    t[0] = False

def p_op_exists(t):
    '''op_exists : 
    '''
    t[0] = True

# ALTER INDEX
def p_instruccion_alter_index1(t):
    '''instruccion : ALTER INDEX op_exists ID op_alter ID ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER INDEX <op_exists> ID <op_alter> ID ID PUNTO_COMA"
    if t[3]:
        strGram += "\n<op_exists> ::= \n" + t[5]
    else:
        strGram += "\n<op_exists> ::= IF EXISTS\n" + t[5]
    t[0] = AlterIndex.AlterIndex(t[3], t[4], t[6], t[7], strGram, t.lexer.lineno, t.lexer.lexpos)
    
def p_instruccion_alter_index2(t):
    '''instruccion : ALTER INDEX op_exists ID op_alter ID ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER INDEX <op_exists> ID <op_alter> ID ENTERO PUNTO_COMA"
    if t[3]:
        strGram += "\n<op_exists> ::= \n" + t[5]
    else:
        strGram += "\n<op_exists> ::= IF EXISTS\n" + t[5]
    t[0] = AlterIndex.AlterIndex(t[3], t[4], t[6], t[7], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_alter1(t):
    '''op_alter : ALTER COLUMN
    '''
    t[0] = "<op_alter> ::= ALTER COLUMN"

def p_op_alter2(t):
    '''op_alter : ALTER 
    '''
    t[0] = "<op_alter> ::= ALTER"

def p_op_alter3(t):
    '''op_alter : 
    '''
    t[0] = "<op_alter> ::= "

# EXEC
def p_instruccion_execute(t):
    '''instruccion : EXECUTE llamada PUNTO_COMA
    '''
    strGram = "<instruccion> ::= EXECUTE <llamada>"
    t[0] = Execute.Execute(t[2].nombre, t[2].parametros, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_llamada1(t):
    '''llamada : ID PARIZQ PARDER
    '''
    strGram = "<llamada> ::= ID PARIZQ PARDER"
    t[0] = Llamada.Llamada(t[1], [], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_llamada2(t):
    '''llamada : ID PARIZQ list_exp PARDER
    '''
    strGram = "<llamada> ::= ID PARIZQ <list_exp> PARDER"
    t[0] = Llamada.Llamada(t[1], t[3], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_list_exp1(t):
    '''list_exp : list_exp COMA expresion
    '''
    strGram = "<list_exp> ::= <list_exp> COMA <expresion>"

def p_list_exp2(t):
    '''list_exp : expresion
    '''
    strGram = "<list_exp> ::= <expresion>"

# CREATE DATABASE
def p_instruccion_create_database1(t):
    '''instruccion : CREATE DATABASE if_not_exists ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, None, 1, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database2(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> ID PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, t[7], 1, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database3(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> MODE IGUAL ENTERO PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, t[7], t[10], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database4(t):
    '''instruccion : CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    strGram  = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID MODE IGUAL ENTERO PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, None, t[7], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database5(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER cowner PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID OWNER <cowner> ID PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, t[6], 1, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database6(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID OWNER <cowner> MODE IGUAL ENTERO PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, t[6], t[9], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database7(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner MODE ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> MODE ENTERO PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, t[7], t[9], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database8(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER cowner MODE ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID OWNER <cowner> MODE ENTERO PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, t[6], t[8], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database9(t):
    '''instruccion : CREATE DATABASE if_not_exists ID MODE ENTERO PUNTO_COMA
    '''
    strGram  = "<instruccion> ::= CREATE DATABASE <if_not_exists> ID MODE ENTERO PUNTO_COMA"
    t[0] = CreateDatabase.CreateDatabase(t[4], None, t[3].valor, None, t[6], strGram, t.lexer.lineno, t.lexer.lexpos)

# CREATE OR REPLACE DATABASE
def p_instruccion_create_or_database1(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, None, 1, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database2(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> ID PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], 1, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database3(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> MODE IGUAL ENTERO PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], t[12], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database4(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID MODE IGUAL ENTERO PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, None, t[9], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database5(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER cowner PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID OWNER <cowner> ID PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[8], 1, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database6(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID OWNER <cowner> MODE IGUAL ENTERO PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[8], t[11], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database7(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner MODE ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID OWNER IGUAL <cowner> MODE ENTERO PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], t[11], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database8(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER cowner MODE ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID OWNER <cowner> MODE ENTERO PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[8], t[10], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database9(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID MODE ENTERO PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE OR REPLACE DATABASE <if_not_exists> ID MODE ENTERO PUNTO_COMA"
    t[0] = CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, None, t[8], strGram, t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = Primitivo.Primitivo("IF NOT EXISTS",Tipo_Dato.VARCHAR, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_if_not_exists1(t):
    '''if_not_exists : 
    '''
    strGram = "<if_not_exists> ::= "
    t[0] = Primitivo.Primitivo("NULL",Tipo_Dato.VARCHAR, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create1(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE TABLE ID PARIZQ <campos> PARDER PUNTO_COMA"
    t[0] =CreateTable.CreateTable(t[3], None, t[5], None, strGram,t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create2(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE TABLE ID PARIZQ <campos> PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA"
    t[0] =CreateTable.CreateTable(t[3],None, t[5], t[9], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_use(t):
    '''instruccion : USE ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= USE ID PUNTO_COMA"
    t[0] =Use.Use(t[2], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_show_database1(t):
    '''instruccion : SHOW DATABASES PUNTO_COMA
    '''
    strGram = "<instruccion> ::= SHOW DATABASES PUNTO_COMA"
    t[0] =ShowDatabases.ShowDatabases(None, None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_show_database2(t):
    '''instruccion : SHOW DATABASES LIKE CARACTER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= SHOW DATABASES LIKE CARACTER PUNTO_COMA"
    t[0] =ShowDatabases.ShowDatabases(t[4],None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_enumerated_type(t):
    '''instruccion : CREATE TYPE ID AS ENUM PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE TYPE ID AS ENUM PARIZQ <l_expresiones> PARDER PUNTO_COMA"
    t[0] =CreateType.CreateType(t[3],None,t[7], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_truncate(t):
    '''instruccion : TRUNCATE TABLE ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= TRUNCATE TABLE ID PUNTO_COMA"
    t[0] =Truncate.Truncate(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)

# DROP DATABASE
def p_instruccion_drop_database1(t):
    '''instruccion : DROP DATABASE ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= DROP DATABASE ID PUNTO_COMA"
    t[0] = DropDatabase.DropDatabase(t[3], None, False, 0, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_drop_database2(t):
    '''instruccion : DROP DATABASE IF EXISTS ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= DROP DATABASE IF EXISTS ID PUNTO_COMA"
    t[0] = DropDatabase.DropDatabase(t[5], None, True, 1, strGram, t.lexer.lineno, t.lexer.lexpos)

# DROP TABLE
def p_instruccion_drop(t):
    '''instruccion : DROP TABLE ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= DROP TABLE ID PUNTO_COMA"
    t[0] = DropTable.DropTable(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_where(t):
    '''
        instructionWhere :  WHERE expre
    '''
    strGram = "<instructionWhere> ::=  WHERE <expre>"
    t[0] = Where.Where(t[2],None, strGram, t.lexer.lineno, t.lexer.lexpos)

# update tabla set campo = valor , campo 2= valor where condicion

def p_instruccion_update(t):
    '''instruccion : UPDATE ID SET lcol instructionWhere PUNTO_COMA

    '''
    strGram = "<instruccion> ::= UPDATE ID SET <lcol> <instructionWhere> PUNTO_COMA"
    strGram2 = ""
    id1 = Identificador(t[2], strGram2 ,t.lexer.lineno, t.lexer.lexpos)
    t[0] = UpdateTable.UpdateTable(id1, None, t[4], t[5], strGram ,t.lexer.lineno, t.lexer.lexpos)

# update tabla set campo = valor , campo 2= valor;

def p_instruccion_update2(t):
    '''instruccion : UPDATE ID SET lcol PUNTO_COMA
    '''
    strGram = "<instruccion> ::= UPDATE ID SET <lcol> PUNTO_COMA"
    strGram2 = ""
    id1 = Identificador(t[2], strGram2 ,t.lexer.lineno, t.lexer.lexpos)
    t[0] = UpdateTable.UpdateTable(id1, None, t[4], None, strGram ,t.lexer.lineno, t.lexer.lexpos)

# DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
def p_columunas_delete(t):
    '''instruccion : DELETE FROM ID instructionWhere PUNTO_COMA
    '''
    strGram = "<instruccion> ::= DELETE FROM ID <instructionWhere> PUNTO_COMA"
    t[0] = DeleteTable.DeleteTable(t[3],None, t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

#FUNCIONES
def p_functions(t):
    ''' instruccion : CREATE FUNCTION ID PARIZQ op_lpar PARDER RETURNS tipo AS body LANGUAGE PLPGSQL PUNTO_COMA
    '''
    strGram = "<instruccion> ::= CREATE FUNCTION ID PARIZQ <op_lpar> PARDER RETURNS <tipo> AS <body> LANGUAGE PLPGSQL PUNTO_COMA"
    t[0] = CreateFunction.CreateFunction(t[3], t[8], t[5], t[10].declaraciones, t[10].sentencias, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_procedures(t):
    ''' instruccion : CREATE PROCEDURE ID PARIZQ op_lpar PARDER LANGUAGE PLPGSQL AS body
    '''
    strGram = "<instruccion> ::= CREATE PROCEDURE ID PARIZQ <op_lpar> PARDER RETURNS <tipo> AS <body> LANGUAGE PLPGSQL PUNTO_COMA"
    t[0] = CreateFunction.CreateFunction(t[3], Tipo(Tipo_Dato.VOID), t[5], t[10].declaraciones, t[10].sentencias, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_lpar1(t):
    '''op_lpar : l_par
    '''
    strGram = "<op_lpar> ::= <l_par>"
    t[0] = t[1]

def p_op_lpar2(t):
    '''op_lpar : 
    '''
    strGram = "<op_lpar> ::= "
    t[0] = []

def p_l_par1(t):
    '''l_par : l_par COMA par
    '''
    strGram = "<l_par> ::= <l_par> COMA <par>"
    t[1].append(t[2])
    t[0] = t[1]

def p_l_par2(t):
    '''l_par : par
    '''
    strGram = "<l_par> ::= <par>"
    t[0] = []
    t[0].append(t[1])

def p_par1(t):
    '''par : ID tipo  
    '''
    strGram = "<par> ::= ID <tipo>"
    t[0] = Parametro.Parametro(t[1], t[2], None, None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_par2(t):
    '''par : ID 
    '''
    strGram = "<par> ::= ID"
    t[0] = Parametro.Parametro(t[1], None, None, None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_body1(t):
    '''body : PLABEL l_dec BEGIN statements END PUNTO_COMA PLABEL
    '''
    strGram = "<body> ::= PLABEL <l_dec> BEGIN statements END PUNTO_COMA PLABEL"
    t[0] = Body.Body(t[2], t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_body2(t):
    '''body : PLABEL BEGIN statements END PUNTO_COMA PLABEL
    '''
    strGram = "<body> ::= PLABEL BEGIN statements END PUNTO_COMA PLABEL"
    t[0] = Body.Body([], t[3], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_l_dec1(t):
    '''l_dec : l_dec dec_sg
    '''
    strGram = "<l_dec> ::= <l_dec> <dec_sg>"
    for val in t[2]:
        t[1].append(val)
    t[0] = t[1]

def p_l_dec2(t):
    '''l_dec : dec_sg
    '''
    strGram = "<l_dec> ::= <dec_sg>"
    t[0] = t[1]

def p_dec_sg(t):
    '''dec_sg : DECLARE l_seg
    '''
    strGram = "<dec_sg> ::= DECLARE <l_seg>"
    t[0] = t[2]

def p_l_seg1(t):
    '''l_seg : l_seg segment
    '''
    strGram = "<l_seg> ::= <l_seg> <segment>"
    t[1].append(t[2])
    t[0] = t[1]

def p_l_seg2(t):
    '''l_seg : segment
    '''
    strGram = "<l_seg> ::= <segment>"
    t[0] = []
    t[0].append(t[1])

def p_segment1(t):
    '''segment : ID op_constant tipo op_nulo op_asig PUNTO_COMA
    '''
    strGram = "<segment> ::= ID <op_constant> <tipo> <op_nulo> <op_asig> PUNTO_COMA"
    t[0] = Variable.Variable(t[1], t[2], t[3], t[4], t[5], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_segment2(t):
    '''segment : ID ALIAS FOR R_PAR PUNTO_COMA
    '''
    strGram = "<segment> ::= ID ALIAS FOR R_PAR PUNTO_COMA"
    cons = Undefined.Undefined("CONSTANT", None, None, t.lexer.lineno, t.lexer.lexpos)
    nulo = Undefined.Undefined("NULL", "", None, t.lexer.lineno, t.lexer.lexpos)
    t[0] = Variable.Variable(t[1], cons, nulo, None, (t[4].split("$"))[1], t.lexer.lineno, t.lexer.lexpos)

def p_segment3(t):
    '''segment : ID ALIAS FOR ID PUNTO_COMA
    '''
    strGram = "<segment> ::= ID ALIAS FOR ID PUNTO_COMA"
    cons = Undefined.Undefined("CONSTANT", None, None, t.lexer.lineno, t.lexer.lexpos)
    nulo = Undefined.Undefined("NULL", "", None, t.lexer.lineno, t.lexer.lexpos)
    t[0] = Variable.Variable(t[1], cons, nulo, None, t[4], t.lexer.lineno, t.lexer.lexpos)

def p_op_constant1(t):
    '''op_constant : CONSTANT
    '''
    strGram = "<op_constant> ::= CONSTANT"
    t[0] = Undefined.Undefined("CONSTANT", "", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_constant2(t):
    '''op_constant : 
    '''
    strGram = "<op_constant> ::= "
    t[0] = Undefined.Undefined("CONSTANT", None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_nulo1(t):
    '''op_nulo : NOT NULL
    '''
    strGram = "<op_nulo> ::= NOT NULL"
    t[0] = Undefined.Undefined("NOT", " NULL", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_nulo2(t):
    '''op_nulo : NULL
    '''
    strGram = "<op_nulo> ::= NULL"
    t[0] = Undefined.Undefined("NULL", "", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_nulo3(t):
    '''op_nulo : 
    '''
    strGram = "<op_nulo> ::= "
    t[0] = Undefined.Undefined("NULL", "", strGram, t.lexer.lineno, t.lexer.lexpos)

def p_op_asig1(t):
    '''op_asig : DEFAULT expresion
    '''
    strGram = "<op_asig> ::= DEFAULT <expresion>"
    t[0] = []
    t[0].append(strGram)
    t[0].append(t[2])

def p_op_asig2(t):
    '''op_asig : DP_IGUAL expresion
    '''
    strGram = "<op_asig> ::= DP_IGUAL <expresion>"
    t[0] = []
    t[0].append(strGram)
    t[0].append(t[2])

def p_op_asig3(t):
    '''op_asig : IGUAL expresion
    '''
    strGram = "<op_asig> ::= IGUAL <expresion>"
    t[0] = []
    t[0].append(strGram)
    t[0].append(t[2])

def p_op_asig4(t):
    '''op_asig :
    '''
    strGram = "<op_asig> ::= "
    t[0] = []
    t[0].append(strGram)
    t[0].append(None)

def p_statements1(t):
    '''statements : statements statement
    '''
    strGram = "<statements> ::= <statements> <statement>"
    t[1].append(t[2])
    t[0] = t[1]
    
def p_statements2(t):
    '''statements : statement
    '''
    strGram = "<statements> ::= <statement>"
    t[0] = []
    t[0].append(t[1])

def p_statement1(t):
    '''statement : instruccion
    '''
    strGram = "<statement> ::= <instruccion>"
    t[0] = t[1]

def p_statement2(t):
    '''statement : ID IGUAL expre PUNTO_COMA
                 | ID DP_IGUAL expre PUNTO_COMA
    '''
    strGram = "<statement> ::= ID IGUAL <expre> PUNTO_COMA"
    t[0] = Asignacion.Asignacion(t[1], t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement3(t):
    '''statement : ID IGUAL query PUNTO_COMA
                 | ID DP_IGUAL query PUNTO_COMA
    '''
    strGram = "<statement> ::= ID IGUAL <query> PUNTO_COMA"
    t[0] = Asignacion.Asignacion(t[1], None, t[3], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement4(t):
    '''statement : RETURN expre PUNTO_COMA
    '''
    strGram = "<statement> ::= RETURN <expre> PUNTO_COMA"
    t[0] = t[1]

def p_statement5(t):
    '''statement : st_if END IF PUNTO_COMA
    '''
    strGram = "<statement> ::= <st_if> END IF PUNTO_COMA"

def p_st_if1(t):
    '''st_if : st_si 
    '''
    strGram = "<st_if> ::= <st_si>"

def p_st_if2(t):
    '''st_if : st_si sts_sino_si
    '''
    strGram = "<st_if> ::= <st_si> <sts_sino_si>"

def p_st_if3(t):
    '''st_if : st_si sts_sino_si st_sino
    '''
    strGram = "<st_if> ::= <st_si> <sts_sino_si> <st_sino>"

def p_st_if4(t):
    '''st_if : st_si st_sino
    '''
    strGram = "<st_if> ::= <st_si> <st_sino>"

def p_st_if1_1(t):
    '''st_si : IF expre THEN statements 
    '''
    strGram = "<st_if> ::= IF <expre> THEN <statements>"

#----> esto es una lista de elseif's
def p_st_if2_1(t):
    '''sts_sino_si : sts_sino_si st_sino_si
    '''
    strGram = "<sts_sino_si> ::= <sts_sino_si> <st_sino_si>"

def p_st_if2_2(t):
    '''sts_sino_si : st_sino_si
    '''
    strGram = "<sts_sino_si> ::= <st_sino_si>"
#----fin lista

def p_st_if2_3(t):
    '''st_sino_si : ELSIF expre THEN statements 
    '''
    strGram = "<st_sino_si> ::= ELSIF <expre> THEN <statements>"

def p_st_if2_4(t):
    '''st_sino : ELSE statements
    '''
    strGram = "<st_sino> ::= ELSE <statements>"

def p_statement6(t):
    '''statement : CASE ID st_case
    '''
    strGram = "<statement> ::= CASE ID <st_case>"
    #t[0] = t[2]

def p_st_case1(t):
    '''st_case : WHEN list_exp THEN statements END CASE PUNTO_COMA
    '''
    strGram = "<st_case> ::=  WHEN <list_exp> THEN <statements> END CASE PUNTO_COMA"

def p_st_case2(t):
    '''st_case : WHEN list_exp THEN statements ELSE statements END CASE PUNTO_COMA
    '''
    strGram = "<st_case> ::=  WHEN <list_exp> THEN <statements> ELSE <statements> END CASE PUNTO_COMA"

def p_st_case3(t):
    '''st_case : WHEN list_exp THEN statements st_case
    '''
    strGram = "<st_case> ::=  WHEN <list_exp> THEN <statements> <st_case>"

def p_statement7(t):
    '''statement : CASE st_case_s
    '''
    strGram = "<statement> ::= CASE <st_case_s>"
    t[0] = t[1]

def p_st_case_s1(t):
    '''st_case_s : WHEN expre THEN statements END CASE PUNTO_COMA
    '''
    strGram = "<st_case_s> ::=  WHEN <expre> THEN <statements> END CASE PUNTO_COMA"

def p_st_case_s2(t):
    '''st_case_s : WHEN expre THEN statements ELSE statements END CASE PUNTO_COMA
    '''
    strGram = "<st_case_s> ::=  WHEN <expre> THEN <statements> ELSE <statements> END CASE PUNTO_COMA"

def p_st_case_s3(t):
    '''st_case_s : WHEN expre THEN statements st_case_s
    '''
    strGram = "<st_case_s> ::=  WHEN <expre> THEN <statements> <st_case_s>"

def p_statement8(t):
    '''statement : LOOP statements END LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= LOOP <statements> END LOOP PUNTO_COMA"
    t[0] = Loop.Loop(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement9(t):
    '''statement : LBL_LOOP LOOP statements END LOOP LBL_LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= LBL_LOOP LOOP <statements> END LOOP LBL_LOOP PUNTO_COMA"
    t[0] = Loop.Loop(t[3], [t[1], t[6]], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement10(t):
    '''statement : WHILE expre LOOP statements END LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= WHILE <expre> LOOP <statements> END LOOP PUNTO_COMA"
    t[0] = While.While(t[2], t[4], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement11(t):
    '''statement : LBL_LOOP WHILE expre LOOP statements END LOOP LBL_LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= LBL_LOOP WHILE <expre> LOOP <statements> END LOOP LBL_LOOP PUNTO_COMA"
    t[0] = While.While(t[3], t[5], [t[1], t[8]], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement12(t):
    '''statement : FOR ID ENTERO P_RANGO ENTERO LOOP statements END LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= FOR ID ENTERO P_RANGO ENTERO LOOP <statements> END LOOP PUNTO_COMA"
    t[0] = For.For(t[2], False, [t[3], t[5]], 1, t[7], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement13(t):
    '''statement : FOR ID REVERSE ENTERO P_RANGO ENTERO LOOP statements END LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= FOR ID REVERSE ENTERO P_RANGO ENTERO LOOP <statements> END LOOP PUNTO_COMA"
    t[0] = For.For(t[2], True, [t[4], t[6]], 1, t[8], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement14(t):
    '''statement : FOR ID ENTERO P_RANGO ENTERO BY ENTERO LOOP statements END LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= FOR ID ENTERO P_RANGO ENTERO BY ENTERO LOOP <statements> END LOOP PUNTO_COMA"
    t[0] = For.For(t[2], False, [t[3], t[5]], t[7], t[9], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement15(t):
    '''statement : FOR ID REVERSE ENTERO P_RANGO ENTERO BY ENTERO LOOP statements END LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= FOR ID REVERSE ENTERO P_RANGO ENTERO BY ENTERO LOOP <statements> END LOOP PUNTO_COMA"
    t[0] = For.For(t[2], True, [t[4], t[6]], t[8], t[10], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement16(t):
    '''statement : LBL_LOOP FOR ID ENTERO P_RANGO ENTERO LOOP statements END LOOP LBL_LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= LBL_LOOP FOR ID ENTERO P_RANGO ENTERO LOOP <statements> END LOOP LBL_LOOP PUNTO_COMA"
    t[0] = For.For(t[3], False, [t[4], t[6]], 1, t[8], [t[1], t[11]], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement17(t):
    '''statement : LBL_LOOP FOR ID REVERSE ENTERO P_RANGO ENTERO LOOP statements END LOOP LBL_LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= LBL_LOOP FOR ID REVERSE ENTERO P_RANGO ENTERO LOOP <statements> END LOOP LBL_LOOP PUNTO_COMA"
    t[0] = For.For(t[3], True, [t[5], t[7]], 1, t[9], [t[1], t[12]], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement18(t):
    '''statement : LBL_LOOP FOR ID ENTERO P_RANGO ENTERO BY ENTERO LOOP statements END LOOP LBL_LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= LBL_LOOP FOR ID ENTERO P_RANGO ENTERO BY ENTERO LOOP <statements> END LOOP LBL_LOOP PUNTO_COMA"
    t[0] = For.For(t[3], False, [t[4], t[6]], t[8], t[10], [t[1], t[13]], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement19(t):
    '''statement : LBL_LOOP FOR ID REVERSE ENTERO P_RANGO ENTERO BY ENTERO LOOP statements END LOOP LBL_LOOP PUNTO_COMA
    '''
    strGram = "<statement> ::= LBL_LOOP FOR ID REVERSE ENTERO P_RANGO ENTERO BY ENTERO LOOP <statements> END LOOP LBL_LOOP PUNTO_COMA"
    t[0] = For.For(t[3], True, [t[5], t[7]], t[9], t[11], [t[1], t[14]], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement20(t):
    '''statements : EXIT PUNTO_COMA
    '''
    strGram = "<statements> ::= EXIT PUNTO_COMA"
    t[0] = Exit.Exit(None, None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement21(t):
    '''statements : EXIT ID PUNTO_COMA
    '''
    strGram = "<statements> ::= EXIT ID PUNTO_COMA"
    t[0] = Exit.Exit(t[2], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement22(t):
    '''statements : EXIT WHEN expre PUNTO_COMA
    '''
    strGram = "<statements> ::= EXIT WHEN <expre> PUNTO_COMA"
    t[0] = Exit.Exit(None, t[3], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement23(t):
    '''statements : EXIT ID WHEN expre PUNTO_COMA
    '''
    strGram = "<statements> ::= EXIT ID WHEN <expre> PUNTO_COMA"
    t[0] = Exit.Exit(t[2], t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement24(t):
    '''statement : CONTINUE PUNTO_COMA
    '''
    strGram = "<statement> ::= CONTINUE PUNTO_COMA"
    t[0] = Continue.Continue(None, None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement25(t):
    '''statement : CONTINUE ID PUNTO_COMA
    '''
    strGram = "<statement> ::= CONTINUE ID PUNTO_COMA"
    t[0] = Continue.Continue(t[2], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement26(t):
    '''statement : CONTINUE WHEN expre PUNTO_COMA
    '''
    strGram = "<statement> ::= CONTINUE WHEN <expre> PUNTO_COMA"
    t[0] = Continue.Continue(None, t[3], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_statement27(t):
    '''statement : CONTINUE ID WHEN expre PUNTO_COMA
    '''
    strGram = "<statement> ::= CONTINUE ID WHEN <expre> PUNTO_COMA"
    t[0] = Continue.Continue(t[2], t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_set(t):
    ''' instruccion : SET expresion IGUAL expre PUNTO_COMA
    '''
    strGram = "<instruccion> ::= SET <expresion> IGUAL <expre> PUNTO_COMA"
    t[0] =Set.Set(t[2], None, t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

# ALTER DATABASE name RENAME TO new_name
def p_instruccion_alter_database1(t):
    '''instruccion : ALTER DATABASE ID RENAME TO ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER DATABASE ID RENAME TO ID PUNTO_COMA"
    t[0] = AlterDatabase.AlterDatabase(t[3], None, t[4], t[6], strGram ,t.lexer.lineno, t.lexer.lexpos)

# ALTER DATABASE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
def p_instruccion_alter_database2(t):
    '''instruccion : ALTER DATABASE ID OWNER TO list_owner PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER DATABASE ID OWNER TO <list_owner> PUNTO_COMA\n"
    strGram = strGram + "<list_owner> ::= ID| CURRENT_USER| SESSION_USER" 
    
    t[0] = AlterDBOwner.AlterDBOwner(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = AlterTableAddColumn.AlterTableAddColumn(t[3], t[4], strGram ,t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = Columna.Columna(t[3], t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;
def p_instruccion_alter2(t):
    '''instruccion : ALTER TABLE ID l_drop_column PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID <l_drop_column> PUNTO_COMA\n"
    strGram = strGram + "<l_drop_column> ::= <l_drop_column> COMA <drop_column>\n"
    strGram = strGram + "<l_drop_column> ::= <drop_column>"
    t[0] = AlterTableDropColumn.AlterTableDropColumn(t[3], t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = Columna.Columna(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CHECK EXP;
def p_instruccion_alter3(t):
    '''instruccion : ALTER TABLE ID ADD CHECK expre PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ADD CHECK <expre> PUNTO_COMA"
    t[0] = AlterTableAddCheck.AlterTableAddCheck(t[3],t[6], strGram, t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter4(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ lista_id PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ <lista_id> PARDER PUNTO_COMA"
    t[0] = AlterTableAddConstraint.AlterTableAddConstraint(t[3], t[6], t[9], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_altercfk(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER PUNTO_COMA"
    t[0] = AlterTableAddConstraintFK.AlterTableAddConstraintFK(t[3], t[6], t[10], t[13], t[15], strGram, t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE child_table ADD FOREIGN KEY (fk_columns) REFERENCES parent_table (parent_key_columns);
def p_instruccion_alter5(t):
    '''instruccion : ALTER TABLE ID ADD FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ADD FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER PUNTO_COMA"
    t[0] = AlterTableAddFK.AlterTableAddFK(t[3], t[8], t[11], t[13], strGram, t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ALTER COLUMN 'NOMBRE' SET NOT NULL;
def p_instruccion_alter6(t):
    '''instruccion : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA"
    t[0] = AlterTableAlterColumn.AlterTableAlterColumn(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' DROP CONSTRAINT 'NOMBRE';
def p_instruccion_alter7(t):
    '''instruccion : ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA"
    t[0] = AlterTableDropConstraint.AlterTableDropConstraint(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter8(t):
    '''instruccion : ALTER TABLE ID l_alter PUNTO_COMA
    '''
    strGram = "<instruccion> ::= ALTER TABLE ID <l_alter> PUNTO_COMA"
    t[0] = AlterTableAlterColumnType.AlterTableAlterColumnType(t[3], t[4], strGram, t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = Columna.Columna(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos)

# insert into tabla (campo1,campo2,campo3,campo4) values (valor1, valor2, valor3, valor4)
# unicamente validar que tengan los mismos campos y la mismas cantidad de valores

def p_instruccion_insert(t):
    '''instruccion : INSERT INTO ID PARIZQ lista_id PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= INSERT INTO ID PARIZQ <lista_id> PARDER VALUES PARIZQ <l_expresiones> PARDER PUNTO_COMA"
    t[0] = insertTable.insertTable(t[3], None, t[5], t[9], strGram, t.lexer.lineno, t.lexer.lexpos)

#insert into tabla values (valor1,valor2,valor3)
# debe validar que la cantidad de valores coincida con la cantidad de columnas de la tabla y el tipo de dato
def p_instruccion_insert2(t):
    '''
    instruccion : INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    strGram = "<instruccion> ::= INSERT INTO ID VALUES PARIZQ <l_expresiones> PARDER PUNTO_COMA"
    t[0] = insertTable.insertTable(t[3], None, None, t[6], strGram, t.lexer.lineno, t.lexer.lexpos)

# SELECT col, col FROM id;
# SELECT * from id;
def p_instruccion_query(t):
    '''
    instruccion : lquery PUNTO_COMA
    '''
    t[0]=t[1]

def p_lista_querys(t):
    '''lquery : lquery relaciones query
    '''
    strGram = "<lquery> ::= <lquery> <relaciones> <query>"    
    t[0] = Relaciones.Relaciones(t[1],t[2],t[3],strGram,t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = t[1]

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
    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, None, None, strGram ,t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select1(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <instructionWhere> <lrows>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, t[6], t[7], strGram ,t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2 ,t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select2(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <instructionWhere>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, t[6], None, strGram,t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select3(t):
    '''
    query : SELECT dist lcol FROM lcol linners 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <linners>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], None, None, strGram,t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2 , t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select4(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <linners> <instructionWhere> <lrows>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], t[7], t[8], strGram, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select5(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <linners> <instructionWhere>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], t[7], None, strGram, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select6(t):
    '''
    query : SELECT dist lcol 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol>"
    t[0] = SelectLista.SelectLista(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select7(t):
    '''
    query   : SELECT dist lcol FROM lcol lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    strGram = "<query> ::= SELECT <dist> <lcol> FROM <lcol> <lrows>"
    strGram2 = ""
    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, None, t[6], strGram, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, strGram2, t.lexer.lineno, t.lexer.lexpos)

def p_lista_case1(t):
    '''lcase : lcase case
    '''
    t[0] = t[1].append(t[2])

def p_lista_case2(t):
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
        | 
    '''
    try:
        t[0] = t[1]
    except:
        #error
        pass

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
        if t[4]:
            if t[4] == "DESC":
                strGram = strGram + " DESC"
            elif t[4] == "ASC":
                strGram = strGram + " ASC"
            else:
                if t[5]:
                    if t[5] == "FIRST":
                        strGram = strGram + " FIRST"
                    else:
                        strGram = strGram + " LAST"


        t[0] = OrderBy.OrderBy(t[3], t[4], strGram,t.lexer.lineno, t.lexer.lexpos)
    elif(t[1] == "GROUP"):
        strGram = "<rows> ::= GROUP BY <l_expresiones>"
        t[0] = GroupBy.GroupBy(t[3], None, strGram,t.lexer.lineno, t.lexer.lexpos)
    elif(t[1] == "HAVING"):
        strGram = "<rows> ::= HAVING <lcol>"
        t[0] = Having.Having(t[2], None, t.lexer.lineno, t.lexer.lexpos)   
    elif(t[1] == "LIMIT"):
        #LIMIT(LIMITE,None,fila,columna)
        strGram = "<rows> ::= LIMIT ENTERO"
        t[0] = Limit.Limit(t[2], None, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_row2(t):
    '''rows : LIMIT ENTERO OFFSET ENTERO'''
    #LIMIT(LIMITE,FILAS_A_EXCLUIR,fila,columna)
    strGram = "<rows> ::= LIMIT ENTERO OFFSET ENTERO"
    t[0] = Limit.Limit(t[2], t[4], strGram, t.lexer.lineno, t.lexer.lexpos) 

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
    if t[2] == "OR":
        strGram = "<expre> ::= <expre> OR <expre>"
    elif t[2] == "AND":
        strGram = "<expre> ::= <expre> AND <expre>"

    t[0] = Logica.Logica(t[1], t[3], t[2].upper(), strGram, t.lexer.lineno, t.lexer.lexpos)

def p_operadores_unarios(t):
    ''' expre : NOT expre
    '''
    strGram = "<expre> ::= NOT <expre>"
    t[0] = Logica.Logica(t[2], None, 'NOT', strGram, t.lexer.lineno, t.lexer.lexpos)

def p_operadores_relacionales(t):
    ''' expre : expre IGUAL expre
            | expre MAYORQ expre
            | expre MENORQ expre
            | expre MAYOR_IGUALQ expre
            | expre MENOR_IGUALQ expre
            | expre DISTINTO expre
    '''
    strGram = ""
    if t[2] == "IGUAL":
        strGram = "<expre> ::= <expre> IGUAL <expre>"
    elif t[2] == "MAYORQ":
        strGram = "<expre> ::= <expre> MAYORQ <expre>"
    elif t[2] == "MENORQ":
        strGram = "<expre> ::= <expre> MENORQ <expre>"
    elif t[2] == "MAYOR_IGUALQ":
        strGram = "<expre> ::= <expre> MAYOR_IGUALQ <expre>"
    elif t[2] == "MENOR_IGUALQ":
        strGram = "<expre> ::= <expre> MENOR_IGUALQ <expre>"
    elif t[2] == "DISTINTO":
        strGram = "<expre> ::= <expre> DISTINTO <expre>"

    
    t[0] = Relacional.Relacional(t[1], t[3], t[2],strGram ,t.lexer.lineno, t.lexer.lexpos)

def p_operadores_aritmeticos(t):
    '''expre : expre MAS expre
            | expre MENOS expre
            | expre POR expre
            | expre DIVIDIDO expre
            | expre EXPONENCIACION expre
            | expre MODULO expre
    '''
    
    strGram = ""
    if t[2] == "MAS":
        strGram = "<expre> ::= <expre> MAS <expre>"
    elif t[2] == "MENOS":
        strGram = "<expre> ::= <expre> MENOS <expre>"
    elif t[2] == "POR":
        strGram = "<expre> ::= <expre> POR <expre>"
    elif t[2] == "DIVIDIDO":
        strGram = "<expre> ::= <expre> DIVIDIDO <expre>"
    elif t[2] == "EXPONENCIACION":
        strGram = "<expre> ::= <expre> EXPONENCIACION <expre>"
    elif t[2] == "MODULO":
        strGram = "<expre> ::= <expre> MODULO <expre>"

    t[0] = Aritmetica.Aritmetica(t[1], t[3], t[2], strGram ,t.lexer.lineno, t.lexer.lexpos)

def p_operador_unario(t):
    'expre : MENOS expre %prec UMENOS'
    strGram = "<expre> ::= MENOS <expre> %prec UMENOS"
    t[0] = Aritmetica.Aritmetica(t[2], None, '-', strGram,t.lexer.lineno, t.lexer.lexpos)

def p_operadores_like(t):
    '''expre : expre LIKE expre
            | expre NOT LIKE expre
    '''
    strGram = ""
    if t[2] == "NOT":
        strGram = "<expre> ::= <expre> NOT LIKE <expre>"
        t[0] = Relacional.Relacional(t[1], t[4], "NOT LIKE", strGram, t.lexer.lineno, t.lexer.lexpos)

    else: 
        strGram = "<expre> ::= <expre> LIKE <expre>"
        t[0] = Relacional.Relacional(t[1], t[3], "LIKE", strGram, t.lexer.lineno, t.lexer.lexpos)
        
    #t[0] = PatternMatching(t[1], t[3], 'LIKE', t.lexer.lineno, t.lexer.lexpos) if t[2] == 'LIKE' else PatternMatching(t[1], t[3], 'NOT_LIKE', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_between(t):
    '''expre : expre BETWEEN expresion AND expresion
            | expre NOT BETWEEN expresion AND expresion
    '''

    if t[2] == "NOT":
        strGram = "<expre> ::= <expre> NOT BETWEEN <expresion> AND <expresion>"
        t[0] = Between.Between(t[1], t[4], t[6], "NOT", strGram, t.lexer.lineno, t.lexer.lexpos)

    else:
        strGram = "<expre> ::= <expre> BETWEEN <expresion> AND <expresion>"
        t[0] = Between.Between(t[1], t[3], t[5], "", strGram, t.lexer.lineno, t.lexer.lexpos)

    #t[0] = Between(t[1], t[3], t[5], 'BETWEEN', t.lexer.lineno, t.lexer.lexpos) if t[2] == 'LIKE' else Between(t[1], t[4], t[5], 'NOT_BETWEEN', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_in(t):
    '''expre : expre IN expre
            | expre NOT IN expre
    '''
    strGram = ""
    if t[2] == "NOT":
        strGram = "<expre> ::= <expre> NOT INT <expre>"
        t[0] = Relacional.Relacional(t[1], t[4], "NOT IN", strGram, t.lexer.lineno, t.lexer.lexpos)

    else: 
        strGram = "<expre> ::= <expre> IN <expre>"
        t[0] = Relacional.Relacional(t[1], t[3], "IN", strGram, t.lexer.lineno, t.lexer.lexpos)

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
        t[0] = Avg.Avg(t[3], Tipo(Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'COUNT':
        strGram = "<expre> ::= COUNT PARIZQ <expre> PARDER"
        t[0] = Count.Count(t[3], Tipo(Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'GREATEST':
        strGram = "<expre> ::= GREATEST PARIZQ <lcol> PARDER"
        t[0] = Greatest.Greatest(t[3], Tipo(Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'LEAST':
        strGram = "<expre> ::= LEAST PARIZQ <lcol> PARDER"
        t[0] = Least.Least(t[3], Tipo(Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'MAX':
        strGram = "<expre> ::= MAX PARIZQ <expre> PARDER"
        t[0] = Max.Max(t[3], Tipo(Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'MIN':
        strGram = "<expre> ::= MIN PARIZQ <expre> PARDER"
        t[0] = Min.Min(t[3], Tipo(Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SUM':
        strGram = "<expre> ::= MAX PARIZQ <expre> PARDER"
        t[0] = Sum.Sum(t[3], Tipo(Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'TOP':
        strGram = "<expre> ::= TOP PARIZQ <lcol> PARDER"
        t[0] = Top.Top(t[3], Tipo(Tipo_Dato.INTEGER), strGram,t.lexer.lineno, t.lexer.lexpos)
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
        t[0] = Abs.Abs(t[3], strGram,t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CBRT':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        t[0] = Cbrt.Cbrt(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CEIL':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        t[0] = Ceil.Ceil(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CEILING':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        t[0] = Ceiling.Ceiling(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'DEGREES':
        strGram = "<expre> :: = "+ t[1] +" PARIZQ <expre> PARDER"
        t[0] = Degrees.Degrees(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'DIV':
        strGram = "<expre> ::= DIV PARIZQ <expre> COMA <expre>  PARDER"
        t[0] = Div.Div(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'EXP':
        strGram = "<expre> ::= EXP PARIZQ <expre> PARDER"
        t[0] = Exp.Exp(t[3], Tipo(Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'FACTORIAL':
        strGram = "<expre> ::= FACTORIAL PARIZQ <expre> PARDER"
        t[0] = Factorial.Factorial(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'FLOOR':
        strGram = "<expre> ::= FLOOR PARIZQ <expre> PARDER"
        t[0] = Floor.Floor(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'GCD':
        strGram = "<expre> ::= GCD PARIZQ <expre> COMA <expre> PARDER"
        t[0] = Gcd.Gcd(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'LCM':
        strGram = "<expre> ::= LCM PARIZQ <expre> PARDER"
        t[0] = Lcm.Lcm(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'LN':
        strGram = "<expre> ::= LN PARIZQ <expre> PARDER"
        t[0] = Ln.Ln(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'LOG':
        strGram = "<expre> ::= LOG PARIZQ <expre> PARDER"
        t[0] = Log.Log(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'LOG10':
        strGram = "<expre> ::= LOG10 PARIZQ <expre> PARDER"
        t[0] = Log10.Log10(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'MIN_SCALE':
        strGram = "<expre> ::= MIN_SCALE PARIZQ <expre> PARDER"
        t[0] = MinScale.MinScale(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'MOD':
        strGram = "<expre> ::= MOD PARIZQ <expre> COMA <expre> PARDER"
        t[0] = Mod.Mod(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'PI':
        strGram = "PI PARIZQ PARDER "
        t[0] = PI.PI(strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'POWER':
        strGram = "<expre> ::= POWER PARIZQ <expre> COMA <expre> PARDER"
        t[0] = Power.Power(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'RADIANS':
        strGram = "<expre> ::= RADIANS PARIZQ <expre> PARDER "
        t[0] = Radians.Radians(t[3], strGram ,t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'RANDOM':
        strGram = "RANDOM PARIZQ PARDER"
        t[0] = Random.Random(strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ROUND':
        strGram = "<expre> ::= ROUND PARIZQ <expre> PARDER "
        t[0] = Round.Round(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SCALE':
        strGram = "<expre> ::= SCALE PARIZQ <expre> PARDER "
        t[0] = Scale.Scale(t[3], strGram ,t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SETSEED':
        strGram = "<expre> ::= SETSEED PARIZQ <expre> PARDER"
        t[0] = SetSeed.SetSeed(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SIGN':
        strGram = "<expre> ::= SIGN PARIZQ <expre> PARDER"
        t[0] = Sign.Sign(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SQRT':
        strGram = "<expre> ::= SQRT PARIZQ <expre> PARDER"
        t[0] = Sqrt.Sqrt(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TRIM_SCALE':
        strGram = "<expre> ::= TRIM_SCALE PARIZQ <expre> PARDER"
        t[0] = TrimScale.TrimScale(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TRUNC':
        strGram = "<expre> ::= TRUNC PARIZQ <expre> PARDER"
        t[0] = Trunc.Trunc(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'WIDTH_BUCKET':
        strGram = "<expre> ::= WIDTH_BUCKET PARIZQ <expresion> COMA <expresion> COMA <expresion> COMA <expresion> PARDER "
        t[0] = WidthBucket.WidthBucket(t[3], t[5], t[7], t[9], Tipo(Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos)

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
        t[0] = Convert.Convert(t[3], None, t[5], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'DECODE':
        strGram = "<expre> ::= DECODE PARIZQ <expre> PARDER"
        t[0] = Decode.Decode(t[3],  None, t[5],strGram,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'ENCODE':
        strGram = "<expre> ::= ENCODE PARIZQ <expre> PARDER"
        t[0] = Encode.Encode(t[3],  None, t[5], strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'GET_BYTE':
        strGram = "<expre> ::= GET_BYTE PARIZQ <expre> COMA ENTERO PARDER"
        t[0] = GetByte.GetByte(t[3], None,t[5], strGram,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'LENGTH':
        strGram = "<expre> ::= LENGTH PARIZQ <expre> PARDER"
        t[0] = Length.Length(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'MD5':
        strGram = "<expre> ::= MD5 PARIZQ <expre> PARDER"
        t[0] = Md5.Md5(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SET_BYTE':
        strGram = "<expre> ::= SET_BYTE PARIZQ <expre> COMA ENTERO COMA ENTERO PARDER"
        t[0] = SetByte.SetByte(t[3], None, t[5], t[7], strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SHA256':
        strGram = "<expre> ::= SHA256 PARIZQ <expre> PARDER"
        t[0] = Sha256.Sha256(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SUBSTR':
        strGram = "<expre> ::= SUBSTR PARIZQ <expre> COMA ENTERO COMA ENTERO PARDER"
        t[0] = Substring.Substring(t[3], t[5], t[7], None, strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SUBSTRING':
        strGram = "<expre> ::= SUBSTRING PARIZQ <expre> COMA ENTERO COMA ENTERO PARDER"
        t[0] = Substring.Substring(t[3], t[5], t[7], None, strGram, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'TRIM':
        strGram = "<expre> ::= TRIM PARIZQ <expre> PARDER"
        t[0] = Trim.Trim(t[3], None, strGram, t.lexer.lineno, t.lexer.lexpos)
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
    if t[1] == 'ACOS':
        t[0] = Acos.Acos(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ACOSD':
        t[0] = Acosd.Acosd(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ACOSH':
        t[0] = Acosh.Acosh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ASIN':
        t[0] = Asin.Asinh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ASIND':
        t[0] = Asind.Asind(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ASINH':
        t[0] = Asinh.Asinh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATAN':
        
        t[0] = Atan.Atan(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATAN2':
        strGram = "<expre> ::= ATAN2 PARIZQ <expre> COMA <expre> PARDER"
        t[0] = Atan2.Atan2(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATAN2D':
        strGram = "<expre> ::= ATAN2D PARIZQ <expre> COMA <expre> PARDER"
        t[0] = Atan2d.Atan2d(t[3], t[5], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATAND':
        t[0] = Atand.Atand(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATANH':
        t[0] = Atanh.Atanh(t[3], strGram,t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COS':
        t[0] = Cos.Cos(t[3], strGram,t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COSD':
        t[0] = Cosd.Cosd(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COSH':
        t[0] = Cosh.Cosh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COT':
        t[0] = Cot.Cot(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COTD':
        t[0] = Cotd.Cotd(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SIN':
        t[0] = Sin.Sin(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SIND':
        t[0] = Sind.Sind(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SINH':
        t[0] = Sinh.Sinh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TAN':
        t[0] = Tan.Tan(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TAND':
        t[0] = Tand.Tand(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TANH':
        t[0] = Tanh.Tanh(t[3], strGram, t.lexer.lineno, t.lexer.lexpos)
            
def p_operadores_otros(t):
    ''' expre : EXTRACT PARIZQ tiempo FROM TIMESTAMP CARACTER PARDER
            | NOW PARIZQ PARDER
            | DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER
            | CURRENT_DATE
            | CURRENT_TIME
            | TIMESTAMP CARACTER
            | CASE lcase END 
    '''
    if t[1] == 'EXTRACT':
        strGram = "<expre> ::= EXTRACT PARIZQ <tiempo> FROM TIMESTAMP CARACTER PARDER"
        t[0] = Extract.Extract(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'NOW':
        strGram = "<expre> ::= NOW PARIZQ PARDER"
        t[0] = Now.Now( strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'DATE_PART':
        strGram = "<expre> ::= DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER"
        t[0] = DatePart.DatePart(t[3], t[6], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CURRENT_DATE':
        strGram = "<expre> ::= CURRENT_DATE"
        t[0] = CurrentDate.CurrentDate(strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CURRENT_TIME':
        strGram = "<expre> ::= CURRENT_TIME"
        t[0] = CurrentTime.CurrentTime(strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TIMESTAMP':
        strGram = "<expre> ::= TIMESTAMP CARACTER"
        t[0] = TimeStamp.TimeStamp(t[2], strGram, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'POR':
        t[0] = 'Pendiente'
    elif t[1] == 'CASE':
        strGram = "<expre> ::= CASE <lcase> END "
        t[0] = Case.Case(t[2], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_operadores_parentesis(t):
    ''' expre : PARIZQ expre PARDER
            | PARIZQ query PARDER
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
    t[1].append(CColumna.Columna(t[3],t[4],t[5], strGram, t.lineno,t.lexpos))
    t[0] =t[1]

def p_campos_tablas1(t):
    '''campos : campos COMA ID tipo
    '''
    strGram = "<campos> ::= <campos> COMA ID tipo"
    t[1].append(CColumna.Columna(t[3],t[4],None,strGram,t.lineno,t.lexpos))
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
    t[1].append(Tipo_Constraint(None,Tipo_Dato_Constraint.UNIQUE,t[5]))
    t[0] = t[1]

def p_campos_tablas5(t):
    '''campos : campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
    '''
    strGram = "<campos> ::= <campos> COMA FOREIGN KEY PARIZQ <lista_id> PARDER REFERENCES ID PARIZQ <lista_id> PARDER"
    t[1].append(Tipo_Constraint(t[6],Tipo_Dato_Constraint.FOREIGN_KEY,Tipo_Constraint([9],Tipo_Dato_Constraint.REFERENCES,t[11])))
    t[0] = t[1]

def p_campos_tablas6(t):
    '''campos : campos COMA PRIMARY KEY PARIZQ lista_id PARDER
    '''
    t[1].append(Tipo_Constraint(None,Tipo_Dato_Constraint.PRIMARY_KEY,t[6]))
    t[0] = t[1]

def p_campos_tablas7(t):
    '''campos : ID tipo lista_op
    '''
    strGram = "<campos> ::= ID <tipo> <lista_op>"
    t[0] = [CColumna.Columna(t[1],t[2],t[3], strGram, t.lineno,t.lexpos)]

def p_campos_tablas8(t):
    '''campos : ID tipo
    '''
    strGram = "<campos> ::= ID <tipo>"
    t[0] = [CColumna.Columna(t[1],t[2],None,strGram,t.lineno,t.lexpos)]

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
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.PRIMARY_KEY, None)

def p_opcion1(t):
    '''opcion : REFERENCES ID PARIZQ lista_id PARDER
    '''
    t[0] = Tipo_Constraint(t[2], Tipo_Dato_Constraint.REFERENCES, t[4])

def p_opcion2(t):
    '''opcion : DEFAULT expresion
    '''
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.DEFAULT, t[2])

def p_opcion3(t):
    '''opcion : NOT NULL
    '''
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.NOT_NULL, None)

def p_opcion4(t):
    '''opcion : NULL
    '''
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.NULL, None)

def p_opcion5(t):
    '''opcion : UNIQUE
    '''
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.UNIQUE, None)

def p_opcion6(t):
    '''opcion : CONSTRAINT ID UNIQUE
    '''
    t[0] = Tipo_Constraint(t[2], Tipo_Dato_Constraint.UNIQUE, None)

def p_opcion7(t):
    '''opcion : CONSTRAINT ID CHECK expre
    '''
    t[0] = Tipo_Constraint(t[2], Tipo_Dato_Constraint.CHECK, t[4])

def p_opcion8(t):
    '''opcion : CHECK expre
    '''
    t[0] = Tipo_Constraint(None, Tipo_Dato_Constraint.CHECK, t[2])

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
    t[0] = Primitivo.Primitivo(t[1],Tipo(Tipo_Dato.TEXT), strGram, t.lexer.lineno, t.lexer.lexpos)

def p_expresion1(t):
    '''expresion : CARACTER
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= CARACTER"
    t[0] = Primitivo.Primitivo(t[1],Tipo(Tipo_Dato.CHAR), strGram, t.lexer.lineno, t.lexer.lexpos)

def p_expresion2(t):
    '''expresion : ENTERO
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ENTERO"
    t[0] = Primitivo.Primitivo(t[1], Tipo(Tipo_Dato.INTEGER), strGram, t.lexer.lineno, t.lexer.lexpos)
    
def p_expresion3(t):
    '''expresion : FDECIMAL
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= FDECIMAL"
    t[0] = Primitivo.Primitivo(t[1],Tipo(Tipo_Dato.NUMERIC), strGram, t.lexer.lineno, t.lexer.lexpos)

def p_expresion4(t):
    '''expresion : DOUBLE
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram +"<expresion> ::= DOUBLE"
    t[0] = Primitivo.Primitivo(t[1],Tipo(Tipo_Dato.DOUBLE_PRECISION), strGram, t.lexer.lineno, t.lexer.lexpos)

def p_expresion5(t):
    '''expresion : ID
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ID"
    #t[0] = Primitivo.Primitivo(t[1],Tipo_Dato.ID, t.lexer.lineno, t.lexer.lexpos)
    t[0] = Identificador(t[1], strGram, t.lexer.lineno, t.lexer.lexpos)

def p_expresion61(t):
    '''expresion : ID PUNTO ID
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ID PUNTO ID"
    t[0] = SelectLista.Alias(t[1],t[3])
    #t[0] = Primitivo.Primitivo(f"{t[1]}.{t[3]}",Tipo_Dato.ID, strGram,t.lexer.lineno, t.lexer.lexpos)

def p_expresion62(t):
    '''expresion : ID PUNTO POR
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ID PUNTO POR"
    t[0] = SelectLista.Alias(t[1],t[3])
    #t[0] = Primitivo.Primitivo(f"{t[1]}.{t[3]}",Tipo_Dato.ID, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_expresion7(t):
    '''expresion : ARROBA ID
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= ARROBA ID"
    t[0] = Primitivo.Primitivo(t[1],Tipo_Dato.ARROBA, strGram, t.lexer.lineno, t.lexer.lexpos)

def p_expresion8(t):
    '''expresion : ID PARIZQ lcol PARDER
    '''

def p_expresion9(t):
    '''expresion : TRUE
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= TRUE"
    t[0] = Primitivo.Primitivo(True,Tipo(Tipo_Dato.BOOLEAN), strGram, t.lexer.lineno, t.lexer.lexpos)

def p_expresion10(t):
    '''expresion : FALSE
    '''
    strGram = "<l_expresiones> ::= <l_expresiones> COMA <expre>\n"
    strGram = strGram + "<l_expresiones> ::= <expre>\n"
    strGram = strGram + "<expresion> ::= FALSE"
    t[0] = Primitivo.Primitivo(False,Tipo(Tipo_Dato.BOOLEAN), strGram, t.lexer.lineno, t.lexer.lexpos)

def p_lista_columas(t):
    '''lcol : lcol COMA expre
    '''
    #print("entro aqui 1")
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_columas1(t):
    '''lcol : lcol COMA expre nombre
    '''
    t[1].append(SelectLista.Alias(t[4],t[3]))
    t[0] = t[1]

def p_lista_columas2(t):
    '''lcol : lcol COMA expre AS nombre
    '''
    t[1].append(SelectLista.Alias(t[5],t[3]))
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
    t[0] = [SelectLista.Alias(t[2],t[1])]

def p_lista_columas5(t):
    '''lcol : expre AS nombre
    '''
    t[0] = [SelectLista.Alias(t[3],t[1])]

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
    t[0] = Tipo(Tipo_Dato.INTEGER)

def p_tipo_datos1(t):
    '''tipo : DATE
    '''
    t[0]=Tipo(Tipo_Dato.DATE)

# NO RECUERDO PARA QUE IMPLEMENTAMOS ESTA PARTE ENTONCES LA COMENTE
#def p_tipo_datos2(t):
#    '''tipo : ID PARIZQ ID PARDER
#    '''
#    t[0]=t[1]

def p_tipo_datos_varchar(t):
    '''tipo : VARCHAR PARIZQ ENTERO PARDER
    '''
    t[0] = Tipo(Tipo_Dato.VARCHAR,t[3])

def p_tipo_datos_varchar1(t):
    '''tipo : CHAR PARIZQ ENTERO PARDER
    '''
    t[0] = Tipo(Tipo_Dato.CHAR,t[3])

def p_tipo_datos_varchar2(t):
    '''tipo : CHARACTER VARYING PARIZQ ENTERO PARDER
    '''
    t[0]= Tipo(Tipo_Dato.VARYING,t[4])

def p_tipo_datos_varchar3(t):
    '''tipo : CHARACTER PARIZQ ENTERO PARDER
    '''
    t[0]= Tipo(Tipo_Dato.CHARACTER,t[3])

def p_tipo_datos_varchar4(t):
    '''tipo : TEXT
    '''
    t[0]=Tipo(Tipo_Dato.TEXT)

#ESTE NO SE CONTEMPLO EN LA GRAMATICA DE MAEDA
def p_tipo_datos_decimal(t):
    '''tipo : DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
    '''
    t[0]= Tipo(Tipo_Dato.DECIMAL,[t[3],t[5]])

#def p_tipo_datos_decimal1(t):
#    '''tipo : DOUBLE
#    '''
#    t[0] = Tipo(Tipo_Dato.DOUBLE_PRECISION)
    
def p_tipo_datos_decimal2(t):
    '''tipo : DECIMAL
    '''
    t[0]=Tipo(Tipo_Dato.DECIMAL)

#ESTE NO SE CONTEMPLO EN LA GRAMATICA
#def p_tipo_datos_decimal3(t):
#    '''tipo : FLOAT PARIZQ ENTERO COMA ENTERO PARDER
#    '''
#    t[0]= 

#HAY QUE VALIDAR ESTE, CREO QUE ESTA DEMAS ACA
#def p_tipo_datos_int(t):
#    '''tipo : ENTERO
#    '''
#    t[0]=Tipo(Tipo_Dato.INTEGER)

def p_tipo_datos_int1(t):
    '''tipo : SMALLINT
    '''
    t[0]=Tipo(Tipo_Dato.SMALLINT)

def p_tipo_datos_int2(t):
    '''tipo : INTEGER
    '''
    t[0]=Tipo(Tipo_Dato.INTEGER)

def p_tipo_datos_int3(t):
    '''tipo : BIGINT
    '''
    t[0]=Tipo(Tipo_Dato.BIGINT)

def p_tipo_datos_int4(t):
    '''tipo : NUMERIC
    '''
    t[0]=Tipo(Tipo_Dato.NUMERIC)

def p_tipo_datos_int5(t):
    '''tipo : REAL
    '''
    t[0]=Tipo(Tipo_Dato.REAL)

def p_tipo_datos_int6(t):
    '''tipo : DOUBLE PRECISION
    '''
    t[0]=Tipo(Tipo_Dato.DOUBLE_PRECISION)

def p_tipo_datos_int7(t):
    '''tipo : MONEY
    '''
    t[0]=Tipo(Tipo_Dato.MONEY)

def p_tipo_datos_int8(t):
    '''tipo : BOOLEAN
    '''
    t[0]=Tipo(Tipo_Dato.BOOLEAN)

def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP
    '''
    t[0]=Tipo(Tipo_Dato.TIMESTAMP)

def p_tipo_datos_date1(t):
    '''tipo : TIME
    '''
    t[0]=Tipo(Tipo_Dato.TIME)

def p_tipo_datos_date2(t):
    '''tipo : INTERVAL
    '''
    t[0]=Tipo(Tipo_Dato.INTERVAL)

def p_tipo_datos2(t):
    '''tipo : ID 
    '''
    t[0] = Tipo(Tipo_Dato.TIPOENUM)
    t[0].nombre = t[1]

#FIN DE LA GRAMATICA
reglas = []
optimizacion = []
pendiente = []
instrucciones2 = []

def p_init2(t):
    'init : instrucciones_generales' # gramática de optimización 3D
    global optimizacion
    cons = op_ast.ast_op(t[1])
    optimizacion.append(cons)

def p_inst_generales(t):
    '''instrucciones_generales  : instrucciones_generales encabezado'''
    arr1 = []
    arr1.append('encabezado')
    arr1.append(t[2])
    t[1].append(arr1)
    t[0] = t[1]

def p_inst_generales3(t):
    '''instrucciones_generales  : encabezado'''
    arr = []
    arr1 = []
    arr1.append('encabezado')
    arr1.append(t[1])

    arr.append(arr1)

    t[0] = arr

def p_inst_generales_ins(t):
    '''instrucciones_generales  : instrucciones_generales instruccion2'''
    t[1].append(t[2])
    t[0] = t[1]
    

def p_inst_generales_ins2(t):
    '''instrucciones_generales  : instruccion2'''
    arr = []
    arr.append(t[1])
    #print('Valor del arr -> ' + str(arr))
    t[0] = arr

def p_inst_generales1(t):
    '''instrucciones_generales : instrucciones_generales temporales'''
    arr1 = []
    arr1.append('encabezado')
    arr1.append(t[2])

    t[1].append(arr1)
    t[0] = t[1]

def p_inst_generales2(t):
    '''instrucciones_generales : temporales'''
    arr = []
    arr1 = []
    arr1.append('encabezado')
    arr1.append(t[1])
    arr.append(arr1)
    
    t[0] = arr

def p_encabezado(t):
    '''encabezado   : FROM GOTO IMPORT WITH_GOTO
                    | ARROBA WITH_GOTO DEF ID PARIZQ PARDER DOSP
                    | HEAP CORIZQ ENTERO CORDER
                    | STACK CORIZQ ENTERO CORDER
                    | H IGUAL ENTERO
                    | P IGUAL ENTERO'''
    global optimizacion


    n = ''

    if t[1] == 'HEAP':
        n = 'heap[' + str(t[3]) + ']'
    elif t[1] ==  'STACK':
        n = 'stack[' + str(t[3]) + ']'
    elif t[1] == 'H':
        n = 'H = ' + str(t[3])
    elif t[1] == 'P':
        n = 'P = ' + str(t[3])
    elif t[1] == 'FROM':
        n = 'from goto import with_goto'
    elif t[1] == '@':
        n = '@with_goto\ndef ' + str(t[4]) + '():'

    t[0] = n

def p_temporales(t):
    '''temporales   : temporales COMA TEMPORAL
                    | temporales COMA ID'''
    texto = str(t[1]) + ',' + str(t[3])
    t[0] = texto

def p_temporales1(t):
    '''temporales   : TEMPORAL
                    | ID'''
    
    t[0] = t[1]

def p_instruccion_2(t):
    '''instruccion2 : asignacion
                    | salto_incondicional
                    | salto_condicional
                    | salto'''

    t[0] = t[1]

def p_asignacion(t):
    '''asignacion   : literal IGUAL operacion_aritmetica'''
    if t[2] == "=":
        if t[3] == 'HEAP':
            print('HEAP')
        elif t[3] == 'STACK':
            print('STACK')
        else:
            arr = []
            arr.append('asignacion')
            arr.append(t[1])
            arr.append(t[3])
            arr.append(t.lexer.lineno)
            t[0] = arr
            #const = op.Aritmetica(t[1], t[3], t.lexer.lineno)
            #optimizacion.append(const)

def p_operacion_aritmetica(t):
    '''operacion_aritmetica : literal MAS literal
                            | literal MENOS literal
                            | literal POR literal
                            | literal DIVIDIDO literal
                            | literal MODULO literal'''
    arr = []
    if t[2] == '+':
        arr.append(t[1])
        arr.append('+')
        arr.append(t[3])
    elif t[2] == '-':
        arr.append(t[1])
        arr.append('-')
        arr.append(t[3])
    if t[2] == '*':
        arr.append(t[1])
        arr.append('*')
        arr.append(t[3])
    elif t[2] == '/':
        arr.append(t[1])
        arr.append('/')
        arr.append(t[3])
    elif t[2] == '%':
        arr.append(t[1])
        arr.append('%')
        arr.append(t[3])
    else:
        arr.append(t[1])
    t[0] = arr

def p_literal(t):
    '''literal  : TEMPORAL
                | FDECIMAL
                | ENTERO
                | ID
                | H
                | P
                | MENOS TEMPORAL
                | MENOS FDECIMAL
                | MENOS ENTERO'''

    #print('Entró a literal')

    if t[1] == 'MENOS':
        t[0] = '-' + t[2]
    else:
        t[0] = t[1]

def p_salto(t):
    '''salto : LABEL ETIQUETA'''
    #print('Entro a salto')
    arr = []
    arr.append('salto')
    arr.append(t[2])
    arr.append(t.lexer.lineno)
    #print(arr)
    t[0] = arr

def p_salto_incondicional(t):
    '''salto_incondicional : GOTO ETIQUETA'''
    #print('Entro a salto_incondicional')
    arr = []
    arr.append('sin')
    arr.append(t[2])
    arr.append(t.lexer.lineno)
    #print(arr)
    t[0] = arr

def p_salto_condicional(t):
    '''salto_condicional : IF PARIZQ operacion_relacional PARDER DOSP GOTO ETIQUETA'''
    #print('Entro a salto condicional')
    arr = []
    arr.append('sc')
    arr.append(t[3])
    arr.append(t[7])
    arr.append(t.lexer.lineno)
    #print(arr)
    t[0] = arr

def p_operacion_relacional(t):
    '''operacion_relacional : literal MAYORQ literal
                            | literal MENORQ literal
                            | literal IGUALIGUAL literal
                            | literal NOIGUAL literal
                            | literal MAYOR_IGUALQ literal
                            | literal MENOR_IGUALQ literal'''
    arr = []
    if t[2] == '>':
        arr.append(t[1])
        arr.append('>')
        arr.append(t[3])
    elif t[2] == '<':
        arr.append(t[1])
        arr.append('<')
        arr.append(t[3])
    if t[2] == '==':
        arr.append(t[1])
        arr.append('==')
        arr.append(t[3])
    elif t[2] == '!=':
        arr.append(t[1])
        arr.append('!=')
        arr.append(t[3])
    elif t[2] == '>=':
        arr.append(t[1])
        arr.append('>=')
        arr.append(t[3])
    elif t[2] == '<=':
        arr.append(t[1])
        arr.append('<=')
        arr.append(t[3])

    t[0] = arr

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
    columna=0
    lista_lexicos.clear()
    lexer.input("")
    lexer.lineno = 0
    print("inicio")
    return parser.parse(texto)

def reporte_optimizacion():
    f = open('Optimizacion.html', 'w')
    f.write("<html>")
    f.write("<body>")
    f.write("<table border=""1"" style=""width:100%""><tr><th>Regla</th><th>Anterior</th><th>Nuevo</th><th>Linea</th></tr>")

    reglas = r.Reglas.reglas

    for i in reglas:
        x = i.split(',')
        f.write("<tr><td align=""center""><font color=""black"">" + str(x[0]) + "<td align=""center""><font color=""black"">" + str(x[1]) + "</td><td align=""center""><font color=""black"">" + str(x[2]) + "</td><td align=""center""><font color=""black"">" + str(x[3]) + "</td></tr>" + '\n')

    f.write("</table>")
    f.write("</body>")
    f.write("</html>")
    f.close()

def optimizar(texto):
    lexer.input("")
    lexer.lineno = 0
    global optimizacion, reglas, pendiente
    optimizacion = []
    reglas = []
    pendiente = []
    parse = parser.parse(texto)
    #print('Optimizacion -> ' + str(len(optimizacion)))
    #vvmensaje = ''
    if len(optimizacion) > 0:
        
        for cons in optimizacion:
            cons.optimizacion() 

    reporte_optimizacion()
    
    f = open('c3d_optimizado.py', 'w')
    f.write(r.Reglas.optimizado)
    f.close()

    #print('Las reglas que se utilizaron fueron:\n' + str(reglas))
    #LIMPIAR VARIABLES
    columna=0
    #lista_lexicos.clear()
    #se limpia analisis lexico
    
    #se obtiene la acción de analisis sintactico
    return None
