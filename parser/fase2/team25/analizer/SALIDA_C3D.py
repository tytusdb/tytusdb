from goto import with_goto
from interpreter import execution
from c3d.stack import Stack

stack = Stack()
RETURN=[None]



@with_goto
def principal():
	t0 = 9 > 0
	t1 = 9 + 1
	t2 = t1 == 14
	t3 = t0 and t2
	if t3: goto .L0
	goto .L1
	label .L0 #etiqueta true
	RETURN[0] = 7
	goto .L2 #EXIT

	label .L1 #etiqueta false
	t4 = 97 == 90
	if t4: goto .L3
	goto .L4
	label .L3 #etiqueta true
	RETURN[0] = 0
	goto .L2 #EXIT

	label .L4 #etiqueta false
	t5 = 99 == 90
	if t5: goto .L5
	goto .L6
	label .L5 #etiqueta true
	RETURN[0] = 80
	goto .L2 #EXIT

	label .L6 #etiqueta false
	t6 = 100 == 110
	if t6: goto .L7
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