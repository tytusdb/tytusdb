from FuncionInter import * 
from goto import with_goto

inter = Intermedio()

@with_goto  # Decorador necesario.
def main():
	Sra = -1
	Ss0 = [0] * 10000

	print(inter.procesar_funcion0())
	print(inter.procesar_funcion1())
	print(inter.procesar_funcion2())
	print(inter.procesar_funcion3())
	print(inter.procesar_funcion4())
	print(inter.procesar_funcion5())
	print(inter.procesar_funcion6())
	print(inter.procesar_funcion7())
	print(inter.procesar_funcion8())
	print(inter.procesar_funcion9())
	print(inter.Reportes())	
	goto. end	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1

	label .end
	return

main()
