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

	t3 = "CREATE INDEX id_index ON tbbodega (bodega);"
	heap.append(t3)
	F3D.ejecutarSQL()

	#Llamada a funcion o procedimiento.
	stack.append("F2")
	goto .F1
	label .F2
	t9 = """ DELETE  From tbbodega WHERE idbodega = 4;  """
	heap.append(t9)
	F3D.ejecutarSQL()

	t10 = """Select  idbodega,bodega from tbbodega; 
"""
	heap.append(t10)
	F3D.ejecutarSQL()


	goto .END

	label .F1
	#**** Funcion *****

	# Parametros 

	# Retorno 
	global r0

	# Declaraciones 
	#Fin declaraciones


	t4 = """ INSERT INTO   tbbodega  values(  1,  "BODEGA CENTRAL",  1   );"""
	heap.append(t4)
	F3D.ejecutarSQL()

	t5 = """ INSERT INTO   tbbodega  values(  4,  "BODEGA ZONA 12",  1   );"""
	heap.append(t5)
	F3D.ejecutarSQL()

	t6 = """ INSERT INTO   tbbodega  values(  4,  "BODEGA ZONA 11",  1   );"""
	heap.append(t6)
	F3D.ejecutarSQL()

	t7 = """ INSERT INTO   tbbodega  values(  4,  "BODEGA ZONA 1",  1   );"""
	heap.append(t7)
	F3D.ejecutarSQL()

	t8 = """ INSERT INTO   tbbodega  values(  5,  "BODEGA ZONA 10",  1   );"""
	heap.append(t8)
	F3D.ejecutarSQL()

	goto .R


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2

	label .END
