from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	t0 = """CREATE DATABASE DBFase2;"""
	heap.append(t0)
	F3D.ejecutarSQL()

	t1 = """USE DBFase2;"""
	heap.append(t1)
	F3D.ejecutarSQL()

	t2 = """
 CREATE TABLE tbbodega (
  
 idbodega  integer   not null     primary key    
,   
 bodega  varchar( 100)   not null    
,   
 estado  integer  
  );
"""
	heap.append(t2)
	F3D.ejecutarSQL()

	t3 = "CREATE INDEX idexbodega ON tbbodega (bodega);"
	heap.append(t3)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	stack.append("F2")
	goto .F1
	label .F2
	#Llamada a funcion o procedimiento.
	stack.append("F4")
	goto .F3
	label .F4
	#Llamada a funcion o procedimiento.
	p0="INICIO CALIFICACION FASE 2"
	stack.append("F6")
	goto .F5
	label .F6
	t5 = r2

	t5 = "SELECT '" + str(t5) + "';"
	heap.append(t5)
	F3D.ejecutarSQL()

	t6 = """
 CREATE TABLE tbProducto (
  
 idproducto  integer   not null     primary key    
,   
 producto  varchar( 150)   not null    
,   
 fechacreacion  date   not null    
,   
 estado  integer  
  );
"""
	heap.append(t6)
	F3D.ejecutarSQL()

	t7 = "CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);"
	heap.append(t7)
	F3D.ejecutarSQL()

	t8 = """
 CREATE TABLE tbCalificacion (
  
 idcalifica  integer   not null     primary key    
,   
 item  varchar( 100)   not null    
,   
 punteo  integer   not null    
  );
"""
	heap.append(t8)
	F3D.ejecutarSQL()

	t9 = "CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);"
	heap.append(t9)
	F3D.ejecutarSQL()



	heap.append(56)
	t10 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t10)
	heap.append("Laptop Lenovo")
	heap.append(1)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t11 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t11)
	heap.append("Bateria para Laptop Lenovo T420")
	heap.append(2)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t12 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t12)
	heap.append("Teclado Inalambrico")
	heap.append(3)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t13 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t13)
	heap.append("Mouse Inalambrico")
	heap.append(4)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t14 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t14)
	heap.append("WIFI USB")
	heap.append(5)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t15 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t15)
	heap.append("Laptop HP")
	heap.append(6)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()


	heap.append(56)
	t16 = F3D.funcionNativa()


	heap.append(1)
	heap.append(t16)
	heap.append("Teclado Flexible USB")
	heap.append(7)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()



	heap.append(1)
	heap.append("2021-01-02")
	heap.append("Laptop Samsung")
	heap.append(8)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()
	#Llamada a funcion o procedimiento.
	p0="Crea Funcion"
	stack.append("F7")
	goto .F5
	label .F7
	t17 = r2

	t17 = "SELECT '" + str(t17) + "';"
	heap.append(t17)
	F3D.ejecutarSQL()



	#Llamada a funcion o procedimiento.
	p1="tbProducto"
	p2=8
	stack.append("F9")
	goto .F8
	label .F9
	t26 = r3

	heap.append(t26)
	heap.append("Create Table and Insert")
	heap.append(1)
	heap.append(3)
	heap.append('tbCalificacion')
	F3D.insert()
	t27 = """ UPDATE  tbProducto  SET   estado = 2  WHERE  estado = 1; """
	heap.append(t27)
	F3D.ejecutarSQL()



	#Llamada a funcion o procedimiento.
	p1="tbProductoUp"
	p2=8
	stack.append("F10")
	goto .F8
	label .F10
	t28 = r3

	heap.append(t28)
	heap.append("Update")
	heap.append(2)
	heap.append(3)
	heap.append('tbCalificacion')
	F3D.insert()


	#Llamada a funcion o procedimiento.
	stack.append("F12")
	goto .F11
	label .F12
	t48 = r4

	heap.append(t48)
	heap.append(" Valida Funciones")
	heap.append(3)
	heap.append(3)
	heap.append('tbCalificacion')
	F3D.insert()
	t49 = "CREATE INDEX idx_bodega ON tbbodega (bodega, estado);"
	heap.append(t49)
	F3D.ejecutarSQL()

	t50 = """ DROP INDEX idx_bodega ;  """
	heap.append(t50)
	F3D.ejecutarSQL()

	t51 = "CREATE INDEX idx_bodega ON tbbodega (bodega, estado);"
	heap.append(t51)
	F3D.ejecutarSQL()



	#Llamada a funcion o procedimiento.
	p1="tbbodega"
	p2=5
	stack.append("F13")
	goto .F8
	label .F13
	t52 = r3

	heap.append(t52)
	heap.append("Valida Store Procedure")
	heap.append(4)
	heap.append(3)
	heap.append('tbCalificacion')
	F3D.insert()
	t53 = """ DELETE  From tbbodega WHERE idbodega = 4;  """
	heap.append(t53)
	F3D.ejecutarSQL()



	#Llamada a funcion o procedimiento.
	p1="tbbodega"
	p2=4
	stack.append("F14")
	goto .F8
	label .F14
	t54 = r3

	heap.append(t54)
	heap.append("Valida Delete")
	heap.append(5)
	heap.append(3)
	heap.append('tbCalificacion')
	F3D.insert()
	t55 = """Select  * from tbbodega; 
"""
	heap.append(t55)
	F3D.ejecutarSQL()

	t56 = "CREATE INDEX idx_bodega ON tbbodega (estado);"
	heap.append(t56)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p3=9
	p4="Bocina Inalambrica"
	p5="2021-01-06"
	stack.append("F16")
	goto .F15
	label .F16
	#Llamada a funcion o procedimiento.
	p3=10
	p4="Audifonos con Microfono USB"
	p5="2021-01-06"
	stack.append("F17")
	goto .F15
	label .F17
	#Llamada a funcion o procedimiento.
	p3=11
	p4="Bocina Inalambrica"
	p5="2021-01-06"
	stack.append("F18")
	goto .F15
	label .F18
	#Llamada a funcion o procedimiento.
	p3=12
	p4="Monitor de 17in"
	p5="2021-01-06"
	stack.append("F19")
	goto .F15
	label .F19
	#Llamada a funcion o procedimiento.
	p3=13
	p4="Bocina Inalambrica Sony"
	p5="2021-01-06"
	stack.append("F21")
	goto .F15
	label .F21
	#Llamada a funcion o procedimiento.
	p3=14
	p4="Audifonos con Microfono USB Lenovo"
	p5="2021-01-06"
	stack.append("F22")
	goto .F15
	label .F22
	#Llamada a funcion o procedimiento.
	p3=15
	p4="Monitor de 21in"
	p5="2021-01-06"
	stack.append("F23")
	goto .F15
	label .F23
	#Llamada a funcion o procedimiento.
	p3=16
	p4="Monitor de 17in Lenovo"
	p5="2021-01-06"
	stack.append("F24")
	goto .F15
	label .F24
	t57 = """
 CREATE TABLE tbinventario (
  
 idinventario  integer   not null     primary key    
,   
 idproducto  integer   not null    
,   
 idbodega  integer   not null    
,   
 cantidad  integer   not null    
,   
 fechacarga  date   not null    
,   
 descripcion  text  
  );
"""
	heap.append(t57)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p7="Bocina Inalambrica"
	stack.append("F26")
	goto .F25
	label .F26
	t60 = r7

	t60 = "SELECT '" + str(t60) + "';"
	heap.append(t60)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p8="BODEGA CENTRAL"
	stack.append("F28")
	goto .F27
	label .F28
	t63 = r8

	t63 = "SELECT '" + str(t63) + "';"
	heap.append(t63)
	F3D.ejecutarSQL()





	heap.append(56)
	t64 = F3D.funcionNativa()


	heap.append("")
	heap.append(t64)
	heap.append(-1)
	heap.append(-1)
	heap.append(-1)
	heap.append(-1)
	heap.append(6)
	heap.append('tbinventario')
	F3D.insert()
	#Llamada a funcion o procedimiento.
	p9=1
	p10="Laptop Lenovo"
	p11="BODEGA CENTRAL"
	p12=200
	p13="Laptop Lenovo T420 i7 8GB"
	stack.append("F32")
	goto .F29
	label .F32
	t73 = r9

	t73 = "SELECT '" + str(t73) + "';"
	heap.append(t73)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p9=2
	p10="Teclado Inalambrico"
	p11="BODEGA CENTRAL"
	p12=100
	p13="Teclado Inalambrico Lenovo"
	stack.append("F33")
	goto .F29
	label .F33
	t74 = r9

	t74 = "SELECT '" + str(t74) + "';"
	heap.append(t74)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p9=3
	p10="Mouse Inalambrico"
	p11="BODEGA ZONA 12"
	p12=50
	p13="L"
	stack.append("F34")
	goto .F29
	label .F34
	t75 = r9

	t75 = "SELECT '" + str(t75) + "';"
	heap.append(t75)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	p9=4
	p10="Laptop HP"
	p11="bodega zona 9"
	p12=20
	p13="Laptop HP i5 4GB RAM"
	stack.append("F35")
	goto .F29
	label .F35
	t76 = r9

	t76 = "SELECT '" + str(t76) + "';"
	heap.append(t76)
	F3D.ejecutarSQL()


	goto .END

	label .F1
	#**** Procedimiento *****

	# Parametros 

	# Retorno 
	r0 = 0

	# Declaraciones 
	#Fin declaraciones




	heap.append(1)
	heap.append("BODEGA CENTRAL")
	heap.append(1)
	heap.append(3)
	heap.append('tbbodega')
	F3D.insert()


	heap.append(1)
	heap.append("BODEGA ZONA 12")
	heap.append(2)
	heap.append(3)
	heap.append('tbbodega')
	F3D.insert()


	heap.append(1)
	heap.append("BODEGA ZONA 11")
	heap.append(3)
	heap.append(3)
	heap.append('tbbodega')
	F3D.insert()


	heap.append(1)
	heap.append("BODEGA ZONA 1")
	heap.append(4)
	heap.append(3)
	heap.append('tbbodega')
	F3D.insert()


	heap.append(1)
	heap.append("BODEGA ZONA 10")
	heap.append(5)
	heap.append(3)
	heap.append('tbbodega')
	F3D.insert()
	goto .R


	label .F3
	#**** Procedimiento *****

	# Parametros 

	# Retorno 
	r1 = 0

	# Declaraciones 
	#Fin declaraciones


	t4 = """ UPDATE  tbbodega  SET   bodega = "bodega zona 9"  WHERE  idbodega = 4; """
	heap.append(t4)
	F3D.ejecutarSQL()

	goto .R


	label .F5
	#**** Funcion *****

	# Parametros 
	p0

	# Retorno 
	r2= 0

	# Declaraciones 
	#Fin declaraciones



	# Return
	r2 = p0
	goto .R


	goto .R


	label .F8
	#**** Funcion *****

	# Parametros 
	p1
	p2

	# Retorno 
	r3= 0

	# Declaraciones 
	t18 = 0
	t19 = 0
	#Fin declaraciones

	# ------ If ------- 
	t20 = p1 == "tbProducto"
	if t20: 
		goto .L0
	else: 
		goto .L1
	label .L0
	print("verdadero")
	t18 = 8

	# ------ If ------- 
	t21 = p2 == t18
	if t21: 
		goto .L3
	else: 
		goto .L4
	label .L3
	print("verdadero")
	t19 = 1

	goto .L5

	label .L4
	print("falso")
	t19 = 0

	label .L5
	goto .L2

	label .L1
	label .L2
	# ------ If ------- 
	t22 = p1 == "tbProductoUp"
	if t22: 
		goto .L6
	else: 
		goto .L7
	label .L6
	print("verdadero")
	t18 = 0

	# ------ If ------- 
	t23 = p2 == t18
	if t23: 
		goto .L9
	else: 
		goto .L10
	label .L9
	print("verdadero")
	t19 = 1

	goto .L11

	label .L10
	print("falso")
	t19 = 0

	label .L11
	goto .L8

	label .L7
	label .L8
	# ------ If ------- 
	t24 = p1 == "tbbodega"
	if t24: 
		goto .L12
	else: 
		goto .L13
	label .L12
	print("verdadero")
	t18 = 5

	# ------ If ------- 
	t25 = p2 == t18
	if t25: 
		goto .L15
	else: 
		goto .L16
	label .L15
	print("verdadero")
	t19 = 1

	goto .L17

	label .L16
	print("falso")
	t19 = 0

	label .L17
	goto .L14

	label .L13
	label .L14


	# Return
	r3 = t19
	goto .R


	goto .R


	label .F11
	#**** Funcion *****

	# Parametros 

	# Retorno 
	r4= 0

	# Declaraciones 
	t29 = 0
	t30 = 0
	t31 = 0
	t32 = 0
	#Fin declaraciones



	heap.append("2001-02-16 20:38:40")
	heap.append("HOUR")

	heap.append(57)
	t33 = F3D.funcionNativa()
	t29 = t33


	heap.append(1)

	heap.append(35)
	t34 = F3D.funcionNativa()
	t30 = t34

	t35 = t30 * t29
	t35 = t30 * t29


	heap.append(0)
	heap.append(t35)

	heap.append(21)
	t36 = F3D.funcionNativa()
	t31 = t36




	heap.append(4)
	heap.append(1)
	heap.append("FASE2")

	heap.append(46)
	t37 = F3D.funcionNativa()



	heap.append(4)
	heap.append(1)
	heap.append("FASE2")

	heap.append(46)
	t37 = F3D.funcionNativa()

	heap.append(t37)

	heap.append(45)
	t38 = F3D.funcionNativa()
	t39 = t31 + t38
	t31 = t39


	heap.append(-1)

	heap.append(39)
	t40 = F3D.funcionNativa()

	heap.append(-1)

	heap.append(39)
	t40 = F3D.funcionNativa()

	heap.append(t40)

	heap.append(1)
	t41 = F3D.funcionNativa()
	t32 = t41


	heap.append(225)

	heap.append(19)
	t42 = F3D.funcionNativa()
	t43 = t32 * t42
	t32 = t43

	t44 = t31 + t32

	heap.append(0.5)

	heap.append(24)
	t45 = F3D.funcionNativa()
	t46 = t44 / t45
	t31 = t46

	# ------ If ------- 
	t47 = t31 > 1
	if t47: 
		goto .L18
	else: 
		goto .L19
	label .L18
	print("verdadero")
	t31 = 20

	goto .L20

	label .L19
	print("falso")
	t31 = 10

	label .L20


	# Return
	r4 = t31
	goto .R


	goto .R


	label .F15
	#**** Procedimiento *****

	# Parametros 
	p3
	p4
	p5

	# Retorno 
	r5 = 0

	# Declaraciones 
	#Fin declaraciones





	heap.append(1)
	heap.append(p5)
	heap.append(p4)
	heap.append(p3)
	heap.append(4)
	heap.append('tbProducto')
	F3D.insert()
	goto .R


	label .F20
	#**** Funcion *****

	# Parametros 
	p6

	# Retorno 
	r6= 0

	# Declaraciones 
	#Fin declaraciones



	# Return
	r6 = p6
	goto .R


	goto .R


	label .F25
	#**** Funcion *****

	# Parametros 
	p7

	# Retorno 
	r7= 0

	# Declaraciones 
	t58 = 0
	#Fin declaraciones


	t59 = """Select idproducto From  tbProducto Where  tbProducto.producto = '""" + str(p7) + """'; """
	heap.append(t59)
	F3D.ejecutarSQL()
	t58 = heap[-1]



	# Return
	r7 = t58
	goto .R


	goto .R


	label .F27
	#**** Funcion *****

	# Parametros 
	p8

	# Retorno 
	r8= 0

	# Declaraciones 
	t61 = 0
	#Fin declaraciones


	t62 = """Select idbodega From  tbbodega Where  tbbodega.bodega = '""" + str(p8) + """'; """
	heap.append(t62)
	F3D.ejecutarSQL()
	t61 = heap[-1]



	# Return
	r8 = t61
	goto .R


	goto .R


	label .F29
	#**** Funcion *****

	# Parametros 
	p9
	p10
	p11
	p12
	p13

	# Retorno 
	r9= 0

	# Declaraciones 
	t65 = 0
	t66 = 0
	t67 = 0
	#Fin declaraciones


	t68 = """Select COUNT (*) From  tbinventario Where  tbinventario.idinventario = """ + str(p9) + """; """
	heap.append(t68)
	F3D.ejecutarSQL()
	t67 = heap[-1]

	# ------ If ------- 
	t69 = t67 == 0
	if t69: 
		goto .L21
	else: 
		goto .L22
	label .L21
	print("verdadero")

	#Llamada a funcion o procedimiento.
	p7=p7
	stack.append("F30")
	goto .F25
	label .F30
	t70 = r7
	t65 = t70


	#Llamada a funcion o procedimiento.
	p8=p8
	stack.append("F31")
	goto .F27
	label .F31
	t71 = r8
	t66 = t71






	heap.append(56)
	t72 = F3D.funcionNativa()


	heap.append(p13)
	heap.append(t72)
	heap.append(p12)
	heap.append(t66)
	heap.append(t65)
	heap.append(p9)
	heap.append(6)
	heap.append('tbinventario')
	F3D.insert()

	goto .L23

	label .L22
	label .L23


	# Return
	r9 = p9
	goto .R


	goto .R


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2
	if u == "F3": 
		goto .F3
	if u == "F4": 
		goto .F4
	if u == "F5": 
		goto .F5
	if u == "F6": 
		goto .F6
	if u == "F7": 
		goto .F7
	if u == "F8": 
		goto .F8
	if u == "F9": 
		goto .F9
	if u == "F10": 
		goto .F10
	if u == "F11": 
		goto .F11
	if u == "F12": 
		goto .F12
	if u == "F13": 
		goto .F13
	if u == "F14": 
		goto .F14
	if u == "F15": 
		goto .F15
	if u == "F16": 
		goto .F16
	if u == "F17": 
		goto .F17
	if u == "F18": 
		goto .F18
	if u == "F19": 
		goto .F19
	if u == "F20": 
		goto .F20
	if u == "F21": 
		goto .F21
	if u == "F22": 
		goto .F22
	if u == "F23": 
		goto .F23
	if u == "F24": 
		goto .F24
	if u == "F25": 
		goto .F25
	if u == "F26": 
		goto .F26
	if u == "F27": 
		goto .F27
	if u == "F28": 
		goto .F28
	if u == "F29": 
		goto .F29
	if u == "F30": 
		goto .F30
	if u == "F31": 
		goto .F31
	if u == "F32": 
		goto .F32
	if u == "F33": 
		goto .F33
	if u == "F34": 
		goto .F34
	if u == "F35": 
		goto .F35

	label .END
