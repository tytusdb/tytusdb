from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
def up():
	executeSentence(Select,Select([Value(6,'*')],False,[Value(4,'TBEMPLEADOPUESTO')],None))
	executeSentence(Update,Update('TBEMPLEADOPUESTO',[['IDPUESTO', Value(1,'5')]],Relational(Value(4,'IDEMPLEADO'),Value(1,'2'),'=')))
	executeSentence(Select,Select([Value(6,'*')],False,[Value(4,'TBEMPLEADOPUESTO')],None))