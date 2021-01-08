from Instrucciones.Excepcion import Excepcion
from tkinter.constants import FALSE
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.TablaSimbolos.Instruccion import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from storageManager.jsonMode import *
class CreateDatabase(Instruccion):
    def __init__(self, base, tipo, existe, owner, mode, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.base=base
        self.tipo=tipo
        self.existe = existe
        self.owner=owner
        self.mode=mode

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bandera = False
        #SE OBTIENE LA LISTA DE BD
        lb=showDatabases()
        #SE RECORRE LA BD PARA VERIFICAR QUE NO EXISTA
        for bd in lb:
            if bd== self.base:
                #SI SE ENCUENTRA LA BD SE TERMINA EL RECORRIDO
                bandera = True
                break
        if self.existe=="IF NOT EXISTS" and bandera==True:
            arbol.consola.append(f"La Base de Datos ya existe: {self.base}.")
        elif self.existe=="IF NOT EXISTS" and bandera==False:
            arbol.consola.append(f"Se Creo la base de datos: {self.base} correctamente.")
            createDatabase(str(self.base))
            nueva = BaseDeDatos(str(self.base))
            arbol.setListaBd(nueva)
        elif self.existe=="NULL" and bandera==True:
            error = Excepcion("42P04","Semantico",f"La Base de Datos {self.base} ya Existe.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        elif self.existe=="NULL" and bandera==False:
            #AVISOS
            arbol.consola.append(f"Se Creo la base de datos: {self.base} correctamente.")
            createDatabase(str(self.base))
            nueva = BaseDeDatos(str(self.base))
            arbol.setListaBd(nueva)

    def traducir(self,tabla,arbol,cadenaTraducida):
        temporal = arbol.generaTemporal()
        codigo = "\t" + temporal + " = " + "\"" + self.strSent + "\"\n"
        codigo += "\tFuncionesPara3D.ejecutarsentecia(" + temporal + ")\n\n"
        return codigo

'''
instruccion = CreateDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''