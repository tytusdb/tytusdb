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
	t4 = "\"INICIO CALIFICACION FASE 2\""
	t5 = myFuncion (t4)

	t6 = f" SELECT   {t5};"
	t7 = T(t6)
	stack.append(t7)

	t8 = f" CREATE TABLE tbProducto (idproducto INTEGER  NOT NULL  PRIMARY KEY ,producto VARCHAR (150) NOT NULL ,fechacreacion DATE  NOT NULL ,estado INTEGER ) ;"
	t9 = T(t8)
	T1 = T3(t9)
	stack.append(T1)

	t10 = " CREATE UNIQUE INDEX idx_producto ON tbProducto  ( idproducto );"
	t11 = T(t10)
	T1 = T3(t11)
	stack.append(T1)

	t12 = f" CREATE TABLE tbCalificacion (idcalifica INTEGER  NOT NULL  PRIMARY KEY ,item VARCHAR (100) NOT NULL ,punteo INTEGER  NOT NULL ) ;"
	t13 = T(t12)
	T1 = T3(t13)
	stack.append(T1)

	t14 = " CREATE UNIQUE INDEX idx_califica ON tbCalificacion  ( idcalifica );"
	t15 = T(t14)
	T1 = T3(t15)
	stack.append(T1)
	t16 = 1
	t17 = "\"Laptop Lenovo\""
	t18 = "now()"
	t19 = 1

	t20 = f" INSERT INTO tbProducto VALUES  ({t16},{t17},{t18},{t19});"
	t21 = T(t20)
	T1 = T3(t21)
	stack.append(T1)
	t22 = 2
	t23 = "\"Bateria para Laptop Lenovo T420\""
	t24 = "now()"
	t25 = 1

	t26 = f" INSERT INTO tbProducto VALUES  ({t22},{t23},{t24},{t25});"
	t27 = T(t26)
	T1 = T3(t27)
	stack.append(T1)
	t28 = 3
	t29 = "\"Teclado Inalambrico\""
	t30 = "now()"
	t31 = 1

	t32 = f" INSERT INTO tbProducto VALUES  ({t28},{t29},{t30},{t31});"
	t33 = T(t32)
	T1 = T3(t33)
	stack.append(T1)
	t34 = 4
	t35 = "\"Mouse Inalambrico\""
	t36 = "now()"
	t37 = 1

	t38 = f" INSERT INTO tbProducto VALUES  ({t34},{t35},{t36},{t37});"
	t39 = T(t38)
	T1 = T3(t39)
	stack.append(T1)
	t40 = 5
	t41 = "\"WIFI USB\""
	t42 = "now()"
	t43 = 1

	t44 = f" INSERT INTO tbProducto VALUES  ({t40},{t41},{t42},{t43});"
	t45 = T(t44)
	T1 = T3(t45)
	stack.append(T1)
	t46 = 6
	t47 = "\"Laptop HP\""
	t48 = "now()"
	t49 = 1

	t50 = f" INSERT INTO tbProducto VALUES  ({t46},{t47},{t48},{t49});"
	t51 = T(t50)
	T1 = T3(t51)
	stack.append(T1)
	t52 = 7
	t53 = "\"Teclado Flexible USB\""
	t54 = "now()"
	t55 = 1

	t56 = f" INSERT INTO tbProducto VALUES  ({t52},{t53},{t54},{t55});"
	t57 = T(t56)
	T1 = T3(t57)
	stack.append(T1)
	t58 = 8
	t59 = "\"Laptop Samsung\""
	t60 = "\"2021-01-02\""
	t61 = 1

	t62 = f" INSERT INTO tbProducto VALUES  ({t58},{t59},{t60},{t61});"
	t63 = T(t62)
	T1 = T3(t63)
	stack.append(T1)
	t76 = 1
	t77 = "\"Create Table and Insert\""
	t78 = "tbProducto"
	t79 = 8
	t80 = ValidaRegistros (t78,t79)

	t81 = f" INSERT INTO tbCalificacion VALUES  ({t76},{t77},{t80});"
	t82 = T(t81)
	T1 = T3(t82)
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

@with_goto  # Decorador necesario.
def myFuncion(texto):
	label .begin
	return texto

@with_goto  # Decorador necesario.
def ValidaRegistros(tabla, cantidad):
	label .declare
	resultado = ''
	retorna = ''
	label .begin
	t64 = tabla == 'tbProducto'
	if t64:
		 goto .L0
	else:
		goto .L1
	label .L0
	print("verdadera")

	t65 ="SELECT   COUNT(*)    FROM   tbProducto  ;"
	t66 =T(t65)
	T1 = T3(t66)
	resultado = T1[1] 
	t67 = cantidad == resultado
	if t67:
		 goto .L2
	else:
		goto .L3
	label .L2
	#parte verdadera
	print("verdadera")
	retorna = 1
	goto .L4
	label .L3
	#parte falsa
	print("falsa")
	retorna = 0
	label .L4
	#continuacion
	print("continuacion")
	label .L1
	t68 = tabla == 'tbProductoUp'
	if t68:
		 goto .L5
	else:
		goto .L6
	label .L5
	print("verdadera")

	t69 ="SELECT   COUNT(*)    FROM   tbProducto   WHERE estado = 2 ;"
	t70 =T(t69)
	T1 = T3(t70)
	resultado = T1[1] 
	t71 = cantidad == resultado
	if t71:
		 goto .L7
	else:
		goto .L8
	label .L7
	#parte verdadera
	print("verdadera")
	retorna = 1
	goto .L9
	label .L8
	#parte falsa
	print("falsa")
	retorna = 0
	label .L9
	#continuacion
	print("continuacion")
	label .L6
	t72 = tabla == 'tbbodega'
	if t72:
		 goto .L10
	else:
		goto .L11
	label .L10
	print("verdadera")

	t73 ="SELECT   COUNT(*)    FROM   tbbodega  ;"
	t74 =T(t73)
	T1 = T3(t74)
	resultado = T1[1] 
	t75 = cantidad == resultado
	if t75:
		 goto .L12
	else:
		goto .L13
	label .L12
	#parte verdadera
	print("verdadera")
	retorna = 1
	goto .L14
	label .L13
	#parte falsa
	print("falsa")
	retorna = 0
	label .L14
	#continuacion
	print("continuacion")
	label .L11
	return retorna


main()