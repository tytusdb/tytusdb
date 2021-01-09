from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Arbol import Arbol
from sql.Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from sql.Instrucciones.Tablas.Tablas import Tablas
from sql.Instrucciones.TablaSimbolos.Tipo import *
from sql.storageManager.jsonMode import *

a = Arbol([])
#create base 
nueva = BaseDeDatos("Shingeki")
a.setListaBd(nueva)
nueva2 = BaseDeDatos("Shokugeki")
a.setListaBd(nueva2)
#use
a.setBaseDatos("Shingeki")
#create tabla
tablaNueva = Tablas("temporada 1",None)
tablaNueva2 = Tablas("temporada 2",None)
tablaNueva3 = Tablas("temporada 3",None)

a.agregarTablaABd(tablaNueva)
a.agregarTablaABd(tablaNueva2)
a.agregarTablaABd(tablaNueva3)

tablaNueva.agregarColumna("capitulo1",Tipo(Tipo_Dato.INTEGER),None)
tablaNueva.agregarColumna("capitulo2",Tipo(Tipo_Dato.INTEGER),None)
tablaNueva.agregarColumna("capitulo3",Tipo(Tipo_Dato.INTEGER),None)
