import sys, os.path
import sys, os.path
gramaticaDir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(gramaticaDir)
sys.path.append(gramaticaDir)
# Seccion de Imports

from goto import with_goto
from gramatica import run_method

display = {}
listaParams = []

@with_goto
def holamundo_5():
	global p
	t1 = 'Select * from usuarios;'
	display[p] = t1
	p = p + 1
	#execute()
	if 5 > 6 :
		goto .L1
	goto .L2
	label .L1
	t2 = 1
	goto .L3
	label .L2
	t2 = 0
	label .L3
	if t2 == 1 :
		goto .L4
	goto .L5
	label .L4
	t3 = 'Select * from usuarios;'
	display[p] = t3
	p = p + 1
	#execute()
	goto .L6
	label .L5
	t4 = 'Select * from usuarios;'
	display[p] = t4
	p = p + 1
	#execute()
	label .L6

p = 0
holamundo_5()
print(display)
