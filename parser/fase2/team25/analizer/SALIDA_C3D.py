from goto import with_goto
from interpreter import execution
from c3d.stack import  Stack

stack = Stack()


@with_goto
def principal():
	t0 = "use mydb;"
	stack.push(t0)
	funcionIntermedia()
	t1 = "select * from unatabla;"
	t2 = 9 > 1
	if t2: goto .L0
	goto .L1
	label .L0 #eTrue
	t3 = 7979 + 9
	return t3
	t4 = 1 + 2
	return t4
	return 7
	t5 = "select * from tanb;"
	stack.push(t5)
	funcionIntermedia()



def funcionIntermedia():
	execution("select 9*9;")
principal()