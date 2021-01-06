from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
class Truncate(Instruccion):
    def __init__(self, id, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bd = arbol.getBaseDatos()
        if bd :
            operacion = truncate(str(bd), self.valor)
            if operacion == 0 :
                arbol.consola.append(f"Se ha eliminado los registros de la Tabla {self.valor} de la Base de Datos {str(bd)}")
            elif operacion == 1:
                error = Exception('XX000',"Semantico","Error Interno",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
            elif operacion == 2:
                error = Exception('XX000',"Semantico","La Base de datos no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
            else :
                error = Exception('XX000',"Semantico","La tabla no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())

    def analizar(self, tabla, arbol):
        print("analizar")

    def traducir(self, tabla, arbol):

        cadena = "\"truncate table "
        if( self.valor != None):
            cadena += self.valor
        
        cadena += ";\""
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
instruccion = DropDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''