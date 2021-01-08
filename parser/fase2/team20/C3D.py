from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
from execution.executeInstruction import createFunction, deleteFunction
from goto import with_goto
import math

@with_goto
def up():
	print(1)

	executeSentence(CreateDatabase,CreateDatabase('DBFASE2',False,False,[None, None]))
	executeSentence(Use,Use('DBFASE2'))
	executeSentence(CreateTable,CreateTable('TBPRODUCTO',[ColumnId('IDPRODUCTO',['INTEGER'],{'null': False, 'primary': True}), ColumnId('PRODUCTO',['VARCHAR', 150],{'null': False}), ColumnId('FECHACREACION',['DATE'],{'null': False}), ColumnId('ESTADO',['INTEGER'],None)],None))
	executeSentence(CreateIndex,CreateIndex('IDX_PRODUCTO','TBPRODUCTO',[['IDPRODUCTO']]))
	executeSentence(CreateTable,CreateTable('TBBODEGA',[ColumnId('IDBODEGA',['INTEGER'],{'null': False, 'primary': True}), ColumnId('BODEGA',['VARCHAR', 100],{'null': False}), ColumnId('ESTADO',['INTEGER'],None)],None))
	executeSentence(CreateIndex,CreateIndex('IDX_VDGA','TBBODEGA',[['BODEGA']]))
	executeSentence(CreateIndex,CreateIndex('IDX_BODEGA','TBBODEGA',[['BODEGA'], ['ESTADO']]))
	executeSentence(DropIndex,DropIndex('IDX_VDGA',False))
	executeSentence(AlterIndex,AlterIndex('IDX_BODEGA','ESTADO','IDBODEGA'))

up()


up()