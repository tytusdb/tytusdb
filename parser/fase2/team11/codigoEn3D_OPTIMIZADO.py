from goto import with_goto
import gramatica_asc as g
from Ast import *

ast = AST()
raiz = Nodo('INSTRUCCIONES','', [])
pila = [] 

################################ FUNCION INTERMEDIA ############################### 

def funcionIntermedia(): 
	global pila
	insts = pila.pop()
	nodo = g.parse(insts)
	raiz.hijos.append(nodo)
	ast.executeAST(nodo)
	ast.printOutputs()
	ast.printErrors()
	ast.generateTSReport()
	ast.erroresHTML()

############################# CODIGO EN 3DIRECCIONES ############################## 

def main(): 
	global pila 
	t0 = "CREATE DATABASE DBFase2;"
	pila = [t0]
	funcionIntermedia()
	t1 = "USE DBFase2;"
	pila = [t1]
	funcionIntermedia()
	print(myFuncion('INICIO CALIFICACION FASE 2'))
	t2 = "CREATE TABLE tbProducto (idproducto integer not null primary key,          producto varchar(150) not null,          fechacreacion date not null,        estado integer);"
	pila = [t2]
	funcionIntermedia()
	t3 = "CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);"
	pila = [t3]
	funcionIntermedia()
	t4 = "CREATE TABLE tbCalificacion (idcalifica integer not null primary key,         item varchar(100) not null,         punteo integer not null);"
	pila = [t4]
	funcionIntermedia()
	t5 = "CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);"
	pila = [t5]
	funcionIntermedia()
	t6 = "INSERT INTO tbProducto values(1,'Laptop Lenovo',now(),1);"
	pila = [t6]
	funcionIntermedia()
	t7 = "INSERT INTO tbProducto values(2,'Bateria para Laptop Lenovo T420',now(),1);"
	pila = [t7]
	funcionIntermedia()
	t8 = "INSERT INTO tbProducto values(3,'Teclado Inalambrico',now(),1);"
	pila = [t8]
	funcionIntermedia()
	t9 = "INSERT INTO tbProducto values(4,'Mouse Inalambrico',now(),1);"
	pila = [t9]
	funcionIntermedia()
	t10 = "INSERT INTO tbProducto values(5,'WIFI USB',now(),1);"
	pila = [t10]
	funcionIntermedia()
	t11 = "INSERT INTO tbProducto values(6,'Laptop HP',now(),1);"
	pila = [t11]
	funcionIntermedia()
	t12 = "INSERT INTO tbProducto values(7,'Teclado Flexible USB',now(),1);"
	pila = [t12]
	funcionIntermedia()
	t13 = "INSERT INTO tbProducto values(8,'Laptop Samsung','2021-01-02',1);"
	pila = [t13]
	funcionIntermedia()
	print(myFuncion('Crea Funcion'))
	t14 = "insert into tbCalificacion values(1,'Create Table and Insert',"+str(ValidaRegistros('tbProducto',8))+");"
	pila = [t14]
	funcionIntermedia()
	t15 = "update tbProducto set estado = 2 where estado = 1;"
	pila = [t15]
	funcionIntermedia()
	t16 = "insert into tbCalificacion values(2,'Update',"+str(ValidaRegistros('tbProductoUp',8))+");"
	pila = [t16]
	funcionIntermedia()
	t17 = "insert into tbCalificacion values(3,' Valida Funciones',"+str(CALCULOS())+");"
	pila = [t17]
	funcionIntermedia()
	t18 = "create table tbbodega (idbodega integer not null primary key,         bodega varchar(100) not null,         estado integer);"
	pila = [t18]
	funcionIntermedia()
	t19 = "CREATE INDEX ON tbbodega ((lower(bodega)));"
	pila = [t19]
	funcionIntermedia()
	sp_validainsert()
	t20 = "insert into tbCalificacion values(4,'Valida Store Procedure',"+str(ValidaRegistros('tbbodega',5))+");"
	pila = [t20]
	funcionIntermedia()
	t21 = "CREATE INDEX idx_bodega ON tbbodega (lower(bodega),estado);"
	pila = [t21]
	funcionIntermedia()
	t22 = "DROP INDEX idx_bodega  CREATE INDEX idx_bodega ON tbbodega (lower(bodega),estado);"
	pila = [t22]
	funcionIntermedia()
	sp_validaupdte()
	t23 = "delete from tbbodega where idbodega = 4;"
	pila = [t23]
	funcionIntermedia()
	t24 = "insert into tbCalificacion values(5,'Valida Delete',"+str(ValidaRegistros('tbbodega',4))+");"
	pila = [t24]
	funcionIntermedia()
	t25 = "select * from tbbodega;"
	pila = [t25]
	funcionIntermedia()
	t26 = "CREATE INDEX idx_bodega ON tbbodega (estado);"
	pila = [t26]
	funcionIntermedia()
	sp_insertaproducto(9,'Bocina Inalambrica','2021-01-06')
	sp_insertaproducto(10,'Audifonos con Microfono USB','2021-01-06')
	sp_insertaproducto(11,'Bocina Inalambrica','2021-01-06')
	sp_insertaproducto(12,'Monitor de 17','2021-01-06')
	globals()['myFuncion'] = 0
	print(myFuncion('Valida drop myFunction'))
	print(myFuncion('Crea funcion Nueva de Mensaje'))
	sp_insertaproducto(13,'Bocina Inalambrica Sony','2021-01-06')
	sp_insertaproducto(14,'Audifonos con Microfono USB Lenovo','2021-01-06')
	sp_insertaproducto(15,'Monitor de 21','2021-01-06')
	sp_insertaproducto(16,'Monitor de 17 Lenovo','2021-01-06')
	t27 = "create table tbinventario (   idinventario integer not null primary key,   idproducto   integer not null,   idbodega     integer not null,   cantidad     integer not null,   fechacarga   date   not null,   descripcion  text );"
	pila = [t27]
	funcionIntermedia()
	print(sp_insertainventario (1,'Laptop Lenovo','BODEGA CENTRAL',200,'Laptop Lenovo T420 i7 8GB'))
	print(sp_insertainventario (2,'Teclado Inalambrico','BODEGA CENTRAL',100,'Teclado Inalambrico Lenovo'))
	print(sp_insertainventario (3,'Mouse Inalambrico','BODEGA ZONA 12',50,''))
	print(sp_insertainventario (4,'Laptop HP','bodega zona 9',20,'Laptop HP i5 4GB RAM'))


@with_goto
def myFuncion( texto):
	global pila
	t28 = texto
	return t28


@with_goto
def ValidaRegistros( tabla, cantidad):
	global pila
	resultado = 0
	retorna = 0
	if tabla=='tbProducto': goto .L0
	goto .L1
	label .L0
	t29 = True
	goto .L2
	label .L1
	t29 = False
	label .L2
	if t29 == True: goto .L3
	goto .L4
	label .L3
	t30 = 'select  COUNT(*) FROM tbProducto;'
	pila = [t30]
	funcionIntermedia()
	t31 = pila[0]
	resultado = t31
	if cantidad==resultado: goto .L5
	goto .L6
	label .L5
	t32 = True
	goto .L7
	label .L6
	t32 = False
	label .L7
	if t32 == True: goto .L8
	goto .L9
	label .L8
	retorna = 1
	goto .L10
	label .L9
	retorna = 0
	label .L10
	label .L4
	if tabla=='tbProductoUp': goto .L11
	goto .L12
	label .L11
	t33 = True
	goto .L13
	label .L12
	t33 = False
	label .L13
	if t33 == True: goto .L14
	goto .L15
	label .L14
	t34 = 'select  COUNT(*) FROM tbProducto where estado = 2;'
	pila = [t34]
	funcionIntermedia()
	t35 = pila[0]
	resultado = t35
	if cantidad==resultado: goto .L16
	goto .L17
	label .L16
	t36 = True
	goto .L18
	label .L17
	t36 = False
	label .L18
	if t36 == True: goto .L19
	goto .L20
	label .L19
	retorna = 1
	goto .L21
	label .L20
	retorna = 0
	label .L21
	label .L15
	if tabla=='tbbodega': goto .L22
	goto .L23
	label .L22
	t37 = True
	goto .L24
	label .L23
	t37 = False
	label .L24
	if t37 == True: goto .L25
	goto .L26
	label .L25
	t38 = 'select  COUNT(*) FROM tbbodega;'
	pila = [t38]
	funcionIntermedia()
	t39 = pila[0]
	resultado = t39
	if cantidad==resultado: goto .L27
	goto .L28
	label .L27
	t40 = True
	goto .L29
	label .L28
	t40 = False
	label .L29
	if t40 == True: goto .L30
	goto .L31
	label .L30
	retorna = 1
	goto .L32
	label .L31
	retorna = 0
	label .L32
	label .L26
	t41 = retorna
	return t41


@with_goto
def CALCULOS():
	global pila
	hora = 0
	SENO = 0
	VALOR = 0
	ABSOLUTO = 0
	t42 = 'select  EXTRACT(HOUR FROM TIMESTAMP \'2001-02-16 20:38:40\');'
	pila = [t42]
	funcionIntermedia()
	t43 = pila[0]
	hora = t43
	t44 = 'select  SIN(1);'
	pila = [t44]
	funcionIntermedia()
	t45 = pila[0]
	SENO = t45
	t46 = SENO*hora
	t47 = math.trunc(t46)
	VALOR = t47
	t48 = 'FASE2'[1:4]
	t49 = len(t48)
	t50 = VALOR+t49
	VALOR = t50
	t51 = -1
	t52 = math.sinh(t51)
	t53 = math.fabs(t52)
	ABSOLUTO = t53
	t54 = math.sqrt(225)
	t55 = ABSOLUTO*t54
	ABSOLUTO = t55
	t56 = VALOR+ABSOLUTO
	t57 = math.acos(0.5)
	t58 = t56/t57
	VALOR = t58
	if VALOR>1: goto .L33
	goto .L34
	label .L33
	t59 = True
	goto .L35
	label .L34
	t59 = False
	label .L35
	if t59 == True: goto .L36
	goto .L37
	label .L36
	VALOR = 20
	goto .L38
	label .L37
	VALOR = 10
	label .L38
	t60 = VALOR
	return t60


@with_goto
def sp_validainsert():
	global pila
	t61 = 'insert into  tbbodega values(1,\'BODEGA CENTRAL\',1);'
	pila = [t61]
	funcionIntermedia()
	t62 = 'insert into  tbbodega (idbodega,bodega) values(2,\'BODEGA ZONA 12\');'
	pila = [t62]
	funcionIntermedia()
	t63 = 'insert into  tbbodega (idbodega,bodega,estado) values(3,\'BODEGA ZONA 11\',1);'
	pila = [t63]
	funcionIntermedia()
	t64 = 'insert into  tbbodega (idbodega,bodega,estado) values(4,\'BODEGA ZONA 1\',1);'
	pila = [t64]
	funcionIntermedia()
	t65 = 'insert into  tbbodega (idbodega,bodega,estado) values(5,\'BODEGA ZONA 10\',1);'
	pila = [t65]
	funcionIntermedia()


@with_goto
def sp_validaupdte():
	global pila
	t66 = 'update  tbbodega set bodega = \'bodega zona 9\' where idbodega = 4;'
	pila = [t66]
	funcionIntermedia()


@with_goto
def sp_insertaproducto( llave, producto, fecha):
	global pila
	t67 = 'insert into  tbProducto values(llave,producto,fecha,1);'
	pila = [t67]
	funcionIntermedia()


@with_goto
def fn_Mensaje( texto):
	global pila
	t68 = texto
	return t68


@with_goto
def fn_retornaproducto( Vproducto):
	global pila
	idp = 0
	t69 = 'select  idproducto from tbProducto where producto = Vproducto;'
	pila = [t69]
	funcionIntermedia()
	t70 = pila[0]
	idp = t70
	t71 = idp
	return t71


@with_goto
def fn_retornabodega( Vbodega):
	global pila
	idb = 0
	t72 = 'select  idbodega from tbbodega where bodega = Vbodega;'
	pila = [t72]
	funcionIntermedia()
	t73 = pila[0]
	idb = t73
	t74 = idb
	return t74


@with_goto
def sp_insertainventario( ide, Vproducto, Vbodega, cantidad, descripcion):
	global pila
	idproducto = 0
	idbodega = 0
	idev = 0
	t75 = 'select  count(*) from tbinventario where idinventario = ide;'
	pila = [t75]
	funcionIntermedia()
	t76 = pila[0]
	idev = t76
	if idev==0: goto .L39
	goto .L40
	label .L39
	t77 = True
	goto .L41
	label .L40
	t77 = False
	label .L41
	if t77 == True: goto .L42
	goto .L43
	label .L42
	t78 = 'select  fn_retornaproducto(Vproducto);'
	pila = [t78]
	funcionIntermedia()
	t79 = pila[0]
	idproducto = t79
	t80 = 'select  fn_retornabodega(Vbodega);'
	pila = [t80]
	funcionIntermedia()
	t81 = pila[0]
	idbodega = t81
	t82 = 'insert into  tbinventario values(ide,idproducto,idbodega,cantidad,now,descripcion);'
	pila = [t82]
	funcionIntermedia()
	label .L43
	t83 = ide
	return t83

if __name__ == "__main__": 
	 main()