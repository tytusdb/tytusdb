from FuncionInter import * 
from goto import with_goto

inter = Intermedio()

@with_goto  # Decorador necesario.
def main():
	Sra = -1
	Ss0 = [0] * 10000
	
	Sra = Sra + 1	
	Ss0[Sra] = 1	
	goto. hola	
	label. retorno1
	print(inter.Reportes())	
	goto. end	
	
	label. hola	
	print('HOLAAA  ')	
	goto. retorno	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1	
	if Ssp == 1: goto. retorno1

	label .end
	return

main()
