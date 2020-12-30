#PARSER
import ply.yacc as yacc
import lexico
import nodo as grammer
import graficas as generar
from instruccion import * 
from expresiones import *

import ReporteErrores 

listGrammer= []
listArbol = []
listDirecciones =[]

tokens = lexico.tokens

precedence = (
    ('left', 'mas', 'menos'),
    ('left', 'por', 'division'),
    ('nonassoc','between', 'like'),
    ('left', 'menor', 'mayor', 'igual', 'menorigual', 'mayorigual', 'diferente'),
    ('right', 'not'),
    ('left', 'and'),
    ('left', 'or')
)


def p_inicio(t):
        'inicio : instrucciones'
        var1 = id(t[1])
        var2 = id(t[0])
        node = grammer.nodoArbol(var1,'inicio')
        listArbol.append(node)
        direc = grammer.nodoDireccion(var1)
        direc.agregar(var2)
        listDirecciones.append(direc)
        instru = grammer.nodoGramatical('Inicio')
        listGrammer.insert(0, instru)
        t[0] = t[1]

def p_instrucciones(t):
        'instrucciones : instrucciones NEWLINE instruccion'
        instru = grammer.nodoGramatical('INSTRUCCIONES')
        instru.agregarDetalle('INSTRUCCIONES')
        instru.agregarDetalle('INSTRUCCION')
        listGrammer.insert(0,instru)
        t[1].append(t[3])
        t[0] = t[1]
        


def p_instrucciones2(t):
        'instrucciones : instruccion'
        instru= grammer.nodoGramatical('INSTRUCCIONES ')
        instru.agregarDetalle('INSTRUCCION No terminal')
        listGrammer.insert(0, instru)
        t[0]= [t[1]]

def p_instruccion(t):
        '''instruccion : ddl
			| dml'''
        isntru = grammer.nodoGramatical('INSTRUCCION')
        isntru.agregarDetalle('| DDL')
        isntru.agregarDetalle('| DML')
        listGrammer.insert(0,isntru)
        t[0] = t[1]

def p_ddl(t):
        '''ddl : sentencia_create
			| sentencia_alter
			| sentencia_drop
			| sentencia_truncate'''

        instr = grammer.nodoGramatical('DDL')
        instr.agregarDetalle('| SENTENCIA_CREATE')
        instr.agregarDetalle('| SENTENCIA_ALTER')
        instr.agregarDetalle('| SENTENCIA_DROP')
        instr.agregarDetalle('| SENTENCIA_TRUNCATE')
        listGrammer.insert(0,instr)
        t[0] = insDDL(t[1])
def p_dml(t):
        '''dml : sentencia_insert
			| sentencia_update
			| sentencia_delete
			| sentencia_select
			| sentencia_show'''
        instr = grammer.nodoGramatical('DML')
        instr.agregarDetalle(' SENTENCIA_INSERT')
        instr.agregarDetalle('| SENTENCIA_UPDATE')
        instr.agregarDetalle('| SENTENCIA_DELETE')
        instr.agregarDetalle('| SENTENCIA_SELECT')
        instr.agregarDetalle('| SENTENCIA_SHOW')
        listGrammer.insert(0,instr)
        t[0] = insDML(t[1])
        

#----------DDL----------
#CREAR
def p_crear(t):
        '''sentencia_create : create create_cont
				        | replace create_cont'''

        instru = grammer.nodoGramatical('SENTENCIA_CREATE')
        
        
        
        if t[1] =='create':
                instru.agregarDetalle('create CREATE_CONT')
                t[0] = Create(t[2])

        else:
                instru.agregarDetalle(' replace CREATE_CONT')
                t[0] = Replace(t[2])

        listGrammer.insert(0,instru)

def p_create_cont(t):
        'create_cont : database if_not pyc'
        instru = grammer.nodoGramatical('CREATE_CONT')
        instru.agregarDetalle('database')
        instru.agregarDetalle('IF_NOT')
        instru.agregarDetalle(';')
        listGrammer.insert(0,instru)
        t[0]= CreateDatabase(t[2])

def p_create_cont2(t):
        'create_cont : table if_not par1 col_tabla par2 fin_tabla '
        instru = grammer.nodoGramatical('CREATE_CONT')
        instru.agregarDetalle('table ')
        instru.agregarDetalle('IF_NOT')
        instru.agregarDetalle('( ')
        instru.agregarDetalle('COL_TABLA')
        instru.agregarDetalle(') ')
        instru.agregarDetalle('FIN_TABLA')
        listGrammer.insert(0, instru)
	#codigo para guardar contenido
        t[0]= CreateTable(t[2], t[4], t[6])

def p_create_cont3(t):
        'create_cont : type valor as enum par1 lista_insertar par2 pyc'
        instru = grammer.nodoGramatical('CREATE_CONT')
        instru.agregarDetalle('type')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('as')
        instru.agregarDetalle('enum')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('LISTA_INSERTAR')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0]= CreateType(t[2], t[6])

def p_inherits(t):
        'fin_tabla : inherits par1 identificador par2 pyc'
        instru = grammer.nodoGramatical('FIN_TABLA')
        instru.agregarDetalle('inherits')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0]= inherencia(t[3])

def p_inherits2(t):
        'fin_tabla : pyc'
        instru = grammer.nodoGramatical('FIN_TABLA')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Empty(t[1])

def p_if_not(t):
        'if_not : if not exists identificador'
        instru = grammer.nodoGramatical('IF_NOT')
        instru.agregarDetalle('if')
        instru.agregarDetalle('not')
        instru.agregarDetalle('exists')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = IfExist(False,t[4])

def p_if_not2(t):
        'if_not : identificador'
        instru = grammer.nodoGramatical('IF_NOT')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0]=ids(t[1])

def p_if_not3(t):
        'if_not : if not exists identificador owner igual valor'
        instru = grammer.nodoGramatical('IF_NOT')
        instru.agregarDetalle('if')
        instru.agregarDetalle('not')
        instru.agregarDetalle('exists')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('owner')
        instru.agregarDetalle('igual')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)
        t[0] = IfExist2(False,t[4], t[5], t[6])

def p_if_not4(t):
        'if_not : identificador owner valor'
        instru = grammer.nodoGramatical('IF_NOT')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('owner')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)
        t[0] = IfExist2(valido.invalido, t[1], t[2], t[3] )
def p_if_not5(t):
        'if_not : if not exists identificador mode igual valor'
        instru = grammer.nodoGramatical('IF_NOT')
        instru.agregarDetalle('if')
        instru.agregarDetalle('not')
        instru.agregarDetalle('exists')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('mode')
        instru.agregarDetalle('igual')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)
        t[0] = modo(False, t[4], t[7])

def p_if_not6(t):
        'if_not : identificador mode igual valor'
        instru = grammer.nodoGramatical('IF_NOT')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('mode')
        instru.agregarDetalle('igual')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)
        t[0] = modo(valido.invalido, t[1], t[4])

def p_col_tabla(t):
        'col_tabla : col_tabla coma identificador tipo propiedades'
        instru = grammer.nodoGramatical('COL_TABLA')
        instru.agregarDetalle('COL_TABLA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('TIPO')
        instru.agregarDetalle('PROPIEDADES')
        listGrammer.insert(0,instru)
        
        vars = [t[1]]
        t[1].append(propCol(t[3] , t[4] , t[5]))
        t[0]= t[1]

def p_col_tabla2(t):
        'col_tabla : col_tabla coma identificador tipo'
        instru = grammer.nodoGramatical('COL_TABLA')
        instru.agregarDetalle('COL_TABLA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('TIPO')
        listGrammer.insert(0,instru)
        vars = [t[1]]
        t[1].append(propCol(t[3] , t[4] , valido.invalido))
        t[0]= t[1]

def p_col_tabla3(t):
        'col_tabla : identificador tipo propiedades'
        instru = grammer.nodoGramatical('COL_TABLA')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('TIPO')
        instru.agregarDetalle('PROPIEDADES')
        listGrammer.insert(0,instru)   
        vars = propCol(t[1] , t[2] , t[3]) 
        t[0] = [vars]

def p_col_tabla4(t):
        'col_tabla : identificador tipo'
        instru = grammer.nodoGramatical('COL_TABLA')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('TIPO')
        listGrammer.insert(0,instru)
        vars= propCol(t[1] , t[2] , valido.invalido)
        t[0] = [vars]

def p_col_tabla5(t):
        'col_tabla : foreing key lista_id references identificador'
        instru = grammer.nodoGramatical('COL_TABLA')
        instru.agregarDetalle('foreing')
        instru.agregarDetalle('key')
        instru.agregarDetalle('LISTA_ID')
        instru.agregarDetalle('references')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = [foreingKey(t[3], t[5])]
        

def p_col_tabla6(t):
        'col_tabla : col_tabla coma primary key lista_id'
        instru = grammer.nodoGramatical('COL_TABLA')
        instru.agregarDetalle('COL_TABLA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('primary')
        instru.agregarDetalle('key')
        instru.agregarDetalle('LISTA_ID')
        listGrammer.insert(0,instru)
        vars = [t[1]]
        t[1].append(primaryKey(t[5]))
        t[0] =t[1]

def p_propiedades(t):
        'propiedades : null propiedades'
        instru = grammer.nodoGramatical('PROPIEDADES')
        instru.agregarDetalle('null')
        instru.agregarDetalle('PROPIEDADES')
        listGrammer.insert(0,instru)
        t[0]= propiedad('Null', t[2])

def p_propiedades2(t):
        'propiedades : not null propiedades'
        instru = grammer.nodoGramatical('PROPIEDADES')
        instru.agregarDetalle('not')
        instru.agregarDetalle('null')
        instru.agregarDetalle('PROPIEDADES')
        listGrammer.insert(0,instru)
        t[0]= propiedad('notNull', t[2])

def p_propiedades3(t):
        'propiedades : identity propiedades'
        instru = grammer.nodoGramatical('PROPIEDADES')
        instru.agregarDetalle('identity')
        instru.agregarDetalle('PROPIEDADES')
        listGrammer.insert(0,instru)
        t[0]= propiedad('identity', t[2])

def p_propiedades4(t):
        'propiedades : primary key propiedades '
        instru = grammer.nodoGramatical('PROPIEDADES')
        instru.agregarDetalle('primary')
        instru.agregarDetalle('key')
        instru.agregarDetalle('PROPIEDADES')
        listGrammer.insert(0,instru)

        t[0] = primaryKey(t[3])

def p_propiedades5(t):
        'propiedades : null'
        instru = grammer.nodoGramatical('PROPIEDADES')
        instru.agregarDetalle('null')
        listGrammer.insert(0,instru)   
        t[0]= propiedad('null', valido.invalido) 

def p_propiedades6(t):
        'propiedades : not null'
        instru = grammer.nodoGramatical('PROPIEDADES')
        instru.agregarDetalle('not')
        instru.agregarDetalle('null')
        listGrammer.insert(0,instru)
        t[0]= propiedad('notNull' , valido.invalido)

def p_propiedades7(t):
        'propiedades : identity'
        instru = grammer.nodoGramatical('PROPIEDADES')
        instru.agregarDetalle('identity')
        listGrammer.insert(0,instru)

        t[0] = propiedad(t[1], valido.invalido)


def p_propiedades8(t):
        'propiedades : primary key'
        instru = grammer.nodoGramatical('PROPIEDADES')
        instru.agregarDetalle('primary')
        instru.agregarDetalle('key')
        listGrammer.insert(0,instru)
        t[0] = primaryKey(valido.invalido)

def p_tipo(t):
        '''tipo    : smallint
	        | integer
	        | bigint
	        | decimal
	        | numeric
	        | real
	        | double
	        | money
	        | character
	        | text
	        | date
	        | boolean
	        | int
	        | identificador'''
        instru = grammer.nodoGramatical('TIPO')
        instru.agregarDetalle(t[1])
        listGrammer.insert(0,instru)
        t[0] = tiposD(t[1], '')

def p_tipo2(t):
        'tipo : varying par1 num par2'
        instru = grammer.nodoGramatical('TIPO')
        instru.agregarDetalle('varying')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('num')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = tiposD(tipod.VARYING, t[3])

def p_tipo3(t):
        'tipo : varchar par1 num par2'
        instru = grammer.nodoGramatical('TIPO')
        instru.agregarDetalle('varchar')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('num')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = tiposD(tipod.VARCHAR, t[3])

def p_tipo4(t):
        'tipo : character par1 num par2'
        instru = grammer.nodoGramatical('TIPO')
        instru.agregarDetalle('character')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('num')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = tiposD(tipod.CHARACTER, t[3])

def p_tipo5(t):
        'tipo : char par1 num par2'
        instru = grammer.nodoGramatical('TIPO')
        instru.agregarDetalle('char')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('num')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)

        t[0] = tiposD(tipod.CHA,t[3])

#ALTER
def p_alter(t):
        'sentencia_alter : alter alter_objeto'
        instru = grammer.nodoGramatical('ALTER_OBJETO')
        instru.agregarDetalle('alter')
        instru.agregarDetalle('ALTER_OBJETO')
        listGrammer.insert(0,instru)

        t[0] = [alter(t[2])]

def p_alter_objeto(t):
        'alter_objeto : table identificador alter_cont pyc'
        instru = grammer.nodoGramatical('ALTER_OBJETO')
        instru.agregarDetalle('table')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('ALTER_CONT')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = tabla(t[2], t[3])

def p_alter_objeto2(t):
        '''alter_objeto : database identificador rename to identificador pyc
                        | database identificador owner to identificador pyc'''
        instru = grammer.nodoGramatical('ALTER_OBJETO')
        instru.agregarDetalle('database')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle(t[3])
        instru.agregarDetalle('to')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = dataBase(t[2], t[3] , t[5])


#8+1+13+1524+122, 111545621+415,

def p_alter_cont(t):
        '''alter_cont : add con_add
        		| drop con_drop
        		| rename con_rename
        		| alter con_alter'''
        instru = grammer.nodoGramatical('ALTER_CONT')
        instru.agregarDetalle(t[1])
        #pendiente de difinir t[2]
        
        if t[1] == 'add':
                instru.agregarDetalle('add')
                instru.agregarDetalle('CON_ADD')

        elif  t[1] == 'drop':
                instru.agregarDetalle('drop')
                instru.agregarDetalle('CON_DROP')
        
        elif t[1] == 'rename':
                instru.agregarDetalle('rename')
                instru.agregarDetalle('CON_RENAME')

        elif t[1] == 'alter':
                instru.agregarDetalle('alter')
                instru.agregarDetalle('CON_ALTER')
        listGrammer.insert(0,instru)
        t[0]= t[2]

def p_con_add(t):
        'con_add : column identificador tipo'
        instru = grammer.nodoGramatical('CON_ADD')
        instru.agregarDetalle('column')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('TIPO')
        listGrammer.insert(0,instru)

        t[0] = conAdd(columnas(t[2], t[3]))

def p_con_add2(t):
        '''con_add : check  par1 valor diferente vacio par2'''
        instru = grammer.nodoGramatical('CON_ADD')
        instru.agregarDetalle('check')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('diferente')
        instru.agregarDetalle('vacio')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)

        t[0] = conAdd(checks(t[3]))

def p_con_add3(t):
        'con_add : foreing key par1 identificador par2 references identificador'
        instru = grammer.nodoGramatical('CON_ADD')
        instru.agregarDetalle('foreing')
        instru.agregarDetalle('key')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('referencias')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = conAdd(foreingKey(t[4], t[7]))

def p_con_drop(t):
        '''con_drop : column identificador
        		| constraint identificador '''
        instru = grammer.nodoGramatical('CON_DROP')
        instru.agregarDetalle(t[1])
        instru.agregarDetalle(t[2])
        listGrammer.insert(0,instru)
        t[0]= conDrop(t[1] , t[2])


def p_con_rename(t):
        'con_rename : column identificador to identificador'
        instru = grammer.nodoGramatical('CON_RENAME')
        instru.agregarDetalle('column')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('to')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)

        t[0]= conRename(t[1] , t[2])

def p_con_alter(t):
        'con_alter : column identificador set not null'
        instru = grammer.nodoGramatical('CON_ALTER')
        instru.agregarDetalle('column')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('set')
        instru.agregarDetalle('not')
        instru.agregarDetalle('null')
        listGrammer.insert(0,instru)
        t[0] = ConAlter(t[2], False)

#DROP
def p_drop(t):
        'sentencia_drop : drop objeto if_exist pyc'
        instru = grammer.nodoGramatical('SENTENCIA_DROP')
        instru.agregarDetalle('drop')
        instru.agregarDetalle('OBJETO')
        instru.agregarDetalle('IF_EXIST')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Drop(t[2] , t[3])

def p_if_exist(t): 
        'if_exist :  if exists identificador'
        instru = grammer.nodoGramatical('IF_EXIST')
        instru.agregarDetalle('if')
        instru.agregarDetalle('exists')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = IfExist(True,t[3])



def p_if_exist2(t): 
        'if_exist :  identificador'
        instru = grammer.nodoGramatical('IF_EXIST')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0]= ids(t[1])
        

def p_objeto(t):
        '''objeto : table
        	   | database'''
        instru = grammer.nodoGramatical('OBJETO')
        instru.agregarDetalle(t[1])
        listGrammer.insert(0,instru)
        t[0] = Objeto(t[1])

#TRUNCATE
def p_truncate(t):
        'sentencia_truncate : truncate table identificador pyc'
        instru = grammer.nodoGramatical('SENTENCIA_TRUNCATE')
        instru.agregarDetalle('truncate')
        instru.agregarDetalle('table')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)

        t[0]= Truncate(t[3])

#----------DML----------
#INSERT
def p_insert(t):
        'sentencia_insert : insert into identificador insert_cont pyc'
        instru = grammer.nodoGramatical('SENTENCIA_INSERT')
        instru.agregarDetalle('insert')
        instru.agregarDetalle('into')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('INSERT_CONT')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)

        t[0] = INSERTAR(t[3], t[4])

def p_insert_cont(t):
        'insert_cont : values par1 lista_insertar par2'
        instru = grammer.nodoGramatical('INSERT_CONT')
        instru.agregarDetalle('values')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('LISTA_INSERTAR')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)

        t[0] = InsertarCont(t[1] , t[3])
                

def p_insert_cont2(t):
        'insert_cont : par1 lista_campos par2 values par1 lista_insertar par2'
        instru = grammer.nodoGramatical('INSERT_CONT')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('LISTA_CAMPOS')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('values')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('LISTA_INSERTAR')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = InsertarCont2(t[2], t[4] , t[6])


        

def p_lista_campos(t):
        'lista_campos : lista_campos coma identificador'
        instru = grammer.nodoGramatical('LISTA_CAMPOS')
        instru.agregarDetalle('LISTA_CAMPOS')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        vars =[t[1]]
        vars.append(ids(t[3]))
        t[0]= vars

def p_lista_campos3(t):
        'lista_campos : identificador'
        instru = grammer.nodoGramatical('LISTA_CAMPOS')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = ids(t[1])

def p_valor(t):
        'valor : num'
        instru = grammer.nodoGramatical('VALOR')
        instru.agregarDetalle('num')
        listGrammer.insert(0,instru)
        t[0] = numero(t[1])

def p_valor7(t):
        'valor : menos num'
        instru = grammer.nodoGramatical('VALOR')
        instru.agregarDetalle('num')
        listGrammer.insert(0,instru)
        t[0] = numeroM(t[2])


def p_valor2(t):
        'valor : cadena'
        instru = grammer.nodoGramatical('VALOR')
        instru.agregarDetalle('cadena')
        listGrammer.insert(0,instru)
        t[0]= cadena(t[1])
                
def p_valor3(t):
        'valor : pdecimal'
        instru = grammer.nodoGramatical('VALOR')
        instru.agregarDetalle('pdecimal')
        listGrammer.insert(0,instru)

        t[0] = numDecimal(t[1])
def p_valor8(t):
        'valor : menos pdecimal'
        instru = grammer.nodoGramatical('VALOR')
        instru.agregarDetalle('pdecimal')
        listGrammer.insert(0,instru)
        t[0] = numDecimalM(t[2])

def p_valor4(t):
        'valor : identificador'
        instru = grammer.nodoGramatical('VALOR')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = ids(t[1])

def p_valor5(t):
        'valor : cadenacaracter'
        instru = grammer.nodoGramatical('VALOR')
        instru.agregarDetalle('cadenacaracter')
        listGrammer.insert(0,instru)
        t[0] = cadenaCaracter(t[1])

def p_valor6(t):
        'valor : substring par1 valor coma valor coma valor par2'
        instru = grammer.nodoGramatical('VALOR')
        instru.agregarDetalle('substring')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)

        t[0] = ListaSubString(True, t[3], t[5], t[7])

def p_lista_insertar(t):
        'lista_insertar : lista_insertar coma operacion_aritmetica'
        instru = grammer.nodoGramatical('LISTA_INSERTAR')
        instru.agregarDetalle('LISTA_INSERTAR')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)
        vars = [t[1]]
        vars.append(t[3])
        t[0]= vars

def p_lista_insertar2(t):
        'lista_insertar : operacion_aritmetica'
        instru = grammer.nodoGramatical('LISTA_INSERTAR')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)

        t[0]= t[1]
                

#UPDATE
def p_update(t):
        'sentencia_update : update  identificador set identificador igual operacion_aritmetica condicion'
        instru = grammer.nodoGramatical('SENTENCIA_UPDATE')
        instru.agregarDetalle('update')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('set')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('igual')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('condicion')
        listGrammer.insert(0,instru)
        t[0]= Actualizar( t[2], t[4], t[6], t[7])


#DELETE
def p_delete(t):
        'sentencia_delete : delete from delete_cont condicion'
        instru = grammer.nodoGramatical('SENTENCIA_DELETE')
        instru.agregarDetalle('delete')
        instru.agregarDetalle('from')
        instru.agregarDetalle('DELETE_CONT')
        instru.agregarDetalle('condicion')
        listGrammer.insert(0,instru)     
        t[0]= Borrar(t[3] , t[4])   

def p_delete_cont(t):
        'delete_cont : only identificador'
        instru = grammer.nodoGramatical('DELETE_CONT')
        instru.agregarDetalle('only')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = BorrarCont(valido.valido, t[2], valido.invalido)

def p_delete_cont2(t):
        'delete_cont : only identificador por'
        instru = grammer.nodoGramatical('DELETE_CONT')
        instru.agregarDetalle('only')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('por')
        listGrammer.insert(0,instru)
        t[0]= BorrarCont(valido.valido, t[2], valido.valido)


def p_delete_cont3(t):
        'delete_cont : identificador por'
        instru = grammer.nodoGramatical('DELETE_CONT')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('por')
        listGrammer.insert(0,instru)

        t[0] = BorrarCont(valido.invalido, t[1], valido.valido)

def p_delete_cont4(t):
        'delete_cont : identificador'
        instru = grammer.nodoGramatical('DELETE_CONT')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = ids(t[1])

#SELECT
def p_select(t):
        'sentencia_select : select opciones_fecha'
        instru = grammer.nodoGramatical('SENTENCIA_SELECT')
        instru.agregarDetalle('select')
        instru.agregarDetalle('OPCIONES_FECHA')
        listGrammer.insert(0,instru)

        t[0] = seleccionF(t[2])


def p_select3(t):
        'sentencia_select : select select_cont pyc'
        instru = grammer.nodoGramatical('SENTENCIA_SELECT')
        instru.agregarDetalle('select')
        instru.agregarDetalle('SELECT_CONT')
        listGrammer.insert(0,instru)
        t[0] = seleccionCont(t[2])


def p_select2(t):
        'sentencia_select : select select_cont from lista_from condicion_cont'
        instru = grammer.nodoGramatical('SENTENCIA_SELECT')
        instru.agregarDetalle('select')
        instru.agregarDetalle('SELECT_CONT')
        instru.agregarDetalle('from')
        instru.agregarDetalle('LISTA_FROM')
        instru.agregarDetalle('CONDICION_CONT')
        listGrammer.insert(0,instru)
        t[0]= seleccion(t[2], t[4] , t[5])

def p_order(t):
        'order_by : order by identificador opcion_order order_by'
        instru = grammer.nodoGramatical('ORDER_BY')
        instru.agregarDetalle('order')
        instru.agregarDetalle('by')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('OPERACION_ORDER')
        instru.agregarDetalle('ORDER_BY')
        listGrammer.insert(0,instru)

        t[0] = ordenar(t[3] , t[4] , t[5])

def p_order2(t):
        'order_by : condicion_cont'
        instru = grammer.nodoGramatical('ORDER_BY')
        instru.agregarDetalle('CONDICION_CONT')
        listGrammer.insert(0,instru)

        t[0]= t[1]

def p_order3(t):
        'order_by : limit operacion_aritmetica order_by'
        instru = grammer.nodoGramatical('ORDER_BY')
        instru.agregarDetalle('limit')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('ORDER_BY')
        listGrammer.insert(0,instru)

        t[0] = limts(t[2] , t[3])

def p_order4(t):
        '''order_by : offset operacion_aritmetica order_by'''
        instru = grammer.nodoGramatical('ORDER_BY')
        instru.agregarDetalle('offset')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('ORDER_BY')
        listGrammer.insert(0,instru)

        t[0] = offsets(t[2] , t[3])

def p_opcion_order(t):
        '''opcion_order : asc
        			 | desc'''
        instru = grammer.nodoGramatical('OPCION_ORDER')
        instru.agregarDetalle(t[1])
        listGrammer.insert(0,instru)

        t[0] = t[1]

def p_condicion_cont(t):
        '''condicion_cont : where operacion_logica fin_select'''
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_LOGICA')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)
        t[0] = WhereSimple(t[2], t[3])

def p_condicion_cont1(t):
        'condicion_cont : where operacion_relacional fin_select'
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)
        t[0] = WhereSimple(t[2], t[3])

def p_condicion_cont2(t):
        'condicion_cont : where operacion_logica group by identificador fin_select'
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_LOGICA')
        instru.agregarDetalle('group')
        instru.agregarDetalle('by')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)
        t[0] = whereAgrupado(t[1], t[5], t[6])


def p_condicion_cont3(t):
        'condicion_cont : group by lista_id fin_select'
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('group')
        instru.agregarDetalle('by')
        instru.agregarDetalle('LISTA_ID')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)

        t[0] = Groups(t[3] , valido.invalido, t[4])


def p_condicion_cont4(t):
        'condicion_cont : group by lista_id having operacion_logica fin_select'
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('group')
        instru.agregarDetalle('by')
        instru.agregarDetalle('LISTA_ID')
        instru.agregarDetalle('having')
        instru.agregarDetalle('OPERACION_LOGICA')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)
        t[0] = Groups(t[3] , t[5], t[6])

def p_condicion_cont5(t):
        'condicion_cont : where exists par1 sentencia_select par2 fin_select'
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('exists')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('SENTENCIA_SELECT')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)
        t[0] = WheresExist(t[4] , t[6])

def p_condicion_cont6(t):
        'condicion_cont : where operacion_aritmetica in par1 sentencia_select par2 fin_select'
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('in')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('SENTENCIA_SELECT')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)
        t[0] = wheres(t[2], True, t[6],t[8])

def p_condicion_cont7(t):
        'condicion_cont : where operacion_aritmetica not in par1 sentencia_select par2 fin_select'
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('not')
        instru.agregarDetalle('in')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('SENTENCIA_SELECT')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)
        t[0] = wheres(t[2], False, t[6],t[8])


def p_condicion_cont8(t):
        'condicion_cont : fin_select'
        instru = grammer.nodoGramatical('CONDICION_CONT')
        instru.agregarDetalle('FIN_SELECT')
        listGrammer.insert(0,instru)
        t[0] =t[1]


def p_fin_select(t):
        'fin_select : order_by '
        instru = grammer.nodoGramatical('FIN_SELECT')
        instru.agregarDetalle('ORDER_BY')
        listGrammer.insert(0,instru)
        t[0] = t[1]

def p_fin_select2(t):
        'fin_select : pyc'
        instru = grammer.nodoGramatical('FIN_SELECT')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        #crear metodos final
        t[0]= Empty(t[1])

def p_fin_select3(t):
        'fin_select : union sentencia_select'
        instru = grammer.nodoGramatical('FIN_SELECT')
        instru.agregarDetalle('union')
        instru.agregarDetalle('SENTENCIA_SELECT')
        listGrammer.insert(0,instru)
        t[0] = uniones(t[2])

def p_fin_select4(t):
        'fin_select : intersect sentencia_select'
        instru = grammer.nodoGramatical('FIN_SELECT')
        instru.agregarDetalle('intersect')
        instru.agregarDetalle('SENTENCIA_SELECT')
        listGrammer.insert(0,instru)
        t[0]= interseccion(t[2])

def p_fin_select5(t):
        'fin_select : except sentencia_select'
        instru = grammer.nodoGramatical('FIN_SELECT')
        instru.agregarDetalle('except')
        instru.agregarDetalle('SENTENCIA_SELECT')
        listGrammer.insert(0,instru)

        t[0] = excepto(t[2])

def p_lista_from(t):
        'lista_from : lista_from coma identificador as identificador'
        instru = grammer.nodoGramatical('LISTA_FROM')
        instru.agregarDetalle('LISTA_FROM')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('as')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)

        vars = [t[1]]
        vars.append(como(t[3] , t[5]))
        t[0] = vars

def p_lista_from2(t):
        'lista_from : lista_from coma identificador'
        instru = grammer.nodoGramatical('LISTA_FROM')
        instru.agregarDetalle('LISTA_FROM')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        var2 = [t[1]]
        var2 .append(t[3])
        t[0] = var2

def p_lista_from3(t):
        'lista_from : identificador as identificador'
        instru = grammer.nodoGramatical('LISTA_FROM')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('as')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0]= como(t[1] , t[2])

def p_lista_from4(t):
        'lista_from : identificador'
        instru = grammer.nodoGramatical('LISTA_FROM')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = ids(t[1])

def p_lista_from5(t):
        'lista_from : hacer_join'
        instru = grammer.nodoGramatical('LISTA_FROM')
        instru.agregarDetalle('HACER_JOIN')
        listGrammer.insert(0,instru)

        t[0] = [t[1]]

def p_lista_from6(t):
        'lista_from : par1 sentencia_select par2 as identificador'
        instru = grammer.nodoGramatical('LISTA_FROM')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('SENTENCIA_SELECT')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)

        t[0] = como(t[2], t[5])


def p_lista_from7(t):
        'lista_from : par1 sentencia_select par2'
        instru = grammer.nodoGramatical('LISTA_FROM')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('SENTENCIA_SELECT')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)

        t[0] = t[2]

def p_tipo_join(t):
        '''tipo_join : inner join
        			 | left join
        			 | right join
        			 | full join
        			 | outer join'''
        instru = grammer.nodoGramatical('TIPO_JOIN')
        instru.agregarDetalle(t[1])
        instru.agregarDetalle(t[2])
        listGrammer.insert(0,instru) 

        t[0] = TipoJoin(t[1])        

def p_tipo_join2(t):
        'tipo_join : join'
        instru = grammer.nodoGramatical('HACER_JOIN')
        instru.agregarDetalle('join')
        listGrammer.insert(0,instru)
        t[0] = TipoJoin(True)


def p_hacer_join(t):
        'hacer_join : identificador tipo_join identificador on operacion_logica'
        instru = grammer.nodoGramatical('HACER_JOIN')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('TIPO_JOIN')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('on')
        instru.agregarDetalle('OPERACION_LOGICA')
        listGrammer.insert(0,instru)
        t[0] = HacerJoinOn(t[1] , t[2], t[3] ,t[5])

def p_hacer_join2(t):
        'hacer_join : identificador tipo_join  identificador'
        instru = grammer.nodoGramatical('HACER_JOIN')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('TIPO_JOIN')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)

        t[0] = HacerJoin(t[1] , t[2] ,t[3])


def p_select_cont(t):
        'select_cont : por'
        instru = grammer.nodoGramatical('SELECT_CONT')
        instru.agregarDetalle('por')
        listGrammer.insert(0,instru)
        t[0] = ast(t[1])


def p_select_cont2(t):
        'select_cont : distinct lista_id'
        instru = grammer.nodoGramatical('SELECT_CONT')
        instru.agregarDetalle('distinct')
        instru.agregarDetalle('LISTA_ID')
        listGrammer.insert(0,instru)
        t[0] = Distinct(t[2])


def p_select_cont3(t):
        'select_cont : lista_id'
        instru = grammer.nodoGramatical('SELECT_CONT')
        instru.agregarDetalle('LISTA_ID')
        listGrammer.insert(0,instru)

        t[0]= t[1]

def p_select_cont4(t):
        'select_cont : sen_case'
        instru = grammer.nodoGramatical('SELECT_CONTE')
        instru.agregarDetalle('SEN_CASE')
        listGrammer.insert(0,instru)

        t[0] = t[1]

def p_sen_case(t):
        'sen_case : case case_when'
        instru = grammer.nodoGramatical('SEN_CASE')
        instru.agregarDetalle('case')
        instru.agregarDetalle('CASE_WHEN')
        listGrammer.insert(0,instru)
        t[0] = t[2]

def p_case_when(t):
        'case_when : when operacion_logica then operacion_aritmetica case_when'
        instru = grammer.nodoGramatical('CASE_WHEN')
        instru.agregarDetalle('when ')
        instru.agregarDetalle('OPERACION_LOGICA')
        instru.agregarDetalle('then')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('CASE_WHEN')
        listGrammer.insert(0,instru)	
        t[0] = CaseWhen(t[2] , t[4] , t[5])	

def p_case_when2(t):
        'case_when : end valor'
        instru = grammer.nodoGramatical('CASE_WHEN')
        instru.agregarDetalle('end')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)
        t[0] = endWhen(t[2])
def p_lista_id(t):
        'lista_id : lista_id coma operacion_aritmetica'
        instru = grammer.nodoGramatical('LISTA_ID')
        instru.agregarDetalle('LISTA_ID')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)
        varss= [t[1]]
        varss.append(t[3])
        t[0]=varss

def p_lista_id2(t):
        'lista_id : lista_id coma identificador punto identificador'
        instru = grammer.nodoGramatical('LISTA_ID')
        instru.agregarDetalle('LISTA_ID')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('punto')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = [ListaId2(t[1] , t[3] ,t[5])]

def p_lista_id3(t):
        'lista_id : operacion_aritmetica'
        instru = grammer.nodoGramatical('LISTA_ID')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)
        t[0] = t[1]

def p_lista_id4(t):
        'lista_id : identificador punto identificador'
        instru = grammer.nodoGramatical('LISTA_ID')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('punto')
        instru.agregarDetalle('identificador')
        listGrammer.insert(0,instru)
        t[0] = [ListaSubString(False,t[1] , t[2] , valido.invalido)]

def p_lista_id5(t):
        'lista_id : substring par1 valor coma valor coma valor par2'
        instru = grammer.nodoGramatical('LISTA_ID')
        instru.agregarDetalle('substring')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)

        t[0]= [ListaSubString( False ,t[3], t[5] ,t[7])]

def p_opciones_fecha(t):
        'opciones_fecha : extract par1 tipo_date from timestamp valor par2 pyc'
        instru = grammer.nodoGramatical('OPCION_FECHA')
        instru.agregarDetalle('extract')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('TIPO_DATE')
        instru.agregarDetalle('from')
        instru.agregarDetalle('timestamp')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)

        t[0] = OpcionesFecha3(t[1], t[3], t[5], t[6])

def p_opciones_fecha2(t):
        'opciones_fecha : now par1 par2 pyc'
        instru = grammer.nodoGramatical('OPCION_FECHA')
        instru.agregarDetalle('now')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0]= OpcionesFecha2(True)

def p_opciones_fecha3(t):
        'opciones_fecha : date_part par1 valor coma interval valor par2 pyc'
        instru = grammer.nodoGramatical('OPCION_FECHA')
        instru.agregarDetalle('DATE_PART')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('intervalo')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = OpcionesFecha3(t[1], t[3], t[5], t[6])

def p_opciones_fecha4(t):
        'opciones_fecha : current_date pyc'
        instru = grammer.nodoGramatical('OPCION_FECHA')
        instru.agregarDetalle('CURRENT_DATE')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Opcionesfecha4(t[1] , valido.invalido)

def p_opciones_fecha5(t):
        'opciones_fecha : current_time pyc'
        instru = grammer.nodoGramatical('OPCION_FECHA')
        instru.agregarDetalle('CURRENT_TIME')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Opcionesfecha4(t[1] , valido.invalido)

def p_opciones_fecha6(t):
        'opciones_fecha : timestamp valor pyc'
        instru = grammer.nodoGramatical('OPCION_FECHA')
        instru.agregarDetalle('timestamp')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Opcionesfecha4(t[1] , t[2])

def p_tipo_date(t):
        '''tipo_date : year
        			  | month
        			  | day
        			  | hour
        			  | minute
        			  | second'''
        instru = grammer.nodoGramatical('TIPO_DATE')
        instru.agregarDetalle(t[1])
        listGrammer.insert(0,instru)

        t[0]= tipo(t[1])

def p_condicion(t):
        'condicion : pyc'
        instru = grammer.nodoGramatical('CONDICION')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Condicion(valido.invalido, valido.invalido , valido.invalido, valido.invalido, valido.invalido)

def p_condicion2(t):
        'condicion : where operacion_logica pyc'
        instru = grammer.nodoGramatical('CONDICION')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_LOGICA')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Condicion(valido.invalido, t[2] , valido.invalido, valido.invalido, valido.invalido)

def p_condicion3(t):
        'condicion : where identificador igual operacion_aritmetica pyc'
        instru = grammer.nodoGramatical('CONDICION')
        instru.agregarDetalle('where')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('igual')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Condicion(valido.invalido, t[4] , valido.invalido, valido.invalido, t[2])

def p_condicion4(t):
        'condicion : where exists par1 sentencia_select par2 pyc'
        instru = grammer.nodoGramatical('CONDICION')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('exists')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('SENTENCIA_SELECT')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Condicion(valido.invalido, t[4] , valido.invalido, valido.valido, valido.invalido)

def p_condicion5(t):
        'condicion : where operacion_aritmetica in par1 sentencia_select par2 pyc'
        instru = grammer.nodoGramatical('CONDICION')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('in')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('SENTENCIA_SELECT')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)
        t[0] = Condicion(True, t[2] , t[5], valido.invalido, valido.invalido)


def p_condicion6(t):
        'condicion : where operacion_aritmetica not in par1 sentencia_select par2 pyc'
        instru = grammer.nodoGramatical('CONDICION')
        instru.agregarDetalle('where')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('not')
        instru.agregarDetalle('in')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('SENTENCIA_SELECT')
        instru.agregarDetalle('par2')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)

        t[0] = Condicion(False, t[2] , t[6], valido.invalido, valido.invalido)

def p_op_aritmetica(t):
        'operacion_aritmetica : operacion_aritmetica mas operacion_aritmetica'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('mas')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)
        t[0] = aritmetica(t[1], t[3], arit.MAS)

def p_op_aritmetica2(t):
        'operacion_aritmetica : operacion_aritmetica menos operacion_aritmetica'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('menos')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)
        t[0] = aritmetica(t[1], t[3], arit.RES)

def p_op_aritmetica3(t):
        'operacion_aritmetica : operacion_aritmetica por operacion_aritmetica'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('por')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)
        t[0] = aritmetica(t[1], t[3], arit.POR)


def p_op_aritmetica4(t):
        'operacion_aritmetica : operacion_aritmetica division operacion_aritmetica'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('division')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)
        t[0] = aritmetica(t[1], t[3], arit.DIV)


def p_op_aritmetica5(t):
        'operacion_aritmetica : par1 operacion_aritmetica par2'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = t[2]


def p_op_aritmetica6(t):
        'operacion_aritmetica : valor'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)  
        t[0] = t[1]

def p_op_aritmetica7(t):
        'operacion_aritmetica : sum par1 operacion_aritmetica par2'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('sum')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = SUM(t[3])

def p_op_aritmetica8(t):
        'operacion_aritmetica : avg par1 operacion_aritmetica par2'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('avg')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = avg(t[3])

def p_op_aritmetica9(t):
        'operacion_aritmetica : max par1 operacion_aritmetica par2'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('max')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = MAX(t[3])

def p_op_aritmetica10(t):
        'operacion_aritmetica :  pi'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('pi')
        listGrammer.insert(0,instru)
        t[0] = pi(True)

def p_op_aritmetica11(t):
        'operacion_aritmetica : power par1 operacion_aritmetica coma operacion_aritmetica par2'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('power')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle(',')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= potencia(t[3],t[5])

def p_op_aritmetica12(t):
        'operacion_aritmetica : sqrt par1 operacion_aritmetica par2'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('sqrt')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0] = raiz(t[3])

def p_op_aritmetica13(t):
        'operacion_aritmetica : valor between valor'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('between')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)
        t[0] = aritmetica(t[0], t[3], arit.BETWEENS)

def p_op_aritmetica14(t):
        'operacion_aritmetica : valor is distinct from valor'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('is')
        instru.agregarDetalle('distinct')
        instru.agregarDetalle('from')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)
        t[0] = distinct(t[1] , t[5] , DIST.isDistinct)

def p_op_aritmetica15(t):
        'operacion_aritmetica : valor is not distinct from valor'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('is')
        instru.agregarDetalle('not')
        instru.agregarDetalle('distinct')
        instru.agregarDetalle('from')
        instru.agregarDetalle('VALOR')
        listGrammer.insert(0,instru)
        t[0] = distinct(t[1] , t[6] , DIST.isNotDistinct)


def p_op_aritmetica16(t):
        'operacion_aritmetica : valor is null'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('is')
        instru.agregarDetalle('null')
        listGrammer.insert(0,instru)
        t[0]= aritmeticaESP(t[1], ESP.isNull)

def p_op_aritmetica17(t):
        'operacion_aritmetica : valor is not null'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('is')
        instru.agregarDetalle('not')
        instru.agregarDetalle('null')
        listGrammer.insert(0,instru)
        t[0]= aritmeticaESP(t[1], ESP.isNotNull)

def p_op_aritmetica18(t):
        'operacion_aritmetica : valor is true'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('is')
        instru.agregarDetalle('true')
        listGrammer.insert(0,instru)
        t[0]= aritmeticaESP(t[1], ESP.isTrue)

def p_op_aritmetica19(t):
        'operacion_aritmetica : valor is not true'
        instru = grammer.nodoGramatical('OPERACION_RELACIONAL')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('is')
        instru.agregarDetalle('not')
        instru.agregarDetalle('true')
        listGrammer.insert(0,instru)
        t[0]= aritmeticaESP(t[1], ESP.isNotTrue)
        

def p_op_aritmetica20(t):
        'operacion_aritmetica : valor is false'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('is')
        instru.agregarDetalle('false')
        listGrammer.insert(0,instru)
        t[0]= aritmeticaESP(t[1], ESP.isFalse)

def p_op_aritmetica21(t):
        'operacion_aritmetica : valor is not false'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('VALOR')
        instru.agregarDetalle('is')
        instru.agregarDetalle('not')
        instru.agregarDetalle('false')
        listGrammer.insert(0,instru)
        t[0] = aritmeticaESP(t[1], ESP.isNotFalse)

def p_op_relacional(t):
        'operacion_relacional : operacion_relacional mayor operacion_relacional'
        instru = grammer.nodoGramatical('OPERACION_RELACIONAL')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        instru.agregarDetalle('mayor')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        listGrammer.insert(0,instru)
        t[0] = relacional(t[1] , relac.MAYOR , t[3])  

def p_op_relacional2(t):
        'operacion_relacional : operacion_relacional menor operacion_relacional'
        instru = grammer.nodoGramatical('OPERACION_RELACIONAL')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        instru.agregarDetalle('menor')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        listGrammer.insert(0,instru)
        t[0] = relacional(t[1]  , t[3], relac.MENOR)  

def p_op_relacional3(t):
        'operacion_relacional : operacion_relacional mayorigual operacion_relacional'
        instru = grammer.nodoGramatical('OPERACION_RELACIONAL')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        instru.agregarDetalle('mayoRigual')
        instru.agregarDetalle('OPEACION_RELACIONAL')
        listGrammer.insert(0,instru)   

        t[0] = relacional(t[1]  , t[3], relac.MAYI)  

def p_op_relacional4(t):
        'operacion_relacional : operacion_relacional menorigual operacion_relacional'
        instru = grammer.nodoGramatical('OPERACION_RELACIONAL')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        instru.agregarDetalle('menorigual')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        listGrammer.insert(0,instru)
        t[0] = relacional(t[1]  , t[3], relac.II)
        

def p_op_relacional5(t):
        'operacion_relacional : operacion_relacional diferente operacion_relacional'
        instru = grammer.nodoGramatical('OPERACION_RELACIONAL')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        instru.agregarDetalle('diferente')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        listGrammer.insert(0,instru)
        t[0] = relacional(t[1]  , t[3], relac.NI)

def p_op_relacional6(t):
        'operacion_relacional : operacion_relacional igual operacion_relacional'
        instru = grammer.nodoGramatical('OPERACION_RELACIONAL')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        instru.agregarDetalle('igual')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        listGrammer.insert(0,instru)
        t[0] = relacional(t[1]  , t[3], relac.II)

def p_op_relacional7(t):
        'operacion_relacional : operacion_aritmetica'
        instru = grammer.nodoGramatical('OPERACION_RELACIONAL')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        listGrammer.insert(0,instru)
        t[0] = t[1]

def p_op_logica(t):
        'operacion_logica : operacion_logica and operacion_logica'
        instru = grammer.nodoGramatical('OPERACION_LOGICA')
        instru.agregarDetalle('OPERACION_LOGICA')
        instru.agregarDetalle('and')
        instru.agregarDetalle('OPERACION_LOGICA')
        listGrammer.insert(0,instru)
        t[0] = logica(t[1] , t[3], logic.AND )

def p_op_logica2(t):
        'operacion_logica : operacion_logica or operacion_logica'
        instru = grammer.nodoGramatical('OPERACION_LOGICA')
        instru.agregarDetalle('OPERACION_LOGICA')
        instru.agregarDetalle('or')
        instru.agregarDetalle('OPERACION_LOGICA')
        listGrammer.insert(0,instru)

        t[0] = logica(t[1]  , t[3], logic.OR)

def p_op_logica3(t):
        'operacion_logica :  not operacion_logica'
        instru = grammer.nodoGramatical('OPERACION_LOGICA')
        instru.agregarDetalle('OPERACION_LOGICA')
        instru.agregarDetalle('not')
        instru.agregarDetalle('OPERACION_LOGICA')
        listGrammer.insert(0,instru)

        t[0] = logica(t[1]  ,valido.invalido, logic.NOT)

def p_op_logica4(t):
        'operacion_logica : operacion_relacional'
        instru = grammer.nodoGramatical('OPERACION_LOGICA')
        instru.agregarDetalle('OPERACION_RELACIONAL')
        listGrammer.insert(0,instru)
        t[0]=t[1]

def p_show(t):
        'sentencia_show : show databases show_cont'
        instru = grammer.nodoGramatical('SENTENCIA_SHOW')
        instru.agregarDetalle('show')
        instru.agregarDetalle('databases')
        instru.agregarDetalle('SHOW_CONT')
        listGrammer.insert(0,instru)

        t[0] = SentenciaShow(t[3])


def p_show_cont(t):
        'show_cont : pyc'
        instru = grammer.nodoGramatical('SHOW_CONT')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)

        t[0] = Empty(True)	

def p_show_cont2(t):
        'show_cont : ins_like pyc'
        instru = grammer.nodoGramatical('SHOW_CONT')
        instru.agregarDetalle('INS_LIKE')
        instru.agregarDetalle('pyc')
        listGrammer.insert(0,instru)

        t[0] = t[1]

def p_ins_like(t):
        'ins_like : like porcentaje identificador porcentaje'
        instru = grammer.nodoGramatical('INS_LIKE')
        instru.agregarDetalle('like')
        instru.agregarDetalle('porcentaje')
        instru.agregarDetalle('identificador')
        instru.agregarDetalle('porcentaje')
        listGrammer.insert(0,instru)
		#CODE

        t[0] = InsLike(t[3])

def p_empty(t):
     'empty :'
     pass
#Operaciones EXTRAS

def p_op_aritmetica22(t):
        'operacion_aritmetica : funciones_extras'
        instru = grammer.nodoGramatical('OPERACION_ARITMETICA')
        instru.agregarDetalle('FUNCIONES_EXTRAS')
        listGrammer.insert(0,instru)
        t[0]= aritmetica2(t[1])

def p_funciones_extras(t):
        'funciones_extras : math_functions'
        instru = grammer.nodoGramatical('FUNCIONES_EXTRAS')
        instru.agregarDetalle('MATH_FUNCTIONS')
        listGrammer.insert(0,instru)
        t[0]= funcionextra(t[1])

def p_funciones_extras2(t):       
        'funciones_extras : f_trigonometricas'
        instru = grammer.nodoGramatical('FUNCIONES_EXTRAS')
        instru.agregarDetalle('TRIGONOMETRICAS')
        listGrammer.insert(0,instru)
        t[0]= funcionextra2(t[1])

def p_funciones_extras3(t):
        'funciones_extras : binary_string'
        instru = grammer.nodoGramatical('FUNCIONES_EXTRAS')
        instru.agregarDetalle('BINARY_STRING')
        listGrammer.insert(0,instru)
        t[0]= funcionextra3(t[1])


def p_math_funciones(t):
        'math_functions : funciones_math1 par1 operacion_aritmetica par2'
        instru = grammer.nodoGramatical('MATH_FUNCTIONS')
        instru.agregarDetalle('FUNCIONES_MATH1')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= mathfunctions(t[1],t[3])

def p_math_funciones2(t):
        'math_functions :  funciones_math2 par1 operacion_aritmetica coma operacion_aritmetica par2'
        instru = grammer.nodoGramatical('MATH_FUNCTIONS')
        instru.agregarDetalle('FUNCIONES_MATH2')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= mathfunctions2(t[1],t[3],t[5])

def p_math_funciones3(t):
        'math_functions : width_bucket par1 operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica par2'
        instru = grammer.nodoGramatical('MATH_FUNCTIONS')
        instru.agregarDetalle('width_bucket')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= mathfunctions3(t[3], t[5], t[7], t[9])

def p_math_funciones4(t):
        'math_functions : random par1 par2'
        instru = grammer.nodoGramatical('MATH_FUNCTIONS')
        instru.agregarDetalle('random')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= randomclass()

def p_funciones_math1(t):
        '''funciones_math1 : abs
        | cbrt
        | ceil
        | celing
        | degrees
        | exp
        | factorial
        | floor
        | ln
        | log
        | radians
        | sign'''
        instru = grammer.nodoGramatical('FUNCIONES_MATH1')
        instru.agregarDetalle(t[1])
        listGrammer.insert(0,instru)
        t[0]= t[1]

def p_funciones_math2(t):
        '''funciones_math2 : div
        | gcd
        | mod
        | round'''
        instru = grammer.nodoGramatical('FUNCIONES_MATH2')
        instru.agregarDetalle(t[1])
        listGrammer.insert(0,instru)
        t[0]= t[1]


def p_trigonometricas(t):
        'f_trigonometricas : funciones_tri par1 operacion_aritmetica par2'
        instru = grammer.nodoGramatical('TRIGONOMETRICAS')
        instru.agregarDetalle('FUNCIONES_TRI')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= trigonometricas(t[1], t[3])

def p_funciones_tri(t):
        '''funciones_tri : acos
        | acosd
        | asin
        | asind
        | atan
        | atand
        | atan2
        | cos
        | cosd
        | cot
        | cotd
        | sin
        | sind
        | tan
        | tand
        | sinh
        | cosh
        | tanh
        | asinh
        | acosh
        | atanh'''
        instru = grammer.nodoGramatical('FUNCIONES_TRI')
        instru.agregarDetalle(t[1])
        listGrammer.insert(0,instru)
        t[0]= t[1]





def p_binary_string2(t):
        'binary_string : funciones_string2 par1 operacion_aritmetica par2'
        instru = grammer.nodoGramatical('BINARY_STRING')
        instru.agregarDetalle('FUNCIONES_STRING1')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= binarystring2(t[1],t[3])

def p_binary_string3(t):
        'binary_string : substr par1 operacion_aritmetica coma operacion_aritmetica coma operacion_aritmetica par2'
        instru = grammer.nodoGramatical('BINARY_STRING')
        instru.agregarDetalle('substr')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= binarystring3(t[3],t[5],t[7])

def p_binary_string4(t):
        'binary_string : funciones_string3 par1 operacion_aritmetica dosp dosp bytea coma operacion_aritmetica par2'
        instru = grammer.nodoGramatical('BINARY_STRING')
        instru.agregarDetalle('FUNCIONES_STRING3')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('dosp')
        instru.agregarDetalle('dosp')
        instru.agregarDetalle('bytea')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= binarystring4(t[1],t[3],t[8])

def p_binary_string5(t):
        'binary_string : set_byte par1 operacion_aritmetica dosp dosp bytea coma operacion_aritmetica coma operacion_aritmetica par2'
        instru = grammer.nodoGramatical('BINARY_STRING')
        instru.agregarDetalle('set_byte')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('dosp')
        instru.agregarDetalle('dosp')
        instru.agregarDetalle('bytea')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= binarystring5(t[3],t[3],t[10])


def p_binary_string6(t):
        'binary_string : convert par1 operacion_aritmetica as operacion_aritmetica par2'
        instru = grammer.nodoGramatical('BINARY_STRING')
        instru.agregarDetalle('convert')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('as')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= binarystring6(t[3],t[5])

def p_binary_string7(t):
        'binary_string : decode par1 operacion_aritmetica coma operacion_aritmetica par2'
        instru = grammer.nodoGramatical('BINARY_STRING')
        instru.agregarDetalle('decode')
        instru.agregarDetalle('par1')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('coma')
        instru.agregarDetalle('OPERACION_ARITMETICA')
        instru.agregarDetalle('par2')
        listGrammer.insert(0,instru)
        t[0]= binarystring7(t[3],t[5])



def p_funciones_string2(t):
        '''funciones_string2 : length
        | sha256
        | trim
        | md5'''
        t[0]= t[1]

def p_funciones_string3(t):
        '''funciones_string3 : get_byte
        | encode'''
        t[0]= t[1]



def p_error(t):
        print("Entrando a error ****************************")
        if t:
                ReporteErrores.esin.append("Syntax error. Msg 42601, line: " + str(t.lexer.lineno) + ", col: " + str(
                t.lexer.lexpos) + ", keyword: " + str(t.value))
                print("Syntax error. Msg 42601, line: " + str(t.lexer.lineno) + ", col: " + str(
                t.lexer.lexpos) + ", keyword: " + str(t.value))
                parser.errok()


parser = yacc.yacc()


#generar.graficaArbol(arbol)
#borrar lo que esta dentro de los parentesis y colocar parser
def parse(input):
    parsear =parser.parse(input)
    gramati= generar.graficaGramatical(listGrammer)
    print('antes de ejecutar grafica')
    gramati.ejecutarGrafica()
    print('ejecutada grafica')
    return parsear

def ejecturar():
        f = open("D:/CURSOS 2DO SEMESTRE 2020/VACACIONES/COMPILADORES/DESARROLLO/COMPI2_DIC2020/Gramaticas/prueba.txt", "r")
        input = f.read()
        print(input)
        resultado = parser.parse(input)
        gramati= generar.graficaGramatical(listGrammer)
        gramati.ejecutarGrafica()

#resultado = parser.parse(input)
#arbolimas = generar.graficaArbol(resultado)
#arbolimas.ejecutarGrafica() 