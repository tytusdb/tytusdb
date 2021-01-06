from execution.executeSentence import executeSentence 
from execution.AST.sentence import *
from execution.AST.expression import *
def up():
	executeSentence(AlterIndex,AlterIndex('IDX_ITEM','ALTER',True,False))