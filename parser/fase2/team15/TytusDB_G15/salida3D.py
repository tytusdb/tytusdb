from FuncionInter import * 
from goto import with_goto

inter = Intermedio()

@with_goto  # Decorador necesario.
def main():
	Sra = -1
	Ss0 = [0] * 10000

	print(inter.procesar_funcion0())
	print(inter.procesar_funcion1())	
	ta0 = 'INICIO CALIFICACION FASE 2'	
	Sra = Sra + 1	
	Ss0[Sra] = 1	
	goto. myFuncion	
	label. retorno1
	print(inter.procesar_funcion2())
	print(inter.procesar_funcion3())
	print(inter.procesar_funcion4())
	print(inter.procesar_funcion5())
	print(inter.procesar_funcion6())
	print(inter.procesar_funcion7())
	print(inter.procesar_funcion8())
	print(inter.procesar_funcion9())
	print(inter.procesar_funcion10())
	print(inter.procesar_funcion11())
	print(inter.procesar_funcion12())
	print(inter.procesar_funcion13())	
	ta1 = 'tbProducto'	
	ta2 = 8	
	Sra = Sra + 1	
	Ss0[Sra] = 2	
	goto. ValidaRegistros	
	label. retorno2
	print(inter.procesar_funcion14())
	print(inter.procesar_funcion15())	
	ta1 = 'tbProductoUp'	
	ta2 = 8	
	Sra = Sra + 1	
	Ss0[Sra] = 3	
	goto. ValidaRegistros	
	label. retorno3
	print(inter.procesar_funcion16())	
	Sra = Sra + 1	
	Ss0[Sra] = 4	
	goto. CALCULOS	
	label. retorno4
	print(inter.procesar_funcion17())
	print(inter.procesar_funcion18())
	print(inter.procesar_funcion19())	
	Sra = Sra + 1	
	Ss0[Sra] = 5	
	goto. sp_validainsert	
	label. retorno5	
	ta1 = 'tbbodega'	
	ta2 = 5	
	Sra = Sra + 1	
	Ss0[Sra] = 6	
	goto. ValidaRegistros	
	label. retorno6
	print(inter.procesar_funcion20())	
	Sra = Sra + 1	
	Ss0[Sra] = 7	
	goto. sp_validaupdate	
	label. retorno7	
	ta1 = 'tbbodega'	
	ta2 = 4	
	Sra = Sra + 1	
	Ss0[Sra] = 8	
	goto. ValidaRegistros	
	label. retorno8
	print(inter.procesar_funcion21())
	print(inter.procesar_funcion22())
	print(inter.Reportes())	
	goto. end	
	
	label. myFuncion	
	print(ta0 )	
	goto. retorno	
	
	label. ValidaRegistros	
	t0 = 0	
	t1 = 0	
	t2 = ta1 == 'tbProducto'	
	if  t2 : goto. L0	
	goto. L1	
	label. L0	
	t0 = 2	
	t3 = ta2 == t0	
	if  t3 : goto. L3	
	goto. L4	
	label. L3	
	t1 = 1	
	goto. L5	
	label. L4	
	t1 = 0	
	label. L5	
	label. L1	
	t4 = ta1 == 'tbProductoUp'	
	if  t4 : goto. L6	
	goto. L7	
	label. L6	
	t0 = 2	
	t5 = ta2 == t0	
	if  t5 : goto. L9	
	goto. L10	
	label. L9	
	t1 = 1	
	goto. L11	
	label. L10	
	t1 = 0	
	label. L11	
	label. L7	
	t6 = ta1 == 'tbbodega'	
	if  t6 : goto. L12	
	goto. L13	
	label. L12	
	t0 = 2	
	t7 = ta2 == t0	
	if  t7 : goto. L15	
	goto. L16	
	label. L15	
	t1 = 1	
	goto. L17	
	label. L16	
	t1 = 0	
	label. L17	
	label. L13	
	print(t1 )	
	goto. retorno	
	
	label. CALCULOS	
	t8 = 0	
	t9 = 0	
	t10 = 0	
	t11 = 0	
	t8 = 2	
	t9 = 3	
	t10 = 4	
	t12 = t10 + 2	
	t10 = t12	
	t11 = 3	
	t11 = 4	
	t13 = t10 + t11	
	t14 = t13 / 2	
	t10 = t14	
	t15 = t10 > 1	
	if  t15 : goto. L18	
	goto. L19	
	label. L18	
	t10 = 20	
	goto. L20	
	label. L19	
	t10 = 10	
	label. L20	
	print(t10 )	
	goto. retorno	
	
	label. sp_validainsert
	print(inter.procesar_funcion23())
	print(inter.procesar_funcion24())
	print(inter.procesar_funcion25())
	print(inter.procesar_funcion26())
	print(inter.procesar_funcion27())	
	print('INSERT  ')	
	goto. retorno	
	
	label. sp_validaupdate	
	print('UPDATE  ')
	print(inter.procesar_funcion28())	
	goto. retorno	
	
	label. retorno	
	Ssp = Ss0[Sra]	
	Sra = Sra - 1	
	if Ssp == 1: goto. retorno1	
	if Ssp == 2: goto. retorno2	
	if Ssp == 3: goto. retorno3	
	if Ssp == 4: goto. retorno4	
	if Ssp == 5: goto. retorno5	
	if Ssp == 6: goto. retorno6	
	if Ssp == 7: goto. retorno7	
	if Ssp == 8: goto. retorno8

	label .end
	return

main()
