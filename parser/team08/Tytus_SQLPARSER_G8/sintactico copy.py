#IMPORTS
from ply import *
import lexico
tokens= lexico.tokens


lista_lexicos=lexico.lista_errores_lexico
recolecion_analisis = []
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
    ('left', 'PARIZQ', 'PARDER')
   # ('right', 'UMENOS'),
)

# Definición de la gramática
def p_instrucciones_lista(t):
    '''instrucciones    :  instrucciones instruccion
                        | instruccion
                        '''

    
# CREATE DATABASE
def p_instruccion_create_database1(t):
    '''instruccion : CREATE DATABASE if_not_exists ID PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    t[0] = CreateDatabase(t[4], None, None, None, None, t.lineno, t.lexpos)

def p_instruccion_create_database2(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL ID PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    t[0] = CreateDatabase(t[4],None,t[5], t[7], None, t.lineno, t.lexpos)

def p_instruccion_create_database3(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    #                     ID  tipo  opcion ID2  ENTERO
    t[0] = CreateDatabase(t[4],None,t[5], t[6], t[10], t.lineno, t.lexpos)

def p_instruccion_create_database4(t):
    '''instruccion : CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    #                     ID    tipo  opcion ID2  ENTERO
    t[0] = CreateDatabase(t[4], None, t[5], None, t[7], t.lineno, t.lexpos)

# CREATE OR REPLACE DATABASE
def p_instruccion_create_or_database1(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
    '''
    t[0] = CreateOrReplace(t[6], None, None, None, t.lineno, t.lexpos)

def p_instruccion_create_or_database2(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL ID PUNTO_COMA
    '''
    t[0] = CreateOrReplace(t[6], t[7], t[9], None, t.lineno, t.lexpos)

def p_instruccion_create_or_database3(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] = CreateOrReplace(t[6], t[7], t[9], t[11], t.lineno, t.lexpos)

def p_instruccion_create_or_database4(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] = CreateOrReplace(t[6], t[7], None, t[9], t.lineno, t.lexpos)

def p_if_not_exists(t):
    '''if_not_exists : IF NOT EXISTS
            | 
    '''
    try:
        t[0] = t[1]
    except:
        #error
        pass

def p_instruccion_create1(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER PUNTO_COMA
    '''
    t[0] = CreateTable(t[3], t[5], None, t.lineno, t.lexpos)

def p_instruccion_create2(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA
    '''
    t[0] = CreateTable(t[3], t[5], t[9], t.lineno, t.lexpos)

def p_instruccion_use(t):
    '''instruccion : USE ID PUNTO_COMA
    '''
    t[0] = Use(t[3], None, t.lineno, t.lexpos)

def p_instruccion_show_database1(t):
    '''instruccion : SHOW DATABASES PUNTO_COMA
    '''
    t[0] = ShowDatabases(None, None, t.lineno, t.lexpos)

def p_instruccion_show_database2(t):
    '''instruccion : SHOW DATABASES LIKE CARACTER PUNTO_COMA
    '''
    t[0] = ShowDatabases(t[3],None,t.lineno, t.lexpos)

def p_instruccion_create_enumerated_type(t):
    '''instruccion : CREATE TYPE ID AS ENUM PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    t[0] = CreateType(t[3],None,t[7],t.lineno, t.lexpos)


def p_instruccion_truncate(t):
    '''instruccion : TRUNCATE TABLE ID PUNTO_COMA
    '''
    t[0] = TruncateTable(t[3], None, t.lineno, t.lexpos)

# DROP DATABASE
def p_instruccion_drop_database1(t):
    '''instruccion : DROP DATABASE ID PUNTO_COMA

    '''
    t[0] = DropDatabase(t[3],None,0,t.lineno, t.lexpos)

def p_instruccion_drop_database2(t):
    '''instruccion : DROP DATABASE IF EXISTS ID PUNTO_COMA

    '''
    t[0] = DropDatabase(t[5],None,1,t.lineno, t.lexpos)

# DROP TABLE
def p_instruccion_drop(t):
    '''instruccion : DROP TABLE ID PUNTO_COMA
    '''
    t[0] = DropTable(t[3],None,t.lineno, t.lexpos)

def p_instruccion_drop2(t):
    '''instruccion : DROP ID

    '''
    t[0] = Drop(t[2],None,t.lineno, t.lexpos)


def p_instruccion_where(t):
    '''
        instructionWhere :  WHERE expre
    '''
    t[0] = Where(t[2],None,t.lineno, t.lexpos)


# update tabla set campo = valor , campo 2= valor where condicion

def p_instruccion_update(t):
    '''instruccion : UPDATE ID SET l_columnas instructionWhere PUNTO_COMA

    '''
    t[0] = Update(t[2],None, t[4], t[5], t.lineno, t.lexpos)

# DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
def p_columunas_delete(t):
    '''
     instruccion : DELETE FROM ID instructionWhere PUNTO_COMA
    '''
    t[0] = Delete(t[3],None, t[4], t.lineno, t.lexpos)

#FUNCIONES
def p_funciones(t):
    '''
     instruccion : CREATE FUNCTION ID BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = CreateFunction(t[3],None, t[5], None, None, t.lineno, t.lexpos)

def p_funciones2(t):
    '''
     instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = CreateFunction(t[3],None, t[5], None, t[8], t.lineno, t.lexpos)


def p_funciones3(t):
    '''
     instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER AS expresion BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = CreateFunction(t[3],None, t[5], t[8], t[10], t.lineno, t.lexpos)

def p_declaracion(t):
    '''
     instruccion : DECLARE expresion AS expresion PUNTO_COMA
    '''
    t[0] = Declare(t[2], None, t[4], t.lineno, t.lexpos)

def p_declaracion1(t):
    '''
     instruccion : DECLARE expresion tipo PUNTO_COMA
    '''
    t[0] = Declare(t[2], t[3], None, t.lineno, t.lexpos)
    
def p_set(t):
    '''
     instruccion : SET expresion IGUAL expre PUNTO_COMA
    '''
    t[0] = Set(t[2], None, t[4], t.lineno, t.lexpos)

def p_columunas_actualizar(t):
    '''
    l_columnas : l_columnas COMA expre
    '''
    t[0] = t[1].append(t[3])

def p_columunas_actualizar1(t):
    '''
    l_columnas : expre
    '''
    t[0] = t[1]

# ALTER TABLE 'NOMBRE_TABLA' ADD NUEVO_CAMPO INT;
# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;

def p_instruccion_alter(t):
    '''instruccion : ALTER TABLE ID ADD ID tipo PUNTO_COMA'''
    t[0] = AlterTable(t[3], t[6], t[4], t[5], None, None, t.lineno, t.lexpos)

# ALTER DATABASE name RENAME TO new_name
def p_instruccion_alter_database1(t):
    '''instruccion : ALTER DATABASE ID RENAME TO ID PUNTO_COMA
    '''
    t[0] = AlterDatabase(t[3], None, t[4], t[6], t.lineno, t.lexpos)

# ALTER DATABASE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
def p_instruccion_alter_database2(t):
    '''instruccion : ALTER DATABASE ID OWNER TO list_owner PUNTO_COMA
    '''
    t[0] = AlterDatabase(t[3], None, t[4], t[6], t.lineno, t.lexpos)


# { new_owner | CURRENT_USER | SESSION_USER }
def p_list_owner(t):
    '''list_owner : ID
                | CURRENT_USER
                | SESSION_USER
    '''
    t[0] = t[1]

# ALTER TABLE 'NOMBRE_TABLA' ADD COLUMN NOMBRE_COLUMNA TIPO;
def p_instruccion_alter1(t):
    '''instruccion : ALTER TABLE ID ADD COLUMN ID tipo PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[6], None, None, t.lineno, t.lexpos)


# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;
def p_instruccion_alter2(t):
    '''instruccion : ALTER TABLE ID DROP COLUMN ID PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[6], None, None, t.lineno, t.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter3(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ lista_id PARDER PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[6], t[9], None, t.lineno, t.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter4(t):
    '''instruccion : ALTER TABLE ID ADD FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[11], t[8], t[13], t.lineno, t.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ALTER COLUMN 'NOMBRE' SET NOT NULL;
def p_instruccion_alter5(t):
    '''instruccion : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[6], None, None, t.lineno, t.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' DROP CONSTRAINT 'NOMBRE';
def p_instruccion_alter6(t):
    '''instruccion : ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[6], None, None, t.lineno, t.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CHECK EXP;
def p_instruccion_alter7(t):
    '''instruccion : ALTER TABLE ID ADD CHECK expre PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[6], None, None, t.lineno, t.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter8(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID CHECK expre PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[6], None, None, t.lineno, t.lexpos)

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter9(t):
    '''instruccion : ALTER TABLE ID RENAME COLUMN ID TO ID PUNTO_COMA
    '''
    t[0] = AlterTable(t[3], None, t[4], t[6], None, None, t.lineno, t.lexpos)


# insert into tabla (campo1,campo2,campo3,campo4) values (valor1, valor2, valor3, valor4)
# unicamente validar que tengan los mismos campos y la mismas cantidad de valores

def p_instruccion_insert(t):
    '''instruccion : INSERT INTO ID PARIZQ lcol PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA

    '''
    t[0] = InsertTable(t[3], None, t[5], t[9], t.lineno, t.lexpos)

#insert into tabla values (valor1,valor2,valor3)
# debe validar que la cantidad de valores coincida con la cantidad de columnas de la tabla y el tipo de dato
def p_instruccion_insert2(t):
    '''instruccion : INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA

    '''
    t[0] = InsertTable(t[3], None, None, t[6], t.lineno, t.lexpos)

# SELECT col, col FROM id;
# SELECT * from id;
def p_instruccion_query(t):
    '''
    instruccion : lquery PUNTO_COMA
    '''
    t[0]=t[1]

def p_lista_querys(t):
    '''lquery : lquery relaciones query
                | query
    '''

def p_tipo_relaciones(t):
    '''
        relaciones : UNION  
                | UNION ALL 
                | INTERSECT
                | INTERSECT ALL 
                | EXCEPT ALL 
                | EXCEPT
    '''
    t[0] = t[1]

def p_instruccion_select(t):
    '''
    query : SELECT dist lcol FROM lcol 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = Select(t[2], None, t[3], t[5], None, None, None, t.lineno, t.lexpos)

def p_instruccion_select1(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = Select(t[2], None, t[3], t[5], None, t[7], t[8], t.lineno, t.lexpos)

def p_instruccion_select2(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = Select(t[2], None, t[3], t[5], None, t[7], None, t.lineno, t.lexpos)

def p_instruccion_select3(t):
    '''
    query : SELECT dist lcol FROM lcol linners 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = Select(t[2], None, t[3], t[5], t[6], None, None, t.lineno, t.lexpos)


def p_instruccion_select4(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = Select(t[2], None, t[3], t[5], t[6], t[7], t[8], t.lineno, t.lexpos)

def p_instruccion_select5(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = Select(t[2], None, t[3], t[5], t[6], t[7], None, t.lineno, t.lexpos)

def p_instruccion_select6(t):
    '''
    query : SELECT dist lcol 
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = Select(t[2], None, t[3], None, None, None, None, t.lineno, t.lexpos)

def p_lista_case(t):
    '''lcase : lcase case
        | case
    '''

def p_instruccion_case(t):
    '''
    case    : WHEN expre THEN expre
            | ELSE expre
    '''
    print(t[1], " - ", t[2])



def p_instruccion_select7(t):
    '''
    query   : SELECT dist lcol FROM lcol lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = Select(t[2], None, t[3], t[5], None, None, None, t.lineno, t.lexpos)



def p_instruccion_lrows(t):
    '''lrows : lrows rows
             | rows
    '''

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
    rows    : ORDER BY lista_order
            | GROUP BY l_expresiones
            | HAVING lcol
            | LIMIT l_expresiones OFFSET expre
            | LIMIT l_expresiones
    '''
    t[0] = OrderBy(t[3], None, t.lineno, t.lexpos)
    t[0] = GroupBy(t[3], None, t.lineno, t.lexpos)
    t[0] = Having(t[2], None, t.lineno, t.lexpos)
    t[0] = Limit(t[2], None, t[4], t.lineno, t.lexpos)
    t[0] = Limit(t[2], None, None, t.lineno, t.lexpos)

def p_lista_order(t):
    '''lista_order : lista_order COMA order_op
        | order_op
    '''

def p_order_op(t):
    '''order_op : expre
            | expre DESC
            | expre ASC
            | expre NULLS FIRST
            | expre NULLS LAST
    '''

def p_linner_join(t):
    '''linners : linners inners
                | inners
    '''
def p_inner_join(t):
    '''
    inners : INNER JOIN expre ON expre
            | LEFT JOIN expre ON expre
            | FULL OUTER JOIN expre ON expre
            | JOIN expre ON expre
            | RIGHT JOIN expre ON expre
    '''
    t[0] = JoinInner(t[3], None, t[5], t.lineno, t.lexpos)
    t[0] = JoinLeft(t[3], None, t[5], t.lineno, t.lexpos)
    t[0] = JoinFull(t[4], None, t[6], t.lineno, t.lexpos)
    t[0] = JoinOuter(t[2], None, t[4], t.lineno, t.lexpos)
    t[0] = JoinRight(t[3], None, t[5], t.lineno, t.lexpos)

def p_operadores_logicos(t):
    ''' expre : expre OR expre
            | expre AND expre
            | NOT expre
            | expre IGUAL expre
            | expre MAYORQ expre
            | expre MENORQ expre
            | expre MAYOR_IGUALQ expre
            | expre MENOR_IGUALQ expre
            | expre DISTINTO expre
            | expre MAS expre
            | expre MENOS expre
            | expre POR expre
            | expre EXPONENCIACION expre
            | expre MODULO expre
            | expre LIKE expre
            | expre NOT LIKE expre
            | expre BETWEEN expresion AND expresion
            | expre NOT BETWEEN expresion AND expresion
            | expre IN PARIZQ lcol PARDER
            | expre IS NULL
            | expre IS NOT NULL
            | expre IS DISTINCT FROM expre
            | expre IS NOT DISTINCT FROM expre
            | MIN PARIZQ expre PARDER
            | MAX PARIZQ expre PARDER
            | SUM PARIZQ expre PARDER
            | AVG PARIZQ expre PARDER
            | COUNT PARIZQ expre PARDER
            | TOP PARIZQ expre PARDER
            | ABS PARIZQ expre PARDER 
            | CBRT PARIZQ expre PARDER 
            | CEIL PARIZQ expre PARDER 
            | CEILING PARIZQ expre PARDER 
            | DEGREES PARIZQ expre PARDER 
            | DIV PARIZQ expre PARDER
            | EXP PARIZQ expre PARDER 
            | FACTORIAL PARIZQ expre PARDER 
            | FLOOR PARIZQ expre PARDER 
            | GCD PARIZQ expre PARDER
            | LCM PARIZQ expre PARDER 
            | LN PARIZQ expre PARDER 
            | LOG PARIZQ expre PARDER 
            | LOG10 PARIZQ expre PARDER 
            | MIN_SCALE PARIZQ expre PARDER
            | MOD PARIZQ expre PARDER 
            | PI PARIZQ expre PARDER 
            | POWER PARIZQ expre PARDER 
            | RADIANS PARIZQ expre PARDER 
            | ROUND PARIZQ expre PARDER 
            | SCALE PARIZQ expre PARDER 
            | SIGN PARIZQ expre PARDER
            | SQRT PARIZQ expre PARDER 
            | TRIM_SCALE PARIZQ expre PARDER 
            | TRUNC PARIZQ expre PARDER 
            | WIDTH_BUCKET PARIZQ expre PARDER 
            | RANDOM PARIZQ expre PARDER 
            | SETSEED PARIZQ expre PARDER
            | LENGTH PARIZQ expre PARDER
            | SUBSTRING PARIZQ lcol PARDER
            | TRIM PARIZQ expre PARDER
            | GET_BYTE PARIZQ lcol PARDER
            | MD5 PARIZQ lcol PARDER
            | SET_BYTE PARIZQ lcol PARDER
            | SHA256 PARIZQ lcol PARDER
            | SUBSTR PARIZQ lcol PARDER
            | CONVERT PARIZQ lcol PARDER
            | ENCODE PARIZQ expre PARDER
            | DECODE PARIZQ expre PARDER
            | ACOS PARIZQ expre PARDER
            | ACOSD PARIZQ expre PARDER
            | ASIND PARIZQ expre PARDER
            | ATAN PARIZQ expre PARDER
            | ATAND PARIZQ expre PARDER
            | ATAN2 PARIZQ expre PARDER
            | ATAN2D PARIZQ expre PARDER
            | COS PARIZQ expre PARDER
            | COSD PARIZQ expre PARDER
            | COT PARIZQ expre PARDER
            | COTD PARIZQ expre PARDER
            | SIN PARIZQ expre PARDER
            | SIND PARIZQ expre PARDER
            | TAN PARIZQ expre PARDER
            | TAND PARIZQ expre PARDER
            | SINH PARIZQ expre PARDER
            | COSH PARIZQ expre PARDER
            | TANH PARIZQ expre PARDER
            | ASINH PARIZQ expre PARDER
            | ACOSH PARIZQ expre PARDER
            | ATANH PARIZQ expre PARDER
            | LEAST PARIZQ lcol PARDER
            | GREATEST PARIZQ lcol PARDER
            | EXTRACT PARIZQ tiempo FROM TIMESTAMP CARACTER PARDER
            | NOW PARIZQ PARDER
            | DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER
            | CURRENT_DATE
            | CURRENT_TIME
            | TIMESTAMP CARACTER
            | POR
            | CASE lcase END 
            | PARIZQ expre PARDER
            | PARIZQ query PARDER
    '''


def p_tiempo(t):
    ''' tiempo :  YEAR
                | MONTH
                | DAY
                | HOUR
                | MINUTE
                | SECOND
    '''


def p_operadores_logicos5(t):
    ''' expre :  expresion
    '''


def p_campos_tablas(t):
    '''campos : campos COMA ID tipo lista_op
            | campos COMA ID tipo
            | campos COMA CHECK expre
            | campos COMA CONSTRAINT ID CHECK expre
            | campos COMA UNIQUE PARIZQ lista_id PARDER
            | campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
            | campos COMA PRIMARY KEY PARIZQ lista_id PARDER
            | ID tipo lista_op
            | ID tipo
    '''

def p_lista_id(t):
    '''lista_id : lista_id COMA ID
            | ID
    '''

def p_lista_op(t):
    '''lista_op : lista_op opcion
             | opcion
    '''

def p_opcion(t):
    '''opcion : PRIMARY KEY
            | REFERENCES ID
            | DEFAULT expresion
            | NOT NULL
            | NULL
            | UNIQUE
            | CONSTRAINT ID UNIQUE
            | CONSTRAINT ID CHECK expre
            | CHECK expre
    '''

def p_lista_expresiones(t):
    '''
    l_expresiones : l_expresiones COMA expresion
                  | expresion

    '''

def p_expresion(t):
    '''
    expresion : CADENA
                | CARACTER
                | ENTERO
                | FDECIMAL
                | DOUBLE
                | ID
                | ID PUNTO ID
                | ARROBA ID
                | ID PARIZQ lcol PARDER
    '''
    t[0]=expresion(t[1],Tipo_Dato.CADENA,t.lineno,t.lexpos)
    t[0]=expresion(t[1],Tipo_Dato.CARACTER,t.lineno,t.lexpos)
    t[0]=expresion(t[1],Tipo_Dato.ENTERO,t.lineno,t.lexpos)
    t[0]=expresion(t[1],Tipo_Dato.FDECIMAL,t.lineno,t.lexpos)
    t[0]=expresion(t[1],Tipo_Dato.DOUBLE,t.lineno,t.lexpos)
    t[0]=expresion(t[1],Tipo_Dato.ID,t.lineno,t.lexpos)
    t[0]=expresion(t[1],t[2],Tipo_Dato.ID,t.lineno,t.lexpos)
    t[0]=expresion(t[1],Tipo_Dato.ARROBA,t.lineno,t.lexpos)

def p_lista_columas(t):
    '''lcol : lcol COMA expre
        | lcol COMA expre ID
        | lcol COMA expre AS ID
        | expre
        | expre ID
        | expre AS ID
    '''

#----------------------TIPO DE DATOS---------------------------------
def p_tipo_datos(t):
    '''tipo : INT
            | DATE
            | ID PARIZQ ID PARDER
    '''
    t[0]=Tipo(Tipo_Dato.INT,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.DATE,t.lineno,t.lexpos)

def p_tipo_datos1(t):
    '''tipo : VARCHAR PARIZQ ENTERO PARDER
            | CHAR PARIZQ ENTERO PARDER
            | CHARACTER VARYING PARIZQ ENTERO PARDER
            | CHARACTER PARIZQ ENTERO PARDER
            | TEXT

    '''
    t[0]=t[1]

def p_tipo_datos2(t):
    '''tipo : DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
             | DOUBLE
             | DECIMAL
             | ENTERO
             | FLOAT PARIZQ ENTERO COMA ENTERO PARDER
    '''
    t[0]=t[1]

def p_tipo_datos3(t):
    '''tipo : SMALLINT
             | INTEGER
             | BIGINT
             | NUMERIC
             | REAL
             | DOUBLE PRECISION
             | MONEY
             | BOOLEAN
    '''
    t[0]=Tipo(Tipo_Dato.SMALLINT,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.INTEGER,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.BIGINT,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.NUMERIC,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.REAL,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.BOOLEAN,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.MONEY,t.lineno,t.lexpos)

def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP
             | TIME
             | INTERVAL
    '''
    t[0]=Tipo(Tipo_Dato.TIMESPACE,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.TIME,t.lineno,t.lexpos)
    t[0]=Tipo(Tipo_Dato.INTERVAL,t.lineno,t.lexpos)

#FIN DE LA GRAMATICA

#def p_error(t):
#    print("Error sintáctico en '%s'" % t.value)

# MODO PANICO ***************************************
def p_error(p):
    print("Error sintáctico en ", p.value, " linea: ", str(p.lexer.lineno))
    print(lexico.columas(lexico.columna))
    if not p:
        print("Fin del Archivo!")
        return
    # Read ahead looking for a closing '}'
    while True:
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PUNTO_COMA':
            if not tok:
                print("FIN DEL ARCHIVO")
            else:
                print("Se recupero con ;")
            break

    parser.restart()


parser = yacc.yacc()

def ejecutar_analisis(texto):
    #LIMPIAR VARIABLES
    lexico.columna=0
    lista_lexicos.clear()
    #se limpia analisis lexico
    lexico.lexer.input("")
    lexico.lexer.lineno = 0
    #se obtiene la acción de analisis sintactico
    parser.parse(texto)
    print("inicio")





    return recolecion_analisis


