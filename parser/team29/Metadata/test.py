import json
import File
import Struct

Struct.createDatabase("db1",1)
Struct.createDatabase("db2",1)
Struct.createDatabase("db3",2)
Struct.createDatabase("db4",2)

Struct.alterDatabase("db2","db2.1")


Struct.dropDatabase("db4")
Struct.createTable("db2.1","table1")
Struct.createTable("db3","Producto")
Struct.createTable("db3","Factura")
Struct.createTable("db3","Cliente")
Struct.createTable("db3","Detalle")
File.exportFile(Struct.Databases,"Bases1")

Struct.alterTable("db1","table3","table3.1")
Struct.dropTable("db1","table2")
File.exportFile(Struct.Databases,"Bases2")

Struct.createTable("db1","table6")

Struct.addCol("db3","Cliente","id","numerico","int",1,None,1,1,4)
Struct.addCol("db3","Cliente","nombre","caracter","varchar",0,None,0,0,30)
Struct.addCol("db3","Cliente","apellido","caracter","varchar",0,None,0,0,30)
Struct.addCol("db3","Cliente","direccion","caracter","varchar",0,None,0,0,30)

Struct.addCol("db3","Producto","id","numerico","int",1,None,1,1,4)
Struct.addCol("db3","Producto","nombre","caracter","varchar",0,None,0,0,30)
Struct.addCol("db3","Producto","descripcion","caracter","varchar",0,None,0,0,200)
Struct.addCol("db3","Producto","precio","numerico","money",0,None,0,0,8)


Struct.addCol("db3","Factura","id","numerico","int",1,None,1,1,4)
Struct.addCol("db3","Factura","fecha","Date/Time","date",0,None,0,0,4)
Struct.addCol("db3","Factura","cliente","numerico","int",0,"Cliente",1,0,4)
Struct.addCol("db3","Factura","total","numerico","money",0,None,0,0,8)

Struct.addCol("db3","Detalle","factura","numerico","int",0,"Factura",1,0,4)
Struct.addCol("db3","Detalle","producto","numerico","int",0,"Producto",1,0,4)
Struct.addCol("db3","Detalle","cantidad","numerico","int",0,None,1,0,4)



Struct.addCol("db1","Factura","numero","numerico","int",1,None,1,1,4)


File.exportFile(Struct.Databases,"Bases3")