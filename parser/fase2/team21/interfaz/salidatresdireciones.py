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

	t0 = " CREATE DATABASE DBFase2 ;"
	t1 = T(t0)
	T1 = T3(t1)
	stack.append(T1)

	t2 = " USE DATABASE DBFase2 ;"
	t3 = T(t2)
	T1 = T3(t3)
	stack.append(T1)

	t4 = f" CREATE TABLE tbProducto (idproducto INTEGER  NOT NULL  PRIMARY KEY ,producto VARCHAR (150) NOT NULL ,fechacreacion DATE  NOT NULL ,estado INTEGER ) ;"
	t5 = T(t4)
	T1 = T3(t5)
	stack.append(T1)
	t6 = 1
	t7 = "\"Laptop Lenovo\""
	t8 = "now()"
	t9 = 1

	t10 = f" INSERT INTO tbProducto VALUES  ({t6},{t7},{t8},{t9});"
	t11 = T(t10)
	T1 = T3(t11)
	stack.append(T1)
	t12 = 2
	t13 = "\"Bateria para Laptop Lenovo T420\""
	t14 = "now()"
	t15 = 1

	t16 = f" INSERT INTO tbProducto VALUES  ({t12},{t13},{t14},{t15});"
	t17 = T(t16)
	T1 = T3(t17)
	stack.append(T1)
	t18 = 3
	t19 = "\"Teclado Inalambrico\""
	t20 = "now()"
	t21 = 1

	t22 = f" INSERT INTO tbProducto VALUES  ({t18},{t19},{t20},{t21});"
	t23 = T(t22)
	T1 = T3(t23)
	stack.append(T1)
	t24 = 4
	t25 = "\"Mouse Inalambrico\""
	t26 = "now()"
	t27 = 1

	t28 = f" INSERT INTO tbProducto VALUES  ({t24},{t25},{t26},{t27});"
	t29 = T(t28)
	T1 = T3(t29)
	stack.append(T1)
	t30 = 5
	t31 = "\"WIFI USB\""
	t32 = "now()"
	t33 = 1

	t34 = f" INSERT INTO tbProducto VALUES  ({t30},{t31},{t32},{t33});"
	t35 = T(t34)
	T1 = T3(t35)
	stack.append(T1)
	t36 = 6
	t37 = "\"Laptop HP\""
	t38 = "now()"
	t39 = 1

	t40 = f" INSERT INTO tbProducto VALUES  ({t36},{t37},{t38},{t39});"
	t41 = T(t40)
	T1 = T3(t41)
	stack.append(T1)
	t42 = 7
	t43 = "\"Teclado Flexible USB\""
	t44 = "now()"
	t45 = 2

	t46 = f" INSERT INTO tbProducto VALUES  ({t42},{t43},{t44},{t45});"
	t47 = T(t46)
	T1 = T3(t47)
	stack.append(T1)
	t48 = 8
	t49 = "\"Laptop Samsung\""
	t50 = "\"2021-01-02\""
	t51 = 1

	t52 = f" INSERT INTO tbProducto VALUES  ({t48},{t49},{t50},{t51});"
	t53 = T(t52)
	T1 = T3(t53)
	stack.append(T1)

	t54 ="SELECT   COUNT(*)    FROM   tbProducto   WHERE estado = 2 ;"
	t55 =T(t54)
	T1 = T3(t55)
	variable = T1[1]
	print("mivariable ,",variable)

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