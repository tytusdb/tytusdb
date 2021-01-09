
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont 
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt
from reportTable import *
from reportError import *
from reportBNF import *
    
    
pila = []
for i in range(100):
    pila.append(i)
    
def ejecutar():
    global cont
    global ts
    NombreDB = ts.nameDB

    sql.execute("CREATE DATABASE DBFase2;")
    sql.execute("USE DATABASE DBFase2;")
    NombreDB = ts.nameDB
    sql.execute("CREATE TABLE tbProducto(idproducto integer NOT NULL PRIMARY KEY,producto varchar(150) NOT NULL,fechacreacion date NOT NULL,estado integer);")
    sql.execute("CREATE UNIQUE INDEX idx_producto ON tbProducto( idproducto);")
    sql.execute("CREATE TABLE tbCalificacion(idcalifica integer NOT NULL PRIMARY KEY,item varchar(100) NOT NULL,punteo integer NOT NULL);")
    sql.execute("CREATE UNIQUE INDEX idx_califica ON tbCalificacion( idcalifica);")
    sql.execute("INSERT INTO tbProducto VALUES('1.0','Laptop Lenovo','2021-01-08 00:00:00','1.0');")
    sql.execute("INSERT INTO tbProducto VALUES('2.0','Bateria para Laptop Lenovo T420','2021-01-08 00:00:00','1.0');")
    sql.execute("INSERT INTO tbProducto VALUES('3.0','Teclado Inalambrico','2021-01-08 00:00:00','1.0');")
    sql.execute("INSERT INTO tbProducto VALUES('4.0','Mouse Inalambrico','2021-01-08 00:00:00','1.0');")
    sql.execute("INSERT INTO tbProducto VALUES('5.0','WIFI USB','2021-01-08 00:00:00','1.0');")
    sql.execute("INSERT INTO tbProducto VALUES('6.0','Laptop HP','2021-01-08 00:00:00','1.0');")
    sql.execute("INSERT INTO tbProducto VALUES('7.0','Teclado Flexible USB','2021-01-08 00:00:00','1.0');")
    sql.execute("INSERT INTO tbProducto VALUES('8.0','Laptop Samsung','2021-01-02','1.0');")
    n_db = ts.buscarIDTB(NombreDB)
    NuevoSimbolo = TAS.Simbolo(cont,'myFuncion',TAS.TIPO.FUNCTION,n_db)
    ts.agregar(NuevoSimbolo)
    cont+=1

    sql.execute('SELECT * FROM temp')
    t1 = 2
    pila[0] = t1
    myFuncion()
    t2 = pila[10]
    
    t3 = 2
    pila[0] = t3
    myFuncion()
    t4 = pila[10]
    
    sql.execute("UPDATE tbProducto SET estado = "+str(t2)+" WHERE  estado ="+str(t4)+";")

    graphTable(ts)
    report_errors()
    report_BNF()
def myFuncion():
    texto = pila[0]
    t0 = texto
    
    pila[10] = t0
    
ejecutar()