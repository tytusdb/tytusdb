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

	#Llamada a funcion o procedimiento.
	p0="INICIO CALIFICACION FASE 2"
	stack.append("F2")
	goto .F1
	label .F2
	t2 = """
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
	heap.append(t2)
	F3D.ejecutarSQL()

	t3 = "CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);"
	heap.append(t3)
	F3D.ejecutarSQL()

	t4 = """
 CREATE TABLE tbCalificacion (
  
 idcalifica  integer   not null     primary key    
,   
 item  varchar( 100)   not null    
,   
 punteo  integer   not null    
  );
"""
	heap.append(t4)
	F3D.ejecutarSQL()

	t5 = "CREATE UNIQUE INDEX id_calificacion ON tbCalificacion (idcalifica);"
	heap.append(t5)
	F3D.ejecutarSQL()

	t6 = """ ALTER INDEX idx_califica RENAME TO id_calificacion ;  """
	heap.append(t6)
	F3D.ejecutarSQL()


	goto .END

	label .F1
	#**** Funcion *****

	# Parametros 
	p0

	# Retorno 
	global r0

	# Declaraciones 
	#Fin declaraciones


	print(" |>> " + str(p0)) 


	# Return
	r0 = p0
	goto .R


	goto .R


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2

	label .END
