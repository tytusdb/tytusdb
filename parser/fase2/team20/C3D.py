from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
from execution.executeInstruction import createFunction, deleteFunction
from goto import with_goto
import math

@with_goto
def up():
	print(1)

	executeSentence(Select,Select([<execution.AST.expression.CountFunction object at 0x000001C7CB01AEE0>],False,[Value(4,'TBEMPLEADOPUESTO')],None))

up()