from goto import with_goto
from interpreter import execution
from c3d.stack import  Stack

stack = Stack()


@with_goto
def principal():
	t0 = "use test;"
	stack.push(t0)
	funcionIntermedia()
	t1 = "insert into h values (3,45,6);"
	stack.push(t1)
	funcionIntermedia()



def funcionIntermedia():
	execution(stack.pop())
principal()