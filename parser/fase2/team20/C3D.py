from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
from goto import with_goto

@with_goto
def up():
	print(1)

	executeSentence(CreateDatabase,CreateDatabase('DBFASE2',False,False,[None, None]))
	executeSentence(Use,Use('DBFASE2'))
	t1='INICIO CALIFICACION FASE 2'

	print(MYFUNCION(t1))

	executeSentence(CreateTable,CreateTable('TBPRODUCTO',[ColumnId('IDPRODUCTO',['INTEGER'],{'null': False, 'primary': True}), ColumnId('PRODUCTO',['VARCHAR', 150],{'null': False}), ColumnId('FECHACREACION',['DATE'],{'null': False}), ColumnId('ESTADO',['INTEGER'],None)],None))
	executeSentence(CreateIndex,CreateIndex('IDX_PRODUCTO','TBPRODUCTO',['IDPRODUCTO']))
	executeSentence(CreateTable,CreateTable('TBCALIFICACION',[ColumnId('IDCALIFICA',['INTEGER'],{'null': False, 'primary': True}), ColumnId('ITEM',['VARCHAR', 100],{'null': False}), ColumnId('PUNTEO',['INTEGER'],{'null': False})],None))
	executeSentence(CreateIndex,CreateIndex('IDX_CALIFICA','TBCALIFICACION',['IDCALIFICA']))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,1), Value(3,'LAPTOP LENOVO'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,2), Value(3,'BATERIA PARA LAPTOP LENOVO T420'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,3), Value(3,'TECLADO INALAMBRICO'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,4), Value(3,'MOUSE INALAMBRICO'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,5), Value(3,'WIFI USB'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,6), Value(3,'LAPTOP HP'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,7), Value(3,'TECLADO FLEXIBLE USB'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,8), Value(3,'LAPTOP SAMSUNG'), Value(3,'2021-01-02'), Value(1,1)]))
	t30='TBPRODUCTO'
	t31=1

	print(VALIDAREGISTROS(t30, t31))

	t32='TBPRODUCTO'
	t33=2

	print(VALIDAREGISTROS(t32, t33))

	t34='TBPRODUCTOUP'
	t35=2

	print(VALIDAREGISTROS(t34, t35))

	t36='TBPRODUCTOUP'
	t37=1

	print(VALIDAREGISTROS(t36, t37))

	t38='TBBODEGA'
	t39=3

	print(VALIDAREGISTROS(t38, t39))

	t40='TBBODEGA'
	t41=1

	print(VALIDAREGISTROS(t40, t41))

	t42='TBPRODUCTO'
	t43=8

	print(VALIDAREGISTROS(t42, t43))

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,1), Value(3,'CREATE TABLE AND INSERT'), Value(1,0)]))
	executeSentence(Update,Update('TBPRODUCTO',[['ESTADO', Value(1,2)]],Relational(Value(4,'ESTADO'),Value(1,1),'=')))
	t44='TBPRODUCTOUP'
	t45=8

	print(VALIDAREGISTROS(t44, t45))

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,2), Value(3,'UPDATE'), Value(1,1)]))

	print(CALCULOS())

	executeSentence(CreateTable,CreateTable('TBBODEGA',[ColumnId('IDBODEGA',['INTEGER'],{'null': False, 'primary': True}), ColumnId('BODEGA',['VARCHAR', 100],{'null': False}), ColumnId('ESTADO',['INTEGER'],None)],None))

	print(SP_VALIDAINSERT())

	t67='TBBODEGA'
	t68=5

	print(VALIDAREGISTROS(t67, t68))

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,4), Value(3,'VALIDA STORE PROCEDURE'), Value(1,1)]))

	print(SP_VALIDAUPDATE())

	executeSentence(Delete,Delete('TBBODEGA',Relational(Value(4,'IDBODEGA'),Value(1,4),'=')))
	t69='TBBODEGA'
	t70=4

	print(VALIDAREGISTROS(t69, t70))

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,5), Value(3,'VALIDA DELETE'), Value(1,1)]))
	executeSentence(Select,Select([Value(6,'*')],False,[Value(4,'TBBODEGA')],None))

@with_goto
def MYFUNCION(TEXTO: str) ->str:
	t0=TEXTO
	return t0

@with_goto
def VALIDAREGISTROS(TABLA: str, CANTIDAD: int) ->int:
	RESULTADO:int
	RETORNA:int
	t2=TABLA
	t3='TBPRODUCTO'
	t4=t2 == t3
	if t4:
		goto .lbl0
	else:
		goto. lbl4
	label .lbl0
	t5=1
	RESULTADO=t5
	t6=CANTIDAD
	t7=RESULTADO
	t8=t6 == t7
	if t8:
		goto .lbl1
	else:
		goto. lbl2
	label .lbl1
	t9=1
	RETORNA=t9
	goto .lbl3
	label .lbl2
	t10=0
	RETORNA=t10
	label .lbl3
	label .lbl4
	t11=TABLA
	t12='TBPRODUCTOUP'
	t13=t11 == t12
	if t13:
		goto .lbl5
	else:
		goto. lbl9
	label .lbl5
	t14=2
	RESULTADO=t14
	t15=CANTIDAD
	t16=RESULTADO
	t17=t15 == t16
	if t17:
		goto .lbl6
	else:
		goto. lbl7
	label .lbl6
	t18=1
	RETORNA=t18
	goto .lbl8
	label .lbl7
	t19=0
	RETORNA=t19
	label .lbl8
	label .lbl9
	t20=TABLA
	t21='TBBODEGA'
	t22=t20 == t21
	if t22:
		goto .lbl10
	else:
		goto. lbl14
	label .lbl10
	t23=3
	RESULTADO=t23
	t24=CANTIDAD
	t25=RESULTADO
	t26=t24 == t25
	if t26:
		goto .lbl11
	else:
		goto. lbl12
	label .lbl11
	t27=1
	RETORNA=t27
	goto .lbl13
	label .lbl12
	t28=0
	RETORNA=t28
	label .lbl13
	label .lbl14
	t29=RETORNA
	return t29

@with_goto
def CALCULOS():
	HORA:int
	SENO:float
	VALOR:int
	ABSOLUTO:float
	t46=20
	HORA=t46
	t47=1
	SENO=t47
	t48=SENO
	t49=HORA
	t50=t48*t49
	VALOR=t50
	t51=VALOR
	t52=3
	t53=t51+t52
	VALOR=t53
	t54=1
	ABSOLUTO=t54
	t55=ABSOLUTO
	t56=225
	t57=t55*t56
	ABSOLUTO=t57
	t58=VALOR
	t59=ABSOLUTO
	t60=t58+t59
	VALOR=t60
	t61=VALOR
	t62=1
	t63=t61 > t62
	if t63:
		goto .lbl15
	else:
		goto. lbl16
	label .lbl15
	t64=20
	VALOR=t64
	goto .lbl17
	label .lbl16
	t65=10
	VALOR=t65
	label .lbl17
	t66=VALOR
	return t66

@with_goto
def SP_VALIDAINSERT():
	executeSentence(InsertAll,InsertAll('TBBODEGA',[Value(1,1), Value(3,'BODEGA CENTRAL'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA'],[Value(1,2), Value(3,'BODEGA ZONA 12')]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,3), Value(3,'BODEGA ZONA 11'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,4), Value(3,'BODEGA ZONA 1'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,5), Value(3,'BODEGA ZONA 10'), Value(1,1)]))

@with_goto
def SP_VALIDAUPDATE():
	executeSentence(Update,Update('TBBODEGA',[['BODEGA', Value(3,'BODEGA ZONA 9')]],Relational(Value(4,'IDBODEGA'),Value(1,4),'=')))

@with_goto
def CALCULOS():
	HORA:int
	SENO:float
	VALOR:int
	ABSOLUTO:float
	t44=20
	HORA=t44
	t45=1
	SENO=t45
	t46=SENO
	t47=HORA
	t48=t46*t47
	VALOR=t48
	t49=VALOR
	t50=3
	t51=t49+t50
	VALOR=t51
	t52=1
	ABSOLUTO=t52
	t53=ABSOLUTO
	t54=225
	t55=t53*t54
	ABSOLUTO=t55
	t56=VALOR
	t57=ABSOLUTO
	t58=t56+t57
	VALOR=t58
	t59=VALOR
	t60=1
	t61=t59 > t60
	if t61:
		goto .lbl15
	else:
		goto. lbl16
	label .lbl15
	t62=20
	VALOR=t62
	goto .lbl17
	label .lbl16
	t63=10
	VALOR=t63
	label .lbl17
	t64=VALOR
	return t64

up()