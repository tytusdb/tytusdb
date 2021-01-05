from goto import with_goto

@with_goto  # Decorador necesario.
def main():
	Sra = -1
	Ss0 = [0] * 10000
	
	ta0 = 17	
	Sra = Sra + 1	
	Ss0[Sra] = 1	
	goto. suma	
	label. retorno1	
	goto. end	
	
	label. suma	
	t0 = 10	
	t1 = ta0 < 20	
	if  t1 : goto. L0	
	goto. L1	
	label. L0	
	print(ta0 )	
	t2 = ta0 + 1	
	ta0 = t2	
	ta1 = ta0	
	Sra = Sra + 1	
	Ss0[Sra] = 2	
	goto. suma1	
	label. retorno2	
	goto. L2	
	label. L1	
	print('ES MAYOR A 20  ')	
	label. L2	
	goto. retorno	
	
	label. suma1	
	t3 = 10	
	t4 = ta1 < 20	
	if  t4 : goto. L3	
	goto. L4	
	label. L3	
	print(ta1 )	
	t5 = ta1 + 1	
	ta1 = t5	
	ta1 = ta1	
	Sra = Sra + 1	
	Ss0[Sra] = 3	
	goto. suma1	
	label. retorno3	
	goto. L5	
	label. L4	
	print('ES MAYOR A 20  ')	
	label. L5	
	goto. retorno	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1	
	if Ssp == 1: goto. retorno1	
	if Ssp == 2: goto. retorno2	
	if Ssp == 3: goto. retorno3

	label .end
	return

main()
