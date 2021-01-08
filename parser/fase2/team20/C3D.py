from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
from execution.executeInstruction import createFunction, deleteFunction
from console import print_error, print_success, print_warning, print_text
from goto import with_goto
import math

@with_goto
def up():
	print(1)

	executeSentence(CreateDatabase,CreateDatabase('DBFASE2',False,False,[None, None]))
	executeSentence(Use,Use('DBFASE2'))
	createFunction('MYFUNCION','''
@with_goto
def MYFUNCION(TEXTO: str) ->str:
	return TEXTO
''',False)


	print_text('MYFUNCION',MYFUNCION('INICIO CALIFICACION FASE 2'),2)

	print(MYFUNCION('INICIO CALIFICACION FASE 2'))

	executeSentence(CreateTable,CreateTable('TBPRODUCTO',[ColumnId('IDPRODUCTO',['INTEGER'],{'null': False, 'primary': True}), ColumnId('PRODUCTO',['VARCHAR', 150],{'null': False}), ColumnId('FECHACREACION',['DATE'],{'null': False}), ColumnId('ESTADO',['INTEGER'],None)],None))
	executeSentence(CreateTable,CreateTable('TBPRODUCTOS',[ColumnId('IDPRODUCTO',['INTEGER'],{'null': False, 'primary': True}), ColumnId('PRODUCTO',['VARCHAR', 150],{'null': False}), ColumnId('FECHACREACION',['DATE'],{'null': False}), ColumnId('ESTADO',['INTEGER'],None)],None))
	executeSentence(CreateIndex,CreateIndex('IDX_PRODUCTO','TBPRODUCTO',[['IDPRODUCTO']]))
	executeSentence(CreateTable,CreateTable('TBCALIFICACION',[ColumnId('IDCALIFICA',['INTEGER'],{'null': False, 'primary': True}), ColumnId('ITEM',['VARCHAR', 100],{'null': False}), ColumnId('PUNTEO',['INTEGER'],{'null': False})],None))
	executeSentence(CreateIndex,CreateIndex('IDX_CALIFICA','TBCALIFICACION',[['IDCALIFICA']]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,1), Value(3,'LAPTOP LENOVO'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,2), Value(3,'BATERIA PARA LAPTOP LENOVO T420'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,3), Value(3,'TECLADO INALAMBRICO'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,4), Value(3,'MOUSE INALAMBRICO'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,5), Value(3,'WIFI USB'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,6), Value(3,'LAPTOP HP'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,7), Value(3,'TECLADO FLEXIBLE USB'), MathFunction('NOW',0), Value(1,1)]))
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(1,8), Value(3,'LAPTOP SAMSUNG'), Value(3,'2021-01-02'), Value(1,1)]))

	print_text('MYFUNCION',MYFUNCION('CREA FUNCION'),2)

	print(MYFUNCION('CREA FUNCION'))

	createFunction('VALIDAREGISTROS','''
@with_goto
def VALIDAREGISTROS(TABLA: str, CANTIDAD: int) ->int:
	RESULTADO:int
	RETORNA:int
	t0=TABLA=='TBPRODUCTO'
	if t0:
		goto .lbl0
	else:
		goto. lbl4
	label .lbl0
	RESULTADO=executeSentence(Select,Select([CountFunction('COUNT')],False,[Value(3,'TBPRODUCTO')],None))
	t1=CANTIDAD==RESULTADO
	if t1:
		goto .lbl1
	else:
		goto. lbl2
	label .lbl1
	RETORNA=1
	goto .lbl3
	label .lbl2
	RETORNA=0
	label .lbl3
	label .lbl4
	t2=TABLA=='TBPRODUCTOUP'
	if t2:
		goto .lbl5
	else:
		goto. lbl9
	label .lbl5
	RESULTADO=executeSentence(Select,Select([CountFunction('COUNT')],False,[Value(3,'TBPRODUCTOS')],None))
	t3=CANTIDAD==RESULTADO
	if t3:
		goto .lbl6
	else:
		goto. lbl7
	label .lbl6
	RETORNA=1
	goto .lbl8
	label .lbl7
	RETORNA=0
	label .lbl8
	label .lbl9
	t4=TABLA=='TBBODEGA'
	if t4:
		goto .lbl10
	else:
		goto. lbl14
	label .lbl10
	RESULTADO=executeSentence(Select,Select([CountFunction('COUNT')],False,[Value(3,'TBBODEGA')],None))
	t5=CANTIDAD==RESULTADO
	if t5:
		goto .lbl11
	else:
		goto. lbl12
	label .lbl11
	RETORNA=1
	goto .lbl13
	label .lbl12
	RETORNA=0
	label .lbl13
	label .lbl14
	return RETORNA
''',False)


	print_text('MYFUNCION',MYFUNCION('VALIDAREGISTROS(TBPRODUCTO,8)='),2)

	print(MYFUNCION('VALIDAREGISTROS(TBPRODUCTO,8)='))


	print_text('VALIDAREGISTROS',VALIDAREGISTROS('TBPRODUCTO', 8),2)

	print(VALIDAREGISTROS('TBPRODUCTO', 8))

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,1), Value(3,'CREATE TABLE AND INSERT'), Value(1,1)]))
	executeSentence(Update,Update('TBPRODUCTO',[['ESTADO', Value(1,2)]],Relational(Value(3,'ID'),Value(1,1),'>=')))

	print_text('MYFUNCION',MYFUNCION('VALIDAREGISTROS(TBPRODUCTO,8)='),2)

	print(MYFUNCION('VALIDAREGISTROS(TBPRODUCTO,8)='))


	print_text('VALIDAREGISTROS',VALIDAREGISTROS('TBPRODUCTO', 8),2)

	print(VALIDAREGISTROS('TBPRODUCTO', 8))

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,2), Value(3,'UPDATE'), Value(1,0)]))
	createFunction('CALCULOS','''
@with_goto
def CALCULOS():
	HORA:int
	SENO:float
	VALOR:int
	ABSOLUTO:float
	HORA=20
	t6=math.sin(1)
	SENO=t6
	t7=SENO*HORA
	t8=math.trunc(t7)
	VALOR=t8
	t9=VALOR+4
	VALOR=t9
	t10=-1
	t11=math.sinh(t10)
	t12=t11>0
	t13=t11<0
	t14=t12-t13
	t15=t11*t14
	ABSOLUTO=t15
	t16=1/2
	t17=1**t16
	t18=ABSOLUTO*t17
	ABSOLUTO=t18
	t19=VALOR+ABSOLUTO
	t20=math.degrees(math.acos(0.5))
	t21=t19/t20
	VALOR=t21
	t22=VALOR>1
	if t22:
		goto .lbl15
	else:
		goto. lbl16
	label .lbl15
	VALOR=20
	goto .lbl17
	label .lbl16
	VALOR=10
	label .lbl17
	return VALOR
''',False)


	print_text('MYFUNCION',MYFUNCION('CALCULOS()='),2)

	print(MYFUNCION('CALCULOS()='))


	print_text('CALCULOS',CALCULOS(),2)

	print(CALCULOS())

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,3), Value(3,' VALIDA FUNCIONES'), Value(1,10)]))
	executeSentence(CreateTable,CreateTable('TBBODEGA',[ColumnId('IDBODEGA',['INTEGER'],{'null': False, 'primary': True}), ColumnId('BODEGA',['VARCHAR', 100],{'null': False}), ColumnId('ESTADO',['INTEGER'],None)],None))
	executeSentence(CreateIndex,CreateIndex('IDX_NOMBRE','TBBODEGA',[['BODEGA']]))
	createFunction('SP_VALIDAINSERT','''
@with_goto
def SP_VALIDAINSERT():
	executeSentence(InsertAll,InsertAll('TBBODEGA',[Value(1,1), Value(3,'BODEGA CENTRAL'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA'],[Value(1,2), Value(3,'BODEGA ZONA 12')]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,3), Value(3,'BODEGA ZONA 11'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,4), Value(3,'BODEGA ZONA 1'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,5), Value(3,'BODEGA ZONA 10'), Value(1,1)]))
''',False)


	print_text('SP_VALIDAINSERT',SP_VALIDAINSERT(),2)

	print(SP_VALIDAINSERT())


	print_text('MYFUNCION',MYFUNCION('VALIDAREGISTROS(TBBODEGA,5)='),2)

	print(MYFUNCION('VALIDAREGISTROS(TBBODEGA,5)='))


	print_text('VALIDAREGISTROS',VALIDAREGISTROS('TBBODEGA', 5),2)

	print(VALIDAREGISTROS('TBBODEGA', 5))

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,4), Value(3,'VALIDA STORE PROCEDURE'), Value(1,1)]))
	executeSentence(DropIndex,DropIndex('IDX_BODEGA',False))
	createFunction('SP_VALIDAUPDATE','''
@with_goto
def SP_VALIDAUPDATE():
	executeSentence(Update,Update('TBBODEGA',[['BODEGA', Value(3,'BODEGA ZONA 9')]],Relational(Value(3,'IDBODEGA'),Value(1,4),'=')))
''',False)


	print_text('SP_VALIDAUPDATE',SP_VALIDAUPDATE(),2)

	print(SP_VALIDAUPDATE())


	print_text('MYFUNCION',MYFUNCION('VALIDAREGISTROS(TBBODEGA,4)='),2)

	print(MYFUNCION('VALIDAREGISTROS(TBBODEGA,4)='))


	print_text('VALIDAREGISTROS',VALIDAREGISTROS('TBBODEGA', 4),2)

	print(VALIDAREGISTROS('TBBODEGA', 4))

	executeSentence(InsertAll,InsertAll('TBCALIFICACION',[Value(1,5), Value(3,'VALIDA DELETE'), Value(1,0)]))
	executeSentence(Select,Select([Value(3,'*')],False,[Value(3,'TBBODEGA')],None))
	executeSentence(CreateIndex,CreateIndex('IDX_BODEGA','TBBODEGA',[['ESTADO']]))
	createFunction('SP_INSERTAPRODUCTO','''
@with_goto
def SP_INSERTAPRODUCTO(LLAVE: int, PRODUCTO: str, FECHA):
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(4,LLAVE), Value(4,PRODUCTO), Value(4,FECHA), Value(1,1)]))
''',False)


	print_text('SP_INSERTAPRODUCTO',SP_INSERTAPRODUCTO(9, 'BOCINA INALAMBRICA', '2021-01-06'),2)

	print(SP_INSERTAPRODUCTO(9, 'BOCINA INALAMBRICA', '2021-01-06'))


	print_text('SP_INSERTAPRODUCTO',SP_INSERTAPRODUCTO(10, 'AUDIFONOS CON MICROFONO USB', '2021-01-06'),2)

	print(SP_INSERTAPRODUCTO(10, 'AUDIFONOS CON MICROFONO USB', '2021-01-06'))


	print_text('SP_INSERTAPRODUCTO',SP_INSERTAPRODUCTO(11, 'BOCINA INALAMBRICA', '2021-01-06'),2)

	print(SP_INSERTAPRODUCTO(11, 'BOCINA INALAMBRICA', '2021-01-06'))


	print_text('SP_INSERTAPRODUCTO',SP_INSERTAPRODUCTO(12, 'MONITOR DE 17"', '2021-01-06'),2)

	print(SP_INSERTAPRODUCTO(12, 'MONITOR DE 17"', '2021-01-06'))

	deleteFunction('MYFUNCION')


	print_text('MYFUNCION',MYFUNCION('VALIDA DROP FUNCTION'),2)

	print(MYFUNCION('VALIDA DROP FUNCTION'))

	createFunction('FN_MENSAJE','''
@with_goto
def FN_MENSAJE(TEXTO: str) ->str:
	return TEXTO
''',False)


	print_text('FN_MENSAJE',FN_MENSAJE('CREA FUNCION NUEVA DE MENSAJE'),2)

	print(FN_MENSAJE('CREA FUNCION NUEVA DE MENSAJE'))


	print_text('SP_INSERTAPRODUCTO',SP_INSERTAPRODUCTO(13, 'BOCINA INALAMBRICA SONY', '2021-01-06'),2)

	print(SP_INSERTAPRODUCTO(13, 'BOCINA INALAMBRICA SONY', '2021-01-06'))


	print_text('SP_INSERTAPRODUCTO',SP_INSERTAPRODUCTO(14, 'AUDIFONOS CON MICROFONO USB LENOVO', '2021-01-06'),2)

	print(SP_INSERTAPRODUCTO(14, 'AUDIFONOS CON MICROFONO USB LENOVO', '2021-01-06'))


	print_text('SP_INSERTAPRODUCTO',SP_INSERTAPRODUCTO(15, 'MONITOR DE 21"', '2021-01-06'),2)

	print(SP_INSERTAPRODUCTO(15, 'MONITOR DE 21"', '2021-01-06'))


	print_text('SP_INSERTAPRODUCTO',SP_INSERTAPRODUCTO(16, 'MONITOR DE 17" LENOVO', '2021-01-06'),2)

	print(SP_INSERTAPRODUCTO(16, 'MONITOR DE 17" LENOVO', '2021-01-06'))


@with_goto
def MYFUNCION(TEXTO: str) ->str:
	return TEXTO

@with_goto
def VALIDAREGISTROS(TABLA: str, CANTIDAD: int) ->int:
	RESULTADO:int
	RETORNA:int
	t0=TABLA=='TBPRODUCTO'
	if t0:
		goto .lbl0
	else:
		goto. lbl4
	label .lbl0
	RESULTADO=executeSentence(Select,Select([CountFunction('COUNT')],False,[Value(3,'TBPRODUCTO')],None))
	t1=CANTIDAD==RESULTADO
	if t1:
		goto .lbl1
	else:
		goto. lbl2
	label .lbl1
	RETORNA=1
	goto .lbl3
	label .lbl2
	RETORNA=0
	label .lbl3
	label .lbl4
	t2=TABLA=='TBPRODUCTOUP'
	if t2:
		goto .lbl5
	else:
		goto. lbl9
	label .lbl5
	RESULTADO=executeSentence(Select,Select([CountFunction('COUNT')],False,[Value(3,'TBPRODUCTOS')],None))
	t3=CANTIDAD==RESULTADO
	if t3:
		goto .lbl6
	else:
		goto. lbl7
	label .lbl6
	RETORNA=1
	goto .lbl8
	label .lbl7
	RETORNA=0
	label .lbl8
	label .lbl9
	t4=TABLA=='TBBODEGA'
	if t4:
		goto .lbl10
	else:
		goto. lbl14
	label .lbl10
	RESULTADO=executeSentence(Select,Select([CountFunction('COUNT')],False,[Value(3,'TBBODEGA')],None))
	t5=CANTIDAD==RESULTADO
	if t5:
		goto .lbl11
	else:
		goto. lbl12
	label .lbl11
	RETORNA=1
	goto .lbl13
	label .lbl12
	RETORNA=0
	label .lbl13
	label .lbl14
	return RETORNA

@with_goto
def CALCULOS():
	HORA:int
	SENO:float
	VALOR:int
	ABSOLUTO:float
	HORA=20
	t6=math.sin(1)
	SENO=t6
	t7=SENO*HORA
	t8=math.trunc(t7)
	VALOR=t8
	t9=VALOR+4
	VALOR=t9
	t10=-1
	t11=math.sinh(t10)
	t12=t11>0
	t13=t11<0
	t14=t12-t13
	t15=t11*t14
	ABSOLUTO=t15
	t16=1/2
	t17=1**t16
	t18=ABSOLUTO*t17
	ABSOLUTO=t18
	t19=VALOR+ABSOLUTO
	t20=math.degrees(math.acos(0.5))
	t21=t19/t20
	VALOR=t21
	t22=VALOR>1
	if t22:
		goto .lbl15
	else:
		goto. lbl16
	label .lbl15
	VALOR=20
	goto .lbl17
	label .lbl16
	VALOR=10
	label .lbl17
	return VALOR

@with_goto
def SP_VALIDAINSERT():
	executeSentence(InsertAll,InsertAll('TBBODEGA',[Value(1,1), Value(3,'BODEGA CENTRAL'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA'],[Value(1,2), Value(3,'BODEGA ZONA 12')]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,3), Value(3,'BODEGA ZONA 11'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,4), Value(3,'BODEGA ZONA 1'), Value(1,1)]))
	executeSentence(Insert,Insert('TBBODEGA',['IDBODEGA', 'BODEGA', 'ESTADO'],[Value(1,5), Value(3,'BODEGA ZONA 10'), Value(1,1)]))

@with_goto
def SP_VALIDAUPDATE():
	executeSentence(Update,Update('TBBODEGA',[['BODEGA', Value(3,'BODEGA ZONA 9')]],Relational(Value(3,'IDBODEGA'),Value(1,4),'=')))

@with_goto
def SP_INSERTAPRODUCTO(LLAVE: int, PRODUCTO: str, FECHA):
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(4,LLAVE), Value(4,PRODUCTO), Value(4,FECHA), Value(1,1)]))

@with_goto
def FN_MENSAJE(TEXTO: str) ->str:
	return TEXTO

#up()