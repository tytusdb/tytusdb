from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
from goto import with_goto

@with_goto
def up():
	print(1)
	print(SP_VALIDAUPDATE())


@with_goto
def SP_VALIDAUPDATE():
	executeSentence(Update,Update('TBBODEGA',[['BODEGA', Value(3,'BODEGA ZONA 9')]],Relational(Value(4,'IDBODEGA'),Value(1,4),'=')))

up()