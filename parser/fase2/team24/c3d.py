from InstruccionesDGA import tabla 
    from datetime import date
    from InstruccionesDGA import cont 
    from InstruccionesDGA import NombreDB
    from tablaDGA import *
    from sql import * 
    import mathtrig as mt
    #Funcion sql.execute
    
    pila = []
    for i in range(100):
        pila.append(i)
    
    def ejecutar(): 
	sql.execute("CREATE DATABASE DBFase2;")
	sql.execute("USE DATABASE DBFase2;")
	NombreDB = ts.nameDB
	sql.execute("CREATE TABLE tbProducto(idproducto integer NOT NULL PRIMARY KEY,producto varchar(150) NOT NULL,fechacreacion date NOT NULL,estado integer);")
	sql.execute("CREATE UNIQUE INDEX idx_producto ON tbProducto( idproducto);")
	sql.execute("CREATE TABLE tbCalificacion(idcalifica integer);")
	sql.execute("CREATE UNIQUE INDEX idx_califica ON tbCalificacion( idcalifica);")
	sql.execute("INSERT INTO tbProducto VALUES('1.0',''Laptop Lenovo'',''x'','1.0');")
	sql.execute('SELECT * FROM temp')
ejecutar() 