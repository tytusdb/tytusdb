from goto import with_goto
from interpreter import execution
from c3d.stack import Stack

stack = Stack()
RETURN=[None]

@with_goto
def calculos(xd,valor):
	ejemplo =  valor
	t0 = valor / valor
	example =  t0
	test =  ''
	valor =  100
	t1 = valor < 1
	if t1: goto .L1
	goto .L2
	label .L1 #etiqueta true
	t2 =  -1
	if valor == t2: goto .L5
	RETURN[0] = True
	goto .L0
	goto .L4
	label .L5
	RETURN[0] = False
	goto .L0
	goto .L4
	label .L4
	goto .L3 #EXIT

	label .L2 #etiqueta false
	t3 = valor > 100
	if t3: goto .L6
	goto .L7
	label .L6 #etiqueta true
	RETURN[0] = False
	goto .L0
	goto .L3 #EXIT

	label .L7 #etiqueta false
	RETURN[0] = True
	goto .L0

	label .L3 # SALE DEL IF
	RETURN[0] = valor
	goto .L0
	label .L0



@with_goto
def principal():



def funcionIntermedia():
	return execution(stack.pop())
principal()