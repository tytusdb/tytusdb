from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from analizer import interpreter as fase1
from goto import with_goto
dbtemp = ""
stack = []


@with_goto
def myfuncion():

	texto = stack.pop()
	stack.append(texto)
	label .endLabel
	stack.append(None)
	myfuncion()
	t0 = stack.pop()
