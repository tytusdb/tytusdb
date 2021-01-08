# -*- coding: latin1 -*-
import  math
import random
import hashlib
import base64
import time
from goto import with_goto
from  tytus.parser.fase2.team21.Analisis_Ascendente.ascendente import T,T3,procesar_instrucciones
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
stack =[]
@with_goto  # Decorador necesario.
def main():
	dropAll()

	t0 = " CREATE UNIQUE INDEX test1_id_index ON test1  ( id );"
	t1 = T(t0)
	T1 = T3(t1)
	stack.append(T1)

	t2 = " CREATE INDEX name ON tabla  ( columna );"
	t3 = T(t2)
	T1 = T3(t3)
	stack.append(T1)

	t4 = " CREATE UNIQUE INDEX test2_mm_idx ON test2  ( major, minor );"
	t5 = T(t4)
	T1 = T3(t5)
	stack.append(T1)

	t6 = " CREATE INDEX test2_info_nulls_low ON test2  ( info NULLS FIRST );"
	t7 = T(t6)
	T1 = T3(t7)
	stack.append(T1)

	t8 = " CREATE INDEX test3_desc_index ON test3  ( id NULLS LAST );"
	t9 = T(t8)
	T1 = T3(t9)
	stack.append(T1)

	t10 = " CREATE UNIQUE INDEX name ON tabla  ( data, data2 );"
	t11 = T(t10)
	T1 = T3(t11)
	stack.append(T1)

	t12 = "  CREATE INDEX test1_lower_col1_idx ON test1  ( lower ( col1) );"
	t13 = T(t12)
	T1 = T3(t13)
	stack.append(T1)

	t14 = " CREATE UNIQUE INDEX access_log_client_ip_ix ON access_log  ( client_ip );"
	t15 = T(t14)
	T1 = T3(t15)
	stack.append(T1)

	t16 = " CREATE UNIQUE INDEX mytable_cat_1 ON mytable  ( data );"
	t17 = T(t16)
	T1 = T3(t17)
	stack.append(T1)

	t18 = " CREATE UNIQUE INDEX mytable_cat_2 ON mytable  ( data );"
	t19 = T(t18)
	T1 = T3(t19)
	stack.append(T1)

	t20 = " CREATE UNIQUE INDEX mytable_cat_3 ON mytable  ( data );"
	t21 = T(t20)
	T1 = T3(t21)
	stack.append(T1)

	intermedio(T1[0])

contador = 0
@with_goto  # Decorador necesario.
def intermedio(outputs):
	global contador
	label .recorrer
	if contador < len(outputs):
		print(outputs[contador])
		contador = contador + 1
		goto .recorrer
	else:
		goto .end
	label .end

#PROCEDMIENTOS Y FUNCIONES


main()