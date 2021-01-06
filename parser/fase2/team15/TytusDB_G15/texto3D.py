from goto import with_goto
from test3DFase1 import * 

inter = Intermedio()

@with_goto  # Decorador necesario.
def f():
	label. main
	Sra = -1
	Ss0 = [0] * 10000
	
	Sra = Sra + 1	
	Ss0[Sra] = 1	
	goto. createDB	
	label. retorno1	
	goto. end	
	
	label. createDB	
	St0 = 10	
	St1 = 30	
	St2 = St0 < 20	
	if  St2 : goto. L0	
	goto. L1	
	label. L0	
	print('ES MENOR A 20  ')
	print(inter.procesar_database1())	
	print(inter.procesar_database2())
	print(inter.Reportes())	
	print('ES MENOR A 20  ')	
	goto. L2	
	label. L1	
	print('ES MAYOR A 20  ')	
	label. L2	
	goto. retorno	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1	
	if Ssp == 1: goto. retorno1

	label .end
	return

f()
