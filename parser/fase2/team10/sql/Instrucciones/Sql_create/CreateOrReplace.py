from sql.Instrucciones.Excepcion import Excepcion
from sql.lexico import columas
from tkinter.constants import FALSE
from sql.Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from sql.Instrucciones.TablaSimbolos.Instruccion import *
from sql.Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from sql.storageManager.jsonMode import *

class CreateOrReplace(Instruccion):
    def __init__(self, base, tipo, existe, owner, mode, strGram ,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.base=base
        self.tipo=tipo
        self.existe = existe
        self.owner=owner
        self.mode=mode

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bandera = False
        arbol.lRepDin.append(self.strGram)
        #SE OBTIENE LA LISTA DE BD
        lb=showDatabases()
        #SE RECORRE LA BD PARA VERIFICAR QUE NO EXISTA
        if self.base in lb:
            dropDatabase(self.base)
            result=createDatabase(self.base)
            if result==0:
                #CUANDO LA TABLA SE CREA CORRECTAMENTE
                arbol.consola.append(f"La Base de Datos: {self.base} fue reemplazada.")
                arbol.eliminarBD(self.base)
                nueva = BaseDeDatos(str(self.base))
                arbol.setListaBd(nueva)
            elif result==2:
                error = Excepcion("100","Semantico","Error Interno.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
        else:
            result=createDatabase(self.base)
            if result==0:
                #CUANDO LA TABLA SE CREA CORRECTAMENTE
                arbol.consola.append(f"La Base de Datos: {self.base} se creo correctamente.")
                nueva = BaseDeDatos(str(self.base))
                arbol.setListaBd(nueva)
            elif result==2:
                error = Excepcion("100","Semantico","Error Interno.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())

        '''for bd in lb:
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
            error = Excepcion("100","Semantico","La Base de Datos ya Existe.",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
        elif self.existe=="NULL" and bandera==False:
            #AVISOS
            arbol.consola.append(f"Se Creo la base de datos: {self.base} correctamente.")
            createDatabase(str(self.base))
            nueva = BaseDeDatos(str(self.base))
            arbol.setListaBd(nueva)
        '''
    
    def analizar(self, tabla, arbol):
        print("hola")

    def traducir(self, tabla, arbol):
        cadena = "\""+"create or replace "
        
        if(self.existe!=None):
            if(self.existe !=  "NULL"):
                cadena += self.existe.lower() + " "

        if(self.base != None):
            cadena += self.base + " "

        if(self.owner!=None):
            cadena += "owner = "
            cadena += str(self.owner) + " "

        if(self.mode!=None):
            if(int(self.mode)!=1):
                cadena += "mode = " 
                cadena += str(self.mode)
        
        cadena += ";"+"\""
        
        arbol.addComen("Asignar cadena")
        temporal1 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = { cadena }")

        arbol.addComen("Entrar al ambito")
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal2} = P+2")
        temporal3 = tabla.getTemporal()
        arbol.addComen("parametro 1")
        arbol.addc3d(f"{temporal3} = { temporal2}+1")
        arbol.addComen("Asignacion de parametros")
        arbol.addc3d(f"Pila[{temporal3}] = {temporal1}")

        arbol.addComen("Llamada de funcion")
        arbol.addc3d(f"P = P+2")
        arbol.addc3d(f"funcionintermedia()")
        
        arbol.addComen("obtener resultado")
        temporalX = tabla.getTemporal()
        arbol.addc3d(f"{temporalX} = P+2")
        temporalR = tabla.getTemporal()
        arbol.addc3d(f"{temporalR} = Pila[{ temporalX }]")

        arbol.addComen("Salida de funcion")
        arbol.addc3d(f"P = P-2")

'''
instruccion = CreateOrReplace("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''