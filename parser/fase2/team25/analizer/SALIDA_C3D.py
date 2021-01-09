from goto import with_goto
from interpreter import execution
from c3d.stack import Stack

stack = Stack()
RETURN=[None]

@with_goto
def calculos():
	hora =  0
	seno =  0.0
	valor =  0
	absoluto =  0.0
	valor =  5
	t0 = valor > 1
	if t0: goto .L1
	goto .L2
	label .L1 #etiqueta true
	valor =  20
	goto .L3 #EXIT

	label .L2 #etiqueta false
	valor =  10

	label .L3 # SALE DEL IF
	RETURN[0] = valor
	goto .L0
	label .L0



@with_goto
def principal():



def funcionIntermedia():
	return execution(stack.pop())
principal()