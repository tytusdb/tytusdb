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
from Instrucciones.Expresiones import Aritmetica, Logica, Primitivo, Relacional
from Instrucciones.DateTimeTypes import Case , CurrentDate, CurrentTime, DatePart, Extract, Now, Por, TimeStamp

from Instrucciones.Sql_alter import AlterDatabase, AlterTable, AlterDBOwner, AlterTableAddColumn, AlterTableAddConstraintFK, Columna, AlterTableDropColumn, AlterTableAddConstraint, AlterTableAddFK, AlterTableAlterColumn, AlterTableDropConstraint, AlterTableAlterColumnType, AlterTableAddCheck
from Instrucciones.Sql_create import CreateDatabase, CreateFunction, CreateOrReplace, CreateTable, CreateType, Use, ShowDatabases,Set
from Instrucciones.Sql_declare import Declare
from Instrucciones.Sql_delete import DeleteTable
from Instrucciones.Sql_drop import DropDatabase, DropTable
from Instrucciones.Sql_insert import insertTable
from Instrucciones.Sql_Joins import Join, JoinFull, JoinInner, JoinLeft, JoinRight
from Instrucciones.Sql_select import GroupBy, Having, Limit, OrderBy, Select, Where, SelectLista
from Instrucciones.Sql_truncate import Truncate
from Instrucciones.Sql_update import UpdateTable
from Instrucciones.Sql_create import Columna as CColumna
from Instrucciones import Relaciones

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
    t[0] =CreateDatabase.CreateDatabase(t[4], None, t[3].valor, None, 1, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database2(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    t[0] =CreateDatabase.CreateDatabase(t[4],None,t[3].valor, t[7], 1, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database3(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO

    t[0] =CreateDatabase.CreateDatabase(t[4],None,t[3].valor, t[7], t[10], t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_database4(t):
    '''instruccion : CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    #                     ID    tipo  opcion ID2  ENTERO
    t[0] =CreateDatabase.CreateDatabase(t[4], None, t[3].valor, None, t[7], t.lexer.lineno, t.lexer.lexpos)

# CREATE OR REPLACE DATABASE
def p_instruccion_create_or_database1(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
    '''
    t[0] =CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, None, 1, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database2(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    t[0] =CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], 1, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database3(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] =CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], t[12], t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_or_database4(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] =CreateOrReplace.CreateOrReplace(t[6], None, t[5].valor, t[9], 1, t.lexer.lineno, t.lexer.lexpos)

def p_owner(t):
    '''cowner : ID
                | CARACTER
                | CADENA
    '''
    t[0] = t[1]

def p_if_not_exists(t):
    '''if_not_exists : IF NOT EXISTS
    '''
    t[0] = Primitivo.Primitivo("IF NOT EXISTS",Tipo_Dato.VARCHAR,t.lexer.lineno, t.lexer.lexpos)

def p_if_not_exists1(t):
    '''if_not_exists : 
    '''
    t[0] = Primitivo.Primitivo("NULL",Tipo_Dato.VARCHAR,t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create1(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER PUNTO_COMA
    '''
    t[0] =CreateTable.CreateTable(t[3], None, t[5], None, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create2(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA
    '''
    t[0] =CreateTable.CreateTable(t[3],None, t[5], t[9], t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_use(t):
    '''instruccion : USE ID PUNTO_COMA
    '''
    t[0] =Use.Use(t[2], t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_show_database1(t):
    '''instruccion : SHOW DATABASES PUNTO_COMA
    '''
    t[0] =ShowDatabases.ShowDatabases(None, None, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_show_database2(t):
    '''instruccion : SHOW DATABASES LIKE CARACTER PUNTO_COMA
    '''
    t[0] =ShowDatabases.ShowDatabases(t[4],None, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_create_enumerated_type(t):
    '''instruccion : CREATE TYPE ID AS ENUM PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    t[0] =CreateType.CreateType(t[3],None,t[7],t.lexer.lineno, t.lexer.lexpos)


def p_instruccion_truncate(t):
    '''instruccion : TRUNCATE TABLE ID PUNTO_COMA
    '''
    t[0] =Truncate.Truncate(t[3], None, t.lexer.lineno, t.lexer.lexpos)

# DROP DATABASE
def p_instruccion_drop_database1(t):
    '''instruccion : DROP DATABASE ID PUNTO_COMA

    '''
    t[0] =DropDatabase.DropDatabase(t[3],None,False,0,t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_drop_database2(t):
    '''instruccion : DROP DATABASE IF EXISTS ID PUNTO_COMA

    '''
    t[0] =DropDatabase.DropDatabase(t[5],None,True,1,t.lexer.lineno, t.lexer.lexpos)

# DROP TABLE
def p_instruccion_drop(t):
    '''instruccion : DROP TABLE ID PUNTO_COMA

    '''
    t[0] =DropTable.DropTable(t[3],None,t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_drop2(t):
    '''instruccion : DROP ID

    '''
    t[0] =DropTable.DropTable(t[2],None,t.lexer.lineno, t.lexer.lexpos)


def p_instruccion_where(t):
    '''
        instructionWhere :  WHERE expre
    '''
    t[0] = Where.Where(t[2],None,t.lexer.lineno, t.lexer.lexpos)


# update tabla set campo = valor , campo 2= valor where condicion

def p_instruccion_update(t):
    '''instruccion : UPDATE ID SET lcol instructionWhere PUNTO_COMA

    '''
    id1 = Identificador(t[2], t.lexer.lineno, t.lexer.lexpos)
    t[0] = UpdateTable.UpdateTable(id1, None, t[4], t[5], t.lexer.lineno, t.lexer.lexpos)

# DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
def p_columunas_delete(t):
    '''
     instruccion : DELETE FROM ID instructionWhere PUNTO_COMA
    '''
    t[0] = DeleteTable.DeleteTable(t[3],None, t[4], t.lexer.lineno, t.lexer.lexpos)

#FUNCIONES
def p_funciones(t):
    '''
     instruccion : CREATE FUNCTION ID BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = CreateFunction.CreateFunction(t[3],None, None, None, t[5], t.lexer.lineno, t.lexer.lexpos)

def p_funciones2(t):
    '''
     instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = CreateFunction.CreateFunction(t[3],None, t[5], None, t[8], t.lexer.lineno, t.lexer.lexpos)

def p_funciones3(t):
    '''
     instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER AS expresion BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = CreateFunction.CreateFunction(t[3],None, t[5], t[8], t[10], t.lexer.lineno, t.lexer.lexpos)


def p_declaracion(t):
    '''
     instruccion : DECLARE expresion AS expresion PUNTO_COMA
    '''
    t[0] = Declare.Declare(t[2], None, t[4], t.lexer.lineno, t.lexer.lexpos)

def p_declaracion1(t):
    '''
     instruccion : DECLARE expresion tipo PUNTO_COMA
    '''
    t[0] = Declare.Declare(t[2], t[3], None, t.lexer.lineno, t.lexer.lexpos)
    
def p_set(t):
    '''
     instruccion : SET expresion IGUAL expre PUNTO_COMA
    '''
    t[0] =Set.Set(t[2], None, t[4], t.lexer.lineno, t.lexer.lexpos)


# ALTER DATABASE name RENAME TO new_name
def p_instruccion_alter_database1(t):
    '''instruccion : ALTER DATABASE ID RENAME TO ID PUNTO_COMA
    '''
    t[0] = AlterDatabase.AlterDatabase(t[3], None, t[4], t[6], t.lexer.lineno, t.lexer.lexpos)


# ALTER DATABASE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
def p_instruccion_alter_database2(t):
    '''instruccion : ALTER DATABASE ID OWNER TO list_owner PUNTO_COMA
    '''
    t[0] = AlterDBOwner.AlterDBOwner(t[3], t[6], t.lexer.lineno, t.lexer.lexpos)


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
    t[0] = AlterTableAddColumn.AlterTableAddColumn(t[3], t[4], t.lexer.lineno, t.lexer.lexpos)

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
    'add_column : ADD COLUMN ID tipo'
    t[0] = Columna.Columna(t[3], t[4], t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;
def p_instruccion_alter2(t):
    '''instruccion : ALTER TABLE ID l_drop_column PUNTO_COMA
    '''
    t[0] = AlterTableDropColumn.AlterTableDropColumn(t[3], t[4], t.lexer.lineno, t.lexer.lexpos)

def p_l_drop_column1(t):
    'l_drop_column : l_drop_column COMA drop_column'
    t[1].append(t[3])
    t[0] = t[1]

def p_l_drop_column2(t):
    'l_drop_column : drop_column'
    t[0] = [t[1]]

def p_drop_column(t):
    'drop_column : DROP COLUMN ID'
    t[0] = Columna.Columna(t[3], None, t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CHECK EXP;
def p_instruccion_alter3(t):
    '''instruccion : ALTER TABLE ID ADD CHECK expre PUNTO_COMA
    '''
    t[0] = AlterTableAddCheck.AlterTableAddCheck(t[3],t[6],t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter4(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ lista_id PARDER PUNTO_COMA
    '''
    t[0] = AlterTableAddConstraint.AlterTableAddConstraint(t[3], t[6], t[9], t.lexer.lineno, t.lexer.lexpos)


def p_instruccion_altercfk(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    t[0] = AlterTableAddConstraintFK.AlterTableAddConstraintFK(t[3], t[6], t[10], t[13], t[15], t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE child_table ADD FOREIGN KEY (fk_columns) REFERENCES parent_table (parent_key_columns);
def p_instruccion_alter5(t):
    '''instruccion : ALTER TABLE ID ADD FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    t[0] = AlterTableAddFK.AlterTableAddFK(t[3], t[8], t[11], t[13], t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ALTER COLUMN 'NOMBRE' SET NOT NULL;
def p_instruccion_alter6(t):
    '''instruccion : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
    '''
    t[0] = AlterTableAlterColumn.AlterTableAlterColumn(t[3], t[6], t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' DROP CONSTRAINT 'NOMBRE';
def p_instruccion_alter7(t):
    '''instruccion : ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
    '''
    t[0] = AlterTableDropConstraint.AlterTableDropConstraint(t[3], t[6], t.lexer.lineno, t.lexer.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter8(t):
    '''instruccion : ALTER TABLE ID l_alter PUNTO_COMA
    '''
    t[0] = AlterTableAlterColumnType.AlterTableAlterColumnType(t[3], t[4], t.lexer.lineno, t.lexer.lexpos)

def p_l_alter1(t):
    'l_alter : l_alter COMA alter_column'
    t[1].append(t[3])
    t[0] = t[1]

def p_l_alter2(t):
    'l_alter : alter_column'
    t[0] = [t[1]]

def p_alter_column(t):
    'alter_column : ALTER COLUMN ID TYPE tipo'
    t[0] = Columna.Columna(t[3], t[5], t.lexer.lineno, t.lexer.lexpos)

# insert into tabla (campo1,campo2,campo3,campo4) values (valor1, valor2, valor3, valor4)
# unicamente validar que tengan los mismos campos y la mismas cantidad de valores

def p_instruccion_insert(t):
    '''instruccion : INSERT INTO ID PARIZQ lista_id PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    t[0] = insertTable.insertTable(t[3], None, t[5], t[9], t.lexer.lineno, t.lexer.lexpos)

#insert into tabla values (valor1,valor2,valor3)
# debe validar que la cantidad de valores coincida con la cantidad de columnas de la tabla y el tipo de dato
def p_instruccion_insert2(t):
    '''
    instruccion : INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    t[0] = insertTable.insertTable(t[3], None, None, t[6], t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = Relaciones.Relaciones(t[1],t[2],t[3],t.lexer.lineno, t.lexer.lexpos)

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
    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, None, None, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select1(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, t[6], t[7], t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select2(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, t[6], None, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select3(t):
    '''
    query : SELECT dist lcol FROM lcol linners 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], None, None, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, t.lexer.lineno, t.lexer.lexpos)


def p_instruccion_select4(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], t[7], t[8], t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select5(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    val = []
    val.append(Select.Select(t[2], t[3], t[5], t[6], t[7], None, t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_select6(t):
    '''
    query : SELECT dist lcol 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = SelectLista.SelectLista(t[3], t.lexer.lineno, t.lexer.lexpos)


def p_instruccion_select7(t):
    '''
    query   : SELECT dist lcol FROM lcol lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    val = []
    val.append(Select.Select(t[2], t[3], t[5], None, None, t[6], t.lexer.lineno, t.lexer.lexpos))
    t[0] = SelectLista.SelectLista(val, t.lexer.lineno, t.lexer.lexpos)

def p_lista_case(t):
    '''lcase : lcase case
    '''
    t[0] = t[1].append(t[2])

def p_lista_case(t):
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
        t[0] = OrderBy.OrderBy(t[3], None, t.lexer.lineno, t.lexer.lexpos)
    elif(t[1] == "GROUP"):
        t[0] = GroupBy.GroupBy(t[3], None, t.lexer.lineno, t.lexer.lexpos)
    elif(t[1] == "HAVING"):
        t[0] = Having.Having(t[2], None, t.lexer.lineno, t.lexer.lexpos)   
    elif(t[1] == "LIMIT"):
        #LIMIT(LIMITE,None,fila,columna)
        t[0] = Limit.Limit(t[2], None, t.lexer.lineno, t.lexer.lexpos)

def P_instruccion_row2(t):
    '''rows : LIMIT ENTERO OFFSET ENTERO'''
    #LIMIT(LIMITE,FILAS_A_EXCLUIR,fila,columna)
    t[0] = Limit.Limit(t[2], t[4], t.lexer.lineno, t.lexer.lexpos) 


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
    t[0] = Logica.Logica(t[1], t[3], t[2].upper(), t.lexer.lineno, t.lexer.lexpos)


def p_operadores_unarios(t):
    ''' expre : NOT expre
    '''
    t[0] = Logica.Logica(t[2], None, 'NOT', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_relacionales(t):
    ''' expre : expre IGUAL expre
            | expre MAYORQ expre
            | expre MENORQ expre
            | expre MAYOR_IGUALQ expre
            | expre MENOR_IGUALQ expre
            | expre DISTINTO expre
    '''
    t[0] = Relacional.Relacional(t[1], t[3], t[2], t.lexer.lineno, t.lexer.lexpos)

def p_operadores_aritmeticos(t):
    '''expre : expre MAS expre
            | expre MENOS expre
            | expre POR expre
            | expre DIVIDIDO expre
            | expre EXPONENCIACION expre
            | expre MODULO expre
    '''
    t[0] = Aritmetica.Aritmetica(t[1], t[3], t[2], t.lexer.lineno, t.lexer.lexpos)

def p_operador_unario(t):
    'expre : MENOS expre %prec UMENOS'
    t[0] = Aritmetica.Aritmetica(t[2], None, '-', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_like(t):
    '''expre : expre LIKE expre
            | expre NOT LIKE expre
    '''
    #t[0] = PatternMatching(t[1], t[3], 'LIKE', t.lexer.lineno, t.lexer.lexpos) if t[2] == 'LIKE' else PatternMatching(t[1], t[3], 'NOT_LIKE', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_between(t):
    '''expre : expre BETWEEN expresion AND expresion
            | expre NOT BETWEEN expresion AND expresion
    '''
    #t[0] = Between(t[1], t[3], t[5], 'BETWEEN', t.lexer.lineno, t.lexer.lexpos) if t[2] == 'LIKE' else Between(t[1], t[4], t[5], 'NOT_BETWEEN', t.lexer.lineno, t.lexer.lexpos)

def p_operadores_in(t):
    '''expre : expre IN lcol
            | expre NOT IN lcol
    '''

    #t[0] = In(t[1], t[4], t.lexer.lineno, t.lexer.lexpos)

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
        t[0] = Avg.Avg(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'COUNT':
        t[0] = Count.Count(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'GREATEST':
        t[0] = Greatest.Greatest(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'LEAST':
        t[0] = Least.Least(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'MAX':
        t[0] = Max.Max(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'MIN':
        t[0] = Min.Min(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SUM':
        t[0] = Sum.Sum(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'TOP':
        t[0] = Top.Top(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
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
        t[0] = Abs.Abs(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CBRT':
        t[0] = Cbrt.Cbrt(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CEIL':
        t[0] = Ceil.Ceil(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CEILING':
        t[0] = Ceiling.Ceiling(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'DEGREES':
        t[0] = Degrees.Degrees(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'DIV':
        t[0] = Div.Div(t[3], t[5], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'EXP':
        t[0] = Exp.Exp(t[3], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'FACTORIAL':
        t[0] = Factorial.Factorial(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'FLOOR':
        t[0] = Floor.Floor(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'GCD':
        t[0] = Gcd.Gcd(t[3], t[5], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'LCM':
        t[0] = Lcm.Lcm(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'LN':
        t[0] = Ln.Ln(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'LOG':
        t[0] = Log.Log(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'LOG10':
        t[0] = Log10.Log10(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'MIN_SCALE':
        t[0] = MinScale.MinScale(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'MOD':
        t[0] = Mod.Mod(t[3], t[5], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'PI':
        t[0] = PI.PI(t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'POWER':
        t[0] = Power.Power(t[3], t[5], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'RADIANS':
        t[0] = Radians.Radians(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'RANDOM':
        t[0] = Random.Random(t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ROUND':
        t[0] = Round.Round(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SCALE':
        t[0] = Scale.Scale(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SETSEED':
        t[0] = SetSeed.SetSeed(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SIGN':
        t[0] = Sign.Sign(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SQRT':
        t[0] = Sqrt.Sqrt(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TRIM_SCALE':
        t[0] = TrimScale.TrimScale(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TRUNC':
        t[0] = Trunc.Trunc(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'WIDTH_BUCKET':
        t[0] = WidthBucket.WidthBucket(t[3], t[5], t[7], t[9], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)

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
        t[0] = Convert.Convert(t[3], None, t[5], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'DECODE':
        t[0] = Decode.Decode(t[3],  None, t[5],t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'ENCODE':
        t[0] = Encode.Encode(t[3],  None, t[5], t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'GET_BYTE':
        t[0] = GetByte.GetByte(t[3], None,t[5],t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'LENGTH':
        t[0] = Length.Length(t[3], None,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'MD5':
        t[0] = Md5.Md5(t[3], None,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SET_BYTE':
        t[0] = SetByte.SetByte(t[3], None, t[5], t[7], t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SHA256':
        t[0] = Sha256.Sha256(t[3], None,t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SUBSTR':
        t[0] = Substring.Substring(t[3], t[5], t[7], None, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'SUBSTRING':
        t[0] = Substring.Substring(t[3], t[5], t[7], None, t.lexer.lineno, t.lexer.lexpos)
        pass
    elif t[1] == 'TRIM':
        t[0] = Trim.Trim(t[3], None, t.lexer.lineno, t.lexer.lexpos)
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
    if t[1] == 'ACOS':
        t[0] = Acos.Acos(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ACOSD':
        t[0] = Acosd.Acosd(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ACOSH':
        t[0] = Acosh.Acosh(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ASIN':
        t[0] = Asin.Asinh(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ASIND':
        t[0] = Asind.Asind(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ASINH':
        t[0] = Asinh.Asinh(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATAN':
        t[0] = Atan.Atan(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATAN2':
        t[0] = Atan2.Atan2(t[3], t[5], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATAN2D':
        t[0] = Atan2d.Atan2d(t[3], t[5], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATAND':
        t[0] = Atand.Atand(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'ATANH':
        t[0] = Atanh.Atanh(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COS':
        t[0] = Cos.Cos(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COSD':
        t[0] = Cosd.Cosd(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COSH':
        t[0] = Cosh.Cosh(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COT':
        t[0] = Cot.Cot(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'COTD':
        t[0] = Cotd.Cotd(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SIN':
        t[0] = Sin.Sin(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SIND':
        t[0] = Sind.Sind(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'SINH':
        t[0] = Sinh.Sinh(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TAN':
        t[0] = Tan.Tan(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TAND':
        t[0] = Tand.Tand(t[3], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TANH':
        t[0] = Tanh.Tanh(t[3], t.lexer.lineno, t.lexer.lexpos)
            
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
        t[0] = Extract.Extract(t[3], t[6], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'NOW':
        t[0] = Now.Now(t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'DATE_PART':
        t[0] = DatePart.DatePart(t[3], t[6], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CURRENT_DATE':
        t[0] = CurrentDate.CurrentDate(t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'CURRENT_TIME':
        t[0] = CurrentTime.CurrentTime(t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'TIMESTAMP':
        t[0] = TimeStamp.TimeStamp(t[2], t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'POR':
        t[0] = 'Pendiente'
    elif t[1] == 'CASE':
        t[0] = Case.Case(t[2], t.lexer.lineno, t.lexer.lexpos)

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
    t[1].append(CColumna.Columna(t[3],t[4],t[5],t.lineno,t.lexpos))
    t[0] =t[1]

def p_campos_tablas1(t):
    '''campos : campos COMA ID tipo
    '''
    t[1].append(CColumna.Columna(t[3],t[4],None,t.lineno,t.lexpos))
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
    t[1].append(Tipo_Constraint(None,Tipo_Dato_Constraint.UNIQUE,t[5]))
    t[0] = t[1]

def p_campos_tablas5(t):
    '''campos : campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
    '''
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
    t[0] = [CColumna.Columna(t[1],t[2],t[3],t.lineno,t.lexpos)]

def p_campos_tablas8(t):
    '''campos : ID tipo
    '''
    t[0] = [CColumna.Columna(t[1],t[2],None,t.lineno,t.lexpos)]

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
    t[0] = Primitivo.Primitivo(t[1],Tipo(Tipo_Dato.TEXT), t.lexer.lineno, t.lexer.lexpos)

def p_expresion1(t):
    '''expresion : CARACTER
    '''
    t[0] = Primitivo.Primitivo(t[1],Tipo(Tipo_Dato.CHAR), t.lexer.lineno, t.lexer.lexpos)
    

def p_expresion2(t):
    '''expresion : ENTERO
    '''
    t[0] = Primitivo.Primitivo(t[1], Tipo(Tipo_Dato.INTEGER), t.lexer.lineno, t.lexer.lexpos)
    
def p_expresion3(t):
    '''expresion : FDECIMAL
    '''
    t[0] = Primitivo.Primitivo(t[1],Tipo(Tipo_Dato.NUMERIC), t.lexer.lineno, t.lexer.lexpos)

def p_expresion4(t):
    '''expresion : DOUBLE
    '''
    t[0] = Primitivo.Primitivo(t[1],Tipo(Tipo_Dato.DOUBLE_PRECISION), t.lexer.lineno, t.lexer.lexpos)

def p_expresion5(t):
    '''expresion : ID
    '''
    #t[0] = Primitivo.Primitivo(t[1],Tipo_Dato.ID, t.lexer.lineno, t.lexer.lexpos)
    t[0] = Identificador(t[1], t.lexer.lineno, t.lexer.lexpos)

def p_expresion61(t):
    '''expresion : ID PUNTO ID
    '''
    t[0] = Primitivo.Primitivo(f"{t[1]}.{t[3]}",Tipo_Dato.ID, t.lexer.lineno, t.lexer.lexpos)

def p_expresion62(t):
    '''expresion : ID PUNTO POR
    '''
    t[0] = Primitivo.Primitivo(f"{t[1]}.{t[3]}",Tipo_Dato.ID, t.lexer.lineno, t.lexer.lexpos)


def p_expresion7(t):
    '''expresion : ARROBA ID
    '''
    t[0] = Primitivo.Primitivo(t[1],Tipo_Dato.ARROBA, t.lexer.lineno, t.lexer.lexpos)

def p_expresion8(t):
    '''expresion : ID PARIZQ lcol PARDER
    '''

def p_expresion9(t):
    '''expresion : TRUE
    '''
    t[0] = Primitivo.Primitivo(True,Tipo(Tipo_Dato.BOOLEAN), t.lexer.lineno, t.lexer.lexpos)

def p_expresion10(t):
    '''expresion : FALSE
    '''
    t[0] = Primitivo.Primitivo(False,Tipo(Tipo_Dato.BOOLEAN), t.lexer.lineno, t.lexer.lexpos)

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
    t[0]= Tipo(Tipo_Dato,[t[3],t[5]])

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


