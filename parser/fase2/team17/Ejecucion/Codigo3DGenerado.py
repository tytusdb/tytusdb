
from Fase1.Sql import Sql
from goto import with_goto
heap = ''
def inter() -> str:
	global heap
	sql: Sql = Sql()
	result = str(sql.query(heap))
	return result

@with_goto
def principal():
	t0 = str(0)
	t1 = 'hola ' + t0 + ' como estas'
	print(str(t1))
	t2 = 5
	t3 = 6
	if t2 > t3:
		goto .L0
	else:
		goto .L1
	label .L0
	t4 = 'hola'
	print(str(t4))
	goto .L2
	label .L1
	t5 = 'adios'
	print(str(t5))
	label .L2


if __name__ == '__main__':
	principal()