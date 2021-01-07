lista = []


def funcionIntermedia():
	global lista
	prueba = lista.pop()
	print('******** ' + str(prueba))


def main():
	global lista
	t0 = " create database if not exists test owner = 'root' mode = 1;"
	lista = [t0 ]
	funcionIntermedia()
	t1 = "use test;"
	lista = [t1 ]
	funcionIntermedia()
	t2 = "create table tbusuario ( idusuario integer  not null  primary key ,nombre  varchar(50),apellido  varchar(50),usuario  varchar(15)  unique   not null ,password  varchar(15)  not null ,fechacreacion date );"
	lista = [t2 ]
	funcionIntermedia()
	t3 = "create table tbroles ( idrol integer  not null  primary key ,rol  varchar(15) );"
	lista = [t3 ]
	funcionIntermedia()
	t4 = "drop table tbroles;"
	lista = [t4 ]
	funcionIntermedia()
	t5 = "create table tbrol ( idrol integer  not null  primary key ,rol  varchar(15) );"
	lista = [t5 ]
	funcionIntermedia()
	t6 = "create table tbrolxusuario ( idrol integer  not null ,idusuario integer  not null  );"
	lista = [t6 ]
	funcionIntermedia()
	t7 = "alter table tbrolxusuario add  constraint FK_rol foreign key (idrol) references tbrol (idrol) ;"
	lista = [t7 ]
	funcionIntermedia()
	t8 = "alter table tbrolxusuario add  constraint FK_usuario foreign key (idusuario) references tbusuario (idusuario) ;"
	lista = [t8 ]
	funcionIntermedia()
	t9 = "insert into tbrol values (  1,'Administrador');"
	lista = [t9 ]
	funcionIntermedia()
	t10 = "insert into tbrol values (  2,'Admin');"
	lista = [t10 ]
	funcionIntermedia()
	t11 = "insert into tbrol values (  3,'Ventas');"
	lista = [t11 ]
	funcionIntermedia()
	t12 = "select * from tbrol;"
	lista = [t12 ]
	funcionIntermedia()
	t13 = "insert into tbusuario values (      1,'Luis Fernando','Salazar Rodriguez','lsalazar', MD5 ( 'paswword'),now());"
	lista = [t13 ]
	funcionIntermedia()
	t14 = "alter table tbusuario  alter column password type varchar (80);"
	lista = [t14 ]
	funcionIntermedia()
	t15 = "insert into tbusuario values (      1,'Luis Fernando','Salazar Rodriguez','lsalazar', MD5 ( 'paswword'),now());"
	lista = [t15 ]
	funcionIntermedia()
	t16 = "insert into tbusuario values (      1,'Maria Cristina','Lopez Ramirez','mlopez', MD5 ( 'Diciembre'),now());"
	lista = [t16 ]
	funcionIntermedia()
	t17 = "insert into tbusuario values (      1,'Hugo Alberto','Huard Ordoñez','hhuard', MD5 ( 'Rafael'),now());"
	lista = [t17 ]
	funcionIntermedia()
	t18 = "select * from tbusuario;"
	lista = [t18 ]
	funcionIntermedia()
	t19 = "insert into tbusuario values (      1,'Luis Fernando','Salazar Rodriguez','lsalazar', MD5 ( 'paswword'),now());"
	lista = [t19 ]
	funcionIntermedia()
	t20 = "insert into tbusuario values (      2,'Maria Cristina','Lopez Ramirez','mlopez', MD5 ( 'Diciembre'),now());"
	lista = [t20 ]
	funcionIntermedia()
	t21 = "insert into tbusuario values (      3,'Hugo Alberto','Huard Ordoñez','hhuard', MD5 ( 'Rafael'),now());"
	lista = [t21 ]
	funcionIntermedia()
	t22 = "insert into tbrolxusuario values (  1,1);"
	lista = [t22 ]
	funcionIntermedia()
	t23 = "insert into tbrolxusuario values (  2,2);"
	lista = [t23 ]
	funcionIntermedia()
	t24 = "insert into tbrolxusuario values (  2,3);"
	lista = [t24 ]
	funcionIntermedia()
	t25 = "select * from tbrol R  where idrol not in (select idrol from tbrolxusuario)  ;"
	lista = [t25 ]
	funcionIntermedia()
	t26 = "select * from tbrol R  where  not  exists (select idrol from tbrolxusuario RU  where RU.idrol = R.idrol)  ;"
	lista = [t26 ]
	funcionIntermedia()
	t27 = "create table tbestado ( idestado integer  not null  primary key ,estado  varchar(30) );"
	lista = [t27 ]
	funcionIntermedia()
	t28 = "create table tbempleado ( idempleado integer  not null   unique  primary key ,primernombre  varchar(50)  not null ,segundonombre  varchar(50),primerapellido  varchar(50)  not null ,segundoapellido  varchar(50),fechadenacimiento DATE  constraint birth_data check fechadenacimiento > '1900-01-01',fechacontratacion DATE  check fechacontratacion > fechadenacimiento,idestado integer );"
	lista = [t28 ]
	funcionIntermedia()
	t29 = "alter table tbempleado add  constraint FK_estado foreign key (idestado) references tbestado (idestado) ;"
	lista = [t29 ]
	funcionIntermedia()
	t30 = "create table tbempleadoidentificacion ( idempleado integer  not null  primary key ,identificacion  varchar(25)  not null ,ididentificaciontipo integer );"
	lista = [t30 ]
	funcionIntermedia()
	t31 = "create table tbidentificaciontipo ( ididentificaciontipo integer  not null  primary key ,tipoidentificacion  varchar(20) );"
	lista = [t31 ]
	funcionIntermedia()
	t32 = "alter table tbempleadoidentificacion add  constraint FK_identificaciontipo foreign key (ididentificaciontipo) references tbidentificaciontipo (ididentificaciontipo) ;"
	lista = [t32 ]
	funcionIntermedia()
	t33 = "insert into tbidentificaciontipo values (  1,'DPI');"
	lista = [t33 ]
	funcionIntermedia()
	t34 = "insert into tbidentificaciontipo values (  2,'Nit');"
	lista = [t34 ]
	funcionIntermedia()
	t35 = "insert into tbidentificaciontipo values (  3,'Pasaporte');"
	lista = [t35 ]
	funcionIntermedia()
	t36 = "insert into tbestado values (  1,'Activo');"
	lista = [t36 ]
	funcionIntermedia()
	t37 = "insert into tbestado values (  2,'Inactivo');"
	lista = [t37 ]
	funcionIntermedia()
	t38 = "insert into tbempleado (      idempleado,primernombre,primerapellido,fechanacimiento,fechacontartacion,idestado) values (     1,'Thelma','Esquit','1981-01-25','2014-07-06',1);"
	lista = [t38 ]
	funcionIntermedia()
	t39 = "insert into tbempleado (        idempleado,primernombre,segundonombre,primerapellido,segundoapellido,fechadenacimiento,fechacontratacion,idestado) values (       5,'Francisco','','Juarez','Perez','1997-10-05','2010-03-01',1);"
	lista = [t39 ]
	funcionIntermedia()
	t40 = "insert into tbempleadoidentificacion values (   1,'4578-784525-6562',1);"
	lista = [t40 ]
	funcionIntermedia()
	t41 = "insert into tbempleadoidentificacion values (   1,'8874585-5',2);"
	lista = [t41 ]
	funcionIntermedia()
	t42 = "insert into tbempleadoidentificacion values (   2,'1245-488454-7854',1);"
	lista = [t42 ]
	funcionIntermedia()
	t43 = "insert into tbempleadoidentificacion values (   3,'2610-417055-0101',1);"
	lista = [t43 ]
	funcionIntermedia()
	t44 = "drop table tbempleadoidentificacion;"
	lista = [t44 ]
	funcionIntermedia()
	t45 = "create table tbempleadoidentificacion ( idempleado integer  not null ,ididentificaciontipo integer  not null ,identificacion  varchar(25)  not null ,primary key (idempleado,ididentificaciontipo) );"
	lista = [t45 ]
	funcionIntermedia()
	t46 = "insert into tbempleadoidentificacion values (   1,1,'4578-784525-6562');"
	lista = [t46 ]
	funcionIntermedia()
	t47 = "insert into tbempleadoidentificacion values (   1,2,'8874585-5');"
	lista = [t47 ]
	funcionIntermedia()
	t48 = "insert into tbempleadoidentificacion values (   2,1,'1245-488454-7854');"
	lista = [t48 ]
	funcionIntermedia()
	t49 = "insert into tbempleadoidentificacion values (   3,1,'2610-417055-0101');"
	lista = [t49 ]
	funcionIntermedia()
	t50 = "select E.*,estado,I.identificacion,tipoidentificacion from tbempleado E ,tbestado ES ,tbempleadoidentificacion I ,tbidentificaciontipo IT  where ES.idestado = E.idestado and I.idempleado = E.idempleado and IT.ididentificaciontipo = I.ididentificaciontipo;"
	lista = [t50 ]
	funcionIntermedia()
	t51 = "select E.*,estado,I.identificacion,tipoidentificacion from tbempleado E ,bestado ES ,tbempleadoidentificacion I ,tbidentificaciontipo IT  where ES.idestado = E.idestado and I.idempleado = E.idempleado and IT.ididentificaciontipo = I.ididentificaciontipo;"
	lista = [t51 ]
	funcionIntermedia()
	t52 = "select E.*,estado,I.identificacion,tipoidentificacion from tbempleado E ,tbestado ES ,tbempleadoidentificacion I ,tbidentificaciontipo IT  where ES.idestado = E.idestado and I.idempleado = E.idempleado and IT.ididentificaciontipo = I.ididentificaciontipo;"
	lista = [t52 ]
	funcionIntermedia()


if __name__ == "__main__":
	 main()
