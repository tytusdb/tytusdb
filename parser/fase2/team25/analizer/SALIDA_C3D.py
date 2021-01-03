from goto import with_goto
from interpreter import execution
from c3d.stack import  Stack

stack = Stack()


@with_goto
def principal():
	t0 = "use MYDB;"
	stack.push(t0)
	funcionIntermedia()
	t1 = 9 * 16
	t2 = 1 + t1
	un_id_ = t2
	t3 = "create table tab5( columna integer NOT NULL );"
	stack.push(t3)
	funcionIntermedia()
	t4 = "select md5('cadena') , funcionNueva(col) from tab5 where col <> 10;"
	stack.push(t4)
	funcionIntermedia()



def funcionIntermedia():
	execution(stack.pop())
principal()