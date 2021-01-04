from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Set(Instruccion):
    def __init__(self, id, tipo, id2, strGram,linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = id
        self.id2 = id2

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
    
    def analizar(self, tabla, arbol):
        pass
    
    def traducir(self, tabla, arbol):
        cadena = "\"set "
        if(self.valor):
            cadena += self.valor.traducir(tabla,arbol)
        cadena += " = "
        if(self.id2):
            cadena += self.id2.traducir(tabla,arbol)
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
instruccion = Use("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''