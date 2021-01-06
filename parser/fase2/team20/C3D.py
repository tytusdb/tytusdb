from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
from goto import with_goto

@with_goto
def up():
<<<<<<< HEAD
	print(VALIDAREGISTROS('TBPRODUCTO',1))
	print(VALIDAREGISTROS('TBPRODUCTO',2))
	print(VALIDAREGISTROS('TBPRODUCTOUP',2))
	print(VALIDAREGISTROS('TBPRODUCTOUP',1))
	print(VALIDAREGISTROS('TBBODEGA',3))
	print(VALIDAREGISTROS('TBBODEGA',1))

@with_goto
def VALIDAREGISTROS(TABLA: str, CANTIDAD: int) ->int:
	RESULTADO:int
	RETORNA:int
	t0=TABLA
	t1='TBPRODUCTO'
	t2=t0 == t1
	if t2:
		goto .lbl0
	else:
		goto. lbl4
	label .lbl0
	t3=1
	RESULTADO=t3
	t4=CANTIDAD
	t5=RESULTADO
	t6=t4 == t5
	if t6:
		goto .lbl1
	else:
		goto. lbl2
	label .lbl1
	t7=1
	RETORNA=t7
	goto .lbl3
	label .lbl2
	t8=0
	RETORNA=t8
	label .lbl3
	label .lbl4
	t9=TABLA
	t10='TBPRODUCTOUP'
	t11=t9 == t10
	if t11:
		goto .lbl5
	else:
		goto. lbl9
	label .lbl5
	t12=2
	RESULTADO=t12
	t13=CANTIDAD
	t14=RESULTADO
	t15=t13 == t14
	if t15:
		goto .lbl6
	else:
		goto. lbl7
	label .lbl6
	t16=1
	RETORNA=t16
	goto .lbl8
	label .lbl7
	t17=0
	RETORNA=t17
	label .lbl8
	label .lbl9
	t18=TABLA
	t19='TBBODEGA'
	t20=t18 == t19
	if t20:
		goto .lbl10
	else:
		goto. lbl14
	label .lbl10
	t21=3
	RESULTADO=t21
	t22=CANTIDAD
	t23=RESULTADO
	t24=t22 == t23
	if t24:
		goto .lbl11
	else:
		goto. lbl12
	label .lbl11
	t25=1
	RETORNA=t25
	goto .lbl13
	label .lbl12
	t26=0
	RETORNA=t26
	label .lbl13
	label .lbl14
	t27=RETORNA
	return t27

up()
=======
	print(1)

def SALES_TAX(SUBTOTAL: float) ->float:
	t0=23
	t1=5
	t2=t0*t1
	t3=6
	t4=2
	t5=t3/t4
	t6=t2+t5
	TOTAL:float=t6
	print(1)
>>>>>>> a29902789cc622cad6c3a731cde75479ec3aea50
