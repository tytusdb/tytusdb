import ply.yacc as yacc
from reporteErrores.errorReport import ErrorReport
from reporteErrores.instance import listaErrores 
from astDML import UpdateTable,InsertTable,DeleteTabla
from lexicosql import tokens
from astExpresion import ExpresionComparacion, ExpresionLogica, ExpresionNegativa, ExpresionNumero, BETWEEN,ExpresionPositiva, ExpresionBetween, OPERACION_LOGICA, OPERACION_RELACIONAL, TIPO_DE_DATO, ExpresionAritmetica, OPERACION_ARITMETICA,ExpresionNegada,ExpresionUnariaIs,OPERACION_UNARIA_IS, ExpresionBinariaIs, OPERACION_BINARIA_IS
from astExpresion import ExpresionCadena, ExpresionID ,ExpresionBooleano , ExpresionAgrupacion
from astFunciones import FuncionCadena, FuncionNumerica, FuncionTime , BitwaseBinaria , BitwaseUnaria
from astDDL import ALTER_TABLE_ADD, ALTER_TABLE_DROP, AlterDatabase, AlterField, AlterTable, AlterTableAdd, AlterTableDrop, CONSTRAINT_FIELD, CheckField, CheckMultipleFields, ConstraintField, ConstraintMultipleFields, CreateDatabase, CreateField, CreateTable, CreateType, DefaultField, DropDatabase, DropTable, ForeignKeyField, ForeignKeyMultipleFields, ShowDatabase, TYPE_COLUMN
from astUse import Use
from arbol import Arbol
from reporteBnf.reporteBnf import bnf 
from reporteErrores.errorReport import ErrorReport
from astSelect import SelectSimple, SelectFrom, ITEM_ALIAS , SelectFilter , SelectFromWhere, WHERE,COMBINE_QUERYS, combineQuery
#_______________________________________________________________________________________________________________________________
#                                                          PARSER
#_______________________________________________________________________________________________________________________________

#---------------- MANEJO DE LA PRECEDENCIA
precedence = (
    ('left','IS','ISNULL','NOTNULL','FROM' , 'SYMMETRIC','NOTBETWEEN','NOT_IN'),
    ('left', 'NOT'),# me da duda que sea a la izquierda :v 
    ('left','AND','OR','AMPERSAND' ,'NUMERAL' ,'PIPE','CORRIMIENTO_DER','CORRIMIENTO_IZQ','DOBLE_PIPE'), # le deje esta precedencia porque postgress asi trabaja estos simbolos << >>  & | ||  
    ('left','IGUAL','DIFERENTE','DIFERENTE2','MENOR','MAYOR','MENORIGUAL','MAYORIGUAL'),
    ('left','BETWEEN','IN','LIKE','ILIKE','SIMILAR'),
    ('left','MAS','MENOS'),
    ('left','ASTERISCO','DIVISION','MODULO'),
    ('right','UMENOS','UMAS','BITWISE_NOT' , 'UNOT' ),
    ('left', 'EXPONENT')
)

def p_init(p):
    'init : instrucciones'
    bnf.addProduccion('\<init> ::= \<instrucciones>')
    p[0] = Arbol(p[1])
    

def p_instrucciones_list(p):
    '''instrucciones    : instrucciones instruccion '''
    p[1].append(p[2])
    p[0] = p[1]
    bnf.addProduccion('\<instrucciones> ::= \<instrucciones> \<instruccion>')

def p_instrucciones_instruccion(p):
    'instrucciones  :   instruccion'
    p[0] = [p[1]]
    bnf.addProduccion('\<instrucciones> ::= \<instruccion>')


def p_instruccion1(p):
    '''instruccion :  sentenciaUpdate   PTCOMA '''
    p[0] = p[1]
    bnf.addProduccion('\<instruccion> ::= \<update> "." ')

def p_instruccion2(p):
    'instruccion : sentenciaDelete   PTCOMA '
    p[0] = p[1]
    bnf.addProduccion('\<instruccion> ::= \<delete> "." ')

def p_instruccion3(p):
    'instruccion : insert   PTCOMA '
    p[0] = p[1]
    bnf.addProduccion('\<instruccion> ::= \<insert> "." ')
    
def p_instruccion4(p):
    'instruccion : definicion  PTCOMA '
    p[0] = p[1]
    bnf.addProduccion('\<instruccion> ::= \<definicion> "."')

def p_instruccion5(p):
    '''instruccion : alter_table       PTCOMA	'''
    p[0] = p[1]
    bnf.addProduccion('\<instruccion> ::= \<alter_table> "." ')                    

def p_instruccion6(p):
    'instruccion : combine_querys    PTCOMA '
    p[0] = p[1]
    bnf.addProduccion('\<instruccion> ::= \<combine_querys> "." ') 

def p_instruccion7(p):
    'instruccion : use PTCOMA '
    p[0] = p[1]
    bnf.addProduccion('\<instruccion> ::= \<use> "." ') 

# def p_instruccion8(p):
#     'instruccion : select PTCOMA '
#     p[0] = p[1]
#     bnf.addProduccion('\<instruccion> ::= \<use> "." ') 
    
def p_use(p):
    'use : USE ID'
    p[0] = Use(p[2], p.slice[2].lineno)
    bnf.addProduccion('\<use> ::= "USE" "ID" ') 

# __________________________________________definicion

# <DEFINICION> ::= 'create' 'type' 'ID' 'as' 'enum' '(' <LISTA_ENUM> ')'
#               | <CREATE_OR_REPLACE> 'database' <COMBINACIONES1>
#               | 'show' 'databases' 'like' regex
#               | 'show' 'databases'
#               | 'alter' 'database' id <ALTER>
#               | 'drop' 'database' 'if' 'exists' id
#               | 'drop' 'database' id
#               | 'drop' 'table' id
#               | 'create' 'table' id (<COLUMNAS>)<INHERITS>
#               | 'create' 'table' id (<COLUMNAS>)


def p_definicion_1(p):
    'definicion : CREATE TYPE ID  AS ENUM PABRE lista_enum PCIERRA'
    bnf.addProduccion('\<definicion> ::= "CREATE" "TYPE" "AS" "ENUM" "(" \<lista_enum> ")"') 
    p[0] = CreateType(p[3], p[7])


def p_definicion_2(p):
    'definicion : create_or_replace DATABASE combinaciones1'
    bnf.addProduccion('\<definicion> ::= \<create_or_replace> "DATABASE"  \<combinaciones1>')
    tempNombre = None
    tempExistencia = False
    tempDuenio = None
    tempModo = 0

    if isinstance(p[3], tuple):
        if len(p[3]) == 2:
            if isinstance(p[3][0], bool):
                tempExistencia = True
                tempNombre = p[3][1]
            else:
                tempExistencia = p[3][0]

                if isinstance(p[3][1], tuple):
                    tempDuenio = p[3][1][0]
                    tempModo = p[3][1][1]
                elif isinstance(p[3][1], int):
                    tempModo = p[3][1]
                else:
                    tempDuenio = p[3][1]
        else:
            tempExistencia = True
            tempNombre = p[3][1]

            if isinstance(p[3][2], tuple):
                tempDuenio = p[3][2][0]
                tempModo = p[3][2][1]
            elif isinstance(p[3][2], int):
                tempModo = p[3][2]
            else:
                tempDuenio = p[3][2]
    else:
        tempNombre = p[3]
    p[0] = CreateDatabase(tempNombre,reemplazo=p[1], existencia=tempExistencia, duenio=tempDuenio, modo=tempModo)

def p_definicion_3(p):
    'definicion : SHOW DATABASES LIKE REGEX'
    bnf.addProduccion('\<definicion> ::= "SHOW" "DATABASE" "LIKE" "REGEX"') 
    p[0] = ShowDatabase()

def p_definicion_4(p):
    'definicion : SHOW DATABASES'
    bnf.addProduccion('\<definicion> ::= "SHOW" "DATABASES"')
    print("databases")
    p[0] = ShowDatabase()


def p_definicion_5(p):
    'definicion : ALTER DATABASE ID  alter'
    bnf.addProduccion('\<definicion> ::= "ALTER" "DATABASE" "ID" \<alter>')
    p[0] = AlterDatabase(p[3],p[4])

def p_definicion_6(p):
    'definicion : DROP DATABASE IF EXISTS ID'
    bnf.addProduccion('\<definicion> ::= "DROP" "DATABASE" "IF" "EXISTS" "ID"')
    p[0] = DropDatabase(p[5], True)


def p_definicion_7(p):
    'definicion : DROP DATABASE ID'
    bnf.addProduccion('\<definicion> ::= "DROP" "DATABASE" "ID"')
    p[0] = DropDatabase(p[3])


def p_definicion_8(p):
    'definicion : DROP TABLE ID'
    bnf.addProduccion('\<definicion> ::= "DROP" "TABLE" "ID"') 
    p[0] = DropTable(p[3])

def p_definicion_9(p):
    'definicion : CREATE TABLE ID PABRE columnas PCIERRA inherits'
    bnf.addProduccion('\<definicion> ::= "CREATE" "TABLE" "ID" "(" \<columnas> ")" \<inherits>')
    p[0] = CreateTable(p[3], p[5], p[7])


def p_definicion_10(p):
    'definicion : CREATE TABLE ID PABRE columnas PCIERRA'
    bnf.addProduccion('\<definicion> ::= "CREATE" "TABLE" "ID" "(" \<columnas> ")"')
    p[0] = CreateTable(p[3], p[5]) 

def p_alter_table(p):
    '''alter_table : ALTER TABLE ID alter_options'''
    bnf.addProduccion('\<alter_table> ::= "ALTER" "TABLE" "ID"  \<alter_varchar_lista> ')
    p[0] = AlterTable(p[3],p[4])
    
def p_alter_table2(p):
    'alter_table :  ALTER TABLE ID alter_varchar_lista'
    bnf.addProduccion('\<alter_table> ::= "ALTER" "TABLE" "ID"  \<alter_varchar_lista> ')
    p[0] = AlterTable(p[3],p[4])
        
def p_alter_options(p):
    'alter_options : ADD COLUMN ID tipo '
    bnf.addProduccion('\<alter_options> ::= "ADD" "COLUMN" "ID" \<tipo>')
    p[0] = AlterTableAdd(p[3], ALTER_TABLE_ADD.COLUMN, p[4])

def p_alter_options2(p):
    'alter_options : DROP COLUMN ID '
    bnf.addProduccion('\<alter_options> ::= "DROP" "COLUMN" "ID" ')
    p[0] = AlterTableDrop(p[3], ALTER_TABLE_DROP.COLUMN)

def p_alter_options3(p):
    'alter_options : ADD CHECK PABRE ID DIFERENTE CADENA PCIERRA '
    bnf.addProduccion('\<alter_options> ::= "ADD" "CHECK" "(" "ID" "<>" "CADENA" ")" ')
    p[0] = AlterTableAdd(p[4], ALTER_TABLE_ADD.CHECKS, p[6])

def p_alter_options4(p):
    'alter_options : ADD CONSTRAINT ID UNIQUE PABRE ID PCIERRA '
    bnf.addProduccion('\<alter_options> ::= "ADD" "CONSTRAINT" "ID" "UNIQUE" "(" "ID" ")"')
    p[0] = AlterTableAdd(p[6], ALTER_TABLE_ADD.UNIQUE, p[3])

#______________________________________________________________________________________________________________________________ NUEVA;
#Cambio por agregado unico y multiple
def p_alter_options5(p):
    'alter_options : ADD CONSTRAINT ID FOREIGN KEY PABRE ID PCIERRA REFERENCES ID PABRE ID PCIERRA'
    bnf.addProduccion('\<alter_options> ::= "ADD" "CONSTRAINT" "ID" "FOREIGN" "KEY" "(" "ID" ")" "REFERENCES" "ID" "(" "ID" ")"')
    p[0] = AlterTableAdd(p[7], ALTER_TABLE_ADD.FOREIGN_KEY, (p[10],p[12],p[3]))

def p_alter_options6(p):
    'alter_options : ADD FOREIGN KEY PABRE lista_ids PCIERRA REFERENCES ID PABRE lista_ids PCIERRA ' 
    bnf.addProduccion('\<alter_options> ::= "ADD" "FOREIGN" "KEY "(" \<lista_ids> ")" "REFERENCES" "ID" "(" \<lista_ids> ")"')
    p[0] = AlterTableAdd(p[5], ALTER_TABLE_ADD.MULTI_FOREIGN_KEY, (p[8], p[10]))       

def p_alter_options7(p):
    'alter_options : ALTER COLUMN ID SET NOT NULL '
    bnf.addProduccion('\<alter_options> ::= "ALTER" "COLUMN" "ID" "SET" "NOT"  "NULL"')
    p[0] = AlterField(p[3])
    
def p_alter_options8(p):
    'alter_options : DROP CONSTRAINT ID '
    bnf.addProduccion('\<alter_options> ::= "DROP" "CONSTRAINT" "ID"')
    p[0] = AlterTableDrop(p[3], ALTER_TABLE_DROP.CONSTRAINT)           


def p_alter_varchar_lista(p):
    '''alter_varchar_lista :  alter_varchar
                           |  alter_varchar_lista COMA alter_varchar'''
    if len(p) == 2:
        bnf.addProduccion('\<alter_varchar_lista> ::= \<alter_varchar>')
        p[0] = [p[1]]
    else:
        bnf.addProduccion('\<alter_varchar_lista> ::= \<alter_varchar> "," \<alter_varchar>')
        p[1].append(p[3])
        p[0] = p[1]

def p_alter_varchar(p):
    '''alter_varchar : ALTER COLUMN ID TYPE VARCHAR PABRE NUMERO PCIERRA '''
    bnf.addProduccion('\<alter_varchar> ::= "ALTER" "COLUMN" "ID" "TYPE" "VARCHAR" "(" NUMERO ")"')
    p[0] = AlterField(p[3],p[7])

# <TABLA> ::=  'id' 
#          |   'id' 'as' 'id'
#          |   <SUBQUERY>
#          |   <SUBQUERY> 'as' 'id'
def p_tablas(p):
    '''tabla : ID
            |  ID alias
            |  ID AS alias '''
    if len(p) == 2:
        p[0] = p[1]
        bnf.addProduccion('\<tabla> ::= "ID"')
    elif len(p) == 3:
        p[0] = ITEM_ALIAS(p[1], p[2])
        bnf.addProduccion('\<tabla> ::= "ID" \<alias>')
    else:
        p[0] = ITEM_ALIAS(p[1], p[3])
        bnf.addProduccion('\<tabla> ::= "ID" "AS" \<alias>')
def p_tablas2(p):
    '''tabla : subquery
            |  subquery alias 
            |  subquery AS alias '''
    if len(p) == 2:
        bnf.addProduccion('\<tabla> ::= \<subquery>')
    elif len(p) ==3:
        bnf.addProduccion('\<tabla> ::= \<subquery> \<alias>')
    else:
        bnf.addProduccion('\<tabla> ::= \<subquery> "AS" \<alias>')            


def p_filtro(p):
    '''filtro : where group_by having
              | where group_by
              | where '''
    if len(p) == 4:
        bnf.addProduccion('\<filtro> ::= \<where> \<group_by> \<having>')
        p[0] = SelectFilter(p[1],p[2],p[3])
    elif len(p) == 3:
        bnf.addProduccion('\<filtro> ::= \<where> \<group_by>')
        p[0] = SelectFilter(p[1],p[2])
    else:
        bnf.addProduccion('\<filtro> ::= \<where>')
        p[0] = SelectFilter(p[1])

        

    

def p_combine_querys1(p):
    'combine_querys : combine_querys UNION ALL select'
    p[0] = combineQuery(p[1], COMBINE_QUERYS.UNION, p[3],p.slice[1].lineno)
    bnf.addProduccion('\<combine_querys> ::= \<combine_querys> "UNION" "ALL" \<select>')

def p_combine_querys2(p):
    'combine_querys : combine_querys UNION select'
    p[0] = combineQuery(p[1], COMBINE_QUERYS.UNION, p[3],p.slice[1].lineno)
    bnf.addProduccion('\<combine_querys> ::= \<combine_querys> "UNION"  \<select>')

def p_combine_querys3(p):
    'combine_querys : combine_querys INTERSECT ALL select'
    p[0] = combineQuery(p[1], COMBINE_QUERYS.INTERSECT, p[3],p.slice[1].lineno)
    bnf.addProduccion('\<combine_querys> ::= \<combine_querys> "INTERSECT" "ALL"  \<select>')

def p_combine_querys4(p):
    'combine_querys : combine_querys INTERSECT select'
    p[0] = combineQuery(p[1], COMBINE_QUERYS.INTERSECT, p[3],p.slice[1].lineno)
    bnf.addProduccion('\<combine_querys> ::= \<combine_querys> "INTERSECT"  \<select>')

def p_combine_querys5(p):
    'combine_querys : combine_querys EXCEPT ALL select'
    p[0] = combineQuery(p[1], COMBINE_QUERYS.EXCEPT, p[3],p.slice[1].lineno)
    bnf.addProduccion('\<combine_querys> ::= \<combine_querys> "EXCEPT" "ALL" \<select>')

def p_combine_querys6(p):
    'combine_querys : combine_querys EXCEPT select'
    p[0] = combineQuery(p[1], COMBINE_QUERYS.EXCEPT, p[3],p.slice[1].lineno)
    bnf.addProduccion('\<combine_querys> ::= \<combine_querys> "EXCEPT"  \<select>')

def p_combine_querys7(p):
    'combine_querys : select'
    p[0] = p[1]
    bnf.addProduccion('\<combine_querys> ::= \<select> ')
#_____________________________________________________________ SELECT


def p_select2(p):#_________________________________- select simple con un where
    'select : SELECT select_list FROM lista_tablas filtro'
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas> \<filtro>')
    p[0] = SelectFromWhere(p[4], p[2] ,p[5],p.slice[1].lineno)



def p_select4(p):
    'select : SELECT select_list FROM lista_tablas orders limits offset'
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas> \<orders> \<limits> \<offset>')


def p_select6(p):
    'select : SELECT select_list FROM lista_tablas orders limits'
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas> \<orders> \<limits>')


def p_select8(p):
    'select : SELECT select_list FROM lista_tablas orders offset'
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas> \<orders> \<offset>')


def p_select10(p):
    'select : SELECT select_list FROM lista_tablas orders'
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas> \<orders>')
    
def p_select12(p):
    'select : SELECT select_list FROM lista_tablas limits offset'
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas> \<limits>  \<offset>')

    
def p_select14(p):
    'select : SELECT select_list FROM lista_tablas limits'
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas> \<limits> ')


def p_select16(p):
    'select : SELECT select_list FROM lista_tablas offset'
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas> \<offset>')



def p_select20(p):
    'select : SELECT DISTINCT select_list FROM lista_tablas filtro'
    bnf.addProduccion('\<select> ::= "SELECT" "DISTINCT" \<select_list>  "FROM"  \<lista_tablas> \<filtro>')


def p_select24(p):
    'select : SELECT select_list FROM lista_tablas'
    p[0] = SelectFrom(p[4], p[2],p.slice[1].lineno)
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list> "FROM"  \<lista_tablas>')


def p_select28(p):
    'select : SELECT DISTINCT select_list FROM lista_tablas'
    bnf.addProduccion('\<select> ::= "SELECT" "DISTINCT" \<select_list> "FROM"  \<lista_tablas>')

def p_select30(p):
    'select : SELECT select_list'
    p[0] = SelectSimple(p[2],p.slice[1].lineno)
    bnf.addProduccion('\<select> ::= "SELECT" \<select_list>')

def p_select31(p):
    'select : SELECT DISTINCT select_list'
    bnf.addProduccion('\<select> ::= "SELECT" "DISTINCT" \<select_list>')
    
def p_select_nuevo_distinct(p):
    'select : SELECT DISTINCT  select_list FROM  lista_tablas filtro limits'
    bnf.addProduccion('\<select> ::= "SELECT" "DISTINCT" \<select_list> "FROM"  \<lista_tablas> \<filtro> \<limits>')
    
def p_select_nuevo(p):
    'select : SELECT select_list FROM  lista_tablas filtro limits'
    bnf.addProduccion('\<select> ::= "SELECT" "DISTINCT" \<select_list> "FROM"  \<lista_tablas> \<filtro> \<limits>')

    
def p_select32(p):
    'select : SELECT  select_list FROM  lista_tablas group_by'
    bnf.addProduccion('\<select> ::= "SELECT" "DISTINCT" \<select_list>')
    # ENTRADA DE PRUEBA
    # select *
    # from t10
    # group by cadena;



#________________________________________ LIMIT 

def p_limits(p):
    'limits : LIMIT limitc'
    bnf.addProduccion('\<limitc> ::= "LIMIT" \<limitc>')

def p_limitc1(p):
    'limitc : NUMERO'
    bnf.addProduccion(f'\<limitc> ::= "{p[1].upper()}"')
    p[0] = p[1]
    

def p_limitc2(p):
    'limitc : ALL'
    bnf.addProduccion(f'\<limitc> ::= "{p[1].upper()}"')
    p[0] = p[1]

def p_offset(p):
    'offset : OFFSET NUMERO'
    bnf.addProduccion(f'\<offset> ::= "{p[1].upper()}" "NUMERO"')
#__________________________________________________________________________________________________________ FUNCIONES 
def p_funciones1(p):#ya
    'funciones : LENGTH PABRE exp_aux PCIERRA'
    p[0] = FuncionCadena(funcion='LENGTH',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones2(p):#ya
    'funciones : SUBSTRING PABRE exp_aux COMA exp_aux COMA exp_aux PCIERRA'
    p[0] = FuncionCadena(funcion='SUBSTRING',parametro1=p[3],parametro2= p[5],parametro3=p[7], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux> "," \<exp_aux> ")"')
    
def p_funciones3(p):#ya
    'funciones : TRIM PABRE exp_aux PCIERRA'
    p[0] = FuncionCadena(funcion='TRIM',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones4(p):#ya
    'funciones : MD5 PABRE exp_aux PCIERRA'
    p[0] = FuncionCadena(funcion='MD5',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones5(p):#ya
    'funciones : SHA256 PABRE exp_aux PCIERRA'
    p[0] = FuncionCadena(funcion='SHA256',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones6(p):#ya
    'funciones : SUBSTR PABRE exp_aux COMA exp_aux COMA exp_aux PCIERRA'
    p[0] = FuncionCadena(funcion='SUBSTR',parametro1=p[3], parametro2=p[5] , parametro3=p[7],  linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux> "," \<exp_aux>  ")"')

def p_funciones7(p):# cadena , numero 
    'funciones : GET_BYTE PABRE exp_aux TYPECAST BYTEA COMA exp_aux PCIERRA'
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "TYPECAST" "BYTEA" "," \<exp_aux>  ")"')

def p_funciones8(p):# cadena , numero , numero 
    'funciones : SET_BYTE PABRE CADENA TYPECAST BYTEA COMA NUMERO COMA NUMERO PCIERRA'
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" "CADENA" "TYPECAST" "BYTEA" "," "NUMERO" "," "NUMERO" ")"')

def p_funciones9(p):
    'funciones : CONVERT PABRE CADENA AS DATE PCIERRA'
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" "CADENA"  "AS" "DATE"  ")"')

def p_funciones10(p): 
    'funciones : CONVERT PABRE CADENA AS INTEGER PCIERRA'
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" "CADENA"  "AS" "INTEGER" ")"')
    
def p_funciones11(p): # FASE 2 
    'funciones : ENCODE PABRE CADENA BYTEA COMA CADENA PCIERRA'
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" "CADENA"  "BYTEA" "," "CADENA" ")"')

def p_funciones12(p): # FASE 2 
    'funciones : DECODE PABRE CADENA COMA CADENA PCIERRA'
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" "CADENA"  "," "CADENA" ")"')



def p_funciones14(p):#ya
    'funciones : ACOS PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ACOS',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones15(p):#ya
    'funciones : ACOSD PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ACOSD',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    

def p_funciones16(p):#ya
    'funciones : ASIN PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ASIN',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones17(p):#ya
    'funciones : ASIND PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ASIND',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones18(p):#ya
    'funciones : ATAN PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ATAN',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones19(p):#ya
    'funciones : ATAND PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ATAND',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
#_______________________________________ BINARIAS
def p_funciones20(p):#ya
    'funciones : ATAN2 PABRE exp_aux COMA exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ATAN2',parametro1=p[3], parametro2=p[5], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux> ")"')
    
def p_funciones21(p):#ya
    'funciones : ATAN2D PABRE exp_aux COMA exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ATAN2D',parametro1=p[3], parametro2=p[5], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux> ")"')

def p_funciones22(p):#ya
    'funciones : COS PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='COS',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
 
def p_funciones23(p):#ya
    'funciones : COSD PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='COSD',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones24(p):#ya
    'funciones : COT PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='COT',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones25(p):#ya
    'funciones : COTD PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='COTD',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
 
def p_funciones26(p):#ya
    'funciones : SIN PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='SIN',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones27(p):#ya
    'funciones : SIND PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='SIND',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones28(p):#ya
    'funciones : TAN PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='TAN',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones29(p):#ya
    'funciones : TAND PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='TAND',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones30(p):#ya
    'funciones : COSH PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='COSH',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones31(p):#YA
    'funciones : SINH PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='SINH',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
     
def p_funciones32(p):#YA
    'funciones : TANH PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='TANH',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
 
def p_funciones33(p):#YA
    'funciones : ACOSH PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ACOSH',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones34(p):#ya
    'funciones : ASINH PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ASINH',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones35(p):#ya
    'funciones : ATANH PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ATANH',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones36(p):#ya
    'funciones : ABS PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='ABS',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
 
def p_funciones37(p):#ya
    'funciones : CBRT PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='CBRT',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones38(p):#ya
    'funciones : CEIL PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='CEIL',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones39(p):#ya
    'funciones : CEILING PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='CEILING',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones40(p):#ya
    'funciones : DEGREES PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='DEGREES',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones41(p):#ya
    'funciones : DIV PABRE exp_aux COMA exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='DIV',parametro1=p[3], parametro2=p[5], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux>  ")"')#BINARIA 
    
def p_funciones42(p):# ya 
    'funciones : FACTORIAL PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='FACTORIAL',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"') 
    
def p_funciones43(p):# ya 
    'funciones : FLOOR PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='FLOOR',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"') 
    
def p_funciones44(p):#ya
    'funciones : GCD PABRE exp_aux COMA exp_aux  PCIERRA'
    p[0] = FuncionNumerica(funcion='GCD',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux>  ")"')#BINARIA 
    
def p_funciones45(p):#ya
    'funciones : LN PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='LN',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones46(p):#ya
    'funciones : LOG PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='LOG',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
 
def p_funciones47(p):#ya
    'funciones : EXP PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='EXP',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones48(p):#ya
    'funciones : MOD PABRE exp_aux COMA exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='MOD',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux>  ")"')#BINARIA 

def p_funciones49(p):#YA
    'funciones : PI PABRE PCIERRA'
    p[0] = FuncionNumerica(funcion='PI', linea= p.slice[1].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" ")"')

def p_funciones50(p):#ya 
    'funciones : POWER PABRE exp_aux COMA exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='POWER',parametro1=p[3], parametro2=p[5], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux>  ")"')#BINARIA
    
def p_funciones51(p):#ya
    'funciones : RADIANS PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='RADIANS',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones52(p):#ya
    'funciones : ROUND PABRE   exp_aux  PCIERRA'
    p[0] = FuncionNumerica(funcion='ROUND',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones52_version2(p):#ya
    'funciones : ROUND PABRE exp_aux  COMA  exp_aux  PCIERRA '
    p[0] = FuncionNumerica(funcion='ROUND',parametro1=p[3],parametro2 = p[5] , linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux>  ")"')#BINARIA

def p_funciones53(p):#ya
    'funciones : SIGN PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='SIGN',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

def p_funciones54(p):#ya 
    'funciones : SQRT PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='SQRT',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones55(p):# decimal y entero  , LISTA DE NUMEROS []
    'funciones : WIDTH_BUCKET PABRE lista_exp PCIERRA'
    p[0] = FuncionNumerica(funcion='WIDTH_BUCKET',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<lista_exp> ")"')

def p_funciones56(p):#ya
    'funciones : TRUNC PABRE exp_aux COMA exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='TRUNC',parametro1=p[3], parametro2=p[5], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> "," \<exp_aux>  ")"')#BINARIA
    
def p_funciones57(p):#ya
    'funciones : TRUNC PABRE exp_aux PCIERRA'
    p[0] = FuncionNumerica(funcion='TRUNC',parametro1=p[3], linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')
    
def p_funciones58(p):#ya
    'funciones : RANDOM PABRE PCIERRA'
    p[0] = FuncionNumerica(funcion='RANDOM', linea= p.slice[2].lineno)
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" \<exp_aux> ")"')

#_______________________________________________________________________ UNARIAS BITWASE
def p_funcionesBitwase1(p):
    'exp_aux : DOBLE_PIPE exp_aux '
    bnf.addProduccion('\<funciones> ::= "||" \<exp_aux> ')
    p[0] = BitwaseUnaria(operador = "||" , exp=p[2] , linea=p.slice[1].lineno)
def p_funcionesBitwase2(p):
    'exp_aux : PIPE exp_aux '
    bnf.addProduccion('\<funciones> ::= "|" \<exp_aux>')
    p[0] = BitwaseUnaria(operador = "|" , exp=p[2] , linea=p.slice[1].lineno)
def p_funcionesBitwase3(p):
    'exp_aux : BITWISE_NOT exp_aux'
    bnf.addProduccion('\<funciones> ::= "~" \<exp_aux>')
    p[0] = BitwaseUnaria(operador = "~" , exp=p[2] , linea=p.slice[1].lineno)

#________________________________________________________________________ BINARIA BITWASE
def p_funcionesBitwase4(p):# AND
    'exp_aux : exp_aux AMPERSAND exp_aux'
    bnf.addProduccion('\<funciones> ::= \<exp_aux> "&" \<exp_aux> ')
    p[0] =  BitwaseBinaria(exp1=p[1] , exp2= p[3] , operador="&",linea=p.slice[2].lineno)
def p_funcionesBitwase5(p):# OR
    'exp_aux : exp_aux PIPE exp_aux'
    bnf.addProduccion('\<funciones> ::= \<exp_aux> "|" \<exp_aux> ')
    p[0] =  BitwaseBinaria(exp1=p[1] , exp2= p[3] , operador="|",linea=p.slice[2].lineno)
def p_funcionesBitwase6(p):# XOR
    'exp_aux : exp_aux NUMERAL exp_aux'
    bnf.addProduccion('\<funciones> ::= \<exp_aux> "#" \<exp_aux> ')
    p[0] =  BitwaseBinaria(exp1=p[1] , exp2= p[3] , operador="#",linea=p.slice[2].lineno)
    
def p_funcionesBitwase7(p):
    'exp_aux : exp_aux CORRIMIENTO_IZQ exp_aux'
    bnf.addProduccion('\<funciones> ::= \<exp_aux> "<<" \<exp_aux> ')
    p[0] =  BitwaseBinaria(exp1=p[1] , exp2= p[3] , operador="<<",linea=p.slice[2].lineno)
def p_funcionesBitwase8(p):
    'exp_aux : exp_aux CORRIMIENTO_DER exp_aux'
    bnf.addProduccion('\<funciones> ::= \<exp_aux> ">>" \<exp_aux> ')
    p[0] =  BitwaseBinaria(exp1=p[1] , exp2= p[3] , operador=">>",linea=p.slice[2].lineno)
#____________________________________________________________________________________________________________________________ FUNCIONES DE TIEMPO     
    
def p_funciones_time1(p):
    'funciones : NOW PABRE PCIERRA'
    bnf.addProduccion(f'\<funciones> ::= "{p[1].upper()}" "(" ")"')
    p[0] = FuncionTime(funcion="NOW" , linea=p.slice[1].lineno)
def p_funciones_time2(p):
    'funciones : TIMESTAMP CADENA_NOW'
    bnf.addProduccion(f'\<timestamp> ::= "{p[1].upper()}" "CADENA_NOW"')
    p[0] = FuncionTime(funcion="TIMESTAMP" , parametro1=p[2],linea=p.slice[1].lineno)

def p_funciones_time3(p):
    'funciones : EXTRACT PABRE opcionesTime FROM TIMESTAMP CADENA_DATE PCIERRA'
    bnf.addProduccion('\<funciones> ::= "EXTRACT" "(" \<opcionesTime> "FROM" "TIMESTAMP" "CADENA_DATE" ")"')
    p[0] = FuncionTime(funcion="EXTRACT" , parametro1=p[3], parametro2=p[6],linea=p.slice[1].lineno)
    
def p_funciones_time4(p):# esta cadena fijo tiene que ser minutes secods o hours
    'funciones : DATE_PART PABRE CADENA COMA INTERVAL CADENA_INTERVAL PCIERRA'
    bnf.addProduccion('\<funciones> ::= "DATE_PART" "(" "CADENA" "," "INTERVAL" "CADENA_INTERVAL" ")"')
    p[0] = FuncionTime(funcion="DATE_PART" , parametro1=p[3].upper(), parametro2=p[6],linea=p.slice[1].lineno)
def p_funciones_time5(p):
    'funciones : CURRENT_DATE'
    bnf.addProduccion('\<funciones> ::= "CURRENT_DATE"')
    p[0] = FuncionTime(funcion="CURRENT_DATE" , linea=p.slice[1].lineno)
    
def p_funciones_time6(p):
    'funciones : CURRENT_TIME'
    bnf.addProduccion('\<funciones> ::= "CURRENT_TIME"')
    p[0] = FuncionTime(funcion="CURRENT_TIME" , linea=p.slice[1].lineno)

def p_funciones_time7(p):
    'funciones : CURRENT_TIMESTAMP'
    p[0] = FuncionTime(funcion="CURRENT_TIMESTAMP" , linea=p.slice[1].lineno)
    
def p_funcionesAgrecacion(p):#ya
    'funciones : aggregate_f'
    bnf.addProduccion(f'\<funciones> ::= "(" \<aggregate_f> ")"')
      
def p_opcionesTime(p):
    '''
    opcionesTime : YEAR
                 | MONTH
                 | DAY
                 | HOUR
                 | MINUTE
                 | SECOND
    '''
    p[0] = p[1]
    

def p_lista_tablas(p):
    '''
    lista_tablas : lista_tablas COMA tabla
                 | tabla
    '''
    if (len(p) == 4):
        p[1].append(p[3])
        p[0] = p[1]
        bnf.addProduccion('\<lista_tablas> ::= \<lista_tablas> "," \<tabla> ')
    else:
        p[0] = [p[1]]
        bnf.addProduccion('\<lista_tablas> ::= \<tabla>')

    

def p_select_list(p):
    '''
    select_list : select_item
                | select_item alias
                | select_item AS alias
    '''
    if len(p) == 2:
        p[0] = [p[1]]
        bnf.addProduccion('\<select_list> ::= \<select_item>')
    elif len(p) == 3:
        p[0] = [ITEM_ALIAS(p[1], p[2])] # considerar que este ya tendria un alias
        bnf.addProduccion('\<select_list> ::= \<select_item>  "ID"')
    elif len(p) == 4:
        p[0] = [ITEM_ALIAS(p[1], p[3])] # considerar que este ya tendria un alias
        bnf.addProduccion('\<select_list> ::= \<select_item> "AS" \<alias>')

def p_select_list2(p):
    '''
    select_list : select_list COMA select_item
                | select_list COMA select_item alias 
                | select_list COMA select_item AS alias 
    '''
    if (len(p) == 4):
        p[1].append(p[3])
        p[0] = p[1]
        bnf.addProduccion('\<select_list> ::= \<select_list> "," \<select_item> ')
    elif len(p) == 5:
        p[1].append(ITEM_ALIAS(p[3], p[4]))
        p[0] = p[1] # falta considerar que este ya tendria un alias
        bnf.addProduccion('\<select_list> ::= \<select_list> "," \<select_item> "ID"')
    elif len(p) == 6:
        p[1].append(ITEM_ALIAS(p[3], p[5]))
        p[0] = p[1] # falta considerar que este ya tendria un alias
        bnf.addProduccion('\<select_list> ::= \<select_list> "," \<select_item> "AS" \<alias>')

# __________________________________________ lista_enum
# <LISTA_ENUM> ::= <ITEM>
#               | <LISTA_ENUM> ',' <ITEM>


def p_lista_enum_1(p):
    'lista_enum : item'
    bnf.addProduccion('\<lista_enum> ::= \<item>')
    p[0] = [p[1]]


def p_lista_enum_2(p):
    'lista_enum : lista_enum COMA item'
    p[1].append(p[3])
    p[0] = p[1]
    bnf.addProduccion('\<lista_enum> ::= \<lista_enum> "," \<item>')
# __________________________________________ ITEM
# <ITEM> ::= cadena


def p_item(p):
    'item : CADENA'
    p[0] = p[1]
    bnf.addProduccion(f'\<item> ::= "{p[1].upper()}"')
# __________________________________________ create_or_replace
# <CREATE_OR_REPLACE> ::= 'create'
#                      | 'create or replace'


def p_create_or_replace_1(p):
    'create_or_replace : CREATE '
    p[0] = False
    bnf.addProduccion(f'\<create_or_replace> ::= "{p[1].upper()}"')


def p_create_or_replace_2(p):
    'create_or_replace : CREATE OR REPLACE'
    bnf.addProduccion(f'\<create_or_replace> ::= "{p[1].upper()}" "OR" "REPLACE"')
    p[0]= True

# __________________________________________ combinaciones1
# <COMBINACIONES1> ::= 'if' 'not' 'exists' id <COMBINACIONES2>
#                   | id <COMBINACIONES2>
#                   | id
def p_combinaciones1_0(p):
    'combinaciones1 : IF NOT EXISTS ID'
    bnf.addProduccion(f'\<combinaciones1> ::= "{p[1].upper()}" "NOT" "EXISTS" "ID"')
    p[0] = (True, p[4])

def p_combinaciones1_1(p):
    'combinaciones1 : IF NOT EXISTS ID combinaciones2'
    bnf.addProduccion(f'\<combinaciones1> ::= "{p[1].upper()}" "NOT" "EXISTS" "ID" \<combinaciones2>')
    p[0] = (True,p[4],p[5])

def p_combinaciones1_2(p):
    'combinaciones1 : ID combinaciones2'
    bnf.addProduccion(f'\<combinaciones1> ::= "{p[1].upper()}" \<combinaciones2>')
    p[0] = (p[1],p[2])

def p_combinaciones1_3(p):
    'combinaciones1 : ID'
    bnf.addProduccion(f'\<combinaciones1> ::= "{p[1].upper()}"')
    p[0] = p[1]
# ________________________________________ combinaciones2
# <COMBINACIONES2> ::= <OWNER>
#                   |<MODE>
#                   |<OWNER><MODE>


def p_combinaciones2_1(p):
    'combinaciones2 : owner'
    bnf.addProduccion('\<combinaciones2> ::= \<owner>')
    p[0] = p[1]


def p_combinaciones2_2(p):
    'combinaciones2 : mode'
    bnf.addProduccion('\<combinaciones2> ::= \<mode>')
    p[0] = p[1]


def p_combinaciones2_3(p):
    'combinaciones2 : owner mode'
    bnf.addProduccion('\<combinaciones2> ::= \<owner> \<mode>')
    p[0] = (p[1],p[2])

def p_owner_1(p):
    'owner : OWNER alias'
    p[0] = p[2]
    bnf.addProduccion('\<owner> ::= "OWNER" \<alias>')

def p_owner_2(p):
    'owner : OWNER IGUAL alias'
    p[0] = p[3]
    bnf.addProduccion('\<owner> ::= "OWNER" "=" \<alias>')

# ________________________________________ <MODE>
# <MODE> ::= 'mode' entero
#         | 'mode' '=' entero


def p_mode_1(p):
    'mode : MODE NUMERO'
    bnf.addProduccion('\<mode> ::= "MODE" "NUMERO"')
    p[0] = p[2]


def p_mode_2(p):
    'mode : MODE IGUAL NUMERO'
    bnf.addProduccion('\<mode> ::= "MODE" "=" "NUMERO"')
    p[0] = p[3]


# _________________________________________ <alter>
# <ALTER> ::= 'rename to' id
#          | 'owner to' <NEW_OWNER>

def p_alter_1(p):
    'alter : RENAME TO ID'
    bnf.addProduccion('\<alter> ::= "RENAME" "TO" "ID"')


def p_alter_2(p):
    'alter : OWNER TO new_owner'
    bnf.addProduccion('\<alter> ::= "OWNER" "TO" \<new_owner>')

# _________________________________________ new_owner
#  <NEW_OWNER> ::= id
#              | 'current_user'
#              | 'session_user'


def p_new_owner_1(p):
    'new_owner : ID '
    bnf.addProduccion('\<new_owner> ::= "ID"')
    p[0] = p[1]


def p_new_owner_2(p):
    'new_owner : CURRENT_USER '
    bnf.addProduccion('\<new_owner> ::= "CURRENT_USER"')
    p[0]=p[1]


def p_new_owner_3(p):
    'new_owner : SESSION_USER'
    bnf.addProduccion('\<new_owner> ::= "SESSION_USER"')
    p[0]=p[1]

# _________________________________________ inherits
# <INHERITS> ::= 'INHERITS' '('ID')'


def p_inherits(p):
    'inherits : INHERITS PABRE ID PCIERRA'
    bnf.addProduccion('\<inherits> ::= "INHERITS" "(" "ID" ")"')
    p[0] = p[3]

# _________________________________________ columnas
# <COLUMNAS> ::= <COLUMNA>
#             | <COLUMNAS>, <COLUMNA>


def p_columnas_1(p):
    'columnas : columna'
    bnf.addProduccion('\<columnas> ::= \<columna>')
    p[0] = [p[1]]

def p_columnas_2(p):
    'columnas : columnas COMA columna'
    bnf.addProduccion('\<columnas> ::= \<columnas> ","  \<columna> ')
    p[1].append(p[3])
    p[0] = p[1]
    


# _________________________________________ columna
#  <COLUMNA> ::=
#             | id' <TIPO>
#             | id' <TIPO> <listaOpciones>
#             | 'constraint' 'id' 'check' (<lista_exp>)
#             | 'id' 'check' (<lista_exp>)
#             | 'unique' (<LISTA_IDS>)
#             | 'primary' 'key' (<LISTA_IDS>)
#             | 'foreign' 'key' (<LISTA_IDS>) 'references' 'id' (<LISTA_IDS>)

# listaOpciones> ::= <listaOpciones> <opCol>
#                  | <opCol>

# <opCol>   ::=  <DEFAULT>
#             |  <CONSTRAINTS>
#             |  <CHECKS>
#             |  <nulleable>
#             |  'primary' 'key'
#             |  'references' 'id'

# ___________________________________________ declaracion de columna
def p_columna_1(p):
    'columna : ID tipo'
    bnf.addProduccion('\<columna> ::= "ID"  \<tipo>')
    p[0] = CreateField(p[1],p[2])


def p_columna_2(p):
    'columna : ID tipo listaOpciones'
    bnf.addProduccion('\<columna> ::= "ID"  \<tipo> \<listaOpciones>')
    p[0] = CreateField(p[1],p[2],p[3])


def p_columna_3(p):
    'columna : CONSTRAINT  ID CHECK PABRE expresion PCIERRA '
    bnf.addProduccion('\<columna> ::= "CONSTRAINT" "ID" "CHECK" "(" \<expresion> ")"')
    p[0] = CheckMultipleFields(p[2],p[5])


def p_columna_4(p):
    'columna : UNIQUE PABRE lista_ids PCIERRA'
    bnf.addProduccion('\<columna> ::= "UNIQUE" "(" \<lista_ids> ")"')
    p[0] = ConstraintMultipleFields(CONSTRAINT_FIELD.UNIQUE, p[3])


def p_columna_5(p):
    'columna :  PRIMARY KEY PABRE lista_ids PCIERRA'
    bnf.addProduccion('\<columna> ::= "PRIMARY" "KEY" "(" \<lista_ids> ")"')
    p[0] = ConstraintMultipleFields(CONSTRAINT_FIELD.PRIMARY_KEY, p[4])

def p_columna_6(p):
    'columna : FOREIGN KEY PABRE lista_ids PCIERRA REFERENCES ID PABRE lista_ids PCIERRA'
    bnf.addProduccion('\<columna> ::= "FOREIGN" "KEY" "(" \<lista_ids> ")" "REFERENCES" "ID" "(" \<lista_ids> ")"')
    p[0] = ForeignKeyMultipleFields(p[4],p[7],p[9])
    


def p_listaOpciones_List(p):
    'listaOpciones : listaOpciones opCol'
    bnf.addProduccion('\<listaOpciones> ::= \<listaOpciones> \<opCol>')
    p[1].append(p[2])
    p[0] = p[1]
        
 
        
def p_listaOpciones_una(p):
    'listaOpciones : opCol'
    bnf.addProduccion('\<listaOpciones> ::= \<opCol>')
    p[0] = [p[1]]


def p_opCol_1(p):
    'opCol : default'
    bnf.addProduccion('\<opCol> ::= \<default>')
    p[0] = p[1]


def p_opCol_2(p):
    'opCol : constraints'
    bnf.addProduccion('\<opCol> ::= \<constraints>')
    p[0] = p[1]


def p_opCol_3(p):
    'opCol :  checks'
    bnf.addProduccion('\<opCol> ::= \<checks>')
    p[0] = p[1]


def p_opCol_4(p):
    'opCol :  PRIMARY KEY'
    bnf.addProduccion('\<opCol> ::= "PRIMARY" "KEY"')
    p[0]= ConstraintField(CONSTRAINT_FIELD.PRIMARY_KEY)


def p_opCol_5(p):
    'opCol : REFERENCES ID PABRE ID PCIERRA'
    bnf.addProduccion('\<opCol> ::= "REFERENCES" "ID" "(" "ID" ")"')
    p[0] = ForeignKeyField(p[2],p[4])


def p_opCol_6(p):
    'opCol : nullable'
    bnf.addProduccion('\<opCol> ::= \<nullable>')
    p[0] = p[1]


# __________________________________________ <TIPO>

# <TIPO> ::= 'smallint'
#         |  'integer'
#         |  'bigint'
#         |  'decimal'
#         |  'deecimal (numero , numero)'
#         |  'numeric'
#         |  'real'
#         |  'double' 'precision'
#         |  'money'
#         |  'character' 'varying' ('numero')
#         |  'varchar' ('numero')
#         |  'character' ('numero')
#         |  'char' ('numero')
#         |  'text'
#         |  <TIMESTAMP>
#         |  'date'
#         |  <TIME>
#         |  <INTERVAL>
#         |  'boolean'
#         |  ID 

def p_tipo_1(p):
    'tipo : SMALLINT'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.SMALLINT  


def p_tipo_2(p):
    'tipo : INTEGER'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.INTEGER


def p_tipo_3(p):
    'tipo : BIGINT'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.BIGINT

def p_tipo_4(p):
    'tipo : DECIMAL'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.DECIMAL

def p_tipo_5(p):
    'tipo : NUMERIC'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.NUMERIC

def p_tipo_6(p):
    'tipo : REAL'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.REAL

def p_tipo_7(p):
    'tipo : DOUBLE PRECISION'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}" "{p[2].upper()}"')
    p[0] = TYPE_COLUMN.DOUBLE_PRECISION
    

def p_tipo_8(p):
    'tipo : MONEY'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.MONEY


def p_tipo_9(p):
    'tipo : CHARACTER VARYING PABRE NUMERO PCIERRA'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}" "VARYING" "(" "NUMERO" ")"')
    p[0] = ( TYPE_COLUMN.VARCHAR, p[4] )

def p_tipo_10(p):
    'tipo : VARCHAR PABRE NUMERO PCIERRA'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}" "(" "NUMERO" ")"')
    p[0] = ( TYPE_COLUMN.VARCHAR, p[3] )

def p_tipo_11(p):
    'tipo : CHARACTER PABRE NUMERO PCIERRA'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}" "(" "NUMERO" ")"')
    p[0] = ( TYPE_COLUMN.CHAR, p[3] )

def p_tipo_12(p):
    'tipo : CHAR PABRE NUMERO PCIERRA'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}" "(" "NUMERO" ")"')
    p[0] = ( TYPE_COLUMN.CHAR, p[3] )


def p_tipo_13(p):
    'tipo : TEXT '
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.TEXT

# def p_tipo_14(p):
#     'tipo : timestamp'
#     bnf.addProduccion('\<opCol> ::= \<timestamp>')
#     p[0] = p[1]


def p_tipo_15(p):
    'tipo : DATE'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.DATE


def p_tipo_16(p):
    'tipo : time'
    bnf.addProduccion('\<tipo> ::= \<time>')
    p[0] = p[1]


def p_tipo_17(p):
    'tipo : interval'
    bnf.addProduccion('\<tipo> ::= \<interval>')
    p[0] = p[1]


def p_tipo_18(p):
    'tipo : BOOLEAN'
    bnf.addProduccion(f'\<tipo> ::="{p[1].upper()}"')
    p[0] = TYPE_COLUMN.BOOLEAN

def p_tipo_19(p):# produccion para los enum
    'tipo : ID'
    bnf.addProduccion('\<tipo> ::= "ID"')
    p[0] = p[1]

def p_tipo_20(p):
    'tipo : DECIMAL PABRE NUMERO COMA NUMERO PCIERRA'
    bnf.addProduccion(f'\<tipo> ::="DECIMAL" "(" "NUMERO" "," "NUMERO" ")"')
    p[0] = (TYPE_COLUMN.DECIMAL, (p[3],p[5]))

def p_tipo_21(p):
    'tipo : NUMERIC PABRE NUMERO COMA NUMERO PCIERRA'
    bnf.addProduccion(f'\<tipo> ::="NUMERIC" "(" "NUMERO" "," "NUMERO" ")"')
    p[0] = (TYPE_COLUMN.DECIMAL, (p[3],p[5]))
# __________________________________________ <INTERVAL>
# <INTERVAL> ::= 'interval' <FIELDS> ('numero')
#             |  'interval' <FIELDS>
#             |  'interval' ('numero')
#             |  'interval'


def p_interval_1(p):
    'interval : INTERVAL fields PABRE NUMERO PCIERRA'
    bnf.addProduccion('\<interval> ::= "INTERVAL" \<fields> "(" "NUMERO" ")"')
    p[0] = TYPE_COLUMN.INTERVAL


def p_interval_2(p):
    'interval : INTERVAL fields'
    bnf.addProduccion('\<interval> ::= "INTERVAL" \<fields>')
    p[0] = TYPE_COLUMN.INTERVAL


def p_interval_3(p):
    'interval : INTERVAL PABRE NUMERO PCIERRA'
    bnf.addProduccion('\<interval> ::= "INTERVAL" "(" "NUMERO" ")"')
    p[0] = TYPE_COLUMN.INTERVAL

def p_interval_4(p):
    'interval : INTERVAL '
    bnf.addProduccion('\<interval> ::= "INTERVAL"')
    p[0] = TYPE_COLUMN.INTERVAL

# _________________________________________ <fields>
# <FIELDS> ::= 'year'
#           |  'month'
#           |  'day'
#           |  'hour'
#           |  'minute'
#           |  'second'


def p_fields(p):
    '''fields : YEAR 
              | MONTH
              | DAY
              | HOUR
              | MINUTE
              | SECOND '''
    bnf.addProduccion(f'\<fields> ::= "{p[1].upper()}"')
    p[0] = p[1]  # fijo es un sintetizado

# __________________________________________ <time>
# <TIME> ::= 'time' ('numero') 'tmstamp'
#         |  'time' 'tmstamp'
#         |  'time' ('numero')
#         |  'time'


def p_time_1(p):
    'time : TIME PABRE NUMERO PCIERRA CADENA_DATE'
    bnf.addProduccion(f'\<time> ::= "{p[1].upper()}" "(" "NUMERO" ")" "CADENA_DATE"')
    p[0] = TYPE_COLUMN.TIME


def p_time_2(p):
    'time : TIME CADENA_DATE'
    bnf.addProduccion(f'\<time> ::= "{p[1].upper()}" "CADENA_DATE"')
    p[0] = TYPE_COLUMN.TIME


def p_time_3(p):
    'time : TIME PABRE NUMERO PCIERRA'
    bnf.addProduccion(f'\<time> ::= "{p[1].upper()}" "(" "NUMERO" ")"')
    p[0] = TYPE_COLUMN.TIME

def p_time_4(p):
    'time : TIME'
    bnf.addProduccion(f'\<time> ::= "{p[1].upper()}"')
    p[0] = TYPE_COLUMN.TIME

# __________________________________________ <DEFAULT>
# <DEFAULT> ::= 'default' <VALOR>


def p_default(p):
    'default : DEFAULT expresion'
    bnf.addProduccion(f'\<default> ::= "{p[1].upper()}" \<expresion>')
    p[0] = DefaultField(p[2])

# _________________________________________ <VALOR>
# falta la produccion valor , le deje expresion :v

# __________________________________________ <NULLABLE>
# <NULLABLE> ::= 'not' 'null'
#             | 'null'


def p_nullable_1(p):
    'nullable : NOT NULL'
    bnf.addProduccion(f'\<nullable> ::= "{p[1].upper()}" "NULL"')
    p[0] = ConstraintField(CONSTRAINT_FIELD.NULL, False)

def p_nullable_2(p):
    'nullable : NULL'
    bnf.addProduccion(f'\<nullable> ::= "{p[1].upper()}" ')
    p[0] = ConstraintField(CONSTRAINT_FIELD.NULL, True)
# __________________________________________ <CONSTRAINTS>
# <CONSTRAINTS> ::= 'constraint' id 'unique'
#                 | 'unique'


def p_constraints_1(p):
    'constraints : CONSTRAINT ID UNIQUE'
    bnf.addProduccion(f'\<constraints> ::= "{p[1].upper()}" "ID" "UNIQUE"')
    p[0] = ConstraintField(CONSTRAINT_FIELD.UNIQUE, p[2])


def p_constraints_2(p):
    'constraints : UNIQUE'
    bnf.addProduccion(f'\<constraints> ::= "{p[1].upper()}" ')
    p[0] = ConstraintField(CONSTRAINT_FIELD.UNIQUE)


#_________________________________________ <CHECKS>
# <CHECKS> ::= 'constraint' 'id' 'check' '('<EXPRESION>')'
#             |'check' '('<EXPRESION>')' 

def p_checks_1(p):
    'checks : CONSTRAINT ID CHECK PABRE expresion PCIERRA '
    bnf.addProduccion(f'\<checks> ::= "{p[1].upper()}" "ID" "CHECK" "(" \<expresion> ")" ')
    p[0] = CheckField(p[5], p[2])

def p_checks_2(p):
    'checks : CHECK PABRE expresion PCIERRA'
    bnf.addProduccion(f'\<checks> ::= "{p[1].upper()}" "(" \<expresion> ")" ')  
    p[0] = CheckField(p[3])







# __________________________________________update
def p_update(p):
    '''sentenciaUpdate : UPDATE ID SET lista_asignaciones WHERE expresion 
                       | UPDATE ID SET lista_asignaciones '''
    if (len(p) == 7):
        bnf.addProduccion(f'\<update> ::= "{p[1].upper()}" "ID" "SET" \<lista_asignaciones> "WHERE" \<expresion>') 
        p[0] = UpdateTable(tabla = p[2], asignaciones= p[4] , condiciones=p[6])
    else:
        bnf.addProduccion(f'\<update> ::= "{p[1].upper()}" "ID" "SET" \<lista_asignaciones>') 
        p[0] = UpdateTable(tabla = p[2], asignaciones= p[4])
# __________________________________________INSERT


def p_sentenciaInsert(p):
    ''' insert : INSERT INTO ID VALUES PABRE lista_exp PCIERRA'''
    p[0] = InsertTable(p[3],p[6],None,p.slice[1].lineno)
    bnf.addProduccion(f'\<insert> ::= "{p[1].upper()}" "INTO" "ID" "VALUES"  "( "\<lista_exp> ")"')
    
def p_sentenciaInsert2(p):
    ''' insert : INSERT INTO ID parametros VALUES PABRE lista_exp PCIERRA'''
    p[0] = InsertTable(p[3],p[7],p[4],p.slice[1].lineno)
    bnf.addProduccion(f'\<insert> ::= "{p[1].upper()}" "INTO" "ID" \<parametros> "VALUES"  "( "\<lista_exp> ")"') 
# ___________________________________________PARAMETROS


def p_parametros(p):
    ''' parametros : PABRE lista_ids  PCIERRA'''
    bnf.addProduccion('\<parametros> ::= "(" \<lista_ids> ")"') 
    p[0] = p[2]
# __________________________________________lista ids
# <LISTA_IDS> ::= <LISTA_IDS> ',' 'ID'
#          | 'ID'


def p_lista_ids(p):
    ''' lista_ids : lista_ids COMA  ID
                  | ID '''

    if (len(p) == 4):
        p[1].append(p[3])
        p[0] = p[1]
        bnf.addProduccion('\<lista_ids> ::= \<lista_ids> "," "ID"') 
    else:
        p[0] = [p[1]]
        bnf.addProduccion('\<lista_ids> ::= "ID"') 


# __________________________________________DELETE
def p_sentenciaDelete(p):
    ''' sentenciaDelete : DELETE FROM ID WHERE expresion
                        | DELETE FROM ID '''
    if len(p) == 6:
        p[0] = DeleteTabla(p[3],p[5],p.slice[1].lineno)
        bnf.addProduccion('\<delete> ::= "DELETE" "FROM" "ID" "WHERE" <expresion>')
    else:
        p[0] = DeleteTabla(p[3],None,p.slice[1].lineno)
        bnf.addProduccion('\<delete> ::= "DELETE" "FROM" "ID"')


# ___________________________________________ASIGNACION____________________________________

def p_lista_asignaciones(p):
    '''lista_asignaciones : lista_asignaciones COMA asignacion
                          | asignacion'''
    if (len(p) == 4):
        p[1].update(p[3])
        p[0] = p[1]
        bnf.addProduccion('\<lista_asignaciones> ::=  \<lista_asignaciones> "," \<asignacion>')
    else:
        p[0] = p[1]
        bnf.addProduccion('\<lista_asignaciones> ::= \<asignacion>')


def p_asignacion(p):
    ''' asignacion : ID IGUAL expresion'''
    bnf.addProduccion('\<asignacion> ::= "ID" "=" \<expresion>')
    p[0] = {p[1]:p[3]}


# ______________________________________________EXPRESION_______________________________
def p_expresionBooleanaTrue(p):
    '''expresion : TRUE '''
    p[0] = ExpresionBooleano(True, p.slice[1].lineno)
    bnf.addProduccion('\<expresion> ::= "TRUE"')

def p_expresionBooleanaFalse(p):
    '''expresion : FALSE '''
    p[0] = ExpresionBooleano(False, p.slice[1].lineno)
    bnf.addProduccion('\<expresion> ::= "FALSE"')
    
def p_exp_auxBooleanaTrue(p):
    '''exp_aux : TRUE '''
    p[0] = ExpresionBooleano(True, p.slice[1].lineno)
    bnf.addProduccion('\<exp_aux> ::= "TRUE"')

def p_exp_auxBooleanaFalse(p):
    '''exp_aux : FALSE '''
    p[0] = ExpresionBooleano(False, p.slice[1].lineno)
    bnf.addProduccion('\<exp_aux> ::= "FALSE"')   



def p_expresiones_unarias(p):
    ''' expresion : MENOS expresion %prec UMENOS 
                  | MAS expresion %prec UMAS
                  | NOT expresion %prec UNOT '''
    if p[1] == '+':
        p[0] = ExpresionPositiva(p[2], p.slice[1].lineno)
        bnf.addProduccion('\<expresion> ::= "-" \<expresion>')
    elif p[1] == '-':
        p[0] = ExpresionNegativa(p[2], p.slice[1].lineno)
        bnf.addProduccion('\<expresion> ::= "+" \<expresion>')
    else:
        p[0] = ExpresionNegada(p[2])
        bnf.addProduccion('\<expresion> ::= "NOT" \<expresion>')
    
def p_expresiones_is_complemento(p):
    'expresion : expresion IS TRUE'
    p[0] = ExpresionUnariaIs(p[1], p.slice[2].lineno, OPERACION_UNARIA_IS.IS_TRUE)
    bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "TRUE"')

def p_expresiones_is_complemento1(p):
    'expresion : expresion IS FALSE'
    p[0] = ExpresionUnariaIs(p[1], p.slice[2].lineno, OPERACION_UNARIA_IS.IS_FALSE)
    bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "FALSE"')

def p_expresiones_is_complemento2_false(p):
    'expresion : expresion IS NOT FALSE'
    p[0] = ExpresionUnariaIs(p[1], p.slice[2].lineno, OPERACION_UNARIA_IS.IS_NOT_FALSE)
    bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "NOT" "FALSE"')
    
def p_expresiones_is_complemento2_true(p):
    'expresion : expresion IS NOT TRUE'
    p[0] = ExpresionUnariaIs(p[1], p.slice[2].lineno, OPERACION_UNARIA_IS.IS_NOT_TRUE)
    bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "NOT" "TRUE"')
    
def p_expresiones_is_complemento4(p):
    'expresion : expresion IS NOT DISTINCT FROM expresion'
    p[0] = ExpresionBinariaIs(p[1], p[6], OPERACION_BINARIA_IS.IS_NOT_DISTINCT_FROM, p.slice[2].lineno)
    bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "NOT ""DISTINCT" "FROM" \<expresion>')


def p_expresion_in_subquery(p): 
    '''expresion : ID IN subquery'''
    bnf.addProduccion('\<expresion> ::= "IN" \<subquery>')

def p_expresion_not_in(p):
    'expresion : ID NOT_IN subquery'
    bnf.addProduccion('\<expresion> ::= "EXISTS" \<subquery>')
    
def p_expresion_exist(p):
    'expresion : EXISTS subquery'
    bnf.addProduccion('\<expresion> ::= "EXISTS" \<subquery>')
    
    

    
#def __init__(self, exp, linea, tipo):
def p_expresiones_is_complemento_nulleable(p):
    '''
    expresion    : expresion IS NULL    
                 | expresion IS NOT NULL '''
    if len(p) == 4:
        bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "NULL"')
        p[0] = ExpresionUnariaIs(p[1],p.slice[2].lineno, OPERACION_UNARIA_IS.IS_NULL)
    else:
        bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "NOT "NULL"')
        p[0] = ExpresionUnariaIs(p[1],p.slice[2].lineno, OPERACION_UNARIA_IS.IS_NOT_NULL)

        
def p_expresiones_is_complemento2(p):
    '''       
    expresion  : expresion ISNULL 
               | expresion NOTNULL'''
    if p[2].upper() == 'ISNULL':
        bnf.addProduccion('\<expresion> ::= \<expresion> "ISNULL"')
        p[0] = ExpresionUnariaIs(p[1],p.slice[2].lineno, OPERACION_UNARIA_IS.IS_NULL)
    else:
        bnf.addProduccion('\<expresion> ::= \<expresion> "NOTNULL"')
        p[0] = ExpresionUnariaIs(p[1],p.slice[2].lineno, OPERACION_UNARIA_IS.IS_NOT_NULL)
        
def p_expresiones_is_complemento5(p):               
    ''' expresion   : expresion IS UNKNOWN
                    | expresion IS NOT UNKNOWN '''
    if len(p) == 4:
        bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "UNKNOWN"')
    else: 
        bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "NOT" "UNKNOWN"')        
        
        
def p_expresiones_is_complemento6(p):     
    ''' expresion   : expresion IS DISTINCT FROM expresion '''
    bnf.addProduccion('\<expresion> ::= \<expresion> "IS" "DISTINCT" "FROM" \<expresion> ') 
    p[0] = ExpresionBinariaIs(p[1], p[5], OPERACION_BINARIA_IS.IS_DISTINCT_FROM, p.slice[2].lineno)



def p_expresion_ternaria(p): 
    '''expresion : expresion BETWEEN  exp_aux AND exp_aux
                 | expresion BETWEEN SYMMETRIC exp_aux AND exp_aux '''
    if len(p) == 6:
        bnf.addProduccion('\<expresion> ::= \<expresion> "BETWEEN" \<exp_aux> "AND" \<exp_aux>')
        p[0] = ExpresionBetween(p[1], p[3], p[5], BETWEEN.BETWEEN,p.slice[4].lineno)
    else:
        bnf.addProduccion('\<expresion> ::= \<expresion> "BETWEEN" "SYMMETRIC" \<exp_aux> "AND" \<exp_aux>')
        p[0] = ExpresionBetween(p[1], p[4], p[6], BETWEEN.BETWEEN_SYMMETRIC,p.slice[5].lineno)
        
def p_expresion_ternaria2(p):
    '''expresion : expresion NOTBETWEEN exp_aux AND exp_aux
                 | expresion NOTBETWEEN SYMMETRIC exp_aux AND exp_aux'''
    if len(p) == 6:
        bnf.addProduccion('\<expresion> ::= \<expresion> "NOTBETWEEN" \<exp_aux> "AND" \<exp_aux>')
        p[0] = ExpresionBetween(p[1], p[3], p[5], BETWEEN.NOT_BETWEEN,p.slice[4].lineno)
    else:
        bnf.addProduccion('\<expresion> ::= \<expresion> "NOTBETWEEN" "SYMMETRIC" \<exp_aux> "AND" \<exp_aux>')
        p[0] = ExpresionBetween(p[1], p[4], p[6], BETWEEN.NOT_BETWEEN_SYMMETRIC,p.slice[5].lineno)
        
        

def p_expreion_funciones(p):
    'expresion : funciones'
    bnf.addProduccion('\<expresion> ::= \<funciones>')
    p[0] = p[1]
    
def p_expreion_entre_parentesis(p):
    'expresion : PABRE expresion  PCIERRA'
    bnf.addProduccion('\<expresion> ::= "(" \<expresion> ")"')
    p[0] = ExpresionAgrupacion(p[2]) 

def p_expresion_primitivo(p):
    'expresion : CADENA'
    p[0] = ExpresionCadena(p[1], TIPO_DE_DATO.CADENA, p.slice[1].lineno)
    bnf.addProduccion(f'\<expresion> ::= "CADENA"')

def p_expresion_primitivo1(p):
    'expresion : NUMERO'
    p[0] = ExpresionNumero(p[1], TIPO_DE_DATO.ENTERO, p.slice[1].lineno)
    bnf.addProduccion(f'\<expresion> ::= "NUMERO"')

def p_expresion_primitivo2(p):
    'expresion : DECIMAL_LITERAL'
    p[0] = ExpresionNumero(p[1], TIPO_DE_DATO.DECIMAL, p.slice[1].lineno)
    bnf.addProduccion(f'\<expresion> ::= "DECIMAL_LITERAL"')

def p_expresion_id(p):
    'expresion : ID'
    p[0] = ExpresionID(p[1], p.slice[1].lineno)
    bnf.addProduccion(f'\<expresion> ::= "ID"')
    
def p_expresion_tabla_campo(p):
    'expresion : ID PUNTO ID'
    p[0] = ExpresionID(p[1]+"."+p[3], p.slice[1].lineno)
    bnf.addProduccion('\<exp_aux> ::= "ID" "." "ID"')
        

def p_expresion_cadenasDate(p):
    'expresion : CADENA_DATE'
    p[0] = ExpresionCadena(p[1], TIPO_DE_DATO.CADENA, p.slice[1].lineno , isFecha = True)
    bnf.addProduccion(f'\<expresion> ::= "CADENA_DATE"')
    
def p_expresion_con_dos_nodos(p):
    '''expresion : expresion MAS expresion 
                 | expresion MENOS expresion
                 | expresion ASTERISCO expresion
                 | expresion DIVISION expresion 
                 | expresion MAYOR expresion 
                 | expresion MENOR expresion
                 | expresion MAYORIGUAL expresion
                 | expresion MENORIGUAL expresion
                 | expresion DIFERENTE expresion
                 | expresion DIFERENTE2 expresion
                 | expresion IGUAL expresion
                 | expresion EXPONENT expresion
                 | expresion MODULO expresion
                 | expresion OR expresion
                 | expresion AND expresion
    '''
    bnf.addProduccion(f'\<expresion> ::= \<expresion> "{p.slice[2].value}" \<expresion>')
    if p[2] == '+':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MAS, p.slice[2].lineno)
    elif p[2] == '-':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MENOS, p.slice[2].lineno)
    elif p[2] == '*':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.POR, p.slice[2].lineno)
    elif p[2] == '/':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.DIVIDO, p.slice[2].lineno)
    elif p[2] == '%':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MODULO, p.slice[2].lineno)
    elif p[2] == '^':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.EXPONENTE, p.slice[2].lineno)
    elif p[2] == '<':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.MENOR, p.slice[2].lineno)
    elif p[2] == '>':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.MAYOR, p.slice[2].lineno)
    elif p[2] == '<=':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.MENORIGUAL, p.slice[2].lineno)
    elif p[2] == '>=':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.MAYORIGUAL, p.slice[2].lineno)
    elif p[2] == '=':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.IGUAL, p.slice[2].lineno)
    elif p[2] == '<>':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.DESIGUAL, p.slice[2].lineno)
    elif p[2] == '!=':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.DESIGUAL, p.slice[2].lineno)
    elif p[2] == 'and':
        p[0] = ExpresionLogica(p[1], p[3], OPERACION_LOGICA.AND, p.slice[2].lineno)
    elif p[2] == 'AND':
        p[0] = ExpresionLogica(p[1], p[3], OPERACION_LOGICA.AND, p.slice[2].lineno)
    elif p[2] == 'or':
        p[0] = ExpresionLogica(p[1], p[3], OPERACION_LOGICA.OR, p.slice[2].lineno)
    elif p[2] == 'OR':
        p[0] = ExpresionLogica(p[1], p[3], OPERACION_LOGICA.OR, p.slice[2].lineno)

#----------------------------------------------------------------------------------------------------- FIN EXPRESION
#<EXP_AUX>::= '-'  <EXP_AUX>
#          |    '+'  <EXP_AUX>
#          | <EXP_AUX>  '+'  <EXP_AUX>
#          | <EXP_AUX>  '-'  <EXP_AUX>
#          | <EXP_AUX>  '*'  <EXP_AUX>
#          | <EXP_AUX>  '/'  <EXP_AUX>
#          | <EXP_AUX>  '%'  <EXP_AUX>
#          | <EXP_AUX>  '^'  <EXP_AUX>
def p_exp_aux_unarias(p):
    ''' exp_aux : MENOS exp_aux %prec UMENOS 
                | MAS exp_aux %prec UMAS
                | NOT exp_aux'''
    if p[1] == '+':
        p[0] = ExpresionPositiva(p[2], p.slice[1].lineno)
        bnf.addProduccion('\<exp_aux> ::= "-" \<exp_aux>')
    elif p[1] == '-':
        p[0] = ExpresionNegativa(p[2], p.slice[1].lineno)
        bnf.addProduccion('\<exp_aux> ::= "+" \<exp_aux>')
    else:
        p[0] = ExpresionNegada(p[2])
        bnf.addProduccion('\<exp_aux> ::= "NOT" \<exp_aux>')


        
def p_exp_auxp(p):#TIENE LO MISMO QUE EXPRESION MENOS EL AND PORQUE DABA PROBLEMA DE SHIFT reduce por eso se creo esta mini expresion
    '''exp_aux : exp_aux MAS exp_aux 
                 | exp_aux MENOS exp_aux
                 | exp_aux ASTERISCO exp_aux
                 | exp_aux DIVISION exp_aux 
                 | exp_aux MAYOR exp_aux 
                 | exp_aux MENOR exp_aux
                 | exp_aux MAYORIGUAL exp_aux
                 | exp_aux MENORIGUAL exp_aux
                 | exp_aux DIFERENTE exp_aux
                 | exp_aux DIFERENTE2 exp_aux
                 | exp_aux IGUAL exp_aux
                 | exp_aux EXPONENT exp_aux
                 | exp_aux MODULO exp_aux
                 | exp_aux OR exp_aux
    '''
    bnf.addProduccion(f'\<exp_aux> ::= \<exp_aux> "{p.slice[2].value}" \<exp_aux>')
    if p[2] == '+':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MAS, p.slice[2].lineno)
    elif p[2] == '-':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MENOS, p.slice[2].lineno)
    elif p[2] == '*':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.POR, p.slice[2].lineno)
    elif p[2] == '/':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.DIVIDO, p.slice[2].lineno)
    elif p[2] == '%':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.MODULO, p.slice[2].lineno)
    elif p[2] == '^':
        p[0] = ExpresionAritmetica(p[1], p[3], OPERACION_ARITMETICA.EXPONENTE, p.slice[2].lineno)
    elif p[2] == '<':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.MENOR, p.slice[2].lineno)
    elif p[2] == '>':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.MAYOR, p.slice[2].lineno)
    elif p[2] == '<=':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.MENORIGUAL, p.slice[2].lineno)
    elif p[2] == '>=':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.MAYORIGUAL, p.slice[2].lineno)
    elif p[2] == '=':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.IGUAL, p.slice[2].lineno)
    elif p[2] == '<>':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.DESIGUAL, p.slice[2].lineno)
    elif p[2] == '!=':
        p[0] = ExpresionComparacion(p[1], p[3], OPERACION_RELACIONAL.DESIGUAL, p.slice[2].lineno)
    elif p[2] == 'or':
        p[0] = ExpresionLogica(p[1], p[3], OPERACION_LOGICA.OR, p.slice[2].lineno)
    elif p[2] == 'OR':
        p[0] = ExpresionLogica(p[1], p[3], OPERACION_LOGICA.OR, p.slice[2].lineno)

def p_expr_aux_cadenasDate(p):
    'exp_aux : CADENA_DATE'
    p[0] = ExpresionCadena(p[1], TIPO_DE_DATO.CADENA, p.slice[1].lineno , isFecha = True)
    bnf.addProduccion(f'\<exp_aux> ::= "CADENA_DATE"')
            
def p_exp_aux_entre_parentesis(p):
    'exp_aux : PABRE exp_aux  PCIERRA'
    bnf.addProduccion('\<exp_aux> ::= "(" \<exp_aux> ")"')
    p[0] = ExpresionAgrupacion(p[2]) 
#          | 'cadena'
def p_exp_aux_cadena(p):
    'exp_aux :  CADENA'
    p[0] = ExpresionCadena(p[1], TIPO_DE_DATO.CADENA, p.slice[1].lineno)
    bnf.addProduccion(f'\<exp_aux> ::= "CADENA"')
#          | 'numero'          
def p_exp_aux_numero(p):
    'exp_aux :  NUMERO'
    p[0] = ExpresionNumero(p[1], TIPO_DE_DATO.ENTERO, p.slice[1].lineno)
    bnf.addProduccion(f'\<exp_aux> ::= "NUMERO"')
#          | 'decimal'
def p_exp_aux_decimal(p):
    'exp_aux :  DECIMAL_LITERAL'
    p[0] = ExpresionNumero(p[1], TIPO_DE_DATO.DECIMAL, p.slice[1].lineno)
    bnf.addProduccion(f'\<exp_aux> ::= "DECIMAL_LITERAL"')
#          | 'id' '.' 'id'
def p_exp_aux_tabla(p):
    'exp_aux :  ID PUNTO ID'
    p[0] = ExpresionID(p[1]+"."+p[3], p.slice[1].lineno ,tabla = p[1]+"."+p[3])
    bnf.addProduccion('\<exp_aux> ::= "ID" "." "ID"')
#          | 'id'
def p_exp_aux_id(p):
    'exp_aux :  ID'
    p[0] = ExpresionID(p[1], p.slice[1].lineno , tabla = p[1])
    bnf.addProduccion('\<exp_aux> ::= "ID"')
#          | <FUNCIONES>
def p_exp_aux_funciones(p):
    'exp_aux :  funciones'
    bnf.addProduccion('\<exp_aux> ::= \<funciones>')
    p[0] = p[1]

#<SUBQUERY> ::= '('<SELECT>')'
def p_subquery(p):
        'subquery :  PABRE select PCIERRA'
        bnf.addProduccion('\<subquery> ::= "(" \<select> ")"')

#<WHERE> ::= 'where' <EXPRESION>
def p_where(p):
        'where : WHERE expresion'
        bnf.addProduccion('\<where> ::= "WHERE" \<expresion>')
        p[0] = WHERE(expresion=p[2])

#<GROUP_BY> ::= <LISTA_IDS>
def p_groupby(p):
        'group_by : GROUP BY lista_ids'
        bnf.addProduccion('\<group_by> ::= "GROUP" "BY" \<lista_ids>')

#<HAVING> ::= 'having' <EXPRESION>
def p_having(p):
        'having : HAVING expresion'
        bnf.addProduccion('\<having> ::= "HAVING" \<expresion>')

#    <ORDERS> ::= <ORDERBY>
def p_orders(p):
        'orders : orderby'
        bnf.addProduccion('\<orders> ::= \<orderby>')
        p[0] = [p[1]]
#                |<ORDERS> ',' <ORDERBY>
def p_orders1(p):
        'orders : orders COMA orderby'
        bnf.addProduccion('\<orders> ::= \<orders> "," <orderby>')
        p[1].append(p[3])
        p[0] = p[1]  

#    <ORDERBY> ::= 'order' 'by' <EXPRESION> <ASC_DEC> <NULLS>
def p_orderby(p):
        'orderby : ORDER BY expresion asc_dec nulls'
        bnf.addProduccion('\<orderby> ::= "ORDER" "BY" \<expresion> \<asc_dec> \<nulls>')
#               | 'order' 'by' <EXPRESION> <ASC_DEC>
def p_orderby1(p):
        'orderby : ORDER BY expresion asc_dec'
        bnf.addProduccion('\<orderby> ::= "ORDER" "BY" \<expresion> \<asc_dec>')
#                | 'order' 'by' <EXPRESION> <NULLS>
def p_orderby2(p):
        'orderby : ORDER BY expresion nulls'
        bnf.addProduccion('\<orderby> ::= "ORDER" "BY" \<expresion> \<nulls>')
#                | 'order' 'by' <EXPRESION>        
def p_orderby3(p):
        'orderby : ORDER BY expresion'
        bnf.addProduccion('\<orderby> ::= "ORDER" "BY" \<expresion>')

#    <ASC_DEC> ::= 'asc'
def p_asc_dec(p):
        'asc_dec : ASC'
        bnf.addProduccion('\<asc_dec> ::= "ASC"')
        p[0] =p[1]
#               | 'desc'
def p_asc_dec1(p):
        'asc_dec : DESC'
        bnf.addProduccion('\<asc_dec> ::= "DESC"')
        p[0] =p[1]

#<NULLS> ::= 'nulls' <FIRST_LAST>
def p_nulls(p):
        'nulls : NULLS first_last'
        bnf.addProduccion('\<nulls> ::= "NULLS" \<first_last>')

#   <FIRST_LAST> ::= 'first'
def p_first_last(p):
        'first_last : FIRST'
        bnf.addProduccion('\<first_last> ::= "FIRST"')
        p[0] =p[1]
#                |    'last'
def p_first_last1(p):
        'first_last : LAST'
        bnf.addProduccion('\<first_last> ::= "LAST"')
        p[0] =p[1]
def p_select_item1(p):
    'select_item : exp_aux'
    bnf.addProduccion('\<select_item> ::= \<exp_aux>')
    p[0] = p[1]
# ESTAS 3 POSIBILIDADES YA ESTAN CONSIDERADAS EN EXP_AUX
#    <SELECT_ITEM>::=  'id'
#                  | 'id' '.' 'id'
#                  | select_item : funciones'

def p_select_item2(p):
        'select_item : count'
        bnf.addProduccion('\<select_item> ::= \<count>')
        p[0] = p[1]
#                  | <AGGREGATE_F>
# def p_select_item3(p):# AHORA ESTAS ESTARAN EN LA PROCUCCION >FUNCIONES>
#         'select_item : aggregate_f'
#         bnf.addProduccion('\<select_item> ::= \<aggregate_f>')
#         p[0] = p[1]
#                  | <SUBQUERY>
def p_select_item4(p):
        'select_item : subquery'
        bnf.addProduccion('\<select_item> ::= \<subquery>')
        p[0] = p[1]
#                  | <CASE>
def p_select_item5(p):
        'select_item : case'
        bnf.addProduccion('\<select_item> ::= \<case>')
        p[0] = p[1]
#                  | <GREATEST>
def p_select_item6(p):
        'select_item : greatest'
        bnf.addProduccion('\<select_item> ::= \<greatest>')
        p[0] = p[1]
#                  | <LEAST>
def p_select_item7(p):
        'select_item : least'
        bnf.addProduccion('\<select_item> ::= \<least>')
        p[0] = p[1]

        
def p_select_item9(p):
        'select_item : ASTERISCO'
        bnf.addProduccion('\<select_item> ::= "ASTERISCO"')
        p[0] = p[1]
        
def p_select_item10(p):
        'select_item : ID PUNTO ASTERISCO'
        p[0] = ExpresionID(p[1]+"."+p[3], p.slice[1].lineno ,tabla = p[1]+"."+p[3])
        bnf.addProduccion('\<select_item> ::= "ID" "." "*"')

#    <COUNT> ::= 'count' '(' '*' ')'  
def p_count(p):
        'count : COUNT PABRE ASTERISCO PCIERRA'
        bnf.addProduccion('\<count> ::= "COUNT" "(" "*" ")"')
#             |  'count' '(' 'id' ')'
def p_count1(p):
        'count : COUNT PABRE ID PCIERRA'
        bnf.addProduccion('\<count> ::= "COUNT" "(" "ID" ")"')
#             |  'count' '(' 'distinct' 'id' ')' 
def p_count2(p):
        'count : COUNT PABRE DISTINCT ID PCIERRA'
        bnf.addProduccion('\<count> ::= "COUNT" "(" "DISTINCT" "ID" ")"')

#    <AGGREGATE_F> ::= 'sum' '(' 'id' ')'
def p_aggregate_f(p):
        'aggregate_f : SUM PABRE exp_aux PCIERRA'
        bnf.addProduccion('\<aggregate_f> ::= "SUM" "(" \<exp_aux> ")"')
#                |     'avg' '(' 'id' ')'
def p_aggregate_f1(p):
        'aggregate_f : AVG PABRE exp_aux PCIERRA'
        bnf.addProduccion('\<aggregate_f> ::= "AVG" "(" \<exp_aux> ")"')
#                |     'max' '(' 'id' ')'
def p_aggregate_f2(p):
        'aggregate_f : MAX PABRE exp_aux PCIERRA'
        bnf.addProduccion('\<aggregate_f> ::= "MAX" "(" \<exp_aux> ")"')
#                |     'min' '(' 'id' ')'
def p_aggregate_f3(p):
        'aggregate_f : MIN PABRE exp_aux PCIERRA'
        bnf.addProduccion('\<aggregate_f> ::= "MIN" "(" \<exp_aux> ")"')

#    <CASE> ::= 'case' <SUBCASE> <ELSE_CASE> 'end'
def p_case(p):
        'case : CASE subcase else_case END'
        bnf.addProduccion('\<case> ::= "CASE" \<subcase> \<else_case> "END"')
#             | 'case' <SUBCASE> 'end'   
def p_case1(p):
        'case : CASE subcase END ID'
        bnf.addProduccion('\<case> ::= "CASE" \<subcase>  "END" "ID"')   
#    <SUBCASE> ::= <WHEN_CASE>
def p_subcase(p):
        'subcase : when_case'
        bnf.addProduccion('\<subcase> ::= \<when_case>')
        p[0] = [p[1]]
#                | <SUBCASE> <WHEN_CASE>
def p_subcase1(p):
        'subcase : subcase when_case'
        bnf.addProduccion('\<subcase> ::= \<subcase> \<when_case>')
        p[1].append(p[2])
        p[0] = p[1]  

#<ELSE_CASE> ::= 'else' <EXPRESION>
def p_else_case(p):
        'else_case : ELSE expresion'
        bnf.addProduccion('\<else_case> ::= "ELSE" \<expresion>')
#<WHEN_CASE> ::= 'when' <EXPRESION> 'then' <EXPRESION>
def p_when_case(p):
    'when_case : WHEN expresion THEN expresion'
    bnf.addProduccion('\<when_case> ::=  "WHEN" \<expresion> "THEN" \<expresion>') 
#<GREATEST> ::= 'greatest' '(' <LISTA_EXP>')'
def p_greatiest(p):
        'greatest : GREATEST PABRE lista_exp PCIERRA'
        bnf.addProduccion('\<greatest> ::= "GREATEST" "(" \<lista_exp> ")"')

#<LEAST> ::= 'least' '(' <LISTA_EXP> ')'
def p_least(p):
        'least : LEAST PABRE lista_exp PCIERRA'
        bnf.addProduccion('\<least> ::= "LEAST" "(" \<lista_exp> ")"')

# <LISTA_EXP> ::= <EXPRESION>
#            | <LISTA_EXP> ',' <EXPRESION>

def p_lista_exp_1(p):
    'lista_exp : expresion'
    bnf.addProduccion('\<lista_exp> ::= \<expresion>')
    p[0] = [p[1]]

def p_lista_exp_2(p):
    'lista_exp : lista_exp COMA expresion'  
    p[1].append(p[3])
    p[0] = p[1]
    bnf.addProduccion('\<lista_exp> ::=  \<lista_exp> "," \<expresion>')  

        
def p_alias(p):
    '''alias : CADENA ''' # VALIDACION SEMANTICA QUE ESTA CADENA VENGA ENTRR COMILLAS DOBLES
    p[0] = p[1]
    bnf.addProduccion('\<alias> ::= "CADENA"')
    
def p_alias2(p):
    '''alias : ID '''
    p[0] = p[1]
    bnf.addProduccion('\<alias> ::= "ID"')
    

def p_error(p):
    print(p)
    try:
        error = ErrorReport('sintactico', f'No se esperaba el token de tipo: {p.type}  valor: {p.value}', p.lineno)
        listaErrores.addError(error)
        print("Error sintáctico en '%s'" % p.value)
    except:
        print("no se recupero del error porque no encontro punto y coma")
        error = ErrorReport('sintactico','no se recupero del error porque no encontro punto y coma',0)
        listaErrores.addError(error)





parser = yacc.yacc()


def analizarEntrada(entrada):
    return parser.parse(entrada)

arbolParser = analizarEntrada('''
use test;

create table tbpuesto 
( idpuesto smallint not null,
  puesto character(25),
  salariobase money,
 primary key (idpuesto)
);

insert into tbpuesto values (1,'Recepcionista','4,000');

alter table tbpuesto
add column tinecomision boolean;

insert into tbpuesto values (2,'Asistente Contable','4,500',false);
insert into tbpuesto values(3,'Contador General','9000',false);
insert into tbpuesto values(4,'Asistente de RRHH','4000',false);
insert into tbpuesto values(5,'Recepcionista Gerencia','5000',false);
insert into tbpuesto values(6,'Vendedor 1','2500',true);
insert into tbpuesto values(7,'Vendedor 2','2750',true);
insert into tbpuesto values(8,'Vendedor 3','3000',true);
insert into tbpuesto values(9,'Jefe de Ventas','4000',true);
insert into tbpuesto values(10,'Jefe de Ventas Regional','2500',true);

CREATE TYPE area AS ENUM ('CONTABILIDAD','ADMINISTRACION','VENTAS','TECNOLOGIA','FABRICA');


CREATE TABLE tbempleadopuesto
(
	idempleado integer not null,
	idpuesto   integer not null,
	departamento area
);

 alter table tbempleadopuesto
 add constraint FK_empleado
 foreign key (idempleado)
 references tbempleado(idempleado);
  
 alter table tbempleadopuesto
 add constraint FK_empleado
 foreign key (idempleado)
 references tbempleado(idempleado);
  
  
insert into tbempleadopuesto values(1,1,'ADMINISTRACION');
insert into tbempleadopuesto values(2,1,'CONTABILIDAD');
insert into tbempleadopuesto values(3,3,'CONTABILIDAD');
insert into tbempleadopuesto values(4,6,'VENTAS');
insert into tbempleadopuesto values(5,6,'VENTAS');


UPDATE tbempleadopuesto SET idpuesto = 2 where idempleado = 2;

create table tbventa 
(  idventa integer not null primary key,
   idempleado integer,
   fechaventa date constraint validaventa check (fechaventa > '1900-01-01'),
   montoventa money constraint ventavalida check (montoventa > '0'),
   ventaregistrada boolean,
   descripcion text
);


insert into tbventa values(1,4,'2020-10-12',450,false,'Venta de bomba de agua para toyota');
insert into tbventa values(2,4,'2020-10-13',250,false,'Tasa distribuidor Mazda 626');
insert into tbventa values(3,4,'2020-10-13',650,false,'Radiador para Mazda 626');
insert into tbventa values(4,4,'2020-10-13',125,false,'Filtro de aire volkswagen');
insert into tbventa values(5,4,'2020-10-13',175,false,'Juego de Candelas volkswagen');
insert into tbventa values(6,4,'2020-10-13',220,false,'Aceite 20w50');
insert into tbventa values(7,5,'2020-10-13',1250,false,'Cremallera Mazda 3');
insert into tbventa values(8,5,'2020-10-14',980,false,'Cremallera timon hidraulico mazda');
insert into tbventa values(9,5,'2020-10-14',1200,false,'Lodera Universal para pickup');
insert into tbventa values(10,5,'2020-10-14',475,false,'Sobre Lodera de Fibra de Carbon');
insert into tbventa values(11,5,'2020-10-14',780,false,'Bomba Auxiliar de agua para volkswagen');
insert into tbventa values(12,4,'2020-10-14',3500,false,'Bomba de agua para volkswagen');
insert into tbventa values(13,5,'2020-10-14',200,false,'Compresor de aire acondicionado');
insert into tbventa values(14,5,'2020-10-15',2000,false,'Bomba Auxiliar de agua para volkswagen');

 

''')
arbolParser.ejecutar()

# create table tb1(
#   numerica integer,
#   cadena varchar(40)
# );


# create table tb2(
#   numerica integer,
#   cadena varchar(40)
# );

# insert into tb1 values (70,'adios');
# insert into tb1 values (99,'hola');
# insert into tb2 values (200,'oracle');
# insert into tb2 values (44,'nuevo');
