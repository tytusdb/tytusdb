from goto import with_goto
from interpreter import execution
from c3d.stack import  Stack

stack = Stack()


@with_goto
def principal():
	t0 = "use MYDB;"
	stack.push(t0)
	funcionIntermedia()
	t1 = "insert into tabla1 values (1,2,3);"
	t2 = "insert into tabla1 values (1,2,3);"
	t3 = "insert into tabla1 values (1,2,3);"
	t4 = "select * from tabla1;"
	t5 = "select * from tabla1 where columna > 1500;"
	t6 = 9 * 8
	return t6
	t7 = "CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);"
	stack.push(t7)
	funcionIntermedia()
	t8 = "select md5('cadena') from tab5 where col <> 10;"
	stack.push(t8)
	funcionIntermedia()



def funcionIntermedia():
	execution(stack.pop())
principal()