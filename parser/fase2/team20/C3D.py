from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
from execution.executeInstruction import createFunction, deleteFunction
from goto import with_goto
import math

@with_goto
def up():
	print(1)

	createFunction('CALCULOS','''
@with_goto
def CALCULOS():
	HORA:int
	SENO:float
	VALOR:int
	ABSOLUTO:float
	t0=20
	HORA=t0
	t1=1
	t2=math.sin(t1)
	SENO=t2
	t3=SENO
	t4=HORA
	t5=t3*t4
	t6=math.trunc(t5)
	VALOR=t6
	t7=VALOR
	t8=4
	t9=t7+t8
	VALOR=t9
	t10=1
	t11=-t10
	t12=math.sinh(t11)
	t13=t12>0
	t14=t12<0
	t15=t13-t14
	t16=t12*t15
	ABSOLUTO=t16
	t17=ABSOLUTO
	t18=225
	t19=1/2
	t20=t18**t19
	t21=t17*t20
	ABSOLUTO=t21
	t22=VALOR
	t23=ABSOLUTO
	t24=t22+t23
	t25=0.5
	t26=math.degrees(math.acos(t25))
	t27=t24/t26
	VALOR=t27
	t28=VALOR
	t29=1
	t30=t28 > t29
	if t30:
		goto .lbl0
	else:
		goto. lbl1
	label .lbl0
	t31=20
	VALOR=t31
	goto .lbl2
	label .lbl1
	t32=10
	VALOR=t32
	label .lbl2
	t33=VALOR
	return t33
''',False)


	print(CALCULOS())


@with_goto
def CALCULOS():
	HORA:int
	SENO:float
	VALOR:int
	ABSOLUTO:float
	t0=20
	HORA=t0
	t1=1
	t2=math.sin(t1)
	SENO=t2
	t3=SENO
	t4=HORA
	t5=t3*t4
	t6=math.trunc(t5)
	VALOR=t6
	t7=VALOR
	t8=4
	t9=t7+t8
	VALOR=t9
	t10=1
	t11=-t10
	t12=math.sinh(t11)
	t13=t12>0
	t14=t12<0
	t15=t13-t14
	t16=t12*t15
	ABSOLUTO=t16
	t17=ABSOLUTO
	t18=225
	t19=1/2
	t20=t18**t19
	t21=t17*t20
	ABSOLUTO=t21
	t22=VALOR
	t23=ABSOLUTO
	t24=t22+t23
	t25=0.5
	t26=math.degrees(math.acos(t25))
	t27=t24/t26
	VALOR=t27
	t28=VALOR
	print(t28)
	t29=1
	t30=t28 > t29
	if t30:
		goto .lbl0
	else:
		goto. lbl1
	label .lbl0
	t31=20
	VALOR=t31
	goto .lbl2
	label .lbl1
	t32=10
	VALOR=t32
	label .lbl2
	t33=VALOR
	return t33

up()