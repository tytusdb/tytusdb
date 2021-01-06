from goto import with_goto
from interpreter import execution
from c3d.stack import Stack

stack = Stack()
RETURN=[None]



@with_goto
def principal():
	nomnbre =  'asdads'
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
	if t6: goto .L0
	goto .L1
	label .L0 #etiqueta true
	RETURN[0] = final
	goto .L2 #EXIT

	label .L1 #etiqueta false
	t7 = 97 == 90
	if t7: goto .L3
	goto .L4
	label .L3 #etiqueta true
	RETURN[0] = 0
	goto .L2 #EXIT

	label .L4 #etiqueta false
	t8 = 99 == 90
	if t8: goto .L5
	goto .L6
	label .L5 #etiqueta true
	RETURN[0] = 80
	goto .L2 #EXIT

	label .L6 #etiqueta false
	t9 = 100 == 100
	if t9: goto .L7
	goto .L8
	label .L7 #etiqueta true
	RETURN[0] = 100
	goto .L2 #EXIT

	label .L8 #etiqueta false
	RETURN[0] = 60

	label .L2 # SALE DEL IF



def funcionIntermedia():
	execution(stack.pop())
principal()

print(RETURN[0])