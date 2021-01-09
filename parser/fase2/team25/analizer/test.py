from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from optimization.genOptimized import optimizeCode
# print(result[0].execute(None))
# print(result[1].execute(None))
# print(grammar.returnPostgreSQLErrors())

s = '''
from goto import with_goto
from interpreter import execution
from c3d.stack import Stack

stack = Stack()
RETURN=[None]
	pprueba()

@with_goto
def calculos(xd,valor):
	ejemplo =  valor
	t0 = ejemplo / valor
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
def nacimiento(xd):
	t4 = xd == '4'
	if t4: goto .L9
	goto .L10
	label .L9 #etiqueta true
	RETURN[0] = False
	goto .L8
	goto .L11 #EXIT

	label .L10 #etiqueta false
	RETURN[0] = True
	goto .L8

	label .L11 # SALE DEL IF
	RETURN[0] = valor
	goto .L8
	label .L8

@with_goto
def pprueba():
	print('Hola' , 'Z')
	RETURN[0] = hola
	goto .L12
	label .L12

@with_goto
def ptesteo(valor):
	x =  0
	print('Hola' , 'Z')
	pprueba()
	t5 = 5 * 9
	t6 = t5 / 1
	t7 = 4 + t6
	valor =  t7
	t8 = valor + 0
	valor =  t8
	t9 = valor - 0
	valor =  t9
	t10 = valor * 0
	valor =  t10
	t11 = 0 / valor
	valor =  t11
	t12 = valor / 1
	valor =  t12
	t13 = x / 1
	valor =  t13
	t14 = x * 1
	valor =  t14
	t15 = x + 0
	valor =  t15
	t16 = x - 0
	valor =  t16
	t17 = x * 2
	valor =  t17
	t18 = valor * 2
	valor =  t18
	label .L13



@with_goto
def principal():
	ptesteo(50)



def funcionIntermedia():
	return execution(stack.pop())
principal()
'''

optimizeCode(s)