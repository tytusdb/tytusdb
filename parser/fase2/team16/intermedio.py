from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack


	goto .END

	label .F1
	#**** Procedimiento *****

	# Parametros 

	# Retorno 
	r0 = 0

	# Declaraciones 
	#Fin declaraciones


	goto .R


	label .F2
	#**** Procedimiento *****

	# Parametros 

	# Retorno 
	r1 = 0

	# Declaraciones 
	#Fin declaraciones


	goto .R


	label .F3
	#**** Procedimiento *****

	# Parametros 

	# Retorno 
	r2 = 0

	# Declaraciones 
	#Fin declaraciones


	goto .R


	label .R
	u = stack.pop()
	if u == "F1": 
		goto .F1
	if u == "F2": 
		goto .F2
	if u == "F3": 
		goto .F3

	label .END
