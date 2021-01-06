# -*- coding: latin1 -*-
import  math
import random
import hashlib
import base64
import time
from goto import with_goto
from Compi2RepoAux.team21.Analisis_Ascendente.ascendente import T,T3,procesar_instrucciones
stack =[]
@with_goto  # Decorador necesario.
def main():
	t0 = 3
	t1 = "\" Valida Funciones\""
	t2 = CALCULOS ()

	t3 = f" INSERT INTO tbCalificacion VALUES  ({t0},{t1},{t2});"
	t4 = T(t3)
	stack.append(t4)

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

@with_goto  # Decorador necesario.
def CALCULOS():
	label .declare
	hora = ''
	SENO = ''
	VALOR = ''
	ABSOLUTO = ''
	label .begin


main()