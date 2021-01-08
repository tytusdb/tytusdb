from goto import with_goto
from interpreter import execution
from c3d.stack import Stack

stack = Stack()
RETURN=[None]

@with_goto
def fvalidaregistros(tabla,cantidad):
	nomnbre =  'test'
	absolute =  52
	t0 =  -5
	numero =  t0
	indice =  5
	t1 = indice * 5
	t2 = numero + t1
	final =  t2
	t3 = 9 > 0
	t4 = 9 + 5
	t5 = t4 == 14
	t6 = t3 and t5
	if t6: goto .L1
	goto .L2
	label .L1 #etiqueta true
	RETURN[0] = final
	goto .L0
	goto .L3 #EXIT

	label .L2 #etiqueta false
	t7 = 97 == 90
	if t7: goto .L4
	goto .L5
	label .L4 #etiqueta true
	RETURN[0] = 0
	goto .L0
	goto .L3 #EXIT

	label .L5 #etiqueta false
	t8 = 99 == 90
	if t8: goto .L6
	goto .L7
	label .L6 #etiqueta true
	RETURN[0] = 80
	goto .L0
	goto .L3 #EXIT

	label .L7 #etiqueta false
	t9 = 100 == 100
	if t9: goto .L8
	goto .L9
	label .L8 #etiqueta true
	RETURN[0] = 100
	goto .L0
	goto .L3 #EXIT

	label .L9 #etiqueta false
	RETURN[0] = 60
	goto .L0

	label .L3 # SALE DEL IF
	label .L0



@with_goto
def principal():
	pass


def funcionIntermedia():
	execution(stack.pop())
principal()
fvalidaregistros('test',50)

print(RETURN[0])