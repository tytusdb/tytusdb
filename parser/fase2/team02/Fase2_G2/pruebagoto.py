from goto import with_goto
import sys
@with_goto  # Decorador necesario.
def main():
	#Inicio print
	t0 = 1
	if(t0 == 1):
		goto .l0
	goto .l1
	#True
	label .l0
	print(True)
	goto .l2
	#False
	label .l1
	print(False)
	label .l2
	#Fin print
	#Inicio print
	t1 = 0
	if(t1 == 1):
		goto .l3
	goto .l4
	#True
	label .l3
	print(True)
	goto .l5
	#False
	label .l4
	print(False)
	label .l5
	#Fin print
if __name__ == "__main__":
	main()
