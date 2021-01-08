
from Fase1.Sql import Sql
from goto import with_goto
heap = ''
def inter() -> str:
	global heap
	sql: Sql = Sql()
	result = str(sql.query(heap))
	return result

@with_goto
def principal():
	heap = 'CREATE DATABASE DBFase2;'
	t0 = inter()
	heap = 'USE DBFase2;'
	t1 = inter()
	t3 = myFuncion('INICIO CALIFICACION FASE 2')
	heap = 'CREATE TABLE tbProducto ( idproducto integer not null primary key, producto varchar(150) not null, fechacreacion date not null, estado integer );'
	t4 = inter()
	heap = 'CREATE TABLE tbCalificacion ( idcalifica integer not null primary key, item varchar(100) not null, punteo integer not null );'
	t5 = inter()
	t6 = '2021-01-08 16:14:28.070014'
	heap = 'insert into tbProducto values (1,'Laptop Lenovo',' + str(t6) + ',1);'
	t7 = inter()
	t8 = '2021-01-08 16:14:28.070076'
	heap = 'insert into tbProducto values (2,'Bateria para Laptop Lenovo T420',' + str(t8) + ',1);'
	t9 = inter()
	t10 = '2021-01-08 16:14:28.070113'
	heap = 'insert into tbProducto values (3,'Teclado Inalambrico',' + str(t10) + ',1);'
	t11 = inter()
	t12 = '2021-01-08 16:14:28.070147'
	heap = 'insert into tbProducto values (4,'Mouse Inalambrico',' + str(t12) + ',1);'
	t13 = inter()
	t14 = '2021-01-08 16:14:28.070182'
	heap = 'insert into tbProducto values (5,'WIFI USB',' + str(t14) + ',1);'
	t15 = inter()
	t16 = '2021-01-08 16:14:28.070215'
	heap = 'insert into tbProducto values (6,'Laptop HP',' + str(t16) + ',1);'
	t17 = inter()
	t18 = '2021-01-08 16:14:28.070249'
	heap = 'insert into tbProducto values (7,'Teclado Flexible USB',' + str(t18) + ',1);'
	t19 = inter()
	heap = 'insert into tbProducto values (8,'Laptop Samsung','2021-01-02',1);'
	t20 = inter()
	t21 = myFuncion('Crea Funcion')
	t38 = ValidaRegistros('tbProducto',8)
	heap = 'insert into tbCalificacion values (1,'Create Table and Insert',' + str(t38) + ');'
	t39 = inter()
	heap = 'update tbProducto set estado = 2 where estado = 1;'
	t40 = inter()
	t41 = ValidaRegistros('tbProductoUp',8)
	heap = 'insert into tbCalificacion values (2,'Update',' + str(t41) + ');'
	t42 = inter()
	t57 = CALCULOS()
	heap = 'insert into tbCalificacion values (3,' Valida Funciones',' + str(t57) + ');'
	t58 = inter()
	heap = 'create table tbbodega ( idbodega integer not null primary key, bodega varchar(100) not null, estado integer );'
	t59 = inter()
	t65 = sp_validainsert()
	t66 = ValidaRegistros('tbbodega',5)
	heap = 'insert into tbCalificacion values (4,'Valida Store Procedure',' + str(t66) + ');'
	t67 = inter()
	t69 = sp_validaupdate()
	t70 = ValidaRegistros('tbbodega',4)
	heap = 'insert into tbCalificacion values (5,'Valida Delete',' + str(t70) + ');'
	t71 = inter()
	heap = 'select * from tbbodega;'
	t72 = inter()
	t77 = sp_insertaproducto(9,'Bocina Inalambrica','2021-01-06')
	t78 = sp_insertaproducto(10,'Audifonos con Microfono USB','2021-01-06')
	t79 = sp_insertaproducto(11,'Bocina Inalambrica','2021-01-06')
	t80 = sp_insertaproducto(12,'Monitor de 17"','2021-01-06')
	t81 = ''
	t83 = ''
	t84 = sp_insertaproducto(13,'Bocina Inalambrica Sony','2021-01-06')
	t85 = sp_insertaproducto(14,'Audifonos con Microfono USB Lenovo','2021-01-06')
	t86 = sp_insertaproducto(15,'Monitor de 21"','2021-01-06')
	t87 = sp_insertaproducto(16,'Monitor de 17" Lenovo','2021-01-06')
	heap = 'create table tbinventario ( idinventario integer not null primary key, idproducto integer not null, idbodega integer not null, cantidad integer not null, fechacarga date not null, descripcion text );'
	t88 = inter()
	t109 = sp_insertainventario(1,'Laptop Lenovo','BODEGA CENTRAL',200,'Laptop Lenovo T420 i7 8GB')
	t110 = sp_insertainventario(2,'Teclado Inalambrico','BODEGA CENTRAL',100,'Teclado Inalambrico Lenovo')
	t111 = sp_insertainventario(3,'Mouse Inalambrico','BODEGA ZONA 12',50,'')
	t112 = sp_insertainventario(4,'Laptop HP','bodega zona 9',20,'Laptop HP i5 4GB RAM')


if __name__ == '__main__':
	principal()