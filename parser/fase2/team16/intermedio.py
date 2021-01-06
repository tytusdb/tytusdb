from goto import with_goto
import FuncionesIntermedias as F3D
heap = F3D.heap
stack = []

@with_goto 
def main(): 
	global heap
	global stack

	t0 = """ ALTER INDEX idx_producto ALTER COLUMN 0 SET STATISTICS integer ; """
	heap.append(t0)
	F3D.ejecutarSQL()


	goto .END

	label .R
	u = stack.pop()

	label .END
