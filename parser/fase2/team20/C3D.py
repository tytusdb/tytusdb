from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
from execution.executeInstruction import createFunction, deleteFunction
from goto import with_goto
import math

@with_goto
def up():
	print(1)

	executeSentence(CreateDatabase,CreateDatabase('PRUEBAINCERSION',False,True,[None, None]))
	executeSentence(Use,Use('PRUEBAINCERSION'))
	executeSentence(CreateTable,CreateTable('TBPRODUCTO',[ColumnId('IDPRODUCTO',['INTEGER'],{'null': False, 'primary': True}), ColumnId('PRODUCTO',['VARCHAR', 150],{'null': False}), ColumnId('FECHACREACION',['DATE'],{'null': False}), ColumnId('ESTADO',['INTEGER'],None)],None))
	createFunction('SP_INSERTAPRODUCTO','''
@with_goto
def SP_INSERTAPRODUCTO(LLAVE: int, PRODUCTO: str, FECHA):
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(4,LLAVE), Value(4,PRODUCTO), Value(4,FECHA), Value(1,1)]))
''',False)


	print(SP_INSERTAPRODUCTO(9, 'BOCINA INALAMBRICA', '2021-01-06'))


	print(SP_INSERTAPRODUCTO(10, 'AUDIFONOS CON MICROFONO USB', '2021-01-06'))


	print(SP_INSERTAPRODUCTO(11, 'BOCINA INALAMBRICA', '2021-01-06'))


	print(SP_INSERTAPRODUCTO(12, 'MONITOR DE 17"', '2021-01-06'))


@with_goto
def SP_INSERTAPRODUCTO(LLAVE: int, PRODUCTO: str, FECHA):
	executeSentence(InsertAll,InsertAll('TBPRODUCTO',[Value(4,LLAVE), Value(4,PRODUCTO), Value(4,FECHA), Value(1,1)]))

up()