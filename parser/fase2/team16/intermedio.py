from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto
def main():
	global heap
	global stack

	#Llamada a funcion o procedimiento.
	stack.append("F2")
	goto .F1
	label .F2

	goto .END

	label .F1
	#**** Procedimiento *****

	# Parametros

	# Retorno
	r0= 0

	# Declaraciones
	t0 = 0
	t1 = 0
	t2 = 0
	t3 = 0
	t4 = 0
	t5 = 0
	t6 = 0
	t7 = 0
	t8 = 0
	#Fin declaraciones

	t9 = t0 + 0
	t0 = t9

	t10 = t1 - 0
	t1 = t10

	t11 = t2 * 1
	t2 = t11

	t12 = t3 / 1
	t3 = t12

	t13 = t3 + 0
	t4 = t13

	t14 = t3 - 0
	t5 = t14

	t15 = t6 * 1
	t6 = t15

	t16 = t7 / 1
	t7 = t16

	t17 = t8 * 2
	t8 = t17

	t18 = t8 * 0
	 = t18

	t19 = 0 / t8
	 = t19

	t0 = t1

	t1 = t0

	# ------ If -------
	t20 = 100 == 100
	if t20:
		goto .L0
	else:
		goto .L1
	label .L0
	print("verdadero")
	t0 = t2

	goto .L2

	label .L1
	label .L2
	# ------ If -------
	t21 = 10 == 1
	if t21:
		goto .L3
	else:
		goto .L4
	label .L3
	print("verdadero")
	t0 = t2

	goto .L5

	label .L4
	label .L5

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
