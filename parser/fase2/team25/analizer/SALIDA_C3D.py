from goto import with_goto
from interpreter import execution
from c3d.stack import Stack

stack = Stack()
RETURN=[None]

@with_goto
def myfuncion(texto):
	RETURN[0] = texto
	goto .L0
	label .L0

@with_goto
def validaregistros(tabla,cantidad):
	resultado =  0
	retorna =  0
	t0 = tabla == 'tbProducto'
	if t0: goto .L2
	goto .L3
	label .L2 #etiqueta true
	resultado =  5
	t1 = cantidad == resultado
	if t1: goto .L4
	goto .L5
	label .L4 #etiqueta true
	retorna =  1
	goto .L6 #EXIT

	label .L5 #etiqueta false
	retorna =  0

	label .L6 # SALE DEL IF
	label .L3 #etiqueta false
	t2 = tabla == 'tbProductoUp'
	if t2: goto .L7
	goto .L8
	label .L7 #etiqueta true
	resultado =  10
	t3 = cantidad == resultado
	if t3: goto .L9
	goto .L10
	label .L9 #etiqueta true
	retorna =  1
	goto .L11 #EXIT

	label .L10 #etiqueta false
	retorna =  0

	label .L11 # SALE DEL IF
	label .L8 #etiqueta false
	t4 = tabla == 'tbbodega'
	if t4: goto .L12
	goto .L13
	label .L12 #etiqueta true
	resultado =  15
	t5 = cantidad == resultado
	if t5: goto .L14
	goto .L15
	label .L14 #etiqueta true
	retorna =  1
	goto .L16 #EXIT

	label .L15 #etiqueta false
	retorna =  0

	label .L16 # SALE DEL IF
	label .L13 #etiqueta false
	RETURN[0] = retorna
	goto .L1
	label .L1

@with_goto
def hola(tabla,cantidad):
	resultado =  0
	retorna =  0
	RETURN[0] = 50
	goto .L17
	label .L17



@with_goto
def principal():



def funcionIntermedia():
	return execution(stack.pop())
principal()