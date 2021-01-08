from FuncionInter import * 
from goto import with_goto

inter = Intermedio()

@with_goto  # Decorador necesario.
def main():
	pos = -1
	arr = [0] * 10000

	inter.procesar_funcionCreateDatabase0()
	inter.procesar_funcionUseDatabase1()	
	tp0 = 'INICIO CALIFICACION FASE 2'	
	pos = pos + 1	
	arr[pos] = 1	
	goto. myFuncion	
	label. retorno1
	inter.procesar_funcionCreateTable2()
	inter.procesar_funcionCreateIndex3()
	inter.procesar_funcionCreateTable4()
	inter.procesar_funcionCreateIndex5()
	inter.procesar_funcionInsert6()
	inter.procesar_funcionInsert7()
	inter.procesar_funcionInsert8()
	inter.procesar_funcionInsert9()
	inter.procesar_funcionInsert10()	
	tp1 = 'tbProducto'	
	tp2 = 2	
	pos = pos + 1	
	arr[pos] = 2	
	goto. ValidaRegistros	
	label. retorno2
	inter.procesar_funcionInsert11()
	inter.procesar_funcionSelect12()
	inter.Reportes()	
	goto. end	
	
	label. myFuncion	
	print(tp0 )	
	goto. retorno	
	
	label. ValidaRegistros	
	t0 = 0	
	t1 = 0	
	t2 = tp1 == 'tbProducto'	
	if  t2 : goto. L0	
	goto. L1	
	label. L0	
	t0 = 2	
	t3 = tp2 == t0	
	if  t3 : goto. L3	
	goto. L4	
	label. L3	
	t1 = 1	
	goto. L5	
	label. L4	
	t1 = 0	
	label. L5	
	label. L1	
	print(t1 )	
	goto. retorno	
	
	label. retorno	
	posR = arr[pos]	
	pos = pos - 1	
	if posR == 1: goto. retorno1	
	if posR == 2: goto. retorno2

	label .end
	return

main()
