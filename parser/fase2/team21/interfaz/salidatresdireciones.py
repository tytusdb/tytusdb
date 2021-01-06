# -*- coding: latin1 -*-
import  math
import random
import hashlib
import base64
import time
from goto import with_goto
from  tytus.parser.fase2.team21.Analisis_Ascendente.ascendente import T,T3,procesar_instrucciones
stack =[]
@with_goto  # Decorador necesario.
def main():
	t0 = 1
	t1 = "\"Create Table and Insert\""
	t2 = "tbProducto"
	t3 = 8
	t4 = ValidaRegistros (t2,t3)

	t5 = f" INSERT INTO tbCalificacion VALUES  ({t0},{t1},{t4});"
	t6 = T(t5)
	stack.append(t6)

	T1 = T3(stack)
	intermedio(T1)

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